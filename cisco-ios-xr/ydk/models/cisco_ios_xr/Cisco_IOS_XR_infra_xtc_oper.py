""" Cisco_IOS_XR_infra_xtc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package operational data.

This module contains definitions
for the following management objects\:
  pce\-lsp\-data\: PCE LSP's data
  pce\-peer\: pce peer
  pce\-topology\: pce topology
  pce\: pce

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LspSetupEnum(Enum):
    """
    LspSetupEnum

    LSP setup type

    .. data:: setup_rsvp = 0

    	LSP is established using RSVP-TE

    .. data:: setup_sr = 1

    	LSP is established using SR-TE

    .. data:: setup_unknown = 2

    	Unknown LSP establishment method

    """

    setup_rsvp = 0

    setup_sr = 1

    setup_unknown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['LspSetupEnum']


class LspStateEnum(Enum):
    """
    LspStateEnum

    LSP setup type

    .. data:: lsp_down = 0

    	LSP is down

    .. data:: lsp_up = 1

    	LSP is up

    """

    lsp_down = 0

    lsp_up = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['LspStateEnum']


class PceAfIdEnum(Enum):
    """
    PceAfIdEnum

    Pce af id

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    none = 0

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceAfIdEnum']


class PceAssoEnum(Enum):
    """
    PceAssoEnum

    Pce asso

    .. data:: unknown = 0

    	Unknown type

    .. data:: link = 1

    	LINK

    .. data:: node = 2

    	NODE

    .. data:: srlg = 3

    	SRLG

    """

    unknown = 0

    link = 1

    node = 2

    srlg = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceAssoEnum']


class PceIgpInfoIdEnum(Enum):
    """
    PceIgpInfoIdEnum

    IGP IDs

    .. data:: isis = 1

    	ISIS

    .. data:: ospf = 2

    	OSPF

    .. data:: bgp = 3

    	BGP

    """

    isis = 1

    ospf = 2

    bgp = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceIgpInfoIdEnum']


class PceProtoEnum(Enum):
    """
    PceProtoEnum

    PCE peer protocol

    .. data:: pcep = 0

    	PCE protocol

    .. data:: netconf = 1

    	Netconf protocol

    """

    pcep = 0

    netconf = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceProtoEnum']


class PceRroEnum(Enum):
    """
    PceRroEnum

    PCE RRO type

    .. data:: rro_type_ipv4_address = 0

    	IPv4 Address

    .. data:: rro_type_mpls_label = 1

    	MPLS Label

    .. data:: rro_type_sripv4_node_sid = 2

    	Segment Routing IPv4 Node SID

    .. data:: rro_type_sripv4_adjacency_sid = 3

    	Segment Routing IPv4 Adjacency SID

    .. data:: rro_type_sr_nai_null = 4

    	Segment Routing with NAI null

    """

    rro_type_ipv4_address = 0

    rro_type_mpls_label = 1

    rro_type_sripv4_node_sid = 2

    rro_type_sripv4_adjacency_sid = 3

    rro_type_sr_nai_null = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceRroEnum']


class PceSrSidEnum(Enum):
    """
    PceSrSidEnum

    PCE SR SID type

    .. data:: ipv4_node_sid = 0

    	IPv4 Node SID

    .. data:: ipv4_adjacency_sid = 1

    	IPv4 Adjacency SID

    .. data:: unknown_sid = 2

    	Unknown SID

    """

    ipv4_node_sid = 0

    ipv4_adjacency_sid = 1

    unknown_sid = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceSrSidEnum']


class PcepLspStateEnum(Enum):
    """
    PcepLspStateEnum

    PCEP operation protocol

    .. data:: lsp_down = 0

    	LSP is down

    .. data:: lsp_up = 1

    	LSP is up

    .. data:: lsp_active = 2

    	LSP is active (carrying traffic)

    .. data:: lsp_going_down = 3

    	LSP is going down

    .. data:: lsp_being_signaled = 4

    	LSP is being signaled

    """

    lsp_down = 0

    lsp_up = 1

    lsp_active = 2

    lsp_going_down = 3

    lsp_being_signaled = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PcepLspStateEnum']


class PcepStateEnum(Enum):
    """
    PcepStateEnum

    PCEP State

    .. data:: tcp_close = 0

    	TCP close

    .. data:: tcp_listen = 1

    	TCP listen

    .. data:: tcp_connect = 2

    	TCP connect

    .. data:: pcep_closed = 3

    	PCEP closed

    .. data:: pcep_opening = 4

    	PCEP opening

    .. data:: pcep_open = 5

    	PCEP open

    """

    tcp_close = 0

    tcp_listen = 1

    tcp_connect = 2

    pcep_closed = 3

    pcep_opening = 4

    pcep_open = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PcepStateEnum']


class SidEnum(Enum):
    """
    SidEnum

    SID Types

    .. data:: sr_protected_adj_sid = 1

    	Protected Adjacency SID

    .. data:: sr_unprotected_adj_sid = 2

    	Unprotected Adjacency SID

    .. data:: srbgp_egress_peer_engineering_sid = 3

    	BGP egress peer engineering SID

    .. data:: sr_reqular_prefix_sid = 4

    	Regular prefix SID

    .. data:: sr_strict_prefix_sid = 5

    	Strict prefix SID

    """

    sr_protected_adj_sid = 1

    sr_unprotected_adj_sid = 2

    srbgp_egress_peer_engineering_sid = 3

    sr_reqular_prefix_sid = 4

    sr_strict_prefix_sid = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['SidEnum']



class PceLspData(object):
    """
    PCE LSP's data
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:   :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos>`
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:   :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2016-05-31'

    def __init__(self):
        self.lsp_summary = PceLspData.LspSummary()
        self.lsp_summary.parent = self
        self.tunnel_detail_infos = PceLspData.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self.tunnel_infos = PceLspData.TunnelInfos()
        self.tunnel_infos.parent = self


    class TunnelInfos(object):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of    :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.tunnel_info = YList()
            self.tunnel_info.parent = self
            self.tunnel_info.name = 'tunnel_info'


        class TunnelInfo(object):
            """
            Tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of    :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.brief_lsp_information = YList()
                self.brief_lsp_information.parent = self
                self.brief_lsp_information.name = 'brief_lsp_information'
                self.pcc_address = None
                self.tunnel_name_xr = None


            class BriefLspInformation(object):
                """
                Brief LSP information
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:   :py:class:`LspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspStateEnum>`
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:   :py:class:`LspSetupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetupEnum>`
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:   :py:class:`PcepLspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspStateEnum>`
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.administrative_state = None
                    self.binding_sid = None
                    self.destination_address = None
                    self.lsp_setup_type = None
                    self.lspid = None
                    self.operational_state = None
                    self.source_address = None
                    self.tunnel_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.administrative_state is not None:
                        return True

                    if self.binding_sid is not None:
                        return True

                    if self.destination_address is not None:
                        return True

                    if self.lsp_setup_type is not None:
                        return True

                    if self.lspid is not None:
                        return True

                    if self.operational_state is not None:
                        return True

                    if self.source_address is not None:
                        return True

                    if self.tunnel_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')
                if self.plsp_id is None:
                    raise YPYModelError('Key property plsp_id is None')
                if self.tunnel_name is None:
                    raise YPYModelError('Key property tunnel_name is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:tunnel-infos/Cisco-IOS-XR-infra-xtc-oper:tunnel-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + '][Cisco-IOS-XR-infra-xtc-oper:plsp-id = ' + str(self.plsp_id) + '][Cisco-IOS-XR-infra-xtc-oper:tunnel-name = ' + str(self.tunnel_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.plsp_id is not None:
                    return True

                if self.tunnel_name is not None:
                    return True

                if self.brief_lsp_information is not None:
                    for child_ref in self.brief_lsp_information:
                        if child_ref._has_data():
                            return True

                if self.pcc_address is not None:
                    return True

                if self.tunnel_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceLspData.TunnelInfos.TunnelInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:tunnel-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_info is not None:
                for child_ref in self.tunnel_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceLspData.TunnelInfos']['meta_info']


    class LspSummary(object):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:   :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of    :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.all_ls_ps = PceLspData.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self.peer_ls_ps_info = YList()
            self.peer_ls_ps_info.parent = self
            self.peer_ls_ps_info.name = 'peer_ls_ps_info'


        class AllLsPs(object):
            """
            Summary for all peers
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.admin_up_ls_ps = None
                self.all_ls_ps = None
                self.rsvp_ls_ps = None
                self.sr_ls_ps = None
                self.up_ls_ps = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:all-ls-ps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.admin_up_ls_ps is not None:
                    return True

                if self.all_ls_ps is not None:
                    return True

                if self.rsvp_ls_ps is not None:
                    return True

                if self.sr_ls_ps is not None:
                    return True

                if self.up_ls_ps is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceLspData.LspSummary.AllLsPs']['meta_info']


        class PeerLsPsInfo(object):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:   :py:class:`LspSummary_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo.LspSummary_>`
            
            .. attribute:: peer_address
            
            	Peer IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.lsp_summary = PceLspData.LspSummary.PeerLsPsInfo.LspSummary_()
                self.lsp_summary.parent = self
                self.peer_address = None


            class LspSummary_(object):
                """
                Number of LSPs for specific peer
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.admin_up_ls_ps = None
                    self.all_ls_ps = None
                    self.rsvp_ls_ps = None
                    self.sr_ls_ps = None
                    self.up_ls_ps = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:peer-ls-ps-info/Cisco-IOS-XR-infra-xtc-oper:lsp-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_up_ls_ps is not None:
                        return True

                    if self.all_ls_ps is not None:
                        return True

                    if self.rsvp_ls_ps is not None:
                        return True

                    if self.sr_ls_ps is not None:
                        return True

                    if self.up_ls_ps is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceLspData.LspSummary.PeerLsPsInfo.LspSummary_']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:peer-ls-ps-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.lsp_summary is not None and self.lsp_summary._has_data():
                    return True

                if self.peer_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceLspData.LspSummary.PeerLsPsInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:lsp-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.all_ls_ps is not None and self.all_ls_ps._has_data():
                return True

            if self.peer_ls_ps_info is not None:
                for child_ref in self.peer_ls_ps_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceLspData.LspSummary']['meta_info']


    class TunnelDetailInfos(object):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of    :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.tunnel_detail_info = YList()
            self.tunnel_detail_info.parent = self
            self.tunnel_detail_info.name = 'tunnel_detail_info'


        class TunnelDetailInfo(object):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of    :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:   :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.detail_lsp_information = YList()
                self.detail_lsp_information.parent = self
                self.detail_lsp_information.name = 'detail_lsp_information'
                self.pcc_address = None
                self.private_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self.tunnel_name_xr = None


            class PrivateLspInformation(object):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of    :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.event_buffer = YList()
                    self.event_buffer.parent = self
                    self.event_buffer.name = 'event_buffer'


                class EventBuffer(object):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\:  str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.event_message = None
                        self.time_stamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:event-buffer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.event_message is not None:
                            return True

                        if self.time_stamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:private-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.event_buffer is not None:
                        for child_ref in self.event_buffer:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info']


            class DetailLspInformation(object):
                """
                Detail LSP information
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\:  bool
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:   :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:   :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:   :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:   :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:   :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of    :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\:  bool
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.actual_bandwidth = None
                    self.actual_bandwidth_specified = None
                    self.brief_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self.computing_pce = None
                    self.er_os = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self.lsp_association_info = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self.lsp_attributes = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self.lsp_role = None
                    self.lsppcep_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self.reporting_pcc_address = None
                    self.rro = YList()
                    self.rro.parent = self
                    self.rro.name = 'rro'
                    self.signaled_bandwidth = None
                    self.signaled_bandwidth_specified = None
                    self.srlg_info = YLeafList()
                    self.srlg_info.parent = self
                    self.srlg_info.name = 'srlg_info'
                    self.state_sync_pce = None
                    self.sub_delegated_pce = None


                class BriefLspInformation(object):
                    """
                    Brief LSP information
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:   :py:class:`LspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspStateEnum>`
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:   :py:class:`LspSetupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetupEnum>`
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:   :py:class:`PcepLspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspStateEnum>`
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.administrative_state = None
                        self.binding_sid = None
                        self.destination_address = None
                        self.lsp_setup_type = None
                        self.lspid = None
                        self.operational_state = None
                        self.source_address = None
                        self.tunnel_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-lsp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.administrative_state is not None:
                            return True

                        if self.binding_sid is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.lsp_setup_type is not None:
                            return True

                        if self.lspid is not None:
                            return True

                        if self.operational_state is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation']['meta_info']


                class ErOs(object):
                    """
                    Paths
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of    :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of    :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of    :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of    :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.computed_hop_list_time = None
                        self.computed_metric_type = None
                        self.computed_metric_value = None
                        self.computed_rsvp_path = YList()
                        self.computed_rsvp_path.parent = self
                        self.computed_rsvp_path.name = 'computed_rsvp_path'
                        self.computed_sr_path = YList()
                        self.computed_sr_path.parent = self
                        self.computed_sr_path.name = 'computed_sr_path'
                        self.reported_metric_type = None
                        self.reported_metric_value = None
                        self.reported_rsvp_path = YList()
                        self.reported_rsvp_path.parent = self
                        self.reported_rsvp_path.name = 'reported_rsvp_path'
                        self.reported_sr_path = YList()
                        self.reported_sr_path.parent = self
                        self.reported_sr_path.name = 'reported_sr_path'


                    class ReportedRsvpPath(object):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:reported-rsvp-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath']['meta_info']


                    class ReportedSrPath(object):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:reported-sr-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath']['meta_info']


                    class ComputedRsvpPath(object):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:computed-rsvp-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath']['meta_info']


                    class ComputedSrPath(object):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:computed-sr-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:er-os'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.computed_hop_list_time is not None:
                            return True

                        if self.computed_metric_type is not None:
                            return True

                        if self.computed_metric_value is not None:
                            return True

                        if self.computed_rsvp_path is not None:
                            for child_ref in self.computed_rsvp_path:
                                if child_ref._has_data():
                                    return True

                        if self.computed_sr_path is not None:
                            for child_ref in self.computed_sr_path:
                                if child_ref._has_data():
                                    return True

                        if self.reported_metric_type is not None:
                            return True

                        if self.reported_metric_value is not None:
                            return True

                        if self.reported_rsvp_path is not None:
                            for child_ref in self.reported_rsvp_path:
                                if child_ref._has_data():
                                    return True

                        if self.reported_sr_path is not None:
                            for child_ref in self.reported_sr_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']


                class LsppcepInformation(object):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\:  bool
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:   :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pcep_flag_a = None
                        self.pcep_flag_d = None
                        self.pcep_flag_o = None
                        self.pcep_flag_r = None
                        self.pcep_flag_s = None
                        self.pcepid = None
                        self.rsvp_error = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self


                    class RsvpError(object):
                        """
                        RSVP error info
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.error_code = None
                            self.error_flags = None
                            self.error_value = None
                            self.node_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:rsvp-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.error_code is not None:
                                return True

                            if self.error_flags is not None:
                                return True

                            if self.error_value is not None:
                                return True

                            if self.node_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsppcep-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcep_flag_a is not None:
                            return True

                        if self.pcep_flag_d is not None:
                            return True

                        if self.pcep_flag_o is not None:
                            return True

                        if self.pcep_flag_r is not None:
                            return True

                        if self.pcep_flag_s is not None:
                            return True

                        if self.pcepid is not None:
                            return True

                        if self.rsvp_error is not None and self.rsvp_error._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info']


                class LspAssociationInfo(object):
                    """
                    LSP association information
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.association_id = None
                        self.association_source = None
                        self.association_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsp-association-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.association_id is not None:
                            return True

                        if self.association_source is not None:
                            return True

                        if self.association_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo']['meta_info']


                class LspAttributes(object):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\:  bool
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.affinity_exclude_any = None
                        self.affinity_include_all = None
                        self.affinity_include_any = None
                        self.hold_priority = None
                        self.local_protection = None
                        self.setup_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsp-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.affinity_exclude_any is not None:
                            return True

                        if self.affinity_include_all is not None:
                            return True

                        if self.affinity_include_any is not None:
                            return True

                        if self.hold_priority is not None:
                            return True

                        if self.local_protection is not None:
                            return True

                        if self.setup_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes']['meta_info']


                class Rro(object):
                    """
                    RRO
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:   :py:class:`PceRroEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRroEnum>`
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:   :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.flags = None
                        self.ipv4_address = None
                        self.mpls_label = None
                        self.rro_type = None
                        self.sr_rro = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self


                    class SrRro(object):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sr-rro'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:rro'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.flags is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.rro_type is not None:
                            return True

                        if self.sr_rro is not None and self.sr_rro._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:detail-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.actual_bandwidth is not None:
                        return True

                    if self.actual_bandwidth_specified is not None:
                        return True

                    if self.brief_lsp_information is not None and self.brief_lsp_information._has_data():
                        return True

                    if self.computing_pce is not None:
                        return True

                    if self.er_os is not None and self.er_os._has_data():
                        return True

                    if self.lsp_association_info is not None and self.lsp_association_info._has_data():
                        return True

                    if self.lsp_attributes is not None and self.lsp_attributes._has_data():
                        return True

                    if self.lsp_role is not None:
                        return True

                    if self.lsppcep_information is not None and self.lsppcep_information._has_data():
                        return True

                    if self.reporting_pcc_address is not None:
                        return True

                    if self.rro is not None:
                        for child_ref in self.rro:
                            if child_ref._has_data():
                                return True

                    if self.signaled_bandwidth is not None:
                        return True

                    if self.signaled_bandwidth_specified is not None:
                        return True

                    if self.srlg_info is not None:
                        for child in self.srlg_info:
                            if child is not None:
                                return True

                    if self.state_sync_pce is not None:
                        return True

                    if self.sub_delegated_pce is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')
                if self.plsp_id is None:
                    raise YPYModelError('Key property plsp_id is None')
                if self.tunnel_name is None:
                    raise YPYModelError('Key property tunnel_name is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-infos/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + '][Cisco-IOS-XR-infra-xtc-oper:plsp-id = ' + str(self.plsp_id) + '][Cisco-IOS-XR-infra-xtc-oper:tunnel-name = ' + str(self.tunnel_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.plsp_id is not None:
                    return True

                if self.tunnel_name is not None:
                    return True

                if self.detail_lsp_information is not None:
                    for child_ref in self.detail_lsp_information:
                        if child_ref._has_data():
                            return True

                if self.pcc_address is not None:
                    return True

                if self.private_lsp_information is not None and self.private_lsp_information._has_data():
                    return True

                if self.tunnel_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_detail_info is not None:
                for child_ref in self.tunnel_detail_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceLspData.TunnelDetailInfos']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.lsp_summary is not None and self.lsp_summary._has_data():
            return True

        if self.tunnel_detail_infos is not None and self.tunnel_detail_infos._has_data():
            return True

        if self.tunnel_infos is not None and self.tunnel_infos._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceLspData']['meta_info']


class PcePeer(object):
    """
    pce peer
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:   :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:   :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2016-05-31'

    def __init__(self):
        self.peer_detail_infos = PcePeer.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self.peer_infos = PcePeer.PeerInfos()
        self.peer_infos.parent = self


    class PeerDetailInfos(object):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of    :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.peer_detail_info = YList()
            self.peer_detail_info.parent = self
            self.peer_detail_info.name = 'peer_detail_info'


        class PeerDetailInfo(object):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:   :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProtoEnum>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.detail_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self.peer_address_xr = None
                self.peer_protocol = None


            class DetailPcepInformation(object):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\:  str
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:   :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:   :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.brief_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self.error = None
                    self.keepalives = None
                    self.keychain_enabled = None
                    self.last_error_rx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self.last_error_tx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self.local_session_id = None
                    self.maximum_dead_interval = None
                    self.md5_enabled = None
                    self.minimum_keepalive_interval = None
                    self.negotiated_dead_time = None
                    self.negotiated_local_keepalive = None
                    self.negotiated_remote_keepalive = None
                    self.pce_error_rx = None
                    self.pce_error_tx = None
                    self.pce_initiate_rx = None
                    self.pce_initiate_tx = None
                    self.pce_keepalive_rx = None
                    self.pce_keepalive_tx = None
                    self.pce_open_rx = None
                    self.pce_open_tx = None
                    self.pce_reply_rx = None
                    self.pce_reply_tx = None
                    self.pce_report_rx = None
                    self.pce_report_tx = None
                    self.pce_request_rx = None
                    self.pce_request_tx = None
                    self.pce_update_rx = None
                    self.pce_update_tx = None
                    self.pcep_up_time = None
                    self.remote_session_id = None
                    self.speaker_id = None


                class BriefPcepInformation(object):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\:  bool
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:   :py:class:`PcepStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepStateEnum>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.capability_db_version = None
                        self.capability_delta_sync = None
                        self.capability_instantiate = None
                        self.capability_segment_routing = None
                        self.capability_triggered_sync = None
                        self.capability_update = None
                        self.pcep_state = None
                        self.stateful = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-pcep-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.capability_db_version is not None:
                            return True

                        if self.capability_delta_sync is not None:
                            return True

                        if self.capability_instantiate is not None:
                            return True

                        if self.capability_segment_routing is not None:
                            return True

                        if self.capability_triggered_sync is not None:
                            return True

                        if self.capability_update is not None:
                            return True

                        if self.pcep_state is not None:
                            return True

                        if self.stateful is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation']['meta_info']


                class LastErrorRx(object):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pc_error_type = None
                        self.pc_error_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:last-error-rx'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pc_error_type is not None:
                            return True

                        if self.pc_error_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx']['meta_info']


                class LastErrorTx(object):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pc_error_type = None
                        self.pc_error_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:last-error-tx'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pc_error_type is not None:
                            return True

                        if self.pc_error_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:detail-pcep-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.brief_pcep_information is not None and self.brief_pcep_information._has_data():
                        return True

                    if self.error is not None:
                        return True

                    if self.keepalives is not None:
                        return True

                    if self.keychain_enabled is not None:
                        return True

                    if self.last_error_rx is not None and self.last_error_rx._has_data():
                        return True

                    if self.last_error_tx is not None and self.last_error_tx._has_data():
                        return True

                    if self.local_session_id is not None:
                        return True

                    if self.maximum_dead_interval is not None:
                        return True

                    if self.md5_enabled is not None:
                        return True

                    if self.minimum_keepalive_interval is not None:
                        return True

                    if self.negotiated_dead_time is not None:
                        return True

                    if self.negotiated_local_keepalive is not None:
                        return True

                    if self.negotiated_remote_keepalive is not None:
                        return True

                    if self.pce_error_rx is not None:
                        return True

                    if self.pce_error_tx is not None:
                        return True

                    if self.pce_initiate_rx is not None:
                        return True

                    if self.pce_initiate_tx is not None:
                        return True

                    if self.pce_keepalive_rx is not None:
                        return True

                    if self.pce_keepalive_tx is not None:
                        return True

                    if self.pce_open_rx is not None:
                        return True

                    if self.pce_open_tx is not None:
                        return True

                    if self.pce_reply_rx is not None:
                        return True

                    if self.pce_reply_tx is not None:
                        return True

                    if self.pce_report_rx is not None:
                        return True

                    if self.pce_report_tx is not None:
                        return True

                    if self.pce_request_rx is not None:
                        return True

                    if self.pce_request_tx is not None:
                        return True

                    if self.pce_update_rx is not None:
                        return True

                    if self.pce_update_tx is not None:
                        return True

                    if self.pcep_up_time is not None:
                        return True

                    if self.remote_session_id is not None:
                        return True

                    if self.speaker_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-peer/Cisco-IOS-XR-infra-xtc-oper:peer-detail-infos/Cisco-IOS-XR-infra-xtc-oper:peer-detail-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.detail_pcep_information is not None and self.detail_pcep_information._has_data():
                    return True

                if self.peer_address_xr is not None:
                    return True

                if self.peer_protocol is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-peer/Cisco-IOS-XR-infra-xtc-oper:peer-detail-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.peer_detail_info is not None:
                for child_ref in self.peer_detail_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PcePeer.PeerDetailInfos']['meta_info']


    class PeerInfos(object):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of    :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.peer_info = YList()
            self.peer_info.parent = self
            self.peer_info.name = 'peer_info'


        class PeerInfo(object):
            """
            PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProtoEnum>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.brief_pcep_information = PcePeer.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self.peer_address_xr = None
                self.peer_protocol = None


            class BriefPcepInformation(object):
                """
                PCE protocol information
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\:  bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\:  bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\:  bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\:  bool
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:   :py:class:`PcepStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepStateEnum>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.capability_db_version = None
                    self.capability_delta_sync = None
                    self.capability_instantiate = None
                    self.capability_segment_routing = None
                    self.capability_triggered_sync = None
                    self.capability_update = None
                    self.pcep_state = None
                    self.stateful = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-pcep-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.capability_db_version is not None:
                        return True

                    if self.capability_delta_sync is not None:
                        return True

                    if self.capability_instantiate is not None:
                        return True

                    if self.capability_segment_routing is not None:
                        return True

                    if self.capability_triggered_sync is not None:
                        return True

                    if self.capability_update is not None:
                        return True

                    if self.pcep_state is not None:
                        return True

                    if self.stateful is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PcePeer.PeerInfos.PeerInfo.BriefPcepInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-peer/Cisco-IOS-XR-infra-xtc-oper:peer-infos/Cisco-IOS-XR-infra-xtc-oper:peer-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.brief_pcep_information is not None and self.brief_pcep_information._has_data():
                    return True

                if self.peer_address_xr is not None:
                    return True

                if self.peer_protocol is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PcePeer.PeerInfos.PeerInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-peer/Cisco-IOS-XR-infra-xtc-oper:peer-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.peer_info is not None:
                for child_ref in self.peer_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PcePeer.PeerInfos']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-xtc-oper:pce-peer'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.peer_detail_infos is not None and self.peer_detail_infos._has_data():
            return True

        if self.peer_infos is not None and self.peer_infos._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PcePeer']['meta_info']


class PceTopology(object):
    """
    pce topology
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:   :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:   :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes>`
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:   :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2016-05-31'

    def __init__(self):
        self.prefix_infos = PceTopology.PrefixInfos()
        self.prefix_infos.parent = self
        self.topology_nodes = PceTopology.TopologyNodes()
        self.topology_nodes.parent = self
        self.topology_summary = PceTopology.TopologySummary()
        self.topology_summary.parent = self


    class TopologySummary(object):
        """
        Node summary database in XTC
        
        .. attribute:: adjacency_sids
        
        	Number of adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: nodes
        
        	Number of nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:   :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\:  bool
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.adjacency_sids = None
            self.links = None
            self.nodes = None
            self.prefix_sids = None
            self.prefixes = None
            self.stats_topology_update = PceTopology.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self.topology_consistent = None


        class StatsTopologyUpdate(object):
            """
            Statistics on topology update
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.num_links_added = None
                self.num_links_deleted = None
                self.num_nodes_added = None
                self.num_nodes_deleted = None
                self.num_prefixes_added = None
                self.num_prefixes_deleted = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:topology-summary/Cisco-IOS-XR-infra-xtc-oper:stats-topology-update'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.num_links_added is not None:
                    return True

                if self.num_links_deleted is not None:
                    return True

                if self.num_nodes_added is not None:
                    return True

                if self.num_nodes_deleted is not None:
                    return True

                if self.num_prefixes_added is not None:
                    return True

                if self.num_prefixes_deleted is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceTopology.TopologySummary.StatsTopologyUpdate']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:topology-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.adjacency_sids is not None:
                return True

            if self.links is not None:
                return True

            if self.nodes is not None:
                return True

            if self.prefix_sids is not None:
                return True

            if self.prefixes is not None:
                return True

            if self.stats_topology_update is not None and self.stats_topology_update._has_data():
                return True

            if self.topology_consistent is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceTopology.TopologySummary']['meta_info']


    class TopologyNodes(object):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of    :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.topology_node = YList()
            self.topology_node.parent = self
            self.topology_node.name = 'topology_node'


        class TopologyNode(object):
            """
            Node information
            
            .. attribute:: node_identifier  <key>
            
            	Node Identifier
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of    :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of    :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\:  bool
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of    :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.PrefixSid>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.node_identifier = None
                self.ipv4_link = YList()
                self.ipv4_link.parent = self
                self.ipv4_link.name = 'ipv4_link'
                self.ipv6_link = YList()
                self.ipv6_link.parent = self
                self.ipv6_link.name = 'ipv6_link'
                self.node_identifier_xr = None
                self.node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self.overload = None
                self.prefix_sid = YList()
                self.prefix_sid.parent = self
                self.prefix_sid.name = 'prefix_sid'


            class NodeProtocolIdentifier(object):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.igp_information = YList()
                    self.igp_information.parent = self
                    self.igp_information.name = 'igp_information'
                    self.ipv4bgp_router_id = None
                    self.ipv4bgp_router_id_set = None
                    self.ipv4te_router_id = None
                    self.ipv4te_router_id_set = None
                    self.node_name = None
                    self.srgb_information = YList()
                    self.srgb_information.parent = self
                    self.srgb_information.name = 'srgb_information'


                class IgpInformation(object):
                    """
                    IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info']


                class SrgbInformation(object):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self.size = None
                        self.start = None


                    class IgpSrgb(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_srgb is not None and self.igp_srgb._has_data():
                            return True

                        if self.size is not None:
                            return True

                        if self.start is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:node-protocol-identifier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.igp_information is not None:
                        for child_ref in self.igp_information:
                            if child_ref._has_data():
                                return True

                    if self.ipv4bgp_router_id is not None:
                        return True

                    if self.ipv4bgp_router_id_set is not None:
                        return True

                    if self.ipv4te_router_id is not None:
                        return True

                    if self.ipv4te_router_id_set is not None:
                        return True

                    if self.node_name is not None:
                        return True

                    if self.srgb_information is not None:
                        for child_ref in self.srgb_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']


            class PrefixSid(object):
                """
                Prefix SIDs
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: eflag
                
                	E Flag
                	**type**\:  bool
                
                .. attribute:: lflag
                
                	L Flag
                	**type**\:  bool
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nflag
                
                	N Flag
                	**type**\:  bool
                
                .. attribute:: pflag
                
                	P Flag
                	**type**\:  bool
                
                .. attribute:: rflag
                
                	R Flag
                	**type**\:  bool
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                
                .. attribute:: vflag
                
                	V Flag
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.domain_identifier = None
                    self.eflag = None
                    self.lflag = None
                    self.mpls_label = None
                    self.nflag = None
                    self.pflag = None
                    self.rflag = None
                    self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix()
                    self.sid_prefix.parent = self
                    self.sid_type = None
                    self.vflag = None


                class SidPrefix(object):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.ipv4 is not None:
                            return True

                        if self.ipv6 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:prefix-sid'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain_identifier is not None:
                        return True

                    if self.eflag is not None:
                        return True

                    if self.lflag is not None:
                        return True

                    if self.mpls_label is not None:
                        return True

                    if self.nflag is not None:
                        return True

                    if self.pflag is not None:
                        return True

                    if self.rflag is not None:
                        return True

                    if self.sid_prefix is not None and self.sid_prefix._has_data():
                        return True

                    if self.sid_type is not None:
                        return True

                    if self.vflag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.PrefixSid']['meta_info']


            class Ipv4Link(object):
                """
                IPv4 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.adjacency_sid = YList()
                    self.adjacency_sid.parent = self
                    self.adjacency_sid.name = 'adjacency_sid'
                    self.igp_metric = None
                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self.local_ipv4_address = None
                    self.max_reservable_bandwidth = None
                    self.maximum_link_bandwidth = None
                    self.remote_ipv4_address = None
                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self.srlgs = YLeafList()
                    self.srlgs.parent = self
                    self.srlgs.name = 'srlgs'
                    self.te_metric = None


                class LocalIgpInformation(object):
                    """
                    Local node IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:local-igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(object):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_information = YList()
                        self.igp_information.parent = self
                        self.igp_information.name = 'igp_information'
                        self.ipv4bgp_router_id = None
                        self.ipv4bgp_router_id_set = None
                        self.ipv4te_router_id = None
                        self.ipv4te_router_id_set = None
                        self.node_name = None
                        self.srgb_information = YList()
                        self.srgb_information.parent = self
                        self.srgb_information.name = 'srgb_information'


                    class IgpInformation(object):
                        """
                        IGP information
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.domain_identifier = None
                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self


                        class Igp(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.domain_identifier is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']


                    class SrgbInformation(object):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self.size = None
                            self.start = None


                        class IgpSrgb(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.igp_srgb is not None and self.igp_srgb._has_data():
                                return True

                            if self.size is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:remote-node-protocol-identifier'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_information is not None:
                            for child_ref in self.igp_information:
                                if child_ref._has_data():
                                    return True

                        if self.ipv4bgp_router_id is not None:
                            return True

                        if self.ipv4bgp_router_id_set is not None:
                            return True

                        if self.ipv4te_router_id is not None:
                            return True

                        if self.ipv4te_router_id_set is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.srgb_information is not None:
                            for child_ref in self.srgb_information:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']


                class AdjacencySid(object):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.eflag = None
                        self.lflag = None
                        self.mpls_label = None
                        self.nflag = None
                        self.pflag = None
                        self.rflag = None
                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self.sid_type = None
                        self.vflag = None


                    class SidPrefix(object):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:adjacency-sid'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.eflag is not None:
                            return True

                        if self.lflag is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.nflag is not None:
                            return True

                        if self.pflag is not None:
                            return True

                        if self.rflag is not None:
                            return True

                        if self.sid_prefix is not None and self.sid_prefix._has_data():
                            return True

                        if self.sid_type is not None:
                            return True

                        if self.vflag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ipv4-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.adjacency_sid is not None:
                        for child_ref in self.adjacency_sid:
                            if child_ref._has_data():
                                return True

                    if self.igp_metric is not None:
                        return True

                    if self.local_igp_information is not None and self.local_igp_information._has_data():
                        return True

                    if self.local_ipv4_address is not None:
                        return True

                    if self.max_reservable_bandwidth is not None:
                        return True

                    if self.maximum_link_bandwidth is not None:
                        return True

                    if self.remote_ipv4_address is not None:
                        return True

                    if self.remote_node_protocol_identifier is not None and self.remote_node_protocol_identifier._has_data():
                        return True

                    if self.srlgs is not None:
                        for child in self.srlgs:
                            if child is not None:
                                return True

                    if self.te_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']


            class Ipv6Link(object):
                """
                IPv6 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.adjacency_sid = YList()
                    self.adjacency_sid.parent = self
                    self.adjacency_sid.name = 'adjacency_sid'
                    self.igp_metric = None
                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self.local_ipv6_address = None
                    self.max_reservable_bandwidth = None
                    self.maximum_link_bandwidth = None
                    self.remote_ipv6_address = None
                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self.te_metric = None


                class LocalIgpInformation(object):
                    """
                    Local node IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:local-igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(object):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_information = YList()
                        self.igp_information.parent = self
                        self.igp_information.name = 'igp_information'
                        self.ipv4bgp_router_id = None
                        self.ipv4bgp_router_id_set = None
                        self.ipv4te_router_id = None
                        self.ipv4te_router_id_set = None
                        self.node_name = None
                        self.srgb_information = YList()
                        self.srgb_information.parent = self
                        self.srgb_information.name = 'srgb_information'


                    class IgpInformation(object):
                        """
                        IGP information
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.domain_identifier = None
                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self


                        class Igp(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.domain_identifier is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']


                    class SrgbInformation(object):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self.size = None
                            self.start = None


                        class IgpSrgb(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.igp_srgb is not None and self.igp_srgb._has_data():
                                return True

                            if self.size is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:remote-node-protocol-identifier'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_information is not None:
                            for child_ref in self.igp_information:
                                if child_ref._has_data():
                                    return True

                        if self.ipv4bgp_router_id is not None:
                            return True

                        if self.ipv4bgp_router_id_set is not None:
                            return True

                        if self.ipv4te_router_id is not None:
                            return True

                        if self.ipv4te_router_id_set is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.srgb_information is not None:
                            for child_ref in self.srgb_information:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']


                class AdjacencySid(object):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.eflag = None
                        self.lflag = None
                        self.mpls_label = None
                        self.nflag = None
                        self.pflag = None
                        self.rflag = None
                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self.sid_type = None
                        self.vflag = None


                    class SidPrefix(object):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:adjacency-sid'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.eflag is not None:
                            return True

                        if self.lflag is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.nflag is not None:
                            return True

                        if self.pflag is not None:
                            return True

                        if self.rflag is not None:
                            return True

                        if self.sid_prefix is not None and self.sid_prefix._has_data():
                            return True

                        if self.sid_type is not None:
                            return True

                        if self.vflag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ipv6-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.adjacency_sid is not None:
                        for child_ref in self.adjacency_sid:
                            if child_ref._has_data():
                                return True

                    if self.igp_metric is not None:
                        return True

                    if self.local_igp_information is not None and self.local_igp_information._has_data():
                        return True

                    if self.local_ipv6_address is not None:
                        return True

                    if self.max_reservable_bandwidth is not None:
                        return True

                    if self.maximum_link_bandwidth is not None:
                        return True

                    if self.remote_ipv6_address is not None:
                        return True

                    if self.remote_node_protocol_identifier is not None and self.remote_node_protocol_identifier._has_data():
                        return True

                    if self.te_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']

            @property
            def _common_path(self):
                if self.node_identifier is None:
                    raise YPYModelError('Key property node_identifier is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:topology-nodes/Cisco-IOS-XR-infra-xtc-oper:topology-node[Cisco-IOS-XR-infra-xtc-oper:node-identifier = ' + str(self.node_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_identifier is not None:
                    return True

                if self.ipv4_link is not None:
                    for child_ref in self.ipv4_link:
                        if child_ref._has_data():
                            return True

                if self.ipv6_link is not None:
                    for child_ref in self.ipv6_link:
                        if child_ref._has_data():
                            return True

                if self.node_identifier_xr is not None:
                    return True

                if self.node_protocol_identifier is not None and self.node_protocol_identifier._has_data():
                    return True

                if self.overload is not None:
                    return True

                if self.prefix_sid is not None:
                    for child_ref in self.prefix_sid:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:topology-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.topology_node is not None:
                for child_ref in self.topology_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceTopology.TopologyNodes']['meta_info']


    class PrefixInfos(object):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of    :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.prefix_info = YList()
            self.prefix_info.parent = self
            self.prefix_info.name = 'prefix_info'


        class PrefixInfo(object):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  <key>
            
            	Node ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.Address>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.node_identifier = None
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.node_identifier_xr = None
                self.node_protocol_identifier = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self


            class NodeProtocolIdentifier(object):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.igp_information = YList()
                    self.igp_information.parent = self
                    self.igp_information.name = 'igp_information'
                    self.ipv4bgp_router_id = None
                    self.ipv4bgp_router_id_set = None
                    self.ipv4te_router_id = None
                    self.ipv4te_router_id_set = None
                    self.node_name = None
                    self.srgb_information = YList()
                    self.srgb_information.parent = self
                    self.srgb_information.name = 'srgb_information'


                class IgpInformation(object):
                    """
                    IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info']


                class SrgbInformation(object):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_srgb = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self.size = None
                        self.start = None


                    class IgpSrgb(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_srgb is not None and self.igp_srgb._has_data():
                            return True

                        if self.size is not None:
                            return True

                        if self.start is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:node-protocol-identifier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.igp_information is not None:
                        for child_ref in self.igp_information:
                            if child_ref._has_data():
                                return True

                    if self.ipv4bgp_router_id is not None:
                        return True

                    if self.ipv4bgp_router_id_set is not None:
                        return True

                    if self.ipv4te_router_id is not None:
                        return True

                    if self.ipv4te_router_id_set is not None:
                        return True

                    if self.node_name is not None:
                        return True

                    if self.srgb_information is not None:
                        for child_ref in self.srgb_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']


            class Address(object):
                """
                Prefix address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.ipv4 is not None:
                        return True

                    if self.ipv6 is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo.Address']['meta_info']

            @property
            def _common_path(self):
                if self.node_identifier is None:
                    raise YPYModelError('Key property node_identifier is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:prefix-infos/Cisco-IOS-XR-infra-xtc-oper:prefix-info[Cisco-IOS-XR-infra-xtc-oper:node-identifier = ' + str(self.node_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_identifier is not None:
                    return True

                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.node_identifier_xr is not None:
                    return True

                if self.node_protocol_identifier is not None and self.node_protocol_identifier._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['PceTopology.PrefixInfos.PrefixInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology/Cisco-IOS-XR-infra-xtc-oper:prefix-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.prefix_info is not None:
                for child_ref in self.prefix_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['PceTopology.PrefixInfos']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-xtc-oper:pce-topology'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.prefix_infos is not None and self.prefix_infos._has_data():
            return True

        if self.topology_nodes is not None and self.topology_nodes._has_data():
            return True

        if self.topology_summary is not None and self.topology_summary._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['PceTopology']['meta_info']


class Pce(object):
    """
    pce
    
    .. attribute:: association_infos
    
    	Associaition database in XTC
    	**type**\:   :py:class:`AssociationInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos>`
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary>`
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:   :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:   :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos>`
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:   :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:   :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes>`
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:   :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:   :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos>`
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:   :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2016-05-31'

    def __init__(self):
        self.association_infos = Pce.AssociationInfos()
        self.association_infos.parent = self
        self.lsp_summary = Pce.LspSummary()
        self.lsp_summary.parent = self
        self.peer_detail_infos = Pce.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self.peer_infos = Pce.PeerInfos()
        self.peer_infos.parent = self
        self.prefix_infos = Pce.PrefixInfos()
        self.prefix_infos.parent = self
        self.topology_nodes = Pce.TopologyNodes()
        self.topology_nodes.parent = self
        self.topology_summary = Pce.TopologySummary()
        self.topology_summary.parent = self
        self.tunnel_detail_infos = Pce.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self.tunnel_infos = Pce.TunnelInfos()
        self.tunnel_infos.parent = self


    class AssociationInfos(object):
        """
        Associaition database in XTC
        
        .. attribute:: association_info
        
        	PCE Association information
        	**type**\: list of    :py:class:`AssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.association_info = YList()
            self.association_info.parent = self
            self.association_info.name = 'association_info'


        class AssociationInfo(object):
            """
            PCE Association information
            
            .. attribute:: group_id  <key>
            
            	Group ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: association_id
            
            	Association ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: association_lsp
            
            	Association LSP Info
            	**type**\: list of    :py:class:`AssociationLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo.AssociationLsp>`
            
            .. attribute:: association_source
            
            	Association Source
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: association_type
            
            	Association Type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: headends_swapped
            
            	Headends Swapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: status
            
            	Association Status
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: strict
            
            	Association Strict Mode
            	**type**\:  bool
            
            .. attribute:: sub_id
            
            	Sub ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: type
            
            	Type
            	**type**\:   :py:class:`PceAssoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAssoEnum>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.group_id = None
                self.association_id = None
                self.association_lsp = YList()
                self.association_lsp.parent = self
                self.association_lsp.name = 'association_lsp'
                self.association_source = None
                self.association_type = None
                self.headends_swapped = None
                self.status = None
                self.strict = None
                self.sub_id = None
                self.type = None


            class AssociationLsp(object):
                """
                Association LSP Info
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcc_address
                
                	PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: pce_based
                
                	PCE Based
                	**type**\:  bool
                
                .. attribute:: plsp_id
                
                	PLSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_name
                
                	Tunnel Name
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.lspid = None
                    self.pcc_address = None
                    self.pce_based = None
                    self.plsp_id = None
                    self.tunnel_id = None
                    self.tunnel_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:association-lsp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.lspid is not None:
                        return True

                    if self.pcc_address is not None:
                        return True

                    if self.pce_based is not None:
                        return True

                    if self.plsp_id is not None:
                        return True

                    if self.tunnel_id is not None:
                        return True

                    if self.tunnel_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.AssociationInfos.AssociationInfo.AssociationLsp']['meta_info']

            @property
            def _common_path(self):
                if self.group_id is None:
                    raise YPYModelError('Key property group_id is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:association-infos/Cisco-IOS-XR-infra-xtc-oper:association-info[Cisco-IOS-XR-infra-xtc-oper:group-id = ' + str(self.group_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.group_id is not None:
                    return True

                if self.association_id is not None:
                    return True

                if self.association_lsp is not None:
                    for child_ref in self.association_lsp:
                        if child_ref._has_data():
                            return True

                if self.association_source is not None:
                    return True

                if self.association_type is not None:
                    return True

                if self.headends_swapped is not None:
                    return True

                if self.status is not None:
                    return True

                if self.strict is not None:
                    return True

                if self.sub_id is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.AssociationInfos.AssociationInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:association-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.association_info is not None:
                for child_ref in self.association_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.AssociationInfos']['meta_info']


    class TopologySummary(object):
        """
        Node summary database in XTC
        
        .. attribute:: adjacency_sids
        
        	Number of adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: nodes
        
        	Number of nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:   :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\:  bool
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.adjacency_sids = None
            self.links = None
            self.nodes = None
            self.prefix_sids = None
            self.prefixes = None
            self.stats_topology_update = Pce.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self.topology_consistent = None


        class StatsTopologyUpdate(object):
            """
            Statistics on topology update
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.num_links_added = None
                self.num_links_deleted = None
                self.num_nodes_added = None
                self.num_nodes_deleted = None
                self.num_prefixes_added = None
                self.num_prefixes_deleted = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:topology-summary/Cisco-IOS-XR-infra-xtc-oper:stats-topology-update'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.num_links_added is not None:
                    return True

                if self.num_links_deleted is not None:
                    return True

                if self.num_nodes_added is not None:
                    return True

                if self.num_nodes_deleted is not None:
                    return True

                if self.num_prefixes_added is not None:
                    return True

                if self.num_prefixes_deleted is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.TopologySummary.StatsTopologyUpdate']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:topology-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.adjacency_sids is not None:
                return True

            if self.links is not None:
                return True

            if self.nodes is not None:
                return True

            if self.prefix_sids is not None:
                return True

            if self.prefixes is not None:
                return True

            if self.stats_topology_update is not None and self.stats_topology_update._has_data():
                return True

            if self.topology_consistent is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.TopologySummary']['meta_info']


    class TunnelInfos(object):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of    :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.tunnel_info = YList()
            self.tunnel_info.parent = self
            self.tunnel_info.name = 'tunnel_info'


        class TunnelInfo(object):
            """
            Tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of    :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.brief_lsp_information = YList()
                self.brief_lsp_information.parent = self
                self.brief_lsp_information.name = 'brief_lsp_information'
                self.pcc_address = None
                self.tunnel_name_xr = None


            class BriefLspInformation(object):
                """
                Brief LSP information
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:   :py:class:`LspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspStateEnum>`
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:   :py:class:`LspSetupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetupEnum>`
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:   :py:class:`PcepLspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspStateEnum>`
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.administrative_state = None
                    self.binding_sid = None
                    self.destination_address = None
                    self.lsp_setup_type = None
                    self.lspid = None
                    self.operational_state = None
                    self.source_address = None
                    self.tunnel_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.administrative_state is not None:
                        return True

                    if self.binding_sid is not None:
                        return True

                    if self.destination_address is not None:
                        return True

                    if self.lsp_setup_type is not None:
                        return True

                    if self.lspid is not None:
                        return True

                    if self.operational_state is not None:
                        return True

                    if self.source_address is not None:
                        return True

                    if self.tunnel_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TunnelInfos.TunnelInfo.BriefLspInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')
                if self.plsp_id is None:
                    raise YPYModelError('Key property plsp_id is None')
                if self.tunnel_name is None:
                    raise YPYModelError('Key property tunnel_name is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:tunnel-infos/Cisco-IOS-XR-infra-xtc-oper:tunnel-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + '][Cisco-IOS-XR-infra-xtc-oper:plsp-id = ' + str(self.plsp_id) + '][Cisco-IOS-XR-infra-xtc-oper:tunnel-name = ' + str(self.tunnel_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.plsp_id is not None:
                    return True

                if self.tunnel_name is not None:
                    return True

                if self.brief_lsp_information is not None:
                    for child_ref in self.brief_lsp_information:
                        if child_ref._has_data():
                            return True

                if self.pcc_address is not None:
                    return True

                if self.tunnel_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.TunnelInfos.TunnelInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:tunnel-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_info is not None:
                for child_ref in self.tunnel_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.TunnelInfos']['meta_info']


    class PeerDetailInfos(object):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of    :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.peer_detail_info = YList()
            self.peer_detail_info.parent = self
            self.peer_detail_info.name = 'peer_detail_info'


        class PeerDetailInfo(object):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:   :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProtoEnum>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.detail_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self.peer_address_xr = None
                self.peer_protocol = None


            class DetailPcepInformation(object):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\:  str
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:   :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:   :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.brief_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self.error = None
                    self.keepalives = None
                    self.keychain_enabled = None
                    self.last_error_rx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self.last_error_tx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self.local_session_id = None
                    self.maximum_dead_interval = None
                    self.md5_enabled = None
                    self.minimum_keepalive_interval = None
                    self.negotiated_dead_time = None
                    self.negotiated_local_keepalive = None
                    self.negotiated_remote_keepalive = None
                    self.pce_error_rx = None
                    self.pce_error_tx = None
                    self.pce_initiate_rx = None
                    self.pce_initiate_tx = None
                    self.pce_keepalive_rx = None
                    self.pce_keepalive_tx = None
                    self.pce_open_rx = None
                    self.pce_open_tx = None
                    self.pce_reply_rx = None
                    self.pce_reply_tx = None
                    self.pce_report_rx = None
                    self.pce_report_tx = None
                    self.pce_request_rx = None
                    self.pce_request_tx = None
                    self.pce_update_rx = None
                    self.pce_update_tx = None
                    self.pcep_up_time = None
                    self.remote_session_id = None
                    self.speaker_id = None


                class BriefPcepInformation(object):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\:  bool
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:   :py:class:`PcepStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepStateEnum>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.capability_db_version = None
                        self.capability_delta_sync = None
                        self.capability_instantiate = None
                        self.capability_segment_routing = None
                        self.capability_triggered_sync = None
                        self.capability_update = None
                        self.pcep_state = None
                        self.stateful = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-pcep-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.capability_db_version is not None:
                            return True

                        if self.capability_delta_sync is not None:
                            return True

                        if self.capability_instantiate is not None:
                            return True

                        if self.capability_segment_routing is not None:
                            return True

                        if self.capability_triggered_sync is not None:
                            return True

                        if self.capability_update is not None:
                            return True

                        if self.pcep_state is not None:
                            return True

                        if self.stateful is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation']['meta_info']


                class LastErrorRx(object):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pc_error_type = None
                        self.pc_error_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:last-error-rx'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pc_error_type is not None:
                            return True

                        if self.pc_error_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx']['meta_info']


                class LastErrorTx(object):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pc_error_type = None
                        self.pc_error_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:last-error-tx'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pc_error_type is not None:
                            return True

                        if self.pc_error_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:detail-pcep-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.brief_pcep_information is not None and self.brief_pcep_information._has_data():
                        return True

                    if self.error is not None:
                        return True

                    if self.keepalives is not None:
                        return True

                    if self.keychain_enabled is not None:
                        return True

                    if self.last_error_rx is not None and self.last_error_rx._has_data():
                        return True

                    if self.last_error_tx is not None and self.last_error_tx._has_data():
                        return True

                    if self.local_session_id is not None:
                        return True

                    if self.maximum_dead_interval is not None:
                        return True

                    if self.md5_enabled is not None:
                        return True

                    if self.minimum_keepalive_interval is not None:
                        return True

                    if self.negotiated_dead_time is not None:
                        return True

                    if self.negotiated_local_keepalive is not None:
                        return True

                    if self.negotiated_remote_keepalive is not None:
                        return True

                    if self.pce_error_rx is not None:
                        return True

                    if self.pce_error_tx is not None:
                        return True

                    if self.pce_initiate_rx is not None:
                        return True

                    if self.pce_initiate_tx is not None:
                        return True

                    if self.pce_keepalive_rx is not None:
                        return True

                    if self.pce_keepalive_tx is not None:
                        return True

                    if self.pce_open_rx is not None:
                        return True

                    if self.pce_open_tx is not None:
                        return True

                    if self.pce_reply_rx is not None:
                        return True

                    if self.pce_reply_tx is not None:
                        return True

                    if self.pce_report_rx is not None:
                        return True

                    if self.pce_report_tx is not None:
                        return True

                    if self.pce_request_rx is not None:
                        return True

                    if self.pce_request_tx is not None:
                        return True

                    if self.pce_update_rx is not None:
                        return True

                    if self.pce_update_tx is not None:
                        return True

                    if self.pcep_up_time is not None:
                        return True

                    if self.remote_session_id is not None:
                        return True

                    if self.speaker_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:peer-detail-infos/Cisco-IOS-XR-infra-xtc-oper:peer-detail-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.detail_pcep_information is not None and self.detail_pcep_information._has_data():
                    return True

                if self.peer_address_xr is not None:
                    return True

                if self.peer_protocol is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.PeerDetailInfos.PeerDetailInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:peer-detail-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.peer_detail_info is not None:
                for child_ref in self.peer_detail_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.PeerDetailInfos']['meta_info']


    class TopologyNodes(object):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of    :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.topology_node = YList()
            self.topology_node.parent = self
            self.topology_node.name = 'topology_node'


        class TopologyNode(object):
            """
            Node information
            
            .. attribute:: node_identifier  <key>
            
            	Node Identifier
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of    :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of    :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\:  bool
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of    :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.PrefixSid>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.node_identifier = None
                self.ipv4_link = YList()
                self.ipv4_link.parent = self
                self.ipv4_link.name = 'ipv4_link'
                self.ipv6_link = YList()
                self.ipv6_link.parent = self
                self.ipv6_link.name = 'ipv6_link'
                self.node_identifier_xr = None
                self.node_protocol_identifier = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self.overload = None
                self.prefix_sid = YList()
                self.prefix_sid.parent = self
                self.prefix_sid.name = 'prefix_sid'


            class NodeProtocolIdentifier(object):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.igp_information = YList()
                    self.igp_information.parent = self
                    self.igp_information.name = 'igp_information'
                    self.ipv4bgp_router_id = None
                    self.ipv4bgp_router_id_set = None
                    self.ipv4te_router_id = None
                    self.ipv4te_router_id_set = None
                    self.node_name = None
                    self.srgb_information = YList()
                    self.srgb_information.parent = self
                    self.srgb_information.name = 'srgb_information'


                class IgpInformation(object):
                    """
                    IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info']


                class SrgbInformation(object):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_srgb = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self.size = None
                        self.start = None


                    class IgpSrgb(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_srgb is not None and self.igp_srgb._has_data():
                            return True

                        if self.size is not None:
                            return True

                        if self.start is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:node-protocol-identifier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.igp_information is not None:
                        for child_ref in self.igp_information:
                            if child_ref._has_data():
                                return True

                    if self.ipv4bgp_router_id is not None:
                        return True

                    if self.ipv4bgp_router_id_set is not None:
                        return True

                    if self.ipv4te_router_id is not None:
                        return True

                    if self.ipv4te_router_id_set is not None:
                        return True

                    if self.node_name is not None:
                        return True

                    if self.srgb_information is not None:
                        for child_ref in self.srgb_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']


            class PrefixSid(object):
                """
                Prefix SIDs
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: eflag
                
                	E Flag
                	**type**\:  bool
                
                .. attribute:: lflag
                
                	L Flag
                	**type**\:  bool
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nflag
                
                	N Flag
                	**type**\:  bool
                
                .. attribute:: pflag
                
                	P Flag
                	**type**\:  bool
                
                .. attribute:: rflag
                
                	R Flag
                	**type**\:  bool
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                
                .. attribute:: vflag
                
                	V Flag
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.domain_identifier = None
                    self.eflag = None
                    self.lflag = None
                    self.mpls_label = None
                    self.nflag = None
                    self.pflag = None
                    self.rflag = None
                    self.sid_prefix = Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix()
                    self.sid_prefix.parent = self
                    self.sid_type = None
                    self.vflag = None


                class SidPrefix(object):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.ipv4 is not None:
                            return True

                        if self.ipv6 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:prefix-sid'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain_identifier is not None:
                        return True

                    if self.eflag is not None:
                        return True

                    if self.lflag is not None:
                        return True

                    if self.mpls_label is not None:
                        return True

                    if self.nflag is not None:
                        return True

                    if self.pflag is not None:
                        return True

                    if self.rflag is not None:
                        return True

                    if self.sid_prefix is not None and self.sid_prefix._has_data():
                        return True

                    if self.sid_type is not None:
                        return True

                    if self.vflag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.PrefixSid']['meta_info']


            class Ipv4Link(object):
                """
                IPv4 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.adjacency_sid = YList()
                    self.adjacency_sid.parent = self
                    self.adjacency_sid.name = 'adjacency_sid'
                    self.igp_metric = None
                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self.local_ipv4_address = None
                    self.max_reservable_bandwidth = None
                    self.maximum_link_bandwidth = None
                    self.remote_ipv4_address = None
                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self.srlgs = YLeafList()
                    self.srlgs.parent = self
                    self.srlgs.name = 'srlgs'
                    self.te_metric = None


                class LocalIgpInformation(object):
                    """
                    Local node IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:local-igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(object):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_information = YList()
                        self.igp_information.parent = self
                        self.igp_information.name = 'igp_information'
                        self.ipv4bgp_router_id = None
                        self.ipv4bgp_router_id_set = None
                        self.ipv4te_router_id = None
                        self.ipv4te_router_id_set = None
                        self.node_name = None
                        self.srgb_information = YList()
                        self.srgb_information.parent = self
                        self.srgb_information.name = 'srgb_information'


                    class IgpInformation(object):
                        """
                        IGP information
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.domain_identifier = None
                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self


                        class Igp(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.domain_identifier is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']


                    class SrgbInformation(object):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.igp_srgb = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self.size = None
                            self.start = None


                        class IgpSrgb(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.igp_srgb is not None and self.igp_srgb._has_data():
                                return True

                            if self.size is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:remote-node-protocol-identifier'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_information is not None:
                            for child_ref in self.igp_information:
                                if child_ref._has_data():
                                    return True

                        if self.ipv4bgp_router_id is not None:
                            return True

                        if self.ipv4bgp_router_id_set is not None:
                            return True

                        if self.ipv4te_router_id is not None:
                            return True

                        if self.ipv4te_router_id_set is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.srgb_information is not None:
                            for child_ref in self.srgb_information:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']


                class AdjacencySid(object):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.eflag = None
                        self.lflag = None
                        self.mpls_label = None
                        self.nflag = None
                        self.pflag = None
                        self.rflag = None
                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self.sid_type = None
                        self.vflag = None


                    class SidPrefix(object):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:adjacency-sid'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.eflag is not None:
                            return True

                        if self.lflag is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.nflag is not None:
                            return True

                        if self.pflag is not None:
                            return True

                        if self.rflag is not None:
                            return True

                        if self.sid_prefix is not None and self.sid_prefix._has_data():
                            return True

                        if self.sid_type is not None:
                            return True

                        if self.vflag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ipv4-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.adjacency_sid is not None:
                        for child_ref in self.adjacency_sid:
                            if child_ref._has_data():
                                return True

                    if self.igp_metric is not None:
                        return True

                    if self.local_igp_information is not None and self.local_igp_information._has_data():
                        return True

                    if self.local_ipv4_address is not None:
                        return True

                    if self.max_reservable_bandwidth is not None:
                        return True

                    if self.maximum_link_bandwidth is not None:
                        return True

                    if self.remote_ipv4_address is not None:
                        return True

                    if self.remote_node_protocol_identifier is not None and self.remote_node_protocol_identifier._has_data():
                        return True

                    if self.srlgs is not None:
                        for child in self.srlgs:
                            if child is not None:
                                return True

                    if self.te_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']


            class Ipv6Link(object):
                """
                IPv6 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.adjacency_sid = YList()
                    self.adjacency_sid.parent = self
                    self.adjacency_sid.name = 'adjacency_sid'
                    self.igp_metric = None
                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self.local_ipv6_address = None
                    self.max_reservable_bandwidth = None
                    self.maximum_link_bandwidth = None
                    self.remote_ipv6_address = None
                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self.te_metric = None


                class LocalIgpInformation(object):
                    """
                    Local node IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:local-igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(object):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_information = YList()
                        self.igp_information.parent = self
                        self.igp_information.name = 'igp_information'
                        self.ipv4bgp_router_id = None
                        self.ipv4bgp_router_id_set = None
                        self.ipv4te_router_id = None
                        self.ipv4te_router_id_set = None
                        self.node_name = None
                        self.srgb_information = YList()
                        self.srgb_information.parent = self
                        self.srgb_information.name = 'srgb_information'


                    class IgpInformation(object):
                        """
                        IGP information
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.domain_identifier = None
                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self


                        class Igp(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.domain_identifier is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']


                    class SrgbInformation(object):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.igp_srgb = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self.size = None
                            self.start = None


                        class IgpSrgb(object):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self.igp_id = None
                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self


                            class Isis(object):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.system_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.system_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                            class Ospf(object):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.area = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                            class Bgp(object):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2016-05-31'

                                def __init__(self):
                                    self.parent = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bgp is not None and self.bgp._has_data():
                                    return True

                                if self.igp_id is not None:
                                    return True

                                if self.isis is not None and self.isis._has_data():
                                    return True

                                if self.ospf is not None and self.ospf._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.igp_srgb is not None and self.igp_srgb._has_data():
                                return True

                            if self.size is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:remote-node-protocol-identifier'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_information is not None:
                            for child_ref in self.igp_information:
                                if child_ref._has_data():
                                    return True

                        if self.ipv4bgp_router_id is not None:
                            return True

                        if self.ipv4bgp_router_id_set is not None:
                            return True

                        if self.ipv4te_router_id is not None:
                            return True

                        if self.ipv4te_router_id_set is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.srgb_information is not None:
                            for child_ref in self.srgb_information:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']


                class AdjacencySid(object):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`SidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.SidEnum>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.eflag = None
                        self.lflag = None
                        self.mpls_label = None
                        self.nflag = None
                        self.pflag = None
                        self.rflag = None
                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self.sid_type = None
                        self.vflag = None


                    class SidPrefix(object):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sid-prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:adjacency-sid'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.eflag is not None:
                            return True

                        if self.lflag is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.nflag is not None:
                            return True

                        if self.pflag is not None:
                            return True

                        if self.rflag is not None:
                            return True

                        if self.sid_prefix is not None and self.sid_prefix._has_data():
                            return True

                        if self.sid_type is not None:
                            return True

                        if self.vflag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ipv6-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.adjacency_sid is not None:
                        for child_ref in self.adjacency_sid:
                            if child_ref._has_data():
                                return True

                    if self.igp_metric is not None:
                        return True

                    if self.local_igp_information is not None and self.local_igp_information._has_data():
                        return True

                    if self.local_ipv6_address is not None:
                        return True

                    if self.max_reservable_bandwidth is not None:
                        return True

                    if self.maximum_link_bandwidth is not None:
                        return True

                    if self.remote_ipv6_address is not None:
                        return True

                    if self.remote_node_protocol_identifier is not None and self.remote_node_protocol_identifier._has_data():
                        return True

                    if self.te_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']

            @property
            def _common_path(self):
                if self.node_identifier is None:
                    raise YPYModelError('Key property node_identifier is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:topology-nodes/Cisco-IOS-XR-infra-xtc-oper:topology-node[Cisco-IOS-XR-infra-xtc-oper:node-identifier = ' + str(self.node_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_identifier is not None:
                    return True

                if self.ipv4_link is not None:
                    for child_ref in self.ipv4_link:
                        if child_ref._has_data():
                            return True

                if self.ipv6_link is not None:
                    for child_ref in self.ipv6_link:
                        if child_ref._has_data():
                            return True

                if self.node_identifier_xr is not None:
                    return True

                if self.node_protocol_identifier is not None and self.node_protocol_identifier._has_data():
                    return True

                if self.overload is not None:
                    return True

                if self.prefix_sid is not None:
                    for child_ref in self.prefix_sid:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.TopologyNodes.TopologyNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:topology-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.topology_node is not None:
                for child_ref in self.topology_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.TopologyNodes']['meta_info']


    class PrefixInfos(object):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of    :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.prefix_info = YList()
            self.prefix_info.parent = self
            self.prefix_info.name = 'prefix_info'


        class PrefixInfo(object):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  <key>
            
            	Node ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.Address>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.node_identifier = None
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.node_identifier_xr = None
                self.node_protocol_identifier = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self


            class NodeProtocolIdentifier(object):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.igp_information = YList()
                    self.igp_information.parent = self
                    self.igp_information.name = 'igp_information'
                    self.ipv4bgp_router_id = None
                    self.ipv4bgp_router_id_set = None
                    self.ipv4te_router_id = None
                    self.ipv4te_router_id_set = None
                    self.node_name = None
                    self.srgb_information = YList()
                    self.srgb_information.parent = self
                    self.srgb_information.name = 'srgb_information'


                class IgpInformation(object):
                    """
                    IGP information
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.domain_identifier = None
                        self.igp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self


                    class Igp(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_identifier is not None:
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info']


                class SrgbInformation(object):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.igp_srgb = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self.size = None
                        self.start = None


                    class IgpSrgb(object):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoIdEnum>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self.igp_id = None
                            self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self


                        class Isis(object):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.system_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:isis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info']


                        class Ospf(object):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.area = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info']


                        class Bgp(object):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:bgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                                return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:igp-srgb'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bgp is not None and self.bgp._has_data():
                                return True

                            if self.igp_id is not None:
                                return True

                            if self.isis is not None and self.isis._has_data():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:srgb-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.igp_srgb is not None and self.igp_srgb._has_data():
                            return True

                        if self.size is not None:
                            return True

                        if self.start is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:node-protocol-identifier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.igp_information is not None:
                        for child_ref in self.igp_information:
                            if child_ref._has_data():
                                return True

                    if self.ipv4bgp_router_id is not None:
                        return True

                    if self.ipv4bgp_router_id_set is not None:
                        return True

                    if self.ipv4te_router_id is not None:
                        return True

                    if self.ipv4te_router_id_set is not None:
                        return True

                    if self.node_name is not None:
                        return True

                    if self.srgb_information is not None:
                        for child_ref in self.srgb_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']


            class Address(object):
                """
                Prefix address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`PceAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfIdEnum>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.ipv4 is not None:
                        return True

                    if self.ipv6 is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.PrefixInfos.PrefixInfo.Address']['meta_info']

            @property
            def _common_path(self):
                if self.node_identifier is None:
                    raise YPYModelError('Key property node_identifier is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:prefix-infos/Cisco-IOS-XR-infra-xtc-oper:prefix-info[Cisco-IOS-XR-infra-xtc-oper:node-identifier = ' + str(self.node_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_identifier is not None:
                    return True

                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.node_identifier_xr is not None:
                    return True

                if self.node_protocol_identifier is not None and self.node_protocol_identifier._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.PrefixInfos.PrefixInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:prefix-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.prefix_info is not None:
                for child_ref in self.prefix_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.PrefixInfos']['meta_info']


    class LspSummary(object):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:   :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of    :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.all_ls_ps = Pce.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self.peer_ls_ps_info = YList()
            self.peer_ls_ps_info.parent = self
            self.peer_ls_ps_info.name = 'peer_ls_ps_info'


        class AllLsPs(object):
            """
            Summary for all peers
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.admin_up_ls_ps = None
                self.all_ls_ps = None
                self.rsvp_ls_ps = None
                self.sr_ls_ps = None
                self.up_ls_ps = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:all-ls-ps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.admin_up_ls_ps is not None:
                    return True

                if self.all_ls_ps is not None:
                    return True

                if self.rsvp_ls_ps is not None:
                    return True

                if self.sr_ls_ps is not None:
                    return True

                if self.up_ls_ps is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.LspSummary.AllLsPs']['meta_info']


        class PeerLsPsInfo(object):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:   :py:class:`LspSummary_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo.LspSummary_>`
            
            .. attribute:: peer_address
            
            	Peer IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.lsp_summary = Pce.LspSummary.PeerLsPsInfo.LspSummary_()
                self.lsp_summary.parent = self
                self.peer_address = None


            class LspSummary_(object):
                """
                Number of LSPs for specific peer
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.admin_up_ls_ps = None
                    self.all_ls_ps = None
                    self.rsvp_ls_ps = None
                    self.sr_ls_ps = None
                    self.up_ls_ps = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:peer-ls-ps-info/Cisco-IOS-XR-infra-xtc-oper:lsp-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_up_ls_ps is not None:
                        return True

                    if self.all_ls_ps is not None:
                        return True

                    if self.rsvp_ls_ps is not None:
                        return True

                    if self.sr_ls_ps is not None:
                        return True

                    if self.up_ls_ps is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.LspSummary.PeerLsPsInfo.LspSummary_']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:lsp-summary/Cisco-IOS-XR-infra-xtc-oper:peer-ls-ps-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.lsp_summary is not None and self.lsp_summary._has_data():
                    return True

                if self.peer_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.LspSummary.PeerLsPsInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:lsp-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.all_ls_ps is not None and self.all_ls_ps._has_data():
                return True

            if self.peer_ls_ps_info is not None:
                for child_ref in self.peer_ls_ps_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.LspSummary']['meta_info']


    class PeerInfos(object):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of    :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.peer_info = YList()
            self.peer_info.parent = self
            self.peer_info.name = 'peer_info'


        class PeerInfo(object):
            """
            PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProtoEnum>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.brief_pcep_information = Pce.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self.peer_address_xr = None
                self.peer_protocol = None


            class BriefPcepInformation(object):
                """
                PCE protocol information
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\:  bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\:  bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\:  bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\:  bool
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:   :py:class:`PcepStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepStateEnum>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.capability_db_version = None
                    self.capability_delta_sync = None
                    self.capability_instantiate = None
                    self.capability_segment_routing = None
                    self.capability_triggered_sync = None
                    self.capability_update = None
                    self.pcep_state = None
                    self.stateful = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-pcep-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.capability_db_version is not None:
                        return True

                    if self.capability_delta_sync is not None:
                        return True

                    if self.capability_instantiate is not None:
                        return True

                    if self.capability_segment_routing is not None:
                        return True

                    if self.capability_triggered_sync is not None:
                        return True

                    if self.capability_update is not None:
                        return True

                    if self.pcep_state is not None:
                        return True

                    if self.stateful is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.PeerInfos.PeerInfo.BriefPcepInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:peer-infos/Cisco-IOS-XR-infra-xtc-oper:peer-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.brief_pcep_information is not None and self.brief_pcep_information._has_data():
                    return True

                if self.peer_address_xr is not None:
                    return True

                if self.peer_protocol is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.PeerInfos.PeerInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:peer-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.peer_info is not None:
                for child_ref in self.peer_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.PeerInfos']['meta_info']


    class TunnelDetailInfos(object):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of    :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.tunnel_detail_info = YList()
            self.tunnel_detail_info.parent = self
            self.tunnel_detail_info.name = 'tunnel_detail_info'


        class TunnelDetailInfo(object):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of    :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:   :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.detail_lsp_information = YList()
                self.detail_lsp_information.parent = self
                self.detail_lsp_information.name = 'detail_lsp_information'
                self.pcc_address = None
                self.private_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self.tunnel_name_xr = None


            class PrivateLspInformation(object):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of    :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.event_buffer = YList()
                    self.event_buffer.parent = self
                    self.event_buffer.name = 'event_buffer'


                class EventBuffer(object):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\:  str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.event_message = None
                        self.time_stamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:event-buffer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.event_message is not None:
                            return True

                        if self.time_stamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:private-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.event_buffer is not None:
                        for child_ref in self.event_buffer:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info']


            class DetailLspInformation(object):
                """
                Detail LSP information
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\:  bool
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:   :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:   :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:   :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:   :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:   :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of    :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\:  bool
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.actual_bandwidth = None
                    self.actual_bandwidth_specified = None
                    self.brief_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self.computing_pce = None
                    self.er_os = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self.lsp_association_info = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self.lsp_attributes = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self.lsp_role = None
                    self.lsppcep_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self.reporting_pcc_address = None
                    self.rro = YList()
                    self.rro.parent = self
                    self.rro.name = 'rro'
                    self.signaled_bandwidth = None
                    self.signaled_bandwidth_specified = None
                    self.srlg_info = YLeafList()
                    self.srlg_info.parent = self
                    self.srlg_info.name = 'srlg_info'
                    self.state_sync_pce = None
                    self.sub_delegated_pce = None


                class BriefLspInformation(object):
                    """
                    Brief LSP information
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:   :py:class:`LspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspStateEnum>`
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:   :py:class:`LspSetupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetupEnum>`
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:   :py:class:`PcepLspStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspStateEnum>`
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.administrative_state = None
                        self.binding_sid = None
                        self.destination_address = None
                        self.lsp_setup_type = None
                        self.lspid = None
                        self.operational_state = None
                        self.source_address = None
                        self.tunnel_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:brief-lsp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.administrative_state is not None:
                            return True

                        if self.binding_sid is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.lsp_setup_type is not None:
                            return True

                        if self.lspid is not None:
                            return True

                        if self.operational_state is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation']['meta_info']


                class ErOs(object):
                    """
                    Paths
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of    :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of    :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of    :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of    :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.computed_hop_list_time = None
                        self.computed_metric_type = None
                        self.computed_metric_value = None
                        self.computed_rsvp_path = YList()
                        self.computed_rsvp_path.parent = self
                        self.computed_rsvp_path.name = 'computed_rsvp_path'
                        self.computed_sr_path = YList()
                        self.computed_sr_path.parent = self
                        self.computed_sr_path.name = 'computed_sr_path'
                        self.reported_metric_type = None
                        self.reported_metric_value = None
                        self.reported_rsvp_path = YList()
                        self.reported_rsvp_path.parent = self
                        self.reported_rsvp_path.name = 'reported_rsvp_path'
                        self.reported_sr_path = YList()
                        self.reported_sr_path.parent = self
                        self.reported_sr_path.name = 'reported_sr_path'


                    class ReportedRsvpPath(object):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:reported-rsvp-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath']['meta_info']


                    class ReportedSrPath(object):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:reported-sr-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath']['meta_info']


                    class ComputedRsvpPath(object):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:computed-rsvp-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath']['meta_info']


                    class ComputedSrPath(object):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:computed-sr-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:er-os'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.computed_hop_list_time is not None:
                            return True

                        if self.computed_metric_type is not None:
                            return True

                        if self.computed_metric_value is not None:
                            return True

                        if self.computed_rsvp_path is not None:
                            for child_ref in self.computed_rsvp_path:
                                if child_ref._has_data():
                                    return True

                        if self.computed_sr_path is not None:
                            for child_ref in self.computed_sr_path:
                                if child_ref._has_data():
                                    return True

                        if self.reported_metric_type is not None:
                            return True

                        if self.reported_metric_value is not None:
                            return True

                        if self.reported_rsvp_path is not None:
                            for child_ref in self.reported_rsvp_path:
                                if child_ref._has_data():
                                    return True

                        if self.reported_sr_path is not None:
                            for child_ref in self.reported_sr_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']


                class LsppcepInformation(object):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\:  bool
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:   :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.pcep_flag_a = None
                        self.pcep_flag_d = None
                        self.pcep_flag_o = None
                        self.pcep_flag_r = None
                        self.pcep_flag_s = None
                        self.pcepid = None
                        self.rsvp_error = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self


                    class RsvpError(object):
                        """
                        RSVP error info
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.error_code = None
                            self.error_flags = None
                            self.error_value = None
                            self.node_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:rsvp-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.error_code is not None:
                                return True

                            if self.error_flags is not None:
                                return True

                            if self.error_value is not None:
                                return True

                            if self.node_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsppcep-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcep_flag_a is not None:
                            return True

                        if self.pcep_flag_d is not None:
                            return True

                        if self.pcep_flag_o is not None:
                            return True

                        if self.pcep_flag_r is not None:
                            return True

                        if self.pcep_flag_s is not None:
                            return True

                        if self.pcepid is not None:
                            return True

                        if self.rsvp_error is not None and self.rsvp_error._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info']


                class LspAssociationInfo(object):
                    """
                    LSP association information
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.association_id = None
                        self.association_source = None
                        self.association_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsp-association-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.association_id is not None:
                            return True

                        if self.association_source is not None:
                            return True

                        if self.association_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo']['meta_info']


                class LspAttributes(object):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\:  bool
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.affinity_exclude_any = None
                        self.affinity_include_all = None
                        self.affinity_include_any = None
                        self.hold_priority = None
                        self.local_protection = None
                        self.setup_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:lsp-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.affinity_exclude_any is not None:
                            return True

                        if self.affinity_include_all is not None:
                            return True

                        if self.affinity_include_any is not None:
                            return True

                        if self.hold_priority is not None:
                            return True

                        if self.local_protection is not None:
                            return True

                        if self.setup_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes']['meta_info']


                class Rro(object):
                    """
                    RRO
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:   :py:class:`PceRroEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRroEnum>`
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:   :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.flags = None
                        self.ipv4_address = None
                        self.mpls_label = None
                        self.rro_type = None
                        self.sr_rro = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self


                    class SrRro(object):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSidEnum>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.local_addr = None
                            self.mpls_label = None
                            self.remote_addr = None
                            self.sid_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:sr-rro'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_addr is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.sid_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                            return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:rro'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.flags is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.rro_type is not None:
                            return True

                        if self.sr_rro is not None and self.sr_rro._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                        return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-oper:detail-lsp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.actual_bandwidth is not None:
                        return True

                    if self.actual_bandwidth_specified is not None:
                        return True

                    if self.brief_lsp_information is not None and self.brief_lsp_information._has_data():
                        return True

                    if self.computing_pce is not None:
                        return True

                    if self.er_os is not None and self.er_os._has_data():
                        return True

                    if self.lsp_association_info is not None and self.lsp_association_info._has_data():
                        return True

                    if self.lsp_attributes is not None and self.lsp_attributes._has_data():
                        return True

                    if self.lsp_role is not None:
                        return True

                    if self.lsppcep_information is not None and self.lsppcep_information._has_data():
                        return True

                    if self.reporting_pcc_address is not None:
                        return True

                    if self.rro is not None:
                        for child_ref in self.rro:
                            if child_ref._has_data():
                                return True

                    if self.signaled_bandwidth is not None:
                        return True

                    if self.signaled_bandwidth_specified is not None:
                        return True

                    if self.srlg_info is not None:
                        for child in self.srlg_info:
                            if child is not None:
                                return True

                    if self.state_sync_pce is not None:
                        return True

                    if self.sub_delegated_pce is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                    return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']

            @property
            def _common_path(self):
                if self.peer_address is None:
                    raise YPYModelError('Key property peer_address is None')
                if self.plsp_id is None:
                    raise YPYModelError('Key property plsp_id is None')
                if self.tunnel_name is None:
                    raise YPYModelError('Key property tunnel_name is None')

                return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-infos/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-info[Cisco-IOS-XR-infra-xtc-oper:peer-address = ' + str(self.peer_address) + '][Cisco-IOS-XR-infra-xtc-oper:plsp-id = ' + str(self.plsp_id) + '][Cisco-IOS-XR-infra-xtc-oper:tunnel-name = ' + str(self.tunnel_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_address is not None:
                    return True

                if self.plsp_id is not None:
                    return True

                if self.tunnel_name is not None:
                    return True

                if self.detail_lsp_information is not None:
                    for child_ref in self.detail_lsp_information:
                        if child_ref._has_data():
                            return True

                if self.pcc_address is not None:
                    return True

                if self.private_lsp_information is not None and self.private_lsp_information._has_data():
                    return True

                if self.tunnel_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
                return meta._meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-oper:pce/Cisco-IOS-XR-infra-xtc-oper:tunnel-detail-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_detail_info is not None:
                for child_ref in self.tunnel_detail_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
            return meta._meta_table['Pce.TunnelDetailInfos']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-xtc-oper:pce'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.association_infos is not None and self.association_infos._has_data():
            return True

        if self.lsp_summary is not None and self.lsp_summary._has_data():
            return True

        if self.peer_detail_infos is not None and self.peer_detail_infos._has_data():
            return True

        if self.peer_infos is not None and self.peer_infos._has_data():
            return True

        if self.prefix_infos is not None and self.prefix_infos._has_data():
            return True

        if self.topology_nodes is not None and self.topology_nodes._has_data():
            return True

        if self.topology_summary is not None and self.topology_summary._has_data():
            return True

        if self.tunnel_detail_infos is not None and self.tunnel_detail_infos._has_data():
            return True

        if self.tunnel_infos is not None and self.tunnel_infos._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_oper as meta
        return meta._meta_table['Pce']['meta_info']


