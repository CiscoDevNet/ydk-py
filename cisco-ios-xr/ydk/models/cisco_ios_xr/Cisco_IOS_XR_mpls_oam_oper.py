""" Cisco_IOS_XR_mpls_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package operational data.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS OAM operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LspvBagInterfaceState(Enum):
    """
    LspvBagInterfaceState

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
        super(MplsOam, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-oam"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-oam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global" : ("global_", MplsOam.Global_), "interface" : ("interface", MplsOam.Interface), "packet" : ("packet", MplsOam.Packet)}
        self._child_list_classes = {}

        self.global_ = MplsOam.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.interface = MplsOam.Interface()
        self.interface.parent = self
        self._children_name_map["interface"] = "interface"
        self._children_yang_names.add("interface")

        self.packet = MplsOam.Packet()
        self.packet.parent = self
        self._children_name_map["packet"] = "packet"
        self._children_yang_names.add("packet")
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam"


    class Global_(Entity):
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
            super(MplsOam.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"collaborator-statistics" : ("collaborator_statistics", MplsOam.Global_.CollaboratorStatistics), "message-statistics" : ("message_statistics", MplsOam.Global_.MessageStatistics)}
            self._child_list_classes = {}

            self.total_clients = YLeaf(YType.uint32, "total-clients")

            self.collaborator_statistics = MplsOam.Global_.CollaboratorStatistics()
            self.collaborator_statistics.parent = self
            self._children_name_map["collaborator_statistics"] = "collaborator-statistics"
            self._children_yang_names.add("collaborator-statistics")

            self.message_statistics = MplsOam.Global_.MessageStatistics()
            self.message_statistics.parent = self
            self._children_name_map["message_statistics"] = "message-statistics"
            self._children_yang_names.add("message-statistics")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsOam.Global_, ['total_clients'], name, value)


        class CollaboratorStatistics(Entity):
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
                super(MplsOam.Global_.CollaboratorStatistics, self).__init__()

                self.yang_name = "collaborator-statistics"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"collaborator-i-parm" : ("collaborator_i_parm", MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm), "collaborator-im" : ("collaborator_im", MplsOam.Global_.CollaboratorStatistics.CollaboratorIm), "collaborator-net-io" : ("collaborator_net_io", MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo), "collaborator-rib" : ("collaborator_rib", MplsOam.Global_.CollaboratorStatistics.CollaboratorRib)}
                self._child_list_classes = {}

                self.collaborator_i_parm = MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm()
                self.collaborator_i_parm.parent = self
                self._children_name_map["collaborator_i_parm"] = "collaborator-i-parm"
                self._children_yang_names.add("collaborator-i-parm")

                self.collaborator_im = MplsOam.Global_.CollaboratorStatistics.CollaboratorIm()
                self.collaborator_im.parent = self
                self._children_name_map["collaborator_im"] = "collaborator-im"
                self._children_yang_names.add("collaborator-im")

                self.collaborator_net_io = MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo()
                self.collaborator_net_io.parent = self
                self._children_name_map["collaborator_net_io"] = "collaborator-net-io"
                self._children_yang_names.add("collaborator-net-io")

                self.collaborator_rib = MplsOam.Global_.CollaboratorStatistics.CollaboratorRib()
                self.collaborator_rib.parent = self
                self._children_name_map["collaborator_rib"] = "collaborator-rib"
                self._children_yang_names.add("collaborator-rib")
                self._segment_path = lambda: "collaborator-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self._segment_path()


            class CollaboratorIParm(Entity):
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
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm, self).__init__()

                    self.yang_name = "collaborator-i-parm"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")
                    self._segment_path = lambda: "collaborator-i-parm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm, ['downs', 'ups'], name, value)


            class CollaboratorIm(Entity):
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
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIm, self).__init__()

                    self.yang_name = "collaborator-im"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")
                    self._segment_path = lambda: "collaborator-im"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global_.CollaboratorStatistics.CollaboratorIm, ['downs', 'ups'], name, value)


            class CollaboratorNetIo(Entity):
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
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo, self).__init__()

                    self.yang_name = "collaborator-net-io"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")
                    self._segment_path = lambda: "collaborator-net-io"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo, ['downs', 'ups'], name, value)


            class CollaboratorRib(Entity):
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
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorRib, self).__init__()

                    self.yang_name = "collaborator-rib"
                    self.yang_parent_name = "collaborator-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")
                    self._segment_path = lambda: "collaborator-rib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Global_.CollaboratorStatistics.CollaboratorRib, ['downs', 'ups'], name, value)


        class MessageStatistics(Entity):
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
                super(MplsOam.Global_.MessageStatistics, self).__init__()

                self.yang_name = "message-statistics"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.echo_cancel_messages = YLeaf(YType.uint32, "echo-cancel-messages")

                self.echo_submit_messages = YLeaf(YType.uint32, "echo-submit-messages")

                self.get_config_messages = YLeaf(YType.uint32, "get-config-messages")

                self.get_response_messages = YLeaf(YType.uint32, "get-response-messages")

                self.get_result_messages = YLeaf(YType.uint32, "get-result-messages")

                self.property_block_messages = YLeaf(YType.uint32, "property-block-messages")

                self.property_request_messages = YLeaf(YType.uint32, "property-request-messages")

                self.property_response_messages = YLeaf(YType.uint32, "property-response-messages")

                self.register_messages = YLeaf(YType.uint32, "register-messages")

                self.thread_request_messages = YLeaf(YType.uint32, "thread-request-messages")

                self.unregister_messages = YLeaf(YType.uint32, "unregister-messages")
                self._segment_path = lambda: "message-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Global_.MessageStatistics, ['echo_cancel_messages', 'echo_submit_messages', 'get_config_messages', 'get_response_messages', 'get_result_messages', 'property_block_messages', 'property_request_messages', 'property_response_messages', 'register_messages', 'thread_request_messages', 'unregister_messages'], name, value)


    class Interface(Entity):
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
            super(MplsOam.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"briefs" : ("briefs", MplsOam.Interface.Briefs), "details" : ("details", MplsOam.Interface.Details)}
            self._child_list_classes = {}

            self.briefs = MplsOam.Interface.Briefs()
            self.briefs.parent = self
            self._children_name_map["briefs"] = "briefs"
            self._children_yang_names.add("briefs")

            self.details = MplsOam.Interface.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")
            self._segment_path = lambda: "interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()


        class Briefs(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: brief
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs.Brief>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Briefs, self).__init__()

                self.yang_name = "briefs"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"brief" : ("brief", MplsOam.Interface.Briefs.Brief)}

                self.brief = YList(self)
                self._segment_path = lambda: "briefs"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Interface.Briefs, [], name, value)


            class Brief(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: interface_name_xr
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                	**type**\:   :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Interface.Briefs.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "briefs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.prefix_length_v6 = YLeaf(YType.uint32, "prefix-length-v6")

                    self.primary_address = YLeaf(YType.str, "primary-address")

                    self.primary_address_v6 = YLeaf(YType.str, "primary-address-v6")

                    self.state = YLeaf(YType.enumeration, "state")
                    self._segment_path = lambda: "brief" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/briefs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Interface.Briefs.Brief, ['interface_name', 'interface_name_xr', 'mtu', 'prefix_length', 'prefix_length_v6', 'primary_address', 'primary_address_v6', 'state'], name, value)


        class Details(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: detail
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"detail" : ("detail", MplsOam.Interface.Details.Detail)}

                self.detail = YList(self)
                self._segment_path = lambda: "details"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsOam.Interface.Details, [], name, value)


            class Detail(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                    super(MplsOam.Interface.Details.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"interface-brief" : ("interface_brief", MplsOam.Interface.Details.Detail.InterfaceBrief), "packet-statistics" : ("packet_statistics", MplsOam.Interface.Details.Detail.PacketStatistics)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface_brief = MplsOam.Interface.Details.Detail.InterfaceBrief()
                    self.interface_brief.parent = self
                    self._children_name_map["interface_brief"] = "interface-brief"
                    self._children_yang_names.add("interface-brief")

                    self.packet_statistics = MplsOam.Interface.Details.Detail.PacketStatistics()
                    self.packet_statistics.parent = self
                    self._children_name_map["packet_statistics"] = "packet-statistics"
                    self._children_yang_names.add("packet-statistics")
                    self._segment_path = lambda: "detail" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/details/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Interface.Details.Detail, ['interface_name'], name, value)


                class InterfaceBrief(Entity):
                    """
                    Interface brief
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                    	**type**\:   :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsOam.Interface.Details.Detail.InterfaceBrief, self).__init__()

                        self.yang_name = "interface-brief"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.mtu = YLeaf(YType.uint32, "mtu")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.prefix_length_v6 = YLeaf(YType.uint32, "prefix-length-v6")

                        self.primary_address = YLeaf(YType.str, "primary-address")

                        self.primary_address_v6 = YLeaf(YType.str, "primary-address-v6")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "interface-brief"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsOam.Interface.Details.Detail.InterfaceBrief, ['interface_name_xr', 'mtu', 'prefix_length', 'prefix_length_v6', 'primary_address', 'primary_address_v6', 'state'], name, value)


                class PacketStatistics(Entity):
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
                        super(MplsOam.Interface.Details.Detail.PacketStatistics, self).__init__()

                        self.yang_name = "packet-statistics"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"protect-rep-sent" : ("protect_rep_sent", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent), "protect-req-sent" : ("protect_req_sent", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent), "received" : ("received", MplsOam.Interface.Details.Detail.PacketStatistics.Received), "sent" : ("sent", MplsOam.Interface.Details.Detail.PacketStatistics.Sent), "working-rep-sent" : ("working_rep_sent", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent), "working-req-sent" : ("working_req_sent", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent)}
                        self._child_list_classes = {}

                        self.protect_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent()
                        self.protect_rep_sent.parent = self
                        self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
                        self._children_yang_names.add("protect-rep-sent")

                        self.protect_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent()
                        self.protect_req_sent.parent = self
                        self._children_name_map["protect_req_sent"] = "protect-req-sent"
                        self._children_yang_names.add("protect-req-sent")

                        self.received = MplsOam.Interface.Details.Detail.PacketStatistics.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"
                        self._children_yang_names.add("received")

                        self.sent = MplsOam.Interface.Details.Detail.PacketStatistics.Sent()
                        self.sent.parent = self
                        self._children_name_map["sent"] = "sent"
                        self._children_yang_names.add("sent")

                        self.working_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent()
                        self.working_rep_sent.parent = self
                        self._children_name_map["working_rep_sent"] = "working-rep-sent"
                        self._children_yang_names.add("working-rep-sent")

                        self.working_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent()
                        self.working_req_sent.parent = self
                        self._children_name_map["working_req_sent"] = "working-req-sent"
                        self._children_yang_names.add("working-req-sent")
                        self._segment_path = lambda: "packet-statistics"


                    class ProtectRepSent(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent, self).__init__()

                            self.yang_name = "protect-rep-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood)}
                            self._child_list_classes = {}

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")
                            self._segment_path = lambda: "protect-rep-sent"


                        class BfdNoReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "bfd-no-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, ['bytes', 'packets'], name, value)


                        class TransmitBfdGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-bfd-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


                        class TransmitDrop(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, ['bytes', 'packets'], name, value)


                        class TransmitGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, ['bytes', 'packets'], name, value)


                    class ProtectReqSent(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent, self).__init__()

                            self.yang_name = "protect-req-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood)}
                            self._child_list_classes = {}

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")
                            self._segment_path = lambda: "protect-req-sent"


                        class BfdNoReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "bfd-no-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, ['bytes', 'packets'], name, value)


                        class TransmitBfdGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-bfd-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


                        class TransmitDrop(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, ['bytes', 'packets'], name, value)


                        class TransmitGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, ['bytes', 'packets'], name, value)


                    class Received(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"protect-protocol-received-good-reply" : ("protect_protocol_received_good_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply), "protect-protocol-received-good-request" : ("protect_protocol_received_good_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest), "received-error-general" : ("received_error_general", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral), "received-error-ip-header" : ("received_error_ip_header", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader), "received-error-no-interface" : ("received_error_no_interface", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface), "received-error-no-memory" : ("received_error_no_memory", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory), "received-error-queue-full" : ("received_error_queue_full", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull), "received-error-runt" : ("received_error_runt", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt), "received-error-udp-header" : ("received_error_udp_header", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader), "received-good-bfd-reply" : ("received_good_bfd_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply), "received-good-bfd-request" : ("received_good_bfd_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest), "received-good-reply" : ("received_good_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply), "received-good-request" : ("received_good_request", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest), "received-unknown" : ("received_unknown", MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown)}
                            self._child_list_classes = {}

                            self.protect_protocol_received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply()
                            self.protect_protocol_received_good_reply.parent = self
                            self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                            self._children_yang_names.add("protect-protocol-received-good-reply")

                            self.protect_protocol_received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest()
                            self.protect_protocol_received_good_request.parent = self
                            self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                            self._children_yang_names.add("protect-protocol-received-good-request")

                            self.received_error_general = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral()
                            self.received_error_general.parent = self
                            self._children_name_map["received_error_general"] = "received-error-general"
                            self._children_yang_names.add("received-error-general")

                            self.received_error_ip_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader()
                            self.received_error_ip_header.parent = self
                            self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                            self._children_yang_names.add("received-error-ip-header")

                            self.received_error_no_interface = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface()
                            self.received_error_no_interface.parent = self
                            self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                            self._children_yang_names.add("received-error-no-interface")

                            self.received_error_no_memory = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory()
                            self.received_error_no_memory.parent = self
                            self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                            self._children_yang_names.add("received-error-no-memory")

                            self.received_error_queue_full = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull()
                            self.received_error_queue_full.parent = self
                            self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                            self._children_yang_names.add("received-error-queue-full")

                            self.received_error_runt = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt()
                            self.received_error_runt.parent = self
                            self._children_name_map["received_error_runt"] = "received-error-runt"
                            self._children_yang_names.add("received-error-runt")

                            self.received_error_udp_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader()
                            self.received_error_udp_header.parent = self
                            self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                            self._children_yang_names.add("received-error-udp-header")

                            self.received_good_bfd_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply()
                            self.received_good_bfd_reply.parent = self
                            self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                            self._children_yang_names.add("received-good-bfd-reply")

                            self.received_good_bfd_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest()
                            self.received_good_bfd_request.parent = self
                            self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                            self._children_yang_names.add("received-good-bfd-request")

                            self.received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply()
                            self.received_good_reply.parent = self
                            self._children_name_map["received_good_reply"] = "received-good-reply"
                            self._children_yang_names.add("received-good-reply")

                            self.received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest()
                            self.received_good_request.parent = self
                            self._children_name_map["received_good_request"] = "received-good-request"
                            self._children_yang_names.add("received-good-request")

                            self.received_unknown = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown()
                            self.received_unknown.parent = self
                            self._children_name_map["received_unknown"] = "received-unknown"
                            self._children_yang_names.add("received-unknown")
                            self._segment_path = lambda: "received"


                        class ProtectProtocolReceivedGoodReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                                self.yang_name = "protect-protocol-received-good-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "protect-protocol-received-good-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, ['bytes', 'packets'], name, value)


                        class ProtectProtocolReceivedGoodRequest(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                                self.yang_name = "protect-protocol-received-good-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "protect-protocol-received-good-request"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, ['bytes', 'packets'], name, value)


                        class ReceivedErrorGeneral(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, self).__init__()

                                self.yang_name = "received-error-general"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-general"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, ['bytes', 'packets'], name, value)


                        class ReceivedErrorIpHeader(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, self).__init__()

                                self.yang_name = "received-error-ip-header"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-ip-header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, ['bytes', 'packets'], name, value)


                        class ReceivedErrorNoInterface(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, self).__init__()

                                self.yang_name = "received-error-no-interface"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-no-interface"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, ['bytes', 'packets'], name, value)


                        class ReceivedErrorNoMemory(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, self).__init__()

                                self.yang_name = "received-error-no-memory"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-no-memory"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, ['bytes', 'packets'], name, value)


                        class ReceivedErrorQueueFull(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, self).__init__()

                                self.yang_name = "received-error-queue-full"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-queue-full"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, ['bytes', 'packets'], name, value)


                        class ReceivedErrorRunt(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, self).__init__()

                                self.yang_name = "received-error-runt"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-runt"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, ['bytes', 'packets'], name, value)


                        class ReceivedErrorUdpHeader(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, self).__init__()

                                self.yang_name = "received-error-udp-header"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-error-udp-header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, ['bytes', 'packets'], name, value)


                        class ReceivedGoodBfdReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, self).__init__()

                                self.yang_name = "received-good-bfd-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-good-bfd-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, ['bytes', 'packets'], name, value)


                        class ReceivedGoodBfdRequest(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, self).__init__()

                                self.yang_name = "received-good-bfd-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-good-bfd-request"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, ['bytes', 'packets'], name, value)


                        class ReceivedGoodReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, self).__init__()

                                self.yang_name = "received-good-reply"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-good-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, ['bytes', 'packets'], name, value)


                        class ReceivedGoodRequest(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, self).__init__()

                                self.yang_name = "received-good-request"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-good-request"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, ['bytes', 'packets'], name, value)


                        class ReceivedUnknown(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, self).__init__()

                                self.yang_name = "received-unknown"
                                self.yang_parent_name = "received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "received-unknown"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, ['bytes', 'packets'], name, value)


                    class Sent(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent, self).__init__()

                            self.yang_name = "sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood)}
                            self._child_list_classes = {}

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")
                            self._segment_path = lambda: "sent"


                        class BfdNoReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "bfd-no-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, ['bytes', 'packets'], name, value)


                        class TransmitBfdGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-bfd-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, ['bytes', 'packets'], name, value)


                        class TransmitDrop(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, ['bytes', 'packets'], name, value)


                        class TransmitGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, ['bytes', 'packets'], name, value)


                    class WorkingRepSent(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent, self).__init__()

                            self.yang_name = "working-rep-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood)}
                            self._child_list_classes = {}

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")
                            self._segment_path = lambda: "working-rep-sent"


                        class BfdNoReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "bfd-no-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, ['bytes', 'packets'], name, value)


                        class TransmitBfdGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-bfd-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


                        class TransmitDrop(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, ['bytes', 'packets'], name, value)


                        class TransmitGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-rep-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, ['bytes', 'packets'], name, value)


                    class WorkingReqSent(Entity):
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
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent, self).__init__()

                            self.yang_name = "working-req-sent"
                            self.yang_parent_name = "packet-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood)}
                            self._child_list_classes = {}

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")
                            self._segment_path = lambda: "working-req-sent"


                        class BfdNoReply(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "bfd-no-reply"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, ['bytes', 'packets'], name, value)


                        class TransmitBfdGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-bfd-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


                        class TransmitDrop(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, ['bytes', 'packets'], name, value)


                        class TransmitGood(Entity):
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
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-req-sent"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")
                                self._segment_path = lambda: "transmit-good"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, ['bytes', 'packets'], name, value)


    class Packet(Entity):
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
            super(MplsOam.Packet, self).__init__()

            self.yang_name = "packet"
            self.yang_parent_name = "mpls-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"protect-rep-sent" : ("protect_rep_sent", MplsOam.Packet.ProtectRepSent), "protect-req-sent" : ("protect_req_sent", MplsOam.Packet.ProtectReqSent), "received" : ("received", MplsOam.Packet.Received), "sent" : ("sent", MplsOam.Packet.Sent), "working-rep-sent" : ("working_rep_sent", MplsOam.Packet.WorkingRepSent), "working-req-sent" : ("working_req_sent", MplsOam.Packet.WorkingReqSent)}
            self._child_list_classes = {}

            self.protect_rep_sent = MplsOam.Packet.ProtectRepSent()
            self.protect_rep_sent.parent = self
            self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
            self._children_yang_names.add("protect-rep-sent")

            self.protect_req_sent = MplsOam.Packet.ProtectReqSent()
            self.protect_req_sent.parent = self
            self._children_name_map["protect_req_sent"] = "protect-req-sent"
            self._children_yang_names.add("protect-req-sent")

            self.received = MplsOam.Packet.Received()
            self.received.parent = self
            self._children_name_map["received"] = "received"
            self._children_yang_names.add("received")

            self.sent = MplsOam.Packet.Sent()
            self.sent.parent = self
            self._children_name_map["sent"] = "sent"
            self._children_yang_names.add("sent")

            self.working_rep_sent = MplsOam.Packet.WorkingRepSent()
            self.working_rep_sent.parent = self
            self._children_name_map["working_rep_sent"] = "working-rep-sent"
            self._children_yang_names.add("working-rep-sent")

            self.working_req_sent = MplsOam.Packet.WorkingReqSent()
            self.working_req_sent.parent = self
            self._children_name_map["working_req_sent"] = "working-req-sent"
            self._children_yang_names.add("working-req-sent")
            self._segment_path = lambda: "packet"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self._segment_path()


        class ProtectRepSent(Entity):
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
                super(MplsOam.Packet.ProtectRepSent, self).__init__()

                self.yang_name = "protect-rep-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Packet.ProtectRepSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Packet.ProtectRepSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Packet.ProtectRepSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Packet.ProtectRepSent.TransmitGood)}
                self._child_list_classes = {}

                self.bfd_no_reply = MplsOam.Packet.ProtectRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.ProtectRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.ProtectRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.ProtectRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")
                self._segment_path = lambda: "protect-rep-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class BfdNoReply(Entity):
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
                    super(MplsOam.Packet.ProtectRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.BfdNoReply, ['bytes', 'packets'], name, value)


            class TransmitBfdGood(Entity):
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
                    super(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


            class TransmitDrop(Entity):
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
                    super(MplsOam.Packet.ProtectRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitDrop, ['bytes', 'packets'], name, value)


            class TransmitGood(Entity):
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
                    super(MplsOam.Packet.ProtectRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectRepSent.TransmitGood, ['bytes', 'packets'], name, value)


        class ProtectReqSent(Entity):
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
                super(MplsOam.Packet.ProtectReqSent, self).__init__()

                self.yang_name = "protect-req-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Packet.ProtectReqSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Packet.ProtectReqSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Packet.ProtectReqSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Packet.ProtectReqSent.TransmitGood)}
                self._child_list_classes = {}

                self.bfd_no_reply = MplsOam.Packet.ProtectReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.ProtectReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.ProtectReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.ProtectReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")
                self._segment_path = lambda: "protect-req-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class BfdNoReply(Entity):
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
                    super(MplsOam.Packet.ProtectReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.BfdNoReply, ['bytes', 'packets'], name, value)


            class TransmitBfdGood(Entity):
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
                    super(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


            class TransmitDrop(Entity):
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
                    super(MplsOam.Packet.ProtectReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitDrop, ['bytes', 'packets'], name, value)


            class TransmitGood(Entity):
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
                    super(MplsOam.Packet.ProtectReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.ProtectReqSent.TransmitGood, ['bytes', 'packets'], name, value)


        class Received(Entity):
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
                super(MplsOam.Packet.Received, self).__init__()

                self.yang_name = "received"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"protect-protocol-received-good-reply" : ("protect_protocol_received_good_reply", MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply), "protect-protocol-received-good-request" : ("protect_protocol_received_good_request", MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest), "received-error-general" : ("received_error_general", MplsOam.Packet.Received.ReceivedErrorGeneral), "received-error-ip-header" : ("received_error_ip_header", MplsOam.Packet.Received.ReceivedErrorIpHeader), "received-error-no-interface" : ("received_error_no_interface", MplsOam.Packet.Received.ReceivedErrorNoInterface), "received-error-no-memory" : ("received_error_no_memory", MplsOam.Packet.Received.ReceivedErrorNoMemory), "received-error-queue-full" : ("received_error_queue_full", MplsOam.Packet.Received.ReceivedErrorQueueFull), "received-error-runt" : ("received_error_runt", MplsOam.Packet.Received.ReceivedErrorRunt), "received-error-udp-header" : ("received_error_udp_header", MplsOam.Packet.Received.ReceivedErrorUdpHeader), "received-good-bfd-reply" : ("received_good_bfd_reply", MplsOam.Packet.Received.ReceivedGoodBfdReply), "received-good-bfd-request" : ("received_good_bfd_request", MplsOam.Packet.Received.ReceivedGoodBfdRequest), "received-good-reply" : ("received_good_reply", MplsOam.Packet.Received.ReceivedGoodReply), "received-good-request" : ("received_good_request", MplsOam.Packet.Received.ReceivedGoodRequest), "received-unknown" : ("received_unknown", MplsOam.Packet.Received.ReceivedUnknown)}
                self._child_list_classes = {}

                self.protect_protocol_received_good_reply = MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply()
                self.protect_protocol_received_good_reply.parent = self
                self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                self._children_yang_names.add("protect-protocol-received-good-reply")

                self.protect_protocol_received_good_request = MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest()
                self.protect_protocol_received_good_request.parent = self
                self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                self._children_yang_names.add("protect-protocol-received-good-request")

                self.received_error_general = MplsOam.Packet.Received.ReceivedErrorGeneral()
                self.received_error_general.parent = self
                self._children_name_map["received_error_general"] = "received-error-general"
                self._children_yang_names.add("received-error-general")

                self.received_error_ip_header = MplsOam.Packet.Received.ReceivedErrorIpHeader()
                self.received_error_ip_header.parent = self
                self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                self._children_yang_names.add("received-error-ip-header")

                self.received_error_no_interface = MplsOam.Packet.Received.ReceivedErrorNoInterface()
                self.received_error_no_interface.parent = self
                self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                self._children_yang_names.add("received-error-no-interface")

                self.received_error_no_memory = MplsOam.Packet.Received.ReceivedErrorNoMemory()
                self.received_error_no_memory.parent = self
                self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                self._children_yang_names.add("received-error-no-memory")

                self.received_error_queue_full = MplsOam.Packet.Received.ReceivedErrorQueueFull()
                self.received_error_queue_full.parent = self
                self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                self._children_yang_names.add("received-error-queue-full")

                self.received_error_runt = MplsOam.Packet.Received.ReceivedErrorRunt()
                self.received_error_runt.parent = self
                self._children_name_map["received_error_runt"] = "received-error-runt"
                self._children_yang_names.add("received-error-runt")

                self.received_error_udp_header = MplsOam.Packet.Received.ReceivedErrorUdpHeader()
                self.received_error_udp_header.parent = self
                self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                self._children_yang_names.add("received-error-udp-header")

                self.received_good_bfd_reply = MplsOam.Packet.Received.ReceivedGoodBfdReply()
                self.received_good_bfd_reply.parent = self
                self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                self._children_yang_names.add("received-good-bfd-reply")

                self.received_good_bfd_request = MplsOam.Packet.Received.ReceivedGoodBfdRequest()
                self.received_good_bfd_request.parent = self
                self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                self._children_yang_names.add("received-good-bfd-request")

                self.received_good_reply = MplsOam.Packet.Received.ReceivedGoodReply()
                self.received_good_reply.parent = self
                self._children_name_map["received_good_reply"] = "received-good-reply"
                self._children_yang_names.add("received-good-reply")

                self.received_good_request = MplsOam.Packet.Received.ReceivedGoodRequest()
                self.received_good_request.parent = self
                self._children_name_map["received_good_request"] = "received-good-request"
                self._children_yang_names.add("received-good-request")

                self.received_unknown = MplsOam.Packet.Received.ReceivedUnknown()
                self.received_unknown.parent = self
                self._children_name_map["received_unknown"] = "received-unknown"
                self._children_yang_names.add("received-unknown")
                self._segment_path = lambda: "received"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class ProtectProtocolReceivedGoodReply(Entity):
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
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                    self.yang_name = "protect-protocol-received-good-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "protect-protocol-received-good-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, ['bytes', 'packets'], name, value)


            class ProtectProtocolReceivedGoodRequest(Entity):
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
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                    self.yang_name = "protect-protocol-received-good-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "protect-protocol-received-good-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, ['bytes', 'packets'], name, value)


            class ReceivedErrorGeneral(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorGeneral, self).__init__()

                    self.yang_name = "received-error-general"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-general"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorGeneral, ['bytes', 'packets'], name, value)


            class ReceivedErrorIpHeader(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorIpHeader, self).__init__()

                    self.yang_name = "received-error-ip-header"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-ip-header"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorIpHeader, ['bytes', 'packets'], name, value)


            class ReceivedErrorNoInterface(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorNoInterface, self).__init__()

                    self.yang_name = "received-error-no-interface"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-no-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoInterface, ['bytes', 'packets'], name, value)


            class ReceivedErrorNoMemory(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorNoMemory, self).__init__()

                    self.yang_name = "received-error-no-memory"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-no-memory"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorNoMemory, ['bytes', 'packets'], name, value)


            class ReceivedErrorQueueFull(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorQueueFull, self).__init__()

                    self.yang_name = "received-error-queue-full"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-queue-full"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorQueueFull, ['bytes', 'packets'], name, value)


            class ReceivedErrorRunt(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorRunt, self).__init__()

                    self.yang_name = "received-error-runt"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-runt"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorRunt, ['bytes', 'packets'], name, value)


            class ReceivedErrorUdpHeader(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedErrorUdpHeader, self).__init__()

                    self.yang_name = "received-error-udp-header"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-error-udp-header"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedErrorUdpHeader, ['bytes', 'packets'], name, value)


            class ReceivedGoodBfdReply(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedGoodBfdReply, self).__init__()

                    self.yang_name = "received-good-bfd-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-good-bfd-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdReply, ['bytes', 'packets'], name, value)


            class ReceivedGoodBfdRequest(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedGoodBfdRequest, self).__init__()

                    self.yang_name = "received-good-bfd-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-good-bfd-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodBfdRequest, ['bytes', 'packets'], name, value)


            class ReceivedGoodReply(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedGoodReply, self).__init__()

                    self.yang_name = "received-good-reply"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-good-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodReply, ['bytes', 'packets'], name, value)


            class ReceivedGoodRequest(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedGoodRequest, self).__init__()

                    self.yang_name = "received-good-request"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-good-request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedGoodRequest, ['bytes', 'packets'], name, value)


            class ReceivedUnknown(Entity):
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
                    super(MplsOam.Packet.Received.ReceivedUnknown, self).__init__()

                    self.yang_name = "received-unknown"
                    self.yang_parent_name = "received"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "received-unknown"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Received.ReceivedUnknown, ['bytes', 'packets'], name, value)


        class Sent(Entity):
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
                super(MplsOam.Packet.Sent, self).__init__()

                self.yang_name = "sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Packet.Sent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Packet.Sent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Packet.Sent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Packet.Sent.TransmitGood)}
                self._child_list_classes = {}

                self.bfd_no_reply = MplsOam.Packet.Sent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.Sent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.Sent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.Sent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")
                self._segment_path = lambda: "sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class BfdNoReply(Entity):
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
                    super(MplsOam.Packet.Sent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.BfdNoReply, ['bytes', 'packets'], name, value)


            class TransmitBfdGood(Entity):
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
                    super(MplsOam.Packet.Sent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitBfdGood, ['bytes', 'packets'], name, value)


            class TransmitDrop(Entity):
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
                    super(MplsOam.Packet.Sent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitDrop, ['bytes', 'packets'], name, value)


            class TransmitGood(Entity):
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
                    super(MplsOam.Packet.Sent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.Sent.TransmitGood, ['bytes', 'packets'], name, value)


        class WorkingRepSent(Entity):
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
                super(MplsOam.Packet.WorkingRepSent, self).__init__()

                self.yang_name = "working-rep-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Packet.WorkingRepSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Packet.WorkingRepSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Packet.WorkingRepSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Packet.WorkingRepSent.TransmitGood)}
                self._child_list_classes = {}

                self.bfd_no_reply = MplsOam.Packet.WorkingRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.WorkingRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.WorkingRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.WorkingRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")
                self._segment_path = lambda: "working-rep-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class BfdNoReply(Entity):
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
                    super(MplsOam.Packet.WorkingRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.BfdNoReply, ['bytes', 'packets'], name, value)


            class TransmitBfdGood(Entity):
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
                    super(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


            class TransmitDrop(Entity):
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
                    super(MplsOam.Packet.WorkingRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitDrop, ['bytes', 'packets'], name, value)


            class TransmitGood(Entity):
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
                    super(MplsOam.Packet.WorkingRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-rep-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingRepSent.TransmitGood, ['bytes', 'packets'], name, value)


        class WorkingReqSent(Entity):
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
                super(MplsOam.Packet.WorkingReqSent, self).__init__()

                self.yang_name = "working-req-sent"
                self.yang_parent_name = "packet"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-no-reply" : ("bfd_no_reply", MplsOam.Packet.WorkingReqSent.BfdNoReply), "transmit-bfd-good" : ("transmit_bfd_good", MplsOam.Packet.WorkingReqSent.TransmitBfdGood), "transmit-drop" : ("transmit_drop", MplsOam.Packet.WorkingReqSent.TransmitDrop), "transmit-good" : ("transmit_good", MplsOam.Packet.WorkingReqSent.TransmitGood)}
                self._child_list_classes = {}

                self.bfd_no_reply = MplsOam.Packet.WorkingReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.WorkingReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.WorkingReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.WorkingReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")
                self._segment_path = lambda: "working-req-sent"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self._segment_path()


            class BfdNoReply(Entity):
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
                    super(MplsOam.Packet.WorkingReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "bfd-no-reply"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.BfdNoReply, ['bytes', 'packets'], name, value)


            class TransmitBfdGood(Entity):
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
                    super(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-bfd-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, ['bytes', 'packets'], name, value)


            class TransmitDrop(Entity):
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
                    super(MplsOam.Packet.WorkingReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-drop"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitDrop, ['bytes', 'packets'], name, value)


            class TransmitGood(Entity):
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
                    super(MplsOam.Packet.WorkingReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-req-sent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "transmit-good"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsOam.Packet.WorkingReqSent.TransmitGood, ['bytes', 'packets'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity

