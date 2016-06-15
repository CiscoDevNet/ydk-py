


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'NtpPeerStatusEnum' : _MetaInfoEnum('NtpPeerStatusEnum', 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-ctl-pst-sel-reject':'NTP_CTL_PST_SEL_REJECT',
            'ntp-ctl-pst-sel-sane':'NTP_CTL_PST_SEL_SANE',
            'ntp-ctl-pst-sel-correct':'NTP_CTL_PST_SEL_CORRECT',
            'ntp-ctl-pst-sel-selcand':'NTP_CTL_PST_SEL_SELCAND',
            'ntp-ctl-pst-sel-sync-cand':'NTP_CTL_PST_SEL_SYNC_CAND',
            'ntp-ctl-pst-sel-distsys-peer':'NTP_CTL_PST_SEL_DISTSYS_PEER',
            'ntp-ctl-pst-sel-sys-peer':'NTP_CTL_PST_SEL_SYS_PEER',
            'ntp-ctl-pst-sel-pps':'NTP_CTL_PST_SEL_PPS',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpModeEnum' : _MetaInfoEnum('NtpModeEnum', 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-mode-unspec':'NTP_MODE_UNSPEC',
            'ntp-mode-symetric-active':'NTP_MODE_SYMETRIC_ACTIVE',
            'ntp-mode-symetric-passive':'NTP_MODE_SYMETRIC_PASSIVE',
            'ntp-mode-client':'NTP_MODE_CLIENT',
            'ntp-mode-server':'NTP_MODE_SERVER',
            'ntp-mode-xcast-server':'NTP_MODE_XCAST_SERVER',
            'ntp-mode-control':'NTP_MODE_CONTROL',
            'ntp-mode-private':'NTP_MODE_PRIVATE',
            'ntp-mode-xcast-client':'NTP_MODE_XCAST_CLIENT',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'ClockUpdateNodeEnum' : _MetaInfoEnum('ClockUpdateNodeEnum', 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'clk-never-updated':'CLK_NEVER_UPDATED',
            'clk-updated':'CLK_UPDATED',
            'clk-no-update-info':'CLK_NO_UPDATE_INFO',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpLoopFilterStateEnum' : _MetaInfoEnum('NtpLoopFilterStateEnum', 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-loop-flt-n-set':'NTP_LOOP_FLT_N_SET',
            'ntp-loop-flt-f-set':'NTP_LOOP_FLT_F_SET',
            'ntp-loop-flt-spik':'NTP_LOOP_FLT_SPIK',
            'ntp-loop-flt-freq':'NTP_LOOP_FLT_FREQ',
            'ntp-loop-flt-sync':'NTP_LOOP_FLT_SYNC',
            'ntp-loop-flt-unkn':'NTP_LOOP_FLT_UNKN',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'NtpLeapEnum' : _MetaInfoEnum('NtpLeapEnum', 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper',
        {
            'ntp-leap-no-warning':'NTP_LEAP_NO_WARNING',
            'ntp-leap-addse-cond':'NTP_LEAP_ADDSE_COND',
            'ntp-leap-delse-cond':'NTP_LEAP_DELSE_COND',
            'ntp-leap-not-in-sync':'NTP_LEAP_NOT_IN_SYNC',
        }, 'Cisco-IOS-XR-ip-ntp-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper']),
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sys-ref-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sys-drift',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status',
            False, 
            [
            _MetaInfoClassMember('clock-period', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('is-updated', REFERENCE_ENUM_CLASS, 'ClockUpdateNodeEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'ClockUpdateNodeEnum', 
                [], [], 
                '''                Is clock updated
                ''',
                'is_updated',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('last-update', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Last Update
                ''',
                'last_update',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('loop-filter-state', REFERENCE_ENUM_CLASS, 'NtpLoopFilterStateEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLoopFilterStateEnum', 
                [], [], 
                '''                Loop Filter State
                ''',
                'loop_filter_state',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
            _MetaInfoClassMember('sys-drift', REFERENCE_CLASS, 'SysDrift' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysDrift', 
                [], [], 
                '''                System Drift
                ''',
                'sys_drift',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
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
                [(-128, 127)], [], 
                '''                Precision
                ''',
                'sys_precision',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-ref-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Reference clock ID
                ''',
                'sys_ref_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-ref-time', REFERENCE_CLASS, 'SysRefTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status.SysRefTime', 
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
                [(0, 255)], [], 
                '''                Stratum
                ''',
                'sys_stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'status',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
            _MetaInfoClassMember('host-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Association mode with this peer
                ''',
                'host_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-poll', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
                [(0, 255)], [], 
                '''                Reachability
                ''',
                'reachability',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reference-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer reference ID
                ''',
                'reference_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'NtpPeerStatusEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpPeerStatusEnum', 
                [], [], 
                '''                Peer status
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('stratum', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Peer stratum
                ''',
                'stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-info-common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo',
            False, 
            [
            _MetaInfoClassMember('peer-info-common', REFERENCE_CLASS, 'PeerInfoCommon' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo.PeerInfoCommon', 
                [], [], 
                '''                Common peer info
                ''',
                'peer_info_common',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('time-since', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time since last frame received (-1=none)
                ''',
                'time_since',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-summary-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
            _MetaInfoClassMember('peer-summary-info', REFERENCE_LIST, 'PeerSummaryInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations.PeerSummaryInfo', 
                [], [], 
                '''                Peer info
                ''',
                'peer_summary_info',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'sys_leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'associations',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
            _MetaInfoClassMember('host-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Association mode with this peer
                ''',
                'host_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('host-poll', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
                [(0, 255)], [], 
                '''                Reachability
                ''',
                'reachability',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('reference-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer reference ID
                ''',
                'reference_id',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'NtpPeerStatusEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpPeerStatusEnum', 
                [], [], 
                '''                Peer status
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('stratum', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Peer stratum
                ''',
                'stratum',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-info-common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'ref-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'originate-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'receive-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec',
            False, 
            [
            _MetaInfoClassMember('int', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Integer format in NTP reference code
                ''',
                'int',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'sec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs',
            False, 
            [
            _MetaInfoClassMember('frac', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Fractional format in NTP reference code
                ''',
                'frac',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'frac-secs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime',
            False, 
            [
            _MetaInfoClassMember('frac-secs', REFERENCE_CLASS, 'FracSecs' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs', 
                [], [], 
                '''                Fractional part in 64-bit NTP timestamp
                ''',
                'frac_secs',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sec', REFERENCE_CLASS, 'Sec' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec', 
                [], [], 
                '''                Second part in 64-bit NTP timestamp
                ''',
                'sec',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'transmit-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo',
            False, 
            [
            _MetaInfoClassMember('filter-detail', REFERENCE_LIST, 'FilterDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.FilterDetail', 
                [], [], 
                '''                Filter Details
                ''',
                'filter_detail',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False, max_elements=8),
            _MetaInfoClassMember('filter-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('originate-time', REFERENCE_CLASS, 'OriginateTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.OriginateTime', 
                [], [], 
                '''                Originate timestamp
                ''',
                'originate_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-info-common', REFERENCE_CLASS, 'PeerInfoCommon' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.PeerInfoCommon', 
                [], [], 
                '''                Common peer info
                ''',
                'peer_info_common',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('peer-mode', REFERENCE_ENUM_CLASS, 'NtpModeEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpModeEnum', 
                [], [], 
                '''                Peer's association mode
                ''',
                'peer_mode',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Peer poll interval
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('precision', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                Precision
                ''',
                'precision',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('receive-time', REFERENCE_CLASS, 'ReceiveTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.ReceiveTime', 
                [], [], 
                '''                Receive timestamp
                ''',
                'receive_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('ref-time', REFERENCE_CLASS, 'RefTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.RefTime', 
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
            _MetaInfoClassMember('transmit-time', REFERENCE_CLASS, 'TransmitTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo.TransmitTime', 
                [], [], 
                '''                Transmit timestamp
                ''',
                'transmit_time',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                NTP version
                ''',
                'version',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'peer-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
            _MetaInfoClassMember('peer-detail-info', REFERENCE_LIST, 'PeerDetailInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail.PeerDetailInfo', 
                [], [], 
                '''                Peer info
                ''',
                'peer_detail_info',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('sys-leap', REFERENCE_ENUM_CLASS, 'NtpLeapEnum' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'NtpLeapEnum', 
                [], [], 
                '''                Leap
                ''',
                'sys_leap',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'associations-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The instance number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('associations', REFERENCE_CLASS, 'Associations' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Associations', 
                [], [], 
                '''                NTP Associations information
                ''',
                'associations',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('associations-detail', REFERENCE_CLASS, 'AssociationsDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.AssociationsDetail', 
                [], [], 
                '''                NTP Associations Detail information
                ''',
                'associations_detail',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance.Status', 
                [], [], 
                '''                Status of NTP peer(s)
                ''',
                'status',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot.Instances' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances.Instance', 
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
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The slot number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot.Instances', 
                [], [], 
                '''                Instance-specific NTP operational data
                ''',
                'instances',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                NTP operational data for a particular slot
                ''',
                'slot',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The rack number
                ''',
                'number',
                'Cisco-IOS-XR-ip-ntp-admin-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack.Slots', 
                [], [], 
                '''                Node-specific NTP operational data
                ''',
                'slots',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp.Racks' : {
        'meta_info' : _MetaInfoClass('Ntp.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks.Rack', 
                [], [], 
                '''                NTP operational data for a particular rack
                ''',
                'rack',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
        ),
    },
    'Ntp' : {
        'meta_info' : _MetaInfoClass('Ntp',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper', 'Ntp.Racks', 
                [], [], 
                '''                Rack-specific NTP operational data
                ''',
                'racks',
                'Cisco-IOS-XR-ip-ntp-admin-oper', False),
            ],
            'Cisco-IOS-XR-ip-ntp-admin-oper',
            'ntp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-admin-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_ntp_admin_oper'
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
