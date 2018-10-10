""" Cisco_IOS_XR_man_ipsla_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ipsla package operational data.

This module contains definitions
for the following management objects\:
  ipsla\: IPSLA operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpslaLspGrpPathStatusEnum(Enum):
    """
    IpslaLspGrpPathStatusEnum (Enum Class)

    Ipsla lsp grp path status enum

    .. data:: ipsla_lsp_grp_path_status_unknown = 0

    	ipsla lsp grp path status unknown

    .. data:: ipsla_lsp_grp_path_status_up = 1

    	ipsla lsp grp path status up

    .. data:: ipsla_lsp_grp_path_status_down = 2

    	ipsla lsp grp path status down

    .. data:: ipsla_lsp_grp_path_status_retry = 3

    	ipsla lsp grp path status retry

    .. data:: ipsla_lsp_grp_path_status_pending = 4

    	ipsla lsp grp path status pending

    """

    ipsla_lsp_grp_path_status_unknown = Enum.YLeaf(0, "ipsla-lsp-grp-path-status-unknown")

    ipsla_lsp_grp_path_status_up = Enum.YLeaf(1, "ipsla-lsp-grp-path-status-up")

    ipsla_lsp_grp_path_status_down = Enum.YLeaf(2, "ipsla-lsp-grp-path-status-down")

    ipsla_lsp_grp_path_status_retry = Enum.YLeaf(3, "ipsla-lsp-grp-path-status-retry")

    ipsla_lsp_grp_path_status_pending = Enum.YLeaf(4, "ipsla-lsp-grp-path-status-pending")


class IpslaLspGrpStatusEnum(Enum):
    """
    IpslaLspGrpStatusEnum (Enum Class)

    Ipsla lsp grp status enum

    .. data:: ipsla_lsp_grp_status_unknown = 1

    	ipsla lsp grp status unknown

    .. data:: ipsla_lsp_grp_status_up = 2

    	ipsla lsp grp status up

    .. data:: ipsla_lsp_grp_status_partial = 3

    	ipsla lsp grp status partial

    .. data:: ipsla_lsp_grp_status_down = 4

    	ipsla lsp grp status down

    .. data:: ipsla_lsp_grp_status_pending = 5

    	ipsla lsp grp status pending

    """

    ipsla_lsp_grp_status_unknown = Enum.YLeaf(1, "ipsla-lsp-grp-status-unknown")

    ipsla_lsp_grp_status_up = Enum.YLeaf(2, "ipsla-lsp-grp-status-up")

    ipsla_lsp_grp_status_partial = Enum.YLeaf(3, "ipsla-lsp-grp-status-partial")

    ipsla_lsp_grp_status_down = Enum.YLeaf(4, "ipsla-lsp-grp-status-down")

    ipsla_lsp_grp_status_pending = Enum.YLeaf(5, "ipsla-lsp-grp-status-pending")


class IpslaMplsAddDeleteEnum(Enum):
    """
    IpslaMplsAddDeleteEnum (Enum Class)

    Ipsla mpls add delete enum

    .. data:: ipsla_mpls_add_delete_add_q = 1

    	ipsla mpls add delete add q

    .. data:: ipsla_mpls_add_delete_delete_q = 2

    	ipsla mpls add delete delete q

    """

    ipsla_mpls_add_delete_add_q = Enum.YLeaf(1, "ipsla-mpls-add-delete-add-q")

    ipsla_mpls_add_delete_delete_q = Enum.YLeaf(2, "ipsla-mpls-add-delete-delete-q")


class IpslaMplsLpdDiscoveryModeEnum(Enum):
    """
    IpslaMplsLpdDiscoveryModeEnum (Enum Class)

    Ipsla mpls lpd discovery mode enum

    .. data:: ipsla_mpls_lpd_unknown = 0

    	ipsla mpls lpd unknown

    .. data:: ipsla_mpls_lpd_initial_running = 1

    	ipsla mpls lpd initial running

    .. data:: ipsla_mpls_lpd_initial_complete = 2

    	ipsla mpls lpd initial complete

    .. data:: ipsla_mpls_lpd_rediscovery_running = 3

    	ipsla mpls lpd rediscovery running

    .. data:: ipsla_mpls_lpd_rediscovery_complete = 4

    	ipsla mpls lpd rediscovery complete

    """

    ipsla_mpls_lpd_unknown = Enum.YLeaf(0, "ipsla-mpls-lpd-unknown")

    ipsla_mpls_lpd_initial_running = Enum.YLeaf(1, "ipsla-mpls-lpd-initial-running")

    ipsla_mpls_lpd_initial_complete = Enum.YLeaf(2, "ipsla-mpls-lpd-initial-complete")

    ipsla_mpls_lpd_rediscovery_running = Enum.YLeaf(3, "ipsla-mpls-lpd-rediscovery-running")

    ipsla_mpls_lpd_rediscovery_complete = Enum.YLeaf(4, "ipsla-mpls-lpd-rediscovery-complete")


class IpslaMplsLpdPathDiscoveryStatus(Enum):
    """
    IpslaMplsLpdPathDiscoveryStatus (Enum Class)

    Ipsla mpls lpd path discovery status

    .. data:: ipsla_mpls_lpd_path_discovery_unknown = 0

    	ipsla mpls lpd path discovery unknown

    .. data:: ipsla_mpls_lpd_path_discovery_ok = 1

    	ipsla mpls lpd path discovery ok

    .. data:: ipsla_mpls_lpd_path_discovery_broken = 2

    	ipsla mpls lpd path discovery broken

    .. data:: ipsla_mpls_lpd_path_discovery_unexplorable = 3

    	ipsla mpls lpd path discovery unexplorable

    """

    ipsla_mpls_lpd_path_discovery_unknown = Enum.YLeaf(0, "ipsla-mpls-lpd-path-discovery-unknown")

    ipsla_mpls_lpd_path_discovery_ok = Enum.YLeaf(1, "ipsla-mpls-lpd-path-discovery-ok")

    ipsla_mpls_lpd_path_discovery_broken = Enum.YLeaf(2, "ipsla-mpls-lpd-path-discovery-broken")

    ipsla_mpls_lpd_path_discovery_unexplorable = Enum.YLeaf(3, "ipsla-mpls-lpd-path-discovery-unexplorable")


class IpslaMplsLpdRetCode(Enum):
    """
    IpslaMplsLpdRetCode (Enum Class)

    Ipsla mpls lpd ret code

    .. data:: ipsla_mpls_lpd_ret_code_unknown = 1

    	ipsla mpls lpd ret code unknown

    .. data:: ipsla_mpls_lpd_ret_code_no_path = 2

    	ipsla mpls lpd ret code no path

    .. data:: ipsla_mpls_lpd_ret_code_all_path_broken = 3

    	ipsla mpls lpd ret code all path broken

    .. data:: ipsla_mpls_lpd_ret_code_all_path_unexplorable = 4

    	ipsla mpls lpd ret code all path unexplorable

    .. data:: ipsla_mpls_lpd_ret_code_all_path_broken_or_unexplorable = 5

    	ipsla mpls lpd ret code all path broken or

    	unexplorable

    .. data:: ipsla_mpls_lpd_ret_code_timeout = 6

    	ipsla mpls lpd ret code timeout

    .. data:: ipsla_mpls_lpd_ret_code_error = 7

    	ipsla mpls lpd ret code error

    .. data:: ipsla_mpls_lpd_ret_code_ok = 8

    	ipsla mpls lpd ret code ok

    """

    ipsla_mpls_lpd_ret_code_unknown = Enum.YLeaf(1, "ipsla-mpls-lpd-ret-code-unknown")

    ipsla_mpls_lpd_ret_code_no_path = Enum.YLeaf(2, "ipsla-mpls-lpd-ret-code-no-path")

    ipsla_mpls_lpd_ret_code_all_path_broken = Enum.YLeaf(3, "ipsla-mpls-lpd-ret-code-all-path-broken")

    ipsla_mpls_lpd_ret_code_all_path_unexplorable = Enum.YLeaf(4, "ipsla-mpls-lpd-ret-code-all-path-unexplorable")

    ipsla_mpls_lpd_ret_code_all_path_broken_or_unexplorable = Enum.YLeaf(5, "ipsla-mpls-lpd-ret-code-all-path-broken-or-unexplorable")

    ipsla_mpls_lpd_ret_code_timeout = Enum.YLeaf(6, "ipsla-mpls-lpd-ret-code-timeout")

    ipsla_mpls_lpd_ret_code_error = Enum.YLeaf(7, "ipsla-mpls-lpd-ret-code-error")

    ipsla_mpls_lpd_ret_code_ok = Enum.YLeaf(8, "ipsla-mpls-lpd-ret-code-ok")


class IpslaOperStateEnum(Enum):
    """
    IpslaOperStateEnum (Enum Class)

    Ipsla oper state enum

    .. data:: ipsla_oper_state_inactive = 0

    	ipsla oper state inactive

    .. data:: ipsla_oper_state_pending = 1

    	ipsla oper state pending

    .. data:: ipsla_oper_state_active = 2

    	ipsla oper state active

    """

    ipsla_oper_state_inactive = Enum.YLeaf(0, "ipsla-oper-state-inactive")

    ipsla_oper_state_pending = Enum.YLeaf(1, "ipsla-oper-state-pending")

    ipsla_oper_state_active = Enum.YLeaf(2, "ipsla-oper-state-active")


class IpslaRetCode(Enum):
    """
    IpslaRetCode (Enum Class)

    Ipsla ret code

    .. data:: ipsla_ret_code_unknown = 0

    	ipsla ret code unknown

    .. data:: ipsla_ret_code_ok = 1

    	ipsla ret code ok

    .. data:: ipsla_ret_code_disconnect = 2

    	ipsla ret code disconnect

    .. data:: ipsla_ret_code_over_threshold = 3

    	ipsla ret code over threshold

    .. data:: ipsla_ret_code_timeout = 4

    	ipsla ret code timeout

    .. data:: ipsla_ret_code_busy = 5

    	ipsla ret code busy

    .. data:: ipsla_ret_code_no_connection = 6

    	ipsla ret code no connection

    .. data:: ipsla_ret_code_dropped = 7

    	ipsla ret code dropped

    .. data:: ipsla_ret_code_sequence_error = 8

    	ipsla ret code sequence error

    .. data:: ipsla_ret_code_verify_error = 9

    	ipsla ret code verify error

    .. data:: ipsla_ret_code_application_specific = 10

    	ipsla ret code application specific

    .. data:: ipsla_ret_code_dns_server_timeout = 11

    	ipsla ret code dns server timeout

    .. data:: ipsla_ret_code_tcp_connect_timeout = 12

    	ipsla ret code tcp connect timeout

    .. data:: ipsla_ret_code_http_transaction_timeout = 13

    	ipsla ret code http transaction timeout

    .. data:: ipsla_ret_code_dns_query_error = 14

    	ipsla ret code dns query error

    .. data:: ipsla_ret_code_http_error = 15

    	ipsla ret code http error

    .. data:: ipsla_ret_code_internal_error = 16

    	ipsla ret code internal error

    .. data:: ipsla_ret_code_mpls_lsp_echo_tx_error = 17

    	ipsla ret code mpls lsp echo tx error

    .. data:: ipsla_ret_code_mpls_lsp_unreachable = 18

    	ipsla ret code mpls lsp unreachable

    .. data:: ipsla_ret_code_mpls_lsp_malformed_request = 19

    	ipsla ret code mpls lsp malformed request

    .. data:: ipsla_ret_code_mpls_lsp_reachable_but_not_fec = 20

    	ipsla ret code mpls lsp reachable but not fec

    .. data:: ipsla_ret_code_mpls_lsp_ds_map_mismatch = 21

    	ipsla ret code mpls lsp ds map mismatch

    .. data:: ipsla_ret_code_mpls_lsp_duplicate = 22

    	ipsla ret code mpls lsp duplicate

    .. data:: ipsla_ret_code_failure = 23

    	ipsla ret code failure

    .. data:: ipsla_ret_code_malloc_failure = 24

    	ipsla ret code malloc failure

    .. data:: ipsla_ret_code_sock_open_error = 25

    	ipsla ret code sock open error

    .. data:: ipsla_ret_code_sock_bind_error = 26

    	ipsla ret code sock bind error

    .. data:: ipsla_ret_code_sock_send_error = 27

    	ipsla ret code sock send error

    .. data:: ipsla_ret_code_sock_recv_error = 28

    	ipsla ret code sock recv error

    .. data:: ipsla_ret_code_sock_connect_error = 29

    	ipsla ret code sock connect error

    .. data:: ipsla_ret_code_sock_set_option_error = 30

    	ipsla ret code sock set option error

    .. data:: ipsla_ret_code_sock_attach_error = 31

    	ipsla ret code sock attach error

    .. data:: ipsla_ret_code_ctrl_msg_error = 32

    	ipsla ret code ctrl msg error

    .. data:: ipsla_ret_code_no_key_chain = 33

    	ipsla ret code no key chain

    .. data:: ipsla_ret_code_key_chain_lib_fail = 34

    	ipsla ret code key chain lib fail

    .. data:: ipsla_ret_code_no_key_id = 35

    	ipsla ret code no key id

    .. data:: ipsla_ret_code_invalid_key_id = 36

    	ipsla ret code invalid key id

    .. data:: ipsla_ret_code_entry_exist = 37

    	ipsla ret code entry exist

    .. data:: ipsla_ret_code_entry_not_found = 38

    	ipsla ret code entry not found

    .. data:: ipsla_ret_code_hop_over_max = 39

    	ipsla ret code hop over max

    .. data:: ipsla_ret_code_hop_dup_address = 40

    	ipsla ret code hop dup address

    .. data:: ipsla_ret_code_vrf_name_error = 41

    	ipsla ret code vrf name error

    .. data:: ipsla_ret_code_resp_failure = 42

    	ipsla ret code resp failure

    .. data:: ipsla_ret_code_auth_failure = 43

    	ipsla ret code auth failure

    .. data:: ipsla_ret_code_format_failure = 44

    	ipsla ret code format failure

    .. data:: ipsla_ret_code_port_in_use = 45

    	ipsla ret code port in use

    .. data:: ipsla_ret_code_no_route = 46

    	ipsla ret code no route

    .. data:: ipsla_ret_code_pending = 47

    	ipsla ret code pending

    .. data:: ipsla_ret_code_invalid_address = 48

    	ipsla ret code invalid address

    .. data:: ipsla_ret_code_max = 49

    	ipsla ret code max

    """

    ipsla_ret_code_unknown = Enum.YLeaf(0, "ipsla-ret-code-unknown")

    ipsla_ret_code_ok = Enum.YLeaf(1, "ipsla-ret-code-ok")

    ipsla_ret_code_disconnect = Enum.YLeaf(2, "ipsla-ret-code-disconnect")

    ipsla_ret_code_over_threshold = Enum.YLeaf(3, "ipsla-ret-code-over-threshold")

    ipsla_ret_code_timeout = Enum.YLeaf(4, "ipsla-ret-code-timeout")

    ipsla_ret_code_busy = Enum.YLeaf(5, "ipsla-ret-code-busy")

    ipsla_ret_code_no_connection = Enum.YLeaf(6, "ipsla-ret-code-no-connection")

    ipsla_ret_code_dropped = Enum.YLeaf(7, "ipsla-ret-code-dropped")

    ipsla_ret_code_sequence_error = Enum.YLeaf(8, "ipsla-ret-code-sequence-error")

    ipsla_ret_code_verify_error = Enum.YLeaf(9, "ipsla-ret-code-verify-error")

    ipsla_ret_code_application_specific = Enum.YLeaf(10, "ipsla-ret-code-application-specific")

    ipsla_ret_code_dns_server_timeout = Enum.YLeaf(11, "ipsla-ret-code-dns-server-timeout")

    ipsla_ret_code_tcp_connect_timeout = Enum.YLeaf(12, "ipsla-ret-code-tcp-connect-timeout")

    ipsla_ret_code_http_transaction_timeout = Enum.YLeaf(13, "ipsla-ret-code-http-transaction-timeout")

    ipsla_ret_code_dns_query_error = Enum.YLeaf(14, "ipsla-ret-code-dns-query-error")

    ipsla_ret_code_http_error = Enum.YLeaf(15, "ipsla-ret-code-http-error")

    ipsla_ret_code_internal_error = Enum.YLeaf(16, "ipsla-ret-code-internal-error")

    ipsla_ret_code_mpls_lsp_echo_tx_error = Enum.YLeaf(17, "ipsla-ret-code-mpls-lsp-echo-tx-error")

    ipsla_ret_code_mpls_lsp_unreachable = Enum.YLeaf(18, "ipsla-ret-code-mpls-lsp-unreachable")

    ipsla_ret_code_mpls_lsp_malformed_request = Enum.YLeaf(19, "ipsla-ret-code-mpls-lsp-malformed-request")

    ipsla_ret_code_mpls_lsp_reachable_but_not_fec = Enum.YLeaf(20, "ipsla-ret-code-mpls-lsp-reachable-but-not-fec")

    ipsla_ret_code_mpls_lsp_ds_map_mismatch = Enum.YLeaf(21, "ipsla-ret-code-mpls-lsp-ds-map-mismatch")

    ipsla_ret_code_mpls_lsp_duplicate = Enum.YLeaf(22, "ipsla-ret-code-mpls-lsp-duplicate")

    ipsla_ret_code_failure = Enum.YLeaf(23, "ipsla-ret-code-failure")

    ipsla_ret_code_malloc_failure = Enum.YLeaf(24, "ipsla-ret-code-malloc-failure")

    ipsla_ret_code_sock_open_error = Enum.YLeaf(25, "ipsla-ret-code-sock-open-error")

    ipsla_ret_code_sock_bind_error = Enum.YLeaf(26, "ipsla-ret-code-sock-bind-error")

    ipsla_ret_code_sock_send_error = Enum.YLeaf(27, "ipsla-ret-code-sock-send-error")

    ipsla_ret_code_sock_recv_error = Enum.YLeaf(28, "ipsla-ret-code-sock-recv-error")

    ipsla_ret_code_sock_connect_error = Enum.YLeaf(29, "ipsla-ret-code-sock-connect-error")

    ipsla_ret_code_sock_set_option_error = Enum.YLeaf(30, "ipsla-ret-code-sock-set-option-error")

    ipsla_ret_code_sock_attach_error = Enum.YLeaf(31, "ipsla-ret-code-sock-attach-error")

    ipsla_ret_code_ctrl_msg_error = Enum.YLeaf(32, "ipsla-ret-code-ctrl-msg-error")

    ipsla_ret_code_no_key_chain = Enum.YLeaf(33, "ipsla-ret-code-no-key-chain")

    ipsla_ret_code_key_chain_lib_fail = Enum.YLeaf(34, "ipsla-ret-code-key-chain-lib-fail")

    ipsla_ret_code_no_key_id = Enum.YLeaf(35, "ipsla-ret-code-no-key-id")

    ipsla_ret_code_invalid_key_id = Enum.YLeaf(36, "ipsla-ret-code-invalid-key-id")

    ipsla_ret_code_entry_exist = Enum.YLeaf(37, "ipsla-ret-code-entry-exist")

    ipsla_ret_code_entry_not_found = Enum.YLeaf(38, "ipsla-ret-code-entry-not-found")

    ipsla_ret_code_hop_over_max = Enum.YLeaf(39, "ipsla-ret-code-hop-over-max")

    ipsla_ret_code_hop_dup_address = Enum.YLeaf(40, "ipsla-ret-code-hop-dup-address")

    ipsla_ret_code_vrf_name_error = Enum.YLeaf(41, "ipsla-ret-code-vrf-name-error")

    ipsla_ret_code_resp_failure = Enum.YLeaf(42, "ipsla-ret-code-resp-failure")

    ipsla_ret_code_auth_failure = Enum.YLeaf(43, "ipsla-ret-code-auth-failure")

    ipsla_ret_code_format_failure = Enum.YLeaf(44, "ipsla-ret-code-format-failure")

    ipsla_ret_code_port_in_use = Enum.YLeaf(45, "ipsla-ret-code-port-in-use")

    ipsla_ret_code_no_route = Enum.YLeaf(46, "ipsla-ret-code-no-route")

    ipsla_ret_code_pending = Enum.YLeaf(47, "ipsla-ret-code-pending")

    ipsla_ret_code_invalid_address = Enum.YLeaf(48, "ipsla-ret-code-invalid-address")

    ipsla_ret_code_max = Enum.YLeaf(49, "ipsla-ret-code-max")


class IpslaTargetTypeEnum(Enum):
    """
    IpslaTargetTypeEnum (Enum Class)

    IPSLA Target Types

    .. data:: ipv4_address_target_type = 1

    	IPv4 address

    .. data:: ipv4_prefix_target_type = 2

    	IPv4 prefix

    .. data:: tunnel_id_target_type = 3

    	Tunnel ID

    .. data:: ipv4_pseudowire_target_type = 4

    	IPv4 pseudowire

    .. data:: ipv6_address_target_type = 5

    	IPv6 address

    """

    ipv4_address_target_type = Enum.YLeaf(1, "ipv4-address-target-type")

    ipv4_prefix_target_type = Enum.YLeaf(2, "ipv4-prefix-target-type")

    tunnel_id_target_type = Enum.YLeaf(3, "tunnel-id-target-type")

    ipv4_pseudowire_target_type = Enum.YLeaf(4, "ipv4-pseudowire-target-type")

    ipv6_address_target_type = Enum.YLeaf(5, "ipv6-address-target-type")


class OpTypeEnum(Enum):
    """
    OpTypeEnum (Enum Class)

    IPSLA Operation Types

    .. data:: icmp_echo = 1

    	icmp echo

    .. data:: icmp_path_jitter = 2

    	icmp path jitter

    .. data:: icmp_path_echo = 4

    	icmp path echo

    .. data:: udp_jitter = 8

    	udp jitter

    .. data:: udp_echo = 16

    	udp echo

    .. data:: mpls_lsp_ping = 32

    	mpls lsp ping

    .. data:: mpls_lsp_trace = 64

    	mpls lsp trace

    .. data:: mpls_lsp_group = 128

    	mpls lsp group

    """

    icmp_echo = Enum.YLeaf(1, "icmp-echo")

    icmp_path_jitter = Enum.YLeaf(2, "icmp-path-jitter")

    icmp_path_echo = Enum.YLeaf(4, "icmp-path-echo")

    udp_jitter = Enum.YLeaf(8, "udp-jitter")

    udp_echo = Enum.YLeaf(16, "udp-echo")

    mpls_lsp_ping = Enum.YLeaf(32, "mpls-lsp-ping")

    mpls_lsp_trace = Enum.YLeaf(64, "mpls-lsp-trace")

    mpls_lsp_group = Enum.YLeaf(128, "mpls-lsp-group")


class SlaOpTypes(Enum):
    """
    SlaOpTypes (Enum Class)

    IPSLA Operation Types

    .. data:: oper_icmp_echo = 1

    	ICMP Echo

    .. data:: oper_icmp_path_jitter = 2

    	ICMP PathJitter

    .. data:: oper_icmp_path_echo = 4

    	ICMP Path Echo

    .. data:: oper_udp_jitter = 8

    	UDP Jitter

    .. data:: oper_udp_echo = 16

    	UDP Echo

    .. data:: oper_mpls_lsp_ping = 32

    	MPLS LSP Ping

    .. data:: oper_mpls_lsp_trace = 64

    	MPLS LSP Trace

    .. data:: oper_mpls_lsp_group = 128

    	MPLS LSP Group

    """

    oper_icmp_echo = Enum.YLeaf(1, "oper-icmp-echo")

    oper_icmp_path_jitter = Enum.YLeaf(2, "oper-icmp-path-jitter")

    oper_icmp_path_echo = Enum.YLeaf(4, "oper-icmp-path-echo")

    oper_udp_jitter = Enum.YLeaf(8, "oper-udp-jitter")

    oper_udp_echo = Enum.YLeaf(16, "oper-udp-echo")

    oper_mpls_lsp_ping = Enum.YLeaf(32, "oper-mpls-lsp-ping")

    oper_mpls_lsp_trace = Enum.YLeaf(64, "oper-mpls-lsp-trace")

    oper_mpls_lsp_group = Enum.YLeaf(128, "oper-mpls-lsp-group")



class Ipsla(Entity):
    """
    IPSLA operational data
    
    .. attribute:: mpls_data
    
    	MPLS operational data
    	**type**\:  :py:class:`MplsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData>`
    
    .. attribute:: responder
    
    	Data from responder probe handling
    	**type**\:  :py:class:`Responder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.Responder>`
    
    .. attribute:: operation_data
    
    	Operations data
    	**type**\:  :py:class:`OperationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData>`
    
    .. attribute:: application_info
    
    	IPSLA application information
    	**type**\:  :py:class:`ApplicationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.ApplicationInfo>`
    
    

    """

    _prefix = 'man-ipsla-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipsla, self).__init__()
        self._top_entity = None

        self.yang_name = "ipsla"
        self.yang_parent_name = "Cisco-IOS-XR-man-ipsla-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mpls-data", ("mpls_data", Ipsla.MplsData)), ("responder", ("responder", Ipsla.Responder)), ("operation-data", ("operation_data", Ipsla.OperationData)), ("application-info", ("application_info", Ipsla.ApplicationInfo))])
        self._leafs = OrderedDict()

        self.mpls_data = Ipsla.MplsData()
        self.mpls_data.parent = self
        self._children_name_map["mpls_data"] = "mpls-data"

        self.responder = Ipsla.Responder()
        self.responder.parent = self
        self._children_name_map["responder"] = "responder"

        self.operation_data = Ipsla.OperationData()
        self.operation_data.parent = self
        self._children_name_map["operation_data"] = "operation-data"

        self.application_info = Ipsla.ApplicationInfo()
        self.application_info.parent = self
        self._children_name_map["application_info"] = "application-info"
        self._segment_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipsla, [], name, value)


    class MplsData(Entity):
        """
        MPLS operational data
        
        .. attribute:: lsp_monitors
        
        	List of MPLS LSP Monitor instances
        	**type**\:  :py:class:`LspMonitors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors>`
        
        .. attribute:: discovery
        
        	Provider Edge(PE) discovery operational data
        	**type**\:  :py:class:`Discovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery>`
        
        

        """

        _prefix = 'man-ipsla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.MplsData, self).__init__()

            self.yang_name = "mpls-data"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lsp-monitors", ("lsp_monitors", Ipsla.MplsData.LspMonitors)), ("discovery", ("discovery", Ipsla.MplsData.Discovery))])
            self._leafs = OrderedDict()

            self.lsp_monitors = Ipsla.MplsData.LspMonitors()
            self.lsp_monitors.parent = self
            self._children_name_map["lsp_monitors"] = "lsp-monitors"

            self.discovery = Ipsla.MplsData.Discovery()
            self.discovery.parent = self
            self._children_name_map["discovery"] = "discovery"
            self._segment_path = lambda: "mpls-data"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.MplsData, [], name, value)


        class LspMonitors(Entity):
            """
            List of MPLS LSP Monitor instances
            
            .. attribute:: lsp_monitor
            
            	Operational data for MPLS LSP Monitor
            	**type**\: list of  		 :py:class:`LspMonitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor>`
            
            

            """

            _prefix = 'man-ipsla-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsData.LspMonitors, self).__init__()

                self.yang_name = "lsp-monitors"
                self.yang_parent_name = "mpls-data"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("lsp-monitor", ("lsp_monitor", Ipsla.MplsData.LspMonitors.LspMonitor))])
                self._leafs = OrderedDict()

                self.lsp_monitor = YList(self)
                self._segment_path = lambda: "lsp-monitors"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsData.LspMonitors, [], name, value)


            class LspMonitor(Entity):
                """
                Operational data for MPLS LSP Monitor
                
                .. attribute:: monitor_id  (key)
                
                	Monitor ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	Operational state of MPLS LSP Monitor
                	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.State>`
                
                .. attribute:: operations
                
                	List of operations in MPLS LSP Monitor
                	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations>`
                
                .. attribute:: scan_queues
                
                	List of Scan Queue entries in MPLS LSP Monitor
                	**type**\:  :py:class:`ScanQueues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues>`
                
                

                """

                _prefix = 'man-ipsla-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.MplsData.LspMonitors.LspMonitor, self).__init__()

                    self.yang_name = "lsp-monitor"
                    self.yang_parent_name = "lsp-monitors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['monitor_id']
                    self._child_classes = OrderedDict([("state", ("state", Ipsla.MplsData.LspMonitors.LspMonitor.State)), ("operations", ("operations", Ipsla.MplsData.LspMonitors.LspMonitor.Operations)), ("scan-queues", ("scan_queues", Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues))])
                    self._leafs = OrderedDict([
                        ('monitor_id', (YLeaf(YType.uint32, 'monitor-id'), ['int'])),
                    ])
                    self.monitor_id = None

                    self.state = Ipsla.MplsData.LspMonitors.LspMonitor.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.operations = Ipsla.MplsData.LspMonitors.LspMonitor.Operations()
                    self.operations.parent = self
                    self._children_name_map["operations"] = "operations"

                    self.scan_queues = Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues()
                    self.scan_queues.parent = self
                    self._children_name_map["scan_queues"] = "scan-queues"
                    self._segment_path = lambda: "lsp-monitor" + "[monitor-id='" + str(self.monitor_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/lsp-monitors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor, ['monitor_id'], name, value)


                class State(Entity):
                    """
                    Operational state of MPLS LSP Monitor
                    
                    .. attribute:: scan_remaining
                    
                    	Number of seconds left before next scan for addition (0xffffffff means the timer is not running)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: delete_scan_remaining
                    
                    	Number of seconds left before next scan for deletion  (0xffffffff means the timer is not running)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: rediscovery_remaining
                    
                    	Number of seconds left before next path discovery (0xffffffff means the timer is not running)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: lpd_compeletion_time
                    
                    	LPD completion time (seconds) for the entire set of PEs which are discovered in this MPLSLM instance (0xffffffff means LPD is never completed yet)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsData.LspMonitors.LspMonitor.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "lsp-monitor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('scan_remaining', (YLeaf(YType.uint32, 'scan-remaining'), ['int'])),
                            ('delete_scan_remaining', (YLeaf(YType.uint32, 'delete-scan-remaining'), ['int'])),
                            ('rediscovery_remaining', (YLeaf(YType.uint32, 'rediscovery-remaining'), ['int'])),
                            ('lpd_compeletion_time', (YLeaf(YType.uint32, 'lpd-compeletion-time'), ['int'])),
                        ])
                        self.scan_remaining = None
                        self.delete_scan_remaining = None
                        self.rediscovery_remaining = None
                        self.lpd_compeletion_time = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.State, [u'scan_remaining', u'delete_scan_remaining', u'rediscovery_remaining', u'lpd_compeletion_time'], name, value)


                class Operations(Entity):
                    """
                    List of operations in MPLS LSP Monitor
                    
                    .. attribute:: operation_
                    
                    	Operation created in MPLS LSP Monitor
                    	**type**\: list of  		 :py:class:`Operation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations, self).__init__()

                        self.yang_name = "operations"
                        self.yang_parent_name = "lsp-monitor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operation", ("operation_", Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation))])
                        self._leafs = OrderedDict()

                        self.operation_ = YList(self)
                        self._segment_path = lambda: "operations"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations, [], name, value)


                    class Operation(Entity):
                        """
                        Operation created in MPLS LSP Monitor
                        
                        .. attribute:: operation_id  (key)
                        
                        	Operation ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	Operational state of the created operation
                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.State>`
                        
                        .. attribute:: lpd_paths
                        
                        	List of LPD paths in MPLS LPD group operation
                        	**type**\:  :py:class:`LpdPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation, self).__init__()

                            self.yang_name = "operation"
                            self.yang_parent_name = "operations"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['operation_id']
                            self._child_classes = OrderedDict([("state", ("state", Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.State)), ("lpd-paths", ("lpd_paths", Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths))])
                            self._leafs = OrderedDict([
                                ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                            ])
                            self.operation_id = None

                            self.state = Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.lpd_paths = Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths()
                            self.lpd_paths.parent = self
                            self._children_name_map["lpd_paths"] = "lpd-paths"
                            self._segment_path = lambda: "operation" + "[operation-id='" + str(self.operation_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation, ['operation_id'], name, value)


                        class State(Entity):
                            """
                            Operational state of the created operation
                            
                            .. attribute:: target_address
                            
                            	PE target address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: target_mask
                            
                            	PE target mask length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: group_status
                            
                            	Latest LSP group status
                            	**type**\:  :py:class:`IpslaLspGrpStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaLspGrpStatusEnum>`
                            
                            .. attribute:: operation_time
                            
                            	Latest operation time
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "operation"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('target_address', (YLeaf(YType.str, 'target-address'), ['str'])),
                                    ('target_mask', (YLeaf(YType.uint32, 'target-mask'), ['int'])),
                                    ('group_status', (YLeaf(YType.enumeration, 'group-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaLspGrpStatusEnum', '')])),
                                    ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                ])
                                self.target_address = None
                                self.target_mask = None
                                self.group_status = None
                                self.operation_time = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.State, [u'target_address', u'target_mask', u'group_status', u'operation_time'], name, value)


                        class LpdPaths(Entity):
                            """
                            List of LPD paths in MPLS LPD group
                            operation
                            
                            .. attribute:: lpd_path
                            
                            	Operational state of LPD path in MPLS LSP Group operation
                            	**type**\: list of  		 :py:class:`LpdPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths, self).__init__()

                                self.yang_name = "lpd-paths"
                                self.yang_parent_name = "operation"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lpd-path", ("lpd_path", Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath))])
                                self._leafs = OrderedDict()

                                self.lpd_path = YList(self)
                                self._segment_path = lambda: "lpd-paths"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths, [], name, value)


                            class LpdPath(Entity):
                                """
                                Operational state of LPD path in MPLS LSP
                                Group operation
                                
                                .. attribute:: path_index  (key)
                                
                                	LPD path index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: path_id
                                
                                	LPD path identifier
                                	**type**\:  :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath.PathId>`
                                
                                .. attribute:: path_status
                                
                                	Latest path status
                                	**type**\:  :py:class:`IpslaLspGrpPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaLspGrpPathStatusEnum>`
                                
                                .. attribute:: operation_time
                                
                                	Latest operation time
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: response_time
                                
                                	Latest RTT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: success_count
                                
                                	Number of path successes
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: failure_count
                                
                                	Number of path failures
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath, self).__init__()

                                    self.yang_name = "lpd-path"
                                    self.yang_parent_name = "lpd-paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['path_index']
                                    self._child_classes = OrderedDict([("path-id", ("path_id", Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath.PathId))])
                                    self._leafs = OrderedDict([
                                        ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                        ('path_status', (YLeaf(YType.enumeration, 'path-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaLspGrpPathStatusEnum', '')])),
                                        ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                        ('success_count', (YLeaf(YType.uint32, 'success-count'), ['int'])),
                                        ('failure_count', (YLeaf(YType.uint32, 'failure-count'), ['int'])),
                                    ])
                                    self.path_index = None
                                    self.path_status = None
                                    self.operation_time = None
                                    self.response_time = None
                                    self.success_count = None
                                    self.failure_count = None

                                    self.path_id = Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath.PathId()
                                    self.path_id.parent = self
                                    self._children_name_map["path_id"] = "path-id"
                                    self._segment_path = lambda: "lpd-path" + "[path-index='" + str(self.path_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath, ['path_index', u'path_status', u'operation_time', u'response_time', u'success_count', u'failure_count'], name, value)


                                class PathId(Entity):
                                    """
                                    LPD path identifier
                                    
                                    .. attribute:: lsp_selector
                                    
                                    	LSP selector
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: output_interface
                                    
                                    	Output interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: nexthop_address
                                    
                                    	Nexthop address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: downstream_label
                                    
                                    	Downstream label stacks
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath.PathId, self).__init__()

                                        self.yang_name = "path-id"
                                        self.yang_parent_name = "lpd-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                            ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                            ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                            ('downstream_label', (YLeafList(YType.uint32, 'downstream-label'), ['int'])),
                                        ])
                                        self.lsp_selector = None
                                        self.output_interface = None
                                        self.nexthop_address = None
                                        self.downstream_label = []
                                        self._segment_path = lambda: "path-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.Operations.Operation.LpdPaths.LpdPath.PathId, [u'lsp_selector', u'output_interface', u'nexthop_address', u'downstream_label'], name, value)


                class ScanQueues(Entity):
                    """
                    List of Scan Queue entries in MPLS LSP
                    Monitor
                    
                    .. attribute:: scan_queue
                    
                    	Provider Edge(PE) addition or deletion requests in Scan Queue
                    	**type**\: list of  		 :py:class:`ScanQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues.ScanQueue>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues, self).__init__()

                        self.yang_name = "scan-queues"
                        self.yang_parent_name = "lsp-monitor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("scan-queue", ("scan_queue", Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues.ScanQueue))])
                        self._leafs = OrderedDict()

                        self.scan_queue = YList(self)
                        self._segment_path = lambda: "scan-queues"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues, [], name, value)


                    class ScanQueue(Entity):
                        """
                        Provider Edge(PE) addition or deletion
                        requests in Scan Queue
                        
                        .. attribute:: address  (key)
                        
                        	Nexthop Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: target_address
                        
                        	PE target address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: target_mask
                        
                        	PE target mask length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: entry
                        
                        	PE addition or deletion
                        	**type**\:  :py:class:`IpslaMplsAddDeleteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsAddDeleteEnum>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues.ScanQueue, self).__init__()

                            self.yang_name = "scan-queue"
                            self.yang_parent_name = "scan-queues"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('target_address', (YLeaf(YType.str, 'target-address'), ['str'])),
                                ('target_mask', (YLeaf(YType.uint32, 'target-mask'), ['int'])),
                                ('entry', (YLeaf(YType.enumeration, 'entry'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsAddDeleteEnum', '')])),
                            ])
                            self.address = None
                            self.target_address = None
                            self.target_mask = None
                            self.entry = None
                            self._segment_path = lambda: "scan-queue" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsData.LspMonitors.LspMonitor.ScanQueues.ScanQueue, ['address', u'target_address', u'target_mask', u'entry'], name, value)


        class Discovery(Entity):
            """
            Provider Edge(PE) discovery operational data
            
            .. attribute:: vpn
            
            	L3 VPN PE discovery operational data
            	**type**\:  :py:class:`Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn>`
            
            

            """

            _prefix = 'man-ipsla-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsData.Discovery, self).__init__()

                self.yang_name = "discovery"
                self.yang_parent_name = "mpls-data"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vpn", ("vpn", Ipsla.MplsData.Discovery.Vpn))])
                self._leafs = OrderedDict()

                self.vpn = Ipsla.MplsData.Discovery.Vpn()
                self.vpn.parent = self
                self._children_name_map["vpn"] = "vpn"
                self._segment_path = lambda: "discovery"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsData.Discovery, [], name, value)


            class Vpn(Entity):
                """
                L3 VPN PE discovery operational data
                
                .. attribute:: state
                
                	Operational state of PE discovery
                	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.State>`
                
                .. attribute:: nexthops
                
                	List of nexthop addresses for remote PE routers
                	**type**\:  :py:class:`Nexthops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.Nexthops>`
                
                

                """

                _prefix = 'man-ipsla-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.MplsData.Discovery.Vpn, self).__init__()

                    self.yang_name = "vpn"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("state", ("state", Ipsla.MplsData.Discovery.Vpn.State)), ("nexthops", ("nexthops", Ipsla.MplsData.Discovery.Vpn.Nexthops))])
                    self._leafs = OrderedDict()

                    self.state = Ipsla.MplsData.Discovery.Vpn.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.nexthops = Ipsla.MplsData.Discovery.Vpn.Nexthops()
                    self.nexthops.parent = self
                    self._children_name_map["nexthops"] = "nexthops"
                    self._segment_path = lambda: "vpn"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/discovery/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.MplsData.Discovery.Vpn, [], name, value)


                class State(Entity):
                    """
                    Operational state of PE discovery
                    
                    .. attribute:: refresh_remaining
                    
                    	Number of seconds left before next refresh
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsData.Discovery.Vpn.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "vpn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('refresh_remaining', (YLeaf(YType.uint32, 'refresh-remaining'), ['int'])),
                        ])
                        self.refresh_remaining = None
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/discovery/vpn/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.State, [u'refresh_remaining'], name, value)


                class Nexthops(Entity):
                    """
                    List of nexthop addresses for remote PE
                    routers
                    
                    .. attribute:: nexthop
                    
                    	Nexthop address for remote PE router
                    	**type**\: list of  		 :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsData.Discovery.Vpn.Nexthops, self).__init__()

                        self.yang_name = "nexthops"
                        self.yang_parent_name = "vpn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("nexthop", ("nexthop", Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop))])
                        self._leafs = OrderedDict()

                        self.nexthop = YList(self)
                        self._segment_path = lambda: "nexthops"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/discovery/vpn/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.Nexthops, [], name, value)


                    class Nexthop(Entity):
                        """
                        Nexthop address for remote PE router
                        
                        .. attribute:: address  (key)
                        
                        	Nexthop Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrfs
                        
                        	List of VRFs for the nexthop address
                        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs>`
                        
                        .. attribute:: prefix
                        
                        	Prefix of the nexthop address
                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Prefix>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop, self).__init__()

                            self.yang_name = "nexthop"
                            self.yang_parent_name = "nexthops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs)), ("prefix", ("prefix", Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Prefix))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.vrfs = Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"

                            self.prefix = Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Prefix()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"
                            self._segment_path = lambda: "nexthop" + "[address='" + str(self.address) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/mpls-data/discovery/vpn/nexthops/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop, ['address'], name, value)


                        class Vrfs(Entity):
                            """
                            List of VRFs for the nexthop address
                            
                            .. attribute:: vrf
                            
                            	VRF information of the nexthop address
                            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "nexthop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("vrf", ("vrf", Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs.Vrf))])
                                self._leafs = OrderedDict()

                                self.vrf = YList(self)
                                self._segment_path = lambda: "vrfs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs, [], name, value)


                            class Vrf(Entity):
                                """
                                VRF information of the nexthop address
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: prefix_count
                                
                                	Number of prefixes in VRF
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('prefix_count', (YLeaf(YType.uint32, 'prefix-count'), ['int'])),
                                    ])
                                    self.vrf_name = None
                                    self.prefix_count = None
                                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Vrfs.Vrf, ['vrf_name', u'prefix_count'], name, value)


                        class Prefix(Entity):
                            """
                            Prefix of the nexthop address
                            
                            .. attribute:: target_address
                            
                            	PE target address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: target_mask
                            
                            	PE target mask length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Prefix, self).__init__()

                                self.yang_name = "prefix"
                                self.yang_parent_name = "nexthop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('target_address', (YLeaf(YType.str, 'target-address'), ['str'])),
                                    ('target_mask', (YLeaf(YType.uint32, 'target-mask'), ['int'])),
                                ])
                                self.target_address = None
                                self.target_mask = None
                                self._segment_path = lambda: "prefix"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsData.Discovery.Vpn.Nexthops.Nexthop.Prefix, [u'target_address', u'target_mask'], name, value)


    class Responder(Entity):
        """
        Data from responder probe handling
        
        .. attribute:: ports
        
        	Statistics maintained by responder
        	**type**\:  :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.Responder.Ports>`
        
        

        """

        _prefix = 'man-ipsla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.Responder, self).__init__()

            self.yang_name = "responder"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ports", ("ports", Ipsla.Responder.Ports))])
            self._leafs = OrderedDict()

            self.ports = Ipsla.Responder.Ports()
            self.ports.parent = self
            self._children_name_map["ports"] = "ports"
            self._segment_path = lambda: "responder"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.Responder, [], name, value)


        class Ports(Entity):
            """
            Statistics maintained by responder
            
            .. attribute:: port
            
            	Port data
            	**type**\: list of  		 :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.Responder.Ports.Port>`
            
            

            """

            _prefix = 'man-ipsla-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Responder.Ports, self).__init__()

                self.yang_name = "ports"
                self.yang_parent_name = "responder"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("port", ("port", Ipsla.Responder.Ports.Port))])
                self._leafs = OrderedDict()

                self.port = YList(self)
                self._segment_path = lambda: "ports"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/responder/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Responder.Ports, [], name, value)


            class Port(Entity):
                """
                Port data
                
                .. attribute:: port  (key)
                
                	Port
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: port_xr
                
                	Port on which Responder is listening
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: local_address
                
                	IP address of Responder
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: num_probes
                
                	Number of probes received from remote end
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ctrl_probes
                
                	Number of control probes received from remote end
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: permanent
                
                	Port type if this is permanent or dynamic port
                	**type**\: bool
                
                .. attribute:: discard_on
                
                	Current discard socket option flag for the port
                	**type**\: bool
                
                .. attribute:: pd_time_stamp_failed
                
                	PD Timestamp failure
                	**type**\: bool
                
                .. attribute:: is_ipsla
                
                	IPSLA or TWAMP protocol
                	**type**\: bool
                
                .. attribute:: drop_counter
                
                	Drop counter for the Responder port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: socket
                
                	Socket
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: sender
                
                	List of senders
                	**type**\: list of  		 :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.Responder.Ports.Port.Sender>`
                
                

                """

                _prefix = 'man-ipsla-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Responder.Ports.Port, self).__init__()

                    self.yang_name = "port"
                    self.yang_parent_name = "ports"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['port']
                    self._child_classes = OrderedDict([("sender", ("sender", Ipsla.Responder.Ports.Port.Sender))])
                    self._leafs = OrderedDict([
                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ('port_xr', (YLeaf(YType.uint16, 'port-xr'), ['int'])),
                        ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                        ('num_probes', (YLeaf(YType.uint32, 'num-probes'), ['int'])),
                        ('ctrl_probes', (YLeaf(YType.uint32, 'ctrl-probes'), ['int'])),
                        ('permanent', (YLeaf(YType.boolean, 'permanent'), ['bool'])),
                        ('discard_on', (YLeaf(YType.boolean, 'discard-on'), ['bool'])),
                        ('pd_time_stamp_failed', (YLeaf(YType.boolean, 'pd-time-stamp-failed'), ['bool'])),
                        ('is_ipsla', (YLeaf(YType.boolean, 'is-ipsla'), ['bool'])),
                        ('drop_counter', (YLeaf(YType.uint32, 'drop-counter'), ['int'])),
                        ('socket', (YLeaf(YType.int32, 'socket'), ['int'])),
                    ])
                    self.port = None
                    self.port_xr = None
                    self.local_address = None
                    self.num_probes = None
                    self.ctrl_probes = None
                    self.permanent = None
                    self.discard_on = None
                    self.pd_time_stamp_failed = None
                    self.is_ipsla = None
                    self.drop_counter = None
                    self.socket = None

                    self.sender = YList(self)
                    self._segment_path = lambda: "port" + "[port='" + str(self.port) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/responder/ports/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Responder.Ports.Port, ['port', u'port_xr', u'local_address', u'num_probes', u'ctrl_probes', u'permanent', u'discard_on', u'pd_time_stamp_failed', u'is_ipsla', u'drop_counter', u'socket'], name, value)


                class Sender(Entity):
                    """
                    List of senders
                    
                    .. attribute:: ip_address
                    
                    	IP address of Sender
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port
                    
                    	Port on which Sender is sending
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: last_recv_time
                    
                    	Last received time
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.Responder.Ports.Port.Sender, self).__init__()

                        self.yang_name = "sender"
                        self.yang_parent_name = "port"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.uint32, 'ip-address'), ['int'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                            ('last_recv_time', (YLeaf(YType.uint64, 'last-recv-time'), ['int'])),
                        ])
                        self.ip_address = None
                        self.port = None
                        self.last_recv_time = None
                        self._segment_path = lambda: "sender"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.Responder.Ports.Port.Sender, [u'ip_address', u'port', u'last_recv_time'], name, value)


    class OperationData(Entity):
        """
        Operations data
        
        .. attribute:: operations
        
        	Configured operations
        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations>`
        
        

        """

        _prefix = 'man-ipsla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.OperationData, self).__init__()

            self.yang_name = "operation-data"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("operations", ("operations", Ipsla.OperationData.Operations))])
            self._leafs = OrderedDict()

            self.operations = Ipsla.OperationData.Operations()
            self.operations.parent = self
            self._children_name_map["operations"] = "operations"
            self._segment_path = lambda: "operation-data"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.OperationData, [], name, value)


        class Operations(Entity):
            """
            Configured operations
            
            .. attribute:: operation_
            
            	Operational data for an operation
            	**type**\: list of  		 :py:class:`Operation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation>`
            
            

            """

            _prefix = 'man-ipsla-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.OperationData.Operations, self).__init__()

                self.yang_name = "operations"
                self.yang_parent_name = "operation-data"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("operation", ("operation_", Ipsla.OperationData.Operations.Operation))])
                self._leafs = OrderedDict()

                self.operation_ = YList(self)
                self._segment_path = lambda: "operations"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/operation-data/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.OperationData.Operations, [], name, value)


            class Operation(Entity):
                """
                Operational data for an operation
                
                .. attribute:: operation_id  (key)
                
                	Operation ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: common
                
                	Common data for all operation types
                	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Common>`
                
                .. attribute:: lpd
                
                	LPD operational data of MPLS LSP group operation
                	**type**\:  :py:class:`Lpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd>`
                
                .. attribute:: history
                
                	Historical data for an operation
                	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History>`
                
                .. attribute:: statistics
                
                	Statistics collected for an operation
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics>`
                
                

                """

                _prefix = 'man-ipsla-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.OperationData.Operations.Operation, self).__init__()

                    self.yang_name = "operation"
                    self.yang_parent_name = "operations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['operation_id']
                    self._child_classes = OrderedDict([("common", ("common", Ipsla.OperationData.Operations.Operation.Common)), ("lpd", ("lpd", Ipsla.OperationData.Operations.Operation.Lpd)), ("history", ("history", Ipsla.OperationData.Operations.Operation.History)), ("statistics", ("statistics", Ipsla.OperationData.Operations.Operation.Statistics))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                    ])
                    self.operation_id = None

                    self.common = Ipsla.OperationData.Operations.Operation.Common()
                    self.common.parent = self
                    self._children_name_map["common"] = "common"

                    self.lpd = Ipsla.OperationData.Operations.Operation.Lpd()
                    self.lpd.parent = self
                    self._children_name_map["lpd"] = "lpd"

                    self.history = Ipsla.OperationData.Operations.Operation.History()
                    self.history.parent = self
                    self._children_name_map["history"] = "history"

                    self.statistics = Ipsla.OperationData.Operations.Operation.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "operation" + "[operation-id='" + str(self.operation_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/operation-data/operations/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.OperationData.Operations.Operation, ['operation_id'], name, value)


                class Common(Entity):
                    """
                    Common data for all operation types
                    
                    .. attribute:: operational_state
                    
                    	Operational state for an operation
                    	**type**\:  :py:class:`OperationalState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Common.OperationalState>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.OperationData.Operations.Operation.Common, self).__init__()

                        self.yang_name = "common"
                        self.yang_parent_name = "operation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operational-state", ("operational_state", Ipsla.OperationData.Operations.Operation.Common.OperationalState))])
                        self._leafs = OrderedDict()

                        self.operational_state = Ipsla.OperationData.Operations.Operation.Common.OperationalState()
                        self.operational_state.parent = self
                        self._children_name_map["operational_state"] = "operational-state"
                        self._segment_path = lambda: "common"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Common, [], name, value)


                    class OperationalState(Entity):
                        """
                        Operational state for an operation
                        
                        .. attribute:: modification_time
                        
                        	Last modification time of the operation expressed in msec since 00\:00\:00 UTC, January 1, 1970
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: start_time
                        
                        	Last start time of the operation expressedin msec since 00\:00\:00 UTC, January 1, 1970
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: attempt_count
                        
                        	Number of data collection attempts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped_count
                        
                        	Number of data collection cycles skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: life_remaining
                        
                        	Number of seconds left in current life
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: frequency
                        
                        	Number of configured frequency Default 60 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recurring
                        
                        	For recurring operation configured
                        	**type**\: bool
                        
                        .. attribute:: operational_state
                        
                        	Operational state
                        	**type**\:  :py:class:`IpslaOperStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaOperStateEnum>`
                        
                        .. attribute:: flags
                        
                        	Internal flags
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_port
                        
                        	Cached local port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: unexpected_packets
                        
                        	Unexpected probe pkts punted from LPTS
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_control_packets
                        
                        	Unexpected control pkts puntedfrom LPTS
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operation_time
                        
                        	Start time of current instance of the operation
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.Common.OperationalState, self).__init__()

                            self.yang_name = "operational-state"
                            self.yang_parent_name = "common"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('modification_time', (YLeaf(YType.uint64, 'modification-time'), ['int'])),
                                ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                ('attempt_count', (YLeaf(YType.uint32, 'attempt-count'), ['int'])),
                                ('skipped_count', (YLeaf(YType.uint32, 'skipped-count'), ['int'])),
                                ('life_remaining', (YLeaf(YType.uint32, 'life-remaining'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('recurring', (YLeaf(YType.boolean, 'recurring'), ['bool'])),
                                ('operational_state', (YLeaf(YType.enumeration, 'operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaOperStateEnum', '')])),
                                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                                ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                                ('unexpected_packets', (YLeaf(YType.uint32, 'unexpected-packets'), ['int'])),
                                ('unexpected_control_packets', (YLeaf(YType.uint32, 'unexpected-control-packets'), ['int'])),
                                ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                            ])
                            self.modification_time = None
                            self.start_time = None
                            self.attempt_count = None
                            self.skipped_count = None
                            self.life_remaining = None
                            self.frequency = None
                            self.recurring = None
                            self.operational_state = None
                            self.flags = None
                            self.local_port = None
                            self.unexpected_packets = None
                            self.unexpected_control_packets = None
                            self.operation_time = None
                            self._segment_path = lambda: "operational-state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Common.OperationalState, [u'modification_time', u'start_time', u'attempt_count', u'skipped_count', u'life_remaining', u'frequency', u'recurring', u'operational_state', u'flags', u'local_port', u'unexpected_packets', u'unexpected_control_packets', u'operation_time'], name, value)


                class Lpd(Entity):
                    """
                    LPD operational data of MPLS LSP group
                    operation
                    
                    .. attribute:: statistics
                    
                    	Statistics collected for LPD group
                    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics>`
                    
                    .. attribute:: status
                    
                    	Operational status of LPD group
                    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.OperationData.Operations.Operation.Lpd, self).__init__()

                        self.yang_name = "lpd"
                        self.yang_parent_name = "operation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("statistics", ("statistics", Ipsla.OperationData.Operations.Operation.Lpd.Statistics)), ("status", ("status", Ipsla.OperationData.Operations.Operation.Lpd.Status))])
                        self._leafs = OrderedDict()

                        self.statistics = Ipsla.OperationData.Operations.Operation.Lpd.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"

                        self.status = Ipsla.OperationData.Operations.Operation.Lpd.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                        self._segment_path = lambda: "lpd"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd, [], name, value)


                    class Statistics(Entity):
                        """
                        Statistics collected for LPD group
                        
                        .. attribute:: latest
                        
                        	LPD statistics collected during the last sampling cycle
                        	**type**\:  :py:class:`Latest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest>`
                        
                        .. attribute:: aggregated
                        
                        	Statistics aggregated for LPD group collected over time intervals
                        	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "lpd"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("latest", ("latest", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest)), ("aggregated", ("aggregated", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated))])
                            self._leafs = OrderedDict()

                            self.latest = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest()
                            self.latest.parent = self
                            self._children_name_map["latest"] = "latest"

                            self.aggregated = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated()
                            self.aggregated.parent = self
                            self._children_name_map["aggregated"] = "aggregated"
                            self._segment_path = lambda: "statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics, [], name, value)


                        class Latest(Entity):
                            """
                            LPD statistics collected during the last
                            sampling cycle
                            
                            .. attribute:: target
                            
                            	Latest statistics of LPD group
                            	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest, self).__init__()

                                self.yang_name = "latest"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("target", ("target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target))])
                                self._leafs = OrderedDict()

                                self.target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target()
                                self.target.parent = self
                                self._children_name_map["target"] = "target"
                                self._segment_path = lambda: "latest"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest, [], name, value)


                            class Target(Entity):
                                """
                                Latest statistics of LPD group
                                
                                .. attribute:: target_address
                                
                                	LPD target
                                	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress>`
                                
                                .. attribute:: start_time
                                
                                	LPD start time
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: return_code
                                
                                	LPD return code
                                	**type**\:  :py:class:`IpslaMplsLpdRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsLpdRetCode>`
                                
                                .. attribute:: completion_time_count
                                
                                	Number of CompT samples
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: completion_time
                                
                                	LPD Completion time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: min_completion_time
                                
                                	Minimum CompT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_completion_time
                                
                                	Maximum CompT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sum_completion_time
                                
                                	Sum of CompT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: path_count
                                
                                	Number of paths
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: min_path_count
                                
                                	Minimum number of paths
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_path_count
                                
                                	Maximum number of paths
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ok_count
                                
                                	Number of successes
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_path_count
                                
                                	Number of failures due to no path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: all_paths_broken_count
                                
                                	Number of failures due to all paths broken
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: all_paths_unexplorable_count
                                
                                	Number of failures due to all paths unexplorable
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: all_paths_broken_or_unexplorable_count
                                
                                	Number of failures due to all paths broken or unexplorable
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: timeout_count
                                
                                	Number of failures due to timeout
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: internal_error_count
                                
                                	Number of failures due to internal error
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_count
                                
                                	Number of failures due to unknown cause
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target, self).__init__()

                                    self.yang_name = "target"
                                    self.yang_parent_name = "latest"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress))])
                                    self._leafs = OrderedDict([
                                        ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                        ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsLpdRetCode', '')])),
                                        ('completion_time_count', (YLeaf(YType.uint32, 'completion-time-count'), ['int'])),
                                        ('completion_time', (YLeaf(YType.uint32, 'completion-time'), ['int'])),
                                        ('min_completion_time', (YLeaf(YType.uint32, 'min-completion-time'), ['int'])),
                                        ('max_completion_time', (YLeaf(YType.uint32, 'max-completion-time'), ['int'])),
                                        ('sum_completion_time', (YLeaf(YType.uint32, 'sum-completion-time'), ['int'])),
                                        ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                                        ('min_path_count', (YLeaf(YType.uint32, 'min-path-count'), ['int'])),
                                        ('max_path_count', (YLeaf(YType.uint32, 'max-path-count'), ['int'])),
                                        ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                        ('no_path_count', (YLeaf(YType.uint32, 'no-path-count'), ['int'])),
                                        ('all_paths_broken_count', (YLeaf(YType.uint32, 'all-paths-broken-count'), ['int'])),
                                        ('all_paths_unexplorable_count', (YLeaf(YType.uint32, 'all-paths-unexplorable-count'), ['int'])),
                                        ('all_paths_broken_or_unexplorable_count', (YLeaf(YType.uint32, 'all-paths-broken-or-unexplorable-count'), ['int'])),
                                        ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                        ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                        ('unknown_count', (YLeaf(YType.uint32, 'unknown-count'), ['int'])),
                                    ])
                                    self.start_time = None
                                    self.return_code = None
                                    self.completion_time_count = None
                                    self.completion_time = None
                                    self.min_completion_time = None
                                    self.max_completion_time = None
                                    self.sum_completion_time = None
                                    self.path_count = None
                                    self.min_path_count = None
                                    self.max_path_count = None
                                    self.ok_count = None
                                    self.no_path_count = None
                                    self.all_paths_broken_count = None
                                    self.all_paths_unexplorable_count = None
                                    self.all_paths_broken_or_unexplorable_count = None
                                    self.timeout_count = None
                                    self.internal_error_count = None
                                    self.unknown_count = None

                                    self.target_address = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress()
                                    self.target_address.parent = self
                                    self._children_name_map["target_address"] = "target-address"
                                    self._segment_path = lambda: "target"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target, [u'start_time', u'return_code', u'completion_time_count', u'completion_time', u'min_completion_time', u'max_completion_time', u'sum_completion_time', u'path_count', u'min_path_count', u'max_path_count', u'ok_count', u'no_path_count', u'all_paths_broken_count', u'all_paths_unexplorable_count', u'all_paths_broken_or_unexplorable_count', u'timeout_count', u'internal_error_count', u'unknown_count'], name, value)


                                class TargetAddress(Entity):
                                    """
                                    LPD target
                                    
                                    .. attribute:: ipv4_prefix_target
                                    
                                    	IPv4 prefix target
                                    	**type**\:  :py:class:`Ipv4PrefixTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PrefixTarget>`
                                    
                                    .. attribute:: tunnel_id_target
                                    
                                    	Tunnel ID target
                                    	**type**\:  :py:class:`TunnelIdTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.TunnelIdTarget>`
                                    
                                    .. attribute:: ipv4_pseudowire_target
                                    
                                    	IPv4 pseudowire target
                                    	**type**\:  :py:class:`Ipv4PseudowireTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PseudowireTarget>`
                                    
                                    .. attribute:: target_type
                                    
                                    	TargetType
                                    	**type**\:  :py:class:`IpslaTargetTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaTargetTypeEnum>`
                                    
                                    .. attribute:: ipv4_address_target
                                    
                                    	IPv4 address target
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address_target
                                    
                                    	IPv6 address target
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress, self).__init__()

                                        self.yang_name = "target-address"
                                        self.yang_parent_name = "target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("ipv4-prefix-target", ("ipv4_prefix_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PrefixTarget)), ("tunnel-id-target", ("tunnel_id_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.TunnelIdTarget)), ("ipv4-pseudowire-target", ("ipv4_pseudowire_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PseudowireTarget))])
                                        self._leafs = OrderedDict([
                                            ('target_type', (YLeaf(YType.enumeration, 'target-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaTargetTypeEnum', '')])),
                                            ('ipv4_address_target', (YLeaf(YType.str, 'ipv4-address-target'), ['str'])),
                                            ('ipv6_address_target', (YLeaf(YType.str, 'ipv6-address-target'), ['str'])),
                                        ])
                                        self.target_type = None
                                        self.ipv4_address_target = None
                                        self.ipv6_address_target = None

                                        self.ipv4_prefix_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PrefixTarget()
                                        self.ipv4_prefix_target.parent = self
                                        self._children_name_map["ipv4_prefix_target"] = "ipv4-prefix-target"

                                        self.tunnel_id_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.TunnelIdTarget()
                                        self.tunnel_id_target.parent = self
                                        self._children_name_map["tunnel_id_target"] = "tunnel-id-target"

                                        self.ipv4_pseudowire_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PseudowireTarget()
                                        self.ipv4_pseudowire_target.parent = self
                                        self._children_name_map["ipv4_pseudowire_target"] = "ipv4-pseudowire-target"
                                        self._segment_path = lambda: "target-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress, [u'target_type', u'ipv4_address_target', u'ipv6_address_target'], name, value)


                                    class Ipv4PrefixTarget(Entity):
                                        """
                                        IPv4 prefix target
                                        
                                        .. attribute:: address
                                        
                                        	IPv4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: mask_length
                                        
                                        	Mask length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PrefixTarget, self).__init__()

                                            self.yang_name = "ipv4-prefix-target"
                                            self.yang_parent_name = "target-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ('mask_length', (YLeaf(YType.uint8, 'mask-length'), ['int'])),
                                            ])
                                            self.address = None
                                            self.mask_length = None
                                            self._segment_path = lambda: "ipv4-prefix-target"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PrefixTarget, [u'address', u'mask_length'], name, value)


                                    class TunnelIdTarget(Entity):
                                        """
                                        Tunnel ID target
                                        
                                        .. attribute:: tunnel_id
                                        
                                        	Tunnel ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.TunnelIdTarget, self).__init__()

                                            self.yang_name = "tunnel-id-target"
                                            self.yang_parent_name = "target-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                            ])
                                            self.tunnel_id = None
                                            self._segment_path = lambda: "tunnel-id-target"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.TunnelIdTarget, [u'tunnel_id'], name, value)


                                    class Ipv4PseudowireTarget(Entity):
                                        """
                                        IPv4 pseudowire target
                                        
                                        .. attribute:: address
                                        
                                        	IPv4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: virtual_circuit_id
                                        
                                        	Virtual circuit ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PseudowireTarget, self).__init__()

                                            self.yang_name = "ipv4-pseudowire-target"
                                            self.yang_parent_name = "target-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ('virtual_circuit_id', (YLeaf(YType.uint32, 'virtual-circuit-id'), ['int'])),
                                            ])
                                            self.address = None
                                            self.virtual_circuit_id = None
                                            self._segment_path = lambda: "ipv4-pseudowire-target"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Latest.Target.TargetAddress.Ipv4PseudowireTarget, [u'address', u'virtual_circuit_id'], name, value)


                        class Aggregated(Entity):
                            """
                            Statistics aggregated for LPD group
                            collected over time intervals
                            
                            .. attribute:: hours
                            
                            	Table of LPD statistics aggregated over 1\-hour intervals
                            	**type**\:  :py:class:`Hours <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated, self).__init__()

                                self.yang_name = "aggregated"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("hours", ("hours", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours))])
                                self._leafs = OrderedDict()

                                self.hours = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours()
                                self.hours.parent = self
                                self._children_name_map["hours"] = "hours"
                                self._segment_path = lambda: "aggregated"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated, [], name, value)


                            class Hours(Entity):
                                """
                                Table of LPD statistics aggregated over
                                1\-hour intervals
                                
                                .. attribute:: hour
                                
                                	LPD statistics aggregated for a 1\-hour interval
                                	**type**\: list of  		 :py:class:`Hour <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours, self).__init__()

                                    self.yang_name = "hours"
                                    self.yang_parent_name = "aggregated"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("hour", ("hour", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour))])
                                    self._leafs = OrderedDict()

                                    self.hour = YList(self)
                                    self._segment_path = lambda: "hours"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours, [], name, value)


                                class Hour(Entity):
                                    """
                                    LPD statistics aggregated for a 1\-hour
                                    interval
                                    
                                    .. attribute:: hour_index  (key)
                                    
                                    	Hour Index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: target_address
                                    
                                    	LPD target
                                    	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress>`
                                    
                                    .. attribute:: start_time
                                    
                                    	LPD start time
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: return_code
                                    
                                    	LPD return code
                                    	**type**\:  :py:class:`IpslaMplsLpdRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsLpdRetCode>`
                                    
                                    .. attribute:: completion_time_count
                                    
                                    	Number of CompT samples
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: completion_time
                                    
                                    	LPD Completion time
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: min_completion_time
                                    
                                    	Minimum CompT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: max_completion_time
                                    
                                    	Maximum CompT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sum_completion_time
                                    
                                    	Sum of CompT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: path_count
                                    
                                    	Number of paths
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: min_path_count
                                    
                                    	Minimum number of paths
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: max_path_count
                                    
                                    	Maximum number of paths
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ok_count
                                    
                                    	Number of successes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: no_path_count
                                    
                                    	Number of failures due to no path
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: all_paths_broken_count
                                    
                                    	Number of failures due to all paths broken
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: all_paths_unexplorable_count
                                    
                                    	Number of failures due to all paths unexplorable
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: all_paths_broken_or_unexplorable_count
                                    
                                    	Number of failures due to all paths broken or unexplorable
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: timeout_count
                                    
                                    	Number of failures due to timeout
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: internal_error_count
                                    
                                    	Number of failures due to internal error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: unknown_count
                                    
                                    	Number of failures due to unknown cause
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour, self).__init__()

                                        self.yang_name = "hour"
                                        self.yang_parent_name = "hours"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['hour_index']
                                        self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress))])
                                        self._leafs = OrderedDict([
                                            ('hour_index', (YLeaf(YType.uint32, 'hour-index'), ['int'])),
                                            ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                            ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsLpdRetCode', '')])),
                                            ('completion_time_count', (YLeaf(YType.uint32, 'completion-time-count'), ['int'])),
                                            ('completion_time', (YLeaf(YType.uint32, 'completion-time'), ['int'])),
                                            ('min_completion_time', (YLeaf(YType.uint32, 'min-completion-time'), ['int'])),
                                            ('max_completion_time', (YLeaf(YType.uint32, 'max-completion-time'), ['int'])),
                                            ('sum_completion_time', (YLeaf(YType.uint32, 'sum-completion-time'), ['int'])),
                                            ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                                            ('min_path_count', (YLeaf(YType.uint32, 'min-path-count'), ['int'])),
                                            ('max_path_count', (YLeaf(YType.uint32, 'max-path-count'), ['int'])),
                                            ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                            ('no_path_count', (YLeaf(YType.uint32, 'no-path-count'), ['int'])),
                                            ('all_paths_broken_count', (YLeaf(YType.uint32, 'all-paths-broken-count'), ['int'])),
                                            ('all_paths_unexplorable_count', (YLeaf(YType.uint32, 'all-paths-unexplorable-count'), ['int'])),
                                            ('all_paths_broken_or_unexplorable_count', (YLeaf(YType.uint32, 'all-paths-broken-or-unexplorable-count'), ['int'])),
                                            ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                            ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                            ('unknown_count', (YLeaf(YType.uint32, 'unknown-count'), ['int'])),
                                        ])
                                        self.hour_index = None
                                        self.start_time = None
                                        self.return_code = None
                                        self.completion_time_count = None
                                        self.completion_time = None
                                        self.min_completion_time = None
                                        self.max_completion_time = None
                                        self.sum_completion_time = None
                                        self.path_count = None
                                        self.min_path_count = None
                                        self.max_path_count = None
                                        self.ok_count = None
                                        self.no_path_count = None
                                        self.all_paths_broken_count = None
                                        self.all_paths_unexplorable_count = None
                                        self.all_paths_broken_or_unexplorable_count = None
                                        self.timeout_count = None
                                        self.internal_error_count = None
                                        self.unknown_count = None

                                        self.target_address = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress()
                                        self.target_address.parent = self
                                        self._children_name_map["target_address"] = "target-address"
                                        self._segment_path = lambda: "hour" + "[hour-index='" + str(self.hour_index) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour, ['hour_index', u'start_time', u'return_code', u'completion_time_count', u'completion_time', u'min_completion_time', u'max_completion_time', u'sum_completion_time', u'path_count', u'min_path_count', u'max_path_count', u'ok_count', u'no_path_count', u'all_paths_broken_count', u'all_paths_unexplorable_count', u'all_paths_broken_or_unexplorable_count', u'timeout_count', u'internal_error_count', u'unknown_count'], name, value)


                                    class TargetAddress(Entity):
                                        """
                                        LPD target
                                        
                                        .. attribute:: ipv4_prefix_target
                                        
                                        	IPv4 prefix target
                                        	**type**\:  :py:class:`Ipv4PrefixTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PrefixTarget>`
                                        
                                        .. attribute:: tunnel_id_target
                                        
                                        	Tunnel ID target
                                        	**type**\:  :py:class:`TunnelIdTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.TunnelIdTarget>`
                                        
                                        .. attribute:: ipv4_pseudowire_target
                                        
                                        	IPv4 pseudowire target
                                        	**type**\:  :py:class:`Ipv4PseudowireTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PseudowireTarget>`
                                        
                                        .. attribute:: target_type
                                        
                                        	TargetType
                                        	**type**\:  :py:class:`IpslaTargetTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaTargetTypeEnum>`
                                        
                                        .. attribute:: ipv4_address_target
                                        
                                        	IPv4 address target
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ipv6_address_target
                                        
                                        	IPv6 address target
                                        	**type**\: str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress, self).__init__()

                                            self.yang_name = "target-address"
                                            self.yang_parent_name = "hour"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ipv4-prefix-target", ("ipv4_prefix_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PrefixTarget)), ("tunnel-id-target", ("tunnel_id_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.TunnelIdTarget)), ("ipv4-pseudowire-target", ("ipv4_pseudowire_target", Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PseudowireTarget))])
                                            self._leafs = OrderedDict([
                                                ('target_type', (YLeaf(YType.enumeration, 'target-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaTargetTypeEnum', '')])),
                                                ('ipv4_address_target', (YLeaf(YType.str, 'ipv4-address-target'), ['str'])),
                                                ('ipv6_address_target', (YLeaf(YType.str, 'ipv6-address-target'), ['str'])),
                                            ])
                                            self.target_type = None
                                            self.ipv4_address_target = None
                                            self.ipv6_address_target = None

                                            self.ipv4_prefix_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PrefixTarget()
                                            self.ipv4_prefix_target.parent = self
                                            self._children_name_map["ipv4_prefix_target"] = "ipv4-prefix-target"

                                            self.tunnel_id_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.TunnelIdTarget()
                                            self.tunnel_id_target.parent = self
                                            self._children_name_map["tunnel_id_target"] = "tunnel-id-target"

                                            self.ipv4_pseudowire_target = Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PseudowireTarget()
                                            self.ipv4_pseudowire_target.parent = self
                                            self._children_name_map["ipv4_pseudowire_target"] = "ipv4-pseudowire-target"
                                            self._segment_path = lambda: "target-address"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress, [u'target_type', u'ipv4_address_target', u'ipv6_address_target'], name, value)


                                        class Ipv4PrefixTarget(Entity):
                                            """
                                            IPv4 prefix target
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: mask_length
                                            
                                            	Mask length
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PrefixTarget, self).__init__()

                                                self.yang_name = "ipv4-prefix-target"
                                                self.yang_parent_name = "target-address"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                    ('mask_length', (YLeaf(YType.uint8, 'mask-length'), ['int'])),
                                                ])
                                                self.address = None
                                                self.mask_length = None
                                                self._segment_path = lambda: "ipv4-prefix-target"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PrefixTarget, [u'address', u'mask_length'], name, value)


                                        class TunnelIdTarget(Entity):
                                            """
                                            Tunnel ID target
                                            
                                            .. attribute:: tunnel_id
                                            
                                            	Tunnel ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.TunnelIdTarget, self).__init__()

                                                self.yang_name = "tunnel-id-target"
                                                self.yang_parent_name = "target-address"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                                ])
                                                self.tunnel_id = None
                                                self._segment_path = lambda: "tunnel-id-target"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.TunnelIdTarget, [u'tunnel_id'], name, value)


                                        class Ipv4PseudowireTarget(Entity):
                                            """
                                            IPv4 pseudowire target
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: virtual_circuit_id
                                            
                                            	Virtual circuit ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PseudowireTarget, self).__init__()

                                                self.yang_name = "ipv4-pseudowire-target"
                                                self.yang_parent_name = "target-address"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                    ('virtual_circuit_id', (YLeaf(YType.uint32, 'virtual-circuit-id'), ['int'])),
                                                ])
                                                self.address = None
                                                self.virtual_circuit_id = None
                                                self._segment_path = lambda: "ipv4-pseudowire-target"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Statistics.Aggregated.Hours.Hour.TargetAddress.Ipv4PseudowireTarget, [u'address', u'virtual_circuit_id'], name, value)


                    class Status(Entity):
                        """
                        Operational status of LPD group
                        
                        .. attribute:: lpd_paths
                        
                        	Operational path state in LPD group
                        	**type**\:  :py:class:`LpdPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths>`
                        
                        .. attribute:: state
                        
                        	Operational status of LPD group
                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.State>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.Lpd.Status, self).__init__()

                            self.yang_name = "status"
                            self.yang_parent_name = "lpd"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lpd-paths", ("lpd_paths", Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths)), ("state", ("state", Ipsla.OperationData.Operations.Operation.Lpd.Status.State))])
                            self._leafs = OrderedDict()

                            self.lpd_paths = Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths()
                            self.lpd_paths.parent = self
                            self._children_name_map["lpd_paths"] = "lpd-paths"

                            self.state = Ipsla.OperationData.Operations.Operation.Lpd.Status.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "status"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status, [], name, value)


                        class LpdPaths(Entity):
                            """
                            Operational path state in LPD group
                            
                            .. attribute:: lpd_path
                            
                            	Current operational path state in LPD group
                            	**type**\: list of  		 :py:class:`LpdPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths, self).__init__()

                                self.yang_name = "lpd-paths"
                                self.yang_parent_name = "status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lpd-path", ("lpd_path", Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath))])
                                self._leafs = OrderedDict()

                                self.lpd_path = YList(self)
                                self._segment_path = lambda: "lpd-paths"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths, [], name, value)


                            class LpdPath(Entity):
                                """
                                Current operational path state in LPD
                                group
                                
                                .. attribute:: path_index  (key)
                                
                                	LPD path index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: path_id
                                
                                	LPD path identifier
                                	**type**\:  :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath.PathId>`
                                
                                .. attribute:: path_status
                                
                                	Path status
                                	**type**\:  :py:class:`IpslaMplsLpdPathDiscoveryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsLpdPathDiscoveryStatus>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath, self).__init__()

                                    self.yang_name = "lpd-path"
                                    self.yang_parent_name = "lpd-paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['path_index']
                                    self._child_classes = OrderedDict([("path-id", ("path_id", Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath.PathId))])
                                    self._leafs = OrderedDict([
                                        ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                        ('path_status', (YLeaf(YType.enumeration, 'path-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsLpdPathDiscoveryStatus', '')])),
                                    ])
                                    self.path_index = None
                                    self.path_status = None

                                    self.path_id = Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath.PathId()
                                    self.path_id.parent = self
                                    self._children_name_map["path_id"] = "path-id"
                                    self._segment_path = lambda: "lpd-path" + "[path-index='" + str(self.path_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath, ['path_index', u'path_status'], name, value)


                                class PathId(Entity):
                                    """
                                    LPD path identifier
                                    
                                    .. attribute:: lsp_selector
                                    
                                    	LSP selector
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: output_interface
                                    
                                    	Output interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: nexthop_address
                                    
                                    	Nexthop address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: downstream_label
                                    
                                    	Downstream label stacks
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath.PathId, self).__init__()

                                        self.yang_name = "path-id"
                                        self.yang_parent_name = "lpd-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                            ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                            ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                            ('downstream_label', (YLeafList(YType.uint32, 'downstream-label'), ['int'])),
                                        ])
                                        self.lsp_selector = None
                                        self.output_interface = None
                                        self.nexthop_address = None
                                        self.downstream_label = []
                                        self._segment_path = lambda: "path-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.LpdPaths.LpdPath.PathId, [u'lsp_selector', u'output_interface', u'nexthop_address', u'downstream_label'], name, value)


                        class State(Entity):
                            """
                            Operational status of LPD group
                            
                            .. attribute:: target_address
                            
                            	Target for LPD
                            	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress>`
                            
                            .. attribute:: monitor_id
                            
                            	MPLSLM monitor ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: discovery_mode
                            
                            	Latest LPD mode
                            	**type**\:  :py:class:`IpslaMplsLpdDiscoveryModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsLpdDiscoveryModeEnum>`
                            
                            .. attribute:: start_time
                            
                            	Latest start time
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: return_code
                            
                            	Latest return code
                            	**type**\:  :py:class:`IpslaMplsLpdRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaMplsLpdRetCode>`
                            
                            .. attribute:: completion_time
                            
                            	Latest completion time
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path_count
                            
                            	Number of discovered paths
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Lpd.Status.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress))])
                                self._leafs = OrderedDict([
                                    ('monitor_id', (YLeaf(YType.uint32, 'monitor-id'), ['int'])),
                                    ('discovery_mode', (YLeaf(YType.enumeration, 'discovery-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsLpdDiscoveryModeEnum', '')])),
                                    ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                    ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaMplsLpdRetCode', '')])),
                                    ('completion_time', (YLeaf(YType.uint32, 'completion-time'), ['int'])),
                                    ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                                ])
                                self.monitor_id = None
                                self.discovery_mode = None
                                self.start_time = None
                                self.return_code = None
                                self.completion_time = None
                                self.path_count = None

                                self.target_address = Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress()
                                self.target_address.parent = self
                                self._children_name_map["target_address"] = "target-address"
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.State, [u'monitor_id', u'discovery_mode', u'start_time', u'return_code', u'completion_time', u'path_count'], name, value)


                            class TargetAddress(Entity):
                                """
                                Target for LPD
                                
                                .. attribute:: ipv4_prefix_target
                                
                                	IPv4 prefix target
                                	**type**\:  :py:class:`Ipv4PrefixTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PrefixTarget>`
                                
                                .. attribute:: tunnel_id_target
                                
                                	Tunnel ID target
                                	**type**\:  :py:class:`TunnelIdTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.TunnelIdTarget>`
                                
                                .. attribute:: ipv4_pseudowire_target
                                
                                	IPv4 pseudowire target
                                	**type**\:  :py:class:`Ipv4PseudowireTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PseudowireTarget>`
                                
                                .. attribute:: target_type
                                
                                	TargetType
                                	**type**\:  :py:class:`IpslaTargetTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaTargetTypeEnum>`
                                
                                .. attribute:: ipv4_address_target
                                
                                	IPv4 address target
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address_target
                                
                                	IPv6 address target
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress, self).__init__()

                                    self.yang_name = "target-address"
                                    self.yang_parent_name = "state"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("ipv4-prefix-target", ("ipv4_prefix_target", Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PrefixTarget)), ("tunnel-id-target", ("tunnel_id_target", Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.TunnelIdTarget)), ("ipv4-pseudowire-target", ("ipv4_pseudowire_target", Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PseudowireTarget))])
                                    self._leafs = OrderedDict([
                                        ('target_type', (YLeaf(YType.enumeration, 'target-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaTargetTypeEnum', '')])),
                                        ('ipv4_address_target', (YLeaf(YType.str, 'ipv4-address-target'), ['str'])),
                                        ('ipv6_address_target', (YLeaf(YType.str, 'ipv6-address-target'), ['str'])),
                                    ])
                                    self.target_type = None
                                    self.ipv4_address_target = None
                                    self.ipv6_address_target = None

                                    self.ipv4_prefix_target = Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PrefixTarget()
                                    self.ipv4_prefix_target.parent = self
                                    self._children_name_map["ipv4_prefix_target"] = "ipv4-prefix-target"

                                    self.tunnel_id_target = Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.TunnelIdTarget()
                                    self.tunnel_id_target.parent = self
                                    self._children_name_map["tunnel_id_target"] = "tunnel-id-target"

                                    self.ipv4_pseudowire_target = Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PseudowireTarget()
                                    self.ipv4_pseudowire_target.parent = self
                                    self._children_name_map["ipv4_pseudowire_target"] = "ipv4-pseudowire-target"
                                    self._segment_path = lambda: "target-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress, [u'target_type', u'ipv4_address_target', u'ipv6_address_target'], name, value)


                                class Ipv4PrefixTarget(Entity):
                                    """
                                    IPv4 prefix target
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: mask_length
                                    
                                    	Mask length
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PrefixTarget, self).__init__()

                                        self.yang_name = "ipv4-prefix-target"
                                        self.yang_parent_name = "target-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('mask_length', (YLeaf(YType.uint8, 'mask-length'), ['int'])),
                                        ])
                                        self.address = None
                                        self.mask_length = None
                                        self._segment_path = lambda: "ipv4-prefix-target"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PrefixTarget, [u'address', u'mask_length'], name, value)


                                class TunnelIdTarget(Entity):
                                    """
                                    Tunnel ID target
                                    
                                    .. attribute:: tunnel_id
                                    
                                    	Tunnel ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.TunnelIdTarget, self).__init__()

                                        self.yang_name = "tunnel-id-target"
                                        self.yang_parent_name = "target-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                        ])
                                        self.tunnel_id = None
                                        self._segment_path = lambda: "tunnel-id-target"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.TunnelIdTarget, [u'tunnel_id'], name, value)


                                class Ipv4PseudowireTarget(Entity):
                                    """
                                    IPv4 pseudowire target
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: virtual_circuit_id
                                    
                                    	Virtual circuit ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PseudowireTarget, self).__init__()

                                        self.yang_name = "ipv4-pseudowire-target"
                                        self.yang_parent_name = "target-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('virtual_circuit_id', (YLeaf(YType.uint32, 'virtual-circuit-id'), ['int'])),
                                        ])
                                        self.address = None
                                        self.virtual_circuit_id = None
                                        self._segment_path = lambda: "ipv4-pseudowire-target"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Lpd.Status.State.TargetAddress.Ipv4PseudowireTarget, [u'address', u'virtual_circuit_id'], name, value)


                class History(Entity):
                    """
                    Historical data for an operation
                    
                    .. attribute:: path
                    
                    	Historical data with multiple hops along the path
                    	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path>`
                    
                    .. attribute:: target
                    
                    	Historical data for the destination node
                    	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.OperationData.Operations.Operation.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "operation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path", ("path", Ipsla.OperationData.Operations.Operation.History.Path)), ("target", ("target", Ipsla.OperationData.Operations.Operation.History.Target))])
                        self._leafs = OrderedDict()

                        self.path = Ipsla.OperationData.Operations.Operation.History.Path()
                        self.path.parent = self
                        self._children_name_map["path"] = "path"

                        self.target = Ipsla.OperationData.Operations.Operation.History.Target()
                        self.target.parent = self
                        self._children_name_map["target"] = "target"
                        self._segment_path = lambda: "history"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.History, [], name, value)


                    class Path(Entity):
                        """
                        Historical data with multiple hops along the
                        path
                        
                        .. attribute:: lifes
                        
                        	Tables of lives for an operation
                        	**type**\:  :py:class:`Lifes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.History.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lifes", ("lifes", Ipsla.OperationData.Operations.Operation.History.Path.Lifes))])
                            self._leafs = OrderedDict()

                            self.lifes = Ipsla.OperationData.Operations.Operation.History.Path.Lifes()
                            self.lifes.parent = self
                            self._children_name_map["lifes"] = "lifes"
                            self._segment_path = lambda: "path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path, [], name, value)


                        class Lifes(Entity):
                            """
                            Tables of lives for an operation
                            
                            .. attribute:: life
                            
                            	History data for a particular life of the operation
                            	**type**\: list of  		 :py:class:`Life <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes, self).__init__()

                                self.yang_name = "lifes"
                                self.yang_parent_name = "path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("life", ("life", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life))])
                                self._leafs = OrderedDict()

                                self.life = YList(self)
                                self._segment_path = lambda: "lifes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes, [], name, value)


                            class Life(Entity):
                                """
                                History data for a particular life of the
                                operation
                                
                                .. attribute:: life_index  (key)
                                
                                	Life Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: buckets
                                
                                	Table of history buckets (samples) for a particular operation
                                	**type**\:  :py:class:`Buckets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life, self).__init__()

                                    self.yang_name = "life"
                                    self.yang_parent_name = "lifes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['life_index']
                                    self._child_classes = OrderedDict([("buckets", ("buckets", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets))])
                                    self._leafs = OrderedDict([
                                        ('life_index', (YLeaf(YType.uint32, 'life-index'), ['int'])),
                                    ])
                                    self.life_index = None

                                    self.buckets = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets()
                                    self.buckets.parent = self
                                    self._children_name_map["buckets"] = "buckets"
                                    self._segment_path = lambda: "life" + "[life-index='" + str(self.life_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life, ['life_index'], name, value)


                                class Buckets(Entity):
                                    """
                                    Table of history buckets (samples) for a
                                    particular operation
                                    
                                    .. attribute:: bucket
                                    
                                    	History bucket for an operation
                                    	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets, self).__init__()

                                        self.yang_name = "buckets"
                                        self.yang_parent_name = "life"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bucket", ("bucket", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket))])
                                        self._leafs = OrderedDict()

                                        self.bucket = YList(self)
                                        self._segment_path = lambda: "buckets"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets, [], name, value)


                                    class Bucket(Entity):
                                        """
                                        History bucket for an operation
                                        
                                        .. attribute:: bucket_index  (key)
                                        
                                        	Bucket Index
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: samples
                                        
                                        	Table of samples for a particular cycle
                                        	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket, self).__init__()

                                            self.yang_name = "bucket"
                                            self.yang_parent_name = "buckets"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['bucket_index']
                                            self._child_classes = OrderedDict([("samples", ("samples", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples))])
                                            self._leafs = OrderedDict([
                                                ('bucket_index', (YLeaf(YType.uint32, 'bucket-index'), ['int'])),
                                            ])
                                            self.bucket_index = None

                                            self.samples = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples()
                                            self.samples.parent = self
                                            self._children_name_map["samples"] = "samples"
                                            self._segment_path = lambda: "bucket" + "[bucket-index='" + str(self.bucket_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket, ['bucket_index'], name, value)


                                        class Samples(Entity):
                                            """
                                            Table of samples for a particular cycle
                                            
                                            .. attribute:: sample
                                            
                                            	Data sample for particular cycle
                                            	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples, self).__init__()

                                                self.yang_name = "samples"
                                                self.yang_parent_name = "bucket"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("sample", ("sample", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample))])
                                                self._leafs = OrderedDict()

                                                self.sample = YList(self)
                                                self._segment_path = lambda: "samples"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples, [], name, value)


                                            class Sample(Entity):
                                                """
                                                Data sample for particular cycle
                                                
                                                .. attribute:: sample_index  (key)
                                                
                                                	Sample Index
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: target_address
                                                
                                                	Target for the operation
                                                	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress>`
                                                
                                                .. attribute:: start_time
                                                
                                                	Sample Start Time expressed in msec since00\:00 \:00 UTC, January 1, 1970
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: response_time
                                                
                                                	Round Trip Time (milliseconds)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: return_code
                                                
                                                	Response Return Code
                                                	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample, self).__init__()

                                                    self.yang_name = "sample"
                                                    self.yang_parent_name = "samples"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['sample_index']
                                                    self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress))])
                                                    self._leafs = OrderedDict([
                                                        ('sample_index', (YLeaf(YType.uint32, 'sample-index'), ['int'])),
                                                        ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                        ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                    ])
                                                    self.sample_index = None
                                                    self.start_time = None
                                                    self.response_time = None
                                                    self.return_code = None

                                                    self.target_address = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress()
                                                    self.target_address.parent = self
                                                    self._children_name_map["target_address"] = "target-address"
                                                    self._segment_path = lambda: "sample" + "[sample-index='" + str(self.sample_index) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample, ['sample_index', u'start_time', u'response_time', u'return_code'], name, value)


                                                class TargetAddress(Entity):
                                                    """
                                                    Target for the operation
                                                    
                                                    .. attribute:: ipv4_prefix_target
                                                    
                                                    	IPv4 prefix target
                                                    	**type**\:  :py:class:`Ipv4PrefixTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PrefixTarget>`
                                                    
                                                    .. attribute:: tunnel_id_target
                                                    
                                                    	Tunnel ID target
                                                    	**type**\:  :py:class:`TunnelIdTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.TunnelIdTarget>`
                                                    
                                                    .. attribute:: ipv4_pseudowire_target
                                                    
                                                    	IPv4 pseudowire target
                                                    	**type**\:  :py:class:`Ipv4PseudowireTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PseudowireTarget>`
                                                    
                                                    .. attribute:: target_type
                                                    
                                                    	TargetType
                                                    	**type**\:  :py:class:`IpslaTargetTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaTargetTypeEnum>`
                                                    
                                                    .. attribute:: ipv4_address_target
                                                    
                                                    	IPv4 address target
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: ipv6_address_target
                                                    
                                                    	IPv6 address target
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'man-ipsla-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress, self).__init__()

                                                        self.yang_name = "target-address"
                                                        self.yang_parent_name = "sample"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("ipv4-prefix-target", ("ipv4_prefix_target", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PrefixTarget)), ("tunnel-id-target", ("tunnel_id_target", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.TunnelIdTarget)), ("ipv4-pseudowire-target", ("ipv4_pseudowire_target", Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PseudowireTarget))])
                                                        self._leafs = OrderedDict([
                                                            ('target_type', (YLeaf(YType.enumeration, 'target-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaTargetTypeEnum', '')])),
                                                            ('ipv4_address_target', (YLeaf(YType.str, 'ipv4-address-target'), ['str'])),
                                                            ('ipv6_address_target', (YLeaf(YType.str, 'ipv6-address-target'), ['str'])),
                                                        ])
                                                        self.target_type = None
                                                        self.ipv4_address_target = None
                                                        self.ipv6_address_target = None

                                                        self.ipv4_prefix_target = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PrefixTarget()
                                                        self.ipv4_prefix_target.parent = self
                                                        self._children_name_map["ipv4_prefix_target"] = "ipv4-prefix-target"

                                                        self.tunnel_id_target = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.TunnelIdTarget()
                                                        self.tunnel_id_target.parent = self
                                                        self._children_name_map["tunnel_id_target"] = "tunnel-id-target"

                                                        self.ipv4_pseudowire_target = Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PseudowireTarget()
                                                        self.ipv4_pseudowire_target.parent = self
                                                        self._children_name_map["ipv4_pseudowire_target"] = "ipv4-pseudowire-target"
                                                        self._segment_path = lambda: "target-address"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress, [u'target_type', u'ipv4_address_target', u'ipv6_address_target'], name, value)


                                                    class Ipv4PrefixTarget(Entity):
                                                        """
                                                        IPv4 prefix target
                                                        
                                                        .. attribute:: address
                                                        
                                                        	IPv4 address
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: mask_length
                                                        
                                                        	Mask length
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PrefixTarget, self).__init__()

                                                            self.yang_name = "ipv4-prefix-target"
                                                            self.yang_parent_name = "target-address"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                                ('mask_length', (YLeaf(YType.uint8, 'mask-length'), ['int'])),
                                                            ])
                                                            self.address = None
                                                            self.mask_length = None
                                                            self._segment_path = lambda: "ipv4-prefix-target"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PrefixTarget, [u'address', u'mask_length'], name, value)


                                                    class TunnelIdTarget(Entity):
                                                        """
                                                        Tunnel ID target
                                                        
                                                        .. attribute:: tunnel_id
                                                        
                                                        	Tunnel ID
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.TunnelIdTarget, self).__init__()

                                                            self.yang_name = "tunnel-id-target"
                                                            self.yang_parent_name = "target-address"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                                            ])
                                                            self.tunnel_id = None
                                                            self._segment_path = lambda: "tunnel-id-target"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.TunnelIdTarget, [u'tunnel_id'], name, value)


                                                    class Ipv4PseudowireTarget(Entity):
                                                        """
                                                        IPv4 pseudowire target
                                                        
                                                        .. attribute:: address
                                                        
                                                        	IPv4 address
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: virtual_circuit_id
                                                        
                                                        	Virtual circuit ID
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PseudowireTarget, self).__init__()

                                                            self.yang_name = "ipv4-pseudowire-target"
                                                            self.yang_parent_name = "target-address"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                                ('virtual_circuit_id', (YLeaf(YType.uint32, 'virtual-circuit-id'), ['int'])),
                                                            ])
                                                            self.address = None
                                                            self.virtual_circuit_id = None
                                                            self._segment_path = lambda: "ipv4-pseudowire-target"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Path.Lifes.Life.Buckets.Bucket.Samples.Sample.TargetAddress.Ipv4PseudowireTarget, [u'address', u'virtual_circuit_id'], name, value)


                    class Target(Entity):
                        """
                        Historical data for the destination node
                        
                        .. attribute:: lifes
                        
                        	Tables of lives for an operation
                        	**type**\:  :py:class:`Lifes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.History.Target, self).__init__()

                            self.yang_name = "target"
                            self.yang_parent_name = "history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lifes", ("lifes", Ipsla.OperationData.Operations.Operation.History.Target.Lifes))])
                            self._leafs = OrderedDict()

                            self.lifes = Ipsla.OperationData.Operations.Operation.History.Target.Lifes()
                            self.lifes.parent = self
                            self._children_name_map["lifes"] = "lifes"
                            self._segment_path = lambda: "target"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target, [], name, value)


                        class Lifes(Entity):
                            """
                            Tables of lives for an operation
                            
                            .. attribute:: life
                            
                            	Operational data for a particular life of the operation
                            	**type**\: list of  		 :py:class:`Life <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes, self).__init__()

                                self.yang_name = "lifes"
                                self.yang_parent_name = "target"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("life", ("life", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life))])
                                self._leafs = OrderedDict()

                                self.life = YList(self)
                                self._segment_path = lambda: "lifes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes, [], name, value)


                            class Life(Entity):
                                """
                                Operational data for a particular life of
                                the operation
                                
                                .. attribute:: life_index  (key)
                                
                                	Life Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: buckets
                                
                                	Table of history buckets (samples) for a particular operation
                                	**type**\:  :py:class:`Buckets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life, self).__init__()

                                    self.yang_name = "life"
                                    self.yang_parent_name = "lifes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['life_index']
                                    self._child_classes = OrderedDict([("buckets", ("buckets", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets))])
                                    self._leafs = OrderedDict([
                                        ('life_index', (YLeaf(YType.uint32, 'life-index'), ['int'])),
                                    ])
                                    self.life_index = None

                                    self.buckets = Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets()
                                    self.buckets.parent = self
                                    self._children_name_map["buckets"] = "buckets"
                                    self._segment_path = lambda: "life" + "[life-index='" + str(self.life_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life, ['life_index'], name, value)


                                class Buckets(Entity):
                                    """
                                    Table of history buckets (samples) for a
                                    particular operation
                                    
                                    .. attribute:: bucket
                                    
                                    	History bucket for an operation
                                    	**type**\: list of  		 :py:class:`Bucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets, self).__init__()

                                        self.yang_name = "buckets"
                                        self.yang_parent_name = "life"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("bucket", ("bucket", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket))])
                                        self._leafs = OrderedDict()

                                        self.bucket = YList(self)
                                        self._segment_path = lambda: "buckets"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets, [], name, value)


                                    class Bucket(Entity):
                                        """
                                        History bucket for an operation
                                        
                                        .. attribute:: bucket_index  (key)
                                        
                                        	Bucket Index
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: target_address
                                        
                                        	Target for the operation
                                        	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress>`
                                        
                                        .. attribute:: start_time
                                        
                                        	Sample Start Time expressed in msec since00\:00 \:00 UTC, January 1, 1970
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: response_time
                                        
                                        	Round Trip Time (milliseconds)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: return_code
                                        
                                        	Response Return Code
                                        	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket, self).__init__()

                                            self.yang_name = "bucket"
                                            self.yang_parent_name = "buckets"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['bucket_index']
                                            self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress))])
                                            self._leafs = OrderedDict([
                                                ('bucket_index', (YLeaf(YType.uint32, 'bucket-index'), ['int'])),
                                                ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                                                ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                            ])
                                            self.bucket_index = None
                                            self.start_time = None
                                            self.response_time = None
                                            self.return_code = None

                                            self.target_address = Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress()
                                            self.target_address.parent = self
                                            self._children_name_map["target_address"] = "target-address"
                                            self._segment_path = lambda: "bucket" + "[bucket-index='" + str(self.bucket_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket, ['bucket_index', u'start_time', u'response_time', u'return_code'], name, value)


                                        class TargetAddress(Entity):
                                            """
                                            Target for the operation
                                            
                                            .. attribute:: ipv4_prefix_target
                                            
                                            	IPv4 prefix target
                                            	**type**\:  :py:class:`Ipv4PrefixTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PrefixTarget>`
                                            
                                            .. attribute:: tunnel_id_target
                                            
                                            	Tunnel ID target
                                            	**type**\:  :py:class:`TunnelIdTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.TunnelIdTarget>`
                                            
                                            .. attribute:: ipv4_pseudowire_target
                                            
                                            	IPv4 pseudowire target
                                            	**type**\:  :py:class:`Ipv4PseudowireTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PseudowireTarget>`
                                            
                                            .. attribute:: target_type
                                            
                                            	TargetType
                                            	**type**\:  :py:class:`IpslaTargetTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaTargetTypeEnum>`
                                            
                                            .. attribute:: ipv4_address_target
                                            
                                            	IPv4 address target
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address_target
                                            
                                            	IPv6 address target
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress, self).__init__()

                                                self.yang_name = "target-address"
                                                self.yang_parent_name = "bucket"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("ipv4-prefix-target", ("ipv4_prefix_target", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PrefixTarget)), ("tunnel-id-target", ("tunnel_id_target", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.TunnelIdTarget)), ("ipv4-pseudowire-target", ("ipv4_pseudowire_target", Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PseudowireTarget))])
                                                self._leafs = OrderedDict([
                                                    ('target_type', (YLeaf(YType.enumeration, 'target-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaTargetTypeEnum', '')])),
                                                    ('ipv4_address_target', (YLeaf(YType.str, 'ipv4-address-target'), ['str'])),
                                                    ('ipv6_address_target', (YLeaf(YType.str, 'ipv6-address-target'), ['str'])),
                                                ])
                                                self.target_type = None
                                                self.ipv4_address_target = None
                                                self.ipv6_address_target = None

                                                self.ipv4_prefix_target = Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PrefixTarget()
                                                self.ipv4_prefix_target.parent = self
                                                self._children_name_map["ipv4_prefix_target"] = "ipv4-prefix-target"

                                                self.tunnel_id_target = Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.TunnelIdTarget()
                                                self.tunnel_id_target.parent = self
                                                self._children_name_map["tunnel_id_target"] = "tunnel-id-target"

                                                self.ipv4_pseudowire_target = Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PseudowireTarget()
                                                self.ipv4_pseudowire_target.parent = self
                                                self._children_name_map["ipv4_pseudowire_target"] = "ipv4-pseudowire-target"
                                                self._segment_path = lambda: "target-address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress, [u'target_type', u'ipv4_address_target', u'ipv6_address_target'], name, value)


                                            class Ipv4PrefixTarget(Entity):
                                                """
                                                IPv4 prefix target
                                                
                                                .. attribute:: address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: mask_length
                                                
                                                	Mask length
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PrefixTarget, self).__init__()

                                                    self.yang_name = "ipv4-prefix-target"
                                                    self.yang_parent_name = "target-address"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                        ('mask_length', (YLeaf(YType.uint8, 'mask-length'), ['int'])),
                                                    ])
                                                    self.address = None
                                                    self.mask_length = None
                                                    self._segment_path = lambda: "ipv4-prefix-target"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PrefixTarget, [u'address', u'mask_length'], name, value)


                                            class TunnelIdTarget(Entity):
                                                """
                                                Tunnel ID target
                                                
                                                .. attribute:: tunnel_id
                                                
                                                	Tunnel ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.TunnelIdTarget, self).__init__()

                                                    self.yang_name = "tunnel-id-target"
                                                    self.yang_parent_name = "target-address"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                                    ])
                                                    self.tunnel_id = None
                                                    self._segment_path = lambda: "tunnel-id-target"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.TunnelIdTarget, [u'tunnel_id'], name, value)


                                            class Ipv4PseudowireTarget(Entity):
                                                """
                                                IPv4 pseudowire target
                                                
                                                .. attribute:: address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: virtual_circuit_id
                                                
                                                	Virtual circuit ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PseudowireTarget, self).__init__()

                                                    self.yang_name = "ipv4-pseudowire-target"
                                                    self.yang_parent_name = "target-address"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                        ('virtual_circuit_id', (YLeaf(YType.uint32, 'virtual-circuit-id'), ['int'])),
                                                    ])
                                                    self.address = None
                                                    self.virtual_circuit_id = None
                                                    self._segment_path = lambda: "ipv4-pseudowire-target"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.History.Target.Lifes.Life.Buckets.Bucket.TargetAddress.Ipv4PseudowireTarget, [u'address', u'virtual_circuit_id'], name, value)


                class Statistics(Entity):
                    """
                    Statistics collected for an operation
                    
                    .. attribute:: latest
                    
                    	Statistics collected during the last sampling cycle of the operation
                    	**type**\:  :py:class:`Latest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest>`
                    
                    .. attribute:: aggregated
                    
                    	Statistics aggregated for data collected over time intervals
                    	**type**\:  :py:class:`Aggregated <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated>`
                    
                    

                    """

                    _prefix = 'man-ipsla-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.OperationData.Operations.Operation.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "operation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("latest", ("latest", Ipsla.OperationData.Operations.Operation.Statistics.Latest)), ("aggregated", ("aggregated", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated))])
                        self._leafs = OrderedDict()

                        self.latest = Ipsla.OperationData.Operations.Operation.Statistics.Latest()
                        self.latest.parent = self
                        self._children_name_map["latest"] = "latest"

                        self.aggregated = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated()
                        self.aggregated.parent = self
                        self._children_name_map["aggregated"] = "aggregated"
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics, [], name, value)


                    class Latest(Entity):
                        """
                        Statistics collected during the last
                        sampling cycle of the operation
                        
                        .. attribute:: target
                        
                        	Latest statistics for the target node
                        	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target>`
                        
                        .. attribute:: hops
                        
                        	Latest statistics for hops in a path\-enabled operation
                        	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops>`
                        
                        .. attribute:: lpd_paths
                        
                        	List of latest LPD paths
                        	**type**\:  :py:class:`LpdPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.Statistics.Latest, self).__init__()

                            self.yang_name = "latest"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("target", ("target", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target)), ("hops", ("hops", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops)), ("lpd-paths", ("lpd_paths", Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths))])
                            self._leafs = OrderedDict()

                            self.target = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target()
                            self.target.parent = self
                            self._children_name_map["target"] = "target"

                            self.hops = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops()
                            self.hops.parent = self
                            self._children_name_map["hops"] = "hops"

                            self.lpd_paths = Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths()
                            self.lpd_paths.parent = self
                            self._children_name_map["lpd_paths"] = "lpd-paths"
                            self._segment_path = lambda: "latest"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest, [], name, value)


                        class Target(Entity):
                            """
                            Latest statistics for the target node
                            
                            .. attribute:: common_stats
                            
                            	Common Stats
                            	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.CommonStats>`
                            
                            .. attribute:: specific_stats
                            
                            	Operation Specific Stats
                            	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target, self).__init__()

                                self.yang_name = "target"
                                self.yang_parent_name = "latest"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats))])
                                self._leafs = OrderedDict()

                                self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.CommonStats()
                                self.common_stats.parent = self
                                self._children_name_map["common_stats"] = "common-stats"

                                self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats()
                                self.specific_stats.parent = self
                                self._children_name_map["specific_stats"] = "specific-stats"
                                self._segment_path = lambda: "target"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target, [], name, value)


                            class CommonStats(Entity):
                                """
                                Common Stats
                                
                                .. attribute:: operation_time
                                
                                	Operation Time
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: return_code
                                
                                	Return code
                                	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                
                                .. attribute:: response_time_count
                                
                                	Number of RTT samples used for the statistics
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: response_time
                                
                                	RTT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: min_response_time
                                
                                	Minimum RTT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_response_time
                                
                                	Maximum RTT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sum_response_time
                                
                                	Sum of RTT
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sum2_response_time
                                
                                	Sum of RTT^2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: update_count
                                
                                	Number of updates processed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ok_count
                                
                                	Number of updates with Okay return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnect_count
                                
                                	Number of updates with Disconnected return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: timeout_count
                                
                                	Number of updates with Timeout return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: busy_count
                                
                                	Number of updates with Busy return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_connection_count
                                
                                	Number of updates with NotConnected return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dropped_count
                                
                                	Number of updates with Dropped return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: internal_error_count
                                
                                	Number of updates with InternalError return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sequence_error_count
                                
                                	Number of updates with SeqError return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: verify_error_count
                                
                                	Number of updates with VerifyError return code
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.CommonStats, self).__init__()

                                    self.yang_name = "common-stats"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                        ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                        ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                        ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                        ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                        ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                        ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                        ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                        ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                        ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                        ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                        ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                        ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                        ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                        ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                        ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                        ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                    ])
                                    self.operation_time = None
                                    self.return_code = None
                                    self.response_time_count = None
                                    self.response_time = None
                                    self.min_response_time = None
                                    self.max_response_time = None
                                    self.sum_response_time = None
                                    self.sum2_response_time = None
                                    self.update_count = None
                                    self.ok_count = None
                                    self.disconnect_count = None
                                    self.timeout_count = None
                                    self.busy_count = None
                                    self.no_connection_count = None
                                    self.dropped_count = None
                                    self.internal_error_count = None
                                    self.sequence_error_count = None
                                    self.verify_error_count = None
                                    self._segment_path = lambda: "common-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                            class SpecificStats(Entity):
                                """
                                Operation Specific Stats
                                
                                .. attribute:: icmp_path_jitter_stats
                                
                                	icmp path jitter stats
                                	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.IcmpPathJitterStats>`
                                
                                .. attribute:: udp_jitter_stats
                                
                                	udp jitter stats
                                	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.UdpJitterStats>`
                                
                                .. attribute:: op_type
                                
                                	op type
                                	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats, self).__init__()

                                    self.yang_name = "specific-stats"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.UdpJitterStats))])
                                    self._leafs = OrderedDict([
                                        ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                    ])
                                    self.op_type = None

                                    self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.IcmpPathJitterStats()
                                    self.icmp_path_jitter_stats.parent = self
                                    self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                    self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.UdpJitterStats()
                                    self.udp_jitter_stats.parent = self
                                    self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                    self._segment_path = lambda: "specific-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats, [u'op_type'], name, value)


                                class IcmpPathJitterStats(Entity):
                                    """
                                    icmp path jitter stats
                                    
                                    .. attribute:: source_address
                                    
                                    	IP Address of the source
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: dest_address
                                    
                                    	IP Address of the destination
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: hop_address
                                    
                                    	IP address of the hop in the path
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: packet_interval
                                    
                                    	Interval between echos in ms
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: response_time_count
                                    
                                    	Number of RTT samples  used for the statistics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: response_time
                                    
                                    	RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: min_response_time
                                    
                                    	Minimum RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: max_response_time
                                    
                                    	Maximum RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sum_response_time
                                    
                                    	Sum of RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sum2_response_time
                                    
                                    	Sum of RTT^2
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_count
                                    
                                    	Number of Echo replies received 
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_loss_count
                                    
                                    	Number of packets lost
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: out_of_sequence_count
                                    
                                    	Number of out of sequence packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: discarded_sample_count
                                    
                                    	Number of discarded samples
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: verify_errors_count
                                    
                                    	Number of packets with data corruption
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: dropped_error_count
                                    
                                    	Number of packets dropped
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: jitter
                                    
                                    	Jitter value for this node in the path
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pos_jitter_sum
                                    
                                    	Sum of positive jitter value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pos_jitter_sum2
                                    
                                    	Sum of squares of positive jitter values
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pos_jitter_min
                                    
                                    	Minimum positive jitter value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pos_jitter_max
                                    
                                    	Maximum positive jitter value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pos_jitter_count
                                    
                                    	Number of positive jitter values
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: neg_jitter_sum
                                    
                                    	Sum of negative jitter values
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: neg_jitter_min
                                    
                                    	Minimum negative jitter value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: neg_jitter_max
                                    
                                    	Maximum negative jitter value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: neg_jitter_sum2
                                    
                                    	Sum of squares of negative jitter values
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: neg_jitter_count
                                    
                                    	Number of negative jitter values
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.IcmpPathJitterStats, self).__init__()

                                        self.yang_name = "icmp-path-jitter-stats"
                                        self.yang_parent_name = "specific-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                            ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                            ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                            ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                            ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                            ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                            ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                            ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                            ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                            ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                            ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                            ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                            ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                            ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                            ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                            ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                            ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                            ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                            ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                            ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                            ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                            ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                            ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                            ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                            ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                            ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                            ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                        ])
                                        self.source_address = None
                                        self.dest_address = None
                                        self.hop_address = None
                                        self.packet_interval = None
                                        self.response_time_count = None
                                        self.response_time = None
                                        self.min_response_time = None
                                        self.max_response_time = None
                                        self.sum_response_time = None
                                        self.sum2_response_time = None
                                        self.packet_count = None
                                        self.packet_loss_count = None
                                        self.out_of_sequence_count = None
                                        self.discarded_sample_count = None
                                        self.verify_errors_count = None
                                        self.dropped_error_count = None
                                        self.jitter = None
                                        self.pos_jitter_sum = None
                                        self.pos_jitter_sum2 = None
                                        self.pos_jitter_min = None
                                        self.pos_jitter_max = None
                                        self.pos_jitter_count = None
                                        self.neg_jitter_sum = None
                                        self.neg_jitter_min = None
                                        self.neg_jitter_max = None
                                        self.neg_jitter_sum2 = None
                                        self.neg_jitter_count = None
                                        self._segment_path = lambda: "icmp-path-jitter-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                class UdpJitterStats(Entity):
                                    """
                                    udp jitter stats
                                    
                                    .. attribute:: jitter_in
                                    
                                    	Input Jitter moving average, computed as per RFC1889
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: jitter_out
                                    
                                    	Output Jitter moving average, computed as per RFC1889
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_loss_sd
                                    
                                    	Packets lost in source to destination (SD) direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_loss_ds
                                    
                                    	Packets lost in destination to source (DS) direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_out_of_sequence
                                    
                                    	Packets out of sequence
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_mia
                                    
                                    	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_skipped
                                    
                                    	Packets which are skipped
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_late_arrivals
                                    
                                    	Packets arriving late
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: packet_invalid_tstamp
                                    
                                    	Packets with bad timestamps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: internal_errors_count
                                    
                                    	Number of internal errors
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: busies_count
                                    
                                    	Number of busies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_sd_sum
                                    
                                    	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: positive_sd_sum2
                                    
                                    	Sum of squares of positive jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: positive_sd_min
                                    
                                    	Minimum of positive jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_sd_max
                                    
                                    	Maximum of positive jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_sd_count
                                    
                                    	Number of positive jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_sd_sum
                                    
                                    	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: negative_sd_sum2
                                    
                                    	Sum of squares of negative jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: negative_sd_min
                                    
                                    	Minimum of negative jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_sd_max
                                    
                                    	Maximum of negative jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_sd_count
                                    
                                    	Number of negative jitter values in SD direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_ds_sum
                                    
                                    	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: positive_ds_sum2
                                    
                                    	Sum of squares of positive jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: positive_ds_min
                                    
                                    	Minimum of positive jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_ds_max
                                    
                                    	Maximum of positive jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: positive_ds_count
                                    
                                    	Number of positive jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_ds_sum
                                    
                                    	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: negative_ds_sum2
                                    
                                    	Sum of squares of negative jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: negative_ds_min
                                    
                                    	Minimum of negative jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_ds_max
                                    
                                    	Maximum of negative jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: negative_ds_count
                                    
                                    	Number of negative jitter values in DS direction
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_count
                                    
                                    	Number of probe/probe\-response pairs used to compute one\-way statistics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_sd_min
                                    
                                    	Minimum of one\-way jitter values in SD direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_sd_max
                                    
                                    	Maximum of one\-way jitter values in SD direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_sd_sum
                                    
                                    	Sum of one\-way jitter values in SD direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_sd_sum2
                                    
                                    	Sum of squares of one\-way jitter values in SD direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: one_way_ds_min
                                    
                                    	Minimum of one\-way jitter values in DS direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_ds_max
                                    
                                    	Maximum of one\-way jitter values in DS direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_ds_sum
                                    
                                    	Sum of one\-way jitter values in DS direction (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: one_way_ds_sum2
                                    
                                    	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.UdpJitterStats, self).__init__()

                                        self.yang_name = "udp-jitter-stats"
                                        self.yang_parent_name = "specific-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                            ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                            ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                            ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                            ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                            ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                            ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                            ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                            ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                            ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                            ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                            ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                            ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                            ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                            ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                            ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                            ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                            ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                            ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                            ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                            ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                            ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                            ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                            ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                            ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                            ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                            ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                            ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                            ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                            ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                            ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                            ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                            ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                            ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                            ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                            ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                            ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                            ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                            ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                            ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                        ])
                                        self.jitter_in = None
                                        self.jitter_out = None
                                        self.packet_loss_sd = None
                                        self.packet_loss_ds = None
                                        self.packet_out_of_sequence = None
                                        self.packet_mia = None
                                        self.packet_skipped = None
                                        self.packet_late_arrivals = None
                                        self.packet_invalid_tstamp = None
                                        self.internal_errors_count = None
                                        self.busies_count = None
                                        self.positive_sd_sum = None
                                        self.positive_sd_sum2 = None
                                        self.positive_sd_min = None
                                        self.positive_sd_max = None
                                        self.positive_sd_count = None
                                        self.negative_sd_sum = None
                                        self.negative_sd_sum2 = None
                                        self.negative_sd_min = None
                                        self.negative_sd_max = None
                                        self.negative_sd_count = None
                                        self.positive_ds_sum = None
                                        self.positive_ds_sum2 = None
                                        self.positive_ds_min = None
                                        self.positive_ds_max = None
                                        self.positive_ds_count = None
                                        self.negative_ds_sum = None
                                        self.negative_ds_sum2 = None
                                        self.negative_ds_min = None
                                        self.negative_ds_max = None
                                        self.negative_ds_count = None
                                        self.one_way_count = None
                                        self.one_way_sd_min = None
                                        self.one_way_sd_max = None
                                        self.one_way_sd_sum = None
                                        self.one_way_sd_sum2 = None
                                        self.one_way_ds_min = None
                                        self.one_way_ds_max = None
                                        self.one_way_ds_sum = None
                                        self.one_way_ds_sum2 = None
                                        self._segment_path = lambda: "udp-jitter-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Target.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                        class Hops(Entity):
                            """
                            Latest statistics for hops in a
                            path\-enabled operation
                            
                            .. attribute:: hop
                            
                            	Latest stats for a hop in a path\-enabled operation
                            	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops, self).__init__()

                                self.yang_name = "hops"
                                self.yang_parent_name = "latest"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("hop", ("hop", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop))])
                                self._leafs = OrderedDict()

                                self.hop = YList(self)
                                self._segment_path = lambda: "hops"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops, [], name, value)


                            class Hop(Entity):
                                """
                                Latest stats for a hop in a path\-enabled
                                operation
                                
                                .. attribute:: hop_index  (key)
                                
                                	Hop Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: common_stats
                                
                                	Common Stats
                                	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.CommonStats>`
                                
                                .. attribute:: specific_stats
                                
                                	Operation Specific Stats
                                	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop, self).__init__()

                                    self.yang_name = "hop"
                                    self.yang_parent_name = "hops"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['hop_index']
                                    self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats))])
                                    self._leafs = OrderedDict([
                                        ('hop_index', (YLeaf(YType.uint32, 'hop-index'), ['int'])),
                                    ])
                                    self.hop_index = None

                                    self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.CommonStats()
                                    self.common_stats.parent = self
                                    self._children_name_map["common_stats"] = "common-stats"

                                    self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats()
                                    self.specific_stats.parent = self
                                    self._children_name_map["specific_stats"] = "specific-stats"
                                    self._segment_path = lambda: "hop" + "[hop-index='" + str(self.hop_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop, ['hop_index'], name, value)


                                class CommonStats(Entity):
                                    """
                                    Common Stats
                                    
                                    .. attribute:: operation_time
                                    
                                    	Operation Time
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: return_code
                                    
                                    	Return code
                                    	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                    
                                    .. attribute:: response_time_count
                                    
                                    	Number of RTT samples used for the statistics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: response_time
                                    
                                    	RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: min_response_time
                                    
                                    	Minimum RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: max_response_time
                                    
                                    	Maximum RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sum_response_time
                                    
                                    	Sum of RTT
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sum2_response_time
                                    
                                    	Sum of RTT^2
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: update_count
                                    
                                    	Number of updates processed
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ok_count
                                    
                                    	Number of updates with Okay return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: disconnect_count
                                    
                                    	Number of updates with Disconnected return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: timeout_count
                                    
                                    	Number of updates with Timeout return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: busy_count
                                    
                                    	Number of updates with Busy return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: no_connection_count
                                    
                                    	Number of updates with NotConnected return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: dropped_count
                                    
                                    	Number of updates with Dropped return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: internal_error_count
                                    
                                    	Number of updates with InternalError return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sequence_error_count
                                    
                                    	Number of updates with SeqError return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: verify_error_count
                                    
                                    	Number of updates with VerifyError return code
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.CommonStats, self).__init__()

                                        self.yang_name = "common-stats"
                                        self.yang_parent_name = "hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                            ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                            ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                            ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                            ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                            ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                            ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                            ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                            ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                            ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                            ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                            ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                            ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                            ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                            ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                            ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                            ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                            ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                        ])
                                        self.operation_time = None
                                        self.return_code = None
                                        self.response_time_count = None
                                        self.response_time = None
                                        self.min_response_time = None
                                        self.max_response_time = None
                                        self.sum_response_time = None
                                        self.sum2_response_time = None
                                        self.update_count = None
                                        self.ok_count = None
                                        self.disconnect_count = None
                                        self.timeout_count = None
                                        self.busy_count = None
                                        self.no_connection_count = None
                                        self.dropped_count = None
                                        self.internal_error_count = None
                                        self.sequence_error_count = None
                                        self.verify_error_count = None
                                        self._segment_path = lambda: "common-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                class SpecificStats(Entity):
                                    """
                                    Operation Specific Stats
                                    
                                    .. attribute:: icmp_path_jitter_stats
                                    
                                    	icmp path jitter stats
                                    	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.IcmpPathJitterStats>`
                                    
                                    .. attribute:: udp_jitter_stats
                                    
                                    	udp jitter stats
                                    	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.UdpJitterStats>`
                                    
                                    .. attribute:: op_type
                                    
                                    	op type
                                    	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats, self).__init__()

                                        self.yang_name = "specific-stats"
                                        self.yang_parent_name = "hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.UdpJitterStats))])
                                        self._leafs = OrderedDict([
                                            ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                        ])
                                        self.op_type = None

                                        self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.IcmpPathJitterStats()
                                        self.icmp_path_jitter_stats.parent = self
                                        self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                        self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.UdpJitterStats()
                                        self.udp_jitter_stats.parent = self
                                        self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                        self._segment_path = lambda: "specific-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats, [u'op_type'], name, value)


                                    class IcmpPathJitterStats(Entity):
                                        """
                                        icmp path jitter stats
                                        
                                        .. attribute:: source_address
                                        
                                        	IP Address of the source
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: dest_address
                                        
                                        	IP Address of the destination
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: hop_address
                                        
                                        	IP address of the hop in the path
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: packet_interval
                                        
                                        	Interval between echos in ms
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: response_time_count
                                        
                                        	Number of RTT samples  used for the statistics
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: response_time
                                        
                                        	RTT
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: min_response_time
                                        
                                        	Minimum RTT
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: max_response_time
                                        
                                        	Maximum RTT
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: sum_response_time
                                        
                                        	Sum of RTT
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: sum2_response_time
                                        
                                        	Sum of RTT^2
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: packet_count
                                        
                                        	Number of Echo replies received 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_loss_count
                                        
                                        	Number of packets lost
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: out_of_sequence_count
                                        
                                        	Number of out of sequence packets
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: discarded_sample_count
                                        
                                        	Number of discarded samples
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: verify_errors_count
                                        
                                        	Number of packets with data corruption
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: dropped_error_count
                                        
                                        	Number of packets dropped
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: jitter
                                        
                                        	Jitter value for this node in the path
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pos_jitter_sum
                                        
                                        	Sum of positive jitter value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pos_jitter_sum2
                                        
                                        	Sum of squares of positive jitter values
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: pos_jitter_min
                                        
                                        	Minimum positive jitter value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pos_jitter_max
                                        
                                        	Maximum positive jitter value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pos_jitter_count
                                        
                                        	Number of positive jitter values
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: neg_jitter_sum
                                        
                                        	Sum of negative jitter values
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: neg_jitter_min
                                        
                                        	Minimum negative jitter value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: neg_jitter_max
                                        
                                        	Maximum negative jitter value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: neg_jitter_sum2
                                        
                                        	Sum of squares of negative jitter values
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: neg_jitter_count
                                        
                                        	Number of negative jitter values
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.IcmpPathJitterStats, self).__init__()

                                            self.yang_name = "icmp-path-jitter-stats"
                                            self.yang_parent_name = "specific-stats"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                            ])
                                            self.source_address = None
                                            self.dest_address = None
                                            self.hop_address = None
                                            self.packet_interval = None
                                            self.response_time_count = None
                                            self.response_time = None
                                            self.min_response_time = None
                                            self.max_response_time = None
                                            self.sum_response_time = None
                                            self.sum2_response_time = None
                                            self.packet_count = None
                                            self.packet_loss_count = None
                                            self.out_of_sequence_count = None
                                            self.discarded_sample_count = None
                                            self.verify_errors_count = None
                                            self.dropped_error_count = None
                                            self.jitter = None
                                            self.pos_jitter_sum = None
                                            self.pos_jitter_sum2 = None
                                            self.pos_jitter_min = None
                                            self.pos_jitter_max = None
                                            self.pos_jitter_count = None
                                            self.neg_jitter_sum = None
                                            self.neg_jitter_min = None
                                            self.neg_jitter_max = None
                                            self.neg_jitter_sum2 = None
                                            self.neg_jitter_count = None
                                            self._segment_path = lambda: "icmp-path-jitter-stats"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                    class UdpJitterStats(Entity):
                                        """
                                        udp jitter stats
                                        
                                        .. attribute:: jitter_in
                                        
                                        	Input Jitter moving average, computed as per RFC1889
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: jitter_out
                                        
                                        	Output Jitter moving average, computed as per RFC1889
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_loss_sd
                                        
                                        	Packets lost in source to destination (SD) direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_loss_ds
                                        
                                        	Packets lost in destination to source (DS) direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_out_of_sequence
                                        
                                        	Packets out of sequence
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_mia
                                        
                                        	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_skipped
                                        
                                        	Packets which are skipped
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_late_arrivals
                                        
                                        	Packets arriving late
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: packet_invalid_tstamp
                                        
                                        	Packets with bad timestamps
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: internal_errors_count
                                        
                                        	Number of internal errors
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: busies_count
                                        
                                        	Number of busies
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_sd_sum
                                        
                                        	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: positive_sd_sum2
                                        
                                        	Sum of squares of positive jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: positive_sd_min
                                        
                                        	Minimum of positive jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_sd_max
                                        
                                        	Maximum of positive jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_sd_count
                                        
                                        	Number of positive jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_sd_sum
                                        
                                        	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: negative_sd_sum2
                                        
                                        	Sum of squares of negative jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: negative_sd_min
                                        
                                        	Minimum of negative jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_sd_max
                                        
                                        	Maximum of negative jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_sd_count
                                        
                                        	Number of negative jitter values in SD direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_ds_sum
                                        
                                        	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: positive_ds_sum2
                                        
                                        	Sum of squares of positive jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: positive_ds_min
                                        
                                        	Minimum of positive jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_ds_max
                                        
                                        	Maximum of positive jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: positive_ds_count
                                        
                                        	Number of positive jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_ds_sum
                                        
                                        	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: millisecond
                                        
                                        .. attribute:: negative_ds_sum2
                                        
                                        	Sum of squares of negative jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: negative_ds_min
                                        
                                        	Minimum of negative jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_ds_max
                                        
                                        	Maximum of negative jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: negative_ds_count
                                        
                                        	Number of negative jitter values in DS direction
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_count
                                        
                                        	Number of probe/probe\-response pairs used to compute one\-way statistics
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_sd_min
                                        
                                        	Minimum of one\-way jitter values in SD direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_sd_max
                                        
                                        	Maximum of one\-way jitter values in SD direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_sd_sum
                                        
                                        	Sum of one\-way jitter values in SD direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_sd_sum2
                                        
                                        	Sum of squares of one\-way jitter values in SD direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: one_way_ds_min
                                        
                                        	Minimum of one\-way jitter values in DS direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_ds_max
                                        
                                        	Maximum of one\-way jitter values in DS direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_ds_sum
                                        
                                        	Sum of one\-way jitter values in DS direction (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: one_way_ds_sum2
                                        
                                        	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.UdpJitterStats, self).__init__()

                                            self.yang_name = "udp-jitter-stats"
                                            self.yang_parent_name = "specific-stats"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                            ])
                                            self.jitter_in = None
                                            self.jitter_out = None
                                            self.packet_loss_sd = None
                                            self.packet_loss_ds = None
                                            self.packet_out_of_sequence = None
                                            self.packet_mia = None
                                            self.packet_skipped = None
                                            self.packet_late_arrivals = None
                                            self.packet_invalid_tstamp = None
                                            self.internal_errors_count = None
                                            self.busies_count = None
                                            self.positive_sd_sum = None
                                            self.positive_sd_sum2 = None
                                            self.positive_sd_min = None
                                            self.positive_sd_max = None
                                            self.positive_sd_count = None
                                            self.negative_sd_sum = None
                                            self.negative_sd_sum2 = None
                                            self.negative_sd_min = None
                                            self.negative_sd_max = None
                                            self.negative_sd_count = None
                                            self.positive_ds_sum = None
                                            self.positive_ds_sum2 = None
                                            self.positive_ds_min = None
                                            self.positive_ds_max = None
                                            self.positive_ds_count = None
                                            self.negative_ds_sum = None
                                            self.negative_ds_sum2 = None
                                            self.negative_ds_min = None
                                            self.negative_ds_max = None
                                            self.negative_ds_count = None
                                            self.one_way_count = None
                                            self.one_way_sd_min = None
                                            self.one_way_sd_max = None
                                            self.one_way_sd_sum = None
                                            self.one_way_sd_sum2 = None
                                            self.one_way_ds_min = None
                                            self.one_way_ds_max = None
                                            self.one_way_ds_sum = None
                                            self.one_way_ds_sum2 = None
                                            self._segment_path = lambda: "udp-jitter-stats"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.Hops.Hop.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                        class LpdPaths(Entity):
                            """
                            List of latest LPD paths
                            
                            .. attribute:: lpd_path
                            
                            	Latest path statistics of MPLS LSP group operation
                            	**type**\: list of  		 :py:class:`LpdPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths, self).__init__()

                                self.yang_name = "lpd-paths"
                                self.yang_parent_name = "latest"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lpd-path", ("lpd_path", Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath))])
                                self._leafs = OrderedDict()

                                self.lpd_path = YList(self)
                                self._segment_path = lambda: "lpd-paths"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths, [], name, value)


                            class LpdPath(Entity):
                                """
                                Latest path statistics of MPLS LSP group
                                operation
                                
                                .. attribute:: path_index  (key)
                                
                                	LPD path index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: path_id
                                
                                	LPD path identifier
                                	**type**\:  :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath.PathId>`
                                
                                .. attribute:: return_code
                                
                                	Path return code
                                	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath, self).__init__()

                                    self.yang_name = "lpd-path"
                                    self.yang_parent_name = "lpd-paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['path_index']
                                    self._child_classes = OrderedDict([("path-id", ("path_id", Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath.PathId))])
                                    self._leafs = OrderedDict([
                                        ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                        ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                    ])
                                    self.path_index = None
                                    self.return_code = None

                                    self.path_id = Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath.PathId()
                                    self.path_id.parent = self
                                    self._children_name_map["path_id"] = "path-id"
                                    self._segment_path = lambda: "lpd-path" + "[path-index='" + str(self.path_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath, ['path_index', u'return_code'], name, value)


                                class PathId(Entity):
                                    """
                                    LPD path identifier
                                    
                                    .. attribute:: lsp_selector
                                    
                                    	LSP selector
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: output_interface
                                    
                                    	Output interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: nexthop_address
                                    
                                    	Nexthop address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: downstream_label
                                    
                                    	Downstream label stacks
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath.PathId, self).__init__()

                                        self.yang_name = "path-id"
                                        self.yang_parent_name = "lpd-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                            ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                            ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                            ('downstream_label', (YLeafList(YType.uint32, 'downstream-label'), ['int'])),
                                        ])
                                        self.lsp_selector = None
                                        self.output_interface = None
                                        self.nexthop_address = None
                                        self.downstream_label = []
                                        self._segment_path = lambda: "path-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Latest.LpdPaths.LpdPath.PathId, [u'lsp_selector', u'output_interface', u'nexthop_address', u'downstream_label'], name, value)


                    class Aggregated(Entity):
                        """
                        Statistics aggregated for data collected
                        over time intervals
                        
                        .. attribute:: enhanced_intervals
                        
                        	Table of statistics aggregated over enhanced intervals
                        	**type**\:  :py:class:`EnhancedIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals>`
                        
                        .. attribute:: hours
                        
                        	Table of statistics aggregated over 1\-hour intervals
                        	**type**\:  :py:class:`Hours <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours>`
                        
                        

                        """

                        _prefix = 'man-ipsla-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated, self).__init__()

                            self.yang_name = "aggregated"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("enhanced-intervals", ("enhanced_intervals", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals)), ("hours", ("hours", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours))])
                            self._leafs = OrderedDict()

                            self.enhanced_intervals = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals()
                            self.enhanced_intervals.parent = self
                            self._children_name_map["enhanced_intervals"] = "enhanced-intervals"

                            self.hours = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours()
                            self.hours.parent = self
                            self._children_name_map["hours"] = "hours"
                            self._segment_path = lambda: "aggregated"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated, [], name, value)


                        class EnhancedIntervals(Entity):
                            """
                            Table of statistics aggregated over
                            enhanced intervals
                            
                            .. attribute:: enhanced_interval
                            
                            	Statistics aggregated over an interval specified in seconds. Specified interval must be a multiple of the operation frequency
                            	**type**\: list of  		 :py:class:`EnhancedInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals, self).__init__()

                                self.yang_name = "enhanced-intervals"
                                self.yang_parent_name = "aggregated"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enhanced-interval", ("enhanced_interval", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval))])
                                self._leafs = OrderedDict()

                                self.enhanced_interval = YList(self)
                                self._segment_path = lambda: "enhanced-intervals"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals, [], name, value)


                            class EnhancedInterval(Entity):
                                """
                                Statistics aggregated over an interval
                                specified in seconds. Specified interval
                                must be a multiple of the operation
                                frequency
                                
                                .. attribute:: enhanced_interval  (key)
                                
                                	Enhanced Interval in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: start_times
                                
                                	Table of start times for the intervals
                                	**type**\:  :py:class:`StartTimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval, self).__init__()

                                    self.yang_name = "enhanced-interval"
                                    self.yang_parent_name = "enhanced-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['enhanced_interval']
                                    self._child_classes = OrderedDict([("start-times", ("start_times", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes))])
                                    self._leafs = OrderedDict([
                                        ('enhanced_interval', (YLeaf(YType.uint32, 'enhanced-interval'), ['int'])),
                                    ])
                                    self.enhanced_interval = None

                                    self.start_times = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes()
                                    self.start_times.parent = self
                                    self._children_name_map["start_times"] = "start-times"
                                    self._segment_path = lambda: "enhanced-interval" + "[enhanced-interval='" + str(self.enhanced_interval) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval, ['enhanced_interval'], name, value)


                                class StartTimes(Entity):
                                    """
                                    Table of start times for the intervals
                                    
                                    .. attribute:: start_time
                                    
                                    	Statistics aggregated over an enhanced interval which starts at a specific time
                                    	**type**\: list of  		 :py:class:`StartTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes, self).__init__()

                                        self.yang_name = "start-times"
                                        self.yang_parent_name = "enhanced-interval"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("start-time", ("start_time", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime))])
                                        self._leafs = OrderedDict()

                                        self.start_time = YList(self)
                                        self._segment_path = lambda: "start-times"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes, [], name, value)


                                    class StartTime(Entity):
                                        """
                                        Statistics aggregated over an enhanced
                                        interval which starts at a specific time
                                        
                                        .. attribute:: interval_start_time  (key)
                                        
                                        	Interval Start Time
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: common_stats
                                        
                                        	Common Stats
                                        	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.CommonStats>`
                                        
                                        .. attribute:: specific_stats
                                        
                                        	Operation Specific Stats
                                        	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime, self).__init__()

                                            self.yang_name = "start-time"
                                            self.yang_parent_name = "start-times"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['interval_start_time']
                                            self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats))])
                                            self._leafs = OrderedDict([
                                                ('interval_start_time', (YLeaf(YType.str, 'interval-start-time'), ['str'])),
                                            ])
                                            self.interval_start_time = None

                                            self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.CommonStats()
                                            self.common_stats.parent = self
                                            self._children_name_map["common_stats"] = "common-stats"

                                            self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats()
                                            self.specific_stats.parent = self
                                            self._children_name_map["specific_stats"] = "specific-stats"
                                            self._segment_path = lambda: "start-time" + "[interval-start-time='" + str(self.interval_start_time) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime, ['interval_start_time'], name, value)


                                        class CommonStats(Entity):
                                            """
                                            Common Stats
                                            
                                            .. attribute:: operation_time
                                            
                                            	Operation Time
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: return_code
                                            
                                            	Return code
                                            	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                            
                                            .. attribute:: response_time_count
                                            
                                            	Number of RTT samples used for the statistics
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: response_time
                                            
                                            	RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: min_response_time
                                            
                                            	Minimum RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: max_response_time
                                            
                                            	Maximum RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sum_response_time
                                            
                                            	Sum of RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sum2_response_time
                                            
                                            	Sum of RTT^2
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: update_count
                                            
                                            	Number of updates processed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: ok_count
                                            
                                            	Number of updates with Okay return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: disconnect_count
                                            
                                            	Number of updates with Disconnected return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: timeout_count
                                            
                                            	Number of updates with Timeout return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: busy_count
                                            
                                            	Number of updates with Busy return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: no_connection_count
                                            
                                            	Number of updates with NotConnected return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: dropped_count
                                            
                                            	Number of updates with Dropped return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: internal_error_count
                                            
                                            	Number of updates with InternalError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sequence_error_count
                                            
                                            	Number of updates with SeqError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: verify_error_count
                                            
                                            	Number of updates with VerifyError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.CommonStats, self).__init__()

                                                self.yang_name = "common-stats"
                                                self.yang_parent_name = "start-time"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                                    ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                    ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                    ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                    ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                    ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                    ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                    ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                    ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                                    ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                                    ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                                    ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                                    ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                                    ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                                    ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                                    ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                                    ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                                    ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                                ])
                                                self.operation_time = None
                                                self.return_code = None
                                                self.response_time_count = None
                                                self.response_time = None
                                                self.min_response_time = None
                                                self.max_response_time = None
                                                self.sum_response_time = None
                                                self.sum2_response_time = None
                                                self.update_count = None
                                                self.ok_count = None
                                                self.disconnect_count = None
                                                self.timeout_count = None
                                                self.busy_count = None
                                                self.no_connection_count = None
                                                self.dropped_count = None
                                                self.internal_error_count = None
                                                self.sequence_error_count = None
                                                self.verify_error_count = None
                                                self._segment_path = lambda: "common-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                        class SpecificStats(Entity):
                                            """
                                            Operation Specific Stats
                                            
                                            .. attribute:: icmp_path_jitter_stats
                                            
                                            	icmp path jitter stats
                                            	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.IcmpPathJitterStats>`
                                            
                                            .. attribute:: udp_jitter_stats
                                            
                                            	udp jitter stats
                                            	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.UdpJitterStats>`
                                            
                                            .. attribute:: op_type
                                            
                                            	op type
                                            	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats, self).__init__()

                                                self.yang_name = "specific-stats"
                                                self.yang_parent_name = "start-time"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.UdpJitterStats))])
                                                self._leafs = OrderedDict([
                                                    ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                                ])
                                                self.op_type = None

                                                self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.IcmpPathJitterStats()
                                                self.icmp_path_jitter_stats.parent = self
                                                self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                                self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.UdpJitterStats()
                                                self.udp_jitter_stats.parent = self
                                                self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                                self._segment_path = lambda: "specific-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats, [u'op_type'], name, value)


                                            class IcmpPathJitterStats(Entity):
                                                """
                                                icmp path jitter stats
                                                
                                                .. attribute:: source_address
                                                
                                                	IP Address of the source
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: dest_address
                                                
                                                	IP Address of the destination
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: hop_address
                                                
                                                	IP address of the hop in the path
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: packet_interval
                                                
                                                	Interval between echos in ms
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: response_time_count
                                                
                                                	Number of RTT samples  used for the statistics
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: response_time
                                                
                                                	RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: min_response_time
                                                
                                                	Minimum RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: max_response_time
                                                
                                                	Maximum RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: sum_response_time
                                                
                                                	Sum of RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: sum2_response_time
                                                
                                                	Sum of RTT^2
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: packet_count
                                                
                                                	Number of Echo replies received 
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_count
                                                
                                                	Number of packets lost
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: out_of_sequence_count
                                                
                                                	Number of out of sequence packets
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: discarded_sample_count
                                                
                                                	Number of discarded samples
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: verify_errors_count
                                                
                                                	Number of packets with data corruption
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: dropped_error_count
                                                
                                                	Number of packets dropped
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: jitter
                                                
                                                	Jitter value for this node in the path
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_sum
                                                
                                                	Sum of positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_sum2
                                                
                                                	Sum of squares of positive jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: pos_jitter_min
                                                
                                                	Minimum positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_max
                                                
                                                	Maximum positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_count
                                                
                                                	Number of positive jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_sum
                                                
                                                	Sum of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_min
                                                
                                                	Minimum negative jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_max
                                                
                                                	Maximum negative jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_sum2
                                                
                                                	Sum of squares of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: neg_jitter_count
                                                
                                                	Number of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.IcmpPathJitterStats, self).__init__()

                                                    self.yang_name = "icmp-path-jitter-stats"
                                                    self.yang_parent_name = "specific-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                        ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                        ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                        ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                        ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                        ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                        ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                        ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                        ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                        ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                        ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                        ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                        ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                        ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                        ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                        ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                        ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                        ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                        ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                        ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                        ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                        ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                        ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                        ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                        ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                        ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                                    ])
                                                    self.source_address = None
                                                    self.dest_address = None
                                                    self.hop_address = None
                                                    self.packet_interval = None
                                                    self.response_time_count = None
                                                    self.response_time = None
                                                    self.min_response_time = None
                                                    self.max_response_time = None
                                                    self.sum_response_time = None
                                                    self.sum2_response_time = None
                                                    self.packet_count = None
                                                    self.packet_loss_count = None
                                                    self.out_of_sequence_count = None
                                                    self.discarded_sample_count = None
                                                    self.verify_errors_count = None
                                                    self.dropped_error_count = None
                                                    self.jitter = None
                                                    self.pos_jitter_sum = None
                                                    self.pos_jitter_sum2 = None
                                                    self.pos_jitter_min = None
                                                    self.pos_jitter_max = None
                                                    self.pos_jitter_count = None
                                                    self.neg_jitter_sum = None
                                                    self.neg_jitter_min = None
                                                    self.neg_jitter_max = None
                                                    self.neg_jitter_sum2 = None
                                                    self.neg_jitter_count = None
                                                    self._segment_path = lambda: "icmp-path-jitter-stats"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                            class UdpJitterStats(Entity):
                                                """
                                                udp jitter stats
                                                
                                                .. attribute:: jitter_in
                                                
                                                	Input Jitter moving average, computed as per RFC1889
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: jitter_out
                                                
                                                	Output Jitter moving average, computed as per RFC1889
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_sd
                                                
                                                	Packets lost in source to destination (SD) direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_ds
                                                
                                                	Packets lost in destination to source (DS) direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_out_of_sequence
                                                
                                                	Packets out of sequence
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_mia
                                                
                                                	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_skipped
                                                
                                                	Packets which are skipped
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_late_arrivals
                                                
                                                	Packets arriving late
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_invalid_tstamp
                                                
                                                	Packets with bad timestamps
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: internal_errors_count
                                                
                                                	Number of internal errors
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: busies_count
                                                
                                                	Number of busies
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_sum
                                                
                                                	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: positive_sd_sum2
                                                
                                                	Sum of squares of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: positive_sd_min
                                                
                                                	Minimum of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_max
                                                
                                                	Maximum of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_count
                                                
                                                	Number of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_sum
                                                
                                                	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: negative_sd_sum2
                                                
                                                	Sum of squares of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: negative_sd_min
                                                
                                                	Minimum of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_max
                                                
                                                	Maximum of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_count
                                                
                                                	Number of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_sum
                                                
                                                	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: positive_ds_sum2
                                                
                                                	Sum of squares of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: positive_ds_min
                                                
                                                	Minimum of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_max
                                                
                                                	Maximum of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_count
                                                
                                                	Number of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_sum
                                                
                                                	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: negative_ds_sum2
                                                
                                                	Sum of squares of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: negative_ds_min
                                                
                                                	Minimum of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_max
                                                
                                                	Maximum of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_count
                                                
                                                	Number of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_count
                                                
                                                	Number of probe/probe\-response pairs used to compute one\-way statistics
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_min
                                                
                                                	Minimum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_max
                                                
                                                	Maximum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_sum
                                                
                                                	Sum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_sum2
                                                
                                                	Sum of squares of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: one_way_ds_min
                                                
                                                	Minimum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_max
                                                
                                                	Maximum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_sum
                                                
                                                	Sum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_sum2
                                                
                                                	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.UdpJitterStats, self).__init__()

                                                    self.yang_name = "udp-jitter-stats"
                                                    self.yang_parent_name = "specific-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                        ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                        ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                        ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                        ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                        ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                        ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                        ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                        ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                        ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                        ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                        ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                        ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                        ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                        ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                        ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                        ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                        ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                        ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                        ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                        ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                        ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                        ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                        ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                        ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                        ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                        ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                        ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                        ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                        ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                        ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                        ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                        ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                        ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                        ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                        ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                        ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                        ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                        ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                        ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                                    ])
                                                    self.jitter_in = None
                                                    self.jitter_out = None
                                                    self.packet_loss_sd = None
                                                    self.packet_loss_ds = None
                                                    self.packet_out_of_sequence = None
                                                    self.packet_mia = None
                                                    self.packet_skipped = None
                                                    self.packet_late_arrivals = None
                                                    self.packet_invalid_tstamp = None
                                                    self.internal_errors_count = None
                                                    self.busies_count = None
                                                    self.positive_sd_sum = None
                                                    self.positive_sd_sum2 = None
                                                    self.positive_sd_min = None
                                                    self.positive_sd_max = None
                                                    self.positive_sd_count = None
                                                    self.negative_sd_sum = None
                                                    self.negative_sd_sum2 = None
                                                    self.negative_sd_min = None
                                                    self.negative_sd_max = None
                                                    self.negative_sd_count = None
                                                    self.positive_ds_sum = None
                                                    self.positive_ds_sum2 = None
                                                    self.positive_ds_min = None
                                                    self.positive_ds_max = None
                                                    self.positive_ds_count = None
                                                    self.negative_ds_sum = None
                                                    self.negative_ds_sum2 = None
                                                    self.negative_ds_min = None
                                                    self.negative_ds_max = None
                                                    self.negative_ds_count = None
                                                    self.one_way_count = None
                                                    self.one_way_sd_min = None
                                                    self.one_way_sd_max = None
                                                    self.one_way_sd_sum = None
                                                    self.one_way_sd_sum2 = None
                                                    self.one_way_ds_min = None
                                                    self.one_way_ds_max = None
                                                    self.one_way_ds_sum = None
                                                    self.one_way_ds_sum2 = None
                                                    self._segment_path = lambda: "udp-jitter-stats"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.EnhancedIntervals.EnhancedInterval.StartTimes.StartTime.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                        class Hours(Entity):
                            """
                            Table of statistics aggregated over 1\-hour
                            intervals
                            
                            .. attribute:: hour
                            
                            	Statistics aggregated for a 1\-hour interval
                            	**type**\: list of  		 :py:class:`Hour <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour>`
                            
                            

                            """

                            _prefix = 'man-ipsla-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours, self).__init__()

                                self.yang_name = "hours"
                                self.yang_parent_name = "aggregated"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("hour", ("hour", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour))])
                                self._leafs = OrderedDict()

                                self.hour = YList(self)
                                self._segment_path = lambda: "hours"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours, [], name, value)


                            class Hour(Entity):
                                """
                                Statistics aggregated for a 1\-hour
                                interval
                                
                                .. attribute:: hour_index  (key)
                                
                                	Hour Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: distributed
                                
                                	Statistics aggregated on distribution value intervals for in 1\-hour intervals
                                	**type**\:  :py:class:`Distributed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed>`
                                
                                .. attribute:: non_distributed
                                
                                	Statistics aggregated for the total range of values in 1\-hour intervals
                                	**type**\:  :py:class:`NonDistributed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed>`
                                
                                

                                """

                                _prefix = 'man-ipsla-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour, self).__init__()

                                    self.yang_name = "hour"
                                    self.yang_parent_name = "hours"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['hour_index']
                                    self._child_classes = OrderedDict([("distributed", ("distributed", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed)), ("non-distributed", ("non_distributed", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed))])
                                    self._leafs = OrderedDict([
                                        ('hour_index', (YLeaf(YType.uint32, 'hour-index'), ['int'])),
                                    ])
                                    self.hour_index = None

                                    self.distributed = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed()
                                    self.distributed.parent = self
                                    self._children_name_map["distributed"] = "distributed"

                                    self.non_distributed = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed()
                                    self.non_distributed.parent = self
                                    self._children_name_map["non_distributed"] = "non-distributed"
                                    self._segment_path = lambda: "hour" + "[hour-index='" + str(self.hour_index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour, ['hour_index'], name, value)


                                class Distributed(Entity):
                                    """
                                    Statistics aggregated on distribution
                                    value intervals for in 1\-hour intervals
                                    
                                    .. attribute:: paths
                                    
                                    	Table of paths identified in the 1\-hour interval
                                    	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths>`
                                    
                                    .. attribute:: target
                                    
                                    	Distribution statistics for the target node
                                    	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed, self).__init__()

                                        self.yang_name = "distributed"
                                        self.yang_parent_name = "hour"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("paths", ("paths", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths)), ("target", ("target", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target))])
                                        self._leafs = OrderedDict()

                                        self.paths = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths()
                                        self.paths.parent = self
                                        self._children_name_map["paths"] = "paths"

                                        self.target = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target()
                                        self.target.parent = self
                                        self._children_name_map["target"] = "target"
                                        self._segment_path = lambda: "distributed"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed, [], name, value)


                                    class Paths(Entity):
                                        """
                                        Table of paths identified in the 1\-hour
                                        interval
                                        
                                        .. attribute:: path
                                        
                                        	Paths identified in a 1\-hour interval
                                        	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths, self).__init__()

                                            self.yang_name = "paths"
                                            self.yang_parent_name = "distributed"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("path", ("path", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path))])
                                            self._leafs = OrderedDict()

                                            self.path = YList(self)
                                            self._segment_path = lambda: "paths"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths, [], name, value)


                                        class Path(Entity):
                                            """
                                            Paths identified in a 1\-hour interval
                                            
                                            .. attribute:: path_index  (key)
                                            
                                            	Path Index
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: hops
                                            
                                            	Table of hops for a particular path
                                            	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path, self).__init__()

                                                self.yang_name = "path"
                                                self.yang_parent_name = "paths"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['path_index']
                                                self._child_classes = OrderedDict([("hops", ("hops", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops))])
                                                self._leafs = OrderedDict([
                                                    ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                                ])
                                                self.path_index = None

                                                self.hops = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops()
                                                self.hops.parent = self
                                                self._children_name_map["hops"] = "hops"
                                                self._segment_path = lambda: "path" + "[path-index='" + str(self.path_index) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path, ['path_index'], name, value)


                                            class Hops(Entity):
                                                """
                                                Table of hops for a particular path
                                                
                                                .. attribute:: hop
                                                
                                                	1\-hour aggregated statistics for a hop in a path\-enabled operation
                                                	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop>`
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops, self).__init__()

                                                    self.yang_name = "hops"
                                                    self.yang_parent_name = "path"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("hop", ("hop", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop))])
                                                    self._leafs = OrderedDict()

                                                    self.hop = YList(self)
                                                    self._segment_path = lambda: "hops"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops, [], name, value)


                                                class Hop(Entity):
                                                    """
                                                    1\-hour aggregated statistics for a
                                                    hop in a path\-enabled operation
                                                    
                                                    .. attribute:: hop_index  (key)
                                                    
                                                    	Hop Index
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: distribution_intervals
                                                    
                                                    	Table of distribution intervals for a particular hop
                                                    	**type**\:  :py:class:`DistributionIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'man-ipsla-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop, self).__init__()

                                                        self.yang_name = "hop"
                                                        self.yang_parent_name = "hops"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['hop_index']
                                                        self._child_classes = OrderedDict([("distribution-intervals", ("distribution_intervals", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals))])
                                                        self._leafs = OrderedDict([
                                                            ('hop_index', (YLeaf(YType.uint32, 'hop-index'), ['int'])),
                                                        ])
                                                        self.hop_index = None

                                                        self.distribution_intervals = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals()
                                                        self.distribution_intervals.parent = self
                                                        self._children_name_map["distribution_intervals"] = "distribution-intervals"
                                                        self._segment_path = lambda: "hop" + "[hop-index='" + str(self.hop_index) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop, ['hop_index'], name, value)


                                                    class DistributionIntervals(Entity):
                                                        """
                                                        Table of distribution intervals for a particular
                                                        hop
                                                        
                                                        .. attribute:: distribution_interval
                                                        
                                                        	1\-hour aggregated statistics for a hop in a path\-enabled operation
                                                        	**type**\: list of  		 :py:class:`DistributionInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals, self).__init__()

                                                            self.yang_name = "distribution-intervals"
                                                            self.yang_parent_name = "hop"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("distribution-interval", ("distribution_interval", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval))])
                                                            self._leafs = OrderedDict()

                                                            self.distribution_interval = YList(self)
                                                            self._segment_path = lambda: "distribution-intervals"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals, [], name, value)


                                                        class DistributionInterval(Entity):
                                                            """
                                                            1\-hour aggregated statistics for a hop in a
                                                            path\-enabled operation
                                                            
                                                            .. attribute:: distribution_index  (key)
                                                            
                                                            	Distribution Interval
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: common_stats
                                                            
                                                            	Common Stats
                                                            	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.CommonStats>`
                                                            
                                                            .. attribute:: specific_stats
                                                            
                                                            	Operation Specific Stats
                                                            	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'man-ipsla-oper'
                                                            _revision = '2015-11-09'

                                                            def __init__(self):
                                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval, self).__init__()

                                                                self.yang_name = "distribution-interval"
                                                                self.yang_parent_name = "distribution-intervals"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = ['distribution_index']
                                                                self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats))])
                                                                self._leafs = OrderedDict([
                                                                    ('distribution_index', (YLeaf(YType.uint32, 'distribution-index'), ['int'])),
                                                                ])
                                                                self.distribution_index = None

                                                                self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.CommonStats()
                                                                self.common_stats.parent = self
                                                                self._children_name_map["common_stats"] = "common-stats"

                                                                self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats()
                                                                self.specific_stats.parent = self
                                                                self._children_name_map["specific_stats"] = "specific-stats"
                                                                self._segment_path = lambda: "distribution-interval" + "[distribution-index='" + str(self.distribution_index) + "']"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval, ['distribution_index'], name, value)


                                                            class CommonStats(Entity):
                                                                """
                                                                Common Stats
                                                                
                                                                .. attribute:: operation_time
                                                                
                                                                	Operation Time
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..18446744073709551615
                                                                
                                                                .. attribute:: return_code
                                                                
                                                                	Return code
                                                                	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                                                
                                                                .. attribute:: response_time_count
                                                                
                                                                	Number of RTT samples used for the statistics
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: response_time
                                                                
                                                                	RTT
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: min_response_time
                                                                
                                                                	Minimum RTT
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: max_response_time
                                                                
                                                                	Maximum RTT
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: sum_response_time
                                                                
                                                                	Sum of RTT
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: sum2_response_time
                                                                
                                                                	Sum of RTT^2
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..18446744073709551615
                                                                
                                                                .. attribute:: update_count
                                                                
                                                                	Number of updates processed
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: ok_count
                                                                
                                                                	Number of updates with Okay return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: disconnect_count
                                                                
                                                                	Number of updates with Disconnected return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: timeout_count
                                                                
                                                                	Number of updates with Timeout return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: busy_count
                                                                
                                                                	Number of updates with Busy return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: no_connection_count
                                                                
                                                                	Number of updates with NotConnected return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: dropped_count
                                                                
                                                                	Number of updates with Dropped return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: internal_error_count
                                                                
                                                                	Number of updates with InternalError return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: sequence_error_count
                                                                
                                                                	Number of updates with SeqError return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                .. attribute:: verify_error_count
                                                                
                                                                	Number of updates with VerifyError return code
                                                                	**type**\: int
                                                                
                                                                	**range:** 0..4294967295
                                                                
                                                                

                                                                """

                                                                _prefix = 'man-ipsla-oper'
                                                                _revision = '2015-11-09'

                                                                def __init__(self):
                                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.CommonStats, self).__init__()

                                                                    self.yang_name = "common-stats"
                                                                    self.yang_parent_name = "distribution-interval"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                                                        ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                                        ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                                        ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                                        ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                                        ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                                        ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                                        ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                                                        ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                                                        ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                                                        ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                                                        ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                                                        ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                                                        ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                                                        ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                                                        ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                                                        ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                                                    ])
                                                                    self.operation_time = None
                                                                    self.return_code = None
                                                                    self.response_time_count = None
                                                                    self.response_time = None
                                                                    self.min_response_time = None
                                                                    self.max_response_time = None
                                                                    self.sum_response_time = None
                                                                    self.sum2_response_time = None
                                                                    self.update_count = None
                                                                    self.ok_count = None
                                                                    self.disconnect_count = None
                                                                    self.timeout_count = None
                                                                    self.busy_count = None
                                                                    self.no_connection_count = None
                                                                    self.dropped_count = None
                                                                    self.internal_error_count = None
                                                                    self.sequence_error_count = None
                                                                    self.verify_error_count = None
                                                                    self._segment_path = lambda: "common-stats"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                                            class SpecificStats(Entity):
                                                                """
                                                                Operation Specific Stats
                                                                
                                                                .. attribute:: icmp_path_jitter_stats
                                                                
                                                                	icmp path jitter stats
                                                                	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats>`
                                                                
                                                                .. attribute:: udp_jitter_stats
                                                                
                                                                	udp jitter stats
                                                                	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats>`
                                                                
                                                                .. attribute:: op_type
                                                                
                                                                	op type
                                                                	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'man-ipsla-oper'
                                                                _revision = '2015-11-09'

                                                                def __init__(self):
                                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats, self).__init__()

                                                                    self.yang_name = "specific-stats"
                                                                    self.yang_parent_name = "distribution-interval"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats))])
                                                                    self._leafs = OrderedDict([
                                                                        ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                                                    ])
                                                                    self.op_type = None

                                                                    self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats()
                                                                    self.icmp_path_jitter_stats.parent = self
                                                                    self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                                                    self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats()
                                                                    self.udp_jitter_stats.parent = self
                                                                    self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                                                    self._segment_path = lambda: "specific-stats"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats, [u'op_type'], name, value)


                                                                class IcmpPathJitterStats(Entity):
                                                                    """
                                                                    icmp path jitter stats
                                                                    
                                                                    .. attribute:: source_address
                                                                    
                                                                    	IP Address of the source
                                                                    	**type**\: str
                                                                    
                                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                                    
                                                                    .. attribute:: dest_address
                                                                    
                                                                    	IP Address of the destination
                                                                    	**type**\: str
                                                                    
                                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                                    
                                                                    .. attribute:: hop_address
                                                                    
                                                                    	IP address of the hop in the path
                                                                    	**type**\: str
                                                                    
                                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                                    
                                                                    .. attribute:: packet_interval
                                                                    
                                                                    	Interval between echos in ms
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: response_time_count
                                                                    
                                                                    	Number of RTT samples  used for the statistics
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: response_time
                                                                    
                                                                    	RTT
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: min_response_time
                                                                    
                                                                    	Minimum RTT
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: max_response_time
                                                                    
                                                                    	Maximum RTT
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: sum_response_time
                                                                    
                                                                    	Sum of RTT
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: sum2_response_time
                                                                    
                                                                    	Sum of RTT^2
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: packet_count
                                                                    
                                                                    	Number of Echo replies received 
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_loss_count
                                                                    
                                                                    	Number of packets lost
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: out_of_sequence_count
                                                                    
                                                                    	Number of out of sequence packets
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: discarded_sample_count
                                                                    
                                                                    	Number of discarded samples
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: verify_errors_count
                                                                    
                                                                    	Number of packets with data corruption
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: dropped_error_count
                                                                    
                                                                    	Number of packets dropped
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: jitter
                                                                    
                                                                    	Jitter value for this node in the path
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: pos_jitter_sum
                                                                    
                                                                    	Sum of positive jitter value
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: pos_jitter_sum2
                                                                    
                                                                    	Sum of squares of positive jitter values
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: pos_jitter_min
                                                                    
                                                                    	Minimum positive jitter value
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: pos_jitter_max
                                                                    
                                                                    	Maximum positive jitter value
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: pos_jitter_count
                                                                    
                                                                    	Number of positive jitter values
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: neg_jitter_sum
                                                                    
                                                                    	Sum of negative jitter values
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: neg_jitter_min
                                                                    
                                                                    	Minimum negative jitter value
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: neg_jitter_max
                                                                    
                                                                    	Maximum negative jitter value
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: neg_jitter_sum2
                                                                    
                                                                    	Sum of squares of negative jitter values
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: neg_jitter_count
                                                                    
                                                                    	Number of negative jitter values
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'man-ipsla-oper'
                                                                    _revision = '2015-11-09'

                                                                    def __init__(self):
                                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats, self).__init__()

                                                                        self.yang_name = "icmp-path-jitter-stats"
                                                                        self.yang_parent_name = "specific-stats"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                                            ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                                            ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                                            ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                                            ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                                            ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                                            ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                                            ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                                            ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                                            ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                                            ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                                            ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                                            ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                                            ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                                            ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                                            ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                                            ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                                            ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                                            ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                                            ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                                            ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                                            ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                                            ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                                            ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                                            ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                                            ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                                            ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                                                        ])
                                                                        self.source_address = None
                                                                        self.dest_address = None
                                                                        self.hop_address = None
                                                                        self.packet_interval = None
                                                                        self.response_time_count = None
                                                                        self.response_time = None
                                                                        self.min_response_time = None
                                                                        self.max_response_time = None
                                                                        self.sum_response_time = None
                                                                        self.sum2_response_time = None
                                                                        self.packet_count = None
                                                                        self.packet_loss_count = None
                                                                        self.out_of_sequence_count = None
                                                                        self.discarded_sample_count = None
                                                                        self.verify_errors_count = None
                                                                        self.dropped_error_count = None
                                                                        self.jitter = None
                                                                        self.pos_jitter_sum = None
                                                                        self.pos_jitter_sum2 = None
                                                                        self.pos_jitter_min = None
                                                                        self.pos_jitter_max = None
                                                                        self.pos_jitter_count = None
                                                                        self.neg_jitter_sum = None
                                                                        self.neg_jitter_min = None
                                                                        self.neg_jitter_max = None
                                                                        self.neg_jitter_sum2 = None
                                                                        self.neg_jitter_count = None
                                                                        self._segment_path = lambda: "icmp-path-jitter-stats"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                                                class UdpJitterStats(Entity):
                                                                    """
                                                                    udp jitter stats
                                                                    
                                                                    .. attribute:: jitter_in
                                                                    
                                                                    	Input Jitter moving average, computed as per RFC1889
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: jitter_out
                                                                    
                                                                    	Output Jitter moving average, computed as per RFC1889
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_loss_sd
                                                                    
                                                                    	Packets lost in source to destination (SD) direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_loss_ds
                                                                    
                                                                    	Packets lost in destination to source (DS) direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_out_of_sequence
                                                                    
                                                                    	Packets out of sequence
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_mia
                                                                    
                                                                    	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_skipped
                                                                    
                                                                    	Packets which are skipped
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_late_arrivals
                                                                    
                                                                    	Packets arriving late
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: packet_invalid_tstamp
                                                                    
                                                                    	Packets with bad timestamps
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: internal_errors_count
                                                                    
                                                                    	Number of internal errors
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: busies_count
                                                                    
                                                                    	Number of busies
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_sd_sum
                                                                    
                                                                    	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    	**units**\: millisecond
                                                                    
                                                                    .. attribute:: positive_sd_sum2
                                                                    
                                                                    	Sum of squares of positive jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: positive_sd_min
                                                                    
                                                                    	Minimum of positive jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_sd_max
                                                                    
                                                                    	Maximum of positive jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_sd_count
                                                                    
                                                                    	Number of positive jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_sd_sum
                                                                    
                                                                    	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    	**units**\: millisecond
                                                                    
                                                                    .. attribute:: negative_sd_sum2
                                                                    
                                                                    	Sum of squares of negative jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: negative_sd_min
                                                                    
                                                                    	Minimum of negative jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_sd_max
                                                                    
                                                                    	Maximum of negative jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_sd_count
                                                                    
                                                                    	Number of negative jitter values in SD direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_ds_sum
                                                                    
                                                                    	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    	**units**\: millisecond
                                                                    
                                                                    .. attribute:: positive_ds_sum2
                                                                    
                                                                    	Sum of squares of positive jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: positive_ds_min
                                                                    
                                                                    	Minimum of positive jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_ds_max
                                                                    
                                                                    	Maximum of positive jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: positive_ds_count
                                                                    
                                                                    	Number of positive jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_ds_sum
                                                                    
                                                                    	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    	**units**\: millisecond
                                                                    
                                                                    .. attribute:: negative_ds_sum2
                                                                    
                                                                    	Sum of squares of negative jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: negative_ds_min
                                                                    
                                                                    	Minimum of negative jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_ds_max
                                                                    
                                                                    	Maximum of negative jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: negative_ds_count
                                                                    
                                                                    	Number of negative jitter values in DS direction
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_count
                                                                    
                                                                    	Number of probe/probe\-response pairs used to compute one\-way statistics
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_sd_min
                                                                    
                                                                    	Minimum of one\-way jitter values in SD direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_sd_max
                                                                    
                                                                    	Maximum of one\-way jitter values in SD direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_sd_sum
                                                                    
                                                                    	Sum of one\-way jitter values in SD direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_sd_sum2
                                                                    
                                                                    	Sum of squares of one\-way jitter values in SD direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    .. attribute:: one_way_ds_min
                                                                    
                                                                    	Minimum of one\-way jitter values in DS direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_ds_max
                                                                    
                                                                    	Maximum of one\-way jitter values in DS direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_ds_sum
                                                                    
                                                                    	Sum of one\-way jitter values in DS direction (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..4294967295
                                                                    
                                                                    .. attribute:: one_way_ds_sum2
                                                                    
                                                                    	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** 0..18446744073709551615
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'man-ipsla-oper'
                                                                    _revision = '2015-11-09'

                                                                    def __init__(self):
                                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats, self).__init__()

                                                                        self.yang_name = "udp-jitter-stats"
                                                                        self.yang_parent_name = "specific-stats"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                                            ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                                            ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                                            ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                                            ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                                            ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                                            ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                                            ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                                            ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                                            ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                                            ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                                            ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                                            ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                                            ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                                            ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                                            ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                                            ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                                            ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                                            ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                                            ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                                            ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                                            ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                                            ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                                            ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                                            ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                                            ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                                            ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                                            ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                                            ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                                            ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                                            ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                                            ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                                            ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                                            ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                                            ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                                            ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                                            ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                                            ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                                            ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                                            ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                                                        ])
                                                                        self.jitter_in = None
                                                                        self.jitter_out = None
                                                                        self.packet_loss_sd = None
                                                                        self.packet_loss_ds = None
                                                                        self.packet_out_of_sequence = None
                                                                        self.packet_mia = None
                                                                        self.packet_skipped = None
                                                                        self.packet_late_arrivals = None
                                                                        self.packet_invalid_tstamp = None
                                                                        self.internal_errors_count = None
                                                                        self.busies_count = None
                                                                        self.positive_sd_sum = None
                                                                        self.positive_sd_sum2 = None
                                                                        self.positive_sd_min = None
                                                                        self.positive_sd_max = None
                                                                        self.positive_sd_count = None
                                                                        self.negative_sd_sum = None
                                                                        self.negative_sd_sum2 = None
                                                                        self.negative_sd_min = None
                                                                        self.negative_sd_max = None
                                                                        self.negative_sd_count = None
                                                                        self.positive_ds_sum = None
                                                                        self.positive_ds_sum2 = None
                                                                        self.positive_ds_min = None
                                                                        self.positive_ds_max = None
                                                                        self.positive_ds_count = None
                                                                        self.negative_ds_sum = None
                                                                        self.negative_ds_sum2 = None
                                                                        self.negative_ds_min = None
                                                                        self.negative_ds_max = None
                                                                        self.negative_ds_count = None
                                                                        self.one_way_count = None
                                                                        self.one_way_sd_min = None
                                                                        self.one_way_sd_max = None
                                                                        self.one_way_sd_sum = None
                                                                        self.one_way_sd_sum2 = None
                                                                        self.one_way_ds_min = None
                                                                        self.one_way_ds_max = None
                                                                        self.one_way_ds_sum = None
                                                                        self.one_way_ds_sum2 = None
                                                                        self._segment_path = lambda: "udp-jitter-stats"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Paths.Path.Hops.Hop.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                                    class Target(Entity):
                                        """
                                        Distribution statistics for the target
                                        node
                                        
                                        .. attribute:: distribution_intervals
                                        
                                        	Table of distribution intervals for a particular hop
                                        	**type**\:  :py:class:`DistributionIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target, self).__init__()

                                            self.yang_name = "target"
                                            self.yang_parent_name = "distributed"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("distribution-intervals", ("distribution_intervals", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals))])
                                            self._leafs = OrderedDict()

                                            self.distribution_intervals = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals()
                                            self.distribution_intervals.parent = self
                                            self._children_name_map["distribution_intervals"] = "distribution-intervals"
                                            self._segment_path = lambda: "target"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target, [], name, value)


                                        class DistributionIntervals(Entity):
                                            """
                                            Table of distribution intervals for a particular
                                            hop
                                            
                                            .. attribute:: distribution_interval
                                            
                                            	1\-hour aggregated statistics for a hop in a path\-enabled operation
                                            	**type**\: list of  		 :py:class:`DistributionInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals, self).__init__()

                                                self.yang_name = "distribution-intervals"
                                                self.yang_parent_name = "target"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("distribution-interval", ("distribution_interval", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval))])
                                                self._leafs = OrderedDict()

                                                self.distribution_interval = YList(self)
                                                self._segment_path = lambda: "distribution-intervals"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals, [], name, value)


                                            class DistributionInterval(Entity):
                                                """
                                                1\-hour aggregated statistics for a hop in a
                                                path\-enabled operation
                                                
                                                .. attribute:: distribution_index  (key)
                                                
                                                	Distribution Interval
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: common_stats
                                                
                                                	Common Stats
                                                	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.CommonStats>`
                                                
                                                .. attribute:: specific_stats
                                                
                                                	Operation Specific Stats
                                                	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats>`
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval, self).__init__()

                                                    self.yang_name = "distribution-interval"
                                                    self.yang_parent_name = "distribution-intervals"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['distribution_index']
                                                    self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats))])
                                                    self._leafs = OrderedDict([
                                                        ('distribution_index', (YLeaf(YType.uint32, 'distribution-index'), ['int'])),
                                                    ])
                                                    self.distribution_index = None

                                                    self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.CommonStats()
                                                    self.common_stats.parent = self
                                                    self._children_name_map["common_stats"] = "common-stats"

                                                    self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats()
                                                    self.specific_stats.parent = self
                                                    self._children_name_map["specific_stats"] = "specific-stats"
                                                    self._segment_path = lambda: "distribution-interval" + "[distribution-index='" + str(self.distribution_index) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval, ['distribution_index'], name, value)


                                                class CommonStats(Entity):
                                                    """
                                                    Common Stats
                                                    
                                                    .. attribute:: operation_time
                                                    
                                                    	Operation Time
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: return_code
                                                    
                                                    	Return code
                                                    	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                                    
                                                    .. attribute:: response_time_count
                                                    
                                                    	Number of RTT samples used for the statistics
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: response_time
                                                    
                                                    	RTT
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: min_response_time
                                                    
                                                    	Minimum RTT
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: max_response_time
                                                    
                                                    	Maximum RTT
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: sum_response_time
                                                    
                                                    	Sum of RTT
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: sum2_response_time
                                                    
                                                    	Sum of RTT^2
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: update_count
                                                    
                                                    	Number of updates processed
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: ok_count
                                                    
                                                    	Number of updates with Okay return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: disconnect_count
                                                    
                                                    	Number of updates with Disconnected return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: timeout_count
                                                    
                                                    	Number of updates with Timeout return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: busy_count
                                                    
                                                    	Number of updates with Busy return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: no_connection_count
                                                    
                                                    	Number of updates with NotConnected return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: dropped_count
                                                    
                                                    	Number of updates with Dropped return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: internal_error_count
                                                    
                                                    	Number of updates with InternalError return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: sequence_error_count
                                                    
                                                    	Number of updates with SeqError return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: verify_error_count
                                                    
                                                    	Number of updates with VerifyError return code
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'man-ipsla-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.CommonStats, self).__init__()

                                                        self.yang_name = "common-stats"
                                                        self.yang_parent_name = "distribution-interval"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                                            ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                            ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                            ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                            ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                            ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                            ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                            ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                            ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                                            ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                                            ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                                            ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                                            ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                                            ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                                            ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                                            ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                                            ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                                            ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                                        ])
                                                        self.operation_time = None
                                                        self.return_code = None
                                                        self.response_time_count = None
                                                        self.response_time = None
                                                        self.min_response_time = None
                                                        self.max_response_time = None
                                                        self.sum_response_time = None
                                                        self.sum2_response_time = None
                                                        self.update_count = None
                                                        self.ok_count = None
                                                        self.disconnect_count = None
                                                        self.timeout_count = None
                                                        self.busy_count = None
                                                        self.no_connection_count = None
                                                        self.dropped_count = None
                                                        self.internal_error_count = None
                                                        self.sequence_error_count = None
                                                        self.verify_error_count = None
                                                        self._segment_path = lambda: "common-stats"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                                class SpecificStats(Entity):
                                                    """
                                                    Operation Specific Stats
                                                    
                                                    .. attribute:: icmp_path_jitter_stats
                                                    
                                                    	icmp path jitter stats
                                                    	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats>`
                                                    
                                                    .. attribute:: udp_jitter_stats
                                                    
                                                    	udp jitter stats
                                                    	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats>`
                                                    
                                                    .. attribute:: op_type
                                                    
                                                    	op type
                                                    	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'man-ipsla-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats, self).__init__()

                                                        self.yang_name = "specific-stats"
                                                        self.yang_parent_name = "distribution-interval"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats))])
                                                        self._leafs = OrderedDict([
                                                            ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                                        ])
                                                        self.op_type = None

                                                        self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats()
                                                        self.icmp_path_jitter_stats.parent = self
                                                        self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                                        self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats()
                                                        self.udp_jitter_stats.parent = self
                                                        self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                                        self._segment_path = lambda: "specific-stats"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats, [u'op_type'], name, value)


                                                    class IcmpPathJitterStats(Entity):
                                                        """
                                                        icmp path jitter stats
                                                        
                                                        .. attribute:: source_address
                                                        
                                                        	IP Address of the source
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: dest_address
                                                        
                                                        	IP Address of the destination
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: hop_address
                                                        
                                                        	IP address of the hop in the path
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: packet_interval
                                                        
                                                        	Interval between echos in ms
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: response_time_count
                                                        
                                                        	Number of RTT samples  used for the statistics
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: response_time
                                                        
                                                        	RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: min_response_time
                                                        
                                                        	Minimum RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: max_response_time
                                                        
                                                        	Maximum RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: sum_response_time
                                                        
                                                        	Sum of RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: sum2_response_time
                                                        
                                                        	Sum of RTT^2
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: packet_count
                                                        
                                                        	Number of Echo replies received 
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_loss_count
                                                        
                                                        	Number of packets lost
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: out_of_sequence_count
                                                        
                                                        	Number of out of sequence packets
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: discarded_sample_count
                                                        
                                                        	Number of discarded samples
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: verify_errors_count
                                                        
                                                        	Number of packets with data corruption
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: dropped_error_count
                                                        
                                                        	Number of packets dropped
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: jitter
                                                        
                                                        	Jitter value for this node in the path
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: pos_jitter_sum
                                                        
                                                        	Sum of positive jitter value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: pos_jitter_sum2
                                                        
                                                        	Sum of squares of positive jitter values
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: pos_jitter_min
                                                        
                                                        	Minimum positive jitter value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: pos_jitter_max
                                                        
                                                        	Maximum positive jitter value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: pos_jitter_count
                                                        
                                                        	Number of positive jitter values
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neg_jitter_sum
                                                        
                                                        	Sum of negative jitter values
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neg_jitter_min
                                                        
                                                        	Minimum negative jitter value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neg_jitter_max
                                                        
                                                        	Maximum negative jitter value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neg_jitter_sum2
                                                        
                                                        	Sum of squares of negative jitter values
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: neg_jitter_count
                                                        
                                                        	Number of negative jitter values
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats, self).__init__()

                                                            self.yang_name = "icmp-path-jitter-stats"
                                                            self.yang_parent_name = "specific-stats"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                                ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                                ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                                ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                                ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                                ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                                ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                                ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                                ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                                ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                                ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                                ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                                ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                                ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                                ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                                ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                                ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                                ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                                ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                                ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                                ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                                ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                                ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                                ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                                ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                                            ])
                                                            self.source_address = None
                                                            self.dest_address = None
                                                            self.hop_address = None
                                                            self.packet_interval = None
                                                            self.response_time_count = None
                                                            self.response_time = None
                                                            self.min_response_time = None
                                                            self.max_response_time = None
                                                            self.sum_response_time = None
                                                            self.sum2_response_time = None
                                                            self.packet_count = None
                                                            self.packet_loss_count = None
                                                            self.out_of_sequence_count = None
                                                            self.discarded_sample_count = None
                                                            self.verify_errors_count = None
                                                            self.dropped_error_count = None
                                                            self.jitter = None
                                                            self.pos_jitter_sum = None
                                                            self.pos_jitter_sum2 = None
                                                            self.pos_jitter_min = None
                                                            self.pos_jitter_max = None
                                                            self.pos_jitter_count = None
                                                            self.neg_jitter_sum = None
                                                            self.neg_jitter_min = None
                                                            self.neg_jitter_max = None
                                                            self.neg_jitter_sum2 = None
                                                            self.neg_jitter_count = None
                                                            self._segment_path = lambda: "icmp-path-jitter-stats"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                                    class UdpJitterStats(Entity):
                                                        """
                                                        udp jitter stats
                                                        
                                                        .. attribute:: jitter_in
                                                        
                                                        	Input Jitter moving average, computed as per RFC1889
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: jitter_out
                                                        
                                                        	Output Jitter moving average, computed as per RFC1889
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_loss_sd
                                                        
                                                        	Packets lost in source to destination (SD) direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_loss_ds
                                                        
                                                        	Packets lost in destination to source (DS) direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_out_of_sequence
                                                        
                                                        	Packets out of sequence
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_mia
                                                        
                                                        	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_skipped
                                                        
                                                        	Packets which are skipped
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_late_arrivals
                                                        
                                                        	Packets arriving late
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: packet_invalid_tstamp
                                                        
                                                        	Packets with bad timestamps
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: internal_errors_count
                                                        
                                                        	Number of internal errors
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: busies_count
                                                        
                                                        	Number of busies
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_sd_sum
                                                        
                                                        	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**units**\: millisecond
                                                        
                                                        .. attribute:: positive_sd_sum2
                                                        
                                                        	Sum of squares of positive jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: positive_sd_min
                                                        
                                                        	Minimum of positive jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_sd_max
                                                        
                                                        	Maximum of positive jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_sd_count
                                                        
                                                        	Number of positive jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_sd_sum
                                                        
                                                        	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**units**\: millisecond
                                                        
                                                        .. attribute:: negative_sd_sum2
                                                        
                                                        	Sum of squares of negative jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: negative_sd_min
                                                        
                                                        	Minimum of negative jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_sd_max
                                                        
                                                        	Maximum of negative jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_sd_count
                                                        
                                                        	Number of negative jitter values in SD direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_ds_sum
                                                        
                                                        	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**units**\: millisecond
                                                        
                                                        .. attribute:: positive_ds_sum2
                                                        
                                                        	Sum of squares of positive jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: positive_ds_min
                                                        
                                                        	Minimum of positive jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_ds_max
                                                        
                                                        	Maximum of positive jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: positive_ds_count
                                                        
                                                        	Number of positive jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_ds_sum
                                                        
                                                        	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**units**\: millisecond
                                                        
                                                        .. attribute:: negative_ds_sum2
                                                        
                                                        	Sum of squares of negative jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: negative_ds_min
                                                        
                                                        	Minimum of negative jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_ds_max
                                                        
                                                        	Maximum of negative jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: negative_ds_count
                                                        
                                                        	Number of negative jitter values in DS direction
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_count
                                                        
                                                        	Number of probe/probe\-response pairs used to compute one\-way statistics
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_sd_min
                                                        
                                                        	Minimum of one\-way jitter values in SD direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_sd_max
                                                        
                                                        	Maximum of one\-way jitter values in SD direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_sd_sum
                                                        
                                                        	Sum of one\-way jitter values in SD direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_sd_sum2
                                                        
                                                        	Sum of squares of one\-way jitter values in SD direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: one_way_ds_min
                                                        
                                                        	Minimum of one\-way jitter values in DS direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_ds_max
                                                        
                                                        	Maximum of one\-way jitter values in DS direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_ds_sum
                                                        
                                                        	Sum of one\-way jitter values in DS direction (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: one_way_ds_sum2
                                                        
                                                        	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats, self).__init__()

                                                            self.yang_name = "udp-jitter-stats"
                                                            self.yang_parent_name = "specific-stats"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                                ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                                ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                                ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                                ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                                ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                                ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                                ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                                ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                                ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                                ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                                ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                                ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                                ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                                ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                                ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                                ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                                ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                                ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                                ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                                ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                                ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                                ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                                ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                                ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                                ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                                ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                                ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                                ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                                ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                                ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                                ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                                ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                                ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                                ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                                ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                                ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                                ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                                ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                                ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                                            ])
                                                            self.jitter_in = None
                                                            self.jitter_out = None
                                                            self.packet_loss_sd = None
                                                            self.packet_loss_ds = None
                                                            self.packet_out_of_sequence = None
                                                            self.packet_mia = None
                                                            self.packet_skipped = None
                                                            self.packet_late_arrivals = None
                                                            self.packet_invalid_tstamp = None
                                                            self.internal_errors_count = None
                                                            self.busies_count = None
                                                            self.positive_sd_sum = None
                                                            self.positive_sd_sum2 = None
                                                            self.positive_sd_min = None
                                                            self.positive_sd_max = None
                                                            self.positive_sd_count = None
                                                            self.negative_sd_sum = None
                                                            self.negative_sd_sum2 = None
                                                            self.negative_sd_min = None
                                                            self.negative_sd_max = None
                                                            self.negative_sd_count = None
                                                            self.positive_ds_sum = None
                                                            self.positive_ds_sum2 = None
                                                            self.positive_ds_min = None
                                                            self.positive_ds_max = None
                                                            self.positive_ds_count = None
                                                            self.negative_ds_sum = None
                                                            self.negative_ds_sum2 = None
                                                            self.negative_ds_min = None
                                                            self.negative_ds_max = None
                                                            self.negative_ds_count = None
                                                            self.one_way_count = None
                                                            self.one_way_sd_min = None
                                                            self.one_way_sd_max = None
                                                            self.one_way_sd_sum = None
                                                            self.one_way_sd_sum2 = None
                                                            self.one_way_ds_min = None
                                                            self.one_way_ds_max = None
                                                            self.one_way_ds_sum = None
                                                            self.one_way_ds_sum2 = None
                                                            self._segment_path = lambda: "udp-jitter-stats"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.Distributed.Target.DistributionIntervals.DistributionInterval.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                                class NonDistributed(Entity):
                                    """
                                    Statistics aggregated for the total range
                                    of values in 1\-hour intervals
                                    
                                    .. attribute:: target
                                    
                                    	Total 1\-hour aggregated statistics for the target node
                                    	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target>`
                                    
                                    .. attribute:: paths
                                    
                                    	Table of paths identified in the 1\-hour interval
                                    	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths>`
                                    
                                    .. attribute:: lpd_paths
                                    
                                    	List of latest LPD paths
                                    	**type**\:  :py:class:`LpdPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths>`
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed, self).__init__()

                                        self.yang_name = "non-distributed"
                                        self.yang_parent_name = "hour"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("target", ("target", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target)), ("paths", ("paths", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths)), ("lpd-paths", ("lpd_paths", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths))])
                                        self._leafs = OrderedDict()

                                        self.target = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target()
                                        self.target.parent = self
                                        self._children_name_map["target"] = "target"

                                        self.paths = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths()
                                        self.paths.parent = self
                                        self._children_name_map["paths"] = "paths"

                                        self.lpd_paths = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths()
                                        self.lpd_paths.parent = self
                                        self._children_name_map["lpd_paths"] = "lpd-paths"
                                        self._segment_path = lambda: "non-distributed"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed, [], name, value)


                                    class Target(Entity):
                                        """
                                        Total 1\-hour aggregated statistics for
                                        the target node
                                        
                                        .. attribute:: common_stats
                                        
                                        	Common Stats
                                        	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.CommonStats>`
                                        
                                        .. attribute:: specific_stats
                                        
                                        	Operation Specific Stats
                                        	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target, self).__init__()

                                            self.yang_name = "target"
                                            self.yang_parent_name = "non-distributed"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats))])
                                            self._leafs = OrderedDict()

                                            self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.CommonStats()
                                            self.common_stats.parent = self
                                            self._children_name_map["common_stats"] = "common-stats"

                                            self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats()
                                            self.specific_stats.parent = self
                                            self._children_name_map["specific_stats"] = "specific-stats"
                                            self._segment_path = lambda: "target"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target, [], name, value)


                                        class CommonStats(Entity):
                                            """
                                            Common Stats
                                            
                                            .. attribute:: operation_time
                                            
                                            	Operation Time
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: return_code
                                            
                                            	Return code
                                            	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                            
                                            .. attribute:: response_time_count
                                            
                                            	Number of RTT samples used for the statistics
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: response_time
                                            
                                            	RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: min_response_time
                                            
                                            	Minimum RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: max_response_time
                                            
                                            	Maximum RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sum_response_time
                                            
                                            	Sum of RTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sum2_response_time
                                            
                                            	Sum of RTT^2
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: update_count
                                            
                                            	Number of updates processed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: ok_count
                                            
                                            	Number of updates with Okay return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: disconnect_count
                                            
                                            	Number of updates with Disconnected return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: timeout_count
                                            
                                            	Number of updates with Timeout return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: busy_count
                                            
                                            	Number of updates with Busy return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: no_connection_count
                                            
                                            	Number of updates with NotConnected return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: dropped_count
                                            
                                            	Number of updates with Dropped return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: internal_error_count
                                            
                                            	Number of updates with InternalError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sequence_error_count
                                            
                                            	Number of updates with SeqError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: verify_error_count
                                            
                                            	Number of updates with VerifyError return code
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.CommonStats, self).__init__()

                                                self.yang_name = "common-stats"
                                                self.yang_parent_name = "target"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                                    ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                    ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                    ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                    ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                    ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                    ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                    ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                    ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                                    ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                                    ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                                    ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                                    ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                                    ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                                    ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                                    ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                                    ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                                    ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                                ])
                                                self.operation_time = None
                                                self.return_code = None
                                                self.response_time_count = None
                                                self.response_time = None
                                                self.min_response_time = None
                                                self.max_response_time = None
                                                self.sum_response_time = None
                                                self.sum2_response_time = None
                                                self.update_count = None
                                                self.ok_count = None
                                                self.disconnect_count = None
                                                self.timeout_count = None
                                                self.busy_count = None
                                                self.no_connection_count = None
                                                self.dropped_count = None
                                                self.internal_error_count = None
                                                self.sequence_error_count = None
                                                self.verify_error_count = None
                                                self._segment_path = lambda: "common-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                        class SpecificStats(Entity):
                                            """
                                            Operation Specific Stats
                                            
                                            .. attribute:: icmp_path_jitter_stats
                                            
                                            	icmp path jitter stats
                                            	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.IcmpPathJitterStats>`
                                            
                                            .. attribute:: udp_jitter_stats
                                            
                                            	udp jitter stats
                                            	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.UdpJitterStats>`
                                            
                                            .. attribute:: op_type
                                            
                                            	op type
                                            	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats, self).__init__()

                                                self.yang_name = "specific-stats"
                                                self.yang_parent_name = "target"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.UdpJitterStats))])
                                                self._leafs = OrderedDict([
                                                    ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                                ])
                                                self.op_type = None

                                                self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.IcmpPathJitterStats()
                                                self.icmp_path_jitter_stats.parent = self
                                                self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                                self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.UdpJitterStats()
                                                self.udp_jitter_stats.parent = self
                                                self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                                self._segment_path = lambda: "specific-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats, [u'op_type'], name, value)


                                            class IcmpPathJitterStats(Entity):
                                                """
                                                icmp path jitter stats
                                                
                                                .. attribute:: source_address
                                                
                                                	IP Address of the source
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: dest_address
                                                
                                                	IP Address of the destination
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: hop_address
                                                
                                                	IP address of the hop in the path
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: packet_interval
                                                
                                                	Interval between echos in ms
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: response_time_count
                                                
                                                	Number of RTT samples  used for the statistics
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: response_time
                                                
                                                	RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: min_response_time
                                                
                                                	Minimum RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: max_response_time
                                                
                                                	Maximum RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: sum_response_time
                                                
                                                	Sum of RTT
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: sum2_response_time
                                                
                                                	Sum of RTT^2
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: packet_count
                                                
                                                	Number of Echo replies received 
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_count
                                                
                                                	Number of packets lost
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: out_of_sequence_count
                                                
                                                	Number of out of sequence packets
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: discarded_sample_count
                                                
                                                	Number of discarded samples
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: verify_errors_count
                                                
                                                	Number of packets with data corruption
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: dropped_error_count
                                                
                                                	Number of packets dropped
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: jitter
                                                
                                                	Jitter value for this node in the path
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_sum
                                                
                                                	Sum of positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_sum2
                                                
                                                	Sum of squares of positive jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: pos_jitter_min
                                                
                                                	Minimum positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_max
                                                
                                                	Maximum positive jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: pos_jitter_count
                                                
                                                	Number of positive jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_sum
                                                
                                                	Sum of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_min
                                                
                                                	Minimum negative jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_max
                                                
                                                	Maximum negative jitter value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neg_jitter_sum2
                                                
                                                	Sum of squares of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: neg_jitter_count
                                                
                                                	Number of negative jitter values
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.IcmpPathJitterStats, self).__init__()

                                                    self.yang_name = "icmp-path-jitter-stats"
                                                    self.yang_parent_name = "specific-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                        ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                        ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                        ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                        ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                        ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                        ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                        ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                        ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                        ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                        ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                        ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                        ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                        ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                        ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                        ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                        ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                        ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                        ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                        ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                        ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                        ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                        ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                        ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                        ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                        ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                        ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                                    ])
                                                    self.source_address = None
                                                    self.dest_address = None
                                                    self.hop_address = None
                                                    self.packet_interval = None
                                                    self.response_time_count = None
                                                    self.response_time = None
                                                    self.min_response_time = None
                                                    self.max_response_time = None
                                                    self.sum_response_time = None
                                                    self.sum2_response_time = None
                                                    self.packet_count = None
                                                    self.packet_loss_count = None
                                                    self.out_of_sequence_count = None
                                                    self.discarded_sample_count = None
                                                    self.verify_errors_count = None
                                                    self.dropped_error_count = None
                                                    self.jitter = None
                                                    self.pos_jitter_sum = None
                                                    self.pos_jitter_sum2 = None
                                                    self.pos_jitter_min = None
                                                    self.pos_jitter_max = None
                                                    self.pos_jitter_count = None
                                                    self.neg_jitter_sum = None
                                                    self.neg_jitter_min = None
                                                    self.neg_jitter_max = None
                                                    self.neg_jitter_sum2 = None
                                                    self.neg_jitter_count = None
                                                    self._segment_path = lambda: "icmp-path-jitter-stats"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                            class UdpJitterStats(Entity):
                                                """
                                                udp jitter stats
                                                
                                                .. attribute:: jitter_in
                                                
                                                	Input Jitter moving average, computed as per RFC1889
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: jitter_out
                                                
                                                	Output Jitter moving average, computed as per RFC1889
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_sd
                                                
                                                	Packets lost in source to destination (SD) direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_loss_ds
                                                
                                                	Packets lost in destination to source (DS) direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_out_of_sequence
                                                
                                                	Packets out of sequence
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_mia
                                                
                                                	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_skipped
                                                
                                                	Packets which are skipped
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_late_arrivals
                                                
                                                	Packets arriving late
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: packet_invalid_tstamp
                                                
                                                	Packets with bad timestamps
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: internal_errors_count
                                                
                                                	Number of internal errors
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: busies_count
                                                
                                                	Number of busies
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_sum
                                                
                                                	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: positive_sd_sum2
                                                
                                                	Sum of squares of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: positive_sd_min
                                                
                                                	Minimum of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_max
                                                
                                                	Maximum of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_sd_count
                                                
                                                	Number of positive jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_sum
                                                
                                                	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: negative_sd_sum2
                                                
                                                	Sum of squares of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: negative_sd_min
                                                
                                                	Minimum of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_max
                                                
                                                	Maximum of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_sd_count
                                                
                                                	Number of negative jitter values in SD direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_sum
                                                
                                                	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: positive_ds_sum2
                                                
                                                	Sum of squares of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: positive_ds_min
                                                
                                                	Minimum of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_max
                                                
                                                	Maximum of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: positive_ds_count
                                                
                                                	Number of positive jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_sum
                                                
                                                	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**units**\: millisecond
                                                
                                                .. attribute:: negative_ds_sum2
                                                
                                                	Sum of squares of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: negative_ds_min
                                                
                                                	Minimum of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_max
                                                
                                                	Maximum of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: negative_ds_count
                                                
                                                	Number of negative jitter values in DS direction
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_count
                                                
                                                	Number of probe/probe\-response pairs used to compute one\-way statistics
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_min
                                                
                                                	Minimum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_max
                                                
                                                	Maximum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_sum
                                                
                                                	Sum of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_sd_sum2
                                                
                                                	Sum of squares of one\-way jitter values in SD direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: one_way_ds_min
                                                
                                                	Minimum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_max
                                                
                                                	Maximum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_sum
                                                
                                                	Sum of one\-way jitter values in DS direction (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: one_way_ds_sum2
                                                
                                                	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.UdpJitterStats, self).__init__()

                                                    self.yang_name = "udp-jitter-stats"
                                                    self.yang_parent_name = "specific-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                        ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                        ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                        ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                        ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                        ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                        ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                        ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                        ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                        ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                        ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                        ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                        ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                        ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                        ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                        ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                        ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                        ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                        ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                        ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                        ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                        ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                        ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                        ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                        ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                        ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                        ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                        ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                        ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                        ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                        ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                        ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                        ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                        ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                        ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                        ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                        ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                        ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                        ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                        ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                                    ])
                                                    self.jitter_in = None
                                                    self.jitter_out = None
                                                    self.packet_loss_sd = None
                                                    self.packet_loss_ds = None
                                                    self.packet_out_of_sequence = None
                                                    self.packet_mia = None
                                                    self.packet_skipped = None
                                                    self.packet_late_arrivals = None
                                                    self.packet_invalid_tstamp = None
                                                    self.internal_errors_count = None
                                                    self.busies_count = None
                                                    self.positive_sd_sum = None
                                                    self.positive_sd_sum2 = None
                                                    self.positive_sd_min = None
                                                    self.positive_sd_max = None
                                                    self.positive_sd_count = None
                                                    self.negative_sd_sum = None
                                                    self.negative_sd_sum2 = None
                                                    self.negative_sd_min = None
                                                    self.negative_sd_max = None
                                                    self.negative_sd_count = None
                                                    self.positive_ds_sum = None
                                                    self.positive_ds_sum2 = None
                                                    self.positive_ds_min = None
                                                    self.positive_ds_max = None
                                                    self.positive_ds_count = None
                                                    self.negative_ds_sum = None
                                                    self.negative_ds_sum2 = None
                                                    self.negative_ds_min = None
                                                    self.negative_ds_max = None
                                                    self.negative_ds_count = None
                                                    self.one_way_count = None
                                                    self.one_way_sd_min = None
                                                    self.one_way_sd_max = None
                                                    self.one_way_sd_sum = None
                                                    self.one_way_sd_sum2 = None
                                                    self.one_way_ds_min = None
                                                    self.one_way_ds_max = None
                                                    self.one_way_ds_sum = None
                                                    self.one_way_ds_sum2 = None
                                                    self._segment_path = lambda: "udp-jitter-stats"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Target.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                                    class Paths(Entity):
                                        """
                                        Table of paths identified in the 1\-hour
                                        interval
                                        
                                        .. attribute:: path
                                        
                                        	Paths identified in a 1\-hour interval
                                        	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths, self).__init__()

                                            self.yang_name = "paths"
                                            self.yang_parent_name = "non-distributed"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("path", ("path", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path))])
                                            self._leafs = OrderedDict()

                                            self.path = YList(self)
                                            self._segment_path = lambda: "paths"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths, [], name, value)


                                        class Path(Entity):
                                            """
                                            Paths identified in a 1\-hour interval
                                            
                                            .. attribute:: path_index  (key)
                                            
                                            	Path Index
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: hops
                                            
                                            	Table of hops for a particular path
                                            	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path, self).__init__()

                                                self.yang_name = "path"
                                                self.yang_parent_name = "paths"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['path_index']
                                                self._child_classes = OrderedDict([("hops", ("hops", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops))])
                                                self._leafs = OrderedDict([
                                                    ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                                ])
                                                self.path_index = None

                                                self.hops = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops()
                                                self.hops.parent = self
                                                self._children_name_map["hops"] = "hops"
                                                self._segment_path = lambda: "path" + "[path-index='" + str(self.path_index) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path, ['path_index'], name, value)


                                            class Hops(Entity):
                                                """
                                                Table of hops for a particular path
                                                
                                                .. attribute:: hop
                                                
                                                	Total 1\-hour aggregated statistics for a hop in a path\-enabled operation
                                                	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop>`
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops, self).__init__()

                                                    self.yang_name = "hops"
                                                    self.yang_parent_name = "path"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("hop", ("hop", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop))])
                                                    self._leafs = OrderedDict()

                                                    self.hop = YList(self)
                                                    self._segment_path = lambda: "hops"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops, [], name, value)


                                                class Hop(Entity):
                                                    """
                                                    Total 1\-hour aggregated statistics
                                                    for a hop in a path\-enabled operation
                                                    
                                                    .. attribute:: hop_index  (key)
                                                    
                                                    	Hop Index
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: common_stats
                                                    
                                                    	Common Stats
                                                    	**type**\:  :py:class:`CommonStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.CommonStats>`
                                                    
                                                    .. attribute:: specific_stats
                                                    
                                                    	Operation Specific Stats
                                                    	**type**\:  :py:class:`SpecificStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'man-ipsla-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop, self).__init__()

                                                        self.yang_name = "hop"
                                                        self.yang_parent_name = "hops"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['hop_index']
                                                        self._child_classes = OrderedDict([("common-stats", ("common_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.CommonStats)), ("specific-stats", ("specific_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats))])
                                                        self._leafs = OrderedDict([
                                                            ('hop_index', (YLeaf(YType.uint32, 'hop-index'), ['int'])),
                                                        ])
                                                        self.hop_index = None

                                                        self.common_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.CommonStats()
                                                        self.common_stats.parent = self
                                                        self._children_name_map["common_stats"] = "common-stats"

                                                        self.specific_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats()
                                                        self.specific_stats.parent = self
                                                        self._children_name_map["specific_stats"] = "specific-stats"
                                                        self._segment_path = lambda: "hop" + "[hop-index='" + str(self.hop_index) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop, ['hop_index'], name, value)


                                                    class CommonStats(Entity):
                                                        """
                                                        Common Stats
                                                        
                                                        .. attribute:: operation_time
                                                        
                                                        	Operation Time
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: return_code
                                                        
                                                        	Return code
                                                        	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                                        
                                                        .. attribute:: response_time_count
                                                        
                                                        	Number of RTT samples used for the statistics
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: response_time
                                                        
                                                        	RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: min_response_time
                                                        
                                                        	Minimum RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: max_response_time
                                                        
                                                        	Maximum RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: sum_response_time
                                                        
                                                        	Sum of RTT
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: sum2_response_time
                                                        
                                                        	Sum of RTT^2
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..18446744073709551615
                                                        
                                                        .. attribute:: update_count
                                                        
                                                        	Number of updates processed
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: ok_count
                                                        
                                                        	Number of updates with Okay return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: disconnect_count
                                                        
                                                        	Number of updates with Disconnected return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: timeout_count
                                                        
                                                        	Number of updates with Timeout return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: busy_count
                                                        
                                                        	Number of updates with Busy return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: no_connection_count
                                                        
                                                        	Number of updates with NotConnected return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: dropped_count
                                                        
                                                        	Number of updates with Dropped return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: internal_error_count
                                                        
                                                        	Number of updates with InternalError return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: sequence_error_count
                                                        
                                                        	Number of updates with SeqError return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: verify_error_count
                                                        
                                                        	Number of updates with VerifyError return code
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.CommonStats, self).__init__()

                                                            self.yang_name = "common-stats"
                                                            self.yang_parent_name = "hop"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('operation_time', (YLeaf(YType.uint64, 'operation-time'), ['int'])),
                                                                ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                                ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                                ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                                ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                                ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                                ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                                ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                                ('update_count', (YLeaf(YType.uint32, 'update-count'), ['int'])),
                                                                ('ok_count', (YLeaf(YType.uint32, 'ok-count'), ['int'])),
                                                                ('disconnect_count', (YLeaf(YType.uint32, 'disconnect-count'), ['int'])),
                                                                ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                                                                ('busy_count', (YLeaf(YType.uint32, 'busy-count'), ['int'])),
                                                                ('no_connection_count', (YLeaf(YType.uint32, 'no-connection-count'), ['int'])),
                                                                ('dropped_count', (YLeaf(YType.uint32, 'dropped-count'), ['int'])),
                                                                ('internal_error_count', (YLeaf(YType.uint32, 'internal-error-count'), ['int'])),
                                                                ('sequence_error_count', (YLeaf(YType.uint32, 'sequence-error-count'), ['int'])),
                                                                ('verify_error_count', (YLeaf(YType.uint32, 'verify-error-count'), ['int'])),
                                                            ])
                                                            self.operation_time = None
                                                            self.return_code = None
                                                            self.response_time_count = None
                                                            self.response_time = None
                                                            self.min_response_time = None
                                                            self.max_response_time = None
                                                            self.sum_response_time = None
                                                            self.sum2_response_time = None
                                                            self.update_count = None
                                                            self.ok_count = None
                                                            self.disconnect_count = None
                                                            self.timeout_count = None
                                                            self.busy_count = None
                                                            self.no_connection_count = None
                                                            self.dropped_count = None
                                                            self.internal_error_count = None
                                                            self.sequence_error_count = None
                                                            self.verify_error_count = None
                                                            self._segment_path = lambda: "common-stats"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.CommonStats, [u'operation_time', u'return_code', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'update_count', u'ok_count', u'disconnect_count', u'timeout_count', u'busy_count', u'no_connection_count', u'dropped_count', u'internal_error_count', u'sequence_error_count', u'verify_error_count'], name, value)


                                                    class SpecificStats(Entity):
                                                        """
                                                        Operation Specific Stats
                                                        
                                                        .. attribute:: icmp_path_jitter_stats
                                                        
                                                        	icmp path jitter stats
                                                        	**type**\:  :py:class:`IcmpPathJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.IcmpPathJitterStats>`
                                                        
                                                        .. attribute:: udp_jitter_stats
                                                        
                                                        	udp jitter stats
                                                        	**type**\:  :py:class:`UdpJitterStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.UdpJitterStats>`
                                                        
                                                        .. attribute:: op_type
                                                        
                                                        	op type
                                                        	**type**\:  :py:class:`OpTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.OpTypeEnum>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'man-ipsla-oper'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats, self).__init__()

                                                            self.yang_name = "specific-stats"
                                                            self.yang_parent_name = "hop"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("icmp-path-jitter-stats", ("icmp_path_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.IcmpPathJitterStats)), ("udp-jitter-stats", ("udp_jitter_stats", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.UdpJitterStats))])
                                                            self._leafs = OrderedDict([
                                                                ('op_type', (YLeaf(YType.enumeration, 'op-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'OpTypeEnum', '')])),
                                                            ])
                                                            self.op_type = None

                                                            self.icmp_path_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.IcmpPathJitterStats()
                                                            self.icmp_path_jitter_stats.parent = self
                                                            self._children_name_map["icmp_path_jitter_stats"] = "icmp-path-jitter-stats"

                                                            self.udp_jitter_stats = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.UdpJitterStats()
                                                            self.udp_jitter_stats.parent = self
                                                            self._children_name_map["udp_jitter_stats"] = "udp-jitter-stats"
                                                            self._segment_path = lambda: "specific-stats"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats, [u'op_type'], name, value)


                                                        class IcmpPathJitterStats(Entity):
                                                            """
                                                            icmp path jitter stats
                                                            
                                                            .. attribute:: source_address
                                                            
                                                            	IP Address of the source
                                                            	**type**\: str
                                                            
                                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                            
                                                            .. attribute:: dest_address
                                                            
                                                            	IP Address of the destination
                                                            	**type**\: str
                                                            
                                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                            
                                                            .. attribute:: hop_address
                                                            
                                                            	IP address of the hop in the path
                                                            	**type**\: str
                                                            
                                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                            
                                                            .. attribute:: packet_interval
                                                            
                                                            	Interval between echos in ms
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: response_time_count
                                                            
                                                            	Number of RTT samples  used for the statistics
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: response_time
                                                            
                                                            	RTT
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: min_response_time
                                                            
                                                            	Minimum RTT
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: max_response_time
                                                            
                                                            	Maximum RTT
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: sum_response_time
                                                            
                                                            	Sum of RTT
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: sum2_response_time
                                                            
                                                            	Sum of RTT^2
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: packet_count
                                                            
                                                            	Number of Echo replies received 
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_loss_count
                                                            
                                                            	Number of packets lost
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: out_of_sequence_count
                                                            
                                                            	Number of out of sequence packets
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: discarded_sample_count
                                                            
                                                            	Number of discarded samples
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: verify_errors_count
                                                            
                                                            	Number of packets with data corruption
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: dropped_error_count
                                                            
                                                            	Number of packets dropped
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: jitter
                                                            
                                                            	Jitter value for this node in the path
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: pos_jitter_sum
                                                            
                                                            	Sum of positive jitter value
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: pos_jitter_sum2
                                                            
                                                            	Sum of squares of positive jitter values
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: pos_jitter_min
                                                            
                                                            	Minimum positive jitter value
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: pos_jitter_max
                                                            
                                                            	Maximum positive jitter value
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: pos_jitter_count
                                                            
                                                            	Number of positive jitter values
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: neg_jitter_sum
                                                            
                                                            	Sum of negative jitter values
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: neg_jitter_min
                                                            
                                                            	Minimum negative jitter value
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: neg_jitter_max
                                                            
                                                            	Maximum negative jitter value
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: neg_jitter_sum2
                                                            
                                                            	Sum of squares of negative jitter values
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: neg_jitter_count
                                                            
                                                            	Number of negative jitter values
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            

                                                            """

                                                            _prefix = 'man-ipsla-oper'
                                                            _revision = '2015-11-09'

                                                            def __init__(self):
                                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.IcmpPathJitterStats, self).__init__()

                                                                self.yang_name = "icmp-path-jitter-stats"
                                                                self.yang_parent_name = "specific-stats"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                                                    ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                                                    ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                                                                    ('packet_interval', (YLeaf(YType.uint32, 'packet-interval'), ['int'])),
                                                                    ('response_time_count', (YLeaf(YType.uint32, 'response-time-count'), ['int'])),
                                                                    ('response_time', (YLeaf(YType.uint32, 'response-time'), ['int'])),
                                                                    ('min_response_time', (YLeaf(YType.uint32, 'min-response-time'), ['int'])),
                                                                    ('max_response_time', (YLeaf(YType.uint32, 'max-response-time'), ['int'])),
                                                                    ('sum_response_time', (YLeaf(YType.uint32, 'sum-response-time'), ['int'])),
                                                                    ('sum2_response_time', (YLeaf(YType.uint64, 'sum2-response-time'), ['int'])),
                                                                    ('packet_count', (YLeaf(YType.uint32, 'packet-count'), ['int'])),
                                                                    ('packet_loss_count', (YLeaf(YType.uint32, 'packet-loss-count'), ['int'])),
                                                                    ('out_of_sequence_count', (YLeaf(YType.uint32, 'out-of-sequence-count'), ['int'])),
                                                                    ('discarded_sample_count', (YLeaf(YType.uint32, 'discarded-sample-count'), ['int'])),
                                                                    ('verify_errors_count', (YLeaf(YType.uint32, 'verify-errors-count'), ['int'])),
                                                                    ('dropped_error_count', (YLeaf(YType.uint32, 'dropped-error-count'), ['int'])),
                                                                    ('jitter', (YLeaf(YType.uint32, 'jitter'), ['int'])),
                                                                    ('pos_jitter_sum', (YLeaf(YType.uint32, 'pos-jitter-sum'), ['int'])),
                                                                    ('pos_jitter_sum2', (YLeaf(YType.uint64, 'pos-jitter-sum2'), ['int'])),
                                                                    ('pos_jitter_min', (YLeaf(YType.uint32, 'pos-jitter-min'), ['int'])),
                                                                    ('pos_jitter_max', (YLeaf(YType.uint32, 'pos-jitter-max'), ['int'])),
                                                                    ('pos_jitter_count', (YLeaf(YType.uint32, 'pos-jitter-count'), ['int'])),
                                                                    ('neg_jitter_sum', (YLeaf(YType.uint32, 'neg-jitter-sum'), ['int'])),
                                                                    ('neg_jitter_min', (YLeaf(YType.uint32, 'neg-jitter-min'), ['int'])),
                                                                    ('neg_jitter_max', (YLeaf(YType.uint32, 'neg-jitter-max'), ['int'])),
                                                                    ('neg_jitter_sum2', (YLeaf(YType.uint64, 'neg-jitter-sum2'), ['int'])),
                                                                    ('neg_jitter_count', (YLeaf(YType.uint32, 'neg-jitter-count'), ['int'])),
                                                                ])
                                                                self.source_address = None
                                                                self.dest_address = None
                                                                self.hop_address = None
                                                                self.packet_interval = None
                                                                self.response_time_count = None
                                                                self.response_time = None
                                                                self.min_response_time = None
                                                                self.max_response_time = None
                                                                self.sum_response_time = None
                                                                self.sum2_response_time = None
                                                                self.packet_count = None
                                                                self.packet_loss_count = None
                                                                self.out_of_sequence_count = None
                                                                self.discarded_sample_count = None
                                                                self.verify_errors_count = None
                                                                self.dropped_error_count = None
                                                                self.jitter = None
                                                                self.pos_jitter_sum = None
                                                                self.pos_jitter_sum2 = None
                                                                self.pos_jitter_min = None
                                                                self.pos_jitter_max = None
                                                                self.pos_jitter_count = None
                                                                self.neg_jitter_sum = None
                                                                self.neg_jitter_min = None
                                                                self.neg_jitter_max = None
                                                                self.neg_jitter_sum2 = None
                                                                self.neg_jitter_count = None
                                                                self._segment_path = lambda: "icmp-path-jitter-stats"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.IcmpPathJitterStats, [u'source_address', u'dest_address', u'hop_address', u'packet_interval', u'response_time_count', u'response_time', u'min_response_time', u'max_response_time', u'sum_response_time', u'sum2_response_time', u'packet_count', u'packet_loss_count', u'out_of_sequence_count', u'discarded_sample_count', u'verify_errors_count', u'dropped_error_count', u'jitter', u'pos_jitter_sum', u'pos_jitter_sum2', u'pos_jitter_min', u'pos_jitter_max', u'pos_jitter_count', u'neg_jitter_sum', u'neg_jitter_min', u'neg_jitter_max', u'neg_jitter_sum2', u'neg_jitter_count'], name, value)


                                                        class UdpJitterStats(Entity):
                                                            """
                                                            udp jitter stats
                                                            
                                                            .. attribute:: jitter_in
                                                            
                                                            	Input Jitter moving average, computed as per RFC1889
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: jitter_out
                                                            
                                                            	Output Jitter moving average, computed as per RFC1889
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_loss_sd
                                                            
                                                            	Packets lost in source to destination (SD) direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_loss_ds
                                                            
                                                            	Packets lost in destination to source (DS) direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_out_of_sequence
                                                            
                                                            	Packets out of sequence
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_mia
                                                            
                                                            	Packets missing in action (cannot determine if theywere lost in SD or DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_skipped
                                                            
                                                            	Packets which are skipped
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_late_arrivals
                                                            
                                                            	Packets arriving late
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: packet_invalid_tstamp
                                                            
                                                            	Packets with bad timestamps
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: internal_errors_count
                                                            
                                                            	Number of internal errors
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: busies_count
                                                            
                                                            	Number of busies
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_sd_sum
                                                            
                                                            	Sum of positive jitter values (i.e., network latency increases for two consecutive  packets) in SD direction Measured  in milliseconds
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            	**units**\: millisecond
                                                            
                                                            .. attribute:: positive_sd_sum2
                                                            
                                                            	Sum of squares of positive jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: positive_sd_min
                                                            
                                                            	Minimum of positive jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_sd_max
                                                            
                                                            	Maximum of positive jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_sd_count
                                                            
                                                            	Number of positive jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_sd_sum
                                                            
                                                            	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in SD direction Measured  in milliseconds
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            	**units**\: millisecond
                                                            
                                                            .. attribute:: negative_sd_sum2
                                                            
                                                            	Sum of squares of negative jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: negative_sd_min
                                                            
                                                            	Minimum of negative jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_sd_max
                                                            
                                                            	Maximum of negative jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_sd_count
                                                            
                                                            	Number of negative jitter values in SD direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_ds_sum
                                                            
                                                            	Sum of positive jitter values (i.e., network latency increases for two consecutive packets) in DS direction Measured  in milliseconds
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            	**units**\: millisecond
                                                            
                                                            .. attribute:: positive_ds_sum2
                                                            
                                                            	Sum of squares of positive jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: positive_ds_min
                                                            
                                                            	Minimum of positive jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_ds_max
                                                            
                                                            	Maximum of positive jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: positive_ds_count
                                                            
                                                            	Number of positive jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_ds_sum
                                                            
                                                            	Sum of negative jitter values (i.e., network latency decreases for two consecutive packets) in DS direction Measured  in milliseconds
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            	**units**\: millisecond
                                                            
                                                            .. attribute:: negative_ds_sum2
                                                            
                                                            	Sum of squares of negative jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: negative_ds_min
                                                            
                                                            	Minimum of negative jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_ds_max
                                                            
                                                            	Maximum of negative jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: negative_ds_count
                                                            
                                                            	Number of negative jitter values in DS direction
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_count
                                                            
                                                            	Number of probe/probe\-response pairs used to compute one\-way statistics
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_sd_min
                                                            
                                                            	Minimum of one\-way jitter values in SD direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_sd_max
                                                            
                                                            	Maximum of one\-way jitter values in SD direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_sd_sum
                                                            
                                                            	Sum of one\-way jitter values in SD direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_sd_sum2
                                                            
                                                            	Sum of squares of one\-way jitter values in SD direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            .. attribute:: one_way_ds_min
                                                            
                                                            	Minimum of one\-way jitter values in DS direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_ds_max
                                                            
                                                            	Maximum of one\-way jitter values in DS direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_ds_sum
                                                            
                                                            	Sum of one\-way jitter values in DS direction (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..4294967295
                                                            
                                                            .. attribute:: one_way_ds_sum2
                                                            
                                                            	Sum of squares of the OneWayMinDS and OneWayMaxDS values (msec)
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..18446744073709551615
                                                            
                                                            

                                                            """

                                                            _prefix = 'man-ipsla-oper'
                                                            _revision = '2015-11-09'

                                                            def __init__(self):
                                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.UdpJitterStats, self).__init__()

                                                                self.yang_name = "udp-jitter-stats"
                                                                self.yang_parent_name = "specific-stats"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('jitter_in', (YLeaf(YType.uint32, 'jitter-in'), ['int'])),
                                                                    ('jitter_out', (YLeaf(YType.uint32, 'jitter-out'), ['int'])),
                                                                    ('packet_loss_sd', (YLeaf(YType.uint32, 'packet-loss-sd'), ['int'])),
                                                                    ('packet_loss_ds', (YLeaf(YType.uint32, 'packet-loss-ds'), ['int'])),
                                                                    ('packet_out_of_sequence', (YLeaf(YType.uint32, 'packet-out-of-sequence'), ['int'])),
                                                                    ('packet_mia', (YLeaf(YType.uint32, 'packet-mia'), ['int'])),
                                                                    ('packet_skipped', (YLeaf(YType.uint32, 'packet-skipped'), ['int'])),
                                                                    ('packet_late_arrivals', (YLeaf(YType.uint32, 'packet-late-arrivals'), ['int'])),
                                                                    ('packet_invalid_tstamp', (YLeaf(YType.uint32, 'packet-invalid-tstamp'), ['int'])),
                                                                    ('internal_errors_count', (YLeaf(YType.uint32, 'internal-errors-count'), ['int'])),
                                                                    ('busies_count', (YLeaf(YType.uint32, 'busies-count'), ['int'])),
                                                                    ('positive_sd_sum', (YLeaf(YType.uint32, 'positive-sd-sum'), ['int'])),
                                                                    ('positive_sd_sum2', (YLeaf(YType.uint64, 'positive-sd-sum2'), ['int'])),
                                                                    ('positive_sd_min', (YLeaf(YType.uint32, 'positive-sd-min'), ['int'])),
                                                                    ('positive_sd_max', (YLeaf(YType.uint32, 'positive-sd-max'), ['int'])),
                                                                    ('positive_sd_count', (YLeaf(YType.uint32, 'positive-sd-count'), ['int'])),
                                                                    ('negative_sd_sum', (YLeaf(YType.uint32, 'negative-sd-sum'), ['int'])),
                                                                    ('negative_sd_sum2', (YLeaf(YType.uint64, 'negative-sd-sum2'), ['int'])),
                                                                    ('negative_sd_min', (YLeaf(YType.uint32, 'negative-sd-min'), ['int'])),
                                                                    ('negative_sd_max', (YLeaf(YType.uint32, 'negative-sd-max'), ['int'])),
                                                                    ('negative_sd_count', (YLeaf(YType.uint32, 'negative-sd-count'), ['int'])),
                                                                    ('positive_ds_sum', (YLeaf(YType.uint32, 'positive-ds-sum'), ['int'])),
                                                                    ('positive_ds_sum2', (YLeaf(YType.uint64, 'positive-ds-sum2'), ['int'])),
                                                                    ('positive_ds_min', (YLeaf(YType.uint32, 'positive-ds-min'), ['int'])),
                                                                    ('positive_ds_max', (YLeaf(YType.uint32, 'positive-ds-max'), ['int'])),
                                                                    ('positive_ds_count', (YLeaf(YType.uint32, 'positive-ds-count'), ['int'])),
                                                                    ('negative_ds_sum', (YLeaf(YType.uint32, 'negative-ds-sum'), ['int'])),
                                                                    ('negative_ds_sum2', (YLeaf(YType.uint64, 'negative-ds-sum2'), ['int'])),
                                                                    ('negative_ds_min', (YLeaf(YType.uint32, 'negative-ds-min'), ['int'])),
                                                                    ('negative_ds_max', (YLeaf(YType.uint32, 'negative-ds-max'), ['int'])),
                                                                    ('negative_ds_count', (YLeaf(YType.uint32, 'negative-ds-count'), ['int'])),
                                                                    ('one_way_count', (YLeaf(YType.uint32, 'one-way-count'), ['int'])),
                                                                    ('one_way_sd_min', (YLeaf(YType.uint32, 'one-way-sd-min'), ['int'])),
                                                                    ('one_way_sd_max', (YLeaf(YType.uint32, 'one-way-sd-max'), ['int'])),
                                                                    ('one_way_sd_sum', (YLeaf(YType.uint32, 'one-way-sd-sum'), ['int'])),
                                                                    ('one_way_sd_sum2', (YLeaf(YType.uint64, 'one-way-sd-sum2'), ['int'])),
                                                                    ('one_way_ds_min', (YLeaf(YType.uint32, 'one-way-ds-min'), ['int'])),
                                                                    ('one_way_ds_max', (YLeaf(YType.uint32, 'one-way-ds-max'), ['int'])),
                                                                    ('one_way_ds_sum', (YLeaf(YType.uint32, 'one-way-ds-sum'), ['int'])),
                                                                    ('one_way_ds_sum2', (YLeaf(YType.uint64, 'one-way-ds-sum2'), ['int'])),
                                                                ])
                                                                self.jitter_in = None
                                                                self.jitter_out = None
                                                                self.packet_loss_sd = None
                                                                self.packet_loss_ds = None
                                                                self.packet_out_of_sequence = None
                                                                self.packet_mia = None
                                                                self.packet_skipped = None
                                                                self.packet_late_arrivals = None
                                                                self.packet_invalid_tstamp = None
                                                                self.internal_errors_count = None
                                                                self.busies_count = None
                                                                self.positive_sd_sum = None
                                                                self.positive_sd_sum2 = None
                                                                self.positive_sd_min = None
                                                                self.positive_sd_max = None
                                                                self.positive_sd_count = None
                                                                self.negative_sd_sum = None
                                                                self.negative_sd_sum2 = None
                                                                self.negative_sd_min = None
                                                                self.negative_sd_max = None
                                                                self.negative_sd_count = None
                                                                self.positive_ds_sum = None
                                                                self.positive_ds_sum2 = None
                                                                self.positive_ds_min = None
                                                                self.positive_ds_max = None
                                                                self.positive_ds_count = None
                                                                self.negative_ds_sum = None
                                                                self.negative_ds_sum2 = None
                                                                self.negative_ds_min = None
                                                                self.negative_ds_max = None
                                                                self.negative_ds_count = None
                                                                self.one_way_count = None
                                                                self.one_way_sd_min = None
                                                                self.one_way_sd_max = None
                                                                self.one_way_sd_sum = None
                                                                self.one_way_sd_sum2 = None
                                                                self.one_way_ds_min = None
                                                                self.one_way_ds_max = None
                                                                self.one_way_ds_sum = None
                                                                self.one_way_ds_sum2 = None
                                                                self._segment_path = lambda: "udp-jitter-stats"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.Paths.Path.Hops.Hop.SpecificStats.UdpJitterStats, [u'jitter_in', u'jitter_out', u'packet_loss_sd', u'packet_loss_ds', u'packet_out_of_sequence', u'packet_mia', u'packet_skipped', u'packet_late_arrivals', u'packet_invalid_tstamp', u'internal_errors_count', u'busies_count', u'positive_sd_sum', u'positive_sd_sum2', u'positive_sd_min', u'positive_sd_max', u'positive_sd_count', u'negative_sd_sum', u'negative_sd_sum2', u'negative_sd_min', u'negative_sd_max', u'negative_sd_count', u'positive_ds_sum', u'positive_ds_sum2', u'positive_ds_min', u'positive_ds_max', u'positive_ds_count', u'negative_ds_sum', u'negative_ds_sum2', u'negative_ds_min', u'negative_ds_max', u'negative_ds_count', u'one_way_count', u'one_way_sd_min', u'one_way_sd_max', u'one_way_sd_sum', u'one_way_sd_sum2', u'one_way_ds_min', u'one_way_ds_max', u'one_way_ds_sum', u'one_way_ds_sum2'], name, value)


                                    class LpdPaths(Entity):
                                        """
                                        List of latest LPD paths
                                        
                                        .. attribute:: lpd_path
                                        
                                        	Latest path statistics of MPLS LSP group operation
                                        	**type**\: list of  		 :py:class:`LpdPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath>`
                                        
                                        

                                        """

                                        _prefix = 'man-ipsla-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths, self).__init__()

                                            self.yang_name = "lpd-paths"
                                            self.yang_parent_name = "non-distributed"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("lpd-path", ("lpd_path", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath))])
                                            self._leafs = OrderedDict()

                                            self.lpd_path = YList(self)
                                            self._segment_path = lambda: "lpd-paths"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths, [], name, value)


                                        class LpdPath(Entity):
                                            """
                                            Latest path statistics of MPLS LSP
                                            group operation
                                            
                                            .. attribute:: path_index  (key)
                                            
                                            	LPD path index
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: path_id
                                            
                                            	LPD path identifier
                                            	**type**\:  :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath.PathId>`
                                            
                                            .. attribute:: return_code
                                            
                                            	Path return code
                                            	**type**\:  :py:class:`IpslaRetCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.IpslaRetCode>`
                                            
                                            

                                            """

                                            _prefix = 'man-ipsla-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath, self).__init__()

                                                self.yang_name = "lpd-path"
                                                self.yang_parent_name = "lpd-paths"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['path_index']
                                                self._child_classes = OrderedDict([("path-id", ("path_id", Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath.PathId))])
                                                self._leafs = OrderedDict([
                                                    ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                                    ('return_code', (YLeaf(YType.enumeration, 'return-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'IpslaRetCode', '')])),
                                                ])
                                                self.path_index = None
                                                self.return_code = None

                                                self.path_id = Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath.PathId()
                                                self.path_id.parent = self
                                                self._children_name_map["path_id"] = "path-id"
                                                self._segment_path = lambda: "lpd-path" + "[path-index='" + str(self.path_index) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath, ['path_index', u'return_code'], name, value)


                                            class PathId(Entity):
                                                """
                                                LPD path identifier
                                                
                                                .. attribute:: lsp_selector
                                                
                                                	LSP selector
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: output_interface
                                                
                                                	Output interface
                                                	**type**\: str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                                
                                                .. attribute:: nexthop_address
                                                
                                                	Nexthop address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: downstream_label
                                                
                                                	Downstream label stacks
                                                	**type**\: list of int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'man-ipsla-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath.PathId, self).__init__()

                                                    self.yang_name = "path-id"
                                                    self.yang_parent_name = "lpd-path"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                                        ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                                        ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                                        ('downstream_label', (YLeafList(YType.uint32, 'downstream-label'), ['int'])),
                                                    ])
                                                    self.lsp_selector = None
                                                    self.output_interface = None
                                                    self.nexthop_address = None
                                                    self.downstream_label = []
                                                    self._segment_path = lambda: "path-id"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipsla.OperationData.Operations.Operation.Statistics.Aggregated.Hours.Hour.NonDistributed.LpdPaths.LpdPath.PathId, [u'lsp_selector', u'output_interface', u'nexthop_address', u'downstream_label'], name, value)


    class ApplicationInfo(Entity):
        """
        IPSLA application information
        
        .. attribute:: version
        
        	Version of the IPSLA in Version.Release .Patch\-level format
        	**type**\: str
        
        .. attribute:: max_entries
        
        	Maximum number of entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: entries_configured
        
        	Number of entries configured
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: active_entries
        
        	Number of active entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: pending_entries
        
        	Number of pending entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: inactive_entries
        
        	Number of inactive entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: configurable_probes
        
        	Number of configurable probes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: min_memory
        
        	IPSLA low memory watermark in KB
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: hw_timestamp_disabled
        
        	IPSLA HW timestamp Disabled flag
        	**type**\: bool
        
        .. attribute:: operation_type
        
        	Operation types available in this IPSLA version
        	**type**\: list of   :py:class:`SlaOpTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper.SlaOpTypes>`
        
        

        """

        _prefix = 'man-ipsla-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.ApplicationInfo, self).__init__()

            self.yang_name = "application-info"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
                ('entries_configured', (YLeaf(YType.uint32, 'entries-configured'), ['int'])),
                ('active_entries', (YLeaf(YType.uint32, 'active-entries'), ['int'])),
                ('pending_entries', (YLeaf(YType.uint32, 'pending-entries'), ['int'])),
                ('inactive_entries', (YLeaf(YType.uint32, 'inactive-entries'), ['int'])),
                ('configurable_probes', (YLeaf(YType.uint32, 'configurable-probes'), ['int'])),
                ('min_memory', (YLeaf(YType.uint32, 'min-memory'), ['int'])),
                ('hw_timestamp_disabled', (YLeaf(YType.boolean, 'hw-timestamp-disabled'), ['bool'])),
                ('operation_type', (YLeafList(YType.enumeration, 'operation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_oper', 'SlaOpTypes', '')])),
            ])
            self.version = None
            self.max_entries = None
            self.entries_configured = None
            self.active_entries = None
            self.pending_entries = None
            self.inactive_entries = None
            self.configurable_probes = None
            self.min_memory = None
            self.hw_timestamp_disabled = None
            self.operation_type = []
            self._segment_path = lambda: "application-info"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-oper:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.ApplicationInfo, [u'version', u'max_entries', u'entries_configured', u'active_entries', u'pending_entries', u'inactive_entries', u'configurable_probes', u'min_memory', u'hw_timestamp_disabled', u'operation_type'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipsla()
        return self._top_entity

