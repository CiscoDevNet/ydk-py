""" Cisco_IOS_XR_ppp_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma package operational data.

This module contains definitions
for the following management objects\:
  ppp\: PPP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NcpIdent(Enum):
    """
    NcpIdent

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

    cdpcp = Enum.YLeaf(1, "cdpcp")

    ipcp = Enum.YLeaf(2, "ipcp")

    ipcpiw = Enum.YLeaf(3, "ipcpiw")

    ipv6cp = Enum.YLeaf(4, "ipv6cp")

    mplscp = Enum.YLeaf(5, "mplscp")

    osicp = Enum.YLeaf(6, "osicp")


class PppFsmState(Enum):
    """
    PppFsmState

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

    ppp_fsm_state_initial_0 = Enum.YLeaf(0, "ppp-fsm-state-initial-0")

    ppp_fsm_state_starting_1 = Enum.YLeaf(1, "ppp-fsm-state-starting-1")

    ppp_fsm_state_closed_2 = Enum.YLeaf(2, "ppp-fsm-state-closed-2")

    ppp_fsm_state_stopped_3 = Enum.YLeaf(3, "ppp-fsm-state-stopped-3")

    ppp_fsm_state_closing_4 = Enum.YLeaf(4, "ppp-fsm-state-closing-4")

    ppp_fsm_state_stopping_5 = Enum.YLeaf(5, "ppp-fsm-state-stopping-5")

    ppp_fsm_state_req_sent_6 = Enum.YLeaf(6, "ppp-fsm-state-req-sent-6")

    ppp_fsm_state_ack_rcvd_7 = Enum.YLeaf(7, "ppp-fsm-state-ack-rcvd-7")

    ppp_fsm_state_ack_sent_8 = Enum.YLeaf(8, "ppp-fsm-state-ack-sent-8")

    ppp_fsm_state_opened_9 = Enum.YLeaf(9, "ppp-fsm-state-opened-9")


class PppIphcCompression(Enum):
    """
    PppIphcCompression

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

    ppp_iphc_compression_fmt_none = Enum.YLeaf(0, "ppp-iphc-compression-fmt-none")

    ppp_iphc_compression_fmt_vj = Enum.YLeaf(1, "ppp-iphc-compression-fmt-vj")

    ppp_iphc_compression_fmt_ietf = Enum.YLeaf(2, "ppp-iphc-compression-fmt-ietf")

    ppp_iphc_compression_fmt_iphc = Enum.YLeaf(3, "ppp-iphc-compression-fmt-iphc")

    ppp_iphc_compression_fmt_cisco = Enum.YLeaf(4, "ppp-iphc-compression-fmt-cisco")


class PppLcpMpMbrState(Enum):
    """
    PppLcpMpMbrState

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

    ppp_lcp_mp_mbr_state_detached = Enum.YLeaf(0, "ppp-lcp-mp-mbr-state-detached")

    ppp_lcp_mp_mbr_state_lcp_not_negotiated = Enum.YLeaf(1, "ppp-lcp-mp-mbr-state-lcp-not-negotiated")

    ppp_lcp_mp_mbr_state_link_noise = Enum.YLeaf(2, "ppp-lcp-mp-mbr-state-link-noise")

    ppp_lcp_mp_mbr_state_bundle_shutdown = Enum.YLeaf(3, "ppp-lcp-mp-mbr-state-bundle-shutdown")

    ppp_lcp_mp_mbr_state_mrru_rejected = Enum.YLeaf(4, "ppp-lcp-mp-mbr-state-mrru-rejected")

    ppp_lcp_mp_mbr_state_mrru_mismatch = Enum.YLeaf(5, "ppp-lcp-mp-mbr-state-mrru-mismatch")

    ppp_lcp_mp_mbr_state_ed_mismatch = Enum.YLeaf(6, "ppp-lcp-mp-mbr-state-ed-mismatch")

    ppp_lcp_mp_mbr_state_auth_name_mismatch = Enum.YLeaf(7, "ppp-lcp-mp-mbr-state-auth-name-mismatch")

    ppp_lcp_mp_mbr_state_mcmp_rejected = Enum.YLeaf(8, "ppp-lcp-mp-mbr-state-mcmp-rejected")

    ppp_lcp_mp_mbr_state_mcmp_not_negotiated = Enum.YLeaf(9, "ppp-lcp-mp-mbr-state-mcmp-not-negotiated")

    ppp_lcp_mp_mbr_state_mcmp_local_mismatch = Enum.YLeaf(10, "ppp-lcp-mp-mbr-state-mcmp-local-mismatch")

    ppp_lcp_mp_mbr_state_mcmp_peer_mismatch = Enum.YLeaf(11, "ppp-lcp-mp-mbr-state-mcmp-peer-mismatch")

    ppp_lcp_mp_mbr_state_standby_up = Enum.YLeaf(12, "ppp-lcp-mp-mbr-state-standby-up")

    ppp_lcp_mp_mbr_state_active = Enum.YLeaf(13, "ppp-lcp-mp-mbr-state-active")


class PppSsoFsmState(Enum):
    """
    PppSsoFsmState

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

    ppp_sso_state_not_ready_0 = Enum.YLeaf(0, "ppp-sso-state-not-ready-0")

    ppp_sso_state_standby_unnegd_1 = Enum.YLeaf(1, "ppp-sso-state-standby-unnegd-1")

    ppp_sso_state_active_down_2 = Enum.YLeaf(2, "ppp-sso-state-active-down-2")

    ppp_sso_state_deactivating_3 = Enum.YLeaf(3, "ppp-sso-state-deactivating-3")

    ppp_sso_state_active_unnegd_4 = Enum.YLeaf(4, "ppp-sso-state-active-unnegd-4")

    ppp_sso_state_standby_negd_5 = Enum.YLeaf(5, "ppp-sso-state-standby-negd-5")

    ppp_sso_state_activating_6 = Enum.YLeaf(6, "ppp-sso-state-activating-6")

    ppp_sso_state_active_negd_7 = Enum.YLeaf(7, "ppp-sso-state-active-negd-7")



class Ppp(Entity):
    """
    PPP operational data
    
    .. attribute:: nodes
    
    	Per node PPP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes>`
    
    

    """

    _prefix = 'ppp-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ppp, self).__init__()
        self._top_entity = None

        self.yang_name = "ppp"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ma-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", Ppp.Nodes)}
        self._child_list_classes = {}

        self.nodes = Ppp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-oper:ppp"


    class Nodes(Entity):
        """
        Per node PPP operational data
        
        .. attribute:: node
        
        	The PPP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node>`
        
        

        """

        _prefix = 'ppp-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ppp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ppp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Ppp.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ma-oper:ppp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ppp.Nodes, [], name, value)


        class Node(Entity):
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
                super(Ppp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-interface-statistics" : ("node_interface_statistics", Ppp.Nodes.Node.NodeInterfaceStatistics), "node-interfaces" : ("node_interfaces", Ppp.Nodes.Node.NodeInterfaces), "sso-alerts" : ("sso_alerts", Ppp.Nodes.Node.SsoAlerts), "sso-groups" : ("sso_groups", Ppp.Nodes.Node.SsoGroups), "sso-summary" : ("sso_summary", Ppp.Nodes.Node.SsoSummary), "statistics" : ("statistics", Ppp.Nodes.Node.Statistics), "summary" : ("summary", Ppp.Nodes.Node.Summary)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.node_interface_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics()
                self.node_interface_statistics.parent = self
                self._children_name_map["node_interface_statistics"] = "node-interface-statistics"
                self._children_yang_names.add("node-interface-statistics")

                self.node_interfaces = Ppp.Nodes.Node.NodeInterfaces()
                self.node_interfaces.parent = self
                self._children_name_map["node_interfaces"] = "node-interfaces"
                self._children_yang_names.add("node-interfaces")

                self.sso_alerts = Ppp.Nodes.Node.SsoAlerts()
                self.sso_alerts.parent = self
                self._children_name_map["sso_alerts"] = "sso-alerts"
                self._children_yang_names.add("sso-alerts")

                self.sso_groups = Ppp.Nodes.Node.SsoGroups()
                self.sso_groups.parent = self
                self._children_name_map["sso_groups"] = "sso-groups"
                self._children_yang_names.add("sso-groups")

                self.sso_summary = Ppp.Nodes.Node.SsoSummary()
                self.sso_summary.parent = self
                self._children_name_map["sso_summary"] = "sso-summary"
                self._children_yang_names.add("sso-summary")

                self.statistics = Ppp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.summary = Ppp.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ma-oper:ppp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ppp.Nodes.Node, ['node_name'], name, value)


            class NodeInterfaceStatistics(Entity):
                """
                Per interface PPP operational statistics
                
                .. attribute:: node_interface_statistic
                
                	LCP and NCP statistics for an interface running PPP
                	**type**\: list of    :py:class:`NodeInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ppp.Nodes.Node.NodeInterfaceStatistics, self).__init__()

                    self.yang_name = "node-interface-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-interface-statistic" : ("node_interface_statistic", Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic)}

                    self.node_interface_statistic = YList(self)
                    self._segment_path = lambda: "node-interface-statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ppp.Nodes.Node.NodeInterfaceStatistics, [], name, value)


                class NodeInterfaceStatistic(Entity):
                    """
                    LCP and NCP statistics for an interface
                    running PPP
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface running PPP
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic, self).__init__()

                        self.yang_name = "node-interface-statistic"
                        self.yang_parent_name = "node-interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"authentication-statistics" : ("authentication_statistics", Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics), "lcp-statistics" : ("lcp_statistics", Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics)}
                        self._child_list_classes = {"ncp-statistics-array" : ("ncp_statistics_array", Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.authentication_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics()
                        self.authentication_statistics.parent = self
                        self._children_name_map["authentication_statistics"] = "authentication-statistics"
                        self._children_yang_names.add("authentication-statistics")

                        self.lcp_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics()
                        self.lcp_statistics.parent = self
                        self._children_name_map["lcp_statistics"] = "lcp-statistics"
                        self._children_yang_names.add("lcp-statistics")

                        self.ncp_statistics_array = YList(self)
                        self._segment_path = lambda: "node-interface-statistic" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic, ['interface_name'], name, value)


                    class AuthenticationStatistics(Entity):
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
                            super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics, self).__init__()

                            self.yang_name = "authentication-statistics"
                            self.yang_parent_name = "node-interface-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.auth_timeout_count = YLeaf(YType.uint16, "auth-timeout-count")

                            self.chap_chall_rcvd = YLeaf(YType.uint16, "chap-chall-rcvd")

                            self.chap_chall_sent = YLeaf(YType.uint16, "chap-chall-sent")

                            self.chap_rep_fail_rcvd = YLeaf(YType.uint16, "chap-rep-fail-rcvd")

                            self.chap_rep_fail_sent = YLeaf(YType.uint16, "chap-rep-fail-sent")

                            self.chap_rep_succ_rcvd = YLeaf(YType.uint16, "chap-rep-succ-rcvd")

                            self.chap_rep_succ_sent = YLeaf(YType.uint16, "chap-rep-succ-sent")

                            self.chap_resp_rcvd = YLeaf(YType.uint16, "chap-resp-rcvd")

                            self.chap_resp_sent = YLeaf(YType.uint16, "chap-resp-sent")

                            self.pap_ack_rcvd = YLeaf(YType.uint16, "pap-ack-rcvd")

                            self.pap_ack_sent = YLeaf(YType.uint16, "pap-ack-sent")

                            self.pap_nak_rcvd = YLeaf(YType.uint16, "pap-nak-rcvd")

                            self.pap_nak_sent = YLeaf(YType.uint16, "pap-nak-sent")

                            self.pap_req_rcvd = YLeaf(YType.uint16, "pap-req-rcvd")

                            self.pap_req_sent = YLeaf(YType.uint16, "pap-req-sent")
                            self._segment_path = lambda: "authentication-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics, ['auth_timeout_count', 'chap_chall_rcvd', 'chap_chall_sent', 'chap_rep_fail_rcvd', 'chap_rep_fail_sent', 'chap_rep_succ_rcvd', 'chap_rep_succ_sent', 'chap_resp_rcvd', 'chap_resp_sent', 'pap_ack_rcvd', 'pap_ack_sent', 'pap_nak_rcvd', 'pap_nak_sent', 'pap_req_rcvd', 'pap_req_sent'], name, value)


                    class LcpStatistics(Entity):
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
                            super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics, self).__init__()

                            self.yang_name = "lcp-statistics"
                            self.yang_parent_name = "node-interface-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.conf_ack_rcvd = YLeaf(YType.uint16, "conf-ack-rcvd")

                            self.conf_ack_sent = YLeaf(YType.uint16, "conf-ack-sent")

                            self.conf_nak_rcvd = YLeaf(YType.uint16, "conf-nak-rcvd")

                            self.conf_nak_sent = YLeaf(YType.uint16, "conf-nak-sent")

                            self.conf_rej_rcvd = YLeaf(YType.uint16, "conf-rej-rcvd")

                            self.conf_rej_sent = YLeaf(YType.uint16, "conf-rej-sent")

                            self.conf_req_rcvd = YLeaf(YType.uint16, "conf-req-rcvd")

                            self.conf_req_sent = YLeaf(YType.uint16, "conf-req-sent")

                            self.disc_req_rcvd = YLeaf(YType.uint16, "disc-req-rcvd")

                            self.disc_req_sent = YLeaf(YType.uint16, "disc-req-sent")

                            self.echo_rep_rcvd = YLeaf(YType.uint16, "echo-rep-rcvd")

                            self.echo_rep_sent = YLeaf(YType.uint16, "echo-rep-sent")

                            self.echo_req_rcvd = YLeaf(YType.uint16, "echo-req-rcvd")

                            self.echo_req_sent = YLeaf(YType.uint16, "echo-req-sent")

                            self.link_error = YLeaf(YType.uint16, "link-error")

                            self.link_up = YLeaf(YType.uint16, "link-up")
                            self._segment_path = lambda: "lcp-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics, ['conf_ack_rcvd', 'conf_ack_sent', 'conf_nak_rcvd', 'conf_nak_sent', 'conf_rej_rcvd', 'conf_rej_sent', 'conf_req_rcvd', 'conf_req_sent', 'disc_req_rcvd', 'disc_req_sent', 'echo_rep_rcvd', 'echo_rep_sent', 'echo_req_rcvd', 'echo_req_sent', 'link_error', 'link_up'], name, value)


                    class NcpStatisticsArray(Entity):
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
                        	**type**\:   :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdent>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray, self).__init__()

                            self.yang_name = "ncp-statistics-array"
                            self.yang_parent_name = "node-interface-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.conf_ack_rcvd = YLeaf(YType.uint16, "conf-ack-rcvd")

                            self.conf_ack_sent = YLeaf(YType.uint16, "conf-ack-sent")

                            self.conf_nak_rcvd = YLeaf(YType.uint16, "conf-nak-rcvd")

                            self.conf_nak_sent = YLeaf(YType.uint16, "conf-nak-sent")

                            self.conf_rej_rcvd = YLeaf(YType.uint16, "conf-rej-rcvd")

                            self.conf_rej_sent = YLeaf(YType.uint16, "conf-rej-sent")

                            self.conf_req_rcvd = YLeaf(YType.uint16, "conf-req-rcvd")

                            self.conf_req_sent = YLeaf(YType.uint16, "conf-req-sent")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")
                            self._segment_path = lambda: "ncp-statistics-array"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray, ['conf_ack_rcvd', 'conf_ack_sent', 'conf_nak_rcvd', 'conf_nak_sent', 'conf_rej_rcvd', 'conf_rej_sent', 'conf_req_rcvd', 'conf_req_sent', 'ncp_identifier'], name, value)


            class NodeInterfaces(Entity):
                """
                Per interface PPP operational data
                
                .. attribute:: node_interface
                
                	LCP and summarized NCP data for an interface running PPP
                	**type**\: list of    :py:class:`NodeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ppp.Nodes.Node.NodeInterfaces, self).__init__()

                    self.yang_name = "node-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-interface" : ("node_interface", Ppp.Nodes.Node.NodeInterfaces.NodeInterface)}

                    self.node_interface = YList(self)
                    self._segment_path = lambda: "node-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces, [], name, value)


                class NodeInterface(Entity):
                    """
                    LCP and summarized NCP data for an interface
                    running PPP
                    
                    .. attribute:: interface  <key>
                    
                    	Interface running PPP
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: auth_info
                    
                    	Authentication information
                    	**type**\:   :py:class:`AuthInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo>`
                    
                    .. attribute:: caps_idb_srg_role
                    
                    	Caps IDB SRG role
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
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
                    	**type**\:   :py:class:`PppFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppFsmState>`
                    
                    .. attribute:: lcpsso_state
                    
                    	LCP SSO state
                    	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                    
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
                    
                    .. attribute:: session_srg_role
                    
                    	Session SRG role
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
                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface, self).__init__()

                        self.yang_name = "node-interface"
                        self.yang_parent_name = "node-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auth-info" : ("auth_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo), "configured-timeout" : ("configured_timeout", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout), "mp-info" : ("mp_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo)}
                        self._child_list_classes = {"ncp-info-array" : ("ncp_info_array", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray)}

                        self.interface = YLeaf(YType.str, "interface")

                        self.caps_idb_srg_role = YLeaf(YType.uint32, "caps-idb-srg-role")

                        self.ip_interworking_enabled = YLeaf(YType.boolean, "ip-interworking-enabled")

                        self.is_l2ac = YLeaf(YType.boolean, "is-l2ac")

                        self.is_lcp_delayed = YLeaf(YType.boolean, "is-lcp-delayed")

                        self.is_loopback_detected = YLeaf(YType.boolean, "is-loopback-detected")

                        self.is_mcmp_enabled = YLeaf(YType.boolean, "is-mcmp-enabled")

                        self.is_ssrp_configured = YLeaf(YType.boolean, "is-ssrp-configured")

                        self.is_tunneled_session = YLeaf(YType.boolean, "is-tunneled-session")

                        self.keepalive_period = YLeaf(YType.uint32, "keepalive-period")

                        self.keepalive_retry_count = YLeaf(YType.uint32, "keepalive-retry-count")

                        self.lcp_state = YLeaf(YType.enumeration, "lcp-state")

                        self.lcpsso_state = YLeaf(YType.enumeration, "lcpsso-state")

                        self.line_state = YLeaf(YType.uint32, "line-state")

                        self.local_ed = YLeaf(YType.str, "local-ed")

                        self.local_mcmp_classes = YLeaf(YType.uint8, "local-mcmp-classes")

                        self.local_mrru = YLeaf(YType.uint16, "local-mrru")

                        self.local_mru = YLeaf(YType.uint16, "local-mru")

                        self.parent_state = YLeaf(YType.uint32, "parent-state")

                        self.peer_ed = YLeaf(YType.str, "peer-ed")

                        self.peer_mcmp_classes = YLeaf(YType.uint8, "peer-mcmp-classes")

                        self.peer_mrru = YLeaf(YType.uint16, "peer-mrru")

                        self.peer_mru = YLeaf(YType.uint16, "peer-mru")

                        self.provisioned = YLeaf(YType.boolean, "provisioned")

                        self.session_expires = YLeaf(YType.uint32, "session-expires")

                        self.session_srg_role = YLeaf(YType.uint32, "session-srg-role")

                        self.ssrp_peer_id = YLeaf(YType.str, "ssrp-peer-id")

                        self.xconnect_id = YLeaf(YType.uint32, "xconnect-id")

                        self.auth_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo()
                        self.auth_info.parent = self
                        self._children_name_map["auth_info"] = "auth-info"
                        self._children_yang_names.add("auth-info")

                        self.configured_timeout = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout()
                        self.configured_timeout.parent = self
                        self._children_name_map["configured_timeout"] = "configured-timeout"
                        self._children_yang_names.add("configured-timeout")

                        self.mp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo()
                        self.mp_info.parent = self
                        self._children_name_map["mp_info"] = "mp-info"
                        self._children_yang_names.add("mp-info")

                        self.ncp_info_array = YList(self)
                        self._segment_path = lambda: "node-interface" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface, ['interface', 'caps_idb_srg_role', 'ip_interworking_enabled', 'is_l2ac', 'is_lcp_delayed', 'is_loopback_detected', 'is_mcmp_enabled', 'is_ssrp_configured', 'is_tunneled_session', 'keepalive_period', 'keepalive_retry_count', 'lcp_state', 'lcpsso_state', 'line_state', 'local_ed', 'local_mcmp_classes', 'local_mrru', 'local_mru', 'parent_state', 'peer_ed', 'peer_mcmp_classes', 'peer_mrru', 'peer_mru', 'provisioned', 'session_expires', 'session_srg_role', 'ssrp_peer_id', 'xconnect_id'], name, value)


                    class AuthInfo(Entity):
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
                        	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                        
                        .. attribute:: of_us_auth
                        
                        	Of Us authentication type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: of_us_name
                        
                        	Local authenticated name
                        	**type**\:  str
                        
                        .. attribute:: of_us_sso_state
                        
                        	Of Us auth SSO FSM State
                        	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo, self).__init__()

                            self.yang_name = "auth-info"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.is_authenticated = YLeaf(YType.boolean, "is-authenticated")

                            self.is_sso_authenticated = YLeaf(YType.boolean, "is-sso-authenticated")

                            self.of_peer_auth = YLeaf(YType.uint8, "of-peer-auth")

                            self.of_peer_name = YLeaf(YType.str, "of-peer-name")

                            self.of_peer_sso_state = YLeaf(YType.enumeration, "of-peer-sso-state")

                            self.of_us_auth = YLeaf(YType.uint8, "of-us-auth")

                            self.of_us_name = YLeaf(YType.str, "of-us-name")

                            self.of_us_sso_state = YLeaf(YType.enumeration, "of-us-sso-state")
                            self._segment_path = lambda: "auth-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo, ['is_authenticated', 'is_sso_authenticated', 'of_peer_auth', 'of_peer_name', 'of_peer_sso_state', 'of_us_auth', 'of_us_name', 'of_us_sso_state'], name, value)


                    class ConfiguredTimeout(Entity):
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
                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout, self).__init__()

                            self.yang_name = "configured-timeout"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.minutes = YLeaf(YType.uint32, "minutes")

                            self.seconds = YLeaf(YType.uint8, "seconds")
                            self._segment_path = lambda: "configured-timeout"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout, ['minutes', 'seconds'], name, value)


                    class MpInfo(Entity):
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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: mp_group
                        
                        	MP Group
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mp_member_info_array
                        
                        	Array of MP members
                        	**type**\: list of    :py:class:`MpMemberInfoArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray>`
                        
                        .. attribute:: mp_state
                        
                        	Member State
                        	**type**\:   :py:class:`PppLcpMpMbrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppLcpMpMbrState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo, self).__init__()

                            self.yang_name = "mp-info"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"mp-member-info-array" : ("mp_member_info_array", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray)}

                            self.active_links = YLeaf(YType.uint16, "active-links")

                            self.inactive_links = YLeaf(YType.uint16, "inactive-links")

                            self.is_mp_bundle = YLeaf(YType.boolean, "is-mp-bundle")

                            self.is_mp_bundle_member = YLeaf(YType.boolean, "is-mp-bundle-member")

                            self.minimum_active_links = YLeaf(YType.uint16, "minimum-active-links")

                            self.mp_bundle_interface = YLeaf(YType.str, "mp-bundle-interface")

                            self.mp_group = YLeaf(YType.uint32, "mp-group")

                            self.mp_state = YLeaf(YType.enumeration, "mp-state")

                            self.mp_member_info_array = YList(self)
                            self._segment_path = lambda: "mp-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo, ['active_links', 'inactive_links', 'is_mp_bundle', 'is_mp_bundle_member', 'minimum_active_links', 'mp_bundle_interface', 'mp_group', 'mp_state'], name, value)


                        class MpMemberInfoArray(Entity):
                            """
                            Array of MP members
                            
                            .. attribute:: interface
                            
                            	Member Interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: state
                            
                            	Member State
                            	**type**\:   :py:class:`PppLcpMpMbrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppLcpMpMbrState>`
                            
                            

                            """

                            _prefix = 'ppp-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray, self).__init__()

                                self.yang_name = "mp-member-info-array"
                                self.yang_parent_name = "mp-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface = YLeaf(YType.str, "interface")

                                self.state = YLeaf(YType.enumeration, "state")
                                self._segment_path = lambda: "mp-member-info-array"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray, ['interface', 'state'], name, value)


                    class NcpInfoArray(Entity):
                        """
                        Array of per\-NCP data
                        
                        .. attribute:: is_passive
                        
                        	Is Passive
                        	**type**\:  bool
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP state identifier
                        	**type**\:   :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdent>`
                        
                        .. attribute:: ncp_info
                        
                        	Specific NCP info
                        	**type**\:   :py:class:`NcpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo>`
                        
                        .. attribute:: ncp_state
                        
                        	NCP state value
                        	**type**\:   :py:class:`PppFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppFsmState>`
                        
                        .. attribute:: ncpsso_state
                        
                        	NCP SSO State
                        	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray, self).__init__()

                            self.yang_name = "ncp-info-array"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ncp-info" : ("ncp_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo)}
                            self._child_list_classes = {}

                            self.is_passive = YLeaf(YType.boolean, "is-passive")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                            self.ncp_state = YLeaf(YType.enumeration, "ncp-state")

                            self.ncpsso_state = YLeaf(YType.enumeration, "ncpsso-state")

                            self.ncp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo()
                            self.ncp_info.parent = self
                            self._children_name_map["ncp_info"] = "ncp-info"
                            self._children_yang_names.add("ncp-info")
                            self._segment_path = lambda: "ncp-info-array"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray, ['is_passive', 'ncp_identifier', 'ncp_state', 'ncpsso_state'], name, value)


                        class NcpInfo(Entity):
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
                            	**type**\:   :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdent>`
                            
                            

                            """

                            _prefix = 'ppp-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo, self).__init__()

                                self.yang_name = "ncp-info"
                                self.yang_parent_name = "ncp-info-array"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipcp-info" : ("ipcp_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo), "ipcpiw-info" : ("ipcpiw_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo), "ipv6cp-info" : ("ipv6cp_info", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo)}
                                self._child_list_classes = {}

                                self.type = YLeaf(YType.enumeration, "type")

                                self.ipcp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo()
                                self.ipcp_info.parent = self
                                self._children_name_map["ipcp_info"] = "ipcp-info"
                                self._children_yang_names.add("ipcp-info")

                                self.ipcpiw_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo()
                                self.ipcpiw_info.parent = self
                                self._children_name_map["ipcpiw_info"] = "ipcpiw-info"
                                self._children_yang_names.add("ipcpiw-info")

                                self.ipv6cp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo()
                                self.ipv6cp_info.parent = self
                                self._children_name_map["ipv6cp_info"] = "ipv6cp-info"
                                self._children_yang_names.add("ipv6cp-info")
                                self._segment_path = lambda: "ncp-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo, ['type'], name, value)


                            class IpcpInfo(Entity):
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
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo, self).__init__()

                                    self.yang_name = "ipcp-info"
                                    self.yang_parent_name = "ncp-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"local-iphc-options" : ("local_iphc_options", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions), "peer-iphc-options" : ("peer_iphc_options", Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions)}
                                    self._child_list_classes = {}

                                    self.dns_primary = YLeaf(YType.str, "dns-primary")

                                    self.dns_secondary = YLeaf(YType.str, "dns-secondary")

                                    self.is_iphc_configured = YLeaf(YType.boolean, "is-iphc-configured")

                                    self.local_address = YLeaf(YType.str, "local-address")

                                    self.peer_address = YLeaf(YType.str, "peer-address")

                                    self.peer_netmask = YLeaf(YType.str, "peer-netmask")

                                    self.wins_primary = YLeaf(YType.str, "wins-primary")

                                    self.wins_secondary = YLeaf(YType.str, "wins-secondary")

                                    self.local_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions()
                                    self.local_iphc_options.parent = self
                                    self._children_name_map["local_iphc_options"] = "local-iphc-options"
                                    self._children_yang_names.add("local-iphc-options")

                                    self.peer_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions()
                                    self.peer_iphc_options.parent = self
                                    self._children_name_map["peer_iphc_options"] = "peer-iphc-options"
                                    self._children_yang_names.add("peer-iphc-options")
                                    self._segment_path = lambda: "ipcp-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo, ['dns_primary', 'dns_secondary', 'is_iphc_configured', 'local_address', 'peer_address', 'peer_netmask', 'wins_primary', 'wins_secondary'], name, value)


                                class LocalIphcOptions(Entity):
                                    """
                                    Local IPHC options
                                    
                                    .. attribute:: compression_type
                                    
                                    	Compression type
                                    	**type**\:   :py:class:`PppIphcCompression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppIphcCompression>`
                                    
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
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions, self).__init__()

                                        self.yang_name = "local-iphc-options"
                                        self.yang_parent_name = "ipcp-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.compression_type = YLeaf(YType.enumeration, "compression-type")

                                        self.ec_rtp_compression = YLeaf(YType.boolean, "ec-rtp-compression")

                                        self.max_header = YLeaf(YType.uint16, "max-header")

                                        self.max_period = YLeaf(YType.uint16, "max-period")

                                        self.max_time = YLeaf(YType.uint16, "max-time")

                                        self.non_tcp_space = YLeaf(YType.uint16, "non-tcp-space")

                                        self.rtp_compression = YLeaf(YType.boolean, "rtp-compression")

                                        self.tcp_space = YLeaf(YType.uint16, "tcp-space")
                                        self._segment_path = lambda: "local-iphc-options"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions, ['compression_type', 'ec_rtp_compression', 'max_header', 'max_period', 'max_time', 'non_tcp_space', 'rtp_compression', 'tcp_space'], name, value)


                                class PeerIphcOptions(Entity):
                                    """
                                    Peer IPHC options
                                    
                                    .. attribute:: compression_type
                                    
                                    	Compression type
                                    	**type**\:   :py:class:`PppIphcCompression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppIphcCompression>`
                                    
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
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions, self).__init__()

                                        self.yang_name = "peer-iphc-options"
                                        self.yang_parent_name = "ipcp-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.compression_type = YLeaf(YType.enumeration, "compression-type")

                                        self.ec_rtp_compression = YLeaf(YType.boolean, "ec-rtp-compression")

                                        self.max_header = YLeaf(YType.uint16, "max-header")

                                        self.max_period = YLeaf(YType.uint16, "max-period")

                                        self.max_time = YLeaf(YType.uint16, "max-time")

                                        self.non_tcp_space = YLeaf(YType.uint16, "non-tcp-space")

                                        self.rtp_compression = YLeaf(YType.boolean, "rtp-compression")

                                        self.tcp_space = YLeaf(YType.uint16, "tcp-space")
                                        self._segment_path = lambda: "peer-iphc-options"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions, ['compression_type', 'ec_rtp_compression', 'max_header', 'max_period', 'max_time', 'non_tcp_space', 'rtp_compression', 'tcp_space'], name, value)


                            class IpcpiwInfo(Entity):
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
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo, self).__init__()

                                    self.yang_name = "ipcpiw-info"
                                    self.yang_parent_name = "ncp-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.local_address = YLeaf(YType.str, "local-address")

                                    self.peer_address = YLeaf(YType.str, "peer-address")
                                    self._segment_path = lambda: "ipcpiw-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo, ['local_address', 'peer_address'], name, value)


                            class Ipv6CpInfo(Entity):
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
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo, self).__init__()

                                    self.yang_name = "ipv6cp-info"
                                    self.yang_parent_name = "ncp-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.local_address = YLeaf(YType.str, "local-address")

                                    self.peer_address = YLeaf(YType.str, "peer-address")
                                    self._segment_path = lambda: "ipv6cp-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo, ['local_address', 'peer_address'], name, value)


            class SsoAlerts(Entity):
                """
                PPP SSO Alert data for a particular node
                
                .. attribute:: sso_alert
                
                	PPP SSO Alert data for a particular interface
                	**type**\: list of    :py:class:`SsoAlert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoAlerts.SsoAlert>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ppp.Nodes.Node.SsoAlerts, self).__init__()

                    self.yang_name = "sso-alerts"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"sso-alert" : ("sso_alert", Ppp.Nodes.Node.SsoAlerts.SsoAlert)}

                    self.sso_alert = YList(self)
                    self._segment_path = lambda: "sso-alerts"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ppp.Nodes.Node.SsoAlerts, [], name, value)


                class SsoAlert(Entity):
                    """
                    PPP SSO Alert data for a particular interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface with SSO Alert
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert, self).__init__()

                        self.yang_name = "sso-alert"
                        self.yang_parent_name = "sso-alerts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipcp-error" : ("ipcp_error", Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError), "lcp-error" : ("lcp_error", Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError), "of-peer-auth-error" : ("of_peer_auth_error", Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError), "of-us-auth-error" : ("of_us_auth_error", Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError)}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.ipcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError()
                        self.ipcp_error.parent = self
                        self._children_name_map["ipcp_error"] = "ipcp-error"
                        self._children_yang_names.add("ipcp-error")

                        self.lcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError()
                        self.lcp_error.parent = self
                        self._children_name_map["lcp_error"] = "lcp-error"
                        self._children_yang_names.add("lcp-error")

                        self.of_peer_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError()
                        self.of_peer_auth_error.parent = self
                        self._children_name_map["of_peer_auth_error"] = "of-peer-auth-error"
                        self._children_yang_names.add("of-peer-auth-error")

                        self.of_us_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError()
                        self.of_us_auth_error.parent = self
                        self._children_name_map["of_us_auth_error"] = "of-us-auth-error"
                        self._children_yang_names.add("of-us-auth-error")
                        self._segment_path = lambda: "sso-alert" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoAlerts.SsoAlert, ['interface'], name, value)


                    class IpcpError(Entity):
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
                            super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError, self).__init__()

                            self.yang_name = "ipcp-error"
                            self.yang_parent_name = "sso-alert"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")
                            self._segment_path = lambda: "ipcp-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError, ['context', 'error', 'is_error'], name, value)


                    class LcpError(Entity):
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
                            super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError, self).__init__()

                            self.yang_name = "lcp-error"
                            self.yang_parent_name = "sso-alert"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")
                            self._segment_path = lambda: "lcp-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError, ['context', 'error', 'is_error'], name, value)


                    class OfPeerAuthError(Entity):
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
                            super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError, self).__init__()

                            self.yang_name = "of-peer-auth-error"
                            self.yang_parent_name = "sso-alert"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")
                            self._segment_path = lambda: "of-peer-auth-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError, ['context', 'error', 'is_error'], name, value)


                    class OfUsAuthError(Entity):
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
                            super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError, self).__init__()

                            self.yang_name = "of-us-auth-error"
                            self.yang_parent_name = "sso-alert"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")
                            self._segment_path = lambda: "of-us-auth-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError, ['context', 'error', 'is_error'], name, value)


            class SsoGroups(Entity):
                """
                PPP SSO Group data for a particular node
                
                .. attribute:: sso_group
                
                	PPP SSO state data for a particular group
                	**type**\: list of    :py:class:`SsoGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup>`
                
                

                """

                _prefix = 'ppp-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ppp.Nodes.Node.SsoGroups, self).__init__()

                    self.yang_name = "sso-groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"sso-group" : ("sso_group", Ppp.Nodes.Node.SsoGroups.SsoGroup)}

                    self.sso_group = YList(self)
                    self._segment_path = lambda: "sso-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ppp.Nodes.Node.SsoGroups, [], name, value)


                class SsoGroup(Entity):
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
                        super(Ppp.Nodes.Node.SsoGroups.SsoGroup, self).__init__()

                        self.yang_name = "sso-group"
                        self.yang_parent_name = "sso-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sso-states" : ("sso_states", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates)}
                        self._child_list_classes = {}

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.sso_states = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates()
                        self.sso_states.parent = self
                        self._children_name_map["sso_states"] = "sso-states"
                        self._children_yang_names.add("sso-states")
                        self._segment_path = lambda: "sso-group" + "[group-id='" + self.group_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup, ['group_id'], name, value)


                    class SsoStates(Entity):
                        """
                        PPP SSO State data for a particular group
                        
                        .. attribute:: sso_state
                        
                        	PPP SSO State data for a particular interface
                        	**type**\: list of    :py:class:`SsoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates, self).__init__()

                            self.yang_name = "sso-states"
                            self.yang_parent_name = "sso-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sso-state" : ("sso_state", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState)}

                            self.sso_state = YList(self)
                            self._segment_path = lambda: "sso-states"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates, [], name, value)


                        class SsoState(Entity):
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
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
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
                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState, self).__init__()

                                self.yang_name = "sso-state"
                                self.yang_parent_name = "sso-states"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipcp-state" : ("ipcp_state", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState), "lcp-state" : ("lcp_state", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState), "of-peer-auth-state" : ("of_peer_auth_state", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState), "of-us-auth-state" : ("of_us_auth_state", Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState)}
                                self._child_list_classes = {}

                                self.session_id = YLeaf(YType.uint32, "session-id")

                                self.interface = YLeaf(YType.str, "interface")

                                self.session_id_xr = YLeaf(YType.uint32, "session-id-xr")

                                self.ipcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState()
                                self.ipcp_state.parent = self
                                self._children_name_map["ipcp_state"] = "ipcp-state"
                                self._children_yang_names.add("ipcp-state")

                                self.lcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState()
                                self.lcp_state.parent = self
                                self._children_name_map["lcp_state"] = "lcp-state"
                                self._children_yang_names.add("lcp-state")

                                self.of_peer_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState()
                                self.of_peer_auth_state.parent = self
                                self._children_name_map["of_peer_auth_state"] = "of-peer-auth-state"
                                self._children_yang_names.add("of-peer-auth-state")

                                self.of_us_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState()
                                self.of_us_auth_state.parent = self
                                self._children_name_map["of_us_auth_state"] = "of-us-auth-state"
                                self._children_yang_names.add("of-us-auth-state")
                                self._segment_path = lambda: "sso-state" + "[session-id='" + self.session_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState, ['session_id', 'interface', 'session_id_xr'], name, value)


                            class IpcpState(Entity):
                                """
                                IPCP SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState, self).__init__()

                                    self.yang_name = "ipcp-state"
                                    self.yang_parent_name = "sso-state"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "ipcp-state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState, ['is_running', 'state'], name, value)


                            class LcpState(Entity):
                                """
                                LCP SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState, self).__init__()

                                    self.yang_name = "lcp-state"
                                    self.yang_parent_name = "sso-state"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "lcp-state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState, ['is_running', 'state'], name, value)


                            class OfPeerAuthState(Entity):
                                """
                                Of\-peer Authentication SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState, self).__init__()

                                    self.yang_name = "of-peer-auth-state"
                                    self.yang_parent_name = "sso-state"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "of-peer-auth-state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState, ['is_running', 'state'], name, value)


                            class OfUsAuthState(Entity):
                                """
                                Of\-us Authentication SSO State
                                
                                .. attribute:: is_running
                                
                                	Is SSO FSM Running
                                	**type**\:  bool
                                
                                .. attribute:: state
                                
                                	SSO FSM State
                                	**type**\:   :py:class:`PppSsoFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppSsoFsmState>`
                                
                                

                                """

                                _prefix = 'ppp-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState, self).__init__()

                                    self.yang_name = "of-us-auth-state"
                                    self.yang_parent_name = "sso-state"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "of-us-auth-state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState, ['is_running', 'state'], name, value)


            class SsoSummary(Entity):
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
                    super(Ppp.Nodes.Node.SsoSummary, self).__init__()

                    self.yang_name = "sso-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ipcp-states" : ("ipcp_states", Ppp.Nodes.Node.SsoSummary.IpcpStates), "lcp-states" : ("lcp_states", Ppp.Nodes.Node.SsoSummary.LcpStates), "of-peer-auth-states" : ("of_peer_auth_states", Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates), "of-us-auth-states" : ("of_us_auth_states", Ppp.Nodes.Node.SsoSummary.OfUsAuthStates)}
                    self._child_list_classes = {}

                    self.ipcp_states = Ppp.Nodes.Node.SsoSummary.IpcpStates()
                    self.ipcp_states.parent = self
                    self._children_name_map["ipcp_states"] = "ipcp-states"
                    self._children_yang_names.add("ipcp-states")

                    self.lcp_states = Ppp.Nodes.Node.SsoSummary.LcpStates()
                    self.lcp_states.parent = self
                    self._children_name_map["lcp_states"] = "lcp-states"
                    self._children_yang_names.add("lcp-states")

                    self.of_peer_auth_states = Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates()
                    self.of_peer_auth_states.parent = self
                    self._children_name_map["of_peer_auth_states"] = "of-peer-auth-states"
                    self._children_yang_names.add("of-peer-auth-states")

                    self.of_us_auth_states = Ppp.Nodes.Node.SsoSummary.OfUsAuthStates()
                    self.of_us_auth_states.parent = self
                    self._children_name_map["of_us_auth_states"] = "of-us-auth-states"
                    self._children_yang_names.add("of-us-auth-states")
                    self._segment_path = lambda: "sso-summary"


                class IpcpStates(Entity):
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
                        super(Ppp.Nodes.Node.SsoSummary.IpcpStates, self).__init__()

                        self.yang_name = "ipcp-states"
                        self.yang_parent_name = "sso-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")
                        self._segment_path = lambda: "ipcp-states"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoSummary.IpcpStates, ['count', 'total'], name, value)


                class LcpStates(Entity):
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
                        super(Ppp.Nodes.Node.SsoSummary.LcpStates, self).__init__()

                        self.yang_name = "lcp-states"
                        self.yang_parent_name = "sso-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")
                        self._segment_path = lambda: "lcp-states"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoSummary.LcpStates, ['count', 'total'], name, value)


                class OfPeerAuthStates(Entity):
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
                        super(Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates, self).__init__()

                        self.yang_name = "of-peer-auth-states"
                        self.yang_parent_name = "sso-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")
                        self._segment_path = lambda: "of-peer-auth-states"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates, ['count', 'total'], name, value)


                class OfUsAuthStates(Entity):
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
                        super(Ppp.Nodes.Node.SsoSummary.OfUsAuthStates, self).__init__()

                        self.yang_name = "of-us-auth-states"
                        self.yang_parent_name = "sso-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")
                        self._segment_path = lambda: "of-us-auth-states"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.SsoSummary.OfUsAuthStates, ['count', 'total'], name, value)


            class Statistics(Entity):
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
                    super(Ppp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"authentication-statistics" : ("authentication_statistics", Ppp.Nodes.Node.Statistics.AuthenticationStatistics), "lcp-statistics" : ("lcp_statistics", Ppp.Nodes.Node.Statistics.LcpStatistics)}
                    self._child_list_classes = {"ncp-statistics-array" : ("ncp_statistics_array", Ppp.Nodes.Node.Statistics.NcpStatisticsArray)}

                    self.authentication_statistics = Ppp.Nodes.Node.Statistics.AuthenticationStatistics()
                    self.authentication_statistics.parent = self
                    self._children_name_map["authentication_statistics"] = "authentication-statistics"
                    self._children_yang_names.add("authentication-statistics")

                    self.lcp_statistics = Ppp.Nodes.Node.Statistics.LcpStatistics()
                    self.lcp_statistics.parent = self
                    self._children_name_map["lcp_statistics"] = "lcp-statistics"
                    self._children_yang_names.add("lcp-statistics")

                    self.ncp_statistics_array = YList(self)
                    self._segment_path = lambda: "statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ppp.Nodes.Node.Statistics, [], name, value)


                class AuthenticationStatistics(Entity):
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
                        super(Ppp.Nodes.Node.Statistics.AuthenticationStatistics, self).__init__()

                        self.yang_name = "authentication-statistics"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.auth_timeout_count = YLeaf(YType.uint64, "auth-timeout-count")

                        self.chap_chall_rcvd = YLeaf(YType.uint64, "chap-chall-rcvd")

                        self.chap_chall_sent = YLeaf(YType.uint64, "chap-chall-sent")

                        self.chap_rep_fail_rcvd = YLeaf(YType.uint64, "chap-rep-fail-rcvd")

                        self.chap_rep_fail_sent = YLeaf(YType.uint64, "chap-rep-fail-sent")

                        self.chap_rep_succ_rcvd = YLeaf(YType.uint64, "chap-rep-succ-rcvd")

                        self.chap_rep_succ_sent = YLeaf(YType.uint64, "chap-rep-succ-sent")

                        self.chap_resp_rcvd = YLeaf(YType.uint64, "chap-resp-rcvd")

                        self.chap_resp_sent = YLeaf(YType.uint64, "chap-resp-sent")

                        self.pap_ack_rcvd = YLeaf(YType.uint64, "pap-ack-rcvd")

                        self.pap_ack_sent = YLeaf(YType.uint64, "pap-ack-sent")

                        self.pap_nak_rcvd = YLeaf(YType.uint64, "pap-nak-rcvd")

                        self.pap_nak_sent = YLeaf(YType.uint64, "pap-nak-sent")

                        self.pap_req_rcvd = YLeaf(YType.uint64, "pap-req-rcvd")

                        self.pap_req_sent = YLeaf(YType.uint64, "pap-req-sent")
                        self._segment_path = lambda: "authentication-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Statistics.AuthenticationStatistics, ['auth_timeout_count', 'chap_chall_rcvd', 'chap_chall_sent', 'chap_rep_fail_rcvd', 'chap_rep_fail_sent', 'chap_rep_succ_rcvd', 'chap_rep_succ_sent', 'chap_resp_rcvd', 'chap_resp_sent', 'pap_ack_rcvd', 'pap_ack_sent', 'pap_nak_rcvd', 'pap_nak_sent', 'pap_req_rcvd', 'pap_req_sent'], name, value)


                class LcpStatistics(Entity):
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
                        super(Ppp.Nodes.Node.Statistics.LcpStatistics, self).__init__()

                        self.yang_name = "lcp-statistics"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.code_rej_rcvd = YLeaf(YType.uint64, "code-rej-rcvd")

                        self.code_rej_sent = YLeaf(YType.uint64, "code-rej-sent")

                        self.conf_ack_rcvd = YLeaf(YType.uint64, "conf-ack-rcvd")

                        self.conf_ack_sent = YLeaf(YType.uint64, "conf-ack-sent")

                        self.conf_nak_rcvd = YLeaf(YType.uint64, "conf-nak-rcvd")

                        self.conf_nak_sent = YLeaf(YType.uint64, "conf-nak-sent")

                        self.conf_rej_rcvd = YLeaf(YType.uint64, "conf-rej-rcvd")

                        self.conf_rej_sent = YLeaf(YType.uint64, "conf-rej-sent")

                        self.conf_req_rcvd = YLeaf(YType.uint64, "conf-req-rcvd")

                        self.conf_req_sent = YLeaf(YType.uint64, "conf-req-sent")

                        self.disc_req_rcvd = YLeaf(YType.uint64, "disc-req-rcvd")

                        self.disc_req_sent = YLeaf(YType.uint64, "disc-req-sent")

                        self.echo_rep_rcvd = YLeaf(YType.uint64, "echo-rep-rcvd")

                        self.echo_rep_sent = YLeaf(YType.uint64, "echo-rep-sent")

                        self.echo_req_rcvd = YLeaf(YType.uint64, "echo-req-rcvd")

                        self.echo_req_sent = YLeaf(YType.uint64, "echo-req-sent")

                        self.link_error = YLeaf(YType.uint64, "link-error")

                        self.link_up = YLeaf(YType.uint64, "link-up")

                        self.proto_rej_rcvd = YLeaf(YType.uint64, "proto-rej-rcvd")

                        self.proto_rej_sent = YLeaf(YType.uint64, "proto-rej-sent")

                        self.term_ack_rcvd = YLeaf(YType.uint64, "term-ack-rcvd")

                        self.term_ack_sent = YLeaf(YType.uint64, "term-ack-sent")

                        self.term_req_rcvd = YLeaf(YType.uint64, "term-req-rcvd")

                        self.term_req_sent = YLeaf(YType.uint64, "term-req-sent")
                        self._segment_path = lambda: "lcp-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Statistics.LcpStatistics, ['code_rej_rcvd', 'code_rej_sent', 'conf_ack_rcvd', 'conf_ack_sent', 'conf_nak_rcvd', 'conf_nak_sent', 'conf_rej_rcvd', 'conf_rej_sent', 'conf_req_rcvd', 'conf_req_sent', 'disc_req_rcvd', 'disc_req_sent', 'echo_rep_rcvd', 'echo_rep_sent', 'echo_req_rcvd', 'echo_req_sent', 'link_error', 'link_up', 'proto_rej_rcvd', 'proto_rej_sent', 'term_ack_rcvd', 'term_ack_sent', 'term_req_rcvd', 'term_req_sent'], name, value)


                class NcpStatisticsArray(Entity):
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
                    	**type**\:   :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdent>`
                    
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
                        super(Ppp.Nodes.Node.Statistics.NcpStatisticsArray, self).__init__()

                        self.yang_name = "ncp-statistics-array"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.conf_ack_rcvd = YLeaf(YType.uint64, "conf-ack-rcvd")

                        self.conf_ack_sent = YLeaf(YType.uint64, "conf-ack-sent")

                        self.conf_nak_rcvd = YLeaf(YType.uint64, "conf-nak-rcvd")

                        self.conf_nak_sent = YLeaf(YType.uint64, "conf-nak-sent")

                        self.conf_rej_rcvd = YLeaf(YType.uint64, "conf-rej-rcvd")

                        self.conf_rej_sent = YLeaf(YType.uint64, "conf-rej-sent")

                        self.conf_req_rcvd = YLeaf(YType.uint64, "conf-req-rcvd")

                        self.conf_req_sent = YLeaf(YType.uint64, "conf-req-sent")

                        self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                        self.proto_rej_rcvd = YLeaf(YType.uint64, "proto-rej-rcvd")

                        self.proto_rej_sent = YLeaf(YType.uint64, "proto-rej-sent")

                        self.term_ack_rcvd = YLeaf(YType.uint64, "term-ack-rcvd")

                        self.term_ack_sent = YLeaf(YType.uint64, "term-ack-sent")

                        self.term_req_rcvd = YLeaf(YType.uint64, "term-req-rcvd")

                        self.term_req_sent = YLeaf(YType.uint64, "term-req-sent")
                        self._segment_path = lambda: "ncp-statistics-array"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Statistics.NcpStatisticsArray, ['conf_ack_rcvd', 'conf_ack_sent', 'conf_nak_rcvd', 'conf_nak_sent', 'conf_rej_rcvd', 'conf_rej_sent', 'conf_req_rcvd', 'conf_req_sent', 'ncp_identifier', 'proto_rej_rcvd', 'proto_rej_sent', 'term_ack_rcvd', 'term_ack_sent', 'term_req_rcvd', 'term_req_sent'], name, value)


            class Summary(Entity):
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
                    super(Ppp.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"fsm-states" : ("fsm_states", Ppp.Nodes.Node.Summary.FsmStates), "intfs" : ("intfs", Ppp.Nodes.Node.Summary.Intfs), "lcp-auth-phases" : ("lcp_auth_phases", Ppp.Nodes.Node.Summary.LcpAuthPhases)}
                    self._child_list_classes = {}

                    self.fsm_states = Ppp.Nodes.Node.Summary.FsmStates()
                    self.fsm_states.parent = self
                    self._children_name_map["fsm_states"] = "fsm-states"
                    self._children_yang_names.add("fsm-states")

                    self.intfs = Ppp.Nodes.Node.Summary.Intfs()
                    self.intfs.parent = self
                    self._children_name_map["intfs"] = "intfs"
                    self._children_yang_names.add("intfs")

                    self.lcp_auth_phases = Ppp.Nodes.Node.Summary.LcpAuthPhases()
                    self.lcp_auth_phases.parent = self
                    self._children_name_map["lcp_auth_phases"] = "lcp-auth-phases"
                    self._children_yang_names.add("lcp-auth-phases")
                    self._segment_path = lambda: "summary"


                class FsmStates(Entity):
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
                        super(Ppp.Nodes.Node.Summary.FsmStates, self).__init__()

                        self.yang_name = "fsm-states"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"lcpfsm-states" : ("lcpfsm_states", Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates)}
                        self._child_list_classes = {"ncpfsm-states-array" : ("ncpfsm_states_array", Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray)}

                        self.lcpfsm_states = Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates()
                        self.lcpfsm_states.parent = self
                        self._children_name_map["lcpfsm_states"] = "lcpfsm-states"
                        self._children_yang_names.add("lcpfsm-states")

                        self.ncpfsm_states_array = YList(self)
                        self._segment_path = lambda: "fsm-states"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Summary.FsmStates, [], name, value)


                    class LcpfsmStates(Entity):
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
                            super(Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates, self).__init__()

                            self.yang_name = "lcpfsm-states"
                            self.yang_parent_name = "fsm-states"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.count = YLeafList(YType.uint32, "count")

                            self.total = YLeaf(YType.uint32, "total")
                            self._segment_path = lambda: "lcpfsm-states"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates, ['count', 'total'], name, value)


                    class NcpfsmStatesArray(Entity):
                        """
                        Array of per\-NCP FSM States
                        
                        .. attribute:: count
                        
                        	Number of FSMs in each State
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP Identifier
                        	**type**\:   :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.NcpIdent>`
                        
                        .. attribute:: total
                        
                        	Total number of FSMs running for this NCP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray, self).__init__()

                            self.yang_name = "ncpfsm-states-array"
                            self.yang_parent_name = "fsm-states"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.count = YLeafList(YType.uint32, "count")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                            self.total = YLeaf(YType.uint32, "total")
                            self._segment_path = lambda: "ncpfsm-states-array"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray, ['count', 'ncp_identifier', 'total'], name, value)


                class Intfs(Entity):
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
                        super(Ppp.Nodes.Node.Summary.Intfs, self).__init__()

                        self.yang_name = "intfs"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.gcc0_count = YLeaf(YType.uint32, "gcc0-count")

                        self.gcc1_count = YLeaf(YType.uint32, "gcc1-count")

                        self.multilink_bundle_count = YLeaf(YType.uint32, "multilink-bundle-count")

                        self.pos_count = YLeaf(YType.uint32, "pos-count")

                        self.pppoe_count = YLeaf(YType.uint32, "pppoe-count")

                        self.serial_count = YLeaf(YType.uint32, "serial-count")

                        self.total = YLeaf(YType.uint32, "total")
                        self._segment_path = lambda: "intfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Summary.Intfs, ['gcc0_count', 'gcc1_count', 'multilink_bundle_count', 'pos_count', 'pppoe_count', 'serial_count', 'total'], name, value)


                class LcpAuthPhases(Entity):
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
                        super(Ppp.Nodes.Node.Summary.LcpAuthPhases, self).__init__()

                        self.yang_name = "lcp-auth-phases"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.authenticating = YLeaf(YType.uint32, "authenticating")

                        self.lcp_not_negotiated = YLeaf(YType.uint32, "lcp-not-negotiated")

                        self.line_held_down = YLeaf(YType.uint32, "line-held-down")

                        self.up_l2_fwded = YLeaf(YType.uint32, "up-l2-fwded")

                        self.up_local_term = YLeaf(YType.uint32, "up-local-term")

                        self.up_tunneled = YLeaf(YType.uint32, "up-tunneled")
                        self._segment_path = lambda: "lcp-auth-phases"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ppp.Nodes.Node.Summary.LcpAuthPhases, ['authenticating', 'lcp_not_negotiated', 'line_held_down', 'up_l2_fwded', 'up_local_term', 'up_tunneled'], name, value)

    def clone_ptr(self):
        self._top_entity = Ppp()
        return self._top_entity

