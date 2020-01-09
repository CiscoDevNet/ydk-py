""" Cisco_IOS_XR_mpls_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package operational data.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS OAM operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
        return meta._meta_table['LspvBagInterfaceState']



class MplsOam(_Entity_):
    """
    MPLS OAM operational data
    
    .. attribute:: interface
    
    	MPLS OAM interface operational data
    	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface>`
    
    	**config**\: False
    
    .. attribute:: packet
    
    	LSPV packet counters operational data
    	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet>`
    
    	**config**\: False
    
    .. attribute:: global_
    
    	LSPV global counters operational data
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global>`
    
    	**config**\: False
    
    

    """

    _prefix = 'mpls-oam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Interface(_Entity_):
        """
        MPLS OAM interface operational data
        
        .. attribute:: briefs
        
        	MPLS OAM interface detail data
        	**type**\:  :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs>`
        
        	**config**\: False
        
        .. attribute:: details
        
        	MPLS OAM interface detail data
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details>`
        
        	**config**\: False
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Briefs(_Entity_):
            """
            MPLS OAM interface detail data
            
            .. attribute:: brief
            
            	MPLS OAM interface operational data
            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs.Brief>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Brief(_Entity_):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: interface_name_xr
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: state
                
                	Interface state
                	**type**\:  :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                
                	**config**\: False
                
                .. attribute:: mtu
                
                	Interface MTU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: prefix_length
                
                	Prefix length (IPv4)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: prefix_length_v6
                
                	Prefix length (IPv6)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: primary_address
                
                	Primary interface address (IPv4)
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: primary_address_v6
                
                	Primary interface address (IPv6)
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Interface.Briefs.Brief, ['interface_name', 'interface_name_xr', 'state', 'mtu', 'prefix_length', 'prefix_length_v6', 'primary_address', 'primary_address_v6'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Interface.Briefs.Brief']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Interface.Briefs']['meta_info']


        class Details(_Entity_):
            """
            MPLS OAM interface detail data
            
            .. attribute:: detail
            
            	MPLS OAM interface operational data
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Detail(_Entity_):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: interface_brief
                
                	Interface brief
                	**type**\:  :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.InterfaceBrief>`
                
                	**config**\: False
                
                .. attribute:: packet_statistics
                
                	Packet statistics
                	**type**\:  :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics>`
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class InterfaceBrief(_Entity_):
                    """
                    Interface brief
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: mtu
                    
                    	Interface MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length (IPv4)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_length_v6
                    
                    	Prefix length (IPv6)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: primary_address
                    
                    	Primary interface address (IPv4)
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: primary_address_v6
                    
                    	Primary interface address (IPv6)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(MplsOam.Interface.Details.Detail.InterfaceBrief, ['interface_name_xr', 'state', 'mtu', 'prefix_length', 'prefix_length_v6', 'primary_address', 'primary_address_v6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                        return meta._meta_table['MplsOam.Interface.Details.Detail.InterfaceBrief']['meta_info']


                class PacketStatistics(_Entity_):
                    """
                    Packet statistics
                    
                    .. attribute:: received
                    
                    	Packet reception counts
                    	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received>`
                    
                    	**config**\: False
                    
                    .. attribute:: sent
                    
                    	Packet transmit counts
                    	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent>`
                    
                    	**config**\: False
                    
                    .. attribute:: working_req_sent
                    
                    	Working Request Packet transmit counts
                    	**type**\:  :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent>`
                    
                    	**config**\: False
                    
                    .. attribute:: working_rep_sent
                    
                    	Working Reply Packet transmit counts
                    	**type**\:  :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent>`
                    
                    	**config**\: False
                    
                    .. attribute:: protect_req_sent
                    
                    	Protect Request Packet transmit counts
                    	**type**\:  :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent>`
                    
                    	**config**\: False
                    
                    .. attribute:: protect_rep_sent
                    
                    	Protect Reply Packet transmit counts
                    	**type**\:  :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Received(_Entity_):
                        """
                        Packet reception counts
                        
                        .. attribute:: received_good_request
                        
                        	Received good request
                        	**type**\:  :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_good_reply
                        
                        	Received good reply
                        	**type**\:  :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_unknown
                        
                        	Received unknown packets
                        	**type**\:  :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_ip_header
                        
                        	IP header error
                        	**type**\:  :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_udp_header
                        
                        	UDP header error
                        	**type**\:  :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_runt
                        
                        	RUNT error
                        	**type**\:  :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_queue_full
                        
                        	Dropped queue full
                        	**type**\:  :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_general
                        
                        	General error
                        	**type**\:  :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_no_interface
                        
                        	Error no Interfaces
                        	**type**\:  :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_error_no_memory
                        
                        	Error no memory
                        	**type**\:  :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory>`
                        
                        	**config**\: False
                        
                        .. attribute:: protect_protocol_received_good_request
                        
                        	Protect Protocol Received good request
                        	**type**\:  :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest>`
                        
                        	**config**\: False
                        
                        .. attribute:: protect_protocol_received_good_reply
                        
                        	Protect Protocol Received good reply
                        	**type**\:  :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_good_bfd_request
                        
                        	Received Reqeust with BFD TLV
                        	**type**\:  :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest>`
                        
                        	**config**\: False
                        
                        .. attribute:: received_good_bfd_reply
                        
                        	Received Reply with BFD TLV
                        	**type**\:  :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class ReceivedGoodRequest(_Entity_):
                            """
                            Received good request
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest']['meta_info']


                        class ReceivedGoodReply(_Entity_):
                            """
                            Received good reply
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply']['meta_info']


                        class ReceivedUnknown(_Entity_):
                            """
                            Received unknown packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown']['meta_info']


                        class ReceivedErrorIpHeader(_Entity_):
                            """
                            IP header error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader']['meta_info']


                        class ReceivedErrorUdpHeader(_Entity_):
                            """
                            UDP header error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader']['meta_info']


                        class ReceivedErrorRunt(_Entity_):
                            """
                            RUNT error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt']['meta_info']


                        class ReceivedErrorQueueFull(_Entity_):
                            """
                            Dropped queue full
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull']['meta_info']


                        class ReceivedErrorGeneral(_Entity_):
                            """
                            General error
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral']['meta_info']


                        class ReceivedErrorNoInterface(_Entity_):
                            """
                            Error no Interfaces
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface']['meta_info']


                        class ReceivedErrorNoMemory(_Entity_):
                            """
                            Error no memory
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory']['meta_info']


                        class ProtectProtocolReceivedGoodRequest(_Entity_):
                            """
                            Protect Protocol Received good request
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest']['meta_info']


                        class ProtectProtocolReceivedGoodReply(_Entity_):
                            """
                            Protect Protocol Received good reply
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply']['meta_info']


                        class ReceivedGoodBfdRequest(_Entity_):
                            """
                            Received Reqeust with BFD TLV
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest']['meta_info']


                        class ReceivedGoodBfdReply(_Entity_):
                            """
                            Received Reply with BFD TLV
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']


                    class Sent(_Entity_):
                        """
                        Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class TransmitGood(_Entity_):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood']['meta_info']


                        class TransmitDrop(_Entity_):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(_Entity_):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(_Entity_):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']


                    class WorkingReqSent(_Entity_):
                        """
                        Working Request Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class TransmitGood(_Entity_):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood']['meta_info']


                        class TransmitDrop(_Entity_):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(_Entity_):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(_Entity_):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']


                    class WorkingRepSent(_Entity_):
                        """
                        Working Reply Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class TransmitGood(_Entity_):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood']['meta_info']


                        class TransmitDrop(_Entity_):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(_Entity_):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(_Entity_):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']


                    class ProtectReqSent(_Entity_):
                        """
                        Protect Request Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class TransmitGood(_Entity_):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood']['meta_info']


                        class TransmitDrop(_Entity_):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(_Entity_):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(_Entity_):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']


                    class ProtectRepSent(_Entity_):
                        """
                        Protect Reply Packet transmit counts
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop>`
                        
                        	**config**\: False
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood>`
                        
                        	**config**\: False
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class TransmitGood(_Entity_):
                            """
                            Transmit good packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood']['meta_info']


                        class TransmitDrop(_Entity_):
                            """
                            Transmit drop packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop']['meta_info']


                        class TransmitBfdGood(_Entity_):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood']['meta_info']


                        class BfdNoReply(_Entity_):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                                return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                            return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                        return meta._meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Interface.Details.Detail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Interface.Details']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Interface']['meta_info']


    class Packet(_Entity_):
        """
        LSPV packet counters operational data
        
        .. attribute:: received
        
        	Packet reception counts
        	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received>`
        
        	**config**\: False
        
        .. attribute:: sent
        
        	Packet transmit counts
        	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent>`
        
        	**config**\: False
        
        .. attribute:: working_req_sent
        
        	Working Request Packet transmit counts
        	**type**\:  :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent>`
        
        	**config**\: False
        
        .. attribute:: working_rep_sent
        
        	Working Reply Packet transmit counts
        	**type**\:  :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent>`
        
        	**config**\: False
        
        .. attribute:: protect_req_sent
        
        	Protect Request Packet transmit counts
        	**type**\:  :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent>`
        
        	**config**\: False
        
        .. attribute:: protect_rep_sent
        
        	Protect Reply Packet transmit counts
        	**type**\:  :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent>`
        
        	**config**\: False
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Received(_Entity_):
            """
            Packet reception counts
            
            .. attribute:: received_good_request
            
            	Received good request
            	**type**\:  :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodRequest>`
            
            	**config**\: False
            
            .. attribute:: received_good_reply
            
            	Received good reply
            	**type**\:  :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodReply>`
            
            	**config**\: False
            
            .. attribute:: received_unknown
            
            	Received unknown packets
            	**type**\:  :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedUnknown>`
            
            	**config**\: False
            
            .. attribute:: received_error_ip_header
            
            	IP header error
            	**type**\:  :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorIpHeader>`
            
            	**config**\: False
            
            .. attribute:: received_error_udp_header
            
            	UDP header error
            	**type**\:  :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorUdpHeader>`
            
            	**config**\: False
            
            .. attribute:: received_error_runt
            
            	RUNT error
            	**type**\:  :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorRunt>`
            
            	**config**\: False
            
            .. attribute:: received_error_queue_full
            
            	Dropped queue full
            	**type**\:  :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorQueueFull>`
            
            	**config**\: False
            
            .. attribute:: received_error_general
            
            	General error
            	**type**\:  :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorGeneral>`
            
            	**config**\: False
            
            .. attribute:: received_error_no_interface
            
            	Error no Interfaces
            	**type**\:  :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoInterface>`
            
            	**config**\: False
            
            .. attribute:: received_error_no_memory
            
            	Error no memory
            	**type**\:  :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoMemory>`
            
            	**config**\: False
            
            .. attribute:: protect_protocol_received_good_request
            
            	Protect Protocol Received good request
            	**type**\:  :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest>`
            
            	**config**\: False
            
            .. attribute:: protect_protocol_received_good_reply
            
            	Protect Protocol Received good reply
            	**type**\:  :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply>`
            
            	**config**\: False
            
            .. attribute:: received_good_bfd_request
            
            	Received Reqeust with BFD TLV
            	**type**\:  :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdRequest>`
            
            	**config**\: False
            
            .. attribute:: received_good_bfd_reply
            
            	Received Reply with BFD TLV
            	**type**\:  :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class ReceivedGoodRequest(_Entity_):
                """
                Received good request
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodRequest, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodRequest']['meta_info']


            class ReceivedGoodReply(_Entity_):
                """
                Received good reply
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodReply']['meta_info']


            class ReceivedUnknown(_Entity_):
                """
                Received unknown packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedUnknown, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedUnknown']['meta_info']


            class ReceivedErrorIpHeader(_Entity_):
                """
                IP header error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorIpHeader, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorIpHeader']['meta_info']


            class ReceivedErrorUdpHeader(_Entity_):
                """
                UDP header error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorUdpHeader, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorUdpHeader']['meta_info']


            class ReceivedErrorRunt(_Entity_):
                """
                RUNT error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorRunt, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorRunt']['meta_info']


            class ReceivedErrorQueueFull(_Entity_):
                """
                Dropped queue full
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorQueueFull, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorQueueFull']['meta_info']


            class ReceivedErrorGeneral(_Entity_):
                """
                General error
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorGeneral, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorGeneral']['meta_info']


            class ReceivedErrorNoInterface(_Entity_):
                """
                Error no Interfaces
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoInterface, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorNoInterface']['meta_info']


            class ReceivedErrorNoMemory(_Entity_):
                """
                Error no memory
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoMemory, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedErrorNoMemory']['meta_info']


            class ProtectProtocolReceivedGoodRequest(_Entity_):
                """
                Protect Protocol Received good request
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest']['meta_info']


            class ProtectProtocolReceivedGoodReply(_Entity_):
                """
                Protect Protocol Received good reply
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply']['meta_info']


            class ReceivedGoodBfdRequest(_Entity_):
                """
                Received Reqeust with BFD TLV
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdRequest, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodBfdRequest']['meta_info']


            class ReceivedGoodBfdReply(_Entity_):
                """
                Received Reply with BFD TLV
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Received.ReceivedGoodBfdReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.Received']['meta_info']


        class Sent(_Entity_):
            """
            Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitGood>`
            
            	**config**\: False
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitDrop>`
            
            	**config**\: False
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitBfdGood>`
            
            	**config**\: False
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.BfdNoReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class TransmitGood(_Entity_):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitGood']['meta_info']


            class TransmitDrop(_Entity_):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitDrop, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitDrop']['meta_info']


            class TransmitBfdGood(_Entity_):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.TransmitBfdGood']['meta_info']


            class BfdNoReply(_Entity_):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.Sent.BfdNoReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.Sent.BfdNoReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.Sent']['meta_info']


        class WorkingReqSent(_Entity_):
            """
            Working Request Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitGood>`
            
            	**config**\: False
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitDrop>`
            
            	**config**\: False
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitBfdGood>`
            
            	**config**\: False
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.BfdNoReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class TransmitGood(_Entity_):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitGood']['meta_info']


            class TransmitDrop(_Entity_):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitDrop, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(_Entity_):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(_Entity_):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.BfdNoReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingReqSent.BfdNoReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']


        class WorkingRepSent(_Entity_):
            """
            Working Reply Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitGood>`
            
            	**config**\: False
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitDrop>`
            
            	**config**\: False
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitBfdGood>`
            
            	**config**\: False
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.BfdNoReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class TransmitGood(_Entity_):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitGood']['meta_info']


            class TransmitDrop(_Entity_):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitDrop, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(_Entity_):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(_Entity_):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.BfdNoReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.WorkingRepSent.BfdNoReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']


        class ProtectReqSent(_Entity_):
            """
            Protect Request Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitGood>`
            
            	**config**\: False
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitDrop>`
            
            	**config**\: False
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitBfdGood>`
            
            	**config**\: False
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.BfdNoReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class TransmitGood(_Entity_):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitGood']['meta_info']


            class TransmitDrop(_Entity_):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitDrop, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(_Entity_):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(_Entity_):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.BfdNoReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectReqSent.BfdNoReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']


        class ProtectRepSent(_Entity_):
            """
            Protect Reply Packet transmit counts
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:  :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitGood>`
            
            	**config**\: False
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:  :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitDrop>`
            
            	**config**\: False
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:  :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitBfdGood>`
            
            	**config**\: False
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:  :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.BfdNoReply>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class TransmitGood(_Entity_):
                """
                Transmit good packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitGood']['meta_info']


            class TransmitDrop(_Entity_):
                """
                Transmit drop packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitDrop, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitDrop']['meta_info']


            class TransmitBfdGood(_Entity_):
                """
                Transmit good BFD request packets
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.TransmitBfdGood']['meta_info']


            class BfdNoReply(_Entity_):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.BfdNoReply, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Packet.ProtectRepSent.BfdNoReply']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Packet']['meta_info']


    class Global(_Entity_):
        """
        LSPV global counters operational data
        
        .. attribute:: message_statistics
        
        	Message statistics
        	**type**\:  :py:class:`MessageStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.MessageStatistics>`
        
        	**config**\: False
        
        .. attribute:: collaborator_statistics
        
        	Collaborator statistics
        	**type**\:  :py:class:`CollaboratorStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics>`
        
        	**config**\: False
        
        .. attribute:: total_clients
        
        	Number of clients
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._perform_setattr(MplsOam.Global, ['total_clients'], name, value)


        class MessageStatistics(_Entity_):
            """
            Message statistics
            
            .. attribute:: register_messages
            
            	Message register count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: unregister_messages
            
            	Message unregister count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: echo_submit_messages
            
            	Message echo submit count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: echo_cancel_messages
            
            	Message echo cancel count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_result_messages
            
            	Message get results count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_config_messages
            
            	Message get configiuration count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_response_messages
            
            	Message get response count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: property_response_messages
            
            	Message property response count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: property_request_messages
            
            	Message property request count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: property_block_messages
            
            	Message property block count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: thread_request_messages
            
            	Message thread request count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(MplsOam.Global.MessageStatistics, ['register_messages', 'unregister_messages', 'echo_submit_messages', 'echo_cancel_messages', 'get_result_messages', 'get_config_messages', 'get_response_messages', 'property_response_messages', 'property_request_messages', 'property_block_messages', 'thread_request_messages'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Global.MessageStatistics']['meta_info']


        class CollaboratorStatistics(_Entity_):
            """
            Collaborator statistics
            
            .. attribute:: collaborator_i_parm
            
            	Collaborator IPARM counts
            	**type**\:  :py:class:`CollaboratorIParm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorIParm>`
            
            	**config**\: False
            
            .. attribute:: collaborator_im
            
            	Collaborator IM counts
            	**type**\:  :py:class:`CollaboratorIm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorIm>`
            
            	**config**\: False
            
            .. attribute:: collaborator_net_io
            
            	Collaborator NetIO counts
            	**type**\:  :py:class:`CollaboratorNetIo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo>`
            
            	**config**\: False
            
            .. attribute:: collaborator_rib
            
            	Collaborator RIB counts
            	**type**\:  :py:class:`CollaboratorRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global.CollaboratorStatistics.CollaboratorRib>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class CollaboratorIParm(_Entity_):
                """
                Collaborator IPARM counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorIParm, ['ups', 'downs'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global.CollaboratorStatistics.CollaboratorIParm']['meta_info']


            class CollaboratorIm(_Entity_):
                """
                Collaborator IM counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorIm, ['ups', 'downs'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global.CollaboratorStatistics.CollaboratorIm']['meta_info']


            class CollaboratorNetIo(_Entity_):
                """
                Collaborator NetIO counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo, ['ups', 'downs'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global.CollaboratorStatistics.CollaboratorNetIo']['meta_info']


            class CollaboratorRib(_Entity_):
                """
                Collaborator RIB counts
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(MplsOam.Global.CollaboratorStatistics.CollaboratorRib, ['ups', 'downs'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                    return meta._meta_table['MplsOam.Global.CollaboratorStatistics.CollaboratorRib']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
                return meta._meta_table['MplsOam.Global.CollaboratorStatistics']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
            return meta._meta_table['MplsOam.Global']['meta_info']

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_oam_oper as meta
        return meta._meta_table['MplsOam']['meta_info']


