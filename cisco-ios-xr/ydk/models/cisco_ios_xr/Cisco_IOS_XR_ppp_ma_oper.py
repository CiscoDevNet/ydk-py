""" Cisco_IOS_XR_ppp_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma package operational data.

This module contains definitions
for the following management objects\:
  ppp\: PPP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.nodes = Ppp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


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

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ppp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ppp.Nodes, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ppp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ppp.Nodes.Node, self).__setattr__(name, value)


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

                    self.authentication_statistics = Ppp.Nodes.Node.Statistics.AuthenticationStatistics()
                    self.authentication_statistics.parent = self
                    self._children_name_map["authentication_statistics"] = "authentication-statistics"
                    self._children_yang_names.add("authentication-statistics")

                    self.lcp_statistics = Ppp.Nodes.Node.Statistics.LcpStatistics()
                    self.lcp_statistics.parent = self
                    self._children_name_map["lcp_statistics"] = "lcp-statistics"
                    self._children_yang_names.add("lcp-statistics")

                    self.ncp_statistics_array = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ppp.Nodes.Node.Statistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ppp.Nodes.Node.Statistics, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("code_rej_rcvd",
                                        "code_rej_sent",
                                        "conf_ack_rcvd",
                                        "conf_ack_sent",
                                        "conf_nak_rcvd",
                                        "conf_nak_sent",
                                        "conf_rej_rcvd",
                                        "conf_rej_sent",
                                        "conf_req_rcvd",
                                        "conf_req_sent",
                                        "disc_req_rcvd",
                                        "disc_req_sent",
                                        "echo_rep_rcvd",
                                        "echo_rep_sent",
                                        "echo_req_rcvd",
                                        "echo_req_sent",
                                        "link_error",
                                        "link_up",
                                        "proto_rej_rcvd",
                                        "proto_rej_sent",
                                        "term_ack_rcvd",
                                        "term_ack_sent",
                                        "term_req_rcvd",
                                        "term_req_sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Statistics.LcpStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Statistics.LcpStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.code_rej_rcvd.is_set or
                            self.code_rej_sent.is_set or
                            self.conf_ack_rcvd.is_set or
                            self.conf_ack_sent.is_set or
                            self.conf_nak_rcvd.is_set or
                            self.conf_nak_sent.is_set or
                            self.conf_rej_rcvd.is_set or
                            self.conf_rej_sent.is_set or
                            self.conf_req_rcvd.is_set or
                            self.conf_req_sent.is_set or
                            self.disc_req_rcvd.is_set or
                            self.disc_req_sent.is_set or
                            self.echo_rep_rcvd.is_set or
                            self.echo_rep_sent.is_set or
                            self.echo_req_rcvd.is_set or
                            self.echo_req_sent.is_set or
                            self.link_error.is_set or
                            self.link_up.is_set or
                            self.proto_rej_rcvd.is_set or
                            self.proto_rej_sent.is_set or
                            self.term_ack_rcvd.is_set or
                            self.term_ack_sent.is_set or
                            self.term_req_rcvd.is_set or
                            self.term_req_sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.code_rej_rcvd.yfilter != YFilter.not_set or
                            self.code_rej_sent.yfilter != YFilter.not_set or
                            self.conf_ack_rcvd.yfilter != YFilter.not_set or
                            self.conf_ack_sent.yfilter != YFilter.not_set or
                            self.conf_nak_rcvd.yfilter != YFilter.not_set or
                            self.conf_nak_sent.yfilter != YFilter.not_set or
                            self.conf_rej_rcvd.yfilter != YFilter.not_set or
                            self.conf_rej_sent.yfilter != YFilter.not_set or
                            self.conf_req_rcvd.yfilter != YFilter.not_set or
                            self.conf_req_sent.yfilter != YFilter.not_set or
                            self.disc_req_rcvd.yfilter != YFilter.not_set or
                            self.disc_req_sent.yfilter != YFilter.not_set or
                            self.echo_rep_rcvd.yfilter != YFilter.not_set or
                            self.echo_rep_sent.yfilter != YFilter.not_set or
                            self.echo_req_rcvd.yfilter != YFilter.not_set or
                            self.echo_req_sent.yfilter != YFilter.not_set or
                            self.link_error.yfilter != YFilter.not_set or
                            self.link_up.yfilter != YFilter.not_set or
                            self.proto_rej_rcvd.yfilter != YFilter.not_set or
                            self.proto_rej_sent.yfilter != YFilter.not_set or
                            self.term_ack_rcvd.yfilter != YFilter.not_set or
                            self.term_ack_sent.yfilter != YFilter.not_set or
                            self.term_req_rcvd.yfilter != YFilter.not_set or
                            self.term_req_sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lcp-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.code_rej_rcvd.is_set or self.code_rej_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.code_rej_rcvd.get_name_leafdata())
                        if (self.code_rej_sent.is_set or self.code_rej_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.code_rej_sent.get_name_leafdata())
                        if (self.conf_ack_rcvd.is_set or self.conf_ack_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_ack_rcvd.get_name_leafdata())
                        if (self.conf_ack_sent.is_set or self.conf_ack_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_ack_sent.get_name_leafdata())
                        if (self.conf_nak_rcvd.is_set or self.conf_nak_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_nak_rcvd.get_name_leafdata())
                        if (self.conf_nak_sent.is_set or self.conf_nak_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_nak_sent.get_name_leafdata())
                        if (self.conf_rej_rcvd.is_set or self.conf_rej_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_rej_rcvd.get_name_leafdata())
                        if (self.conf_rej_sent.is_set or self.conf_rej_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_rej_sent.get_name_leafdata())
                        if (self.conf_req_rcvd.is_set or self.conf_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_req_rcvd.get_name_leafdata())
                        if (self.conf_req_sent.is_set or self.conf_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_req_sent.get_name_leafdata())
                        if (self.disc_req_rcvd.is_set or self.disc_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disc_req_rcvd.get_name_leafdata())
                        if (self.disc_req_sent.is_set or self.disc_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disc_req_sent.get_name_leafdata())
                        if (self.echo_rep_rcvd.is_set or self.echo_rep_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_rep_rcvd.get_name_leafdata())
                        if (self.echo_rep_sent.is_set or self.echo_rep_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_rep_sent.get_name_leafdata())
                        if (self.echo_req_rcvd.is_set or self.echo_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_req_rcvd.get_name_leafdata())
                        if (self.echo_req_sent.is_set or self.echo_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_req_sent.get_name_leafdata())
                        if (self.link_error.is_set or self.link_error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.link_error.get_name_leafdata())
                        if (self.link_up.is_set or self.link_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.link_up.get_name_leafdata())
                        if (self.proto_rej_rcvd.is_set or self.proto_rej_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proto_rej_rcvd.get_name_leafdata())
                        if (self.proto_rej_sent.is_set or self.proto_rej_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proto_rej_sent.get_name_leafdata())
                        if (self.term_ack_rcvd.is_set or self.term_ack_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_ack_rcvd.get_name_leafdata())
                        if (self.term_ack_sent.is_set or self.term_ack_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_ack_sent.get_name_leafdata())
                        if (self.term_req_rcvd.is_set or self.term_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_req_rcvd.get_name_leafdata())
                        if (self.term_req_sent.is_set or self.term_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_req_sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "code-rej-rcvd" or name == "code-rej-sent" or name == "conf-ack-rcvd" or name == "conf-ack-sent" or name == "conf-nak-rcvd" or name == "conf-nak-sent" or name == "conf-rej-rcvd" or name == "conf-rej-sent" or name == "conf-req-rcvd" or name == "conf-req-sent" or name == "disc-req-rcvd" or name == "disc-req-sent" or name == "echo-rep-rcvd" or name == "echo-rep-sent" or name == "echo-req-rcvd" or name == "echo-req-sent" or name == "link-error" or name == "link-up" or name == "proto-rej-rcvd" or name == "proto-rej-sent" or name == "term-ack-rcvd" or name == "term-ack-sent" or name == "term-req-rcvd" or name == "term-req-sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "code-rej-rcvd"):
                            self.code_rej_rcvd = value
                            self.code_rej_rcvd.value_namespace = name_space
                            self.code_rej_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "code-rej-sent"):
                            self.code_rej_sent = value
                            self.code_rej_sent.value_namespace = name_space
                            self.code_rej_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-ack-rcvd"):
                            self.conf_ack_rcvd = value
                            self.conf_ack_rcvd.value_namespace = name_space
                            self.conf_ack_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-ack-sent"):
                            self.conf_ack_sent = value
                            self.conf_ack_sent.value_namespace = name_space
                            self.conf_ack_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-nak-rcvd"):
                            self.conf_nak_rcvd = value
                            self.conf_nak_rcvd.value_namespace = name_space
                            self.conf_nak_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-nak-sent"):
                            self.conf_nak_sent = value
                            self.conf_nak_sent.value_namespace = name_space
                            self.conf_nak_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-rej-rcvd"):
                            self.conf_rej_rcvd = value
                            self.conf_rej_rcvd.value_namespace = name_space
                            self.conf_rej_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-rej-sent"):
                            self.conf_rej_sent = value
                            self.conf_rej_sent.value_namespace = name_space
                            self.conf_rej_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-req-rcvd"):
                            self.conf_req_rcvd = value
                            self.conf_req_rcvd.value_namespace = name_space
                            self.conf_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-req-sent"):
                            self.conf_req_sent = value
                            self.conf_req_sent.value_namespace = name_space
                            self.conf_req_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "disc-req-rcvd"):
                            self.disc_req_rcvd = value
                            self.disc_req_rcvd.value_namespace = name_space
                            self.disc_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "disc-req-sent"):
                            self.disc_req_sent = value
                            self.disc_req_sent.value_namespace = name_space
                            self.disc_req_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-rep-rcvd"):
                            self.echo_rep_rcvd = value
                            self.echo_rep_rcvd.value_namespace = name_space
                            self.echo_rep_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-rep-sent"):
                            self.echo_rep_sent = value
                            self.echo_rep_sent.value_namespace = name_space
                            self.echo_rep_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-req-rcvd"):
                            self.echo_req_rcvd = value
                            self.echo_req_rcvd.value_namespace = name_space
                            self.echo_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-req-sent"):
                            self.echo_req_sent = value
                            self.echo_req_sent.value_namespace = name_space
                            self.echo_req_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "link-error"):
                            self.link_error = value
                            self.link_error.value_namespace = name_space
                            self.link_error.value_namespace_prefix = name_space_prefix
                        if(value_path == "link-up"):
                            self.link_up = value
                            self.link_up.value_namespace = name_space
                            self.link_up.value_namespace_prefix = name_space_prefix
                        if(value_path == "proto-rej-rcvd"):
                            self.proto_rej_rcvd = value
                            self.proto_rej_rcvd.value_namespace = name_space
                            self.proto_rej_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "proto-rej-sent"):
                            self.proto_rej_sent = value
                            self.proto_rej_sent.value_namespace = name_space
                            self.proto_rej_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-ack-rcvd"):
                            self.term_ack_rcvd = value
                            self.term_ack_rcvd.value_namespace = name_space
                            self.term_ack_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-ack-sent"):
                            self.term_ack_sent = value
                            self.term_ack_sent.value_namespace = name_space
                            self.term_ack_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-req-rcvd"):
                            self.term_req_rcvd = value
                            self.term_req_rcvd.value_namespace = name_space
                            self.term_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-req-sent"):
                            self.term_req_sent = value
                            self.term_req_sent.value_namespace = name_space
                            self.term_req_sent.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auth_timeout_count",
                                        "chap_chall_rcvd",
                                        "chap_chall_sent",
                                        "chap_rep_fail_rcvd",
                                        "chap_rep_fail_sent",
                                        "chap_rep_succ_rcvd",
                                        "chap_rep_succ_sent",
                                        "chap_resp_rcvd",
                                        "chap_resp_sent",
                                        "pap_ack_rcvd",
                                        "pap_ack_sent",
                                        "pap_nak_rcvd",
                                        "pap_nak_sent",
                                        "pap_req_rcvd",
                                        "pap_req_sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Statistics.AuthenticationStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Statistics.AuthenticationStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.auth_timeout_count.is_set or
                            self.chap_chall_rcvd.is_set or
                            self.chap_chall_sent.is_set or
                            self.chap_rep_fail_rcvd.is_set or
                            self.chap_rep_fail_sent.is_set or
                            self.chap_rep_succ_rcvd.is_set or
                            self.chap_rep_succ_sent.is_set or
                            self.chap_resp_rcvd.is_set or
                            self.chap_resp_sent.is_set or
                            self.pap_ack_rcvd.is_set or
                            self.pap_ack_sent.is_set or
                            self.pap_nak_rcvd.is_set or
                            self.pap_nak_sent.is_set or
                            self.pap_req_rcvd.is_set or
                            self.pap_req_sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auth_timeout_count.yfilter != YFilter.not_set or
                            self.chap_chall_rcvd.yfilter != YFilter.not_set or
                            self.chap_chall_sent.yfilter != YFilter.not_set or
                            self.chap_rep_fail_rcvd.yfilter != YFilter.not_set or
                            self.chap_rep_fail_sent.yfilter != YFilter.not_set or
                            self.chap_rep_succ_rcvd.yfilter != YFilter.not_set or
                            self.chap_rep_succ_sent.yfilter != YFilter.not_set or
                            self.chap_resp_rcvd.yfilter != YFilter.not_set or
                            self.chap_resp_sent.yfilter != YFilter.not_set or
                            self.pap_ack_rcvd.yfilter != YFilter.not_set or
                            self.pap_ack_sent.yfilter != YFilter.not_set or
                            self.pap_nak_rcvd.yfilter != YFilter.not_set or
                            self.pap_nak_sent.yfilter != YFilter.not_set or
                            self.pap_req_rcvd.yfilter != YFilter.not_set or
                            self.pap_req_sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authentication-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auth_timeout_count.is_set or self.auth_timeout_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_timeout_count.get_name_leafdata())
                        if (self.chap_chall_rcvd.is_set or self.chap_chall_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_chall_rcvd.get_name_leafdata())
                        if (self.chap_chall_sent.is_set or self.chap_chall_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_chall_sent.get_name_leafdata())
                        if (self.chap_rep_fail_rcvd.is_set or self.chap_rep_fail_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_rep_fail_rcvd.get_name_leafdata())
                        if (self.chap_rep_fail_sent.is_set or self.chap_rep_fail_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_rep_fail_sent.get_name_leafdata())
                        if (self.chap_rep_succ_rcvd.is_set or self.chap_rep_succ_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_rep_succ_rcvd.get_name_leafdata())
                        if (self.chap_rep_succ_sent.is_set or self.chap_rep_succ_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_rep_succ_sent.get_name_leafdata())
                        if (self.chap_resp_rcvd.is_set or self.chap_resp_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_resp_rcvd.get_name_leafdata())
                        if (self.chap_resp_sent.is_set or self.chap_resp_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chap_resp_sent.get_name_leafdata())
                        if (self.pap_ack_rcvd.is_set or self.pap_ack_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_ack_rcvd.get_name_leafdata())
                        if (self.pap_ack_sent.is_set or self.pap_ack_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_ack_sent.get_name_leafdata())
                        if (self.pap_nak_rcvd.is_set or self.pap_nak_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_nak_rcvd.get_name_leafdata())
                        if (self.pap_nak_sent.is_set or self.pap_nak_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_nak_sent.get_name_leafdata())
                        if (self.pap_req_rcvd.is_set or self.pap_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_req_rcvd.get_name_leafdata())
                        if (self.pap_req_sent.is_set or self.pap_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pap_req_sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auth-timeout-count" or name == "chap-chall-rcvd" or name == "chap-chall-sent" or name == "chap-rep-fail-rcvd" or name == "chap-rep-fail-sent" or name == "chap-rep-succ-rcvd" or name == "chap-rep-succ-sent" or name == "chap-resp-rcvd" or name == "chap-resp-sent" or name == "pap-ack-rcvd" or name == "pap-ack-sent" or name == "pap-nak-rcvd" or name == "pap-nak-sent" or name == "pap-req-rcvd" or name == "pap-req-sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auth-timeout-count"):
                            self.auth_timeout_count = value
                            self.auth_timeout_count.value_namespace = name_space
                            self.auth_timeout_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-chall-rcvd"):
                            self.chap_chall_rcvd = value
                            self.chap_chall_rcvd.value_namespace = name_space
                            self.chap_chall_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-chall-sent"):
                            self.chap_chall_sent = value
                            self.chap_chall_sent.value_namespace = name_space
                            self.chap_chall_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-rep-fail-rcvd"):
                            self.chap_rep_fail_rcvd = value
                            self.chap_rep_fail_rcvd.value_namespace = name_space
                            self.chap_rep_fail_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-rep-fail-sent"):
                            self.chap_rep_fail_sent = value
                            self.chap_rep_fail_sent.value_namespace = name_space
                            self.chap_rep_fail_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-rep-succ-rcvd"):
                            self.chap_rep_succ_rcvd = value
                            self.chap_rep_succ_rcvd.value_namespace = name_space
                            self.chap_rep_succ_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-rep-succ-sent"):
                            self.chap_rep_succ_sent = value
                            self.chap_rep_succ_sent.value_namespace = name_space
                            self.chap_rep_succ_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-resp-rcvd"):
                            self.chap_resp_rcvd = value
                            self.chap_resp_rcvd.value_namespace = name_space
                            self.chap_resp_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "chap-resp-sent"):
                            self.chap_resp_sent = value
                            self.chap_resp_sent.value_namespace = name_space
                            self.chap_resp_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-ack-rcvd"):
                            self.pap_ack_rcvd = value
                            self.pap_ack_rcvd.value_namespace = name_space
                            self.pap_ack_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-ack-sent"):
                            self.pap_ack_sent = value
                            self.pap_ack_sent.value_namespace = name_space
                            self.pap_ack_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-nak-rcvd"):
                            self.pap_nak_rcvd = value
                            self.pap_nak_rcvd.value_namespace = name_space
                            self.pap_nak_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-nak-sent"):
                            self.pap_nak_sent = value
                            self.pap_nak_sent.value_namespace = name_space
                            self.pap_nak_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-req-rcvd"):
                            self.pap_req_rcvd = value
                            self.pap_req_rcvd.value_namespace = name_space
                            self.pap_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "pap-req-sent"):
                            self.pap_req_sent = value
                            self.pap_req_sent.value_namespace = name_space
                            self.pap_req_sent.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("conf_ack_rcvd",
                                        "conf_ack_sent",
                                        "conf_nak_rcvd",
                                        "conf_nak_sent",
                                        "conf_rej_rcvd",
                                        "conf_rej_sent",
                                        "conf_req_rcvd",
                                        "conf_req_sent",
                                        "ncp_identifier",
                                        "proto_rej_rcvd",
                                        "proto_rej_sent",
                                        "term_ack_rcvd",
                                        "term_ack_sent",
                                        "term_req_rcvd",
                                        "term_req_sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Statistics.NcpStatisticsArray, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Statistics.NcpStatisticsArray, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.conf_ack_rcvd.is_set or
                            self.conf_ack_sent.is_set or
                            self.conf_nak_rcvd.is_set or
                            self.conf_nak_sent.is_set or
                            self.conf_rej_rcvd.is_set or
                            self.conf_rej_sent.is_set or
                            self.conf_req_rcvd.is_set or
                            self.conf_req_sent.is_set or
                            self.ncp_identifier.is_set or
                            self.proto_rej_rcvd.is_set or
                            self.proto_rej_sent.is_set or
                            self.term_ack_rcvd.is_set or
                            self.term_ack_sent.is_set or
                            self.term_req_rcvd.is_set or
                            self.term_req_sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.conf_ack_rcvd.yfilter != YFilter.not_set or
                            self.conf_ack_sent.yfilter != YFilter.not_set or
                            self.conf_nak_rcvd.yfilter != YFilter.not_set or
                            self.conf_nak_sent.yfilter != YFilter.not_set or
                            self.conf_rej_rcvd.yfilter != YFilter.not_set or
                            self.conf_rej_sent.yfilter != YFilter.not_set or
                            self.conf_req_rcvd.yfilter != YFilter.not_set or
                            self.conf_req_sent.yfilter != YFilter.not_set or
                            self.ncp_identifier.yfilter != YFilter.not_set or
                            self.proto_rej_rcvd.yfilter != YFilter.not_set or
                            self.proto_rej_sent.yfilter != YFilter.not_set or
                            self.term_ack_rcvd.yfilter != YFilter.not_set or
                            self.term_ack_sent.yfilter != YFilter.not_set or
                            self.term_req_rcvd.yfilter != YFilter.not_set or
                            self.term_req_sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ncp-statistics-array" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.conf_ack_rcvd.is_set or self.conf_ack_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_ack_rcvd.get_name_leafdata())
                        if (self.conf_ack_sent.is_set or self.conf_ack_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_ack_sent.get_name_leafdata())
                        if (self.conf_nak_rcvd.is_set or self.conf_nak_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_nak_rcvd.get_name_leafdata())
                        if (self.conf_nak_sent.is_set or self.conf_nak_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_nak_sent.get_name_leafdata())
                        if (self.conf_rej_rcvd.is_set or self.conf_rej_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_rej_rcvd.get_name_leafdata())
                        if (self.conf_rej_sent.is_set or self.conf_rej_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_rej_sent.get_name_leafdata())
                        if (self.conf_req_rcvd.is_set or self.conf_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_req_rcvd.get_name_leafdata())
                        if (self.conf_req_sent.is_set or self.conf_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conf_req_sent.get_name_leafdata())
                        if (self.ncp_identifier.is_set or self.ncp_identifier.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ncp_identifier.get_name_leafdata())
                        if (self.proto_rej_rcvd.is_set or self.proto_rej_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proto_rej_rcvd.get_name_leafdata())
                        if (self.proto_rej_sent.is_set or self.proto_rej_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proto_rej_sent.get_name_leafdata())
                        if (self.term_ack_rcvd.is_set or self.term_ack_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_ack_rcvd.get_name_leafdata())
                        if (self.term_ack_sent.is_set or self.term_ack_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_ack_sent.get_name_leafdata())
                        if (self.term_req_rcvd.is_set or self.term_req_rcvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_req_rcvd.get_name_leafdata())
                        if (self.term_req_sent.is_set or self.term_req_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.term_req_sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "conf-ack-rcvd" or name == "conf-ack-sent" or name == "conf-nak-rcvd" or name == "conf-nak-sent" or name == "conf-rej-rcvd" or name == "conf-rej-sent" or name == "conf-req-rcvd" or name == "conf-req-sent" or name == "ncp-identifier" or name == "proto-rej-rcvd" or name == "proto-rej-sent" or name == "term-ack-rcvd" or name == "term-ack-sent" or name == "term-req-rcvd" or name == "term-req-sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "conf-ack-rcvd"):
                            self.conf_ack_rcvd = value
                            self.conf_ack_rcvd.value_namespace = name_space
                            self.conf_ack_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-ack-sent"):
                            self.conf_ack_sent = value
                            self.conf_ack_sent.value_namespace = name_space
                            self.conf_ack_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-nak-rcvd"):
                            self.conf_nak_rcvd = value
                            self.conf_nak_rcvd.value_namespace = name_space
                            self.conf_nak_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-nak-sent"):
                            self.conf_nak_sent = value
                            self.conf_nak_sent.value_namespace = name_space
                            self.conf_nak_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-rej-rcvd"):
                            self.conf_rej_rcvd = value
                            self.conf_rej_rcvd.value_namespace = name_space
                            self.conf_rej_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-rej-sent"):
                            self.conf_rej_sent = value
                            self.conf_rej_sent.value_namespace = name_space
                            self.conf_rej_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-req-rcvd"):
                            self.conf_req_rcvd = value
                            self.conf_req_rcvd.value_namespace = name_space
                            self.conf_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "conf-req-sent"):
                            self.conf_req_sent = value
                            self.conf_req_sent.value_namespace = name_space
                            self.conf_req_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "ncp-identifier"):
                            self.ncp_identifier = value
                            self.ncp_identifier.value_namespace = name_space
                            self.ncp_identifier.value_namespace_prefix = name_space_prefix
                        if(value_path == "proto-rej-rcvd"):
                            self.proto_rej_rcvd = value
                            self.proto_rej_rcvd.value_namespace = name_space
                            self.proto_rej_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "proto-rej-sent"):
                            self.proto_rej_sent = value
                            self.proto_rej_sent.value_namespace = name_space
                            self.proto_rej_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-ack-rcvd"):
                            self.term_ack_rcvd = value
                            self.term_ack_rcvd.value_namespace = name_space
                            self.term_ack_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-ack-sent"):
                            self.term_ack_sent = value
                            self.term_ack_sent.value_namespace = name_space
                            self.term_ack_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-req-rcvd"):
                            self.term_req_rcvd = value
                            self.term_req_rcvd.value_namespace = name_space
                            self.term_req_rcvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "term-req-sent"):
                            self.term_req_sent = value
                            self.term_req_sent.value_namespace = name_space
                            self.term_req_sent.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ncp_statistics_array:
                        if (c.has_data()):
                            return True
                    return (
                        (self.authentication_statistics is not None and self.authentication_statistics.has_data()) or
                        (self.lcp_statistics is not None and self.lcp_statistics.has_data()))

                def has_operation(self):
                    for c in self.ncp_statistics_array:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.authentication_statistics is not None and self.authentication_statistics.has_operation()) or
                        (self.lcp_statistics is not None and self.lcp_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "authentication-statistics"):
                        if (self.authentication_statistics is None):
                            self.authentication_statistics = Ppp.Nodes.Node.Statistics.AuthenticationStatistics()
                            self.authentication_statistics.parent = self
                            self._children_name_map["authentication_statistics"] = "authentication-statistics"
                        return self.authentication_statistics

                    if (child_yang_name == "lcp-statistics"):
                        if (self.lcp_statistics is None):
                            self.lcp_statistics = Ppp.Nodes.Node.Statistics.LcpStatistics()
                            self.lcp_statistics.parent = self
                            self._children_name_map["lcp_statistics"] = "lcp-statistics"
                        return self.lcp_statistics

                    if (child_yang_name == "ncp-statistics-array"):
                        for c in self.ncp_statistics_array:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ppp.Nodes.Node.Statistics.NcpStatisticsArray()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ncp_statistics_array.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "authentication-statistics" or name == "lcp-statistics" or name == "ncp-statistics-array"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.node_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ppp.Nodes.Node.NodeInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ppp.Nodes.Node.NodeInterfaces, self).__setattr__(name, value)


                class NodeInterface(Entity):
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "caps_idb_srg_role",
                                        "ip_interworking_enabled",
                                        "is_l2ac",
                                        "is_lcp_delayed",
                                        "is_loopback_detected",
                                        "is_mcmp_enabled",
                                        "is_ssrp_configured",
                                        "is_tunneled_session",
                                        "keepalive_period",
                                        "keepalive_retry_count",
                                        "lcp_state",
                                        "lcpsso_state",
                                        "line_state",
                                        "local_ed",
                                        "local_mcmp_classes",
                                        "local_mrru",
                                        "local_mru",
                                        "parent_state",
                                        "peer_ed",
                                        "peer_mcmp_classes",
                                        "peer_mrru",
                                        "peer_mru",
                                        "provisioned",
                                        "session_expires",
                                        "session_srg_role",
                                        "ssrp_peer_id",
                                        "xconnect_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface, self).__setattr__(name, value)


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
                        	**type**\:   :py:class:`PppLcpMpMbrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_oper.PppLcpMpMbrState>`
                        
                        

                        """

                        _prefix = 'ppp-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo, self).__init__()

                            self.yang_name = "mp-info"
                            self.yang_parent_name = "node-interface"

                            self.active_links = YLeaf(YType.uint16, "active-links")

                            self.inactive_links = YLeaf(YType.uint16, "inactive-links")

                            self.is_mp_bundle = YLeaf(YType.boolean, "is-mp-bundle")

                            self.is_mp_bundle_member = YLeaf(YType.boolean, "is-mp-bundle-member")

                            self.minimum_active_links = YLeaf(YType.uint16, "minimum-active-links")

                            self.mp_bundle_interface = YLeaf(YType.str, "mp-bundle-interface")

                            self.mp_group = YLeaf(YType.uint32, "mp-group")

                            self.mp_state = YLeaf(YType.enumeration, "mp-state")

                            self.mp_member_info_array = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("active_links",
                                            "inactive_links",
                                            "is_mp_bundle",
                                            "is_mp_bundle_member",
                                            "minimum_active_links",
                                            "mp_bundle_interface",
                                            "mp_group",
                                            "mp_state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo, self).__setattr__(name, value)


                        class MpMemberInfoArray(Entity):
                            """
                            Array of MP members
                            
                            .. attribute:: interface
                            
                            	Member Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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

                                self.interface = YLeaf(YType.str, "interface")

                                self.state = YLeaf(YType.enumeration, "state")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface",
                                                "state") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface.is_set or
                                    self.state.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mp-member-info-array" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface" or name == "state"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.mp_member_info_array:
                                if (c.has_data()):
                                    return True
                            return (
                                self.active_links.is_set or
                                self.inactive_links.is_set or
                                self.is_mp_bundle.is_set or
                                self.is_mp_bundle_member.is_set or
                                self.minimum_active_links.is_set or
                                self.mp_bundle_interface.is_set or
                                self.mp_group.is_set or
                                self.mp_state.is_set)

                        def has_operation(self):
                            for c in self.mp_member_info_array:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.active_links.yfilter != YFilter.not_set or
                                self.inactive_links.yfilter != YFilter.not_set or
                                self.is_mp_bundle.yfilter != YFilter.not_set or
                                self.is_mp_bundle_member.yfilter != YFilter.not_set or
                                self.minimum_active_links.yfilter != YFilter.not_set or
                                self.mp_bundle_interface.yfilter != YFilter.not_set or
                                self.mp_group.yfilter != YFilter.not_set or
                                self.mp_state.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mp-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.active_links.is_set or self.active_links.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.active_links.get_name_leafdata())
                            if (self.inactive_links.is_set or self.inactive_links.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inactive_links.get_name_leafdata())
                            if (self.is_mp_bundle.is_set or self.is_mp_bundle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_mp_bundle.get_name_leafdata())
                            if (self.is_mp_bundle_member.is_set or self.is_mp_bundle_member.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_mp_bundle_member.get_name_leafdata())
                            if (self.minimum_active_links.is_set or self.minimum_active_links.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minimum_active_links.get_name_leafdata())
                            if (self.mp_bundle_interface.is_set or self.mp_bundle_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mp_bundle_interface.get_name_leafdata())
                            if (self.mp_group.is_set or self.mp_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mp_group.get_name_leafdata())
                            if (self.mp_state.is_set or self.mp_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mp_state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "mp-member-info-array"):
                                for c in self.mp_member_info_array:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo.MpMemberInfoArray()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.mp_member_info_array.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mp-member-info-array" or name == "active-links" or name == "inactive-links" or name == "is-mp-bundle" or name == "is-mp-bundle-member" or name == "minimum-active-links" or name == "mp-bundle-interface" or name == "mp-group" or name == "mp-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "active-links"):
                                self.active_links = value
                                self.active_links.value_namespace = name_space
                                self.active_links.value_namespace_prefix = name_space_prefix
                            if(value_path == "inactive-links"):
                                self.inactive_links = value
                                self.inactive_links.value_namespace = name_space
                                self.inactive_links.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-mp-bundle"):
                                self.is_mp_bundle = value
                                self.is_mp_bundle.value_namespace = name_space
                                self.is_mp_bundle.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-mp-bundle-member"):
                                self.is_mp_bundle_member = value
                                self.is_mp_bundle_member.value_namespace = name_space
                                self.is_mp_bundle_member.value_namespace_prefix = name_space_prefix
                            if(value_path == "minimum-active-links"):
                                self.minimum_active_links = value
                                self.minimum_active_links.value_namespace = name_space
                                self.minimum_active_links.value_namespace_prefix = name_space_prefix
                            if(value_path == "mp-bundle-interface"):
                                self.mp_bundle_interface = value
                                self.mp_bundle_interface.value_namespace = name_space
                                self.mp_bundle_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "mp-group"):
                                self.mp_group = value
                                self.mp_group.value_namespace = name_space
                                self.mp_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "mp-state"):
                                self.mp_state = value
                                self.mp_state.value_namespace = name_space
                                self.mp_state.value_namespace_prefix = name_space_prefix


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

                            self.minutes = YLeaf(YType.uint32, "minutes")

                            self.seconds = YLeaf(YType.uint8, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("minutes",
                                            "seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.minutes.is_set or
                                self.seconds.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.minutes.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "configured-timeout" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minutes.get_name_leafdata())
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "minutes" or name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "minutes"):
                                self.minutes = value
                                self.minutes.value_namespace = name_space
                                self.minutes.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix


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

                            self.is_authenticated = YLeaf(YType.boolean, "is-authenticated")

                            self.is_sso_authenticated = YLeaf(YType.boolean, "is-sso-authenticated")

                            self.of_peer_auth = YLeaf(YType.uint8, "of-peer-auth")

                            self.of_peer_name = YLeaf(YType.str, "of-peer-name")

                            self.of_peer_sso_state = YLeaf(YType.enumeration, "of-peer-sso-state")

                            self.of_us_auth = YLeaf(YType.uint8, "of-us-auth")

                            self.of_us_name = YLeaf(YType.str, "of-us-name")

                            self.of_us_sso_state = YLeaf(YType.enumeration, "of-us-sso-state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_authenticated",
                                            "is_sso_authenticated",
                                            "of_peer_auth",
                                            "of_peer_name",
                                            "of_peer_sso_state",
                                            "of_us_auth",
                                            "of_us_name",
                                            "of_us_sso_state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.is_authenticated.is_set or
                                self.is_sso_authenticated.is_set or
                                self.of_peer_auth.is_set or
                                self.of_peer_name.is_set or
                                self.of_peer_sso_state.is_set or
                                self.of_us_auth.is_set or
                                self.of_us_name.is_set or
                                self.of_us_sso_state.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_authenticated.yfilter != YFilter.not_set or
                                self.is_sso_authenticated.yfilter != YFilter.not_set or
                                self.of_peer_auth.yfilter != YFilter.not_set or
                                self.of_peer_name.yfilter != YFilter.not_set or
                                self.of_peer_sso_state.yfilter != YFilter.not_set or
                                self.of_us_auth.yfilter != YFilter.not_set or
                                self.of_us_name.yfilter != YFilter.not_set or
                                self.of_us_sso_state.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auth-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_authenticated.is_set or self.is_authenticated.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_authenticated.get_name_leafdata())
                            if (self.is_sso_authenticated.is_set or self.is_sso_authenticated.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_sso_authenticated.get_name_leafdata())
                            if (self.of_peer_auth.is_set or self.of_peer_auth.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_peer_auth.get_name_leafdata())
                            if (self.of_peer_name.is_set or self.of_peer_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_peer_name.get_name_leafdata())
                            if (self.of_peer_sso_state.is_set or self.of_peer_sso_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_peer_sso_state.get_name_leafdata())
                            if (self.of_us_auth.is_set or self.of_us_auth.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_us_auth.get_name_leafdata())
                            if (self.of_us_name.is_set or self.of_us_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_us_name.get_name_leafdata())
                            if (self.of_us_sso_state.is_set or self.of_us_sso_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.of_us_sso_state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "is-authenticated" or name == "is-sso-authenticated" or name == "of-peer-auth" or name == "of-peer-name" or name == "of-peer-sso-state" or name == "of-us-auth" or name == "of-us-name" or name == "of-us-sso-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-authenticated"):
                                self.is_authenticated = value
                                self.is_authenticated.value_namespace = name_space
                                self.is_authenticated.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-sso-authenticated"):
                                self.is_sso_authenticated = value
                                self.is_sso_authenticated.value_namespace = name_space
                                self.is_sso_authenticated.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-peer-auth"):
                                self.of_peer_auth = value
                                self.of_peer_auth.value_namespace = name_space
                                self.of_peer_auth.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-peer-name"):
                                self.of_peer_name = value
                                self.of_peer_name.value_namespace = name_space
                                self.of_peer_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-peer-sso-state"):
                                self.of_peer_sso_state = value
                                self.of_peer_sso_state.value_namespace = name_space
                                self.of_peer_sso_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-us-auth"):
                                self.of_us_auth = value
                                self.of_us_auth.value_namespace = name_space
                                self.of_us_auth.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-us-name"):
                                self.of_us_name = value
                                self.of_us_name.value_namespace = name_space
                                self.of_us_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "of-us-sso-state"):
                                self.of_us_sso_state = value
                                self.of_us_sso_state.value_namespace = name_space
                                self.of_us_sso_state.value_namespace_prefix = name_space_prefix


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

                            self.is_passive = YLeaf(YType.boolean, "is-passive")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                            self.ncp_state = YLeaf(YType.enumeration, "ncp-state")

                            self.ncpsso_state = YLeaf(YType.enumeration, "ncpsso-state")

                            self.ncp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo()
                            self.ncp_info.parent = self
                            self._children_name_map["ncp_info"] = "ncp-info"
                            self._children_yang_names.add("ncp-info")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_passive",
                                            "ncp_identifier",
                                            "ncp_state",
                                            "ncpsso_state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo, self).__setattr__(name, value)


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

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("dns_primary",
                                                    "dns_secondary",
                                                    "is_iphc_configured",
                                                    "local_address",
                                                    "peer_address",
                                                    "peer_netmask",
                                                    "wins_primary",
                                                    "wins_secondary") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo, self).__setattr__(name, value)


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

                                        self.compression_type = YLeaf(YType.enumeration, "compression-type")

                                        self.ec_rtp_compression = YLeaf(YType.boolean, "ec-rtp-compression")

                                        self.max_header = YLeaf(YType.uint16, "max-header")

                                        self.max_period = YLeaf(YType.uint16, "max-period")

                                        self.max_time = YLeaf(YType.uint16, "max-time")

                                        self.non_tcp_space = YLeaf(YType.uint16, "non-tcp-space")

                                        self.rtp_compression = YLeaf(YType.boolean, "rtp-compression")

                                        self.tcp_space = YLeaf(YType.uint16, "tcp-space")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("compression_type",
                                                        "ec_rtp_compression",
                                                        "max_header",
                                                        "max_period",
                                                        "max_time",
                                                        "non_tcp_space",
                                                        "rtp_compression",
                                                        "tcp_space") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.compression_type.is_set or
                                            self.ec_rtp_compression.is_set or
                                            self.max_header.is_set or
                                            self.max_period.is_set or
                                            self.max_time.is_set or
                                            self.non_tcp_space.is_set or
                                            self.rtp_compression.is_set or
                                            self.tcp_space.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.compression_type.yfilter != YFilter.not_set or
                                            self.ec_rtp_compression.yfilter != YFilter.not_set or
                                            self.max_header.yfilter != YFilter.not_set or
                                            self.max_period.yfilter != YFilter.not_set or
                                            self.max_time.yfilter != YFilter.not_set or
                                            self.non_tcp_space.yfilter != YFilter.not_set or
                                            self.rtp_compression.yfilter != YFilter.not_set or
                                            self.tcp_space.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "local-iphc-options" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.compression_type.is_set or self.compression_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.compression_type.get_name_leafdata())
                                        if (self.ec_rtp_compression.is_set or self.ec_rtp_compression.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ec_rtp_compression.get_name_leafdata())
                                        if (self.max_header.is_set or self.max_header.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_header.get_name_leafdata())
                                        if (self.max_period.is_set or self.max_period.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_period.get_name_leafdata())
                                        if (self.max_time.is_set or self.max_time.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_time.get_name_leafdata())
                                        if (self.non_tcp_space.is_set or self.non_tcp_space.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.non_tcp_space.get_name_leafdata())
                                        if (self.rtp_compression.is_set or self.rtp_compression.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rtp_compression.get_name_leafdata())
                                        if (self.tcp_space.is_set or self.tcp_space.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.tcp_space.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "compression-type" or name == "ec-rtp-compression" or name == "max-header" or name == "max-period" or name == "max-time" or name == "non-tcp-space" or name == "rtp-compression" or name == "tcp-space"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "compression-type"):
                                            self.compression_type = value
                                            self.compression_type.value_namespace = name_space
                                            self.compression_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ec-rtp-compression"):
                                            self.ec_rtp_compression = value
                                            self.ec_rtp_compression.value_namespace = name_space
                                            self.ec_rtp_compression.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-header"):
                                            self.max_header = value
                                            self.max_header.value_namespace = name_space
                                            self.max_header.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-period"):
                                            self.max_period = value
                                            self.max_period.value_namespace = name_space
                                            self.max_period.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-time"):
                                            self.max_time = value
                                            self.max_time.value_namespace = name_space
                                            self.max_time.value_namespace_prefix = name_space_prefix
                                        if(value_path == "non-tcp-space"):
                                            self.non_tcp_space = value
                                            self.non_tcp_space.value_namespace = name_space
                                            self.non_tcp_space.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rtp-compression"):
                                            self.rtp_compression = value
                                            self.rtp_compression.value_namespace = name_space
                                            self.rtp_compression.value_namespace_prefix = name_space_prefix
                                        if(value_path == "tcp-space"):
                                            self.tcp_space = value
                                            self.tcp_space.value_namespace = name_space
                                            self.tcp_space.value_namespace_prefix = name_space_prefix


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

                                        self.compression_type = YLeaf(YType.enumeration, "compression-type")

                                        self.ec_rtp_compression = YLeaf(YType.boolean, "ec-rtp-compression")

                                        self.max_header = YLeaf(YType.uint16, "max-header")

                                        self.max_period = YLeaf(YType.uint16, "max-period")

                                        self.max_time = YLeaf(YType.uint16, "max-time")

                                        self.non_tcp_space = YLeaf(YType.uint16, "non-tcp-space")

                                        self.rtp_compression = YLeaf(YType.boolean, "rtp-compression")

                                        self.tcp_space = YLeaf(YType.uint16, "tcp-space")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("compression_type",
                                                        "ec_rtp_compression",
                                                        "max_header",
                                                        "max_period",
                                                        "max_time",
                                                        "non_tcp_space",
                                                        "rtp_compression",
                                                        "tcp_space") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.compression_type.is_set or
                                            self.ec_rtp_compression.is_set or
                                            self.max_header.is_set or
                                            self.max_period.is_set or
                                            self.max_time.is_set or
                                            self.non_tcp_space.is_set or
                                            self.rtp_compression.is_set or
                                            self.tcp_space.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.compression_type.yfilter != YFilter.not_set or
                                            self.ec_rtp_compression.yfilter != YFilter.not_set or
                                            self.max_header.yfilter != YFilter.not_set or
                                            self.max_period.yfilter != YFilter.not_set or
                                            self.max_time.yfilter != YFilter.not_set or
                                            self.non_tcp_space.yfilter != YFilter.not_set or
                                            self.rtp_compression.yfilter != YFilter.not_set or
                                            self.tcp_space.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "peer-iphc-options" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.compression_type.is_set or self.compression_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.compression_type.get_name_leafdata())
                                        if (self.ec_rtp_compression.is_set or self.ec_rtp_compression.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ec_rtp_compression.get_name_leafdata())
                                        if (self.max_header.is_set or self.max_header.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_header.get_name_leafdata())
                                        if (self.max_period.is_set or self.max_period.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_period.get_name_leafdata())
                                        if (self.max_time.is_set or self.max_time.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.max_time.get_name_leafdata())
                                        if (self.non_tcp_space.is_set or self.non_tcp_space.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.non_tcp_space.get_name_leafdata())
                                        if (self.rtp_compression.is_set or self.rtp_compression.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rtp_compression.get_name_leafdata())
                                        if (self.tcp_space.is_set or self.tcp_space.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.tcp_space.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "compression-type" or name == "ec-rtp-compression" or name == "max-header" or name == "max-period" or name == "max-time" or name == "non-tcp-space" or name == "rtp-compression" or name == "tcp-space"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "compression-type"):
                                            self.compression_type = value
                                            self.compression_type.value_namespace = name_space
                                            self.compression_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ec-rtp-compression"):
                                            self.ec_rtp_compression = value
                                            self.ec_rtp_compression.value_namespace = name_space
                                            self.ec_rtp_compression.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-header"):
                                            self.max_header = value
                                            self.max_header.value_namespace = name_space
                                            self.max_header.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-period"):
                                            self.max_period = value
                                            self.max_period.value_namespace = name_space
                                            self.max_period.value_namespace_prefix = name_space_prefix
                                        if(value_path == "max-time"):
                                            self.max_time = value
                                            self.max_time.value_namespace = name_space
                                            self.max_time.value_namespace_prefix = name_space_prefix
                                        if(value_path == "non-tcp-space"):
                                            self.non_tcp_space = value
                                            self.non_tcp_space.value_namespace = name_space
                                            self.non_tcp_space.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rtp-compression"):
                                            self.rtp_compression = value
                                            self.rtp_compression.value_namespace = name_space
                                            self.rtp_compression.value_namespace_prefix = name_space_prefix
                                        if(value_path == "tcp-space"):
                                            self.tcp_space = value
                                            self.tcp_space.value_namespace = name_space
                                            self.tcp_space.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.dns_primary.is_set or
                                        self.dns_secondary.is_set or
                                        self.is_iphc_configured.is_set or
                                        self.local_address.is_set or
                                        self.peer_address.is_set or
                                        self.peer_netmask.is_set or
                                        self.wins_primary.is_set or
                                        self.wins_secondary.is_set or
                                        (self.local_iphc_options is not None and self.local_iphc_options.has_data()) or
                                        (self.peer_iphc_options is not None and self.peer_iphc_options.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.dns_primary.yfilter != YFilter.not_set or
                                        self.dns_secondary.yfilter != YFilter.not_set or
                                        self.is_iphc_configured.yfilter != YFilter.not_set or
                                        self.local_address.yfilter != YFilter.not_set or
                                        self.peer_address.yfilter != YFilter.not_set or
                                        self.peer_netmask.yfilter != YFilter.not_set or
                                        self.wins_primary.yfilter != YFilter.not_set or
                                        self.wins_secondary.yfilter != YFilter.not_set or
                                        (self.local_iphc_options is not None and self.local_iphc_options.has_operation()) or
                                        (self.peer_iphc_options is not None and self.peer_iphc_options.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipcp-info" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.dns_primary.is_set or self.dns_primary.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dns_primary.get_name_leafdata())
                                    if (self.dns_secondary.is_set or self.dns_secondary.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dns_secondary.get_name_leafdata())
                                    if (self.is_iphc_configured.is_set or self.is_iphc_configured.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_iphc_configured.get_name_leafdata())
                                    if (self.local_address.is_set or self.local_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_address.get_name_leafdata())
                                    if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peer_address.get_name_leafdata())
                                    if (self.peer_netmask.is_set or self.peer_netmask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peer_netmask.get_name_leafdata())
                                    if (self.wins_primary.is_set or self.wins_primary.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.wins_primary.get_name_leafdata())
                                    if (self.wins_secondary.is_set or self.wins_secondary.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.wins_secondary.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "local-iphc-options"):
                                        if (self.local_iphc_options is None):
                                            self.local_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.LocalIphcOptions()
                                            self.local_iphc_options.parent = self
                                            self._children_name_map["local_iphc_options"] = "local-iphc-options"
                                        return self.local_iphc_options

                                    if (child_yang_name == "peer-iphc-options"):
                                        if (self.peer_iphc_options is None):
                                            self.peer_iphc_options = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo.PeerIphcOptions()
                                            self.peer_iphc_options.parent = self
                                            self._children_name_map["peer_iphc_options"] = "peer-iphc-options"
                                        return self.peer_iphc_options

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "local-iphc-options" or name == "peer-iphc-options" or name == "dns-primary" or name == "dns-secondary" or name == "is-iphc-configured" or name == "local-address" or name == "peer-address" or name == "peer-netmask" or name == "wins-primary" or name == "wins-secondary"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "dns-primary"):
                                        self.dns_primary = value
                                        self.dns_primary.value_namespace = name_space
                                        self.dns_primary.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dns-secondary"):
                                        self.dns_secondary = value
                                        self.dns_secondary.value_namespace = name_space
                                        self.dns_secondary.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-iphc-configured"):
                                        self.is_iphc_configured = value
                                        self.is_iphc_configured.value_namespace = name_space
                                        self.is_iphc_configured.value_namespace_prefix = name_space_prefix
                                    if(value_path == "local-address"):
                                        self.local_address = value
                                        self.local_address.value_namespace = name_space
                                        self.local_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peer-address"):
                                        self.peer_address = value
                                        self.peer_address.value_namespace = name_space
                                        self.peer_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peer-netmask"):
                                        self.peer_netmask = value
                                        self.peer_netmask.value_namespace = name_space
                                        self.peer_netmask.value_namespace_prefix = name_space_prefix
                                    if(value_path == "wins-primary"):
                                        self.wins_primary = value
                                        self.wins_primary.value_namespace = name_space
                                        self.wins_primary.value_namespace_prefix = name_space_prefix
                                    if(value_path == "wins-secondary"):
                                        self.wins_secondary = value
                                        self.wins_secondary.value_namespace = name_space
                                        self.wins_secondary.value_namespace_prefix = name_space_prefix


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

                                    self.local_address = YLeaf(YType.str, "local-address")

                                    self.peer_address = YLeaf(YType.str, "peer-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("local_address",
                                                    "peer_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.local_address.is_set or
                                        self.peer_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.local_address.yfilter != YFilter.not_set or
                                        self.peer_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipcpiw-info" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.local_address.is_set or self.local_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_address.get_name_leafdata())
                                    if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peer_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "local-address" or name == "peer-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "local-address"):
                                        self.local_address = value
                                        self.local_address.value_namespace = name_space
                                        self.local_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peer-address"):
                                        self.peer_address = value
                                        self.peer_address.value_namespace = name_space
                                        self.peer_address.value_namespace_prefix = name_space_prefix


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

                                    self.local_address = YLeaf(YType.str, "local-address")

                                    self.peer_address = YLeaf(YType.str, "peer-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("local_address",
                                                    "peer_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.local_address.is_set or
                                        self.peer_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.local_address.yfilter != YFilter.not_set or
                                        self.peer_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv6cp-info" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.local_address.is_set or self.local_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_address.get_name_leafdata())
                                    if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peer_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "local-address" or name == "peer-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "local-address"):
                                        self.local_address = value
                                        self.local_address.value_namespace = name_space
                                        self.local_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peer-address"):
                                        self.peer_address = value
                                        self.peer_address.value_namespace = name_space
                                        self.peer_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.type.is_set or
                                    (self.ipcp_info is not None and self.ipcp_info.has_data()) or
                                    (self.ipcpiw_info is not None and self.ipcpiw_info.has_data()) or
                                    (self.ipv6cp_info is not None and self.ipv6cp_info.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    (self.ipcp_info is not None and self.ipcp_info.has_operation()) or
                                    (self.ipcpiw_info is not None and self.ipcpiw_info.has_operation()) or
                                    (self.ipv6cp_info is not None and self.ipv6cp_info.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ncp-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipcp-info"):
                                    if (self.ipcp_info is None):
                                        self.ipcp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpInfo()
                                        self.ipcp_info.parent = self
                                        self._children_name_map["ipcp_info"] = "ipcp-info"
                                    return self.ipcp_info

                                if (child_yang_name == "ipcpiw-info"):
                                    if (self.ipcpiw_info is None):
                                        self.ipcpiw_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.IpcpiwInfo()
                                        self.ipcpiw_info.parent = self
                                        self._children_name_map["ipcpiw_info"] = "ipcpiw-info"
                                    return self.ipcpiw_info

                                if (child_yang_name == "ipv6cp-info"):
                                    if (self.ipv6cp_info is None):
                                        self.ipv6cp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo.Ipv6CpInfo()
                                        self.ipv6cp_info.parent = self
                                        self._children_name_map["ipv6cp_info"] = "ipv6cp-info"
                                    return self.ipv6cp_info

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipcp-info" or name == "ipcpiw-info" or name == "ipv6cp-info" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.is_passive.is_set or
                                self.ncp_identifier.is_set or
                                self.ncp_state.is_set or
                                self.ncpsso_state.is_set or
                                (self.ncp_info is not None and self.ncp_info.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_passive.yfilter != YFilter.not_set or
                                self.ncp_identifier.yfilter != YFilter.not_set or
                                self.ncp_state.yfilter != YFilter.not_set or
                                self.ncpsso_state.yfilter != YFilter.not_set or
                                (self.ncp_info is not None and self.ncp_info.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ncp-info-array" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_passive.is_set or self.is_passive.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_passive.get_name_leafdata())
                            if (self.ncp_identifier.is_set or self.ncp_identifier.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ncp_identifier.get_name_leafdata())
                            if (self.ncp_state.is_set or self.ncp_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ncp_state.get_name_leafdata())
                            if (self.ncpsso_state.is_set or self.ncpsso_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ncpsso_state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ncp-info"):
                                if (self.ncp_info is None):
                                    self.ncp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray.NcpInfo()
                                    self.ncp_info.parent = self
                                    self._children_name_map["ncp_info"] = "ncp-info"
                                return self.ncp_info

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ncp-info" or name == "is-passive" or name == "ncp-identifier" or name == "ncp-state" or name == "ncpsso-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-passive"):
                                self.is_passive = value
                                self.is_passive.value_namespace = name_space
                                self.is_passive.value_namespace_prefix = name_space_prefix
                            if(value_path == "ncp-identifier"):
                                self.ncp_identifier = value
                                self.ncp_identifier.value_namespace = name_space
                                self.ncp_identifier.value_namespace_prefix = name_space_prefix
                            if(value_path == "ncp-state"):
                                self.ncp_state = value
                                self.ncp_state.value_namespace = name_space
                                self.ncp_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "ncpsso-state"):
                                self.ncpsso_state = value
                                self.ncpsso_state.value_namespace = name_space
                                self.ncpsso_state.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ncp_info_array:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface.is_set or
                            self.caps_idb_srg_role.is_set or
                            self.ip_interworking_enabled.is_set or
                            self.is_l2ac.is_set or
                            self.is_lcp_delayed.is_set or
                            self.is_loopback_detected.is_set or
                            self.is_mcmp_enabled.is_set or
                            self.is_ssrp_configured.is_set or
                            self.is_tunneled_session.is_set or
                            self.keepalive_period.is_set or
                            self.keepalive_retry_count.is_set or
                            self.lcp_state.is_set or
                            self.lcpsso_state.is_set or
                            self.line_state.is_set or
                            self.local_ed.is_set or
                            self.local_mcmp_classes.is_set or
                            self.local_mrru.is_set or
                            self.local_mru.is_set or
                            self.parent_state.is_set or
                            self.peer_ed.is_set or
                            self.peer_mcmp_classes.is_set or
                            self.peer_mrru.is_set or
                            self.peer_mru.is_set or
                            self.provisioned.is_set or
                            self.session_expires.is_set or
                            self.session_srg_role.is_set or
                            self.ssrp_peer_id.is_set or
                            self.xconnect_id.is_set or
                            (self.auth_info is not None and self.auth_info.has_data()) or
                            (self.configured_timeout is not None and self.configured_timeout.has_data()) or
                            (self.mp_info is not None and self.mp_info.has_data()))

                    def has_operation(self):
                        for c in self.ncp_info_array:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.caps_idb_srg_role.yfilter != YFilter.not_set or
                            self.ip_interworking_enabled.yfilter != YFilter.not_set or
                            self.is_l2ac.yfilter != YFilter.not_set or
                            self.is_lcp_delayed.yfilter != YFilter.not_set or
                            self.is_loopback_detected.yfilter != YFilter.not_set or
                            self.is_mcmp_enabled.yfilter != YFilter.not_set or
                            self.is_ssrp_configured.yfilter != YFilter.not_set or
                            self.is_tunneled_session.yfilter != YFilter.not_set or
                            self.keepalive_period.yfilter != YFilter.not_set or
                            self.keepalive_retry_count.yfilter != YFilter.not_set or
                            self.lcp_state.yfilter != YFilter.not_set or
                            self.lcpsso_state.yfilter != YFilter.not_set or
                            self.line_state.yfilter != YFilter.not_set or
                            self.local_ed.yfilter != YFilter.not_set or
                            self.local_mcmp_classes.yfilter != YFilter.not_set or
                            self.local_mrru.yfilter != YFilter.not_set or
                            self.local_mru.yfilter != YFilter.not_set or
                            self.parent_state.yfilter != YFilter.not_set or
                            self.peer_ed.yfilter != YFilter.not_set or
                            self.peer_mcmp_classes.yfilter != YFilter.not_set or
                            self.peer_mrru.yfilter != YFilter.not_set or
                            self.peer_mru.yfilter != YFilter.not_set or
                            self.provisioned.yfilter != YFilter.not_set or
                            self.session_expires.yfilter != YFilter.not_set or
                            self.session_srg_role.yfilter != YFilter.not_set or
                            self.ssrp_peer_id.yfilter != YFilter.not_set or
                            self.xconnect_id.yfilter != YFilter.not_set or
                            (self.auth_info is not None and self.auth_info.has_operation()) or
                            (self.configured_timeout is not None and self.configured_timeout.has_operation()) or
                            (self.mp_info is not None and self.mp_info.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node-interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.caps_idb_srg_role.is_set or self.caps_idb_srg_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.caps_idb_srg_role.get_name_leafdata())
                        if (self.ip_interworking_enabled.is_set or self.ip_interworking_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_interworking_enabled.get_name_leafdata())
                        if (self.is_l2ac.is_set or self.is_l2ac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_l2ac.get_name_leafdata())
                        if (self.is_lcp_delayed.is_set or self.is_lcp_delayed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_lcp_delayed.get_name_leafdata())
                        if (self.is_loopback_detected.is_set or self.is_loopback_detected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_loopback_detected.get_name_leafdata())
                        if (self.is_mcmp_enabled.is_set or self.is_mcmp_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_mcmp_enabled.get_name_leafdata())
                        if (self.is_ssrp_configured.is_set or self.is_ssrp_configured.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_ssrp_configured.get_name_leafdata())
                        if (self.is_tunneled_session.is_set or self.is_tunneled_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_tunneled_session.get_name_leafdata())
                        if (self.keepalive_period.is_set or self.keepalive_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keepalive_period.get_name_leafdata())
                        if (self.keepalive_retry_count.is_set or self.keepalive_retry_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keepalive_retry_count.get_name_leafdata())
                        if (self.lcp_state.is_set or self.lcp_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lcp_state.get_name_leafdata())
                        if (self.lcpsso_state.is_set or self.lcpsso_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lcpsso_state.get_name_leafdata())
                        if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.line_state.get_name_leafdata())
                        if (self.local_ed.is_set or self.local_ed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_ed.get_name_leafdata())
                        if (self.local_mcmp_classes.is_set or self.local_mcmp_classes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mcmp_classes.get_name_leafdata())
                        if (self.local_mrru.is_set or self.local_mrru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mrru.get_name_leafdata())
                        if (self.local_mru.is_set or self.local_mru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mru.get_name_leafdata())
                        if (self.parent_state.is_set or self.parent_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_state.get_name_leafdata())
                        if (self.peer_ed.is_set or self.peer_ed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_ed.get_name_leafdata())
                        if (self.peer_mcmp_classes.is_set or self.peer_mcmp_classes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mcmp_classes.get_name_leafdata())
                        if (self.peer_mrru.is_set or self.peer_mrru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mrru.get_name_leafdata())
                        if (self.peer_mru.is_set or self.peer_mru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mru.get_name_leafdata())
                        if (self.provisioned.is_set or self.provisioned.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.provisioned.get_name_leafdata())
                        if (self.session_expires.is_set or self.session_expires.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_expires.get_name_leafdata())
                        if (self.session_srg_role.is_set or self.session_srg_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_srg_role.get_name_leafdata())
                        if (self.ssrp_peer_id.is_set or self.ssrp_peer_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ssrp_peer_id.get_name_leafdata())
                        if (self.xconnect_id.is_set or self.xconnect_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.xconnect_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "auth-info"):
                            if (self.auth_info is None):
                                self.auth_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.AuthInfo()
                                self.auth_info.parent = self
                                self._children_name_map["auth_info"] = "auth-info"
                            return self.auth_info

                        if (child_yang_name == "configured-timeout"):
                            if (self.configured_timeout is None):
                                self.configured_timeout = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.ConfiguredTimeout()
                                self.configured_timeout.parent = self
                                self._children_name_map["configured_timeout"] = "configured-timeout"
                            return self.configured_timeout

                        if (child_yang_name == "mp-info"):
                            if (self.mp_info is None):
                                self.mp_info = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.MpInfo()
                                self.mp_info.parent = self
                                self._children_name_map["mp_info"] = "mp-info"
                            return self.mp_info

                        if (child_yang_name == "ncp-info-array"):
                            for c in self.ncp_info_array:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ppp.Nodes.Node.NodeInterfaces.NodeInterface.NcpInfoArray()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ncp_info_array.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auth-info" or name == "configured-timeout" or name == "mp-info" or name == "ncp-info-array" or name == "interface" or name == "caps-idb-srg-role" or name == "ip-interworking-enabled" or name == "is-l2ac" or name == "is-lcp-delayed" or name == "is-loopback-detected" or name == "is-mcmp-enabled" or name == "is-ssrp-configured" or name == "is-tunneled-session" or name == "keepalive-period" or name == "keepalive-retry-count" or name == "lcp-state" or name == "lcpsso-state" or name == "line-state" or name == "local-ed" or name == "local-mcmp-classes" or name == "local-mrru" or name == "local-mru" or name == "parent-state" or name == "peer-ed" or name == "peer-mcmp-classes" or name == "peer-mrru" or name == "peer-mru" or name == "provisioned" or name == "session-expires" or name == "session-srg-role" or name == "ssrp-peer-id" or name == "xconnect-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "caps-idb-srg-role"):
                            self.caps_idb_srg_role = value
                            self.caps_idb_srg_role.value_namespace = name_space
                            self.caps_idb_srg_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-interworking-enabled"):
                            self.ip_interworking_enabled = value
                            self.ip_interworking_enabled.value_namespace = name_space
                            self.ip_interworking_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-l2ac"):
                            self.is_l2ac = value
                            self.is_l2ac.value_namespace = name_space
                            self.is_l2ac.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-lcp-delayed"):
                            self.is_lcp_delayed = value
                            self.is_lcp_delayed.value_namespace = name_space
                            self.is_lcp_delayed.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-loopback-detected"):
                            self.is_loopback_detected = value
                            self.is_loopback_detected.value_namespace = name_space
                            self.is_loopback_detected.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-mcmp-enabled"):
                            self.is_mcmp_enabled = value
                            self.is_mcmp_enabled.value_namespace = name_space
                            self.is_mcmp_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-ssrp-configured"):
                            self.is_ssrp_configured = value
                            self.is_ssrp_configured.value_namespace = name_space
                            self.is_ssrp_configured.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-tunneled-session"):
                            self.is_tunneled_session = value
                            self.is_tunneled_session.value_namespace = name_space
                            self.is_tunneled_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "keepalive-period"):
                            self.keepalive_period = value
                            self.keepalive_period.value_namespace = name_space
                            self.keepalive_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "keepalive-retry-count"):
                            self.keepalive_retry_count = value
                            self.keepalive_retry_count.value_namespace = name_space
                            self.keepalive_retry_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "lcp-state"):
                            self.lcp_state = value
                            self.lcp_state.value_namespace = name_space
                            self.lcp_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "lcpsso-state"):
                            self.lcpsso_state = value
                            self.lcpsso_state.value_namespace = name_space
                            self.lcpsso_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "line-state"):
                            self.line_state = value
                            self.line_state.value_namespace = name_space
                            self.line_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-ed"):
                            self.local_ed = value
                            self.local_ed.value_namespace = name_space
                            self.local_ed.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mcmp-classes"):
                            self.local_mcmp_classes = value
                            self.local_mcmp_classes.value_namespace = name_space
                            self.local_mcmp_classes.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mrru"):
                            self.local_mrru = value
                            self.local_mrru.value_namespace = name_space
                            self.local_mrru.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mru"):
                            self.local_mru = value
                            self.local_mru.value_namespace = name_space
                            self.local_mru.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-state"):
                            self.parent_state = value
                            self.parent_state.value_namespace = name_space
                            self.parent_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-ed"):
                            self.peer_ed = value
                            self.peer_ed.value_namespace = name_space
                            self.peer_ed.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mcmp-classes"):
                            self.peer_mcmp_classes = value
                            self.peer_mcmp_classes.value_namespace = name_space
                            self.peer_mcmp_classes.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mrru"):
                            self.peer_mrru = value
                            self.peer_mrru.value_namespace = name_space
                            self.peer_mrru.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mru"):
                            self.peer_mru = value
                            self.peer_mru.value_namespace = name_space
                            self.peer_mru.value_namespace_prefix = name_space_prefix
                        if(value_path == "provisioned"):
                            self.provisioned = value
                            self.provisioned.value_namespace = name_space
                            self.provisioned.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-expires"):
                            self.session_expires = value
                            self.session_expires.value_namespace = name_space
                            self.session_expires.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-srg-role"):
                            self.session_srg_role = value
                            self.session_srg_role.value_namespace = name_space
                            self.session_srg_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "ssrp-peer-id"):
                            self.ssrp_peer_id = value
                            self.ssrp_peer_id.value_namespace = name_space
                            self.ssrp_peer_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "xconnect-id"):
                            self.xconnect_id = value
                            self.xconnect_id.value_namespace = name_space
                            self.xconnect_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.node_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.node_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "node-interface"):
                        for c in self.node_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ppp.Nodes.Node.NodeInterfaces.NodeInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.node_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.sso_alert = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ppp.Nodes.Node.SsoAlerts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ppp.Nodes.Node.SsoAlerts, self).__setattr__(name, value)


                class SsoAlert(Entity):
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
                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert, self).__init__()

                        self.yang_name = "sso-alert"
                        self.yang_parent_name = "sso-alerts"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoAlerts.SsoAlert, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoAlerts.SsoAlert, self).__setattr__(name, value)


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

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("context",
                                            "error",
                                            "is_error") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.context.is_set or
                                self.error.is_set or
                                self.is_error.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.context.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.is_error.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lcp-error" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.context.get_name_leafdata())
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.is_error.is_set or self.is_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_error.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context" or name == "error" or name == "is-error"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "context"):
                                self.context = value
                                self.context.value_namespace = name_space
                                self.context.value_namespace_prefix = name_space_prefix
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-error"):
                                self.is_error = value
                                self.is_error.value_namespace = name_space
                                self.is_error.value_namespace_prefix = name_space_prefix


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

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("context",
                                            "error",
                                            "is_error") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.context.is_set or
                                self.error.is_set or
                                self.is_error.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.context.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.is_error.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "of-us-auth-error" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.context.get_name_leafdata())
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.is_error.is_set or self.is_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_error.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context" or name == "error" or name == "is-error"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "context"):
                                self.context = value
                                self.context.value_namespace = name_space
                                self.context.value_namespace_prefix = name_space_prefix
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-error"):
                                self.is_error = value
                                self.is_error.value_namespace = name_space
                                self.is_error.value_namespace_prefix = name_space_prefix


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

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("context",
                                            "error",
                                            "is_error") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.context.is_set or
                                self.error.is_set or
                                self.is_error.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.context.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.is_error.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "of-peer-auth-error" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.context.get_name_leafdata())
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.is_error.is_set or self.is_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_error.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context" or name == "error" or name == "is-error"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "context"):
                                self.context = value
                                self.context.value_namespace = name_space
                                self.context.value_namespace_prefix = name_space_prefix
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-error"):
                                self.is_error = value
                                self.is_error.value_namespace = name_space
                                self.is_error.value_namespace_prefix = name_space_prefix


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

                            self.context = YLeaf(YType.uint32, "context")

                            self.error = YLeaf(YType.uint32, "error")

                            self.is_error = YLeaf(YType.boolean, "is-error")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("context",
                                            "error",
                                            "is_error") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.context.is_set or
                                self.error.is_set or
                                self.is_error.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.context.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.is_error.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipcp-error" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.context.get_name_leafdata())
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.is_error.is_set or self.is_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_error.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context" or name == "error" or name == "is-error"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "context"):
                                self.context = value
                                self.context.value_namespace = name_space
                                self.context.value_namespace_prefix = name_space_prefix
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-error"):
                                self.is_error = value
                                self.is_error.value_namespace = name_space
                                self.is_error.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            (self.ipcp_error is not None and self.ipcp_error.has_data()) or
                            (self.lcp_error is not None and self.lcp_error.has_data()) or
                            (self.of_peer_auth_error is not None and self.of_peer_auth_error.has_data()) or
                            (self.of_us_auth_error is not None and self.of_us_auth_error.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            (self.ipcp_error is not None and self.ipcp_error.has_operation()) or
                            (self.lcp_error is not None and self.lcp_error.has_operation()) or
                            (self.of_peer_auth_error is not None and self.of_peer_auth_error.has_operation()) or
                            (self.of_us_auth_error is not None and self.of_us_auth_error.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sso-alert" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipcp-error"):
                            if (self.ipcp_error is None):
                                self.ipcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.IpcpError()
                                self.ipcp_error.parent = self
                                self._children_name_map["ipcp_error"] = "ipcp-error"
                            return self.ipcp_error

                        if (child_yang_name == "lcp-error"):
                            if (self.lcp_error is None):
                                self.lcp_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.LcpError()
                                self.lcp_error.parent = self
                                self._children_name_map["lcp_error"] = "lcp-error"
                            return self.lcp_error

                        if (child_yang_name == "of-peer-auth-error"):
                            if (self.of_peer_auth_error is None):
                                self.of_peer_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfPeerAuthError()
                                self.of_peer_auth_error.parent = self
                                self._children_name_map["of_peer_auth_error"] = "of-peer-auth-error"
                            return self.of_peer_auth_error

                        if (child_yang_name == "of-us-auth-error"):
                            if (self.of_us_auth_error is None):
                                self.of_us_auth_error = Ppp.Nodes.Node.SsoAlerts.SsoAlert.OfUsAuthError()
                                self.of_us_auth_error.parent = self
                                self._children_name_map["of_us_auth_error"] = "of-us-auth-error"
                            return self.of_us_auth_error

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipcp-error" or name == "lcp-error" or name == "of-peer-auth-error" or name == "of-us-auth-error" or name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sso_alert:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sso_alert:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sso-alerts" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sso-alert"):
                        for c in self.sso_alert:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ppp.Nodes.Node.SsoAlerts.SsoAlert()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sso_alert.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sso-alert"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.node_interface_statistic = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ppp.Nodes.Node.NodeInterfaceStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ppp.Nodes.Node.NodeInterfaceStatistics, self).__setattr__(name, value)


                class NodeInterfaceStatistic(Entity):
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
                        super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic, self).__init__()

                        self.yang_name = "node-interface-statistic"
                        self.yang_parent_name = "node-interface-statistics"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("conf_ack_rcvd",
                                            "conf_ack_sent",
                                            "conf_nak_rcvd",
                                            "conf_nak_sent",
                                            "conf_rej_rcvd",
                                            "conf_rej_sent",
                                            "conf_req_rcvd",
                                            "conf_req_sent",
                                            "disc_req_rcvd",
                                            "disc_req_sent",
                                            "echo_rep_rcvd",
                                            "echo_rep_sent",
                                            "echo_req_rcvd",
                                            "echo_req_sent",
                                            "link_error",
                                            "link_up") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.conf_ack_rcvd.is_set or
                                self.conf_ack_sent.is_set or
                                self.conf_nak_rcvd.is_set or
                                self.conf_nak_sent.is_set or
                                self.conf_rej_rcvd.is_set or
                                self.conf_rej_sent.is_set or
                                self.conf_req_rcvd.is_set or
                                self.conf_req_sent.is_set or
                                self.disc_req_rcvd.is_set or
                                self.disc_req_sent.is_set or
                                self.echo_rep_rcvd.is_set or
                                self.echo_rep_sent.is_set or
                                self.echo_req_rcvd.is_set or
                                self.echo_req_sent.is_set or
                                self.link_error.is_set or
                                self.link_up.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.conf_ack_rcvd.yfilter != YFilter.not_set or
                                self.conf_ack_sent.yfilter != YFilter.not_set or
                                self.conf_nak_rcvd.yfilter != YFilter.not_set or
                                self.conf_nak_sent.yfilter != YFilter.not_set or
                                self.conf_rej_rcvd.yfilter != YFilter.not_set or
                                self.conf_rej_sent.yfilter != YFilter.not_set or
                                self.conf_req_rcvd.yfilter != YFilter.not_set or
                                self.conf_req_sent.yfilter != YFilter.not_set or
                                self.disc_req_rcvd.yfilter != YFilter.not_set or
                                self.disc_req_sent.yfilter != YFilter.not_set or
                                self.echo_rep_rcvd.yfilter != YFilter.not_set or
                                self.echo_rep_sent.yfilter != YFilter.not_set or
                                self.echo_req_rcvd.yfilter != YFilter.not_set or
                                self.echo_req_sent.yfilter != YFilter.not_set or
                                self.link_error.yfilter != YFilter.not_set or
                                self.link_up.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lcp-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.conf_ack_rcvd.is_set or self.conf_ack_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_ack_rcvd.get_name_leafdata())
                            if (self.conf_ack_sent.is_set or self.conf_ack_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_ack_sent.get_name_leafdata())
                            if (self.conf_nak_rcvd.is_set or self.conf_nak_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_nak_rcvd.get_name_leafdata())
                            if (self.conf_nak_sent.is_set or self.conf_nak_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_nak_sent.get_name_leafdata())
                            if (self.conf_rej_rcvd.is_set or self.conf_rej_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_rej_rcvd.get_name_leafdata())
                            if (self.conf_rej_sent.is_set or self.conf_rej_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_rej_sent.get_name_leafdata())
                            if (self.conf_req_rcvd.is_set or self.conf_req_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_req_rcvd.get_name_leafdata())
                            if (self.conf_req_sent.is_set or self.conf_req_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_req_sent.get_name_leafdata())
                            if (self.disc_req_rcvd.is_set or self.disc_req_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disc_req_rcvd.get_name_leafdata())
                            if (self.disc_req_sent.is_set or self.disc_req_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disc_req_sent.get_name_leafdata())
                            if (self.echo_rep_rcvd.is_set or self.echo_rep_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_rep_rcvd.get_name_leafdata())
                            if (self.echo_rep_sent.is_set or self.echo_rep_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_rep_sent.get_name_leafdata())
                            if (self.echo_req_rcvd.is_set or self.echo_req_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_req_rcvd.get_name_leafdata())
                            if (self.echo_req_sent.is_set or self.echo_req_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_req_sent.get_name_leafdata())
                            if (self.link_error.is_set or self.link_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.link_error.get_name_leafdata())
                            if (self.link_up.is_set or self.link_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.link_up.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "conf-ack-rcvd" or name == "conf-ack-sent" or name == "conf-nak-rcvd" or name == "conf-nak-sent" or name == "conf-rej-rcvd" or name == "conf-rej-sent" or name == "conf-req-rcvd" or name == "conf-req-sent" or name == "disc-req-rcvd" or name == "disc-req-sent" or name == "echo-rep-rcvd" or name == "echo-rep-sent" or name == "echo-req-rcvd" or name == "echo-req-sent" or name == "link-error" or name == "link-up"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "conf-ack-rcvd"):
                                self.conf_ack_rcvd = value
                                self.conf_ack_rcvd.value_namespace = name_space
                                self.conf_ack_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-ack-sent"):
                                self.conf_ack_sent = value
                                self.conf_ack_sent.value_namespace = name_space
                                self.conf_ack_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-nak-rcvd"):
                                self.conf_nak_rcvd = value
                                self.conf_nak_rcvd.value_namespace = name_space
                                self.conf_nak_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-nak-sent"):
                                self.conf_nak_sent = value
                                self.conf_nak_sent.value_namespace = name_space
                                self.conf_nak_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-rej-rcvd"):
                                self.conf_rej_rcvd = value
                                self.conf_rej_rcvd.value_namespace = name_space
                                self.conf_rej_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-rej-sent"):
                                self.conf_rej_sent = value
                                self.conf_rej_sent.value_namespace = name_space
                                self.conf_rej_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-req-rcvd"):
                                self.conf_req_rcvd = value
                                self.conf_req_rcvd.value_namespace = name_space
                                self.conf_req_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-req-sent"):
                                self.conf_req_sent = value
                                self.conf_req_sent.value_namespace = name_space
                                self.conf_req_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "disc-req-rcvd"):
                                self.disc_req_rcvd = value
                                self.disc_req_rcvd.value_namespace = name_space
                                self.disc_req_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "disc-req-sent"):
                                self.disc_req_sent = value
                                self.disc_req_sent.value_namespace = name_space
                                self.disc_req_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-rep-rcvd"):
                                self.echo_rep_rcvd = value
                                self.echo_rep_rcvd.value_namespace = name_space
                                self.echo_rep_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-rep-sent"):
                                self.echo_rep_sent = value
                                self.echo_rep_sent.value_namespace = name_space
                                self.echo_rep_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-req-rcvd"):
                                self.echo_req_rcvd = value
                                self.echo_req_rcvd.value_namespace = name_space
                                self.echo_req_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-req-sent"):
                                self.echo_req_sent = value
                                self.echo_req_sent.value_namespace = name_space
                                self.echo_req_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "link-error"):
                                self.link_error = value
                                self.link_error.value_namespace = name_space
                                self.link_error.value_namespace_prefix = name_space_prefix
                            if(value_path == "link-up"):
                                self.link_up = value
                                self.link_up.value_namespace = name_space
                                self.link_up.value_namespace_prefix = name_space_prefix


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("auth_timeout_count",
                                            "chap_chall_rcvd",
                                            "chap_chall_sent",
                                            "chap_rep_fail_rcvd",
                                            "chap_rep_fail_sent",
                                            "chap_rep_succ_rcvd",
                                            "chap_rep_succ_sent",
                                            "chap_resp_rcvd",
                                            "chap_resp_sent",
                                            "pap_ack_rcvd",
                                            "pap_ack_sent",
                                            "pap_nak_rcvd",
                                            "pap_nak_sent",
                                            "pap_req_rcvd",
                                            "pap_req_sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.auth_timeout_count.is_set or
                                self.chap_chall_rcvd.is_set or
                                self.chap_chall_sent.is_set or
                                self.chap_rep_fail_rcvd.is_set or
                                self.chap_rep_fail_sent.is_set or
                                self.chap_rep_succ_rcvd.is_set or
                                self.chap_rep_succ_sent.is_set or
                                self.chap_resp_rcvd.is_set or
                                self.chap_resp_sent.is_set or
                                self.pap_ack_rcvd.is_set or
                                self.pap_ack_sent.is_set or
                                self.pap_nak_rcvd.is_set or
                                self.pap_nak_sent.is_set or
                                self.pap_req_rcvd.is_set or
                                self.pap_req_sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.auth_timeout_count.yfilter != YFilter.not_set or
                                self.chap_chall_rcvd.yfilter != YFilter.not_set or
                                self.chap_chall_sent.yfilter != YFilter.not_set or
                                self.chap_rep_fail_rcvd.yfilter != YFilter.not_set or
                                self.chap_rep_fail_sent.yfilter != YFilter.not_set or
                                self.chap_rep_succ_rcvd.yfilter != YFilter.not_set or
                                self.chap_rep_succ_sent.yfilter != YFilter.not_set or
                                self.chap_resp_rcvd.yfilter != YFilter.not_set or
                                self.chap_resp_sent.yfilter != YFilter.not_set or
                                self.pap_ack_rcvd.yfilter != YFilter.not_set or
                                self.pap_ack_sent.yfilter != YFilter.not_set or
                                self.pap_nak_rcvd.yfilter != YFilter.not_set or
                                self.pap_nak_sent.yfilter != YFilter.not_set or
                                self.pap_req_rcvd.yfilter != YFilter.not_set or
                                self.pap_req_sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "authentication-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.auth_timeout_count.is_set or self.auth_timeout_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.auth_timeout_count.get_name_leafdata())
                            if (self.chap_chall_rcvd.is_set or self.chap_chall_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_chall_rcvd.get_name_leafdata())
                            if (self.chap_chall_sent.is_set or self.chap_chall_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_chall_sent.get_name_leafdata())
                            if (self.chap_rep_fail_rcvd.is_set or self.chap_rep_fail_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_rep_fail_rcvd.get_name_leafdata())
                            if (self.chap_rep_fail_sent.is_set or self.chap_rep_fail_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_rep_fail_sent.get_name_leafdata())
                            if (self.chap_rep_succ_rcvd.is_set or self.chap_rep_succ_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_rep_succ_rcvd.get_name_leafdata())
                            if (self.chap_rep_succ_sent.is_set or self.chap_rep_succ_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_rep_succ_sent.get_name_leafdata())
                            if (self.chap_resp_rcvd.is_set or self.chap_resp_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_resp_rcvd.get_name_leafdata())
                            if (self.chap_resp_sent.is_set or self.chap_resp_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_resp_sent.get_name_leafdata())
                            if (self.pap_ack_rcvd.is_set or self.pap_ack_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_ack_rcvd.get_name_leafdata())
                            if (self.pap_ack_sent.is_set or self.pap_ack_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_ack_sent.get_name_leafdata())
                            if (self.pap_nak_rcvd.is_set or self.pap_nak_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_nak_rcvd.get_name_leafdata())
                            if (self.pap_nak_sent.is_set or self.pap_nak_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_nak_sent.get_name_leafdata())
                            if (self.pap_req_rcvd.is_set or self.pap_req_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_req_rcvd.get_name_leafdata())
                            if (self.pap_req_sent.is_set or self.pap_req_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap_req_sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "auth-timeout-count" or name == "chap-chall-rcvd" or name == "chap-chall-sent" or name == "chap-rep-fail-rcvd" or name == "chap-rep-fail-sent" or name == "chap-rep-succ-rcvd" or name == "chap-rep-succ-sent" or name == "chap-resp-rcvd" or name == "chap-resp-sent" or name == "pap-ack-rcvd" or name == "pap-ack-sent" or name == "pap-nak-rcvd" or name == "pap-nak-sent" or name == "pap-req-rcvd" or name == "pap-req-sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "auth-timeout-count"):
                                self.auth_timeout_count = value
                                self.auth_timeout_count.value_namespace = name_space
                                self.auth_timeout_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-chall-rcvd"):
                                self.chap_chall_rcvd = value
                                self.chap_chall_rcvd.value_namespace = name_space
                                self.chap_chall_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-chall-sent"):
                                self.chap_chall_sent = value
                                self.chap_chall_sent.value_namespace = name_space
                                self.chap_chall_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-rep-fail-rcvd"):
                                self.chap_rep_fail_rcvd = value
                                self.chap_rep_fail_rcvd.value_namespace = name_space
                                self.chap_rep_fail_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-rep-fail-sent"):
                                self.chap_rep_fail_sent = value
                                self.chap_rep_fail_sent.value_namespace = name_space
                                self.chap_rep_fail_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-rep-succ-rcvd"):
                                self.chap_rep_succ_rcvd = value
                                self.chap_rep_succ_rcvd.value_namespace = name_space
                                self.chap_rep_succ_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-rep-succ-sent"):
                                self.chap_rep_succ_sent = value
                                self.chap_rep_succ_sent.value_namespace = name_space
                                self.chap_rep_succ_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-resp-rcvd"):
                                self.chap_resp_rcvd = value
                                self.chap_resp_rcvd.value_namespace = name_space
                                self.chap_resp_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "chap-resp-sent"):
                                self.chap_resp_sent = value
                                self.chap_resp_sent.value_namespace = name_space
                                self.chap_resp_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-ack-rcvd"):
                                self.pap_ack_rcvd = value
                                self.pap_ack_rcvd.value_namespace = name_space
                                self.pap_ack_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-ack-sent"):
                                self.pap_ack_sent = value
                                self.pap_ack_sent.value_namespace = name_space
                                self.pap_ack_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-nak-rcvd"):
                                self.pap_nak_rcvd = value
                                self.pap_nak_rcvd.value_namespace = name_space
                                self.pap_nak_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-nak-sent"):
                                self.pap_nak_sent = value
                                self.pap_nak_sent.value_namespace = name_space
                                self.pap_nak_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-req-rcvd"):
                                self.pap_req_rcvd = value
                                self.pap_req_rcvd.value_namespace = name_space
                                self.pap_req_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap-req-sent"):
                                self.pap_req_sent = value
                                self.pap_req_sent.value_namespace = name_space
                                self.pap_req_sent.value_namespace_prefix = name_space_prefix


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

                            self.conf_ack_rcvd = YLeaf(YType.uint16, "conf-ack-rcvd")

                            self.conf_ack_sent = YLeaf(YType.uint16, "conf-ack-sent")

                            self.conf_nak_rcvd = YLeaf(YType.uint16, "conf-nak-rcvd")

                            self.conf_nak_sent = YLeaf(YType.uint16, "conf-nak-sent")

                            self.conf_rej_rcvd = YLeaf(YType.uint16, "conf-rej-rcvd")

                            self.conf_rej_sent = YLeaf(YType.uint16, "conf-rej-sent")

                            self.conf_req_rcvd = YLeaf(YType.uint16, "conf-req-rcvd")

                            self.conf_req_sent = YLeaf(YType.uint16, "conf-req-sent")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("conf_ack_rcvd",
                                            "conf_ack_sent",
                                            "conf_nak_rcvd",
                                            "conf_nak_sent",
                                            "conf_rej_rcvd",
                                            "conf_rej_sent",
                                            "conf_req_rcvd",
                                            "conf_req_sent",
                                            "ncp_identifier") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.conf_ack_rcvd.is_set or
                                self.conf_ack_sent.is_set or
                                self.conf_nak_rcvd.is_set or
                                self.conf_nak_sent.is_set or
                                self.conf_rej_rcvd.is_set or
                                self.conf_rej_sent.is_set or
                                self.conf_req_rcvd.is_set or
                                self.conf_req_sent.is_set or
                                self.ncp_identifier.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.conf_ack_rcvd.yfilter != YFilter.not_set or
                                self.conf_ack_sent.yfilter != YFilter.not_set or
                                self.conf_nak_rcvd.yfilter != YFilter.not_set or
                                self.conf_nak_sent.yfilter != YFilter.not_set or
                                self.conf_rej_rcvd.yfilter != YFilter.not_set or
                                self.conf_rej_sent.yfilter != YFilter.not_set or
                                self.conf_req_rcvd.yfilter != YFilter.not_set or
                                self.conf_req_sent.yfilter != YFilter.not_set or
                                self.ncp_identifier.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ncp-statistics-array" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.conf_ack_rcvd.is_set or self.conf_ack_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_ack_rcvd.get_name_leafdata())
                            if (self.conf_ack_sent.is_set or self.conf_ack_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_ack_sent.get_name_leafdata())
                            if (self.conf_nak_rcvd.is_set or self.conf_nak_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_nak_rcvd.get_name_leafdata())
                            if (self.conf_nak_sent.is_set or self.conf_nak_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_nak_sent.get_name_leafdata())
                            if (self.conf_rej_rcvd.is_set or self.conf_rej_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_rej_rcvd.get_name_leafdata())
                            if (self.conf_rej_sent.is_set or self.conf_rej_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_rej_sent.get_name_leafdata())
                            if (self.conf_req_rcvd.is_set or self.conf_req_rcvd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_req_rcvd.get_name_leafdata())
                            if (self.conf_req_sent.is_set or self.conf_req_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.conf_req_sent.get_name_leafdata())
                            if (self.ncp_identifier.is_set or self.ncp_identifier.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ncp_identifier.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "conf-ack-rcvd" or name == "conf-ack-sent" or name == "conf-nak-rcvd" or name == "conf-nak-sent" or name == "conf-rej-rcvd" or name == "conf-rej-sent" or name == "conf-req-rcvd" or name == "conf-req-sent" or name == "ncp-identifier"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "conf-ack-rcvd"):
                                self.conf_ack_rcvd = value
                                self.conf_ack_rcvd.value_namespace = name_space
                                self.conf_ack_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-ack-sent"):
                                self.conf_ack_sent = value
                                self.conf_ack_sent.value_namespace = name_space
                                self.conf_ack_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-nak-rcvd"):
                                self.conf_nak_rcvd = value
                                self.conf_nak_rcvd.value_namespace = name_space
                                self.conf_nak_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-nak-sent"):
                                self.conf_nak_sent = value
                                self.conf_nak_sent.value_namespace = name_space
                                self.conf_nak_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-rej-rcvd"):
                                self.conf_rej_rcvd = value
                                self.conf_rej_rcvd.value_namespace = name_space
                                self.conf_rej_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-rej-sent"):
                                self.conf_rej_sent = value
                                self.conf_rej_sent.value_namespace = name_space
                                self.conf_rej_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-req-rcvd"):
                                self.conf_req_rcvd = value
                                self.conf_req_rcvd.value_namespace = name_space
                                self.conf_req_rcvd.value_namespace_prefix = name_space_prefix
                            if(value_path == "conf-req-sent"):
                                self.conf_req_sent = value
                                self.conf_req_sent.value_namespace = name_space
                                self.conf_req_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "ncp-identifier"):
                                self.ncp_identifier = value
                                self.ncp_identifier.value_namespace = name_space
                                self.ncp_identifier.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ncp_statistics_array:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            (self.authentication_statistics is not None and self.authentication_statistics.has_data()) or
                            (self.lcp_statistics is not None and self.lcp_statistics.has_data()))

                    def has_operation(self):
                        for c in self.ncp_statistics_array:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.authentication_statistics is not None and self.authentication_statistics.has_operation()) or
                            (self.lcp_statistics is not None and self.lcp_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node-interface-statistic" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "authentication-statistics"):
                            if (self.authentication_statistics is None):
                                self.authentication_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.AuthenticationStatistics()
                                self.authentication_statistics.parent = self
                                self._children_name_map["authentication_statistics"] = "authentication-statistics"
                            return self.authentication_statistics

                        if (child_yang_name == "lcp-statistics"):
                            if (self.lcp_statistics is None):
                                self.lcp_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.LcpStatistics()
                                self.lcp_statistics.parent = self
                                self._children_name_map["lcp_statistics"] = "lcp-statistics"
                            return self.lcp_statistics

                        if (child_yang_name == "ncp-statistics-array"):
                            for c in self.ncp_statistics_array:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic.NcpStatisticsArray()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ncp_statistics_array.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authentication-statistics" or name == "lcp-statistics" or name == "ncp-statistics-array" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.node_interface_statistic:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.node_interface_statistic:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node-interface-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "node-interface-statistic"):
                        for c in self.node_interface_statistic:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ppp.Nodes.Node.NodeInterfaceStatistics.NodeInterfaceStatistic()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.node_interface_statistic.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node-interface-statistic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoSummary.LcpStates, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoSummary.LcpStates, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.total.is_set

                    def has_operation(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lcp-states" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        leaf_name_data.extend(self.count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count.append(value)
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix


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

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoSummary.OfUsAuthStates, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoSummary.OfUsAuthStates, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.total.is_set

                    def has_operation(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "of-us-auth-states" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        leaf_name_data.extend(self.count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count.append(value)
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix


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

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.total.is_set

                    def has_operation(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "of-peer-auth-states" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        leaf_name_data.extend(self.count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count.append(value)
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix


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

                        self.count = YLeafList(YType.uint16, "count")

                        self.total = YLeaf(YType.uint16, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoSummary.IpcpStates, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoSummary.IpcpStates, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.total.is_set

                    def has_operation(self):
                        for leaf in self.count.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipcp-states" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        leaf_name_data.extend(self.count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count.append(value)
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.ipcp_states is not None and self.ipcp_states.has_data()) or
                        (self.lcp_states is not None and self.lcp_states.has_data()) or
                        (self.of_peer_auth_states is not None and self.of_peer_auth_states.has_data()) or
                        (self.of_us_auth_states is not None and self.of_us_auth_states.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipcp_states is not None and self.ipcp_states.has_operation()) or
                        (self.lcp_states is not None and self.lcp_states.has_operation()) or
                        (self.of_peer_auth_states is not None and self.of_peer_auth_states.has_operation()) or
                        (self.of_us_auth_states is not None and self.of_us_auth_states.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sso-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipcp-states"):
                        if (self.ipcp_states is None):
                            self.ipcp_states = Ppp.Nodes.Node.SsoSummary.IpcpStates()
                            self.ipcp_states.parent = self
                            self._children_name_map["ipcp_states"] = "ipcp-states"
                        return self.ipcp_states

                    if (child_yang_name == "lcp-states"):
                        if (self.lcp_states is None):
                            self.lcp_states = Ppp.Nodes.Node.SsoSummary.LcpStates()
                            self.lcp_states.parent = self
                            self._children_name_map["lcp_states"] = "lcp-states"
                        return self.lcp_states

                    if (child_yang_name == "of-peer-auth-states"):
                        if (self.of_peer_auth_states is None):
                            self.of_peer_auth_states = Ppp.Nodes.Node.SsoSummary.OfPeerAuthStates()
                            self.of_peer_auth_states.parent = self
                            self._children_name_map["of_peer_auth_states"] = "of-peer-auth-states"
                        return self.of_peer_auth_states

                    if (child_yang_name == "of-us-auth-states"):
                        if (self.of_us_auth_states is None):
                            self.of_us_auth_states = Ppp.Nodes.Node.SsoSummary.OfUsAuthStates()
                            self.of_us_auth_states.parent = self
                            self._children_name_map["of_us_auth_states"] = "of-us-auth-states"
                        return self.of_us_auth_states

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipcp-states" or name == "lcp-states" or name == "of-peer-auth-states" or name == "of-us-auth-states"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.sso_group = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ppp.Nodes.Node.SsoGroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ppp.Nodes.Node.SsoGroups, self).__setattr__(name, value)


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

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.sso_states = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates()
                        self.sso_states.parent = self
                        self._children_name_map["sso_states"] = "sso-states"
                        self._children_yang_names.add("sso-states")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup, self).__setattr__(name, value)


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

                            self.sso_state = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates, self).__setattr__(name, value)


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
                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState, self).__init__()

                                self.yang_name = "sso-state"
                                self.yang_parent_name = "sso-states"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("session_id",
                                                "interface",
                                                "session_id_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState, self).__setattr__(name, value)


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

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("is_running",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.is_running.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.is_running.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "lcp-state" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.is_running.is_set or self.is_running.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_running.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "is-running" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "is-running"):
                                        self.is_running = value
                                        self.is_running.value_namespace = name_space
                                        self.is_running.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix


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

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("is_running",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.is_running.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.is_running.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "of-us-auth-state" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.is_running.is_set or self.is_running.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_running.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "is-running" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "is-running"):
                                        self.is_running = value
                                        self.is_running.value_namespace = name_space
                                        self.is_running.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix


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

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("is_running",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.is_running.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.is_running.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "of-peer-auth-state" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.is_running.is_set or self.is_running.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_running.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "is-running" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "is-running"):
                                        self.is_running = value
                                        self.is_running.value_namespace = name_space
                                        self.is_running.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix


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

                                    self.is_running = YLeaf(YType.boolean, "is-running")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("is_running",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.is_running.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.is_running.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipcp-state" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.is_running.is_set or self.is_running.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_running.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "is-running" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "is-running"):
                                        self.is_running = value
                                        self.is_running.value_namespace = name_space
                                        self.is_running.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.session_id.is_set or
                                    self.interface.is_set or
                                    self.session_id_xr.is_set or
                                    (self.ipcp_state is not None and self.ipcp_state.has_data()) or
                                    (self.lcp_state is not None and self.lcp_state.has_data()) or
                                    (self.of_peer_auth_state is not None and self.of_peer_auth_state.has_data()) or
                                    (self.of_us_auth_state is not None and self.of_us_auth_state.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.session_id.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.session_id_xr.yfilter != YFilter.not_set or
                                    (self.ipcp_state is not None and self.ipcp_state.has_operation()) or
                                    (self.lcp_state is not None and self.lcp_state.has_operation()) or
                                    (self.of_peer_auth_state is not None and self.of_peer_auth_state.has_operation()) or
                                    (self.of_us_auth_state is not None and self.of_us_auth_state.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sso-state" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_id.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.session_id_xr.is_set or self.session_id_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_id_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipcp-state"):
                                    if (self.ipcp_state is None):
                                        self.ipcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.IpcpState()
                                        self.ipcp_state.parent = self
                                        self._children_name_map["ipcp_state"] = "ipcp-state"
                                    return self.ipcp_state

                                if (child_yang_name == "lcp-state"):
                                    if (self.lcp_state is None):
                                        self.lcp_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.LcpState()
                                        self.lcp_state.parent = self
                                        self._children_name_map["lcp_state"] = "lcp-state"
                                    return self.lcp_state

                                if (child_yang_name == "of-peer-auth-state"):
                                    if (self.of_peer_auth_state is None):
                                        self.of_peer_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfPeerAuthState()
                                        self.of_peer_auth_state.parent = self
                                        self._children_name_map["of_peer_auth_state"] = "of-peer-auth-state"
                                    return self.of_peer_auth_state

                                if (child_yang_name == "of-us-auth-state"):
                                    if (self.of_us_auth_state is None):
                                        self.of_us_auth_state = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState.OfUsAuthState()
                                        self.of_us_auth_state.parent = self
                                        self._children_name_map["of_us_auth_state"] = "of-us-auth-state"
                                    return self.of_us_auth_state

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipcp-state" or name == "lcp-state" or name == "of-peer-auth-state" or name == "of-us-auth-state" or name == "session-id" or name == "interface" or name == "session-id-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "session-id"):
                                    self.session_id = value
                                    self.session_id.value_namespace = name_space
                                    self.session_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-id-xr"):
                                    self.session_id_xr = value
                                    self.session_id_xr.value_namespace = name_space
                                    self.session_id_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sso_state:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sso_state:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sso-states" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sso-state"):
                                for c in self.sso_state:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates.SsoState()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sso_state.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sso-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.group_id.is_set or
                            (self.sso_states is not None and self.sso_states.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            (self.sso_states is not None and self.sso_states.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sso-group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sso-states"):
                            if (self.sso_states is None):
                                self.sso_states = Ppp.Nodes.Node.SsoGroups.SsoGroup.SsoStates()
                                self.sso_states.parent = self
                                self._children_name_map["sso_states"] = "sso-states"
                            return self.sso_states

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sso-states" or name == "group-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sso_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sso_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sso-groups" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sso-group"):
                        for c in self.sso_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ppp.Nodes.Node.SsoGroups.SsoGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sso_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sso-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                        self.gcc0_count = YLeaf(YType.uint32, "gcc0-count")

                        self.gcc1_count = YLeaf(YType.uint32, "gcc1-count")

                        self.multilink_bundle_count = YLeaf(YType.uint32, "multilink-bundle-count")

                        self.pos_count = YLeaf(YType.uint32, "pos-count")

                        self.pppoe_count = YLeaf(YType.uint32, "pppoe-count")

                        self.serial_count = YLeaf(YType.uint32, "serial-count")

                        self.total = YLeaf(YType.uint32, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("gcc0_count",
                                        "gcc1_count",
                                        "multilink_bundle_count",
                                        "pos_count",
                                        "pppoe_count",
                                        "serial_count",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Summary.Intfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Summary.Intfs, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.gcc0_count.is_set or
                            self.gcc1_count.is_set or
                            self.multilink_bundle_count.is_set or
                            self.pos_count.is_set or
                            self.pppoe_count.is_set or
                            self.serial_count.is_set or
                            self.total.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.gcc0_count.yfilter != YFilter.not_set or
                            self.gcc1_count.yfilter != YFilter.not_set or
                            self.multilink_bundle_count.yfilter != YFilter.not_set or
                            self.pos_count.yfilter != YFilter.not_set or
                            self.pppoe_count.yfilter != YFilter.not_set or
                            self.serial_count.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "intfs" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.gcc0_count.is_set or self.gcc0_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.gcc0_count.get_name_leafdata())
                        if (self.gcc1_count.is_set or self.gcc1_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.gcc1_count.get_name_leafdata())
                        if (self.multilink_bundle_count.is_set or self.multilink_bundle_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multilink_bundle_count.get_name_leafdata())
                        if (self.pos_count.is_set or self.pos_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pos_count.get_name_leafdata())
                        if (self.pppoe_count.is_set or self.pppoe_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pppoe_count.get_name_leafdata())
                        if (self.serial_count.is_set or self.serial_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.serial_count.get_name_leafdata())
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "gcc0-count" or name == "gcc1-count" or name == "multilink-bundle-count" or name == "pos-count" or name == "pppoe-count" or name == "serial-count" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "gcc0-count"):
                            self.gcc0_count = value
                            self.gcc0_count.value_namespace = name_space
                            self.gcc0_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "gcc1-count"):
                            self.gcc1_count = value
                            self.gcc1_count.value_namespace = name_space
                            self.gcc1_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "multilink-bundle-count"):
                            self.multilink_bundle_count = value
                            self.multilink_bundle_count.value_namespace = name_space
                            self.multilink_bundle_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "pos-count"):
                            self.pos_count = value
                            self.pos_count.value_namespace = name_space
                            self.pos_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "pppoe-count"):
                            self.pppoe_count = value
                            self.pppoe_count.value_namespace = name_space
                            self.pppoe_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "serial-count"):
                            self.serial_count = value
                            self.serial_count.value_namespace = name_space
                            self.serial_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix


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

                        self.lcpfsm_states = Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates()
                        self.lcpfsm_states.parent = self
                        self._children_name_map["lcpfsm_states"] = "lcpfsm-states"
                        self._children_yang_names.add("lcpfsm-states")

                        self.ncpfsm_states_array = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Summary.FsmStates, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Summary.FsmStates, self).__setattr__(name, value)


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

                            self.count = YLeafList(YType.uint32, "count")

                            self.total = YLeaf(YType.uint32, "total")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("count",
                                            "total") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.count.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.total.is_set

                        def has_operation(self):
                            for leaf in self.count.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.count.yfilter != YFilter.not_set or
                                self.total.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lcpfsm-states" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total.get_name_leafdata())

                            leaf_name_data.extend(self.count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "count" or name == "total"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "count"):
                                self.count.append(value)
                            if(value_path == "total"):
                                self.total = value
                                self.total.value_namespace = name_space
                                self.total.value_namespace_prefix = name_space_prefix


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

                            self.count = YLeafList(YType.uint32, "count")

                            self.ncp_identifier = YLeaf(YType.enumeration, "ncp-identifier")

                            self.total = YLeaf(YType.uint32, "total")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("count",
                                            "ncp_identifier",
                                            "total") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.count.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return (
                                self.ncp_identifier.is_set or
                                self.total.is_set)

                        def has_operation(self):
                            for leaf in self.count.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.count.yfilter != YFilter.not_set or
                                self.ncp_identifier.yfilter != YFilter.not_set or
                                self.total.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ncpfsm-states-array" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ncp_identifier.is_set or self.ncp_identifier.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ncp_identifier.get_name_leafdata())
                            if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total.get_name_leafdata())

                            leaf_name_data.extend(self.count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "count" or name == "ncp-identifier" or name == "total"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "count"):
                                self.count.append(value)
                            if(value_path == "ncp-identifier"):
                                self.ncp_identifier = value
                                self.ncp_identifier.value_namespace = name_space
                                self.ncp_identifier.value_namespace_prefix = name_space_prefix
                            if(value_path == "total"):
                                self.total = value
                                self.total.value_namespace = name_space
                                self.total.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ncpfsm_states_array:
                            if (c.has_data()):
                                return True
                        return (self.lcpfsm_states is not None and self.lcpfsm_states.has_data())

                    def has_operation(self):
                        for c in self.ncpfsm_states_array:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.lcpfsm_states is not None and self.lcpfsm_states.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fsm-states" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "lcpfsm-states"):
                            if (self.lcpfsm_states is None):
                                self.lcpfsm_states = Ppp.Nodes.Node.Summary.FsmStates.LcpfsmStates()
                                self.lcpfsm_states.parent = self
                                self._children_name_map["lcpfsm_states"] = "lcpfsm-states"
                            return self.lcpfsm_states

                        if (child_yang_name == "ncpfsm-states-array"):
                            for c in self.ncpfsm_states_array:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ppp.Nodes.Node.Summary.FsmStates.NcpfsmStatesArray()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ncpfsm_states_array.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lcpfsm-states" or name == "ncpfsm-states-array"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.authenticating = YLeaf(YType.uint32, "authenticating")

                        self.lcp_not_negotiated = YLeaf(YType.uint32, "lcp-not-negotiated")

                        self.line_held_down = YLeaf(YType.uint32, "line-held-down")

                        self.up_l2_fwded = YLeaf(YType.uint32, "up-l2-fwded")

                        self.up_local_term = YLeaf(YType.uint32, "up-local-term")

                        self.up_tunneled = YLeaf(YType.uint32, "up-tunneled")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("authenticating",
                                        "lcp_not_negotiated",
                                        "line_held_down",
                                        "up_l2_fwded",
                                        "up_local_term",
                                        "up_tunneled") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ppp.Nodes.Node.Summary.LcpAuthPhases, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ppp.Nodes.Node.Summary.LcpAuthPhases, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.authenticating.is_set or
                            self.lcp_not_negotiated.is_set or
                            self.line_held_down.is_set or
                            self.up_l2_fwded.is_set or
                            self.up_local_term.is_set or
                            self.up_tunneled.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.authenticating.yfilter != YFilter.not_set or
                            self.lcp_not_negotiated.yfilter != YFilter.not_set or
                            self.line_held_down.yfilter != YFilter.not_set or
                            self.up_l2_fwded.yfilter != YFilter.not_set or
                            self.up_local_term.yfilter != YFilter.not_set or
                            self.up_tunneled.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lcp-auth-phases" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.authenticating.is_set or self.authenticating.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.authenticating.get_name_leafdata())
                        if (self.lcp_not_negotiated.is_set or self.lcp_not_negotiated.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lcp_not_negotiated.get_name_leafdata())
                        if (self.line_held_down.is_set or self.line_held_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.line_held_down.get_name_leafdata())
                        if (self.up_l2_fwded.is_set or self.up_l2_fwded.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_l2_fwded.get_name_leafdata())
                        if (self.up_local_term.is_set or self.up_local_term.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_local_term.get_name_leafdata())
                        if (self.up_tunneled.is_set or self.up_tunneled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_tunneled.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authenticating" or name == "lcp-not-negotiated" or name == "line-held-down" or name == "up-l2-fwded" or name == "up-local-term" or name == "up-tunneled"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "authenticating"):
                            self.authenticating = value
                            self.authenticating.value_namespace = name_space
                            self.authenticating.value_namespace_prefix = name_space_prefix
                        if(value_path == "lcp-not-negotiated"):
                            self.lcp_not_negotiated = value
                            self.lcp_not_negotiated.value_namespace = name_space
                            self.lcp_not_negotiated.value_namespace_prefix = name_space_prefix
                        if(value_path == "line-held-down"):
                            self.line_held_down = value
                            self.line_held_down.value_namespace = name_space
                            self.line_held_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-l2-fwded"):
                            self.up_l2_fwded = value
                            self.up_l2_fwded.value_namespace = name_space
                            self.up_l2_fwded.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-local-term"):
                            self.up_local_term = value
                            self.up_local_term.value_namespace = name_space
                            self.up_local_term.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-tunneled"):
                            self.up_tunneled = value
                            self.up_tunneled.value_namespace = name_space
                            self.up_tunneled.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.fsm_states is not None and self.fsm_states.has_data()) or
                        (self.intfs is not None and self.intfs.has_data()) or
                        (self.lcp_auth_phases is not None and self.lcp_auth_phases.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.fsm_states is not None and self.fsm_states.has_operation()) or
                        (self.intfs is not None and self.intfs.has_operation()) or
                        (self.lcp_auth_phases is not None and self.lcp_auth_phases.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fsm-states"):
                        if (self.fsm_states is None):
                            self.fsm_states = Ppp.Nodes.Node.Summary.FsmStates()
                            self.fsm_states.parent = self
                            self._children_name_map["fsm_states"] = "fsm-states"
                        return self.fsm_states

                    if (child_yang_name == "intfs"):
                        if (self.intfs is None):
                            self.intfs = Ppp.Nodes.Node.Summary.Intfs()
                            self.intfs.parent = self
                            self._children_name_map["intfs"] = "intfs"
                        return self.intfs

                    if (child_yang_name == "lcp-auth-phases"):
                        if (self.lcp_auth_phases is None):
                            self.lcp_auth_phases = Ppp.Nodes.Node.Summary.LcpAuthPhases()
                            self.lcp_auth_phases.parent = self
                            self._children_name_map["lcp_auth_phases"] = "lcp-auth-phases"
                        return self.lcp_auth_phases

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fsm-states" or name == "intfs" or name == "lcp-auth-phases"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.node_interface_statistics is not None and self.node_interface_statistics.has_data()) or
                    (self.node_interfaces is not None and self.node_interfaces.has_data()) or
                    (self.sso_alerts is not None and self.sso_alerts.has_data()) or
                    (self.sso_groups is not None and self.sso_groups.has_data()) or
                    (self.sso_summary is not None and self.sso_summary.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.node_interface_statistics is not None and self.node_interface_statistics.has_operation()) or
                    (self.node_interfaces is not None and self.node_interfaces.has_operation()) or
                    (self.sso_alerts is not None and self.sso_alerts.has_operation()) or
                    (self.sso_groups is not None and self.sso_groups.has_operation()) or
                    (self.sso_summary is not None and self.sso_summary.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ppp-ma-oper:ppp/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node-interface-statistics"):
                    if (self.node_interface_statistics is None):
                        self.node_interface_statistics = Ppp.Nodes.Node.NodeInterfaceStatistics()
                        self.node_interface_statistics.parent = self
                        self._children_name_map["node_interface_statistics"] = "node-interface-statistics"
                    return self.node_interface_statistics

                if (child_yang_name == "node-interfaces"):
                    if (self.node_interfaces is None):
                        self.node_interfaces = Ppp.Nodes.Node.NodeInterfaces()
                        self.node_interfaces.parent = self
                        self._children_name_map["node_interfaces"] = "node-interfaces"
                    return self.node_interfaces

                if (child_yang_name == "sso-alerts"):
                    if (self.sso_alerts is None):
                        self.sso_alerts = Ppp.Nodes.Node.SsoAlerts()
                        self.sso_alerts.parent = self
                        self._children_name_map["sso_alerts"] = "sso-alerts"
                    return self.sso_alerts

                if (child_yang_name == "sso-groups"):
                    if (self.sso_groups is None):
                        self.sso_groups = Ppp.Nodes.Node.SsoGroups()
                        self.sso_groups.parent = self
                        self._children_name_map["sso_groups"] = "sso-groups"
                    return self.sso_groups

                if (child_yang_name == "sso-summary"):
                    if (self.sso_summary is None):
                        self.sso_summary = Ppp.Nodes.Node.SsoSummary()
                        self.sso_summary.parent = self
                        self._children_name_map["sso_summary"] = "sso-summary"
                    return self.sso_summary

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Ppp.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = Ppp.Nodes.Node.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node-interface-statistics" or name == "node-interfaces" or name == "sso-alerts" or name == "sso-groups" or name == "sso-summary" or name == "statistics" or name == "summary" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ppp-ma-oper:ppp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ppp.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ppp-ma-oper:ppp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Ppp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ppp()
        return self._top_entity

