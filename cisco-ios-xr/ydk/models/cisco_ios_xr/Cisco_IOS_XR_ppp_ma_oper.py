""" Cisco_IOS_XR_ppp_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma package operational data.

This module contains definitions
for the following management objects\:
  ppp\: PPP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NcpIdentEnum(Enum):
    """
    NcpIdentEnum

    Ncp ident

    .. data:: cdpcp = 1

    	CDP control protocol

    .. data:: ipcp = 2

    	IPv4 control protocol

    .. data:: ipcpiw = 3

    	IPv4 Interworking control protocol

    .. data:: ipv6cp = 4

    	IPv6 control protocol

    .. data:: mplscp = 5

    	MPLS control protocol

    .. data:: osicp = 6

    	OSI (CLNS) control protocol

    """

    cdpcp = 1

    ipcp = 2

    ipcpiw = 3

    ipv6cp = 4

    mplscp = 5

    osicp = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['NcpIdentEnum']


class PppFsmStateEnum(Enum):
    """
    PppFsmStateEnum

    Ppp fsm state

    .. data:: ppp_fsm_state_initial_0 = 0

    	Connection Idle

    .. data:: ppp_fsm_state_starting_1 = 1

    	This layer required, but lower layer down

    .. data:: ppp_fsm_state_closed_2 = 2

    	Lower layer up, but this layer not required

    .. data:: ppp_fsm_state_stopped_3 = 3

    	Listening for a Config Request

    .. data:: ppp_fsm_state_closing_4 = 4

    	Shutting down due to local change

    .. data:: ppp_fsm_state_stopping_5 = 5

    	Shutting down due to peer's actions

    .. data:: ppp_fsm_state_req_sent_6 = 6

    	Config Request Sent

    .. data:: ppp_fsm_state_ack_rcvd_7 = 7

    	Config Ack Received

    .. data:: ppp_fsm_state_ack_sent_8 = 8

    	Config Ack Sent

    .. data:: ppp_fsm_state_opened_9 = 9

    	Connection Open

    """

    ppp_fsm_state_initial_0 = 0

    ppp_fsm_state_starting_1 = 1

    ppp_fsm_state_closed_2 = 2

    ppp_fsm_state_stopped_3 = 3

    ppp_fsm_state_closing_4 = 4

    ppp_fsm_state_stopping_5 = 5

    ppp_fsm_state_req_sent_6 = 6

    ppp_fsm_state_ack_rcvd_7 = 7

    ppp_fsm_state_ack_sent_8 = 8

    ppp_fsm_state_opened_9 = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['PppFsmStateEnum']


class PppIphcCompressionEnum(Enum):
    """
    PppIphcCompressionEnum

    IPHC compression type

    .. data:: ppp_iphc_compression_fmt_none = 0

    	None

    .. data:: ppp_iphc_compression_fmt_vj = 1

    	VJ

    .. data:: ppp_iphc_compression_fmt_ietf = 2

    	IETF

    .. data:: ppp_iphc_compression_fmt_iphc = 3

    	IPHC

    .. data:: ppp_iphc_compression_fmt_cisco = 4

    	CISCO

    """

    ppp_iphc_compression_fmt_none = 0

    ppp_iphc_compression_fmt_vj = 1

    ppp_iphc_compression_fmt_ietf = 2

    ppp_iphc_compression_fmt_iphc = 3

    ppp_iphc_compression_fmt_cisco = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['PppIphcCompressionEnum']


class PppLcpMpMbrStateEnum(Enum):
    """
    PppLcpMpMbrStateEnum

    MP member states

    .. data:: ppp_lcp_mp_mbr_state_detached = 0

    	Detached member

    .. data:: ppp_lcp_mp_mbr_state_lcp_not_negotiated = 1

    	LCP has not been negotiated

    .. data:: ppp_lcp_mp_mbr_state_link_noise = 2

    	Link Noise detected

    .. data:: ppp_lcp_mp_mbr_state_bundle_shutdown = 3

    	Multilink Bundle is shutdown

    .. data:: ppp_lcp_mp_mbr_state_mrru_rejected = 4

    	MRRU has been rejected

    .. data:: ppp_lcp_mp_mbr_state_mrru_mismatch = 5

    	MRRU mismatch

    .. data:: ppp_lcp_mp_mbr_state_ed_mismatch = 6

    	ED mismatch

    .. data:: ppp_lcp_mp_mbr_state_auth_name_mismatch = 7

    	Authenticated name mismatch

    .. data:: ppp_lcp_mp_mbr_state_mcmp_rejected = 8

    	MCMP option rejected by peer

    .. data:: ppp_lcp_mp_mbr_state_mcmp_not_negotiated = 9

    	MCMP option not negotiated

    .. data:: ppp_lcp_mp_mbr_state_mcmp_local_mismatch = 10

    	Local MCMP class mismatch

    .. data:: ppp_lcp_mp_mbr_state_mcmp_peer_mismatch = 11

    	Peer MCMP class mismatch

    .. data:: ppp_lcp_mp_mbr_state_standby_up = 12

    	SSO Standby up

    .. data:: ppp_lcp_mp_mbr_state_active = 13

    	Active member

    """

    ppp_lcp_mp_mbr_state_detached = 0

    ppp_lcp_mp_mbr_state_lcp_not_negotiated = 1

    ppp_lcp_mp_mbr_state_link_noise = 2

    ppp_lcp_mp_mbr_state_bundle_shutdown = 3

    ppp_lcp_mp_mbr_state_mrru_rejected = 4

    ppp_lcp_mp_mbr_state_mrru_mismatch = 5

    ppp_lcp_mp_mbr_state_ed_mismatch = 6

    ppp_lcp_mp_mbr_state_auth_name_mismatch = 7

    ppp_lcp_mp_mbr_state_mcmp_rejected = 8

    ppp_lcp_mp_mbr_state_mcmp_not_negotiated = 9

    ppp_lcp_mp_mbr_state_mcmp_local_mismatch = 10

    ppp_lcp_mp_mbr_state_mcmp_peer_mismatch = 11

    ppp_lcp_mp_mbr_state_standby_up = 12

    ppp_lcp_mp_mbr_state_active = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['PppLcpMpMbrStateEnum']


class PppSsoFsmStateEnum(Enum):
    """
    PppSsoFsmStateEnum

    Ppp sso fsm state

    .. data:: ppp_sso_state_not_ready_0 = 0

    	Not ready

    .. data:: ppp_sso_state_standby_unnegd_1 = 1

    	S UnNegd

    .. data:: ppp_sso_state_active_down_2 = 2

    	A Down

    .. data:: ppp_sso_state_deactivating_3 = 3

    	Deactivating

    .. data:: ppp_sso_state_active_unnegd_4 = 4

    	A UnNegd

    .. data:: ppp_sso_state_standby_negd_5 = 5

    	S Negd

    .. data:: ppp_sso_state_activating_6 = 6

    	Activating

    .. data:: ppp_sso_state_active_negd_7 = 7

    	A Negd

    """

    ppp_sso_state_not_ready_0 = 0

    ppp_sso_state_standby_unnegd_1 = 1

    ppp_sso_state_active_down_2 = 2

    ppp_sso_state_deactivating_3 = 3

    ppp_sso_state_active_unnegd_4 = 4

    ppp_sso_state_standby_negd_5 = 5

    ppp_sso_state_activating_6 = 6

    ppp_sso_state_active_negd_7 = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['PppSsoFsmStateEnum']



class Ppp(object):
    """
    PPP operational data
    
    .. attribute:: nodes
    
    	Per node PPP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes>`
    
    

    """

    _prefix = 'ppp-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Ppp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Per node PPP operational data
        
        .. attribute:: node
        
        	The PPP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node>`
        
        

        """

        _prefix = 'ppp-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The PPP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: node_interface_statistics
            
            	Per interface PPP operational statistics
            	**type**\:   :py:class:`NodeInterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics>`
            
            .. attribute:: node_interfaces
            
            	Per interface PPP operational data
            	**type**\:   :py:class:`NodeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces>`
            
            .. attribute:: sso_alerts
            
            	PPP SSO Alert data for a particular node
            	**type**\:   :py:class:`SsoAlerts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts>`
            
            .. attribute:: sso_groups
            
            	PPP SSO Group data for a particular node
            	**type**\:   :py:class:`SsoGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups>`
            
            .. attribute:: sso_summary
            
            	Summarized PPP SSO data for a particular node
            	**type**\:   :py:class:`SsoSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoSummary>`
            
            .. attribute:: statistics
            
            	PPP statistics data for a particular node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Statistics>`
            
            .. attribute:: summary
            
            	Summarized PPP data for a particular node
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'ppp-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.node_interface_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics()
                self.node_interface_statistics.parent = self
                self.node_interfaces = Ppp.Nodes.Node.NodeInterfaces()
                self.node_interfaces.parent = self
                self.sso_alerts = Ppp.Nodes.Node.SsoAlerts()
                self.sso_alerts.parent = self
                self.sso_groups = Ppp.Nodes.Node.SsoGroups()
                self.sso_groups.parent = self
                self.sso_summary = Ppp.Nodes.Node.SsoSummary()
                self.sso_summary.parent = self
                self.statistics = Ppp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self.summary = Ppp.Nodes.Node.Summary()
                self.summary.parent = self


            class Statistics(object):
                """
                PPP statistics data for a particular node
                
                .. attribute:: authentication_statistics
                
                	PPP Authentication statistics
                	**type**\:   :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Statistics.AuthenticationStatistics>`
                
                .. attribute:: lcp_statistics
                
                	PPP LCP Statistics
                	**type**\:   :py:class:`LcpStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Statistics.LcpStatistics>`
                
                .. attribute:: ncp_statistics_array
                
                	Array of PPP NCP Statistics
                	**type**\: list of    :py:class:`NcpStatisticsArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Statistics.NcpStatisticsArray>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.authentication_statistics = Ppp.Nodes.Node.Statistics.AuthenticationStatistics()
                    self.authentication_statistics.parent = self
                    self.lcp_statistics = Ppp.Nodes.Node.Statistics.LcpStatistics()
                    self.lcp_statistics.parent = self
                    self.ncp_statistics_array = YList()
                    self.ncp_statistics_array.parent = self
                    self.ncp_statistics_array.name = 'ncp_statistics_array'


                class LcpStatistics(object):
                    """
                    PPP LCP Statistics
                    
                    .. attribute:: code_rej_rcvd
                    
                    	Code Rej Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: code_rej_sent
                    
                    	Code Rej Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_ack_rcvd
                    
                    	Conf Ack Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_ack_sent
                    
                    	Conf Ack Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_nak_rcvd
                    
                    	Conf Nak Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_nak_sent
                    
                    	Conf Nak Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_rej_rcvd
                    
                    	Conf Rej Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_rej_sent
                    
                    	Conf Rej Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_req_rcvd
                    
                    	Conf Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_req_sent
                    
                    	Conf Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: disc_req_rcvd
                    
                    	Disc Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: disc_req_sent
                    
                    	Disc Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: echo_rep_rcvd
                    
                    	Echo Rep Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: echo_rep_sent
                    
                    	Echo Rep Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: echo_req_rcvd
                    
                    	Echo Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: echo_req_sent
                    
                    	Echo Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: link_error
                    
                    	Keepalive link failure count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: link_up
                    
                    	Line Protocol Up count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: proto_rej_rcvd
                    
                    	Proto Rej Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: proto_rej_sent
                    
                    	Proto Rej Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_ack_rcvd
                    
                    	Term Ack Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_ack_sent
                    
                    	Term Ack Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_req_rcvd
                    
                    	Term Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_req_sent
                    
                    	Term Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.code_rej_rcvd = None
                        self.code_rej_sent = None
                        self.conf_ack_rcvd = None
                        self.conf_ack_sent = None
                        self.conf_nak_rcvd = None
                        self.conf_nak_sent = None
                        self.conf_rej_rcvd = None
                        self.conf_rej_sent = None
                        self.conf_req_rcvd = None
                        self.conf_req_sent = None
                        self.disc_req_rcvd = None
                        self.disc_req_sent = None
                        self.echo_rep_rcvd = None
                        self.echo_rep_sent = None
                        self.echo_req_rcvd = None
                        self.echo_req_sent = None
                        self.link_error = None
                        self.link_up = None
                        self.proto_rej_rcvd = None
                        self.proto_rej_sent = None
                        self.term_ack_rcvd = None
                        self.term_ack_sent = None
                        self.term_req_rcvd = None
                        self.term_req_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.code_rej_rcvd is not None:
                            return True

                        if self.code_rej_sent is not None:
                            return True

                        if self.conf_ack_rcvd is not None:
                            return True

                        if self.conf_ack_sent is not None:
                            return True

                        if self.conf_nak_rcvd is not None:
                            return True

                        if self.conf_nak_sent is not None:
                            return True

                        if self.conf_rej_rcvd is not None:
                            return True

                        if self.conf_rej_sent is not None:
                            return True

                        if self.conf_req_rcvd is not None:
                            return True

                        if self.conf_req_sent is not None:
                            return True

                        if self.disc_req_rcvd is not None:
                            return True

                        if self.disc_req_sent is not None:
                            return True

                        if self.echo_rep_rcvd is not None:
                            return True

                        if self.echo_rep_sent is not None:
                            return True

                        if self.echo_req_rcvd is not None:
                            return True

                        if self.echo_req_sent is not None:
                            return True

                        if self.link_error is not None:
                            return True

                        if self.link_up is not None:
                            return True

                        if self.proto_rej_rcvd is not None:
                            return True

                        if self.proto_rej_sent is not None:
                            return True

                        if self.term_ack_rcvd is not None:
                            return True

                        if self.term_ack_sent is not None:
                            return True

                        if self.term_req_rcvd is not None:
                            return True

                        if self.term_req_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Statistics.LcpStatistics']['meta_info']


                class AuthenticationStatistics(object):
                    """
                    PPP Authentication statistics
                    
                    .. attribute:: auth_timeout_count
                    
                    	Authentication timeout count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_chall_rcvd
                    
                    	CHAP challenge packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_chall_sent
                    
                    	CHAP challenge packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_rep_fail_rcvd
                    
                    	CHAP reply failure packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_rep_fail_sent
                    
                    	CHAP reply failure packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_rep_succ_rcvd
                    
                    	CHAP reply success packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_rep_succ_sent
                    
                    	CHAP reply success packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_resp_rcvd
                    
                    	CHAP response packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: chap_resp_sent
                    
                    	CHAP response packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_ack_rcvd
                    
                    	PAP Ack packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_ack_sent
                    
                    	PAP Ack packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_nak_rcvd
                    
                    	PAP Nak packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_nak_sent
                    
                    	PAP Nak packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_req_rcvd
                    
                    	PAP Request packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pap_req_sent
                    
                    	PAP Request packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.auth_timeout_count = None
                        self.chap_chall_rcvd = None
                        self.chap_chall_sent = None
                        self.chap_rep_fail_rcvd = None
                        self.chap_rep_fail_sent = None
                        self.chap_rep_succ_rcvd = None
                        self.chap_rep_succ_sent = None
                        self.chap_resp_rcvd = None
                        self.chap_resp_sent = None
                        self.pap_ack_rcvd = None
                        self.pap_ack_sent = None
                        self.pap_nak_rcvd = None
                        self.pap_nak_sent = None
                        self.pap_req_rcvd = None
                        self.pap_req_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:authentication-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.auth_timeout_count is not None:
                            return True

                        if self.chap_chall_rcvd is not None:
                            return True

                        if self.chap_chall_sent is not None:
                            return True

                        if self.chap_rep_fail_rcvd is not None:
                            return True

                        if self.chap_rep_fail_sent is not None:
                            return True

                        if self.chap_rep_succ_rcvd is not None:
                            return True

                        if self.chap_rep_succ_sent is not None:
                            return True

                        if self.chap_resp_rcvd is not None:
                            return True

                        if self.chap_resp_sent is not None:
                            return True

                        if self.pap_ack_rcvd is not None:
                            return True

                        if self.pap_ack_sent is not None:
                            return True

                        if self.pap_nak_rcvd is not None:
                            return True

                        if self.pap_nak_sent is not None:
                            return True

                        if self.pap_req_rcvd is not None:
                            return True

                        if self.pap_req_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Statistics.AuthenticationStatistics']['meta_info']


                class NcpStatisticsArray(object):
                    """
                    Array of PPP NCP Statistics
                    
                    .. attribute:: conf_ack_rcvd
                    
                    	Conf Ack Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_ack_sent
                    
                    	Conf Ack Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_nak_rcvd
                    
                    	Conf Nak Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_nak_sent
                    
                    	Conf Nak Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_rej_rcvd
                    
                    	Conf Rej Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_rej_sent
                    
                    	Conf Rej Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_req_rcvd
                    
                    	Conf Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: conf_req_sent
                    
                    	Conf Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ncp_identifier
                    
                    	NCP identifier
                    	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdentEnum>`
                    
                    .. attribute:: proto_rej_rcvd
                    
                    	Proto Rej Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: proto_rej_sent
                    
                    	Proto Rej Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_ack_rcvd
                    
                    	Term Ack Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_ack_sent
                    
                    	Term Ack Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_req_rcvd
                    
                    	Term Req Packets Received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: term_req_sent
                    
                    	Term Req Packets Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.conf_ack_rcvd = None
                        self.conf_ack_sent = None
                        self.conf_nak_rcvd = None
                        self.conf_nak_sent = None
                        self.conf_rej_rcvd = None
                        self.conf_rej_sent = None
                        self.conf_req_rcvd = None
                        self.conf_req_sent = None
                        self.ncp_identifier = None
                        self.proto_rej_rcvd = None
                        self.proto_rej_sent = None
                        self.term_ack_rcvd = None
                        self.term_ack_sent = None
                        self.term_req_rcvd = None
                        self.term_req_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ncp-statistics-array'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.conf_ack_rcvd is not None:
                            return True

                        if self.conf_ack_sent is not None:
                            return True

                        if self.conf_nak_rcvd is not None:
                            return True

                        if self.conf_nak_sent is not None:
                            return True

                        if self.conf_rej_rcvd is not None:
                            return True

                        if self.conf_rej_sent is not None:
                            return True

                        if self.conf_req_rcvd is not None:
                            return True

                        if self.conf_req_sent is not None:
                            return True

                        if self.ncp_identifier is not None:
                            return True

                        if self.proto_rej_rcvd is not None:
                            return True

                        if self.proto_rej_sent is not None:
                            return True

                        if self.term_ack_rcvd is not None:
                            return True

                        if self.term_ack_sent is not None:
                            return True

                        if self.term_req_rcvd is not None:
                            return True

                        if self.term_req_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Statistics.NcpStatisticsArray']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.authentication_statistics is not None and self.authentication_statistics._has_data():
                        return True

                    if self.lcp_statistics is not None and self.lcp_statistics._has_data():
                        return True

                    if self.ncp_statistics_array is not None:
                        for child_ref in self.ncp_statistics_array:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.Statistics']['meta_info']


            class NodeInterfaces(object):
                """
                Per interface PPP operational data
                
                .. attribute:: node_interface
                
                	LCP and summarized NCP data for an interface running PPP
                	**type**\: list of    :py:class:`NodeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_interface = YList()
                    self.node_interface.parent = self
                    self.node_interface.name = 'node_interface'


                class NodeInterface(object):
                    """
                    LCP and summarized NCP data for an interface
                    running PPP
                    
                    .. attribute:: interface  <key>
                    
                    	Interface running PPP
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: auth_info
                    
                    	Authentication information
                    	**type**\:   :py:class:`AuthInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo>`
                    
                    .. attribute:: configured_timeout
                    
                    	Configured timeout
                    	**type**\:   :py:class:`ConfiguredTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout>`
                    
                    .. attribute:: ip_interworking_enabled
                    
                    	IP Interworking Enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_l2ac
                    
                    	Is L2 AC
                    	**type**\:  bool
                    
                    .. attribute:: is_lcp_delayed
                    
                    	Is LCP Delayed
                    	**type**\:  bool
                    
                    .. attribute:: is_loopback_detected
                    
                    	Loopback detected
                    	**type**\:  bool
                    
                    .. attribute:: is_mcmp_enabled
                    
                    	Is MCMP enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_ssrp_configured
                    
                    	Is SSRP configured
                    	**type**\:  bool
                    
                    .. attribute:: is_tunneled_session
                    
                    	Is tunneled session
                    	**type**\:  bool
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalive_retry_count
                    
                    	Keepalive retry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lcp_state
                    
                    	PPP/LCP state value
                    	**type**\:   :py:class:`PppFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppFsmStateEnum>`
                    
                    .. attribute:: lcpsso_state
                    
                    	LCP SSO state
                    	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                    
                    .. attribute:: line_state
                    
                    	Line state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_ed
                    
                    	Local Endpt Discriminator
                    	**type**\:  str
                    
                    	**length:** 0..41
                    
                    .. attribute:: local_mcmp_classes
                    
                    	Local MCMP classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_mrru
                    
                    	Local MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_mru
                    
                    	Local MRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mp_info
                    
                    	MP information
                    	**type**\:   :py:class:`MpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo>`
                    
                    .. attribute:: ncp_info_array
                    
                    	Array of per\-NCP data
                    	**type**\: list of    :py:class:`NcpInfoArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray>`
                    
                    .. attribute:: parent_state
                    
                    	Parent state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_ed
                    
                    	Peer Endpt Discriminator
                    	**type**\:  str
                    
                    	**length:** 0..41
                    
                    .. attribute:: peer_mcmp_classes
                    
                    	Peer MCMP classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: peer_mrru
                    
                    	Peer MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: peer_mru
                    
                    	Peer MRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: provisioned
                    
                    	Provisioned
                    	**type**\:  bool
                    
                    .. attribute:: session_expires
                    
                    	Session expiry time in seconds since 00\:00\:00 on January 1, 1970, UTC
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: srg_role
                    
                    	SRG role
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ssrp_peer_id
                    
                    	SSRP Peer ID
                    	**type**\:  str
                    
                    .. attribute:: xconnect_id
                    
                    	XConnect ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.auth_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo()
                        self.auth_info.parent = self
                        self.configured_timeout = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout()
                        self.configured_timeout.parent = self
                        self.ip_interworking_enabled = None
                        self.is_l2ac = None
                        self.is_lcp_delayed = None
                        self.is_loopback_detected = None
                        self.is_mcmp_enabled = None
                        self.is_ssrp_configured = None
                        self.is_tunneled_session = None
                        self.keepalive_period = None
                        self.keepalive_retry_count = None
                        self.lcp_state = None
                        self.lcpsso_state = None
                        self.line_state = None
                        self.local_ed = None
                        self.local_mcmp_classes = None
                        self.local_mrru = None
                        self.local_mru = None
                        self.mp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo()
                        self.mp_info.parent = self
                        self.ncp_info_array = YList()
                        self.ncp_info_array.parent = self
                        self.ncp_info_array.name = 'ncp_info_array'
                        self.parent_state = None
                        self.peer_ed = None
                        self.peer_mcmp_classes = None
                        self.peer_mrru = None
                        self.peer_mru = None
                        self.provisioned = None
                        self.session_expires = None
                        self.srg_role = None
                        self.ssrp_peer_id = None
                        self.xconnect_id = None


                    class MpInfo(object):
                        """
                        MP information
                        
                        .. attribute:: active_links
                        
                        	Number of active links
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: inactive_links
                        
                        	Number of inactive links
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: is_mp_bundle
                        
                        	Is an MP bundle
                        	**type**\:  bool
                        
                        .. attribute:: is_mp_bundle_member
                        
                        	MP Bundle Member
                        	**type**\:  bool
                        
                        .. attribute:: minimum_active_links
                        
                        	Minimum active links required for the MPbundle to come up
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mp_bundle_interface
                        
                        	MP Bundle Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: mp_group
                        
                        	MP Group
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mp_member_info_array
                        
                        	Array of MP members
                        	**type**\: list of    :py:class:`MpMemberInfoArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray>`
                        
                        .. attribute:: mp_state
                        
                        	Member State
                        	**type**\:   :py:class:`PppLcpMpMbrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppLcpMpMbrStateEnum>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.active_links = None
                            self.inactive_links = None
                            self.is_mp_bundle = None
                            self.is_mp_bundle_member = None
                            self.minimum_active_links = None
                            self.mp_bundle_interface = None
                            self.mp_group = None
                            self.mp_member_info_array = YList()
                            self.mp_member_info_array.parent = self
                            self.mp_member_info_array.name = 'mp_member_info_array'
                            self.mp_state = None


                        class MpMemberInfoArray(object):
                            """
                            Array of MP members
                            
                            .. attribute:: interface
                            
                            	Member Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: state
                            
                            	Member State
                            	**type**\:   :py:class:`PppLcpMpMbrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppLcpMpMbrStateEnum>`
                            
                            

                            """

                            _prefix = 'ppp-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface = None
                                self.state = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:mp-member-info-array'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:mp-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.active_links is not None:
                                return True

                            if self.inactive_links is not None:
                                return True

                            if self.is_mp_bundle is not None:
                                return True

                            if self.is_mp_bundle_member is not None:
                                return True

                            if self.minimum_active_links is not None:
                                return True

                            if self.mp_bundle_interface is not None:
                                return True

                            if self.mp_group is not None:
                                return True

                            if self.mp_member_info_array is not None:
                                for child_ref in self.mp_member_info_array:
                                    if child_ref._has_data():
                                        return True

                            if self.mp_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo']['meta_info']


                    class ConfiguredTimeout(object):
                        """
                        Configured timeout
                        
                        .. attribute:: minutes
                        
                        	Minutes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: minute
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.minutes = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:configured-timeout'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.minutes is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout']['meta_info']


                    class AuthInfo(object):
                        """
                        Authentication information
                        
                        .. attribute:: is_authenticated
                        
                        	Is authenticated
                        	**type**\:  bool
                        
                        .. attribute:: is_sso_authenticated
                        
                        	Is SSO authenticated
                        	**type**\:  bool
                        
                        .. attribute:: of_peer_auth
                        
                        	Of Peer authentication type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: of_peer_name
                        
                        	Peer's authenticated name
                        	**type**\:  str
                        
                        .. attribute:: of_peer_sso_state
                        
                        	Of Peer auth SSO FSM State
                        	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                        
                        .. attribute:: of_us_auth
                        
                        	Of Us authentication type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: of_us_name
                        
                        	Local authenticated name
                        	**type**\:  str
                        
                        .. attribute:: of_us_sso_state
                        
                        	Of Us auth SSO FSM State
                        	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_authenticated = None
                            self.is_sso_authenticated = None
                            self.of_peer_auth = None
                            self.of_peer_name = None
                            self.of_peer_sso_state = None
                            self.of_us_auth = None
                            self.of_us_name = None
                            self.of_us_sso_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:auth-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_authenticated is not None:
                                return True

                            if self.is_sso_authenticated is not None:
                                return True

                            if self.of_peer_auth is not None:
                                return True

                            if self.of_peer_name is not None:
                                return True

                            if self.of_peer_sso_state is not None:
                                return True

                            if self.of_us_auth is not None:
                                return True

                            if self.of_us_name is not None:
                                return True

                            if self.of_us_sso_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo']['meta_info']


                    class NcpInfoArray(object):
                        """
                        Array of per\-NCP data
                        
                        .. attribute:: is_passive
                        
                        	Is Passive
                        	**type**\:  bool
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP state identifier
                        	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdentEnum>`
                        
                        .. attribute:: ncp_info
                        
                        	Specific NCP info
                        	**type**\:   :py:class:`NcpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo>`
                        
                        .. attribute:: ncp_state
                        
                        	NCP state value
                        	**type**\:   :py:class:`PppFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppFsmStateEnum>`
                        
                        .. attribute:: ncpsso_state
                        
                        	NCP SSO State
                        	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_passive = None
                            self.ncp_identifier = None
                            self.ncp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo()
                            self.ncp_info.parent = self
                            self.ncp_state = None
                            self.ncpsso_state = None


                        class NcpInfo(object):
                            """
                            Specific NCP info
                            
                            .. attribute:: ipcp_info
                            
                            	Info for IPCP
                            	**type**\:   :py:class:`IpcpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo>`
                            
                            .. attribute:: ipcpiw_info
                            
                            	Info for IPCPIW
                            	**type**\:   :py:class:`IpcpiwInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo>`
                            
                            .. attribute:: ipv6cp_info
                            
                            	Info for IPv6CP
                            	**type**\:   :py:class:`Ipv6CpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo>`
                            
                            .. attribute:: type
                            
                            	Type
                            	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdentEnum>`
                            
                            

                            """

                            _prefix = 'ppp-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipcp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo()
                                self.ipcp_info.parent = self
                                self.ipcpiw_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo()
                                self.ipcpiw_info.parent = self
                                self.ipv6cp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo()
                                self.ipv6cp_info.parent = self
                                self.type = None


                            class IpcpInfo(object):
                                """
                                Info for IPCP
                                
                                .. attribute:: dns_primary
                                
                                	Peer DNS Primary
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: dns_secondary
                                
                                	Peer DNS Secondary
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: is_iphc_configured
                                
                                	Is IPHC Configured
                                	**type**\:  bool
                                
                                .. attribute:: local_address
                                
                                	Local IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: local_iphc_options
                                
                                	Local IPHC options
                                	**type**\:   :py:class:`LocalIphcOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions>`
                                
                                .. attribute:: peer_address
                                
                                	Peer IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: peer_iphc_options
                                
                                	Peer IPHC options
                                	**type**\:   :py:class:`PeerIphcOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions>`
                                
                                .. attribute:: peer_netmask
                                
                                	Peer IPv4 netmask
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: wins_primary
                                
                                	Peer WINS Primary
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: wins_secondary
                                
                                	Peer WINS Secondary
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dns_primary = None
                                    self.dns_secondary = None
                                    self.is_iphc_configured = None
                                    self.local_address = None
                                    self.local_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions()
                                    self.local_iphc_options.parent = self
                                    self.peer_address = None
                                    self.peer_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions()
                                    self.peer_iphc_options.parent = self
                                    self.peer_netmask = None
                                    self.wins_primary = None
                                    self.wins_secondary = None


                                class LocalIphcOptions(object):
                                    """
                                    Local IPHC options
                                    
                                    .. attribute:: compression_type
                                    
                                    	Compression type
                                    	**type**\:   :py:class:`PppIphcCompressionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppIphcCompressionEnum>`
                                    
                                    .. attribute:: ec_rtp_compression
                                    
                                    	EcRTP compression
                                    	**type**\:  bool
                                    
                                    .. attribute:: max_header
                                    
                                    	Max header
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: max_period
                                    
                                    	Max period
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: max_time
                                    
                                    	Max time
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: non_tcp_space
                                    
                                    	Non\-TCP space
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: rtp_compression
                                    
                                    	RTP compression
                                    	**type**\:  bool
                                    
                                    .. attribute:: tcp_space
                                    
                                    	TCP space
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ppp-ma-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.compression_type = None
                                        self.ec_rtp_compression = None
                                        self.max_header = None
                                        self.max_period = None
                                        self.max_time = None
                                        self.non_tcp_space = None
                                        self.rtp_compression = None
                                        self.tcp_space = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:local-iphc-options'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.compression_type is not None:
                                            return True

                                        if self.ec_rtp_compression is not None:
                                            return True

                                        if self.max_header is not None:
                                            return True

                                        if self.max_period is not None:
                                            return True

                                        if self.max_time is not None:
                                            return True

                                        if self.non_tcp_space is not None:
                                            return True

                                        if self.rtp_compression is not None:
                                            return True

                                        if self.tcp_space is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                        return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions']['meta_info']


                                class PeerIphcOptions(object):
                                    """
                                    Peer IPHC options
                                    
                                    .. attribute:: compression_type
                                    
                                    	Compression type
                                    	**type**\:   :py:class:`PppIphcCompressionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppIphcCompressionEnum>`
                                    
                                    .. attribute:: ec_rtp_compression
                                    
                                    	EcRTP compression
                                    	**type**\:  bool
                                    
                                    .. attribute:: max_header
                                    
                                    	Max header
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: max_period
                                    
                                    	Max period
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: max_time
                                    
                                    	Max time
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: non_tcp_space
                                    
                                    	Non\-TCP space
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: rtp_compression
                                    
                                    	RTP compression
                                    	**type**\:  bool
                                    
                                    .. attribute:: tcp_space
                                    
                                    	TCP space
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ppp-ma-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.compression_type = None
                                        self.ec_rtp_compression = None
                                        self.max_header = None
                                        self.max_period = None
                                        self.max_time = None
                                        self.non_tcp_space = None
                                        self.rtp_compression = None
                                        self.tcp_space = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:peer-iphc-options'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.compression_type is not None:
                                            return True

                                        if self.ec_rtp_compression is not None:
                                            return True

                                        if self.max_header is not None:
                                            return True

                                        if self.max_period is not None:
                                            return True

                                        if self.max_time is not None:
                                            return True

                                        if self.non_tcp_space is not None:
                                            return True

                                        if self.rtp_compression is not None:
                                            return True

                                        if self.tcp_space is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                        return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipcp-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dns_primary is not None:
                                        return True

                                    if self.dns_secondary is not None:
                                        return True

                                    if self.is_iphc_configured is not None:
                                        return True

                                    if self.local_address is not None:
                                        return True

                                    if self.local_iphc_options is not None and self.local_iphc_options._has_data():
                                        return True

                                    if self.peer_address is not None:
                                        return True

                                    if self.peer_iphc_options is not None and self.peer_iphc_options._has_data():
                                        return True

                                    if self.peer_netmask is not None:
                                        return True

                                    if self.wins_primary is not None:
                                        return True

                                    if self.wins_secondary is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo']['meta_info']


                            class IpcpiwInfo(object):
                                """
                                Info for IPCPIW
                                
                                .. attribute:: local_address
                                
                                	Local IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: peer_address
                                
                                	Peer IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.local_address = None
                                    self.peer_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipcpiw-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.local_address is not None:
                                        return True

                                    if self.peer_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo']['meta_info']


                            class Ipv6CpInfo(object):
                                """
                                Info for IPv6CP
                                
                                .. attribute:: local_address
                                
                                	Local IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: peer_address
                                
                                	Peer IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.local_address = None
                                    self.peer_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipv6cp-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.local_address is not None:
                                        return True

                                    if self.peer_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ncp-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipcp_info is not None and self.ipcp_info._has_data():
                                    return True

                                if self.ipcpiw_info is not None and self.ipcpiw_info._has_data():
                                    return True

                                if self.ipv6cp_info is not None and self.ipv6cp_info._has_data():
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ncp-info-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_passive is not None:
                                return True

                            if self.ncp_identifier is not None:
                                return True

                            if self.ncp_info is not None and self.ncp_info._has_data():
                                return True

                            if self.ncp_state is not None:
                                return True

                            if self.ncpsso_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:node-interface[Cisco-IOS-XR-ppp-ma-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.auth_info is not None and self.auth_info._has_data():
                            return True

                        if self.configured_timeout is not None and self.configured_timeout._has_data():
                            return True

                        if self.ip_interworking_enabled is not None:
                            return True

                        if self.is_l2ac is not None:
                            return True

                        if self.is_lcp_delayed is not None:
                            return True

                        if self.is_loopback_detected is not None:
                            return True

                        if self.is_mcmp_enabled is not None:
                            return True

                        if self.is_ssrp_configured is not None:
                            return True

                        if self.is_tunneled_session is not None:
                            return True

                        if self.keepalive_period is not None:
                            return True

                        if self.keepalive_retry_count is not None:
                            return True

                        if self.lcp_state is not None:
                            return True

                        if self.lcpsso_state is not None:
                            return True

                        if self.line_state is not None:
                            return True

                        if self.local_ed is not None:
                            return True

                        if self.local_mcmp_classes is not None:
                            return True

                        if self.local_mrru is not None:
                            return True

                        if self.local_mru is not None:
                            return True

                        if self.mp_info is not None and self.mp_info._has_data():
                            return True

                        if self.ncp_info_array is not None:
                            for child_ref in self.ncp_info_array:
                                if child_ref._has_data():
                                    return True

                        if self.parent_state is not None:
                            return True

                        if self.peer_ed is not None:
                            return True

                        if self.peer_mcmp_classes is not None:
                            return True

                        if self.peer_mrru is not None:
                            return True

                        if self.peer_mru is not None:
                            return True

                        if self.provisioned is not None:
                            return True

                        if self.session_expires is not None:
                            return True

                        if self.srg_role is not None:
                            return True

                        if self.ssrp_peer_id is not None:
                            return True

                        if self.xconnect_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:node-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_interface is not None:
                        for child_ref in self.node_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.NodeInterfaces']['meta_info']


            class SsoAlerts(object):
                """
                PPP SSO Alert data for a particular node
                
                .. attribute:: sso_alert
                
                	PPP SSO Alert data for a particular interface
                	**type**\: list of    :py:class:`SsoAlert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sso_alert = YList()
                    self.sso_alert.parent = self
                    self.sso_alert.name = 'sso_alert'


                class SsoAlert(object):
                    """
                    PPP SSO Alert data for a particular interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface with SSO Alert
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: ipcp_error
                    
                    	IPCP SSO Error
                    	**type**\:   :py:class:`IpcpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError>`
                    
                    .. attribute:: lcp_error
                    
                    	LCP SSO Error
                    	**type**\:   :py:class:`LcpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError>`
                    
                    .. attribute:: of_peer_auth_error
                    
                    	Of\-peer Authentication SSO Error
                    	**type**\:   :py:class:`OfPeerAuthError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError>`
                    
                    .. attribute:: of_us_auth_error
                    
                    	Of\-us Authentication SSO Error
                    	**type**\:   :py:class:`OfUsAuthError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError>`
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.ipcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError()
                        self.ipcp_error.parent = self
                        self.lcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError()
                        self.lcp_error.parent = self
                        self.of_peer_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError()
                        self.of_peer_auth_error.parent = self
                        self.of_us_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError()
                        self.of_us_auth_error.parent = self


                    class LcpError(object):
                        """
                        LCP SSO Error
                        
                        .. attribute:: context
                        
                        	Context
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: error
                        
                        	SSO Error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_error
                        
                        	Is SSO Error
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = None
                            self.error = None
                            self.is_error = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.context is not None:
                                return True

                            if self.error is not None:
                                return True

                            if self.is_error is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError']['meta_info']


                    class OfUsAuthError(object):
                        """
                        Of\-us Authentication SSO Error
                        
                        .. attribute:: context
                        
                        	Context
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: error
                        
                        	SSO Error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_error
                        
                        	Is SSO Error
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = None
                            self.error = None
                            self.is_error = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-us-auth-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.context is not None:
                                return True

                            if self.error is not None:
                                return True

                            if self.is_error is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError']['meta_info']


                    class OfPeerAuthError(object):
                        """
                        Of\-peer Authentication SSO Error
                        
                        .. attribute:: context
                        
                        	Context
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: error
                        
                        	SSO Error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_error
                        
                        	Is SSO Error
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = None
                            self.error = None
                            self.is_error = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-peer-auth-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.context is not None:
                                return True

                            if self.error is not None:
                                return True

                            if self.is_error is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError']['meta_info']


                    class IpcpError(object):
                        """
                        IPCP SSO Error
                        
                        .. attribute:: context
                        
                        	Context
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: error
                        
                        	SSO Error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_error
                        
                        	Is SSO Error
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = None
                            self.error = None
                            self.is_error = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipcp-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.context is not None:
                                return True

                            if self.error is not None:
                                return True

                            if self.is_error is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-alert[Cisco-IOS-XR-ppp-ma-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.ipcp_error is not None and self.ipcp_error._has_data():
                            return True

                        if self.lcp_error is not None and self.lcp_error._has_data():
                            return True

                        if self.of_peer_auth_error is not None and self.of_peer_auth_error._has_data():
                            return True

                        if self.of_us_auth_error is not None and self.of_us_auth_error._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoAlerts.SsoAlert']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-alerts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.sso_alert is not None:
                        for child_ref in self.sso_alert:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.SsoAlerts']['meta_info']


            class NodeInterfaceStatistics(object):
                """
                Per interface PPP operational statistics
                
                .. attribute:: node_interface_statistic
                
                	LCP and NCP statistics for an interface running PPP
                	**type**\: list of    :py:class:`NodeInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_interface_statistic = YList()
                    self.node_interface_statistic.parent = self
                    self.node_interface_statistic.name = 'node_interface_statistic'


                class NodeInterfaceStatistic(object):
                    """
                    LCP and NCP statistics for an interface
                    running PPP
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface running PPP
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: authentication_statistics
                    
                    	PPP Authentication statistics
                    	**type**\:   :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics>`
                    
                    .. attribute:: lcp_statistics
                    
                    	PPP LCP Statistics
                    	**type**\:   :py:class:`LcpStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics>`
                    
                    .. attribute:: ncp_statistics_array
                    
                    	Array of PPP NCP Statistics
                    	**type**\: list of    :py:class:`NcpStatisticsArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray>`
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.authentication_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics()
                        self.authentication_statistics.parent = self
                        self.lcp_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics()
                        self.lcp_statistics.parent = self
                        self.ncp_statistics_array = YList()
                        self.ncp_statistics_array.parent = self
                        self.ncp_statistics_array.name = 'ncp_statistics_array'


                    class LcpStatistics(object):
                        """
                        PPP LCP Statistics
                        
                        .. attribute:: conf_ack_rcvd
                        
                        	Conf Ack Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_ack_sent
                        
                        	Conf Ack Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_nak_rcvd
                        
                        	Conf Nak Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_nak_sent
                        
                        	Conf Nak Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_rej_rcvd
                        
                        	Conf Rej Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_rej_sent
                        
                        	Conf Rej Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_req_rcvd
                        
                        	Conf Req Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_req_sent
                        
                        	Conf Req Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: disc_req_rcvd
                        
                        	Disc Req Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: disc_req_sent
                        
                        	Disc Req Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: echo_rep_rcvd
                        
                        	Echo Rep Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: echo_rep_sent
                        
                        	Echo Rep Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: echo_req_rcvd
                        
                        	Echo Req Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: echo_req_sent
                        
                        	Echo Req Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: link_error
                        
                        	Keepalive link failure count
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: link_up
                        
                        	Line Protocol Up count
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.conf_ack_rcvd = None
                            self.conf_ack_sent = None
                            self.conf_nak_rcvd = None
                            self.conf_nak_sent = None
                            self.conf_rej_rcvd = None
                            self.conf_rej_sent = None
                            self.conf_req_rcvd = None
                            self.conf_req_sent = None
                            self.disc_req_rcvd = None
                            self.disc_req_sent = None
                            self.echo_rep_rcvd = None
                            self.echo_rep_sent = None
                            self.echo_req_rcvd = None
                            self.echo_req_sent = None
                            self.link_error = None
                            self.link_up = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.conf_ack_rcvd is not None:
                                return True

                            if self.conf_ack_sent is not None:
                                return True

                            if self.conf_nak_rcvd is not None:
                                return True

                            if self.conf_nak_sent is not None:
                                return True

                            if self.conf_rej_rcvd is not None:
                                return True

                            if self.conf_rej_sent is not None:
                                return True

                            if self.conf_req_rcvd is not None:
                                return True

                            if self.conf_req_sent is not None:
                                return True

                            if self.disc_req_rcvd is not None:
                                return True

                            if self.disc_req_sent is not None:
                                return True

                            if self.echo_rep_rcvd is not None:
                                return True

                            if self.echo_rep_sent is not None:
                                return True

                            if self.echo_req_rcvd is not None:
                                return True

                            if self.echo_req_sent is not None:
                                return True

                            if self.link_error is not None:
                                return True

                            if self.link_up is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics']['meta_info']


                    class AuthenticationStatistics(object):
                        """
                        PPP Authentication statistics
                        
                        .. attribute:: auth_timeout_count
                        
                        	Authentication timeout count
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_chall_rcvd
                        
                        	CHAP challenge packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_chall_sent
                        
                        	CHAP challenge packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_rep_fail_rcvd
                        
                        	CHAP reply failure packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_rep_fail_sent
                        
                        	CHAP reply failure packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_rep_succ_rcvd
                        
                        	CHAP reply success packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_rep_succ_sent
                        
                        	CHAP reply success packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_resp_rcvd
                        
                        	CHAP response packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: chap_resp_sent
                        
                        	CHAP response packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_ack_rcvd
                        
                        	PAP Ack packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_ack_sent
                        
                        	PAP Ack packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_nak_rcvd
                        
                        	PAP Nak packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_nak_sent
                        
                        	PAP Nak packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_req_rcvd
                        
                        	PAP Request packets received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: pap_req_sent
                        
                        	PAP Request packets sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.auth_timeout_count = None
                            self.chap_chall_rcvd = None
                            self.chap_chall_sent = None
                            self.chap_rep_fail_rcvd = None
                            self.chap_rep_fail_sent = None
                            self.chap_rep_succ_rcvd = None
                            self.chap_rep_succ_sent = None
                            self.chap_resp_rcvd = None
                            self.chap_resp_sent = None
                            self.pap_ack_rcvd = None
                            self.pap_ack_sent = None
                            self.pap_nak_rcvd = None
                            self.pap_nak_sent = None
                            self.pap_req_rcvd = None
                            self.pap_req_sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:authentication-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.auth_timeout_count is not None:
                                return True

                            if self.chap_chall_rcvd is not None:
                                return True

                            if self.chap_chall_sent is not None:
                                return True

                            if self.chap_rep_fail_rcvd is not None:
                                return True

                            if self.chap_rep_fail_sent is not None:
                                return True

                            if self.chap_rep_succ_rcvd is not None:
                                return True

                            if self.chap_rep_succ_sent is not None:
                                return True

                            if self.chap_resp_rcvd is not None:
                                return True

                            if self.chap_resp_sent is not None:
                                return True

                            if self.pap_ack_rcvd is not None:
                                return True

                            if self.pap_ack_sent is not None:
                                return True

                            if self.pap_nak_rcvd is not None:
                                return True

                            if self.pap_nak_sent is not None:
                                return True

                            if self.pap_req_rcvd is not None:
                                return True

                            if self.pap_req_sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics']['meta_info']


                    class NcpStatisticsArray(object):
                        """
                        Array of PPP NCP Statistics
                        
                        .. attribute:: conf_ack_rcvd
                        
                        	Conf Ack Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_ack_sent
                        
                        	Conf Ack Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_nak_rcvd
                        
                        	Conf Nak Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_nak_sent
                        
                        	Conf Nak Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_rej_rcvd
                        
                        	Conf Rej Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_rej_sent
                        
                        	Conf Rej Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_req_rcvd
                        
                        	Conf Req Packets Received
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: conf_req_sent
                        
                        	Conf Req Packets Sent
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP identifier
                        	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdentEnum>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.conf_ack_rcvd = None
                            self.conf_ack_sent = None
                            self.conf_nak_rcvd = None
                            self.conf_nak_sent = None
                            self.conf_rej_rcvd = None
                            self.conf_rej_sent = None
                            self.conf_req_rcvd = None
                            self.conf_req_sent = None
                            self.ncp_identifier = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ncp-statistics-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.conf_ack_rcvd is not None:
                                return True

                            if self.conf_ack_sent is not None:
                                return True

                            if self.conf_nak_rcvd is not None:
                                return True

                            if self.conf_nak_sent is not None:
                                return True

                            if self.conf_rej_rcvd is not None:
                                return True

                            if self.conf_rej_sent is not None:
                                return True

                            if self.conf_req_rcvd is not None:
                                return True

                            if self.conf_req_sent is not None:
                                return True

                            if self.ncp_identifier is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:node-interface-statistic[Cisco-IOS-XR-ppp-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.authentication_statistics is not None and self.authentication_statistics._has_data():
                            return True

                        if self.lcp_statistics is not None and self.lcp_statistics._has_data():
                            return True

                        if self.ncp_statistics_array is not None:
                            for child_ref in self.ncp_statistics_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:node-interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_interface_statistic is not None:
                        for child_ref in self.node_interface_statistic:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.NodeInterfaceStatistics']['meta_info']


            class SsoSummary(object):
                """
                Summarized PPP SSO data for a particular node
                
                .. attribute:: ipcp_states
                
                	IPCP SSO FSM States
                	**type**\:   :py:class:`IpcpStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoSummary.IpcpStates>`
                
                .. attribute:: lcp_states
                
                	LCP SSO FSM States
                	**type**\:   :py:class:`LcpStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoSummary.LcpStates>`
                
                .. attribute:: of_peer_auth_states
                
                	Of\-peer Authentication SSO FSM States
                	**type**\:   :py:class:`OfPeerAuthStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates>`
                
                .. attribute:: of_us_auth_states
                
                	Of\-us Authentication SSO FSM States
                	**type**\:   :py:class:`OfUsAuthStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoSummary.OfUsAuthStates>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipcp_states = Ppp.Nodes.Node.SsoSummary.IpcpStates()
                    self.ipcp_states.parent = self
                    self.lcp_states = Ppp.Nodes.Node.SsoSummary.LcpStates()
                    self.lcp_states.parent = self
                    self.of_peer_auth_states = Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates()
                    self.of_peer_auth_states.parent = self
                    self.of_us_auth_states = Ppp.Nodes.Node.SsoSummary.OfUsAuthStates()
                    self.of_us_auth_states.parent = self


                class LcpStates(object):
                    """
                    LCP SSO FSM States
                    
                    .. attribute:: count
                    
                    	Number of SSO FSMs in each State
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: total
                    
                    	Total number of SSO FSMs running
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.count = YLeafList()
                        self.count.parent = self
                        self.count.name = 'count'
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            for child in self.count:
                                if child is not None:
                                    return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoSummary.LcpStates']['meta_info']


                class OfUsAuthStates(object):
                    """
                    Of\-us Authentication SSO FSM States
                    
                    .. attribute:: count
                    
                    	Number of SSO FSMs in each State
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: total
                    
                    	Total number of SSO FSMs running
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.count = YLeafList()
                        self.count.parent = self
                        self.count.name = 'count'
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-us-auth-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            for child in self.count:
                                if child is not None:
                                    return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoSummary.OfUsAuthStates']['meta_info']


                class OfPeerAuthStates(object):
                    """
                    Of\-peer Authentication SSO FSM States
                    
                    .. attribute:: count
                    
                    	Number of SSO FSMs in each State
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: total
                    
                    	Total number of SSO FSMs running
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.count = YLeafList()
                        self.count.parent = self
                        self.count.name = 'count'
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-peer-auth-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            for child in self.count:
                                if child is not None:
                                    return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates']['meta_info']


                class IpcpStates(object):
                    """
                    IPCP SSO FSM States
                    
                    .. attribute:: count
                    
                    	Number of SSO FSMs in each State
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: total
                    
                    	Total number of SSO FSMs running
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.count = YLeafList()
                        self.count.parent = self
                        self.count.name = 'count'
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipcp-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            for child in self.count:
                                if child is not None:
                                    return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoSummary.IpcpStates']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ipcp_states is not None and self.ipcp_states._has_data():
                        return True

                    if self.lcp_states is not None and self.lcp_states._has_data():
                        return True

                    if self.of_peer_auth_states is not None and self.of_peer_auth_states._has_data():
                        return True

                    if self.of_us_auth_states is not None and self.of_us_auth_states._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.SsoSummary']['meta_info']


            class SsoGroups(object):
                """
                PPP SSO Group data for a particular node
                
                .. attribute:: sso_group
                
                	PPP SSO state data for a particular group
                	**type**\: list of    :py:class:`SsoGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sso_group = YList()
                    self.sso_group.parent = self
                    self.sso_group.name = 'sso_group'


                class SsoGroup(object):
                    """
                    PPP SSO state data for a particular group
                    
                    .. attribute:: group_id  <key>
                    
                    	The identifier for the group
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: sso_states
                    
                    	PPP SSO State data for a particular group
                    	**type**\:   :py:class:`SsoStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates>`
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.sso_states = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates()
                        self.sso_states.parent = self


                    class SsoStates(object):
                        """
                        PPP SSO State data for a particular group
                        
                        .. attribute:: sso_state
                        
                        	PPP SSO State data for a particular interface
                        	**type**\: list of    :py:class:`SsoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sso_state = YList()
                            self.sso_state.parent = self
                            self.sso_state.name = 'sso_state'


                        class SsoState(object):
                            """
                            PPP SSO State data for a particular
                            interface
                            
                            .. attribute:: session_id  <key>
                            
                            	Session ID for the interface with SSO State
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: ipcp_state
                            
                            	IPCP SSO State
                            	**type**\:   :py:class:`IpcpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState>`
                            
                            .. attribute:: lcp_state
                            
                            	LCP SSO State
                            	**type**\:   :py:class:`LcpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState>`
                            
                            .. attribute:: of_peer_auth_state
                            
                            	Of\-peer Authentication SSO State
                            	**type**\:   :py:class:`OfPeerAuthState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState>`
                            
                            .. attribute:: of_us_auth_state
                            
                            	Of\-us Authentication SSO State
                            	**type**\:   :py:class:`OfUsAuthState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState>`
                            
                            .. attribute:: session_id_xr
                            
                            	SSRP Session ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ppp-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.session_id = None
                                self.interface = None
                                self.ipcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState()
                                self.ipcp_state.parent = self
                                self.lcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState()
                                self.lcp_state.parent = self
                                self.of_peer_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState()
                                self.of_peer_auth_state.parent = self
                                self.of_us_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState()
                                self.of_us_auth_state.parent = self
                                self.session_id_xr = None


                            class LcpState(object):
                                """
                                LCP SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.is_running = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_running is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState']['meta_info']


                            class OfUsAuthState(object):
                                """
                                Of\-us Authentication SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.is_running = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-us-auth-state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_running is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState']['meta_info']


                            class OfPeerAuthState(object):
                                """
                                Of\-peer Authentication SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.is_running = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:of-peer-auth-state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_running is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState']['meta_info']


                            class IpcpState(object):
                                """
                                IPCP SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmStateEnum>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.is_running = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ipcp-state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_running is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                    return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.session_id is None:
                                    raise YPYModelError('Key property session_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-state[Cisco-IOS-XR-ppp-ma-oper:session-id = ' + str(self.session_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.session_id is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.ipcp_state is not None and self.ipcp_state._has_data():
                                    return True

                                if self.lcp_state is not None and self.lcp_state._has_data():
                                    return True

                                if self.of_peer_auth_state is not None and self.of_peer_auth_state._has_data():
                                    return True

                                if self.of_us_auth_state is not None and self.of_us_auth_state._has_data():
                                    return True

                                if self.session_id_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                                return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-states'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sso_state is not None:
                                for child_ref in self.sso_state:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-group[Cisco-IOS-XR-ppp-ma-oper:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.sso_states is not None and self.sso_states._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.SsoGroups.SsoGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:sso-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.sso_group is not None:
                        for child_ref in self.sso_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.SsoGroups']['meta_info']


            class Summary(object):
                """
                Summarized PPP data for a particular node
                
                .. attribute:: fsm_states
                
                	FSM States
                	**type**\:   :py:class:`FsmStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary.FsmStates>`
                
                .. attribute:: intfs
                
                	Interfaces running PPP
                	**type**\:   :py:class:`Intfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary.Intfs>`
                
                .. attribute:: lcp_auth_phases
                
                	LCP/Auth Phases
                	**type**\:   :py:class:`LcpAuthPhases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary.LcpAuthPhases>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.fsm_states = Ppp.Nodes.Node.Summary.FsmStates()
                    self.fsm_states.parent = self
                    self.intfs = Ppp.Nodes.Node.Summary.Intfs()
                    self.intfs.parent = self
                    self.lcp_auth_phases = Ppp.Nodes.Node.Summary.LcpAuthPhases()
                    self.lcp_auth_phases.parent = self


                class Intfs(object):
                    """
                    Interfaces running PPP
                    
                    .. attribute:: gcc0_count
                    
                    	GCC0 Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gcc1_count
                    
                    	GCC1 Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multilink_bundle_count
                    
                    	Multilink Bundle Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pos_count
                    
                    	POS Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe_count
                    
                    	PPPoE Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: serial_count
                    
                    	Serial Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.gcc0_count = None
                        self.gcc1_count = None
                        self.multilink_bundle_count = None
                        self.pos_count = None
                        self.pppoe_count = None
                        self.serial_count = None
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:intfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.gcc0_count is not None:
                            return True

                        if self.gcc1_count is not None:
                            return True

                        if self.multilink_bundle_count is not None:
                            return True

                        if self.pos_count is not None:
                            return True

                        if self.pppoe_count is not None:
                            return True

                        if self.serial_count is not None:
                            return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Summary.Intfs']['meta_info']


                class FsmStates(object):
                    """
                    FSM States
                    
                    .. attribute:: lcpfsm_states
                    
                    	Array of per\-LCP FSM States
                    	**type**\:   :py:class:`LcpfsmStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates>`
                    
                    .. attribute:: ncpfsm_states_array
                    
                    	Array of per\-NCP FSM States
                    	**type**\: list of    :py:class:`NcpfsmStatesArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray>`
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lcpfsm_states = Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates()
                        self.lcpfsm_states.parent = self
                        self.ncpfsm_states_array = YList()
                        self.ncpfsm_states_array.parent = self
                        self.ncpfsm_states_array.name = 'ncpfsm_states_array'


                    class LcpfsmStates(object):
                        """
                        Array of per\-LCP FSM States
                        
                        .. attribute:: count
                        
                        	Number of FSMs in each State
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total
                        
                        	Total number of LCP FSMs running
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.count = YLeafList()
                            self.count.parent = self
                            self.count.name = 'count'
                            self.total = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcpfsm-states'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.count is not None:
                                for child in self.count:
                                    if child is not None:
                                        return True

                            if self.total is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates']['meta_info']


                    class NcpfsmStatesArray(object):
                        """
                        Array of per\-NCP FSM States
                        
                        .. attribute:: count
                        
                        	Number of FSMs in each State
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP Identifier
                        	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdentEnum>`
                        
                        .. attribute:: total
                        
                        	Total number of FSMs running for this NCP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.count = YLeafList()
                            self.count.parent = self
                            self.count.name = 'count'
                            self.ncp_identifier = None
                            self.total = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:ncpfsm-states-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.count is not None:
                                for child in self.count:
                                    if child is not None:
                                        return True

                            if self.ncp_identifier is not None:
                                return True

                            if self.total is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                            return meta._meta_table['Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:fsm-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.lcpfsm_states is not None and self.lcpfsm_states._has_data():
                            return True

                        if self.ncpfsm_states_array is not None:
                            for child_ref in self.ncpfsm_states_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Summary.FsmStates']['meta_info']


                class LcpAuthPhases(object):
                    """
                    LCP/Auth Phases
                    
                    .. attribute:: authenticating
                    
                    	Number of sessions authenticating
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lcp_not_negotiated
                    
                    	Number of sessions with LCP not negotiated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: line_held_down
                    
                    	Number of sessions negotiated but with the line held down
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_l2_fwded
                    
                    	Number of L2 forwarded sessions brought up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_local_term
                    
                    	Number of locally terminated sessions brought up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_tunneled
                    
                    	Number of VPDN tunneled sessions brought up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ppp-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.authenticating = None
                        self.lcp_not_negotiated = None
                        self.line_held_down = None
                        self.up_l2_fwded = None
                        self.up_local_term = None
                        self.up_tunneled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:lcp-auth-phases'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.authenticating is not None:
                            return True

                        if self.lcp_not_negotiated is not None:
                            return True

                        if self.line_held_down is not None:
                            return True

                        if self.up_l2_fwded is not None:
                            return True

                        if self.up_local_term is not None:
                            return True

                        if self.up_tunneled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                        return meta._meta_table['Ppp.Nodes.Node.Summary.LcpAuthPhases']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fsm_states is not None and self.fsm_states._has_data():
                        return True

                    if self.intfs is not None and self.intfs._has_data():
                        return True

                    if self.lcp_auth_phases is not None and self.lcp_auth_phases._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                    return meta._meta_table['Ppp.Nodes.Node.Summary']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ppp-ma-oper:ppp/Cisco-IOS-XR-ppp-ma-oper:nodes/Cisco-IOS-XR-ppp-ma-oper:node[Cisco-IOS-XR-ppp-ma-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.node_interface_statistics is not None and self.node_interface_statistics._has_data():
                    return True

                if self.node_interfaces is not None and self.node_interfaces._has_data():
                    return True

                if self.sso_alerts is not None and self.sso_alerts._has_data():
                    return True

                if self.sso_groups is not None and self.sso_groups._has_data():
                    return True

                if self.sso_summary is not None and self.sso_summary._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
                return meta._meta_table['Ppp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ppp-ma-oper:ppp/Cisco-IOS-XR-ppp-ma-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
            return meta._meta_table['Ppp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ppp-ma-oper:ppp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_oper as meta
        return meta._meta_table['Ppp']['meta_info']


