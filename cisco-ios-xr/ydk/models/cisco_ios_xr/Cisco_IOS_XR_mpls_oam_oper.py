""" Cisco_IOS_XR_mpls_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package operational data.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS OAM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LspvBagInterfaceStateEnum(Enum):
    """
    LspvBagInterfaceStateEnum

    LSPV interface state

    .. data:: not_ready = 0

    	Not ready

    .. data:: admin_down = 1

    	Admin down

    .. data:: down = 2

    	Down

    .. data:: up = 3

    	UP

    .. data:: shutdown = 4

    	Shutdown

    .. data:: error_disable = 5

    	Error disable

    .. data:: down_immediate = 6

    	Immediate down

    .. data:: admin_immediate = 7

    	Immediate admin

    .. data:: graceful_down = 8

    	Graceful down

    .. data:: begin_shutdown = 9

    	Begin shutdown

    .. data:: end_shutdown = 10

    	End shutdown

    .. data:: begin_error_disable = 11

    	Begin error disable

    .. data:: end_error_disable = 12

    	End error disable

    .. data:: begin_graceful_down = 13

    	Begin graceful down

    .. data:: reset = 14

    	Reset

    .. data:: operational = 15

    	Operational

    .. data:: not_operational = 16

    	Not operational

    .. data:: not_known = 17

    	Unknown

    """

    not_ready = 0

    admin_down = 1

    down = 2

    up = 3

    shutdown = 4

    error_disable = 5

    down_immediate = 6

    admin_immediate = 7

    graceful_down = 8

    begin_shutdown = 9

    end_shutdown = 10

    begin_error_disable = 11

    end_error_disable = 12

    begin_graceful_down = 13

    reset = 14

    operational = 15

    not_operational = 16

    not_known = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
        return meta._meta_table['LspvBagInterfaceStateEnum']



class MplsOam(object):
    """
    MPLS OAM operational data
    
    .. attribute:: global_
    
    	LSPV global counters operational data
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_>`
    
    .. attribute:: interface
    
    	MPLS OAM interface operational data
    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface>`
    
    .. attribute:: packet
    
    	LSPV packet counters operational data
    	**type**\:   :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet>`
    
    

    """

    _prefix = 'mpls-oam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_ = MplsOam.Global_()
        self.global_.parent = self
        self.interface = MplsOam.Interface()
        self.interface.parent = self
        self.packet = MplsOam.Packet()
        self.packet.parent = self


    class Interface(object):
        """
        MPLS OAM interface operational data
        
        .. attribute:: briefs
        
        	MPLS OAM interface detail data
        	**type**\:   :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs>`
        
        .. attribute:: details
        
        	MPLS OAM interface detail data
        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.briefs = MplsOam.Interface.Briefs()
            self.briefs.parent = self
            self.details = MplsOam.Interface.Details()
            self.details.parent = self


        class Briefs(object):
            """
            MPLS OAM interface detail data
            
            .. attribute:: brief
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs.Brief>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.brief = YList()
                self.brief.parent = self
                self.brief.name = 'brief'


            class Brief(object):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name_xr
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mtu
                
                	Interface MTU
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length (IPv4)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length_v6
                
                	Prefix length (IPv6)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: primary_address
                
                	Primary interface address (IPv4)
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: primary_address_v6
                
                	Primary interface address (IPv6)
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: state
                
                	Interface state
                	**type**\:   :py:class:`LspvBagInterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceStateEnum>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.interface_name_xr = None
                    self.mtu = None
                    self.prefix_length = None
                    self.prefix_length_v6 = None
                    self.primary_address = None
                    self.primary_address_v6 = None
                    self.state = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:interface/Cisco-IOS-XR-mpls-oam-oper:briefs/Cisco-IOS-XR-mpls-oam-oper:brief[Cisco-IOS-XR-mpls-oam-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface_name_xr is not None:
                        return True

                    if self.mtu is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    if self.prefix_length_v6 is not None:
                        return True

                    if self.primary_address is not None:
                        return True

                    if self.primary_address_v6 is not None:
                        return True

                    if self.state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Interface.Briefs.Brief']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:interface/Cisco-IOS-XR-mpls-oam-oper:briefs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.brief is not None:
                    for child_ref in self.brief:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Interface.Briefs']['meta_info']


        class Details(object):
            """
            MPLS OAM interface detail data
            
            .. attribute:: detail
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.detail = YList()
                self.detail.parent = self
                self.detail.name = 'detail'


            class Detail(object):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_brief
                
                	Interface brief
                	**type**\:   :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.InterfaceBrief>`
                
                .. attribute:: packet_statistics
                
                	Packet statistics
                	**type**\:   :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.interface_brief = MplsOam.Interface.Details.Detail.InterfaceBrief()
                    self.interface_brief.parent = self
                    self.packet_statistics = MplsOam.Interface.Details.Detail.PacketStatistics()
                    self.packet_statistics.parent = self


                class InterfaceBrief(object):
                    """
                    Interface brief
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	Interface MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length (IPv4)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length_v6
                    
                    	Prefix length (IPv6)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: primary_address
                    
                    	Primary interface address (IPv4)
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: primary_address_v6
                    
                    	Primary interface address (IPv6)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`LspvBagInterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceStateEnum>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name_xr = None
                        self.mtu = None
                        self.prefix_length = None
                        self.prefix_length_v6 = None
                        self.primary_address = None
                        self.primary_address_v6 = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:interface-brief'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name_xr is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.prefix_length_v6 is not None:
                            return True

                        if self.primary_address is not None:
                            return True

                        if self.primary_address_v6 is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                        return meta._meta_table['MplsOam.Interface.Details.Detail.InterfaceBrief']['meta_info']


                class PacketStatistics(object):
                    """
                    Packet statistics
                    
                    .. attribute:: protect_rep_sent
                    
                    	Protect Reply Packet transmit counts
                    	**type**\:   :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent>`
                    
                    .. attribute:: protect_req_sent
                    
                    	Protect Request Packet transmit counts
                    	**type**\:   :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent>`
                    
                    .. attribute:: received
                    
                    	Packet reception counts
                    	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received>`
                    
                    .. attribute:: sent
                    
                    	Packet transmit counts
                    	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent>`
                    
                    .. attribute:: working_rep_sent
                    
                    	Working Reply Packet transmit counts
                    	**type**\:   :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent>`
                    
                    .. attribute:: working_req_sent
                    
                    	Working Request Packet transmit counts
                    	**type**\:   :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protect_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent()
                        self.protect_rep_sent.parent = self
                        self.protect_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent()
                        self.protect_req_sent.parent = self
                        self.received = MplsOam.Interface.Details.Detail.PacketStatistics.Received()
                        self.received.parent = self
                        self.sent = MplsOam.Interface.Details.Detail.PacketStatistics.Sent()
                        self.sent.parent = self
                        self.working_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent()
                        self.working_rep_sent.parent = self
                        self.working_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent()
                        self.working_req_sent.parent = self


                    class Received(object):
                        """
                        Packet reception counts
                        
                        .. attribute:: protect_protocol_received_good_reply
                        
                        	Protect Protocol Received good reply
                        	**type**\:   :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply>`
                        
                        .. attribute:: protect_protocol_received_good_request
                        
                        	Protect Protocol Received good request
                        	**type**\:   :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest>`
                        
                        .. attribute:: received_error_general
                        
                        	General error
                        	**type**\:   :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral>`
                        
                        .. attribute:: received_error_ip_header
                        
                        	IP header error
                        	**type**\:   :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader>`
                        
                        .. attribute:: received_error_no_interface
                        
                        	Error no Interfaces
                        	**type**\:   :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface>`
                        
                        .. attribute:: received_error_no_memory
                        
                        	Error no memory
                        	**type**\:   :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory>`
                        
                        .. attribute:: received_error_queue_full
                        
                        	Dropped queue full
                        	**type**\:   :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull>`
                        
                        .. attribute:: received_error_runt
                        
                        	RUNT error
                        	**type**\:   :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt>`
                        
                        .. attribute:: received_error_udp_header
                        
                        	UDP header error
                        	**type**\:   :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader>`
                        
                        .. attribute:: received_good_bfd_reply
                        
                        	Received Reply with BFD TLV
                        	**type**\:   :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply>`
                        
                        .. attribute:: received_good_bfd_request
                        
                        	Received Reqeust with BFD TLV
                        	**type**\:   :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest>`
                        
                        .. attribute:: received_good_reply
                        
                        	Received good reply
                        	**type**\:   :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply>`
                        
                        .. attribute:: received_good_request
                        
                        	Received good request
                        	**type**\:   :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest>`
                        
                        .. attribute:: received_unknown
                        
                        	Received unknown packets
                        	**type**\:   :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.protect_protocol_received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply()
                            self.protect_protocol_received_good_reply.parent = self
                            self.protect_protocol_received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest()
                            self.protect_protocol_received_good_request.parent = self
                            self.received_error_general = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral()
                            self.received_error_general.parent = self
                            self.received_error_ip_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader()
                            self.received_error_ip_header.parent = self
                            self.received_error_no_interface = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface()
                            self.received_error_no_interface.parent = self
                            self.received_error_no_memory = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory()
                            self.received_error_no_memory.parent = self
                            self.received_error_queue_full = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull()
                            self.received_error_queue_full.parent = self
                            self.received_error_runt = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt()
                            self.received_error_runt.parent = self
                            self.received_error_udp_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader()
                            self.received_error_udp_header.parent = self
                            self.received_good_bfd_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply()
                            self.received_good_bfd_reply.parent = self
                            self.received_good_bfd_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest()
                            self.received_good_bfd_request.parent = self
                            self.received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply()
                            self.received_good_reply.parent = self
                            self.received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest()
                            self.received_good_request.parent = self
                            self.received_unknown = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown()
                            self.received_unknown.parent = self


                        class ReceivedGoodRequest(object):
                            """
                            Received good request
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-good-request'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest']['meta_info']


                        class ReceivedGoodReply(object):
                            """
                            Received good reply
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-good-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply']['meta_info']


                        class ReceivedUnknown(object):
                            """
                            Received unknown packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-unknown'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown']['meta_info']


                        class ReceivedErrorIpHeader(object):
                            """
                            IP header error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-ip-header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader']['meta_info']


                        class ReceivedErrorUdpHeader(object):
                            """
                            UDP header error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-udp-header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader']['meta_info']


                        class ReceivedErrorRunt(object):
                            """
                            RUNT error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-runt'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt']['meta_info']


                        class ReceivedErrorQueueFull(object):
                            """
                            Dropped queue full
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-queue-full'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull']['meta_info']


                        class ReceivedErrorGeneral(object):
                            """
                            General error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-general'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral']['meta_info']


                        class ReceivedErrorNoInterface(object):
                            """
                            Error no Interfaces
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-no-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface']['meta_info']


                        class ReceivedErrorNoMemory(object):
                            """
                            Error no memory
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-error-no-memory'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory']['meta_info']


                        class ProtectProtocolReceivedGoodRequest(object):
                            """
                            Protect Protocol Received good request
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:protect-protocol-received-good-request'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest']['meta_info']


                        class ProtectProtocolReceivedGoodReply(object):
                            """
                            Protect Protocol Received good reply
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:protect-protocol-received-good-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply']['meta_info']


                        class ReceivedGoodBfdRequest(object):
                            """
                            Received Reqeust with BFD TLV
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-good-bfd-request'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest']['meta_info']


                        class ReceivedGoodBfdReply(object):
                            """
                            Received Reply with BFD TLV
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received-good-bfd-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply._has_data():
                                return True

                            if self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request._has_data():
                                return True

                            if self.received_error_general is not None and self.received_error_general._has_data():
                                return True

                            if self.received_error_ip_header is not None and self.received_error_ip_header._has_data():
                                return True

                            if self.received_error_no_interface is not None and self.received_error_no_interface._has_data():
                                return True

                            if self.received_error_no_memory is not None and self.received_error_no_memory._has_data():
                                return True

                            if self.received_error_queue_full is not None and self.received_error_queue_full._has_data():
                                return True

                            if self.received_error_runt is not None and self.received_error_runt._has_data():
                                return True

                            if self.received_error_udp_header is not None and self.received_error_udp_header._has_data():
                                return True

                            if self.received_good_bfd_reply is not None and self.received_good_bfd_reply._has_data():
                                return True

                            if self.received_good_bfd_request is not None and self.received_good_bfd_request._has_data():
                                return True

                            if self.received_good_reply is not None and self.received_good_reply._has_data():
                                return True

                            if self.received_good_request is not None and self.received_good_request._has_data():
                                return True

                            if self.received_unknown is not None and self.received_unknown._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']


                    class Sent(object):
                        """
                        Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood()
                            self.transmit_good.parent = self


                        class TransmitGood(object):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood']['meta_info']


                        class TransmitDrop(object):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(object):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(object):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                                return True

                            if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                                return True

                            if self.transmit_drop is not None and self.transmit_drop._has_data():
                                return True

                            if self.transmit_good is not None and self.transmit_good._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']


                    class WorkingReqSent(object):
                        """
                        Working Request Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood()
                            self.transmit_good.parent = self


                        class TransmitGood(object):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood']['meta_info']


                        class TransmitDrop(object):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(object):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(object):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:working-req-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                                return True

                            if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                                return True

                            if self.transmit_drop is not None and self.transmit_drop._has_data():
                                return True

                            if self.transmit_good is not None and self.transmit_good._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']


                    class WorkingRepSent(object):
                        """
                        Working Reply Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood()
                            self.transmit_good.parent = self


                        class TransmitGood(object):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood']['meta_info']


                        class TransmitDrop(object):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(object):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(object):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                                return True

                            if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                                return True

                            if self.transmit_drop is not None and self.transmit_drop._has_data():
                                return True

                            if self.transmit_good is not None and self.transmit_good._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']


                    class ProtectReqSent(object):
                        """
                        Protect Request Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood()
                            self.transmit_good.parent = self


                        class TransmitGood(object):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood']['meta_info']


                        class TransmitDrop(object):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(object):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(object):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                                return True

                            if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                                return True

                            if self.transmit_drop is not None and self.transmit_drop._has_data():
                                return True

                            if self.transmit_good is not None and self.transmit_good._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']


                    class ProtectRepSent(object):
                        """
                        Protect Reply Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood()
                            self.transmit_good.parent = self


                        class TransmitGood(object):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood']['meta_info']


                        class TransmitDrop(object):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(object):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(object):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bytes = None
                                self.packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bytes is not None:
                                    return True

                                if self.packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                                return True

                            if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                                return True

                            if self.transmit_drop is not None and self.transmit_drop._has_data():
                                return True

                            if self.transmit_good is not None and self.transmit_good._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-oam-oper:packet-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.protect_rep_sent is not None and self.protect_rep_sent._has_data():
                            return True

                        if self.protect_req_sent is not None and self.protect_req_sent._has_data():
                            return True

                        if self.received is not None and self.received._has_data():
                            return True

                        if self.sent is not None and self.sent._has_data():
                            return True

                        if self.working_rep_sent is not None and self.working_rep_sent._has_data():
                            return True

                        if self.working_req_sent is not None and self.working_req_sent._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                        return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:interface/Cisco-IOS-XR-mpls-oam-oper:details/Cisco-IOS-XR-mpls-oam-oper:detail[Cisco-IOS-XR-mpls-oam-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface_brief is not None and self.interface_brief._has_data():
                        return True

                    if self.packet_statistics is not None and self.packet_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Interface.Details.Detail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:interface/Cisco-IOS-XR-mpls-oam-oper:details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.detail is not None:
                    for child_ref in self.detail:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Interface.Details']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:interface'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.briefs is not None and self.briefs._has_data():
                return True

            if self.details is not None and self.details._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Interface']['meta_info']


    class Packet(object):
        """
        LSPV packet counters operational data
        
        .. attribute:: protect_rep_sent
        
        	Protect Reply Packet transmit counts
        	**type**\:   :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent>`
        
        .. attribute:: protect_req_sent
        
        	Protect Request Packet transmit counts
        	**type**\:   :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent>`
        
        .. attribute:: received
        
        	Packet reception counts
        	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received>`
        
        .. attribute:: sent
        
        	Packet transmit counts
        	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent>`
        
        .. attribute:: working_rep_sent
        
        	Working Reply Packet transmit counts
        	**type**\:   :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent>`
        
        .. attribute:: working_req_sent
        
        	Working Request Packet transmit counts
        	**type**\:   :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.protect_rep_sent = MplsOam.Packet.ProtectRepSent()
            self.protect_rep_sent.parent = self
            self.protect_req_sent = MplsOam.Packet.ProtectReqSent()
            self.protect_req_sent.parent = self
            self.received = MplsOam.Packet.Received()
            self.received.parent = self
            self.sent = MplsOam.Packet.Sent()
            self.sent.parent = self
            self.working_rep_sent = MplsOam.Packet.WorkingRepSent()
            self.working_rep_sent.parent = self
            self.working_req_sent = MplsOam.Packet.WorkingReqSent()
            self.working_req_sent.parent = self


        class Received(object):
            """
            Packet reception counts
            
            .. attribute:: protect_protocol_received_good_reply
            
            	Protect Protocol Received good reply
            	**type**\:   :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply>`
            
            .. attribute:: protect_protocol_received_good_request
            
            	Protect Protocol Received good request
            	**type**\:   :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest>`
            
            .. attribute:: received_error_general
            
            	General error
            	**type**\:   :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorGeneral>`
            
            .. attribute:: received_error_ip_header
            
            	IP header error
            	**type**\:   :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorIpHeader>`
            
            .. attribute:: received_error_no_interface
            
            	Error no Interfaces
            	**type**\:   :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoInterface>`
            
            .. attribute:: received_error_no_memory
            
            	Error no memory
            	**type**\:   :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoMemory>`
            
            .. attribute:: received_error_queue_full
            
            	Dropped queue full
            	**type**\:   :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorQueueFull>`
            
            .. attribute:: received_error_runt
            
            	RUNT error
            	**type**\:   :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorRunt>`
            
            .. attribute:: received_error_udp_header
            
            	UDP header error
            	**type**\:   :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorUdpHeader>`
            
            .. attribute:: received_good_bfd_reply
            
            	Received Reply with BFD TLV
            	**type**\:   :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdReply>`
            
            .. attribute:: received_good_bfd_request
            
            	Received Reqeust with BFD TLV
            	**type**\:   :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdRequest>`
            
            .. attribute:: received_good_reply
            
            	Received good reply
            	**type**\:   :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodReply>`
            
            .. attribute:: received_good_request
            
            	Received good request
            	**type**\:   :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodRequest>`
            
            .. attribute:: received_unknown
            
            	Received unknown packets
            	**type**\:   :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedUnknown>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.protect_protocol_received_good_reply = MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply()
                self.protect_protocol_received_good_reply.parent = self
                self.protect_protocol_received_good_request = MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest()
                self.protect_protocol_received_good_request.parent = self
                self.received_error_general = MplsOam.Packet.Received.ReceivedErrorGeneral()
                self.received_error_general.parent = self
                self.received_error_ip_header = MplsOam.Packet.Received.ReceivedErrorIpHeader()
                self.received_error_ip_header.parent = self
                self.received_error_no_interface = MplsOam.Packet.Received.ReceivedErrorNoInterface()
                self.received_error_no_interface.parent = self
                self.received_error_no_memory = MplsOam.Packet.Received.ReceivedErrorNoMemory()
                self.received_error_no_memory.parent = self
                self.received_error_queue_full = MplsOam.Packet.Received.ReceivedErrorQueueFull()
                self.received_error_queue_full.parent = self
                self.received_error_runt = MplsOam.Packet.Received.ReceivedErrorRunt()
                self.received_error_runt.parent = self
                self.received_error_udp_header = MplsOam.Packet.Received.ReceivedErrorUdpHeader()
                self.received_error_udp_header.parent = self
                self.received_good_bfd_reply = MplsOam.Packet.Received.ReceivedGoodBfdReply()
                self.received_good_bfd_reply.parent = self
                self.received_good_bfd_request = MplsOam.Packet.Received.ReceivedGoodBfdRequest()
                self.received_good_bfd_request.parent = self
                self.received_good_reply = MplsOam.Packet.Received.ReceivedGoodReply()
                self.received_good_reply.parent = self
                self.received_good_request = MplsOam.Packet.Received.ReceivedGoodRequest()
                self.received_good_request.parent = self
                self.received_unknown = MplsOam.Packet.Received.ReceivedUnknown()
                self.received_unknown.parent = self


            class ReceivedGoodRequest(object):
                """
                Received good request
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-good-request'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodRequest']['meta_info']


            class ReceivedGoodReply(object):
                """
                Received good reply
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-good-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodReply']['meta_info']


            class ReceivedUnknown(object):
                """
                Received unknown packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-unknown'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedUnknown']['meta_info']


            class ReceivedErrorIpHeader(object):
                """
                IP header error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-ip-header'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorIpHeader']['meta_info']


            class ReceivedErrorUdpHeader(object):
                """
                UDP header error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-udp-header'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorUdpHeader']['meta_info']


            class ReceivedErrorRunt(object):
                """
                RUNT error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-runt'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorRunt']['meta_info']


            class ReceivedErrorQueueFull(object):
                """
                Dropped queue full
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-queue-full'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorQueueFull']['meta_info']


            class ReceivedErrorGeneral(object):
                """
                General error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-general'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorGeneral']['meta_info']


            class ReceivedErrorNoInterface(object):
                """
                Error no Interfaces
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-no-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorNoInterface']['meta_info']


            class ReceivedErrorNoMemory(object):
                """
                Error no memory
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-error-no-memory'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorNoMemory']['meta_info']


            class ProtectProtocolReceivedGoodRequest(object):
                """
                Protect Protocol Received good request
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:protect-protocol-received-good-request'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest']['meta_info']


            class ProtectProtocolReceivedGoodReply(object):
                """
                Protect Protocol Received good reply
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:protect-protocol-received-good-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply']['meta_info']


            class ReceivedGoodBfdRequest(object):
                """
                Received Reqeust with BFD TLV
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-good-bfd-request'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodBfdRequest']['meta_info']


            class ReceivedGoodBfdReply(object):
                """
                Received Reply with BFD TLV
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received/Cisco-IOS-XR-mpls-oam-oper:received-good-bfd-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodBfdReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:received'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply._has_data():
                    return True

                if self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request._has_data():
                    return True

                if self.received_error_general is not None and self.received_error_general._has_data():
                    return True

                if self.received_error_ip_header is not None and self.received_error_ip_header._has_data():
                    return True

                if self.received_error_no_interface is not None and self.received_error_no_interface._has_data():
                    return True

                if self.received_error_no_memory is not None and self.received_error_no_memory._has_data():
                    return True

                if self.received_error_queue_full is not None and self.received_error_queue_full._has_data():
                    return True

                if self.received_error_runt is not None and self.received_error_runt._has_data():
                    return True

                if self.received_error_udp_header is not None and self.received_error_udp_header._has_data():
                    return True

                if self.received_good_bfd_reply is not None and self.received_good_bfd_reply._has_data():
                    return True

                if self.received_good_bfd_request is not None and self.received_good_bfd_request._has_data():
                    return True

                if self.received_good_reply is not None and self.received_good_reply._has_data():
                    return True

                if self.received_good_request is not None and self.received_good_request._has_data():
                    return True

                if self.received_unknown is not None and self.received_unknown._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.Received']['meta_info']


        class Sent(object):
            """
            Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bfd_no_reply = MplsOam.Packet.Sent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self.transmit_bfd_good = MplsOam.Packet.Sent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self.transmit_drop = MplsOam.Packet.Sent.TransmitDrop()
                self.transmit_drop.parent = self
                self.transmit_good = MplsOam.Packet.Sent.TransmitGood()
                self.transmit_good.parent = self


            class TransmitGood(object):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:sent/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitGood']['meta_info']


            class TransmitDrop(object):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:sent/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitDrop']['meta_info']


            class TransmitBfdGood(object):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:sent/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitBfdGood']['meta_info']


            class BfdNoReply(object):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:sent/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.BfdNoReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:sent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                    return True

                if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                    return True

                if self.transmit_drop is not None and self.transmit_drop._has_data():
                    return True

                if self.transmit_good is not None and self.transmit_good._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.Sent']['meta_info']


        class WorkingReqSent(object):
            """
            Working Request Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bfd_no_reply = MplsOam.Packet.WorkingReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self.transmit_bfd_good = MplsOam.Packet.WorkingReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self.transmit_drop = MplsOam.Packet.WorkingReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self.transmit_good = MplsOam.Packet.WorkingReqSent.TransmitGood()
                self.transmit_good.parent = self


            class TransmitGood(object):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitGood']['meta_info']


            class TransmitDrop(object):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(object):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(object):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-req-sent/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.BfdNoReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-req-sent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                    return True

                if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                    return True

                if self.transmit_drop is not None and self.transmit_drop._has_data():
                    return True

                if self.transmit_good is not None and self.transmit_good._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']


        class WorkingRepSent(object):
            """
            Working Reply Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bfd_no_reply = MplsOam.Packet.WorkingRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self.transmit_bfd_good = MplsOam.Packet.WorkingRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self.transmit_drop = MplsOam.Packet.WorkingRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self.transmit_good = MplsOam.Packet.WorkingRepSent.TransmitGood()
                self.transmit_good.parent = self


            class TransmitGood(object):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitGood']['meta_info']


            class TransmitDrop(object):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(object):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(object):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.BfdNoReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:working-rep-sent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                    return True

                if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                    return True

                if self.transmit_drop is not None and self.transmit_drop._has_data():
                    return True

                if self.transmit_good is not None and self.transmit_good._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']


        class ProtectReqSent(object):
            """
            Protect Request Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bfd_no_reply = MplsOam.Packet.ProtectReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self.transmit_bfd_good = MplsOam.Packet.ProtectReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self.transmit_drop = MplsOam.Packet.ProtectReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self.transmit_good = MplsOam.Packet.ProtectReqSent.TransmitGood()
                self.transmit_good.parent = self


            class TransmitGood(object):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitGood']['meta_info']


            class TransmitDrop(object):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(object):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(object):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.BfdNoReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-req-sent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                    return True

                if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                    return True

                if self.transmit_drop is not None and self.transmit_drop._has_data():
                    return True

                if self.transmit_good is not None and self.transmit_good._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']


        class ProtectRepSent(object):
            """
            Protect Reply Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bfd_no_reply = MplsOam.Packet.ProtectRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self.transmit_bfd_good = MplsOam.Packet.ProtectRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self.transmit_drop = MplsOam.Packet.ProtectRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self.transmit_good = MplsOam.Packet.ProtectRepSent.TransmitGood()
                self.transmit_good.parent = self


            class TransmitGood(object):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitGood']['meta_info']


            class TransmitDrop(object):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-drop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(object):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent/Cisco-IOS-XR-mpls-oam-oper:transmit-bfd-good'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(object):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.packets = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent/Cisco-IOS-XR-mpls-oam-oper:bfd-no-reply'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.BfdNoReply']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet/Cisco-IOS-XR-mpls-oam-oper:protect-rep-sent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bfd_no_reply is not None and self.bfd_no_reply._has_data():
                    return True

                if self.transmit_bfd_good is not None and self.transmit_bfd_good._has_data():
                    return True

                if self.transmit_drop is not None and self.transmit_drop._has_data():
                    return True

                if self.transmit_good is not None and self.transmit_good._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:packet'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.protect_rep_sent is not None and self.protect_rep_sent._has_data():
                return True

            if self.protect_req_sent is not None and self.protect_req_sent._has_data():
                return True

            if self.received is not None and self.received._has_data():
                return True

            if self.sent is not None and self.sent._has_data():
                return True

            if self.working_rep_sent is not None and self.working_rep_sent._has_data():
                return True

            if self.working_req_sent is not None and self.working_req_sent._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Packet']['meta_info']


    class Global_(object):
        """
        LSPV global counters operational data
        
        .. attribute:: collaborator_statistics
        
        	Collaborator statistics
        	**type**\:   :py:class:`CollaboratorStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics>`
        
        .. attribute:: message_statistics
        
        	Message statistics
        	**type**\:   :py:class:`MessageStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.MessageStatistics>`
        
        .. attribute:: total_clients
        
        	Number of clients
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.collaborator_statistics = MplsOam.Global_.CollaboratorStatistics()
            self.collaborator_statistics.parent = self
            self.message_statistics = MplsOam.Global_.MessageStatistics()
            self.message_statistics.parent = self
            self.total_clients = None


        class MessageStatistics(object):
            """
            Message statistics
            
            .. attribute:: echo_cancel_messages
            
            	Message echo cancel count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: echo_submit_messages
            
            	Message echo submit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_config_messages
            
            	Message get configiuration count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_response_messages
            
            	Message get response count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_result_messages
            
            	Message get results count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_block_messages
            
            	Message property block count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_request_messages
            
            	Message property request count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_response_messages
            
            	Message property response count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: register_messages
            
            	Message register count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: thread_request_messages
            
            	Message thread request count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unregister_messages
            
            	Message unregister count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.echo_cancel_messages = None
                self.echo_submit_messages = None
                self.get_config_messages = None
                self.get_response_messages = None
                self.get_result_messages = None
                self.property_block_messages = None
                self.property_request_messages = None
                self.property_response_messages = None
                self.register_messages = None
                self.thread_request_messages = None
                self.unregister_messages = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:message-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.echo_cancel_messages is not None:
                    return True

                if self.echo_submit_messages is not None:
                    return True

                if self.get_config_messages is not None:
                    return True

                if self.get_response_messages is not None:
                    return True

                if self.get_result_messages is not None:
                    return True

                if self.property_block_messages is not None:
                    return True

                if self.property_request_messages is not None:
                    return True

                if self.property_response_messages is not None:
                    return True

                if self.register_messages is not None:
                    return True

                if self.thread_request_messages is not None:
                    return True

                if self.unregister_messages is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Global_.MessageStatistics']['meta_info']


        class CollaboratorStatistics(object):
            """
            Collaborator statistics
            
            .. attribute:: collaborator_i_parm
            
            	Collaborator IPARM counts
            	**type**\:   :py:class:`CollaboratorIParm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm>`
            
            .. attribute:: collaborator_im
            
            	Collaborator IM counts
            	**type**\:   :py:class:`CollaboratorIm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorIm>`
            
            .. attribute:: collaborator_net_io
            
            	Collaborator NetIO counts
            	**type**\:   :py:class:`CollaboratorNetIo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo>`
            
            .. attribute:: collaborator_rib
            
            	Collaborator RIB counts
            	**type**\:   :py:class:`CollaboratorRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorRib>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.collaborator_i_parm = MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm()
                self.collaborator_i_parm.parent = self
                self.collaborator_im = MplsOam.Global_.CollaboratorStatistics.CollaboratorIm()
                self.collaborator_im.parent = self
                self.collaborator_net_io = MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo()
                self.collaborator_net_io.parent = self
                self.collaborator_rib = MplsOam.Global_.CollaboratorStatistics.CollaboratorRib()
                self.collaborator_rib.parent = self


            class CollaboratorIParm(object):
                """
                Collaborator IPARM counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.downs = None
                    self.ups = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:collaborator-statistics/Cisco-IOS-XR-mpls-oam-oper:collaborator-i-parm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.downs is not None:
                        return True

                    if self.ups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm']['meta_info']


            class CollaboratorIm(object):
                """
                Collaborator IM counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.downs = None
                    self.ups = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:collaborator-statistics/Cisco-IOS-XR-mpls-oam-oper:collaborator-im'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.downs is not None:
                        return True

                    if self.ups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorIm']['meta_info']


            class CollaboratorNetIo(object):
                """
                Collaborator NetIO counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.downs = None
                    self.ups = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:collaborator-statistics/Cisco-IOS-XR-mpls-oam-oper:collaborator-net-io'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.downs is not None:
                        return True

                    if self.ups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo']['meta_info']


            class CollaboratorRib(object):
                """
                Collaborator RIB counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.downs = None
                    self.ups = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:collaborator-statistics/Cisco-IOS-XR-mpls-oam-oper:collaborator-rib'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.downs is not None:
                        return True

                    if self.ups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorRib']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global/Cisco-IOS-XR-mpls-oam-oper:collaborator-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.collaborator_i_parm is not None and self.collaborator_i_parm._has_data():
                    return True

                if self.collaborator_im is not None and self.collaborator_im._has_data():
                    return True

                if self.collaborator_net_io is not None and self.collaborator_net_io._has_data():
                    return True

                if self.collaborator_rib is not None and self.collaborator_rib._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam/Cisco-IOS-XR-mpls-oam-oper:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.collaborator_statistics is not None and self.collaborator_statistics._has_data():
                return True

            if self.message_statistics is not None and self.message_statistics._has_data():
                return True

            if self.total_clients is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Global_']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-oam-oper:mpls-oam'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.interface is not None and self.interface._has_data():
            return True

        if self.packet is not None and self.packet._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
        return meta._meta_table['MplsOam']['meta_info']


