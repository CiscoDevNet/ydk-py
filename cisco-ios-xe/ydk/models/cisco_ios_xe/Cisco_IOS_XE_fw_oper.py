""" Cisco_IOS_XE_fw_oper 

This module contains a collection of YANG definitions
for ZBFW operational data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class FwOperData(Entity):
    """
    Operational state of ZBFW
    
    .. attribute:: fw_drop_stats
    
    	Firewall Drop Statistcis
    	**type**\:  :py:class:`FwDropStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fw_oper.FwOperData.FwDropStats>`
    
    	**presence node**\: True
    
    	**config**\: False
    
    .. attribute:: fw_zonepair_entries
    
    	Firewall Zonepair list entries
    	**type**\: list of  		 :py:class:`FwZonepairEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fw_oper.FwOperData.FwZonepairEntries>`
    
    	**config**\: False
    
    

    """

    _prefix = 'fw-ios-xe-oper'
    _revision = '2018-02-22'

    def __init__(self):
        super(FwOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "fw-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-fw-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("fw-drop-stats", ("fw_drop_stats", FwOperData.FwDropStats)), ("fw-zonepair-entries", ("fw_zonepair_entries", FwOperData.FwZonepairEntries))])
        self._leafs = OrderedDict()

        self.fw_drop_stats = None
        self._children_name_map["fw_drop_stats"] = "fw-drop-stats"

        self.fw_zonepair_entries = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-fw-oper:fw-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FwOperData, [], name, value)


    class FwDropStats(Entity):
        """
        Firewall Drop Statistcis
        
        .. attribute:: catch_all
        
        	Total packet drops seen since bringup
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_max_halfsession
        
        	Packet drops due to maximum L4 half\-open sessions reached
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_too_many_pkts
        
        	Packet drops due to exceeding the maximum number of inspectable packets allowed per flow
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_session_limit
        
        	Packet drops for session initiators after exceeding maximum session limit
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_invalid_hdr
        
        	Packet drops due to invalid header/packet length
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_internal_err_undefined_dir
        
        	Packet drops due to a failure in determining direction
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_scb_close
        
        	Packet drops due to session in internal close state
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_ack_flag
        
        	Packet drops due to invalid TCP ACK flags
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_ack_num
        
        	Packet drops due to invalid ACK number
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_tcp_initiator
        
        	Packet drops due to non\-SYN packets received without valid session
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_syn_with_data
        
        	Packet drops due to SYN packets having data
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_win_scale_option
        
        	Packet drops due to invalid TCP window scale option
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seg_synsent_state
        
        	Packet drops due to invalid packets received in SYNSENT state
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seg_synrcvd_state
        
        	Packet drops due to invalid packets received in SYNRCVD state
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seg_pkt_too_old
        
        	Packet drops due to packets being too old/out of window
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seg_pkt_win_overflow
        
        	Packet drops due to receiver window overflow (except when vTCP is enabled)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seg_pyld_after_fin_send
        
        	Packet drops due to payload received after FIN is sent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_flags
        
        	Packet drops due to invalid/unexpected TCP flags
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_invalid_seq
        
        	Packet drops due to invalid sequence number
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_retrans_invalid_flags
        
        	Packet drops due to invalid flags in TCP retransmitted packet
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_l7_ooo_seg
        
        	Packet drops due to L7 not accepting out\-of\-order TCP segments
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_syn_flood_drop
        
        	Packet drops during SYN flood attack
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_internal_err_synflood_alloc_hostdb_fail
        
        	Packet drops due to failure of hostdb allocation during a SYN flood attack
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_synflood_blackout_drop
        
        	Packet drops due to blackout drop time when exceeding configured half\-open connections
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_unexpect_tcp_payload
        
        	Packet drops due to receiving TCP packet with payload when a response is expected for SYN
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_syn_in_win
        
        	Packet drops due to receiving SYN in an established connection
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_rst_in_win
        
        	Packet drops due to receiving RST in an established connection
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_stray_seg
        
        	Packet drops due to unexpected/stray TCP segments
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_tcp_rst_to_resp
        
        	RST sent to responder in SYNSENT state when ACK sequence is invalid
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_pam_lookup_fail
        
        	Packet drops when policy exists in zone\-pair but PAM lookup fails
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_internal_err_get_stat_blk_fail
        
        	Packet drops due to failure to get statistics block
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_dstaddr_lookup_fail
        
        	Packet drops due to destination address lookup failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_policy_not_present
        
        	Packet drops due to inspection policy not present in zone\-pair
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_sess_miss_policy_not_present
        
        	Packet drops due to session lookup failure and no matching policy present
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_classification_fail
        
        	Packet drops due to protocol classification failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_class_action_drop
        
        	Packet drops due to a drop classification action
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: insp_policy_misconfigure
        
        	Packet drops due to failed classification because of misconfigured security policy
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_too_many_err_pkts
        
        	Packet drops after exceeding the maximum number of ICMP error packets allowed per flow
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_internal_err_no_nat
        
        	Packet drops when ICMP is NATed without internal NAT info
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_internal_err_alloc_fail
        
        	Packet drops when ICMP failed to get error packets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_internal_err_get_stat_blk_fail
        
        	Packet drops due to a failure to get statistics block
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_internal_err_dir_not_identified
        
        	Packet drops due to unidentified ICMP packet direction
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_scb_close
        
        	Packet drops due to receiving ICMP packets when session is in internal close state
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_pkt_no_ip_hdr
        
        	Packet drops due to missing IP header in ICMP packets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_pkt_too_short
        
        	Packet drops due to ICMP error where packets are too short
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_no_ip_no_icmp
        
        	Packet drops due to packets not identified as IP or ICMP
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_pkts_burst
        
        	Packet drops due to ICMP error where packet bursts exceed a limit of 10
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_multiple_unreach
        
        	Packet drops due to receiving multiple unreachable packets; only 1 is allowed
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_l4_invalid_seq
        
        	Packet drops when inner TCP sequence number of packet doesn't match that of packet originating the ICMP error
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_l4_invalid_ack
        
        	Packet drops due to inner TCP header invalid ACK
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_policy_not_present
        
        	Packet drops due to missing policy on zone\-pair for ICMP
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l4_icmp_err_classification_fail
        
        	Packet drops due to a miss when doing reverse path flow check
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: syncookie_max_dst
        
        	SYNcookie Packet drops when we've reached maximum number of SYN destinations per zone
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: syncookie_internal_err_alloc_fail
        
        	SYNcookie Packet drops due to a failure in allocating memory in the destination table
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: syncookie_trigger
        
        	Packet drops due to a SYNcookie trigger
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: policy_fragment_drop
        
        	Packet drops due to dropping fragmented packet when first fragment drops
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: policy_action_drop
        
        	Packet drops when policy action is drop
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: policy_icmp_action_drop
        
        	Packet drops when policy action for the ICMP packet is to drop
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_type_drop
        
        	Packet drops when L7 inspection returns drop as the action
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_no_seg
        
        	Packet drops due to receiving segmented packets when ALG doesn't honor them
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_no_frag
        
        	Packet drops due to receiving fragmented packets when ALG doesn't honor them
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_unknown_proto
        
        	Packet drops due to unrecognized L7 protocol type
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_alg_ret_drop
        
        	Packet drops due to L7 (ALG) deciding to drop the packet
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_promote_fail_no_zone_pair
        
        	Packet drops due to L7 sub\-channel promotion failure due to no zone pair configured for the sub\-channel
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: l7_promote_fail_no_policy
        
        	Packet drops due to L7 sub\-channel promotion failure due to no policy configured for the sub\-channel
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: no_session
        
        	Packet drops due to session creation failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: no_new_session
        
        	Packet drops due to internal state not allowing new session creation
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: not_initiator
        
        	Packet drops due to receiving a non\-initiator packet for a session
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: invalid_zone
        
        	Packet drops due to a zone not configured for interface
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: ha_ar_standby
        
        	Packet drops due to asymmetric routing not configured and box not in active state
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: no_forwarding_zone
        
        	Packet drops when Firewall is uninitialized
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: backpressure
        
        	Packet drops due to backpressure by log mechanism
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: zone_mismatch
        
        	Packet drops due to zone mismatch
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: fdb_err
        
        	Packet drops due to a failure to register flow with flow database
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: lisp_header_restore_fail
        
        	Packet drops due to LISP header restoration failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: lisp_inner_pkt_insane
        
        	Packet drops due to LISP inner packet sanity check failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: lisp_inner_ipv4_insane
        
        	Packet drops due to LISP inner packet IPV4 sanity check failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: lisp_inner_ipv6_insane
        
        	Packet drops due to LISP inner packet IPV6 sanity check failure
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'fw-ios-xe-oper'
        _revision = '2018-02-22'

        def __init__(self):
            super(FwOperData.FwDropStats, self).__init__()

            self.yang_name = "fw-drop-stats"
            self.yang_parent_name = "fw-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('catch_all', (YLeaf(YType.uint64, 'catch-all'), ['int'])),
                ('l4_max_halfsession', (YLeaf(YType.uint64, 'l4-max-halfsession'), ['int'])),
                ('l4_too_many_pkts', (YLeaf(YType.uint64, 'l4-too-many-pkts'), ['int'])),
                ('l4_session_limit', (YLeaf(YType.uint64, 'l4-session-limit'), ['int'])),
                ('l4_invalid_hdr', (YLeaf(YType.uint64, 'l4-invalid-hdr'), ['int'])),
                ('l4_internal_err_undefined_dir', (YLeaf(YType.uint64, 'l4-internal-err-undefined-dir'), ['int'])),
                ('l4_scb_close', (YLeaf(YType.uint64, 'l4-scb-close'), ['int'])),
                ('l4_tcp_invalid_ack_flag', (YLeaf(YType.uint64, 'l4-tcp-invalid-ack-flag'), ['int'])),
                ('l4_tcp_invalid_ack_num', (YLeaf(YType.uint64, 'l4-tcp-invalid-ack-num'), ['int'])),
                ('l4_tcp_invalid_tcp_initiator', (YLeaf(YType.uint64, 'l4-tcp-invalid-tcp-initiator'), ['int'])),
                ('l4_tcp_syn_with_data', (YLeaf(YType.uint64, 'l4-tcp-syn-with-data'), ['int'])),
                ('l4_tcp_invalid_win_scale_option', (YLeaf(YType.uint64, 'l4-tcp-invalid-win-scale-option'), ['int'])),
                ('l4_tcp_invalid_seg_synsent_state', (YLeaf(YType.uint64, 'l4-tcp-invalid-seg-synsent-state'), ['int'])),
                ('l4_tcp_invalid_seg_synrcvd_state', (YLeaf(YType.uint64, 'l4-tcp-invalid-seg-synrcvd-state'), ['int'])),
                ('l4_tcp_invalid_seg_pkt_too_old', (YLeaf(YType.uint64, 'l4-tcp-invalid-seg-pkt-too-old'), ['int'])),
                ('l4_tcp_invalid_seg_pkt_win_overflow', (YLeaf(YType.uint64, 'l4-tcp-invalid-seg-pkt-win-overflow'), ['int'])),
                ('l4_tcp_invalid_seg_pyld_after_fin_send', (YLeaf(YType.uint64, 'l4-tcp-invalid-seg-pyld-after-fin-send'), ['int'])),
                ('l4_tcp_invalid_flags', (YLeaf(YType.uint64, 'l4-tcp-invalid-flags'), ['int'])),
                ('l4_tcp_invalid_seq', (YLeaf(YType.uint64, 'l4-tcp-invalid-seq'), ['int'])),
                ('l4_tcp_retrans_invalid_flags', (YLeaf(YType.uint64, 'l4-tcp-retrans-invalid-flags'), ['int'])),
                ('l4_tcp_l7_ooo_seg', (YLeaf(YType.uint64, 'l4-tcp-l7-ooo-seg'), ['int'])),
                ('l4_tcp_syn_flood_drop', (YLeaf(YType.uint64, 'l4-tcp-syn-flood-drop'), ['int'])),
                ('l4_tcp_internal_err_synflood_alloc_hostdb_fail', (YLeaf(YType.uint64, 'l4-tcp-internal-err-synflood-alloc-hostdb-fail'), ['int'])),
                ('l4_tcp_synflood_blackout_drop', (YLeaf(YType.uint64, 'l4-tcp-synflood-blackout-drop'), ['int'])),
                ('l4_tcp_unexpect_tcp_payload', (YLeaf(YType.uint64, 'l4-tcp-unexpect-tcp-payload'), ['int'])),
                ('l4_tcp_syn_in_win', (YLeaf(YType.uint64, 'l4-tcp-syn-in-win'), ['int'])),
                ('l4_tcp_rst_in_win', (YLeaf(YType.uint64, 'l4-tcp-rst-in-win'), ['int'])),
                ('l4_tcp_stray_seg', (YLeaf(YType.uint64, 'l4-tcp-stray-seg'), ['int'])),
                ('l4_tcp_rst_to_resp', (YLeaf(YType.uint64, 'l4-tcp-rst-to-resp'), ['int'])),
                ('insp_pam_lookup_fail', (YLeaf(YType.uint64, 'insp-pam-lookup-fail'), ['int'])),
                ('insp_internal_err_get_stat_blk_fail', (YLeaf(YType.uint64, 'insp-internal-err-get-stat-blk-fail'), ['int'])),
                ('insp_dstaddr_lookup_fail', (YLeaf(YType.uint64, 'insp-dstaddr-lookup-fail'), ['int'])),
                ('insp_policy_not_present', (YLeaf(YType.uint64, 'insp-policy-not-present'), ['int'])),
                ('insp_sess_miss_policy_not_present', (YLeaf(YType.uint64, 'insp-sess-miss-policy-not-present'), ['int'])),
                ('insp_classification_fail', (YLeaf(YType.uint64, 'insp-classification-fail'), ['int'])),
                ('insp_class_action_drop', (YLeaf(YType.uint64, 'insp-class-action-drop'), ['int'])),
                ('insp_policy_misconfigure', (YLeaf(YType.uint64, 'insp-policy-misconfigure'), ['int'])),
                ('l4_icmp_too_many_err_pkts', (YLeaf(YType.uint64, 'l4-icmp-too-many-err-pkts'), ['int'])),
                ('l4_icmp_internal_err_no_nat', (YLeaf(YType.uint64, 'l4-icmp-internal-err-no-nat'), ['int'])),
                ('l4_icmp_internal_err_alloc_fail', (YLeaf(YType.uint64, 'l4-icmp-internal-err-alloc-fail'), ['int'])),
                ('l4_icmp_internal_err_get_stat_blk_fail', (YLeaf(YType.uint64, 'l4-icmp-internal-err-get-stat-blk-fail'), ['int'])),
                ('l4_icmp_internal_err_dir_not_identified', (YLeaf(YType.uint64, 'l4-icmp-internal-err-dir-not-identified'), ['int'])),
                ('l4_icmp_scb_close', (YLeaf(YType.uint64, 'l4-icmp-scb-close'), ['int'])),
                ('l4_icmp_pkt_no_ip_hdr', (YLeaf(YType.uint64, 'l4-icmp-pkt-no-ip-hdr'), ['int'])),
                ('l4_icmp_pkt_too_short', (YLeaf(YType.uint64, 'l4-icmp-pkt-too-short'), ['int'])),
                ('l4_icmp_err_no_ip_no_icmp', (YLeaf(YType.uint64, 'l4-icmp-err-no-ip-no-icmp'), ['int'])),
                ('l4_icmp_err_pkts_burst', (YLeaf(YType.uint64, 'l4-icmp-err-pkts-burst'), ['int'])),
                ('l4_icmp_err_multiple_unreach', (YLeaf(YType.uint64, 'l4-icmp-err-multiple-unreach'), ['int'])),
                ('l4_icmp_err_l4_invalid_seq', (YLeaf(YType.uint64, 'l4-icmp-err-l4-invalid-seq'), ['int'])),
                ('l4_icmp_err_l4_invalid_ack', (YLeaf(YType.uint64, 'l4-icmp-err-l4-invalid-ack'), ['int'])),
                ('l4_icmp_err_policy_not_present', (YLeaf(YType.uint64, 'l4-icmp-err-policy-not-present'), ['int'])),
                ('l4_icmp_err_classification_fail', (YLeaf(YType.uint64, 'l4-icmp-err-classification-fail'), ['int'])),
                ('syncookie_max_dst', (YLeaf(YType.uint64, 'syncookie-max-dst'), ['int'])),
                ('syncookie_internal_err_alloc_fail', (YLeaf(YType.uint64, 'syncookie-internal-err-alloc-fail'), ['int'])),
                ('syncookie_trigger', (YLeaf(YType.uint64, 'syncookie-trigger'), ['int'])),
                ('policy_fragment_drop', (YLeaf(YType.uint64, 'policy-fragment-drop'), ['int'])),
                ('policy_action_drop', (YLeaf(YType.uint64, 'policy-action-drop'), ['int'])),
                ('policy_icmp_action_drop', (YLeaf(YType.uint64, 'policy-icmp-action-drop'), ['int'])),
                ('l7_type_drop', (YLeaf(YType.uint64, 'l7-type-drop'), ['int'])),
                ('l7_no_seg', (YLeaf(YType.uint64, 'l7-no-seg'), ['int'])),
                ('l7_no_frag', (YLeaf(YType.uint64, 'l7-no-frag'), ['int'])),
                ('l7_unknown_proto', (YLeaf(YType.uint64, 'l7-unknown-proto'), ['int'])),
                ('l7_alg_ret_drop', (YLeaf(YType.uint64, 'l7-alg-ret-drop'), ['int'])),
                ('l7_promote_fail_no_zone_pair', (YLeaf(YType.uint64, 'l7-promote-fail-no-zone-pair'), ['int'])),
                ('l7_promote_fail_no_policy', (YLeaf(YType.uint64, 'l7-promote-fail-no-policy'), ['int'])),
                ('no_session', (YLeaf(YType.uint64, 'no-session'), ['int'])),
                ('no_new_session', (YLeaf(YType.uint64, 'no-new-session'), ['int'])),
                ('not_initiator', (YLeaf(YType.uint64, 'not-initiator'), ['int'])),
                ('invalid_zone', (YLeaf(YType.uint64, 'invalid-zone'), ['int'])),
                ('ha_ar_standby', (YLeaf(YType.uint64, 'ha-ar-standby'), ['int'])),
                ('no_forwarding_zone', (YLeaf(YType.uint64, 'no-forwarding-zone'), ['int'])),
                ('backpressure', (YLeaf(YType.uint64, 'backpressure'), ['int'])),
                ('zone_mismatch', (YLeaf(YType.uint64, 'zone-mismatch'), ['int'])),
                ('fdb_err', (YLeaf(YType.uint64, 'fdb-err'), ['int'])),
                ('lisp_header_restore_fail', (YLeaf(YType.uint64, 'lisp-header-restore-fail'), ['int'])),
                ('lisp_inner_pkt_insane', (YLeaf(YType.uint64, 'lisp-inner-pkt-insane'), ['int'])),
                ('lisp_inner_ipv4_insane', (YLeaf(YType.uint64, 'lisp-inner-ipv4-insane'), ['int'])),
                ('lisp_inner_ipv6_insane', (YLeaf(YType.uint64, 'lisp-inner-ipv6-insane'), ['int'])),
            ])
            self.catch_all = None
            self.l4_max_halfsession = None
            self.l4_too_many_pkts = None
            self.l4_session_limit = None
            self.l4_invalid_hdr = None
            self.l4_internal_err_undefined_dir = None
            self.l4_scb_close = None
            self.l4_tcp_invalid_ack_flag = None
            self.l4_tcp_invalid_ack_num = None
            self.l4_tcp_invalid_tcp_initiator = None
            self.l4_tcp_syn_with_data = None
            self.l4_tcp_invalid_win_scale_option = None
            self.l4_tcp_invalid_seg_synsent_state = None
            self.l4_tcp_invalid_seg_synrcvd_state = None
            self.l4_tcp_invalid_seg_pkt_too_old = None
            self.l4_tcp_invalid_seg_pkt_win_overflow = None
            self.l4_tcp_invalid_seg_pyld_after_fin_send = None
            self.l4_tcp_invalid_flags = None
            self.l4_tcp_invalid_seq = None
            self.l4_tcp_retrans_invalid_flags = None
            self.l4_tcp_l7_ooo_seg = None
            self.l4_tcp_syn_flood_drop = None
            self.l4_tcp_internal_err_synflood_alloc_hostdb_fail = None
            self.l4_tcp_synflood_blackout_drop = None
            self.l4_tcp_unexpect_tcp_payload = None
            self.l4_tcp_syn_in_win = None
            self.l4_tcp_rst_in_win = None
            self.l4_tcp_stray_seg = None
            self.l4_tcp_rst_to_resp = None
            self.insp_pam_lookup_fail = None
            self.insp_internal_err_get_stat_blk_fail = None
            self.insp_dstaddr_lookup_fail = None
            self.insp_policy_not_present = None
            self.insp_sess_miss_policy_not_present = None
            self.insp_classification_fail = None
            self.insp_class_action_drop = None
            self.insp_policy_misconfigure = None
            self.l4_icmp_too_many_err_pkts = None
            self.l4_icmp_internal_err_no_nat = None
            self.l4_icmp_internal_err_alloc_fail = None
            self.l4_icmp_internal_err_get_stat_blk_fail = None
            self.l4_icmp_internal_err_dir_not_identified = None
            self.l4_icmp_scb_close = None
            self.l4_icmp_pkt_no_ip_hdr = None
            self.l4_icmp_pkt_too_short = None
            self.l4_icmp_err_no_ip_no_icmp = None
            self.l4_icmp_err_pkts_burst = None
            self.l4_icmp_err_multiple_unreach = None
            self.l4_icmp_err_l4_invalid_seq = None
            self.l4_icmp_err_l4_invalid_ack = None
            self.l4_icmp_err_policy_not_present = None
            self.l4_icmp_err_classification_fail = None
            self.syncookie_max_dst = None
            self.syncookie_internal_err_alloc_fail = None
            self.syncookie_trigger = None
            self.policy_fragment_drop = None
            self.policy_action_drop = None
            self.policy_icmp_action_drop = None
            self.l7_type_drop = None
            self.l7_no_seg = None
            self.l7_no_frag = None
            self.l7_unknown_proto = None
            self.l7_alg_ret_drop = None
            self.l7_promote_fail_no_zone_pair = None
            self.l7_promote_fail_no_policy = None
            self.no_session = None
            self.no_new_session = None
            self.not_initiator = None
            self.invalid_zone = None
            self.ha_ar_standby = None
            self.no_forwarding_zone = None
            self.backpressure = None
            self.zone_mismatch = None
            self.fdb_err = None
            self.lisp_header_restore_fail = None
            self.lisp_inner_pkt_insane = None
            self.lisp_inner_ipv4_insane = None
            self.lisp_inner_ipv6_insane = None
            self._segment_path = lambda: "fw-drop-stats"
            self._absolute_path = lambda: "Cisco-IOS-XE-fw-oper:fw-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FwOperData.FwDropStats, ['catch_all', 'l4_max_halfsession', 'l4_too_many_pkts', 'l4_session_limit', 'l4_invalid_hdr', 'l4_internal_err_undefined_dir', 'l4_scb_close', 'l4_tcp_invalid_ack_flag', 'l4_tcp_invalid_ack_num', 'l4_tcp_invalid_tcp_initiator', 'l4_tcp_syn_with_data', 'l4_tcp_invalid_win_scale_option', 'l4_tcp_invalid_seg_synsent_state', 'l4_tcp_invalid_seg_synrcvd_state', 'l4_tcp_invalid_seg_pkt_too_old', 'l4_tcp_invalid_seg_pkt_win_overflow', 'l4_tcp_invalid_seg_pyld_after_fin_send', 'l4_tcp_invalid_flags', 'l4_tcp_invalid_seq', 'l4_tcp_retrans_invalid_flags', 'l4_tcp_l7_ooo_seg', 'l4_tcp_syn_flood_drop', 'l4_tcp_internal_err_synflood_alloc_hostdb_fail', 'l4_tcp_synflood_blackout_drop', 'l4_tcp_unexpect_tcp_payload', 'l4_tcp_syn_in_win', 'l4_tcp_rst_in_win', 'l4_tcp_stray_seg', 'l4_tcp_rst_to_resp', 'insp_pam_lookup_fail', 'insp_internal_err_get_stat_blk_fail', 'insp_dstaddr_lookup_fail', 'insp_policy_not_present', 'insp_sess_miss_policy_not_present', 'insp_classification_fail', 'insp_class_action_drop', 'insp_policy_misconfigure', 'l4_icmp_too_many_err_pkts', 'l4_icmp_internal_err_no_nat', 'l4_icmp_internal_err_alloc_fail', 'l4_icmp_internal_err_get_stat_blk_fail', 'l4_icmp_internal_err_dir_not_identified', 'l4_icmp_scb_close', 'l4_icmp_pkt_no_ip_hdr', 'l4_icmp_pkt_too_short', 'l4_icmp_err_no_ip_no_icmp', 'l4_icmp_err_pkts_burst', 'l4_icmp_err_multiple_unreach', 'l4_icmp_err_l4_invalid_seq', 'l4_icmp_err_l4_invalid_ack', 'l4_icmp_err_policy_not_present', 'l4_icmp_err_classification_fail', 'syncookie_max_dst', 'syncookie_internal_err_alloc_fail', 'syncookie_trigger', 'policy_fragment_drop', 'policy_action_drop', 'policy_icmp_action_drop', 'l7_type_drop', 'l7_no_seg', 'l7_no_frag', 'l7_unknown_proto', 'l7_alg_ret_drop', 'l7_promote_fail_no_zone_pair', 'l7_promote_fail_no_policy', 'no_session', 'no_new_session', 'not_initiator', 'invalid_zone', 'ha_ar_standby', 'no_forwarding_zone', 'backpressure', 'zone_mismatch', 'fdb_err', 'lisp_header_restore_fail', 'lisp_inner_pkt_insane', 'lisp_inner_ipv4_insane', 'lisp_inner_ipv6_insane'], name, value)



    class FwZonepairEntries(Entity):
        """
        Firewall Zonepair list entries
        
        .. attribute:: zonepair_name  (key)
        
        	Name of the zone pair
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: src_zone_name
        
        	Name of the source zone
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: dst_zone_name
        
        	Name of the destination zone
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: policy_name
        
        	Name of the policy applied for this zone pair
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: fw_traffic_class_entry
        
        	Firewall Traffic class list entries
        	**type**\: list of  		 :py:class:`FwTrafficClassEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fw_oper.FwOperData.FwZonepairEntries.FwTrafficClassEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fw-ios-xe-oper'
        _revision = '2018-02-22'

        def __init__(self):
            super(FwOperData.FwZonepairEntries, self).__init__()

            self.yang_name = "fw-zonepair-entries"
            self.yang_parent_name = "fw-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['zonepair_name']
            self._child_classes = OrderedDict([("fw-traffic-class-entry", ("fw_traffic_class_entry", FwOperData.FwZonepairEntries.FwTrafficClassEntry))])
            self._leafs = OrderedDict([
                ('zonepair_name', (YLeaf(YType.str, 'zonepair-name'), ['str'])),
                ('src_zone_name', (YLeaf(YType.str, 'src-zone-name'), ['str'])),
                ('dst_zone_name', (YLeaf(YType.str, 'dst-zone-name'), ['str'])),
                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
            ])
            self.zonepair_name = None
            self.src_zone_name = None
            self.dst_zone_name = None
            self.policy_name = None

            self.fw_traffic_class_entry = YList(self)
            self._segment_path = lambda: "fw-zonepair-entries" + "[zonepair-name='" + str(self.zonepair_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-fw-oper:fw-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FwOperData.FwZonepairEntries, ['zonepair_name', 'src_zone_name', 'dst_zone_name', 'policy_name'], name, value)


        class FwTrafficClassEntry(Entity):
            """
            Firewall Traffic class list entries
            
            .. attribute:: class_name  (key)
            
            	Name of the traffic class
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: zonepair_name
            
            	Zonepair name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: class_action
            
            	Action for the traffic class
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: pkts_counter
            
            	Total Packets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: bytes_counter
            
            	Total bytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: attempted_conn
            
            	Total number for the attempted connections matching this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: current_active_conn
            
            	Current number of active connections matching this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: max_active_conn
            
            	Maximum number of active connections seen for this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: current_halfopen_conn
            
            	Current number of half\-open connections seen for this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: max_halfopen_conn
            
            	Maximum number of half\-open connections seen for this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: current_terminating_conn
            
            	Current number of terminating connections seen for this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: max_terminating_conn
            
            	Maximum number of terminating connections seen for this traffic class
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: time_since_last_session_create
            
            	Seconds since last session creation
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: fw_tc_match_entry
            
            	List of match conditions
            	**type**\: list of  		 :py:class:`FwTcMatchEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fw_oper.FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcMatchEntry>`
            
            	**config**\: False
            
            .. attribute:: fw_tc_proto_entry
            
            	Firewall Traffic class protocol list entries
            	**type**\: list of  		 :py:class:`FwTcProtoEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fw_oper.FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcProtoEntry>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fw-ios-xe-oper'
            _revision = '2018-02-22'

            def __init__(self):
                super(FwOperData.FwZonepairEntries.FwTrafficClassEntry, self).__init__()

                self.yang_name = "fw-traffic-class-entry"
                self.yang_parent_name = "fw-zonepair-entries"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['class_name']
                self._child_classes = OrderedDict([("fw-tc-match-entry", ("fw_tc_match_entry", FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcMatchEntry)), ("fw-tc-proto-entry", ("fw_tc_proto_entry", FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcProtoEntry))])
                self._leafs = OrderedDict([
                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                    ('zonepair_name', (YLeaf(YType.str, 'zonepair-name'), ['str'])),
                    ('class_action', (YLeaf(YType.str, 'class-action'), ['str'])),
                    ('pkts_counter', (YLeaf(YType.uint64, 'pkts-counter'), ['int'])),
                    ('bytes_counter', (YLeaf(YType.uint64, 'bytes-counter'), ['int'])),
                    ('attempted_conn', (YLeaf(YType.uint64, 'attempted-conn'), ['int'])),
                    ('current_active_conn', (YLeaf(YType.uint64, 'current-active-conn'), ['int'])),
                    ('max_active_conn', (YLeaf(YType.uint64, 'max-active-conn'), ['int'])),
                    ('current_halfopen_conn', (YLeaf(YType.uint64, 'current-halfopen-conn'), ['int'])),
                    ('max_halfopen_conn', (YLeaf(YType.uint64, 'max-halfopen-conn'), ['int'])),
                    ('current_terminating_conn', (YLeaf(YType.uint64, 'current-terminating-conn'), ['int'])),
                    ('max_terminating_conn', (YLeaf(YType.uint64, 'max-terminating-conn'), ['int'])),
                    ('time_since_last_session_create', (YLeaf(YType.uint64, 'time-since-last-session-create'), ['int'])),
                ])
                self.class_name = None
                self.zonepair_name = None
                self.class_action = None
                self.pkts_counter = None
                self.bytes_counter = None
                self.attempted_conn = None
                self.current_active_conn = None
                self.max_active_conn = None
                self.current_halfopen_conn = None
                self.max_halfopen_conn = None
                self.current_terminating_conn = None
                self.max_terminating_conn = None
                self.time_since_last_session_create = None

                self.fw_tc_match_entry = YList(self)
                self.fw_tc_proto_entry = YList(self)
                self._segment_path = lambda: "fw-traffic-class-entry" + "[class-name='" + str(self.class_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FwOperData.FwZonepairEntries.FwTrafficClassEntry, ['class_name', 'zonepair_name', 'class_action', 'pkts_counter', 'bytes_counter', 'attempted_conn', 'current_active_conn', 'max_active_conn', 'current_halfopen_conn', 'max_halfopen_conn', 'current_terminating_conn', 'max_terminating_conn', 'time_since_last_session_create'], name, value)


            class FwTcMatchEntry(Entity):
                """
                List of match conditions
                
                .. attribute:: match_name  (key)
                
                	Match Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: match_type_id  (key)
                
                	Match Type Identifier
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: match_type
                
                	Match Type
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'fw-ios-xe-oper'
                _revision = '2018-02-22'

                def __init__(self):
                    super(FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcMatchEntry, self).__init__()

                    self.yang_name = "fw-tc-match-entry"
                    self.yang_parent_name = "fw-traffic-class-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['match_name','match_type_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('match_name', (YLeaf(YType.str, 'match-name'), ['str'])),
                        ('match_type_id', (YLeaf(YType.uint8, 'match-type-id'), ['int'])),
                        ('match_type', (YLeaf(YType.str, 'match-type'), ['str'])),
                    ])
                    self.match_name = None
                    self.match_type_id = None
                    self.match_type = None
                    self._segment_path = lambda: "fw-tc-match-entry" + "[match-name='" + str(self.match_name) + "']" + "[match-type-id='" + str(self.match_type_id) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcMatchEntry, ['match_name', 'match_type_id', 'match_type'], name, value)



            class FwTcProtoEntry(Entity):
                """
                Firewall Traffic class protocol list entries
                
                .. attribute:: proto_id  (key)
                
                	Protocol ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: protocol_name
                
                	Protocol Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: byte_counters
                
                	Number of bytes matching this protocol
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pkt_counters
                
                	Number of packets matching this protocol
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'fw-ios-xe-oper'
                _revision = '2018-02-22'

                def __init__(self):
                    super(FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcProtoEntry, self).__init__()

                    self.yang_name = "fw-tc-proto-entry"
                    self.yang_parent_name = "fw-traffic-class-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['proto_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('proto_id', (YLeaf(YType.uint16, 'proto-id'), ['int'])),
                        ('protocol_name', (YLeaf(YType.str, 'protocol-name'), ['str'])),
                        ('byte_counters', (YLeaf(YType.uint64, 'byte-counters'), ['int'])),
                        ('pkt_counters', (YLeaf(YType.uint64, 'pkt-counters'), ['int'])),
                    ])
                    self.proto_id = None
                    self.protocol_name = None
                    self.byte_counters = None
                    self.pkt_counters = None
                    self._segment_path = lambda: "fw-tc-proto-entry" + "[proto-id='" + str(self.proto_id) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FwOperData.FwZonepairEntries.FwTrafficClassEntry.FwTcProtoEntry, ['proto_id', 'protocol_name', 'byte_counters', 'pkt_counters'], name, value)




    def clone_ptr(self):
        self._top_entity = FwOperData()
        return self._top_entity



