


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NtpModeEnum' : _MetaInfoEnum('NtpModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-mode-unspec':'ntp_mode_unspec',
            'ntp-mode-symetric-active':'ntp_mode_symetric_active',
            'ntp-mode-symetric-passive':'ntp_mode_symetric_passive',
            'ntp-mode-client':'ntp_mode_client',
            'ntp-mode-server':'ntp_mode_server',
            'ntp-mode-xcast-server':'ntp_mode_xcast_server',
            'ntp-mode-control':'ntp_mode_control',
            'ntp-mode-private':'ntp_mode_private',
            'ntp-mode-xcast-client':'ntp_mode_xcast_client',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpPeerStatusEnum' : _MetaInfoEnum('NtpPeerStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-ctl-pst-sel-reject':'ntp_ctl_pst_sel_reject',
            'ntp-ctl-pst-sel-sane':'ntp_ctl_pst_sel_sane',
            'ntp-ctl-pst-sel-correct':'ntp_ctl_pst_sel_correct',
            'ntp-ctl-pst-sel-selcand':'ntp_ctl_pst_sel_selcand',
            'ntp-ctl-pst-sel-sync-cand':'ntp_ctl_pst_sel_sync_cand',
            'ntp-ctl-pst-sel-distsys-peer':'ntp_ctl_pst_sel_distsys_peer',
            'ntp-ctl-pst-sel-sys-peer':'ntp_ctl_pst_sel_sys_peer',
            'ntp-ctl-pst-sel-pps':'ntp_ctl_pst_sel_pps',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpLoopFilterStateEnum' : _MetaInfoEnum('NtpLoopFilterStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-loop-flt-n-set':'ntp_loop_flt_n_set',
            'ntp-loop-flt-f-set':'ntp_loop_flt_f_set',
            'ntp-loop-flt-spik':'ntp_loop_flt_spik',
            'ntp-loop-flt-freq':'ntp_loop_flt_freq',
            'ntp-loop-flt-sync':'ntp_loop_flt_sync',
            'ntp-loop-flt-unkn':'ntp_loop_flt_unkn',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'ClockUpdateNodeEnum' : _MetaInfoEnum('ClockUpdateNodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'clk-never-updated':'clk_never_updated',
            'clk-updated':'clk_updated',
            'clk-no-update-info':'clk_no_update_info',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpLeapEnum' : _MetaInfoEnum('NtpLeapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-leap-no-warning':'ntp_leap_no_warning',
            'ntp-leap-addse-cond':'ntp_leap_addse_cond',
            'ntp-leap-delse-cond':'ntp_leap_delse_cond',
            'ntp-leap-not-in-sync':'ntp_leap_not_in_sync',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sys-ref-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sys-drift',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status',
            False, 
            [
            _MetaInfoClassMember('clock-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Clock period in nanosecs
                ''',
                'clock_period',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-ntp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is NTP enabled
                ''',
                'is_ntp_enabled',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-updated', REFERENCE_ENUM_CLASS, 'ClockUpdateNodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'ClockUpdateNodeEnum', 
                [], [], 
                '''                Is clock updated
                ''',
                'is_updated',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('last-update', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Last Update
                ''',
                'last_update',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('loop-filter-state', REFERENCE_ENUM_CLASS, 'NtpLoopFilterStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLoopFilterStateEnum', 
                [], [], 
                '''                Loop Filter State
                ''',
                'loop_filter_state',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Peer poll interval
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer dispersion
                ''',
                'sys_dispersion',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-drift', REFERENCE_CLASS, 'SysDrift' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift', 
                [], [], 
                '''                System Drift
                ''',
                'sys_drift',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                leap
                ''',
                'sys_leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Clock offset
                ''',
                'sys_offset',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-precision', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Precision
                ''',
                'sys_precision',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-ref-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Reference clock ID
                ''',
                'sys_ref_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-ref-time', REFERENCE_CLASS, 'SysRefTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime', 
                [], [], 
                '''                Reference time
                ''',
                'sys_ref_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-root-delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root delay
                ''',
                'sys_root_delay',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-root-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root dispersion
                ''',
                'sys_root_dispersion',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-stratum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Stratum
                ''',
                'sys_stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'status',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo.PeerInfoCommon' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo.PeerInfoCommon',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer delay
                ''',
                'delay',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer dispersion
                ''',
                'dispersion',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Association mode with this peer
                ''',
                'host_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-poll', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Host poll
                ''',
                'host_poll',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is configured
                ''',
                'is_configured',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-sys-peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this is syspeer
                ''',
                'is_sys_peer',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer offset
                ''',
                'offset',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reachability', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Reachability
                ''',
                'reachability',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reference-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer reference ID
                ''',
                'reference_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'NtpPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpPeerStatusEnum', 
                [], [], 
                '''                Peer status
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('stratum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Peer stratum
                ''',
                'stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-info-common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo',
            False, 
            [
            _MetaInfoClassMember('peer-info-common', REFERENCE_CLASS, 'PeerInfoCommon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo.PeerInfoCommon', 
                [], [], 
                '''                Common peer info
                ''',
                'peer_info_common',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('time-since', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time since last frame received (-1=none)
                ''',
                'time_since',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-summary-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations',
            False, 
            [
            _MetaInfoClassMember('is-ntp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is NTP enabled
                ''',
                'is_ntp_enabled',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-summary-info', REFERENCE_LIST, 'PeerSummaryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo', 
                [], [], 
                '''                Peer info
                ''',
                'peer_summary_info',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'sys_leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'associations',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.PeerInfoCommon' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.PeerInfoCommon',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer delay
                ''',
                'delay',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer dispersion
                ''',
                'dispersion',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Association mode with this peer
                ''',
                'host_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-poll', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Host poll
                ''',
                'host_poll',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is configured
                ''',
                'is_configured',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-sys-peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this is syspeer
                ''',
                'is_sys_peer',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer offset
                ''',
                'offset',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reachability', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Reachability
                ''',
                'reachability',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reference-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer reference ID
                ''',
                'reference_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'NtpPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpPeerStatusEnum', 
                [], [], 
                '''                Peer status
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('stratum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Peer stratum
                ''',
                'stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-info-common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'ref-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'originate-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'receive-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'transmit-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.FilterDetail' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.FilterDetail',
            False, 
            [
            _MetaInfoClassMember('filter-delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                filter delay
                ''',
                'filter_delay',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('filter-disp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                filter disp
                ''',
                'filter_disp',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('filter-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                filter offset
                ''',
                'filter_offset',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'filter-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo',
            False, 
            [
            _MetaInfoClassMember('filter-detail', REFERENCE_LIST, 'FilterDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.FilterDetail', 
                [], [], 
                '''                Filter Details
                ''',
                'filter_detail',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False, max_elements=8),
            _MetaInfoClassMember('filter-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index into filter shift register
                ''',
                'filter_index',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-authenticated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is authenticated
                ''',
                'is_authenticated',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('is-ref-clock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is refclock
                ''',
                'is_ref_clock',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('originate-time', REFERENCE_CLASS, 'OriginateTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime', 
                [], [], 
                '''                Originate timestamp
                ''',
                'originate_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-info-common', REFERENCE_CLASS, 'PeerInfoCommon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.PeerInfoCommon', 
                [], [], 
                '''                Common peer info
                ''',
                'peer_info_common',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Peer's association mode
                ''',
                'peer_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Peer poll interval
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('precision', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Precision
                ''',
                'precision',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('receive-time', REFERENCE_CLASS, 'ReceiveTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime', 
                [], [], 
                '''                Receive timestamp
                ''',
                'receive_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('ref-time', REFERENCE_CLASS, 'RefTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime', 
                [], [], 
                '''                Reference time
                ''',
                'ref_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('root-delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root delay
                ''',
                'root_delay',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('root-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root dispersion
                ''',
                'root_dispersion',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('synch-distance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Synch distance
                ''',
                'synch_distance',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('transmit-time', REFERENCE_CLASS, 'TransmitTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime', 
                [], [], 
                '''                Transmit timestamp
                ''',
                'transmit_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                NTP version
                ''',
                'version',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail',
            False, 
            [
            _MetaInfoClassMember('is-ntp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is NTP enabled
                ''',
                'is_ntp_enabled',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-detail-info', REFERENCE_LIST, 'PeerDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo', 
                [], [], 
                '''                Peer info
                ''',
                'peer_detail_info',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'sys_leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'associations-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The instance number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('associations', REFERENCE_CLASS, 'Associations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations', 
                [], [], 
                '''                NTP Associations information
                ''',
                'associations',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('associations-detail', REFERENCE_CLASS, 'AssociationsDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail', 
                [], [], 
                '''                NTP Associations Detail information
                ''',
                'associations_detail',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status', 
                [], [], 
                '''                Status of NTP peer(s)
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance', 
                [], [], 
                '''                NTP operational data for a particular
                instance
                ''',
                'instance',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The slot number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances', 
                [], [], 
                '''                Instance-specific NTP operational data
                ''',
                'instances',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                NTP operational data for a particular slot
                ''',
                'slot',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The rack number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots', 
                [], [], 
                '''                Node-specific NTP operational data
                ''',
                'slots',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack', 
                [], [], 
                '''                NTP operational data for a particular rack
                ''',
                'rack',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp' : {
        'meta_info' : _MetaInfoClass('Ntp',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks', 
                [], [], 
                '''                Rack-specific NTP operational data
                ''',
                'racks',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'ntp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
}
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo.PeerInfoCommon']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.PeerInfoCommon']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.FilterDetail']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot.Instances']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['Ntp.Racks.Rack.Slots']['meta_info']
_meta_table['Ntp.Racks.Rack.Slots']['meta_info'].parent =_meta_table['Ntp.Racks.Rack']['meta_info']
_meta_table['Ntp.Racks.Rack']['meta_info'].parent =_meta_table['Ntp.Racks']['meta_info']
_meta_table['Ntp.Racks']['meta_info'].parent =_meta_table['Ntp']['meta_info']
