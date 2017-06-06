


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BfdMgmtSessionDiagEnum' : _MetaInfoEnum('BfdMgmtSessionDiagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-session-diag-none':'bfd_mgmt_session_diag_none',
            'bfd-mgmt-session-diag-control-detect-expired':'bfd_mgmt_session_diag_control_detect_expired',
            'bfd-mgmt-session-diag-echo-function-failed':'bfd_mgmt_session_diag_echo_function_failed',
            'bfd-mgmt-session-diag-nb-or-signaled-down':'bfd_mgmt_session_diag_nb_or_signaled_down',
            'bfd-mgmt-session-diag-fwding-plane-reset':'bfd_mgmt_session_diag_fwding_plane_reset',
            'bfd-mgmt-session-diag-path-down':'bfd_mgmt_session_diag_path_down',
            'bfd-mgmt-session-diag-conc-path-down':'bfd_mgmt_session_diag_conc_path_down',
            'bfd-mgmt-session-diag-admin-down':'bfd_mgmt_session_diag_admin_down',
            'bfd-mgmt-session-diag-rev-conc-path-down':'bfd_mgmt_session_diag_rev_conc_path_down',
            'bfd-mgmt-session-diag-num':'bfd_mgmt_session_diag_num',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'MplsLibCEnum' : _MetaInfoEnum('MplsLibCEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'mpls-lib-c-type-null':'mpls_lib_c_type_null',
            'mpls-lib-c-type-ipv4':'mpls_lib_c_type_ipv4',
            'mpls-lib-c-type-ipv4-p2p-tunnel':'mpls_lib_c_type_ipv4_p2p_tunnel',
            'mpls-lib-c-type-ipv6-p2p-tunnel':'mpls_lib_c_type_ipv6_p2p_tunnel',
            'mpls-lib-c-type-ipv4-uni':'mpls_lib_c_type_ipv4_uni',
            'mpls-lib-c-type-ipv4-p2mp-tunnel':'mpls_lib_c_type_ipv4_p2mp_tunnel',
            'mpls-lib-c-type-ipv6-p2mp-tunnel':'mpls_lib_c_type_ipv6_p2mp_tunnel',
            'mpls-lib-c-type-ipv4-tp-tunnel':'mpls_lib_c_type_ipv4_tp_tunnel',
            'mpls-lib-c-type-ipv6-tp-tunnel':'mpls_lib_c_type_ipv6_tp_tunnel',
            'mpls-lib-c-type-p2p-binding-label':'mpls_lib_c_type_p2p_binding_label',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMgmtSessionStateEnum' : _MetaInfoEnum('BfdMgmtSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-session-state-admin-down':'bfd_mgmt_session_state_admin_down',
            'bfd-mgmt-session-state-down':'bfd_mgmt_session_state_down',
            'bfd-mgmt-session-state-init':'bfd_mgmt_session_state_init',
            'bfd-mgmt-session-state-up':'bfd_mgmt_session_state_up',
            'bfd-mgmt-session-state-failing':'bfd_mgmt_session_state_failing',
            'bfd-mgmt-session-state-unknown':'bfd_mgmt_session_state_unknown',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMpDownloadStateEnum' : _MetaInfoEnum('BfdMpDownloadStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mp-download-none':'bfd_mp_download_none',
            'bfd-mp-download-no-lc':'bfd_mp_download_no_lc',
            'bfd-mp-download-downloaded':'bfd_mp_download_downloaded',
            'bfd-mp-download-ack':'bfd_mp_download_ack',
            'bfd-mp-download-nack':'bfd_mp_download_nack',
            'bfd-mp-download-delete':'bfd_mp_download_delete',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdAfIdEnum' : _MetaInfoEnum('BfdAfIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-af-id-none':'bfd_af_id_none',
            'bfd-af-id-ipv4':'bfd_af_id_ipv4',
            'bfd-af-id-ipv6':'bfd_af_id_ipv6',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMgmtPktDisplayEnum' : _MetaInfoEnum('BfdMgmtPktDisplayEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-pkt-display-type-none':'bfd_mgmt_pkt_display_type_none',
            'bfd-mgmt-pkt-display-type-bob-mbr':'bfd_mgmt_pkt_display_type_bob_mbr',
            'bfd-mgmt-pkt-display-type-max':'bfd_mgmt_pkt_display_type_max',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdApiFecEnum' : _MetaInfoEnum('BfdApiFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-api-fec-type-none':'bfd_api_fec_type_none',
            'bfd-api-fec-type-p2p-te':'bfd_api_fec_type_p2p_te',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdSessionEnum' : _MetaInfoEnum('BfdSessionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper',
        {
            'undefined':'undefined',
            'bundle-member':'bundle_member',
            'bundle-interface':'bundle_interface',
            'state-inheriting':'state_inheriting',
            'bundle-vlan':'bundle_vlan',
            'mpls-tp':'mpls_tp',
            'gre':'gre',
            'pseudowire-headend':'pseudowire_headend',
            'ip-single-hop':'ip_single_hop',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief',
            False, 
            [
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('label-session-brief', REFERENCE_LIST, 'LabelSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief', 
                [], [], 
                '''                Brief information for a single Label BFD
                session
                ''',
                'label_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-packet-counter', REFERENCE_LIST, 'Ipv6SingleHopPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter', 
                [], [], 
                '''                Interface IPv6 single hop Packet counters
                ''',
                'ipv6_single_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-packet-counters', REFERENCE_CLASS, 'Ipv6SingleHopPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters', 
                [], [], 
                '''                Table of IPv6 single hop Packet counters
                ''',
                'ipv6_single_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters.PacketCounters.PacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters.PacketCounters.PacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters.PacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters.PacketCounters',
            False, 
            [
            _MetaInfoClassMember('packet-counter', REFERENCE_LIST, 'PacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters.PacketCounters.PacketCounter', 
                [], [], 
                '''                Interface Packet counters
                ''',
                'packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters',
            False, 
            [
            _MetaInfoClassMember('packet-counters', REFERENCE_CLASS, 'PacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters.PacketCounters', 
                [], [], 
                '''                Table of Packet counters
                ''',
                'packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail.Brief' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail.Brief',
            False, 
            [
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where client resides
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions created by this client
                ''',
                'session_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail.Flags' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail.Flags',
            False, 
            [
            _MetaInfoClassMember('is-recreate-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Client is in Recreate State
                ''',
                'is_recreate_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('is-zombie-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Client is in Zombie State
                ''',
                'is_zombie_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Name
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail.Brief', 
                [], [], 
                '''                Brief client information
                ''',
                'brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('flags', REFERENCE_CLASS, 'Flags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail.Flags', 
                [], [], 
                '''                The BFD Client Flags
                ''',
                'flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('recreate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Recreate Time in Seconds
                ''',
                'recreate_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails',
            False, 
            [
            _MetaInfoClassMember('client-detail', REFERENCE_LIST, 'ClientDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail', 
                [], [], 
                '''                Detailed information of client
                ''',
                'client_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelMultiPaths.LabelMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelMultiPaths.LabelMultiPath',
            False, 
            [
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelMultiPaths',
            False, 
            [
            _MetaInfoClassMember('label-multi-path', REFERENCE_LIST, 'LabelMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelMultiPaths.LabelMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'label_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-session-detail', REFERENCE_LIST, 'Ipv4MultiHopSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 multihop
                BFD session
                ''',
                'ipv4_multi_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-session-detail', REFERENCE_LIST, 'Ipv4SingleHopSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4
                singlehop BFD session
                ''',
                'ipv4_single_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-session-brief', REFERENCE_LIST, 'Ipv4MultiHopSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 multihop
                BFD session
                ''',
                'ipv4_multi_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.GenericSummaries.GenericSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.GenericSummaries.GenericSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('max-session-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Session Number
                ''',
                'max_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-session-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MP Session Number
                ''',
                'mp_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pps-allocated-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocated PPS value
                ''',
                'pps_allocated_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pps-max-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max PPS value
                ''',
                'pps_max_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ppsmp-allocated-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocated MP PPS value
                ''',
                'ppsmp_allocated_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ppsmp-max-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max MP PPS value
                ''',
                'ppsmp_max_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-session-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Session Number
                ''',
                'total_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'generic-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.GenericSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.GenericSummaries',
            False, 
            [
            _MetaInfoClassMember('generic-summary', REFERENCE_LIST, 'GenericSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.GenericSummaries.GenericSummary', 
                [], [], 
                '''                Generic summary information for bfd location
                table
                ''',
                'generic_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'generic-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-multi-path', REFERENCE_LIST, 'Ipv6SingleHopMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath', 
                [], [], 
                '''                IPv6 single hop multipath table
                ''',
                'ipv6_single_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-node-location-summary', REFERENCE_LIST, 'Ipv4SingleHopNodeLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 singlehop
                sessions for location
                ''',
                'ipv4_single_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-brief', REFERENCE_LIST, 'Ipv4BfDoMplsteHeadSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 BFD over
                MPLS-TE Head session
                ''',
                'ipv4bf_do_mplste_head_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-detail', REFERENCE_LIST, 'Ipv4BfDoMplsteTailSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 BFD over
                MPLS-TE Tail session
                ''',
                'ipv4bf_do_mplste_tail_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-node-location-summary', REFERENCE_LIST, 'Ipv4MultiHopNodeLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 multihop
                sessions for location
                ''',
                'ipv4_multi_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-brief', REFERENCE_LIST, 'Ipv4BfDoMplsteTailSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 BFD over
                MPLS-TE session
                ''',
                'ipv4bf_do_mplste_tail_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-node-location-summary', REFERENCE_LIST, 'Ipv6MultiHopNodeLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 multihop
                sessions for location
                ''',
                'ipv6_multi_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-packet-counter', REFERENCE_LIST, 'Ipv4SingleHopPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter', 
                [], [], 
                '''                Interface IPv4 single hop Packet counters
                ''',
                'ipv4_single_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-packet-counters', REFERENCE_CLASS, 'Ipv4SingleHopPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters', 
                [], [], 
                '''                Table of IPv4 single hop Packet counters
                ''',
                'ipv4_single_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-session-detail', REFERENCE_LIST, 'Ipv6MultiHopSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv6 multihop
                BFD session
                ''',
                'ipv6_multi_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-multi-path', REFERENCE_LIST, 'Ipv6MultiHopMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath', 
                [], [], 
                '''                IPv6 multihop multipath table
                ''',
                'ipv6_multi_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters.Ipv4BfDoMplsteHeadPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters.Ipv4BfDoMplsteHeadPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-packet-counter', REFERENCE_LIST, 'Ipv4BfDoMplsteHeadPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters.Ipv4BfDoMplsteHeadPacketCounter', 
                [], [], 
                '''                Interface  IPv4 BFD over MPLS-TE Packet
                counters
                ''',
                'ipv4bf_do_mplste_head_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-packet-counters', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters', 
                [], [], 
                '''                Table of IPv4 BFD over MPLS-TE Packet counters
                ''',
                'ipv4bf_do_mplste_head_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs.SessionMib.DestAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs.SessionMib.DestAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dest-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs.SessionMib' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs.SessionMib',
            False, 
            [
            _MetaInfoClassMember('discriminator', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sesison Discr 
                ''',
                'discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('desired-min-tx-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired Min TX Interval
                ''',
                'desired_min_tx_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dest-address', REFERENCE_CLASS, 'DestAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs.SessionMib.DestAddress', 
                [], [], 
                '''                Session Destination address
                ''',
                'dest_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('int-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Interface Handle
                ''',
                'int_handle',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-diag', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Last Session Down Diag
                ''',
                'last_down_diag',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Session Down Time (nanoseconds)
                ''',
                'last_down_time_nsec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-time-sec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Session Down Time (seconds)
                ''',
                'last_down_time_sec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-time-cached', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Time Session Info Queried
                ''',
                'last_time_cached',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-up-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Session Up Time (nanoseconds)
                ''',
                'last_up_time_nsec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-up-time-sec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Session Up Time (seconds)
                ''',
                'last_up_time_sec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions' Local Discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pkt-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet In Counter
                ''',
                'pkt_in',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pkt-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet Out Counter
                ''',
                'pkt_out',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions' Remote Discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-min-rx-echo-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required Min RX Echo Interval
                ''',
                'required_min_rx_echo_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-min-rx-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required Min RX Interval
                ''',
                'required_min_rx_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessionversion', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session BFD Version
                ''',
                'sessionversion',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('trap-bitmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trap Generator Bitmap
                ''',
                'trap_bitmap',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up Count
                ''',
                'up_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs',
            False, 
            [
            _MetaInfoClassMember('session-mib', REFERENCE_LIST, 'SessionMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs.SessionMib', 
                [], [], 
                '''                Brief information for BFD session MIB
                ''',
                'session_mib',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-mibs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes.LabelSummaryNode' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes.LabelSummaryNode',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes',
            False, 
            [
            _MetaInfoClassMember('label-summary-node', REFERENCE_LIST, 'LabelSummaryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes.LabelSummaryNode', 
                [], [], 
                '''                Summary of Label BFD 
                ''',
                'label_summary_node',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-session-brief', REFERENCE_LIST, 'Ipv6MultiHopSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv6 multihop
                BFD session
                ''',
                'ipv6_multi_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs',
            False, 
            [
            _MetaInfoClassMember('session-brief', REFERENCE_LIST, 'SessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 singlehop
                BFD session
                ''',
                'session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-node-location-summary', REFERENCE_LIST, 'Ipv6SingleHopNodeLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 singlehop
                sessions for location
                ''',
                'ipv6_single_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Summary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Summary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Summary' : {
        'meta_info' : _MetaInfoClass('Bfd.Summary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Summary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-tail-node-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteTailNodeSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteTailNodeSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4bfd-mplste-tail-node-summary', REFERENCE_LIST, 'Ipv4BfdMplsteTailNodeSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary', 
                [], [], 
                '''                Summary of IPv4 BFD over MPLS-TE tail
                ''',
                'ipv4bfd_mplste_tail_node_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-tail-node-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location Name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-location-summary', REFERENCE_LIST, 'Ipv4SingleHopLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 singlehop
                sessions for location
                ''',
                'ipv4_single_hop_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-head-summary-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfdMplsteHeadSummaryNodes' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfdMplsteHeadSummaryNodes',
            False, 
            [
            _MetaInfoClassMember('ipv4bfd-mplste-head-summary-node', REFERENCE_LIST, 'Ipv4BfdMplsteHeadSummaryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode', 
                [], [], 
                '''                Summary of IPv4 BFD over MPLS-TE head
                ''',
                'ipv4bfd_mplste_head_summary_node',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-head-summary-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails',
            False, 
            [
            _MetaInfoClassMember('label-session-detail', REFERENCE_LIST, 'LabelSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail', 
                [], [], 
                '''                Detailed information for a single BFD session
                ''',
                'label_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-session-detail', REFERENCE_LIST, 'Ipv6SingleHopSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv6
                singlehop BFD session
                ''',
                'ipv6_single_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-packet-counter', REFERENCE_LIST, 'Ipv4MultiHopPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter', 
                [], [], 
                '''                IPv4 multiple hop Packet counters
                ''',
                'ipv4_multi_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-packet-counters', REFERENCE_CLASS, 'Ipv4MultiHopPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters', 
                [], [], 
                '''                Table of IPv4 multiple hop Packet counters
                ''',
                'ipv4_multi_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails',
            False, 
            [
            _MetaInfoClassMember('session-detail', REFERENCE_LIST, 'SessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4
                singlehop BFD session
                ''',
                'session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-multi-path', REFERENCE_LIST, 'Ipv4SingleHopMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath', 
                [], [], 
                '''                IPv4 single hop multipath table
                ''',
                'ipv4_single_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-session-brief', REFERENCE_LIST, 'Ipv4SingleHopSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 singlehop
                BFD session
                ''',
                'ipv4_single_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters.Ipv6MultiHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters.Ipv6MultiHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-packet-counter', REFERENCE_LIST, 'Ipv6MultiHopPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters.Ipv6MultiHopPacketCounter', 
                [], [], 
                '''                IPv4 multiple hop Packet counters
                ''',
                'ipv6_multi_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-packet-counters', REFERENCE_CLASS, 'Ipv6MultiHopPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters', 
                [], [], 
                '''                Table of IPv6 multiple hop Packet counters
                ''',
                'ipv6_multi_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location Name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-location-summary', REFERENCE_LIST, 'Ipv6SingleHopLocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 singlehop
                sessions for location
                ''',
                'ipv6_single_hop_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters.LabelPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters.LabelPacketCounters',
            False, 
            [
            _MetaInfoClassMember('label-packet-counter', REFERENCE_LIST, 'LabelPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter', 
                [], [], 
                '''                Interface Label Packet counters
                ''',
                'label_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters',
            False, 
            [
            _MetaInfoClassMember('label-packet-counters', REFERENCE_CLASS, 'LabelPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters.LabelPacketCounters', 
                [], [], 
                '''                Table of Label Packet counters
                ''',
                'label_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiagEnum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadStateEnum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-detail', REFERENCE_LIST, 'Ipv4BfDoMplsteHeadSessionDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 BFD over
                MPLS-TE head session
                ''',
                'ipv4bf_do_mplste_head_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs.RelationBrief.LinkInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs.RelationBrief.LinkInformation',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs.RelationBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs.RelationBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('link-information', REFERENCE_LIST, 'LinkInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs.RelationBrief.LinkInformation', 
                [], [], 
                '''                Brief Member Link Information
                ''',
                'link_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs',
            False, 
            [
            _MetaInfoClassMember('relation-brief', REFERENCE_LIST, 'RelationBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs.RelationBrief', 
                [], [], 
                '''                Brief information for relation of a single BFD
                session
                ''',
                'relation_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientBriefs.ClientBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientBriefs.ClientBrief',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where client resides
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions created by this client
                ''',
                'session_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientBriefs',
            False, 
            [
            _MetaInfoClassMember('client-brief', REFERENCE_LIST, 'ClientBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientBriefs.ClientBrief', 
                [], [], 
                '''                Brief information of client
                ''',
                'client_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadMultiPaths.Ipv4BfDoMplsteHeadMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadMultiPaths.Ipv4BfDoMplsteHeadMultiPath',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-multi-path', REFERENCE_LIST, 'Ipv4BfDoMplsteHeadMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadMultiPaths.Ipv4BfDoMplsteHeadMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'ipv4bf_do_mplste_head_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.LinkInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.LinkInformation',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibCEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibCEnum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFecEnum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2LFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SBFD enable flag
                ''',
                'sbfd_enabled',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sbfd-target-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SBFD target type
                ''',
                'sbfd_target_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.TargetAddress', 
                [], [], 
                '''                sbfd target address
                ''',
                'target_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('link-information', REFERENCE_LIST, 'LinkInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.LinkInformation', 
                [], [], 
                '''                Detail Member Link Information
                ''',
                'link_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails',
            False, 
            [
            _MetaInfoClassMember('relation-detail', REFERENCE_LIST, 'RelationDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail', 
                [], [], 
                '''                Detail information for relation of a single BFD
                session
                ''',
                'relation_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters.Ipv4BfDoMplsteTailPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters.Ipv4BfDoMplsteTailPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplayEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplayEnum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-packet-counter', REFERENCE_LIST, 'Ipv4BfDoMplsteTailPacketCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters.Ipv4BfDoMplsteTailPacketCounter', 
                [], [], 
                '''                Interface  IPv4 BFD over MPLS-TE Packet
                counters
                ''',
                'ipv4bf_do_mplste_tail_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-packet-counters', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailPacketCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters', 
                [], [], 
                '''                Table of IPv4 BFD over MPLS-TE Packet counters
                ''',
                'ipv4bf_do_mplste_tail_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdSessionEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-session-brief', REFERENCE_LIST, 'Ipv6SingleHopSessionBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv6 singlehop
                BFD session
                ''',
                'ipv6_single_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailMultiPaths.Ipv4BfDoMplsteTailMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailMultiPaths.Ipv4BfDoMplsteTailMultiPath',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteTailMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteTailMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-multi-path', REFERENCE_LIST, 'Ipv4BfDoMplsteTailMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailMultiPaths.Ipv4BfDoMplsteTailMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'ipv4bf_do_mplste_tail_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-multi-path', REFERENCE_LIST, 'Ipv4MultiHopMultiPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath', 
                [], [], 
                '''                IPv4 multi hop multipath table
                ''',
                'ipv4_multi_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4BfDoMplsteHeadSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4BfDoMplsteHeadSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd' : {
        'meta_info' : _MetaInfoClass('Bfd',
            False, 
            [
            _MetaInfoClassMember('client-briefs', REFERENCE_CLASS, 'ClientBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientBriefs', 
                [], [], 
                '''                Table of Brief information about BFD clients
                ''',
                'client_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('client-details', REFERENCE_CLASS, 'ClientDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails', 
                [], [], 
                '''                Table of detailed information about BFD clients
                ''',
                'client_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters', 
                [], [], 
                '''                Counters
                ''',
                'counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('generic-summaries', REFERENCE_CLASS, 'GenericSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.GenericSummaries', 
                [], [], 
                '''                Generic summary information about BFD location
                ''',
                'generic_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-counters', REFERENCE_CLASS, 'Ipv4MultiHopCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters', 
                [], [], 
                '''                IPv4 multiple hop Counters
                ''',
                'ipv4_multi_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-multi-paths', REFERENCE_CLASS, 'Ipv4MultiHopMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopMultiPaths', 
                [], [], 
                '''                IPv4 multi-hop multipath
                ''',
                'ipv4_multi_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv4MultiHopNodeLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv4
                multihop sessions per location
                ''',
                'ipv4_multi_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-session-briefs', REFERENCE_CLASS, 'Ipv4MultiHopSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4
                multihop BFD sessions in the System
                ''',
                'ipv4_multi_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-session-details', REFERENCE_CLASS, 'Ipv4MultiHopSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4
                multihop BFD sessions in the System 
                ''',
                'ipv4_multi_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-summary', REFERENCE_CLASS, 'Ipv4MultiHopSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv4 multihop
                sessions
                ''',
                'ipv4_multi_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-counters', REFERENCE_CLASS, 'Ipv4SingleHopCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters', 
                [], [], 
                '''                IPv4 single hop Counters
                ''',
                'ipv4_single_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-location-summaries', REFERENCE_CLASS, 'Ipv4SingleHopLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries', 
                [], [], 
                '''                Table of summary information about IPv4
                singlehop BFD sessions for location
                ''',
                'ipv4_single_hop_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-multi-paths', REFERENCE_CLASS, 'Ipv4SingleHopMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopMultiPaths', 
                [], [], 
                '''                IPv4 single hop multipath
                ''',
                'ipv4_single_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv4SingleHopNodeLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv4
                singlehop sessions per location
                ''',
                'ipv4_single_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-session-briefs', REFERENCE_CLASS, 'Ipv4SingleHopSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4
                singlehop BFD sessions in the System
                ''',
                'ipv4_single_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-session-details', REFERENCE_CLASS, 'Ipv4SingleHopSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4
                singlehop BFD sessions in the System 
                ''',
                'ipv4_single_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-summary', REFERENCE_CLASS, 'Ipv4SingleHopSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv4 singlehop
                sessions
                ''',
                'ipv4_single_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-counters', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadCounters', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Counters
                ''',
                'ipv4bf_do_mplste_head_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-multi-paths', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadMultiPaths', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Head multipath
                ''',
                'ipv4bf_do_mplste_head_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-briefs', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4 BFD
                over MPLS-TE Head sessions in the System
                ''',
                'ipv4bf_do_mplste_head_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-details', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4 BFD
                over MPLS-TE Head sessions in the System
                ''',
                'ipv4bf_do_mplste_head_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-summary', REFERENCE_CLASS, 'Ipv4BfDoMplsteHeadSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteHeadSummary', 
                [], [], 
                '''                Summary information of IPv4 BFD over MPLS-TE
                Head
                ''',
                'ipv4bf_do_mplste_head_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-counters', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailCounters', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Counters
                ''',
                'ipv4bf_do_mplste_tail_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-multi-paths', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailMultiPaths', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Tail multipath
                ''',
                'ipv4bf_do_mplste_tail_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-briefs', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4 BFD
                over MPLS-TE Tail sessions in the System
                ''',
                'ipv4bf_do_mplste_tail_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-details', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4 BFD
                over MPLS-TE Tail sessions in the System
                ''',
                'ipv4bf_do_mplste_tail_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-summary', REFERENCE_CLASS, 'Ipv4BfDoMplsteTailSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfDoMplsteTailSummary', 
                [], [], 
                '''                Summary information of IPv4 BFD over MPLS-TE
                Tail
                ''',
                'ipv4bf_do_mplste_tail_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bfd-mplste-head-summary-nodes', REFERENCE_CLASS, 'Ipv4BfdMplsteHeadSummaryNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteHeadSummaryNodes', 
                [], [], 
                '''                Table of summary about IPv4 TE head BFD sessions
                for location
                ''',
                'ipv4bfd_mplste_head_summary_nodes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bfd-mplste-tail-node-summaries', REFERENCE_CLASS, 'Ipv4BfdMplsteTailNodeSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4BfdMplsteTailNodeSummaries', 
                [], [], 
                '''                Table of summary about IPv4 TE tail BFD sessions
                for location
                ''',
                'ipv4bfd_mplste_tail_node_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-counters', REFERENCE_CLASS, 'Ipv6MultiHopCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopCounters', 
                [], [], 
                '''                IPv6 multiple hop Counters
                ''',
                'ipv6_multi_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-multi-paths', REFERENCE_CLASS, 'Ipv6MultiHopMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopMultiPaths', 
                [], [], 
                '''                IPv6 multi hop multipath
                ''',
                'ipv6_multi_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv6MultiHopNodeLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                multihop sessions per location
                ''',
                'ipv6_multi_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-session-briefs', REFERENCE_CLASS, 'Ipv6MultiHopSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv6
                multihop BFD sessions in the System
                ''',
                'ipv6_multi_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-session-details', REFERENCE_CLASS, 'Ipv6MultiHopSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv6
                multihop BFD sessions in the System 
                ''',
                'ipv6_multi_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-summary', REFERENCE_CLASS, 'Ipv6MultiHopSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv6 multihop
                sessions
                ''',
                'ipv6_multi_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-counters', REFERENCE_CLASS, 'Ipv6SingleHopCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters', 
                [], [], 
                '''                IPv6 single hop Counters
                ''',
                'ipv6_single_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-location-summaries', REFERENCE_CLASS, 'Ipv6SingleHopLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                singlehop sessions per location
                ''',
                'ipv6_single_hop_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-multi-paths', REFERENCE_CLASS, 'Ipv6SingleHopMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopMultiPaths', 
                [], [], 
                '''                IPv6 single hop multipath
                ''',
                'ipv6_single_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv6SingleHopNodeLocationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                singlehop sessions per location
                ''',
                'ipv6_single_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-session-briefs', REFERENCE_CLASS, 'Ipv6SingleHopSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv6
                singlehop BFD sessions in the System
                ''',
                'ipv6_single_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-session-details', REFERENCE_CLASS, 'Ipv6SingleHopSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv6
                singlehop BFD sessions in the System 
                ''',
                'ipv6_single_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-summary', REFERENCE_CLASS, 'Ipv6SingleHopSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv6 singlehop
                sessions
                ''',
                'ipv6_single_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-counters', REFERENCE_CLASS, 'LabelCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters', 
                [], [], 
                '''                Label Counters
                ''',
                'label_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-multi-paths', REFERENCE_CLASS, 'LabelMultiPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelMultiPaths', 
                [], [], 
                '''                Label multipath
                ''',
                'label_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-session-briefs', REFERENCE_CLASS, 'LabelSessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs', 
                [], [], 
                '''                Table of brief information about all Label BFD
                sessions in the System
                ''',
                'label_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-session-details', REFERENCE_CLASS, 'LabelSessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails', 
                [], [], 
                '''                Table of detailed information about all Label
                BFD sessions in the System 
                ''',
                'label_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-summary', REFERENCE_CLASS, 'LabelSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummary', 
                [], [], 
                '''                Summary information of Label BFD
                ''',
                'label_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-summary-nodes', REFERENCE_CLASS, 'LabelSummaryNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes', 
                [], [], 
                '''                Table of summary about Label BFD sessions for
                location
                ''',
                'label_summary_nodes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('relation-briefs', REFERENCE_CLASS, 'RelationBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs', 
                [], [], 
                '''                Table of brief information about all BFD
                relations in the System
                ''',
                'relation_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('relation-details', REFERENCE_CLASS, 'RelationDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails', 
                [], [], 
                '''                Table of detail information about all BFD
                relations in the System
                ''',
                'relation_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-briefs', REFERENCE_CLASS, 'SessionBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs', 
                [], [], 
                '''                Table of brief information about singlehop IPv4
                BFD sessions in the System
                ''',
                'session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-details', REFERENCE_CLASS, 'SessionDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails', 
                [], [], 
                '''                Table of detailed information about IPv4
                singlehop BFD sessions in the System 
                ''',
                'session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-mibs', REFERENCE_CLASS, 'SessionMibs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs', 
                [], [], 
                '''                BFD session MIB database
                ''',
                'session_mibs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Summary', 
                [], [], 
                '''                Summary information of BFD IPv4 singlehop
                sessions
                ''',
                'summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
}
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopCounters']['meta_info']
_meta_table['Bfd.Counters.PacketCounters.PacketCounter']['meta_info'].parent =_meta_table['Bfd.Counters.PacketCounters']['meta_info']
_meta_table['Bfd.Counters.PacketCounters']['meta_info'].parent =_meta_table['Bfd.Counters']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail.Brief']['meta_info'].parent =_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail.Flags']['meta_info'].parent =_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info'].parent =_meta_table['Bfd.ClientDetails']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSummary']['meta_info']
_meta_table['Bfd.LabelMultiPaths.LabelMultiPath']['meta_info'].parent =_meta_table['Bfd.LabelMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs']['meta_info']
_meta_table['Bfd.GenericSummaries.GenericSummary']['meta_info'].parent =_meta_table['Bfd.GenericSummaries']['meta_info']
_meta_table['Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.LabelSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.LabelSummary']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs.Ipv4BfDoMplsteHeadSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs.Ipv4BfDoMplsteTailSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopCounters']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters.Ipv4BfDoMplsteHeadPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadCounters.Ipv4BfDoMplsteHeadPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadCounters']['meta_info']
_meta_table['Bfd.SessionMibs.SessionMib.DestAddress']['meta_info'].parent =_meta_table['Bfd.SessionMibs.SessionMib']['meta_info']
_meta_table['Bfd.SessionMibs.SessionMib']['meta_info'].parent =_meta_table['Bfd.SessionMibs']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSummary']['meta_info']
_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState']['meta_info'].parent =_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode']['meta_info']
_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode']['meta_info'].parent =_meta_table['Bfd.LabelSummaryNodes']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief']['meta_info'].parent =_meta_table['Bfd.SessionBriefs']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Summary.SessionState']['meta_info'].parent =_meta_table['Bfd.Summary']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteTailNodeSummaries.Ipv4BfdMplsteTailNodeSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4BfdMplsteTailNodeSummaries']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteHeadSummaryNodes.Ipv4BfdMplsteHeadSummaryNode']['meta_info'].parent =_meta_table['Bfd.Ipv4BfdMplsteHeadSummaryNodes']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopCounters']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info'].parent =_meta_table['Bfd.SessionDetails']['meta_info']
_meta_table['Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters.Ipv6MultiHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv6MultiHopCounters.Ipv6MultiHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopCounters']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopLocationSummaries']['meta_info']
_meta_table['Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter']['meta_info'].parent =_meta_table['Bfd.LabelCounters.LabelPacketCounters']['meta_info']
_meta_table['Bfd.LabelCounters.LabelPacketCounters']['meta_info'].parent =_meta_table['Bfd.LabelCounters']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails']['meta_info']
_meta_table['Bfd.RelationBriefs.RelationBrief.LinkInformation']['meta_info'].parent =_meta_table['Bfd.RelationBriefs.RelationBrief']['meta_info']
_meta_table['Bfd.RelationBriefs.RelationBrief']['meta_info'].parent =_meta_table['Bfd.RelationBriefs']['meta_info']
_meta_table['Bfd.ClientBriefs.ClientBrief']['meta_info'].parent =_meta_table['Bfd.ClientBriefs']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadMultiPaths.Ipv4BfDoMplsteHeadMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadMultiPaths']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2LFec']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.TargetAddress']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.LinkInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info'].parent =_meta_table['Bfd.RelationDetails']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters.Ipv4BfDoMplsteTailPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailCounters.Ipv4BfDoMplsteTailPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailCounters']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailMultiPaths.Ipv4BfDoMplsteTailMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteTailMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4BfDoMplsteHeadSummary']['meta_info']
_meta_table['Bfd.LabelSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Counters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.ClientDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.GenericSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionMibs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSummaryNodes']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Summary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteTailNodeSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfdMplsteHeadSummaryNodes']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.RelationBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.ClientBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.RelationDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteTailMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4BfDoMplsteHeadSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
