""" Cisco_IOS_XR_mpls_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package operational data.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS OAM operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LspvBagInterfaceState(Enum):
    """
    LspvBagInterfaceState (Enum Class)

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

    not_ready = Enum.YLeaf(0, "not-ready")

    admin_down = Enum.YLeaf(1, "admin-down")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    shutdown = Enum.YLeaf(4, "shutdown")

    error_disable = Enum.YLeaf(5, "error-disable")

    down_immediate = Enum.YLeaf(6, "down-immediate")

    admin_immediate = Enum.YLeaf(7, "admin-immediate")

    graceful_down = Enum.YLeaf(8, "graceful-down")

    begin_shutdown = Enum.YLeaf(9, "begin-shutdown")

    end_shutdown = Enum.YLeaf(10, "end-shutdown")

    begin_error_disable = Enum.YLeaf(11, "begin-error-disable")

    end_error_disable = Enum.YLeaf(12, "end-error-disable")

    begin_graceful_down = Enum.YLeaf(13, "begin-graceful-down")

    reset = Enum.YLeaf(14, "reset")

    operational = Enum.YLeaf(15, "operational")

    not_operational = Enum.YLeaf(16, "not-operational")

    not_known = Enum.YLeaf(17, "not-known")



class MplsOam(Entity):
    """
    MPLS OAM operational data
    
    .. attribute:: interface
    
    	MPLS OAM interface operational data
    	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface>`
    
    .. attribute:: packet
    
    	LSPV packet counters operational data
    	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet>`
    
    .. attribute:: global_
    
    	LSPV global counters operational data
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global>`
    
    

    """

    _prefix = 'mpls-oam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsOam, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-oam"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-oam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interface", ("interface", MplsOam.Interface)), ("packet", ("packet", MplsOam.Packet)), ("global", ("global_", MplsOam.Global))])
        self._leafs = OrderedDict()

        self.interface = MplsOam.Interface()
        self.interface.parent = self
        self._children_name_map["interface"] = "interface"

        self.packet = MplsOam.Packet()
        self.packet.parent = self
        self._children_name_map["packet"] = "packet"

        self.global_ = MplsOam.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsOam, [], name, value)


    class Interface(Entity):
        """
        MPLS OAM interface operational data
        
        .. attribute:: briefs
        
        	MPLS OAM interface detail data
        	**type**\:  :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs>`
        
        .. attribute:: details
        
        	MPLS OAM interface detail data
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("briefs", ("briefs", MplsOam.Interface.Briefs)), ("details", ("details", MplsOam.Interface.Details))])
            self._leafs = OrderedDict()

            self.briefs = MplsOam.Interface.Briefs()
            self.briefs.parent = self
            self._children_name_map["briefs"] = "briefs"

            self.details = MplsOam.Interface.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._segment_path = lambda: "interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsOam.Interface, [], name, value)


        class Briefs(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: brief
            
            	MPLS OAM interface operational data
            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs.Brief>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Briefs, self).__init__()

                self.yang_name = "briefs"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("brief", ("brief", MplsOam.Interface.Briefs.Brief))])
                self._leafs = OrderedDict()

                self.brief = YList(self)
                self._segment_path = lambda: "briefs"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Interface.Briefs, [], name, value)


            class Brief(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_name_xr
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: state
                
                	Interface state
                	**type**\:  :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                
                .. attribute:: mtu
                
                	Interface MTU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length (IPv4)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length_v6
                
                	Prefix length (IPv6)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: primary_address
                
                	Primary interface address (IPv4)
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: primary_address_v6
                
                	Primary interface address (IPv6)
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Interface.Briefs.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "briefs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'LspvBagInterfaceState', '')])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                        ('prefix_length_v6', (YLeaf(YType.uint32, 'prefix-length-v6'), ['int'])),
                        ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                        ('primary_address_v6', (YLeaf(YType.str, 'primary-address-v6'), ['str'])),
                    ])
                    self.interface_name = None
                    self.interface_name_xr = None
                    self.state = None
                    self.mtu = None
                    self.prefix_length = None
                    self.prefix_length_v6 = None
                    self.primary_address = None
                    self.primary_address_v6 = None
                    self._segment_path = lambda: "brief" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/briefs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Interface.Briefs.Brief, ['interface_name', u'interface_name_xr', u'state', u'mtu', u'prefix_length', u'prefix_length_v6', u'primary_address', u'primary_address_v6'], name, value)


        class Details(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: detail
            
            	MPLS OAM interface operational data
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail", ("detail", MplsOam.Interface.Details.Detail))])
                self._leafs = OrderedDict()

                self.detail = YList(self)
                self._segment_path = lambda: "details"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Interface.Details, [], name, value)


            class Detail(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_brief
                
                	Interface brief
                	**type**\:  :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.InterfaceBrief>`
                
                .. attribute:: packet_statistics
                
                	Packet statistics
                	**type**\:  :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Interface.Details.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("interface-brief", ("interface_brief", MplsOam.Interface.Details.Detail.InterfaceBrief)), ("packet-statistics", ("packet_statistics", MplsOam.Interface.Details.Detail.PacketStatistics))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ])
                    self.interface_name = None

                    self.interface_brief = MplsOam.Interface.Details.Detail.InterfaceBrief()
                    self.interface_brief.parent = self
                    self._children_name_map["interface_brief"] = "interface-brief"

                    self.packet_statistics = MplsOam.Interface.Details.Detail.PacketStatistics()
                    self.packet_statistics.parent = self
                    self._children_name_map["packet_statistics"] = "packet-statistics"
                    self._segment_path = lambda: "detail" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Interface.Details.Detail, ['interface_name'], name, value)


                class InterfaceBrief(Entity):
                    """
                    Interface brief
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                    
                    .. attribute:: mtu
                    
                    	Interface MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length (IPv4)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length_v6
                    
                    	Prefix length (IPv6)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: primary_address
                    
                    	Primary interface address (IPv4)
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: primary_address_v6
                    
                    	Primary interface address (IPv6)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsOam.Interface.Details.Detail.InterfaceBrief, self).__init__()

                        self.yang_name = "interface-brief"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'LspvBagInterfaceState', '')])),
                            ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('prefix_length_v6', (YLeaf(YType.uint32, 'prefix-length-v6'), ['int'])),
                            ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                            ('primary_address_v6', (YLeaf(YType.str, 'primary-address-v6'), ['str'])),
                        ])
                        self.interface_name_xr = None
                        self.state = None
                        self.mtu = None
                        self.prefix_length = None
                        self.prefix_length_v6 = None
                        self.primary_address = None
                        self.primary_address_v6 = None
                        self._segment_path = lambda: "interface-brief"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsOam.Interface.Details.Detail.InterfaceBrief, [u'interface_name_xr', u'state', u'mtu', u'prefix_length', u'prefix_length_v6', u'primary_address', u'primary_address_v6'], name, value)


                class PacketStatistics(Entity):
                    """
                    Packet statistics
                    
                    .. attribute:: received
                    
                    	Packet reception counts
                    	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received>`
                    
                    .. attribute:: sent
                    
                    	Packet transmit counts
                    	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent>`
                    
                    .. attribute:: working_req_sent
                    
                    	Working Request Packet transmit counts
                    	**type**\:  :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent>`
                    
                    .. attribute:: working_rep_sent
                    
                    	Working Reply Packet transmit counts
                    	**type**\:  :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent>`
                    
                    .. attribute:: protect_req_sent
                    
                    	Protect Request Packet transmit counts
                    	**type**\:  :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent>`
                    
                    .. attribute:: protect_rep_sent
                    
                    	Protect Reply Packet transmit counts
                    	**type**\:  :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsOam.Interface.Details.Detail.PacketStatistics, self).__init__()

                        self.yang_name = "packet-statistics"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("received", ("received", MplsOam.Interface.Details.Detail.PacketStatistics.Received)), ("sent", ("sent", MplsOam.Interface.Details.Detail.PacketStatistics.Sent)), ("working-req-sent", ("working_req_sent", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent)), ("working-rep-sent", ("working_rep_sent", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent)), ("protect-req-sent", ("protect_req_sent", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent)), ("protect-rep-sent", ("protect_rep_sent", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent))])
                        self._leafs = OrderedDict()

                        self.received = MplsOam.Interface.Details.Detail.PacketStatistics.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"

                        self.sent = MplsOam.Interface.Details.Detail.PacketStatistics.Sent()
                        self.sent.parent = self
                        self._children_name_map["sent"] = "sent"

                        self.working_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent()
                        self.working_req_sent.parent = self
                        self._children_name_map["working_req_sent"] = "working-req-sent"

                        self.working_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent()
                        self.working_rep_sent.parent = self
                        self._children_name_map["working_rep_sent"] = "working-rep-sent"

                        self.protect_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent()
                        self.protect_req_sent.parent = self
                        self._children_name_map["protect_req_sent"] = "protect-req-sent"

                        self.protect_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent()
                        self.protect_rep_sent.parent = self
                        self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
                        self._segment_path = lambda: "packet-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics, [], name, value)


                    class Received(Entity):
                        """
                        Packet reception counts
                        
                        .. attribute:: received_good_request
                        
                        	Received good request
                        	**type**\:  :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest>`
                        
                        .. attribute:: received_good_reply
                        
                        	Received good reply
                        	**type**\:  :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply>`
                        
                        .. attribute:: received_unknown
                        
                        	Received unknown packets
                        	**type**\:  :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown>`
                        
                        .. attribute:: received_error_ip_header
                        
                        	IP header error
                        	**type**\:  :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader>`
                        
                        .. attribute:: received_error_udp_header
                        
                        	UDP header error
                        	**type**\:  :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader>`
                        
                        .. attribute:: received_error_runt
                        
                        	RUNT error
                        	**type**\:  :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt>`
                        
                        .. attribute:: received_error_queue_full
                        
                        	Dropped queue full
                        	**type**\:  :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull>`
                        
                        .. attribute:: received_error_general
                        
                        	General error
                        	**type**\:  :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral>`
                        
                        .. attribute:: received_error_no_interface
                        
                        	Error no Interfaces
                        	**type**\:  :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface>`
                        
                        .. attribute:: received_error_no_memory
                        
                        	Error no memory
                        	**type**\:  :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory>`
                        
                        .. attribute:: protect_protocol_received_good_request
                        
                        	Protect Protocol Received good request
                        	**type**\:  :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest>`
                        
                        .. attribute:: protect_protocol_received_good_reply
                        
                        	Protect Protocol Received good reply
                        	**type**\:  :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply>`
                        
                        .. attribute:: received_good_bfd_request
                        
                        	Received Reqeust with BFD TLV
                        	**type**\:  :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest>`
                        
                        .. attribute:: received_good_bfd_reply
                        
                        	Received Reply with BFD TLV
                        	**type**\:  :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("received-good-request", ("received_good_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest)), ("received-good-reply", ("received_good_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply)), ("received-unknown", ("received_unknown", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown)), ("received-error-ip-header", ("received_error_ip_header", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader)), ("received-error-udp-header", ("received_error_udp_header", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader)), ("received-error-runt", ("received_error_runt", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt)), ("received-error-queue-full", ("received_error_queue_full", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull)), ("received-error-general", ("received_error_general", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral)), ("received-error-no-interface", ("received_error_no_interface", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface)), ("received-error-no-memory", ("received_error_no_memory", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory)), ("protect-protocol-received-good-request", ("protect_protocol_received_good_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest)), ("protect-protocol-received-good-reply", ("protect_protocol_received_good_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply)), ("received-good-bfd-request", ("received_good_bfd_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest)), ("received-good-bfd-reply", ("received_good_bfd_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply))])
                            self._leafs = OrderedDict()

                            self.received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest()
                            self.received_good_request.parent = self
                            self._children_name_map["received_good_request"] = "received-good-request"

                            self.received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply()
                            self.received_good_reply.parent = self
                            self._children_name_map["received_good_reply"] = "received-good-reply"

                            self.received_unknown = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown()
                            self.received_unknown.parent = self
                            self._children_name_map["received_unknown"] = "received-unknown"

                            self.received_error_ip_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader()
                            self.received_error_ip_header.parent = self
                            self._children_name_map["received_error_ip_header"] = "received-error-ip-header"

                            self.received_error_udp_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader()
                            self.received_error_udp_header.parent = self
                            self._children_name_map["received_error_udp_header"] = "received-error-udp-header"

                            self.received_error_runt = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt()
                            self.received_error_runt.parent = self
                            self._children_name_map["received_error_runt"] = "received-error-runt"

                            self.received_error_queue_full = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull()
                            self.received_error_queue_full.parent = self
                            self._children_name_map["received_error_queue_full"] = "received-error-queue-full"

                            self.received_error_general = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral()
                            self.received_error_general.parent = self
                            self._children_name_map["received_error_general"] = "received-error-general"

                            self.received_error_no_interface = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface()
                            self.received_error_no_interface.parent = self
                            self._children_name_map["received_error_no_interface"] = "received-error-no-interface"

                            self.received_error_no_memory = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory()
                            self.received_error_no_memory.parent = self
                            self._children_name_map["received_error_no_memory"] = "received-error-no-memory"

                            self.protect_protocol_received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest()
                            self.protect_protocol_received_good_request.parent = self
                            self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"

                            self.protect_protocol_received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply()
                            self.protect_protocol_received_good_reply.parent = self
                            self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"

                            self.received_good_bfd_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest()
                            self.received_good_bfd_request.parent = self
                            self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"

                            self.received_good_bfd_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply()
                            self.received_good_bfd_reply.parent = self
                            self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                            self._segment_path = lambda: "received"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received, [], name, value)


                        class ReceivedGoodRequest(Entity):
                            """
                            Received good request
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, self).__init__()

                                self.yang_name = "received-good-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-good-request"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, [u'packets', u'bytes'], name, value)


                        class ReceivedGoodReply(Entity):
                            """
                            Received good reply
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, self).__init__()

                                self.yang_name = "received-good-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-good-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, [u'packets', u'bytes'], name, value)


                        class ReceivedUnknown(Entity):
                            """
                            Received unknown packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, self).__init__()

                                self.yang_name = "received-unknown"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-unknown"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorIpHeader(Entity):
                            """
                            IP header error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, self).__init__()

                                self.yang_name = "received-error-ip-header"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-ip-header"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorUdpHeader(Entity):
                            """
                            UDP header error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, self).__init__()

                                self.yang_name = "received-error-udp-header"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-udp-header"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorRunt(Entity):
                            """
                            RUNT error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, self).__init__()

                                self.yang_name = "received-error-runt"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-runt"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorQueueFull(Entity):
                            """
                            Dropped queue full
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, self).__init__()

                                self.yang_name = "received-error-queue-full"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-queue-full"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorGeneral(Entity):
                            """
                            General error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, self).__init__()

                                self.yang_name = "received-error-general"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-general"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorNoInterface(Entity):
                            """
                            Error no Interfaces
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, self).__init__()

                                self.yang_name = "received-error-no-interface"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-no-interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, [u'packets', u'bytes'], name, value)


                        class ReceivedErrorNoMemory(Entity):
                            """
                            Error no memory
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, self).__init__()

                                self.yang_name = "received-error-no-memory"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-error-no-memory"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, [u'packets', u'bytes'], name, value)


                        class ProtectProtocolReceivedGoodRequest(Entity):
                            """
                            Protect Protocol Received good request
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                                self.yang_name = "protect-protocol-received-good-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "protect-protocol-received-good-request"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, [u'packets', u'bytes'], name, value)


                        class ProtectProtocolReceivedGoodReply(Entity):
                            """
                            Protect Protocol Received good reply
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                                self.yang_name = "protect-protocol-received-good-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "protect-protocol-received-good-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, [u'packets', u'bytes'], name, value)


                        class ReceivedGoodBfdRequest(Entity):
                            """
                            Received Reqeust with BFD TLV
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, self).__init__()

                                self.yang_name = "received-good-bfd-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-good-bfd-request"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, [u'packets', u'bytes'], name, value)


                        class ReceivedGoodBfdReply(Entity):
                            """
                            Received Reply with BFD TLV
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, self).__init__()

                                self.yang_name = "received-good-bfd-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "received-good-bfd-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, [u'packets', u'bytes'], name, value)


                    class Sent(Entity):
                        """
                        Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood>`
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent, self).__init__()

                            self.yang_name = "sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply))])
                            self._leafs = OrderedDict()

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._segment_path = lambda: "sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent, [], name, value)


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, [u'packets', u'bytes'], name, value)


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, [u'packets', u'bytes'], name, value)


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-bfd-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "bfd-no-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, [u'packets', u'bytes'], name, value)


                    class WorkingReqSent(Entity):
                        """
                        Working Request Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood>`
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent, self).__init__()

                            self.yang_name = "working-req-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply))])
                            self._leafs = OrderedDict()

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._segment_path = lambda: "working-req-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent, [], name, value)


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, [u'packets', u'bytes'], name, value)


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, [u'packets', u'bytes'], name, value)


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-bfd-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "bfd-no-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, [u'packets', u'bytes'], name, value)


                    class WorkingRepSent(Entity):
                        """
                        Working Reply Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood>`
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent, self).__init__()

                            self.yang_name = "working-rep-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply))])
                            self._leafs = OrderedDict()

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._segment_path = lambda: "working-rep-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent, [], name, value)


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, [u'packets', u'bytes'], name, value)


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, [u'packets', u'bytes'], name, value)


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-bfd-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "bfd-no-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, [u'packets', u'bytes'], name, value)


                    class ProtectReqSent(Entity):
                        """
                        Protect Request Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood>`
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent, self).__init__()

                            self.yang_name = "protect-req-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply))])
                            self._leafs = OrderedDict()

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._segment_path = lambda: "protect-req-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent, [], name, value)


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, [u'packets', u'bytes'], name, value)


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, [u'packets', u'bytes'], name, value)


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-bfd-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "bfd-no-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, [u'packets', u'bytes'], name, value)


                    class ProtectRepSent(Entity):
                        """
                        Protect Reply Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood>`
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent, self).__init__()

                            self.yang_name = "protect-rep-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply))])
                            self._leafs = OrderedDict()

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._segment_path = lambda: "protect-rep-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent, [], name, value)


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, [u'packets', u'bytes'], name, value)


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, [u'packets', u'bytes'], name, value)


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "transmit-bfd-good"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "bfd-no-reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, [u'packets', u'bytes'], name, value)


    class Packet(Entity):
        """
        LSPV packet counters operational data
        
        .. attribute:: received
        
        	Packet reception counts
        	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received>`
        
        .. attribute:: sent
        
        	Packet transmit counts
        	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent>`
        
        .. attribute:: working_req_sent
        
        	Working Request Packet transmit counts
        	**type**\:  :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent>`
        
        .. attribute:: working_rep_sent
        
        	Working Reply Packet transmit counts
        	**type**\:  :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent>`
        
        .. attribute:: protect_req_sent
        
        	Protect Request Packet transmit counts
        	**type**\:  :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent>`
        
        .. attribute:: protect_rep_sent
        
        	Protect Reply Packet transmit counts
        	**type**\:  :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Packet, self).__init__()

            self.yang_name = "packet"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("received", ("received", MplsOam.Packet.Received)), ("sent", ("sent", MplsOam.Packet.Sent)), ("working-req-sent", ("working_req_sent", MplsOam.Packet.WorkingReqSent)), ("working-rep-sent", ("working_rep_sent", MplsOam.Packet.WorkingRepSent)), ("protect-req-sent", ("protect_req_sent", MplsOam.Packet.ProtectReqSent)), ("protect-rep-sent", ("protect_rep_sent", MplsOam.Packet.ProtectRepSent))])
            self._leafs = OrderedDict()

            self.received = MplsOam.Packet.Received()
            self.received.parent = self
            self._children_name_map["received"] = "received"

            self.sent = MplsOam.Packet.Sent()
            self.sent.parent = self
            self._children_name_map["sent"] = "sent"

            self.working_req_sent = MplsOam.Packet.WorkingReqSent()
            self.working_req_sent.parent = self
            self._children_name_map["working_req_sent"] = "working-req-sent"

            self.working_rep_sent = MplsOam.Packet.WorkingRepSent()
            self.working_rep_sent.parent = self
            self._children_name_map["working_rep_sent"] = "working-rep-sent"

            self.protect_req_sent = MplsOam.Packet.ProtectReqSent()
            self.protect_req_sent.parent = self
            self._children_name_map["protect_req_sent"] = "protect-req-sent"

            self.protect_rep_sent = MplsOam.Packet.ProtectRepSent()
            self.protect_rep_sent.parent = self
            self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
            self._segment_path = lambda: "packet"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsOam.Packet, [], name, value)


        class Received(Entity):
            """
            Packet reception counts
            
            .. attribute:: received_good_request
            
            	Received good request
            	**type**\:  :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodRequest>`
            
            .. attribute:: received_good_reply
            
            	Received good reply
            	**type**\:  :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodReply>`
            
            .. attribute:: received_unknown
            
            	Received unknown packets
            	**type**\:  :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedUnknown>`
            
            .. attribute:: received_error_ip_header
            
            	IP header error
            	**type**\:  :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorIpHeader>`
            
            .. attribute:: received_error_udp_header
            
            	UDP header error
            	**type**\:  :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorUdpHeader>`
            
            .. attribute:: received_error_runt
            
            	RUNT error
            	**type**\:  :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorRunt>`
            
            .. attribute:: received_error_queue_full
            
            	Dropped queue full
            	**type**\:  :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorQueueFull>`
            
            .. attribute:: received_error_general
            
            	General error
            	**type**\:  :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorGeneral>`
            
            .. attribute:: received_error_no_interface
            
            	Error no Interfaces
            	**type**\:  :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoInterface>`
            
            .. attribute:: received_error_no_memory
            
            	Error no memory
            	**type**\:  :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoMemory>`
            
            .. attribute:: protect_protocol_received_good_request
            
            	Protect Protocol Received good request
            	**type**\:  :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest>`
            
            .. attribute:: protect_protocol_received_good_reply
            
            	Protect Protocol Received good reply
            	**type**\:  :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply>`
            
            .. attribute:: received_good_bfd_request
            
            	Received Reqeust with BFD TLV
            	**type**\:  :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdRequest>`
            
            .. attribute:: received_good_bfd_reply
            
            	Received Reply with BFD TLV
            	**type**\:  :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.Received, self).__init__()

                self.yang_name = "received"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("received-good-request", ("received_good_request", MplsOam.Packet.Received.ReceivedGoodRequest)), ("received-good-reply", ("received_good_reply", MplsOam.Packet.Received.ReceivedGoodReply)), ("received-unknown", ("received_unknown", MplsOam.Packet.Received.ReceivedUnknown)), ("received-error-ip-header", ("received_error_ip_header", MplsOam.Packet.Received.ReceivedErrorIpHeader)), ("received-error-udp-header", ("received_error_udp_header", MplsOam.Packet.Received.ReceivedErrorUdpHeader)), ("received-error-runt", ("received_error_runt", MplsOam.Packet.Received.ReceivedErrorRunt)), ("received-error-queue-full", ("received_error_queue_full", MplsOam.Packet.Received.ReceivedErrorQueueFull)), ("received-error-general", ("received_error_general", MplsOam.Packet.Received.ReceivedErrorGeneral)), ("received-error-no-interface", ("received_error_no_interface", MplsOam.Packet.Received.ReceivedErrorNoInterface)), ("received-error-no-memory", ("received_error_no_memory", MplsOam.Packet.Received.ReceivedErrorNoMemory)), ("protect-protocol-received-good-request", ("protect_protocol_received_good_request", MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest)), ("protect-protocol-received-good-reply", ("protect_protocol_received_good_reply", MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply)), ("received-good-bfd-request", ("received_good_bfd_request", MplsOam.Packet.Received.ReceivedGoodBfdRequest)), ("received-good-bfd-reply", ("received_good_bfd_reply", MplsOam.Packet.Received.ReceivedGoodBfdReply))])
                self._leafs = OrderedDict()

                self.received_good_request = MplsOam.Packet.Received.ReceivedGoodRequest()
                self.received_good_request.parent = self
                self._children_name_map["received_good_request"] = "received-good-request"

                self.received_good_reply = MplsOam.Packet.Received.ReceivedGoodReply()
                self.received_good_reply.parent = self
                self._children_name_map["received_good_reply"] = "received-good-reply"

                self.received_unknown = MplsOam.Packet.Received.ReceivedUnknown()
                self.received_unknown.parent = self
                self._children_name_map["received_unknown"] = "received-unknown"

                self.received_error_ip_header = MplsOam.Packet.Received.ReceivedErrorIpHeader()
                self.received_error_ip_header.parent = self
                self._children_name_map["received_error_ip_header"] = "received-error-ip-header"

                self.received_error_udp_header = MplsOam.Packet.Received.ReceivedErrorUdpHeader()
                self.received_error_udp_header.parent = self
                self._children_name_map["received_error_udp_header"] = "received-error-udp-header"

                self.received_error_runt = MplsOam.Packet.Received.ReceivedErrorRunt()
                self.received_error_runt.parent = self
                self._children_name_map["received_error_runt"] = "received-error-runt"

                self.received_error_queue_full = MplsOam.Packet.Received.ReceivedErrorQueueFull()
                self.received_error_queue_full.parent = self
                self._children_name_map["received_error_queue_full"] = "received-error-queue-full"

                self.received_error_general = MplsOam.Packet.Received.ReceivedErrorGeneral()
                self.received_error_general.parent = self
                self._children_name_map["received_error_general"] = "received-error-general"

                self.received_error_no_interface = MplsOam.Packet.Received.ReceivedErrorNoInterface()
                self.received_error_no_interface.parent = self
                self._children_name_map["received_error_no_interface"] = "received-error-no-interface"

                self.received_error_no_memory = MplsOam.Packet.Received.ReceivedErrorNoMemory()
                self.received_error_no_memory.parent = self
                self._children_name_map["received_error_no_memory"] = "received-error-no-memory"

                self.protect_protocol_received_good_request = MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest()
                self.protect_protocol_received_good_request.parent = self
                self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"

                self.protect_protocol_received_good_reply = MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply()
                self.protect_protocol_received_good_reply.parent = self
                self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"

                self.received_good_bfd_request = MplsOam.Packet.Received.ReceivedGoodBfdRequest()
                self.received_good_bfd_request.parent = self
                self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"

                self.received_good_bfd_reply = MplsOam.Packet.Received.ReceivedGoodBfdReply()
                self.received_good_bfd_reply.parent = self
                self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                self._segment_path = lambda: "received"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.Received, [], name, value)


            class ReceivedGoodRequest(Entity):
                """
                Received good request
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodRequest, self).__init__()

                    self.yang_name = "received-good-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-good-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodRequest, [u'packets', u'bytes'], name, value)


            class ReceivedGoodReply(Entity):
                """
                Received good reply
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodReply, self).__init__()

                    self.yang_name = "received-good-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-good-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodReply, [u'packets', u'bytes'], name, value)


            class ReceivedUnknown(Entity):
                """
                Received unknown packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedUnknown, self).__init__()

                    self.yang_name = "received-unknown"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-unknown"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedUnknown, [u'packets', u'bytes'], name, value)


            class ReceivedErrorIpHeader(Entity):
                """
                IP header error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorIpHeader, self).__init__()

                    self.yang_name = "received-error-ip-header"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-ip-header"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorIpHeader, [u'packets', u'bytes'], name, value)


            class ReceivedErrorUdpHeader(Entity):
                """
                UDP header error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorUdpHeader, self).__init__()

                    self.yang_name = "received-error-udp-header"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-udp-header"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorUdpHeader, [u'packets', u'bytes'], name, value)


            class ReceivedErrorRunt(Entity):
                """
                RUNT error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorRunt, self).__init__()

                    self.yang_name = "received-error-runt"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-runt"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorRunt, [u'packets', u'bytes'], name, value)


            class ReceivedErrorQueueFull(Entity):
                """
                Dropped queue full
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorQueueFull, self).__init__()

                    self.yang_name = "received-error-queue-full"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-queue-full"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorQueueFull, [u'packets', u'bytes'], name, value)


            class ReceivedErrorGeneral(Entity):
                """
                General error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorGeneral, self).__init__()

                    self.yang_name = "received-error-general"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-general"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorGeneral, [u'packets', u'bytes'], name, value)


            class ReceivedErrorNoInterface(Entity):
                """
                Error no Interfaces
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorNoInterface, self).__init__()

                    self.yang_name = "received-error-no-interface"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-no-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoInterface, [u'packets', u'bytes'], name, value)


            class ReceivedErrorNoMemory(Entity):
                """
                Error no memory
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorNoMemory, self).__init__()

                    self.yang_name = "received-error-no-memory"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-error-no-memory"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoMemory, [u'packets', u'bytes'], name, value)


            class ProtectProtocolReceivedGoodRequest(Entity):
                """
                Protect Protocol Received good request
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                    self.yang_name = "protect-protocol-received-good-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "protect-protocol-received-good-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, [u'packets', u'bytes'], name, value)


            class ProtectProtocolReceivedGoodReply(Entity):
                """
                Protect Protocol Received good reply
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                    self.yang_name = "protect-protocol-received-good-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "protect-protocol-received-good-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, [u'packets', u'bytes'], name, value)


            class ReceivedGoodBfdRequest(Entity):
                """
                Received Reqeust with BFD TLV
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodBfdRequest, self).__init__()

                    self.yang_name = "received-good-bfd-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-good-bfd-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdRequest, [u'packets', u'bytes'], name, value)


            class ReceivedGoodBfdReply(Entity):
                """
                Received Reply with BFD TLV
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodBfdReply, self).__init__()

                    self.yang_name = "received-good-bfd-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "received-good-bfd-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdReply, [u'packets', u'bytes'], name, value)


        class Sent(Entity):
            """
            Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitDrop>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitBfdGood>`
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.BfdNoReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.Sent, self).__init__()

                self.yang_name = "sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Packet.Sent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Packet.Sent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Packet.Sent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Packet.Sent.BfdNoReply))])
                self._leafs = OrderedDict()

                self.transmit_good = MplsOam.Packet.Sent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"

                self.transmit_drop = MplsOam.Packet.Sent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"

                self.transmit_bfd_good = MplsOam.Packet.Sent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                self.bfd_no_reply = MplsOam.Packet.Sent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._segment_path = lambda: "sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.Sent, [], name, value)


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitGood, [u'packets', u'bytes'], name, value)


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitDrop, [u'packets', u'bytes'], name, value)


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.BfdNoReply, [u'packets', u'bytes'], name, value)


        class WorkingReqSent(Entity):
            """
            Working Request Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitDrop>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitBfdGood>`
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.BfdNoReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.WorkingReqSent, self).__init__()

                self.yang_name = "working-req-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Packet.WorkingReqSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Packet.WorkingReqSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Packet.WorkingReqSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Packet.WorkingReqSent.BfdNoReply))])
                self._leafs = OrderedDict()

                self.transmit_good = MplsOam.Packet.WorkingReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"

                self.transmit_drop = MplsOam.Packet.WorkingReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"

                self.transmit_bfd_good = MplsOam.Packet.WorkingReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                self.bfd_no_reply = MplsOam.Packet.WorkingReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._segment_path = lambda: "working-req-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.WorkingReqSent, [], name, value)


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitGood, [u'packets', u'bytes'], name, value)


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitDrop, [u'packets', u'bytes'], name, value)


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.BfdNoReply, [u'packets', u'bytes'], name, value)


        class WorkingRepSent(Entity):
            """
            Working Reply Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitDrop>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitBfdGood>`
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.BfdNoReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.WorkingRepSent, self).__init__()

                self.yang_name = "working-rep-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Packet.WorkingRepSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Packet.WorkingRepSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Packet.WorkingRepSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Packet.WorkingRepSent.BfdNoReply))])
                self._leafs = OrderedDict()

                self.transmit_good = MplsOam.Packet.WorkingRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"

                self.transmit_drop = MplsOam.Packet.WorkingRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"

                self.transmit_bfd_good = MplsOam.Packet.WorkingRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                self.bfd_no_reply = MplsOam.Packet.WorkingRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._segment_path = lambda: "working-rep-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.WorkingRepSent, [], name, value)


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitGood, [u'packets', u'bytes'], name, value)


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitDrop, [u'packets', u'bytes'], name, value)


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.BfdNoReply, [u'packets', u'bytes'], name, value)


        class ProtectReqSent(Entity):
            """
            Protect Request Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitDrop>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitBfdGood>`
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.BfdNoReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.ProtectReqSent, self).__init__()

                self.yang_name = "protect-req-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Packet.ProtectReqSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Packet.ProtectReqSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Packet.ProtectReqSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Packet.ProtectReqSent.BfdNoReply))])
                self._leafs = OrderedDict()

                self.transmit_good = MplsOam.Packet.ProtectReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"

                self.transmit_drop = MplsOam.Packet.ProtectReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"

                self.transmit_bfd_good = MplsOam.Packet.ProtectReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                self.bfd_no_reply = MplsOam.Packet.ProtectReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._segment_path = lambda: "protect-req-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.ProtectReqSent, [], name, value)


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitGood, [u'packets', u'bytes'], name, value)


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitDrop, [u'packets', u'bytes'], name, value)


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.BfdNoReply, [u'packets', u'bytes'], name, value)


        class ProtectRepSent(Entity):
            """
            Protect Reply Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitDrop>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitBfdGood>`
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.BfdNoReply>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.ProtectRepSent, self).__init__()

                self.yang_name = "protect-rep-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transmit-good", ("transmit_good", MplsOam.Packet.ProtectRepSent.TransmitGood)), ("transmit-drop", ("transmit_drop", MplsOam.Packet.ProtectRepSent.TransmitDrop)), ("transmit-bfd-good", ("transmit_bfd_good", MplsOam.Packet.ProtectRepSent.TransmitBfdGood)), ("bfd-no-reply", ("bfd_no_reply", MplsOam.Packet.ProtectRepSent.BfdNoReply))])
                self._leafs = OrderedDict()

                self.transmit_good = MplsOam.Packet.ProtectRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"

                self.transmit_drop = MplsOam.Packet.ProtectRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"

                self.transmit_bfd_good = MplsOam.Packet.ProtectRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"

                self.bfd_no_reply = MplsOam.Packet.ProtectRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._segment_path = lambda: "protect-rep-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Packet.ProtectRepSent, [], name, value)


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitGood, [u'packets', u'bytes'], name, value)


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitDrop, [u'packets', u'bytes'], name, value)


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, [u'packets', u'bytes'], name, value)


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.BfdNoReply, [u'packets', u'bytes'], name, value)


    class Global(Entity):
        """
        LSPV global counters operational data
        
        .. attribute:: message_statistics
        
        	Message statistics
        	**type**\:  :py:class:`MessageStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.MessageStatistics>`
        
        .. attribute:: collaborator_statistics
        
        	Collaborator statistics
        	**type**\:  :py:class:`CollaboratorStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics>`
        
        .. attribute:: total_clients
        
        	Number of clients
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("message-statistics", ("message_statistics", MplsOam.Global.MessageStatistics)), ("collaborator-statistics", ("collaborator_statistics", MplsOam.Global.CollaboratorStatistics))])
            self._leafs = OrderedDict([
                ('total_clients', (YLeaf(YType.uint32, 'total-clients'), ['int'])),
            ])
            self.total_clients = None

            self.message_statistics = MplsOam.Global.MessageStatistics()
            self.message_statistics.parent = self
            self._children_name_map["message_statistics"] = "message-statistics"

            self.collaborator_statistics = MplsOam.Global.CollaboratorStatistics()
            self.collaborator_statistics.parent = self
            self._children_name_map["collaborator_statistics"] = "collaborator-statistics"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsOam.Global, [u'total_clients'], name, value)


        class MessageStatistics(Entity):
            """
            Message statistics
            
            .. attribute:: register_messages
            
            	Message register count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: unregister_messages
            
            	Message unregister count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: echo_submit_messages
            
            	Message echo submit count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: echo_cancel_messages
            
            	Message echo cancel count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_result_messages
            
            	Message get results count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_config_messages
            
            	Message get configiuration count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_response_messages
            
            	Message get response count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_response_messages
            
            	Message property response count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_request_messages
            
            	Message property request count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_block_messages
            
            	Message property block count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: thread_request_messages
            
            	Message thread request count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Global.MessageStatistics, self).__init__()

                self.yang_name = "message-statistics"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('register_messages', (YLeaf(YType.uint32, 'register-messages'), ['int'])),
                    ('unregister_messages', (YLeaf(YType.uint32, 'unregister-messages'), ['int'])),
                    ('echo_submit_messages', (YLeaf(YType.uint32, 'echo-submit-messages'), ['int'])),
                    ('echo_cancel_messages', (YLeaf(YType.uint32, 'echo-cancel-messages'), ['int'])),
                    ('get_result_messages', (YLeaf(YType.uint32, 'get-result-messages'), ['int'])),
                    ('get_config_messages', (YLeaf(YType.uint32, 'get-config-messages'), ['int'])),
                    ('get_response_messages', (YLeaf(YType.uint32, 'get-response-messages'), ['int'])),
                    ('property_response_messages', (YLeaf(YType.uint32, 'property-response-messages'), ['int'])),
                    ('property_request_messages', (YLeaf(YType.uint32, 'property-request-messages'), ['int'])),
                    ('property_block_messages', (YLeaf(YType.uint32, 'property-block-messages'), ['int'])),
                    ('thread_request_messages', (YLeaf(YType.uint32, 'thread-request-messages'), ['int'])),
                ])
                self.register_messages = None
                self.unregister_messages = None
                self.echo_submit_messages = None
                self.echo_cancel_messages = None
                self.get_result_messages = None
                self.get_config_messages = None
                self.get_response_messages = None
                self.property_response_messages = None
                self.property_request_messages = None
                self.property_block_messages = None
                self.thread_request_messages = None
                self._segment_path = lambda: "message-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Global.MessageStatistics, [u'register_messages', u'unregister_messages', u'echo_submit_messages', u'echo_cancel_messages', u'get_result_messages', u'get_config_messages', u'get_response_messages', u'property_response_messages', u'property_request_messages', u'property_block_messages', u'thread_request_messages'], name, value)


        class CollaboratorStatistics(Entity):
            """
            Collaborator statistics
            
            .. attribute:: collaborator_i_parm
            
            	Collaborator IPARM counts
            	**type**\:  :py:class:`CollaboratorIParm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorIParm>`
            
            .. attribute:: collaborator_im
            
            	Collaborator IM counts
            	**type**\:  :py:class:`CollaboratorIm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorIm>`
            
            .. attribute:: collaborator_net_io
            
            	Collaborator NetIO counts
            	**type**\:  :py:class:`CollaboratorNetIo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo>`
            
            .. attribute:: collaborator_rib
            
            	Collaborator RIB counts
            	**type**\:  :py:class:`CollaboratorRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorRib>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Global.CollaboratorStatistics, self).__init__()

                self.yang_name = "collaborator-statistics"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("collaborator-i-parm", ("collaborator_i_parm", MplsOam.Global.CollaboratorStatistics.CollaboratorIParm)), ("collaborator-im", ("collaborator_im", MplsOam.Global.CollaboratorStatistics.CollaboratorIm)), ("collaborator-net-io", ("collaborator_net_io", MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo)), ("collaborator-rib", ("collaborator_rib", MplsOam.Global.CollaboratorStatistics.CollaboratorRib))])
                self._leafs = OrderedDict()

                self.collaborator_i_parm = MplsOam.Global.CollaboratorStatistics.CollaboratorIParm()
                self.collaborator_i_parm.parent = self
                self._children_name_map["collaborator_i_parm"] = "collaborator-i-parm"

                self.collaborator_im = MplsOam.Global.CollaboratorStatistics.CollaboratorIm()
                self.collaborator_im.parent = self
                self._children_name_map["collaborator_im"] = "collaborator-im"

                self.collaborator_net_io = MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo()
                self.collaborator_net_io.parent = self
                self._children_name_map["collaborator_net_io"] = "collaborator-net-io"

                self.collaborator_rib = MplsOam.Global.CollaboratorStatistics.CollaboratorRib()
                self.collaborator_rib.parent = self
                self._children_name_map["collaborator_rib"] = "collaborator-rib"
                self._segment_path = lambda: "collaborator-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Global.CollaboratorStatistics, [], name, value)


            class CollaboratorIParm(Entity):
                """
                Collaborator IPARM counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global.CollaboratorStatistics.CollaboratorIParm, self).__init__()

                    self.yang_name = "collaborator-i-parm"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ups', (YLeaf(YType.uint32, 'ups'), ['int'])),
                        ('downs', (YLeaf(YType.uint32, 'downs'), ['int'])),
                    ])
                    self.ups = None
                    self.downs = None
                    self._segment_path = lambda: "collaborator-i-parm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorIParm, [u'ups', u'downs'], name, value)


            class CollaboratorIm(Entity):
                """
                Collaborator IM counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global.CollaboratorStatistics.CollaboratorIm, self).__init__()

                    self.yang_name = "collaborator-im"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ups', (YLeaf(YType.uint32, 'ups'), ['int'])),
                        ('downs', (YLeaf(YType.uint32, 'downs'), ['int'])),
                    ])
                    self.ups = None
                    self.downs = None
                    self._segment_path = lambda: "collaborator-im"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorIm, [u'ups', u'downs'], name, value)


            class CollaboratorNetIo(Entity):
                """
                Collaborator NetIO counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo, self).__init__()

                    self.yang_name = "collaborator-net-io"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ups', (YLeaf(YType.uint32, 'ups'), ['int'])),
                        ('downs', (YLeaf(YType.uint32, 'downs'), ['int'])),
                    ])
                    self.ups = None
                    self.downs = None
                    self._segment_path = lambda: "collaborator-net-io"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo, [u'ups', u'downs'], name, value)


            class CollaboratorRib(Entity):
                """
                Collaborator RIB counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global.CollaboratorStatistics.CollaboratorRib, self).__init__()

                    self.yang_name = "collaborator-rib"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ups', (YLeaf(YType.uint32, 'ups'), ['int'])),
                        ('downs', (YLeaf(YType.uint32, 'downs'), ['int'])),
                    ])
                    self.ups = None
                    self.downs = None
                    self._segment_path = lambda: "collaborator-rib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorRib, [u'ups', u'downs'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity

