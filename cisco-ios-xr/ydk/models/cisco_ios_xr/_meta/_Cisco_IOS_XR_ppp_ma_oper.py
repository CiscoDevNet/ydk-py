


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PppIphcCompressionEnum' : _MetaInfoEnum('PppIphcCompressionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper',
        {
            'ppp-iphc-compression-fmt-none':'ppp_iphc_compression_fmt_none',
            'ppp-iphc-compression-fmt-vj':'ppp_iphc_compression_fmt_vj',
            'ppp-iphc-compression-fmt-ietf':'ppp_iphc_compression_fmt_ietf',
            'ppp-iphc-compression-fmt-iphc':'ppp_iphc_compression_fmt_iphc',
            'ppp-iphc-compression-fmt-cisco':'ppp_iphc_compression_fmt_cisco',
        }, 'Cisco-IOS-XR-ppp-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper']),
    'PppLcpMpMbrStateEnum' : _MetaInfoEnum('PppLcpMpMbrStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper',
        {
            'ppp-lcp-mp-mbr-state-detached':'ppp_lcp_mp_mbr_state_detached',
            'ppp-lcp-mp-mbr-state-lcp-not-negotiated':'ppp_lcp_mp_mbr_state_lcp_not_negotiated',
            'ppp-lcp-mp-mbr-state-link-noise':'ppp_lcp_mp_mbr_state_link_noise',
            'ppp-lcp-mp-mbr-state-bundle-shutdown':'ppp_lcp_mp_mbr_state_bundle_shutdown',
            'ppp-lcp-mp-mbr-state-mrru-rejected':'ppp_lcp_mp_mbr_state_mrru_rejected',
            'ppp-lcp-mp-mbr-state-mrru-mismatch':'ppp_lcp_mp_mbr_state_mrru_mismatch',
            'ppp-lcp-mp-mbr-state-ed-mismatch':'ppp_lcp_mp_mbr_state_ed_mismatch',
            'ppp-lcp-mp-mbr-state-auth-name-mismatch':'ppp_lcp_mp_mbr_state_auth_name_mismatch',
            'ppp-lcp-mp-mbr-state-mcmp-rejected':'ppp_lcp_mp_mbr_state_mcmp_rejected',
            'ppp-lcp-mp-mbr-state-mcmp-not-negotiated':'ppp_lcp_mp_mbr_state_mcmp_not_negotiated',
            'ppp-lcp-mp-mbr-state-mcmp-local-mismatch':'ppp_lcp_mp_mbr_state_mcmp_local_mismatch',
            'ppp-lcp-mp-mbr-state-mcmp-peer-mismatch':'ppp_lcp_mp_mbr_state_mcmp_peer_mismatch',
            'ppp-lcp-mp-mbr-state-standby-up':'ppp_lcp_mp_mbr_state_standby_up',
            'ppp-lcp-mp-mbr-state-active':'ppp_lcp_mp_mbr_state_active',
        }, 'Cisco-IOS-XR-ppp-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper']),
    'PppSsoFsmStateEnum' : _MetaInfoEnum('PppSsoFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper',
        {
            'ppp-sso-state-not-ready-0':'ppp_sso_state_not_ready_0',
            'ppp-sso-state-standby-unnegd-1':'ppp_sso_state_standby_unnegd_1',
            'ppp-sso-state-active-down-2':'ppp_sso_state_active_down_2',
            'ppp-sso-state-deactivating-3':'ppp_sso_state_deactivating_3',
            'ppp-sso-state-active-unnegd-4':'ppp_sso_state_active_unnegd_4',
            'ppp-sso-state-standby-negd-5':'ppp_sso_state_standby_negd_5',
            'ppp-sso-state-activating-6':'ppp_sso_state_activating_6',
            'ppp-sso-state-active-negd-7':'ppp_sso_state_active_negd_7',
        }, 'Cisco-IOS-XR-ppp-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper']),
    'PppFsmStateEnum' : _MetaInfoEnum('PppFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper',
        {
            'ppp-fsm-state-initial-0':'ppp_fsm_state_initial_0',
            'ppp-fsm-state-starting-1':'ppp_fsm_state_starting_1',
            'ppp-fsm-state-closed-2':'ppp_fsm_state_closed_2',
            'ppp-fsm-state-stopped-3':'ppp_fsm_state_stopped_3',
            'ppp-fsm-state-closing-4':'ppp_fsm_state_closing_4',
            'ppp-fsm-state-stopping-5':'ppp_fsm_state_stopping_5',
            'ppp-fsm-state-req-sent-6':'ppp_fsm_state_req_sent_6',
            'ppp-fsm-state-ack-rcvd-7':'ppp_fsm_state_ack_rcvd_7',
            'ppp-fsm-state-ack-sent-8':'ppp_fsm_state_ack_sent_8',
            'ppp-fsm-state-opened-9':'ppp_fsm_state_opened_9',
        }, 'Cisco-IOS-XR-ppp-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper']),
    'NcpIdentEnum' : _MetaInfoEnum('NcpIdentEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper',
        {
            'cdpcp':'cdpcp',
            'ipcp':'ipcp',
            'ipcpiw':'ipcpiw',
            'ipv6cp':'ipv6cp',
            'mplscp':'mplscp',
            'osicp':'osicp',
        }, 'Cisco-IOS-XR-ppp-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper']),
    'Ppp.Nodes.Node.Statistics.LcpStatistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Statistics.LcpStatistics',
            False, 
            [
            _MetaInfoClassMember('code-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Code Rej Packets Received
                ''',
                'code_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('code-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Code Rej Packets Sent
                ''',
                'code_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Ack Packets Received
                ''',
                'conf_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Ack Packets Sent
                ''',
                'conf_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Nak Packets Received
                ''',
                'conf_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Nak Packets Sent
                ''',
                'conf_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Rej Packets Received
                ''',
                'conf_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Rej Packets Sent
                ''',
                'conf_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Req Packets Received
                ''',
                'conf_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Req Packets Sent
                ''',
                'conf_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('disc-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Disc Req Packets Received
                ''',
                'disc_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('disc-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Disc Req Packets Sent
                ''',
                'disc_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-rep-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Echo Rep Packets Received
                ''',
                'echo_rep_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-rep-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Echo Rep Packets Sent
                ''',
                'echo_rep_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Echo Req Packets Received
                ''',
                'echo_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Echo Req Packets Sent
                ''',
                'echo_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('link-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Keepalive link failure count
                ''',
                'link_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('link-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Line Protocol Up count
                ''',
                'link_up',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('proto-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Proto Rej Packets Received
                ''',
                'proto_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('proto-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Proto Rej Packets Sent
                ''',
                'proto_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Ack Packets Received
                ''',
                'term_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Ack Packets Sent
                ''',
                'term_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Req Packets Received
                ''',
                'term_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Req Packets Sent
                ''',
                'term_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Statistics.AuthenticationStatistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Statistics.AuthenticationStatistics',
            False, 
            [
            _MetaInfoClassMember('auth-timeout-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Authentication timeout count
                ''',
                'auth_timeout_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-chall-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP challenge packets received
                ''',
                'chap_chall_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-chall-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP challenge packets sent
                ''',
                'chap_chall_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-fail-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP reply failure packets received
                ''',
                'chap_rep_fail_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-fail-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP reply failure packets sent
                ''',
                'chap_rep_fail_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-succ-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP reply success packets received
                ''',
                'chap_rep_succ_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-succ-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP reply success packets sent
                ''',
                'chap_rep_succ_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-resp-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP response packets received
                ''',
                'chap_resp_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-resp-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CHAP response packets sent
                ''',
                'chap_resp_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Ack packets received
                ''',
                'pap_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Ack packets sent
                ''',
                'pap_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Nak packets received
                ''',
                'pap_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Nak packets sent
                ''',
                'pap_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Request packets received
                ''',
                'pap_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PAP Request packets sent
                ''',
                'pap_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'authentication-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Statistics.NcpStatisticsArray' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Statistics.NcpStatisticsArray',
            False, 
            [
            _MetaInfoClassMember('conf-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Ack Packets Received
                ''',
                'conf_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Ack Packets Sent
                ''',
                'conf_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Nak Packets Received
                ''',
                'conf_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Nak Packets Sent
                ''',
                'conf_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Rej Packets Received
                ''',
                'conf_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Rej Packets Sent
                ''',
                'conf_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Req Packets Received
                ''',
                'conf_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Conf Req Packets Sent
                ''',
                'conf_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-identifier', REFERENCE_ENUM_CLASS, 'NcpIdentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'NcpIdentEnum', 
                [], [], 
                '''                NCP identifier
                ''',
                'ncp_identifier',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('proto-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Proto Rej Packets Received
                ''',
                'proto_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('proto-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Proto Rej Packets Sent
                ''',
                'proto_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Ack Packets Received
                ''',
                'term_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Ack Packets Sent
                ''',
                'term_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Req Packets Received
                ''',
                'term_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('term-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Term Req Packets Sent
                ''',
                'term_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ncp-statistics-array',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('authentication-statistics', REFERENCE_CLASS, 'AuthenticationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Statistics.AuthenticationStatistics', 
                [], [], 
                '''                PPP Authentication statistics
                ''',
                'authentication_statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-statistics', REFERENCE_CLASS, 'LcpStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Statistics.LcpStatistics', 
                [], [], 
                '''                PPP LCP Statistics
                ''',
                'lcp_statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-statistics-array', REFERENCE_LIST, 'NcpStatisticsArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Statistics.NcpStatisticsArray', 
                [], [], 
                '''                Array of PPP NCP Statistics
                ''',
                'ncp_statistics_array',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppLcpMpMbrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppLcpMpMbrStateEnum', 
                [], [], 
                '''                Member State
                ''',
                'state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'mp-member-info-array',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo',
            False, 
            [
            _MetaInfoClassMember('active-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of active links
                ''',
                'active_links',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('inactive-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of inactive links
                ''',
                'inactive_links',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-mp-bundle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is an MP bundle
                ''',
                'is_mp_bundle',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-mp-bundle-member', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MP Bundle Member
                ''',
                'is_mp_bundle_member',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('minimum-active-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum active links required for the MPbundle
                to come up
                ''',
                'minimum_active_links',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('mp-bundle-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                MP Bundle Interface
                ''',
                'mp_bundle_interface',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('mp-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MP Group
                ''',
                'mp_group',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('mp-member-info-array', REFERENCE_LIST, 'MpMemberInfoArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray', 
                [], [], 
                '''                Array of MP members
                ''',
                'mp_member_info_array',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('mp-state', REFERENCE_ENUM_CLASS, 'PppLcpMpMbrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppLcpMpMbrStateEnum', 
                [], [], 
                '''                Member State
                ''',
                'mp_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'mp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout',
            False, 
            [
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'configured-timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo',
            False, 
            [
            _MetaInfoClassMember('is-authenticated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is authenticated
                ''',
                'is_authenticated',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-sso-authenticated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO authenticated
                ''',
                'is_sso_authenticated',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Of Peer authentication type
                ''',
                'of_peer_auth',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer's authenticated name
                ''',
                'of_peer_name',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-sso-state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                Of Peer auth SSO FSM State
                ''',
                'of_peer_sso_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Of Us authentication type
                ''',
                'of_us_auth',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local authenticated name
                ''',
                'of_us_name',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-sso-state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                Of Us auth SSO FSM State
                ''',
                'of_us_sso_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'auth-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions',
            False, 
            [
            _MetaInfoClassMember('compression-type', REFERENCE_ENUM_CLASS, 'PppIphcCompressionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppIphcCompressionEnum', 
                [], [], 
                '''                Compression type
                ''',
                'compression_type',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ec-rtp-compression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EcRTP compression
                ''',
                'ec_rtp_compression',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max header
                ''',
                'max_header',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max period
                ''',
                'max_period',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max time
                ''',
                'max_time',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('non-tcp-space', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Non-TCP space
                ''',
                'non_tcp_space',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('rtp-compression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RTP compression
                ''',
                'rtp_compression',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('tcp-space', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TCP space
                ''',
                'tcp_space',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'local-iphc-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions',
            False, 
            [
            _MetaInfoClassMember('compression-type', REFERENCE_ENUM_CLASS, 'PppIphcCompressionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppIphcCompressionEnum', 
                [], [], 
                '''                Compression type
                ''',
                'compression_type',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ec-rtp-compression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EcRTP compression
                ''',
                'ec_rtp_compression',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max header
                ''',
                'max_header',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max period
                ''',
                'max_period',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('max-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max time
                ''',
                'max_time',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('non-tcp-space', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Non-TCP space
                ''',
                'non_tcp_space',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('rtp-compression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RTP compression
                ''',
                'rtp_compression',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('tcp-space', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TCP space
                ''',
                'tcp_space',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'peer-iphc-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo',
            False, 
            [
            _MetaInfoClassMember('dns-primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer DNS Primary
                ''',
                'dns_primary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('dns-secondary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer DNS Secondary
                ''',
                'dns_secondary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-iphc-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is IPHC Configured
                ''',
                'is_iphc_configured',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv4 address
                ''',
                'local_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-iphc-options', REFERENCE_CLASS, 'LocalIphcOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions', 
                [], [], 
                '''                Local IPHC options
                ''',
                'local_iphc_options',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 address
                ''',
                'peer_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-iphc-options', REFERENCE_CLASS, 'PeerIphcOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions', 
                [], [], 
                '''                Peer IPHC options
                ''',
                'peer_iphc_options',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 netmask
                ''',
                'peer_netmask',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('wins-primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer WINS Primary
                ''',
                'wins_primary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('wins-secondary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer WINS Secondary
                ''',
                'wins_secondary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipcp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo',
            False, 
            [
            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv4 address
                ''',
                'local_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 address
                ''',
                'peer_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipcpiw-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo',
            False, 
            [
            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv6 address
                ''',
                'local_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 address
                ''',
                'peer_address',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipv6cp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo',
            False, 
            [
            _MetaInfoClassMember('ipcp-info', REFERENCE_CLASS, 'IpcpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo', 
                [], [], 
                '''                Info for IPCP
                ''',
                'ipcp_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ipcpiw-info', REFERENCE_CLASS, 'IpcpiwInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo', 
                [], [], 
                '''                Info for IPCPIW
                ''',
                'ipcpiw_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ipv6cp-info', REFERENCE_CLASS, 'Ipv6CpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo', 
                [], [], 
                '''                Info for IPv6CP
                ''',
                'ipv6cp_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'NcpIdentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'NcpIdentEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ncp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray',
            False, 
            [
            _MetaInfoClassMember('is-passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Passive
                ''',
                'is_passive',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-identifier', REFERENCE_ENUM_CLASS, 'NcpIdentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'NcpIdentEnum', 
                [], [], 
                '''                NCP state identifier
                ''',
                'ncp_identifier',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-info', REFERENCE_CLASS, 'NcpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo', 
                [], [], 
                '''                Specific NCP info
                ''',
                'ncp_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-state', REFERENCE_ENUM_CLASS, 'PppFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppFsmStateEnum', 
                [], [], 
                '''                NCP state value
                ''',
                'ncp_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncpsso-state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                NCP SSO State
                ''',
                'ncpsso_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ncp-info-array',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces.NodeInterface' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces.NodeInterface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface running PPP
                ''',
                'interface',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('auth-info', REFERENCE_CLASS, 'AuthInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo', 
                [], [], 
                '''                Authentication information
                ''',
                'auth_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('configured-timeout', REFERENCE_CLASS, 'ConfiguredTimeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout', 
                [], [], 
                '''                Configured timeout
                ''',
                'configured_timeout',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ip-interworking-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP Interworking Enabled
                ''',
                'ip_interworking_enabled',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-l2ac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is L2 AC
                ''',
                'is_l2ac',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-lcp-delayed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is LCP Delayed
                ''',
                'is_lcp_delayed',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-loopback-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loopback detected
                ''',
                'is_loopback_detected',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-mcmp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is MCMP enabled
                ''',
                'is_mcmp_enabled',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-ssrp-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSRP configured
                ''',
                'is_ssrp_configured',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-tunneled-session', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is tunneled session
                ''',
                'is_tunneled_session',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('keepalive-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive value
                ''',
                'keepalive_period',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('keepalive-retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive retry count
                ''',
                'keepalive_retry_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-state', REFERENCE_ENUM_CLASS, 'PppFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppFsmStateEnum', 
                [], [], 
                '''                PPP/LCP state value
                ''',
                'lcp_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcpsso-state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                LCP SSO state
                ''',
                'lcpsso_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('line-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line state
                ''',
                'line_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-ed', ATTRIBUTE, 'str' , None, None, 
                [(0, 41)], [], 
                '''                Local Endpt Discriminator
                ''',
                'local_ed',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-mcmp-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local MCMP classes
                ''',
                'local_mcmp_classes',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-mrru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local MRRU
                ''',
                'local_mrru',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('local-mru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local MRU
                ''',
                'local_mru',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('mp-info', REFERENCE_CLASS, 'MpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo', 
                [], [], 
                '''                MP information
                ''',
                'mp_info',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-info-array', REFERENCE_LIST, 'NcpInfoArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray', 
                [], [], 
                '''                Array of per-NCP data
                ''',
                'ncp_info_array',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('parent-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parent state
                ''',
                'parent_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-ed', ATTRIBUTE, 'str' , None, None, 
                [(0, 41)], [], 
                '''                Peer Endpt Discriminator
                ''',
                'peer_ed',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-mcmp-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Peer MCMP classes
                ''',
                'peer_mcmp_classes',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-mrru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Peer MRRU
                ''',
                'peer_mrru',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('peer-mru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Peer MRU
                ''',
                'peer_mru',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('provisioned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Provisioned
                ''',
                'provisioned',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('session-expires', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session expiry time in seconds since 00:00:00 on
                January 1, 1970, UTC.
                ''',
                'session_expires',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('srg-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRG role
                ''',
                'srg_role',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ssrp-peer-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SSRP Peer ID
                ''',
                'ssrp_peer_id',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('xconnect-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                XConnect ID
                ''',
                'xconnect_id',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'node-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaces',
            False, 
            [
            _MetaInfoClassMember('node-interface', REFERENCE_LIST, 'NodeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces.NodeInterface', 
                [], [], 
                '''                LCP and summarized NCP data for an interface
                running PPP
                ''',
                'node_interface',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'node-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSO Error
                ''',
                'error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO Error
                ''',
                'is_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSO Error
                ''',
                'error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO Error
                ''',
                'is_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-us-auth-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSO Error
                ''',
                'error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO Error
                ''',
                'is_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-peer-auth-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSO Error
                ''',
                'error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('is-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO Error
                ''',
                'is_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipcp-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts.SsoAlert' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts.SsoAlert',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface with SSO Alert
                ''',
                'interface',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('ipcp-error', REFERENCE_CLASS, 'IpcpError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError', 
                [], [], 
                '''                IPCP SSO Error
                ''',
                'ipcp_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-error', REFERENCE_CLASS, 'LcpError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError', 
                [], [], 
                '''                LCP SSO Error
                ''',
                'lcp_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-auth-error', REFERENCE_CLASS, 'OfPeerAuthError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError', 
                [], [], 
                '''                Of-peer Authentication SSO Error
                ''',
                'of_peer_auth_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-auth-error', REFERENCE_CLASS, 'OfUsAuthError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError', 
                [], [], 
                '''                Of-us Authentication SSO Error
                ''',
                'of_us_auth_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-alert',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoAlerts' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoAlerts',
            False, 
            [
            _MetaInfoClassMember('sso-alert', REFERENCE_LIST, 'SsoAlert' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts.SsoAlert', 
                [], [], 
                '''                PPP SSO Alert data for a particular interface
                ''',
                'sso_alert',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-alerts',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics',
            False, 
            [
            _MetaInfoClassMember('conf-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Ack Packets Received
                ''',
                'conf_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Ack Packets Sent
                ''',
                'conf_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Nak Packets Received
                ''',
                'conf_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Nak Packets Sent
                ''',
                'conf_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Rej Packets Received
                ''',
                'conf_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Rej Packets Sent
                ''',
                'conf_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Req Packets Received
                ''',
                'conf_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Req Packets Sent
                ''',
                'conf_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('disc-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Disc Req Packets Received
                ''',
                'disc_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('disc-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Disc Req Packets Sent
                ''',
                'disc_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-rep-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Echo Rep Packets Received
                ''',
                'echo_rep_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-rep-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Echo Rep Packets Sent
                ''',
                'echo_rep_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Echo Req Packets Received
                ''',
                'echo_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('echo-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Echo Req Packets Sent
                ''',
                'echo_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('link-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive link failure count
                ''',
                'link_error',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('link-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Line Protocol Up count
                ''',
                'link_up',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics',
            False, 
            [
            _MetaInfoClassMember('auth-timeout-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Authentication timeout count
                ''',
                'auth_timeout_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-chall-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP challenge packets received
                ''',
                'chap_chall_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-chall-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP challenge packets sent
                ''',
                'chap_chall_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-fail-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP reply failure packets received
                ''',
                'chap_rep_fail_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-fail-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP reply failure packets sent
                ''',
                'chap_rep_fail_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-succ-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP reply success packets received
                ''',
                'chap_rep_succ_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-rep-succ-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP reply success packets sent
                ''',
                'chap_rep_succ_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-resp-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP response packets received
                ''',
                'chap_resp_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('chap-resp-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                CHAP response packets sent
                ''',
                'chap_resp_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Ack packets received
                ''',
                'pap_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Ack packets sent
                ''',
                'pap_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Nak packets received
                ''',
                'pap_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Nak packets sent
                ''',
                'pap_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Request packets received
                ''',
                'pap_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pap-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PAP Request packets sent
                ''',
                'pap_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'authentication-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray',
            False, 
            [
            _MetaInfoClassMember('conf-ack-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Ack Packets Received
                ''',
                'conf_ack_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Ack Packets Sent
                ''',
                'conf_ack_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Nak Packets Received
                ''',
                'conf_nak_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-nak-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Nak Packets Sent
                ''',
                'conf_nak_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Rej Packets Received
                ''',
                'conf_rej_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-rej-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Rej Packets Sent
                ''',
                'conf_rej_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Req Packets Received
                ''',
                'conf_req_rcvd',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('conf-req-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Conf Req Packets Sent
                ''',
                'conf_req_sent',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-identifier', REFERENCE_ENUM_CLASS, 'NcpIdentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'NcpIdentEnum', 
                [], [], 
                '''                NCP identifier
                ''',
                'ncp_identifier',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ncp-statistics-array',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface running PPP
                ''',
                'interface_name',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('authentication-statistics', REFERENCE_CLASS, 'AuthenticationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics', 
                [], [], 
                '''                PPP Authentication statistics
                ''',
                'authentication_statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-statistics', REFERENCE_CLASS, 'LcpStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics', 
                [], [], 
                '''                PPP LCP Statistics
                ''',
                'lcp_statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncp-statistics-array', REFERENCE_LIST, 'NcpStatisticsArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray', 
                [], [], 
                '''                Array of PPP NCP Statistics
                ''',
                'ncp_statistics_array',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'node-interface-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.NodeInterfaceStatistics' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.NodeInterfaceStatistics',
            False, 
            [
            _MetaInfoClassMember('node-interface-statistic', REFERENCE_LIST, 'NodeInterfaceStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic', 
                [], [], 
                '''                LCP and NCP statistics for an interface
                running PPP
                ''',
                'node_interface_statistic',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'node-interface-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoSummary.LcpStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoSummary.LcpStates',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of SSO FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=8),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of SSO FSMs running
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoSummary.OfUsAuthStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoSummary.OfUsAuthStates',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of SSO FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=8),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of SSO FSMs running
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-us-auth-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of SSO FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=8),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of SSO FSMs running
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-peer-auth-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoSummary.IpcpStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoSummary.IpcpStates',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of SSO FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=8),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of SSO FSMs running
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipcp-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoSummary' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoSummary',
            False, 
            [
            _MetaInfoClassMember('ipcp-states', REFERENCE_CLASS, 'IpcpStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoSummary.IpcpStates', 
                [], [], 
                '''                IPCP SSO FSM States
                ''',
                'ipcp_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-states', REFERENCE_CLASS, 'LcpStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoSummary.LcpStates', 
                [], [], 
                '''                LCP SSO FSM States
                ''',
                'lcp_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-auth-states', REFERENCE_CLASS, 'OfPeerAuthStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates', 
                [], [], 
                '''                Of-peer Authentication SSO FSM States
                ''',
                'of_peer_auth_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-auth-states', REFERENCE_CLASS, 'OfUsAuthStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoSummary.OfUsAuthStates', 
                [], [], 
                '''                Of-us Authentication SSO FSM States
                ''',
                'of_us_auth_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState',
            False, 
            [
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO FSM Running
                ''',
                'is_running',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                SSO FSM State
                ''',
                'state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState',
            False, 
            [
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO FSM Running
                ''',
                'is_running',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                SSO FSM State
                ''',
                'state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-us-auth-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState',
            False, 
            [
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO FSM Running
                ''',
                'is_running',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                SSO FSM State
                ''',
                'state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'of-peer-auth-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState',
            False, 
            [
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SSO FSM Running
                ''',
                'is_running',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppSsoFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'PppSsoFsmStateEnum', 
                [], [], 
                '''                SSO FSM State
                ''',
                'state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ipcp-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Session ID for the interface with SSO
                State
                ''',
                'session_id',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ipcp-state', REFERENCE_CLASS, 'IpcpState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState', 
                [], [], 
                '''                IPCP SSO State
                ''',
                'ipcp_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-state', REFERENCE_CLASS, 'LcpState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState', 
                [], [], 
                '''                LCP SSO State
                ''',
                'lcp_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-peer-auth-state', REFERENCE_CLASS, 'OfPeerAuthState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState', 
                [], [], 
                '''                Of-peer Authentication SSO State
                ''',
                'of_peer_auth_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('of-us-auth-state', REFERENCE_CLASS, 'OfUsAuthState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState', 
                [], [], 
                '''                Of-us Authentication SSO State
                ''',
                'of_us_auth_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('session-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSRP Session ID
                ''',
                'session_id_xr',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates',
            False, 
            [
            _MetaInfoClassMember('sso-state', REFERENCE_LIST, 'SsoState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState', 
                [], [], 
                '''                PPP SSO State data for a particular
                interface
                ''',
                'sso_state',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups.SsoGroup' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups.SsoGroup',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The identifier for the group
                ''',
                'group_id',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('sso-states', REFERENCE_CLASS, 'SsoStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates', 
                [], [], 
                '''                PPP SSO State data for a particular group
                ''',
                'sso_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.SsoGroups' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.SsoGroups',
            False, 
            [
            _MetaInfoClassMember('sso-group', REFERENCE_LIST, 'SsoGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups.SsoGroup', 
                [], [], 
                '''                PPP SSO state data for a particular group
                ''',
                'sso_group',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'sso-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary.Intfs' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary.Intfs',
            False, 
            [
            _MetaInfoClassMember('gcc0-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                GCC0 Count
                ''',
                'gcc0_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('gcc1-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                GCC1 Count
                ''',
                'gcc1_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('multilink-bundle-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multilink Bundle Count
                ''',
                'multilink_bundle_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pos-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POS Count
                ''',
                'pos_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('pppoe-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PPPoE Count
                ''',
                'pppoe_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('serial-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Serial Count
                ''',
                'serial_count',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Count
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'intfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=10),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of LCP FSMs running
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcpfsm-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FSMs in each State
                ''',
                'count',
                'Cisco-IOS-XR-ppp-ma-oper', False, max_elements=10),
            _MetaInfoClassMember('ncp-identifier', REFERENCE_ENUM_CLASS, 'NcpIdentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'NcpIdentEnum', 
                [], [], 
                '''                NCP Identifier
                ''',
                'ncp_identifier',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of FSMs running for this NCP
                ''',
                'total',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ncpfsm-states-array',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary.FsmStates' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary.FsmStates',
            False, 
            [
            _MetaInfoClassMember('lcpfsm-states', REFERENCE_CLASS, 'LcpfsmStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates', 
                [], [], 
                '''                Array of per-LCP FSM States
                ''',
                'lcpfsm_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('ncpfsm-states-array', REFERENCE_LIST, 'NcpfsmStatesArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray', 
                [], [], 
                '''                Array of per-NCP FSM States
                ''',
                'ncpfsm_states_array',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'fsm-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary.LcpAuthPhases' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary.LcpAuthPhases',
            False, 
            [
            _MetaInfoClassMember('authenticating', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions authenticating
                ''',
                'authenticating',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-not-negotiated', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions with LCP not negotiated
                ''',
                'lcp_not_negotiated',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('line-held-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions negotiated but with the line
                held down
                ''',
                'line_held_down',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('up-l2-fwded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of L2 forwarded sessions brought up
                ''',
                'up_l2_fwded',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('up-local-term', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of locally terminated sessions brought up
                ''',
                'up_local_term',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('up-tunneled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VPDN tunneled sessions brought up
                ''',
                'up_tunneled',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'lcp-auth-phases',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('fsm-states', REFERENCE_CLASS, 'FsmStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary.FsmStates', 
                [], [], 
                '''                FSM States
                ''',
                'fsm_states',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('intfs', REFERENCE_CLASS, 'Intfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary.Intfs', 
                [], [], 
                '''                Interfaces running PPP
                ''',
                'intfs',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('lcp-auth-phases', REFERENCE_CLASS, 'LcpAuthPhases' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary.LcpAuthPhases', 
                [], [], 
                '''                LCP/Auth Phases
                ''',
                'lcp_auth_phases',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for the node
                ''',
                'node_name',
                'Cisco-IOS-XR-ppp-ma-oper', True),
            _MetaInfoClassMember('node-interface-statistics', REFERENCE_CLASS, 'NodeInterfaceStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaceStatistics', 
                [], [], 
                '''                Per interface PPP operational statistics
                ''',
                'node_interface_statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('node-interfaces', REFERENCE_CLASS, 'NodeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.NodeInterfaces', 
                [], [], 
                '''                Per interface PPP operational data
                ''',
                'node_interfaces',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('sso-alerts', REFERENCE_CLASS, 'SsoAlerts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoAlerts', 
                [], [], 
                '''                PPP SSO Alert data for a particular node
                ''',
                'sso_alerts',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('sso-groups', REFERENCE_CLASS, 'SsoGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoGroups', 
                [], [], 
                '''                PPP SSO Group data for a particular node
                ''',
                'sso_groups',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('sso-summary', REFERENCE_CLASS, 'SsoSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.SsoSummary', 
                [], [], 
                '''                Summarized PPP SSO data for a particular node
                ''',
                'sso_summary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Statistics', 
                [], [], 
                '''                PPP statistics data for a particular node
                ''',
                'statistics',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node.Summary', 
                [], [], 
                '''                Summarized PPP data for a particular node
                ''',
                'summary',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp.Nodes' : {
        'meta_info' : _MetaInfoClass('Ppp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes.Node', 
                [], [], 
                '''                The PPP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
    'Ppp' : {
        'meta_info' : _MetaInfoClass('Ppp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper', 'Ppp.Nodes', 
                [], [], 
                '''                Per node PPP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ppp-ma-oper', False),
            ],
            'Cisco-IOS-XR-ppp-ma-oper',
            'ppp',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper'
        ),
    },
}
_meta_table['Ppp.Nodes.Node.Statistics.LcpStatistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Statistics']['meta_info']
_meta_table['Ppp.Nodes.Node.Statistics.AuthenticationStatistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Statistics']['meta_info']
_meta_table['Ppp.Nodes.Node.Statistics.NcpStatisticsArray']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Statistics']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaces']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoAlerts']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoSummary.LcpStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoSummary.OfUsAuthStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoSummary.IpcpStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.SsoGroups']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Summary.FsmStates']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Summary.FsmStates']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary.Intfs']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Summary']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary.FsmStates']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Summary']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary.LcpAuthPhases']['meta_info'].parent =_meta_table['Ppp.Nodes.Node.Summary']['meta_info']
_meta_table['Ppp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaces']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoAlerts']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.SsoGroups']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node.Summary']['meta_info'].parent =_meta_table['Ppp.Nodes.Node']['meta_info']
_meta_table['Ppp.Nodes.Node']['meta_info'].parent =_meta_table['Ppp.Nodes']['meta_info']
_meta_table['Ppp.Nodes']['meta_info'].parent =_meta_table['Ppp']['meta_info']
