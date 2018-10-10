""" Cisco_IOS_XR_dnx_driver_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-driver package operational data.

This module contains definitions
for the following management objects\:
  fia\: FIA driver operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AdminState(Enum):
    """
    AdminState (Enum Class)

    Admin state

    .. data:: admin_unset = -1

    	admin unset

    .. data:: admin_up = 0

    	admin up

    .. data:: admin_down = 1

    	admin down

    """

    admin_unset = Enum.YLeaf(-1, "admin-unset")

    admin_up = Enum.YLeaf(0, "admin-up")

    admin_down = Enum.YLeaf(1, "admin-down")


class Asic(Enum):
    """
    Asic (Enum Class)

    Asic

    .. data:: asic_unset = -1

    	asic unset

    .. data:: asic_unavail = 0

    	asic unavail

    .. data:: asic_fia = 1

    	asic fia

    .. data:: asic_s123 = 2

    	asic s123

    .. data:: asic_s13 = 3

    	asic s13

    .. data:: asic_s2 = 4

    	asic s2

    .. data:: asic_b2b = 5

    	asic b2b

    .. data:: asic_type_unknown = 6

    	asic type unknown

    """

    asic_unset = Enum.YLeaf(-1, "asic-unset")

    asic_unavail = Enum.YLeaf(0, "asic-unavail")

    asic_fia = Enum.YLeaf(1, "asic-fia")

    asic_s123 = Enum.YLeaf(2, "asic-s123")

    asic_s13 = Enum.YLeaf(3, "asic-s13")

    asic_s2 = Enum.YLeaf(4, "asic-s2")

    asic_b2b = Enum.YLeaf(5, "asic-b2b")

    asic_type_unknown = Enum.YLeaf(6, "asic-type-unknown")


class AsicAccessState(Enum):
    """
    AsicAccessState (Enum Class)

    Asic access state

    .. data:: asic_state_unset = -1

    	asic state unset

    .. data:: asic_state_none = 0

    	asic state none

    .. data:: asic_state_device_off_line = 1

    	asic state device off line

    .. data:: asic_state_device_created = 2

    	asic state device created

    .. data:: asic_state_device_online = 3

    	asic state device online

    .. data:: asic_state_warmboot = 4

    	asic state warmboot

    .. data:: asic_state_de_init_start = 5

    	asic state de init start

    .. data:: asic_state_intr_de_init = 6

    	asic state intr de init

    .. data:: asic_state_bcm_detach = 7

    	asic state bcm detach

    .. data:: asic_state_soc_de_init = 8

    	asic state soc de init

    .. data:: asic_state_de_init_done = 9

    	asic state de init done

    .. data:: asic_state_soc_init = 10

    	asic state soc init

    .. data:: asic_state_bcm_init = 11

    	asic state bcm init

    .. data:: asic_state_intr_init = 12

    	asic state intr init

    .. data:: asic_state_soc_init_start = 13

    	asic state soc init start

    .. data:: asic_state_bcm_init_start = 14

    	asic state bcm init start

    .. data:: asic_state_intr_init_start = 15

    	asic state intr init start

    .. data:: asic_state_hard_reset = 16

    	asic state hard reset

    .. data:: asic_state_normal = 17

    	asic state normal

    .. data:: asic_state_exception = 18

    	asic state exception

    .. data:: asic_state_hp_attached = 19

    	asic state hp attached

    .. data:: asic_state_quiesce = 20

    	asic state quiesce

    .. data:: asic_state_issu_started = 21

    	asic state issu started

    .. data:: asic_state_issu_started_nn = 22

    	asic state issu started nn

    .. data:: asic_state_issu_abort = 23

    	asic state issu abort

    .. data:: asic_state_max = 24

    	asic state max

    """

    asic_state_unset = Enum.YLeaf(-1, "asic-state-unset")

    asic_state_none = Enum.YLeaf(0, "asic-state-none")

    asic_state_device_off_line = Enum.YLeaf(1, "asic-state-device-off-line")

    asic_state_device_created = Enum.YLeaf(2, "asic-state-device-created")

    asic_state_device_online = Enum.YLeaf(3, "asic-state-device-online")

    asic_state_warmboot = Enum.YLeaf(4, "asic-state-warmboot")

    asic_state_de_init_start = Enum.YLeaf(5, "asic-state-de-init-start")

    asic_state_intr_de_init = Enum.YLeaf(6, "asic-state-intr-de-init")

    asic_state_bcm_detach = Enum.YLeaf(7, "asic-state-bcm-detach")

    asic_state_soc_de_init = Enum.YLeaf(8, "asic-state-soc-de-init")

    asic_state_de_init_done = Enum.YLeaf(9, "asic-state-de-init-done")

    asic_state_soc_init = Enum.YLeaf(10, "asic-state-soc-init")

    asic_state_bcm_init = Enum.YLeaf(11, "asic-state-bcm-init")

    asic_state_intr_init = Enum.YLeaf(12, "asic-state-intr-init")

    asic_state_soc_init_start = Enum.YLeaf(13, "asic-state-soc-init-start")

    asic_state_bcm_init_start = Enum.YLeaf(14, "asic-state-bcm-init-start")

    asic_state_intr_init_start = Enum.YLeaf(15, "asic-state-intr-init-start")

    asic_state_hard_reset = Enum.YLeaf(16, "asic-state-hard-reset")

    asic_state_normal = Enum.YLeaf(17, "asic-state-normal")

    asic_state_exception = Enum.YLeaf(18, "asic-state-exception")

    asic_state_hp_attached = Enum.YLeaf(19, "asic-state-hp-attached")

    asic_state_quiesce = Enum.YLeaf(20, "asic-state-quiesce")

    asic_state_issu_started = Enum.YLeaf(21, "asic-state-issu-started")

    asic_state_issu_started_nn = Enum.YLeaf(22, "asic-state-issu-started-nn")

    asic_state_issu_abort = Enum.YLeaf(23, "asic-state-issu-abort")

    asic_state_max = Enum.YLeaf(24, "asic-state-max")


class AsicInitMethod(Enum):
    """
    AsicInitMethod (Enum Class)

    Asic init method

    .. data:: asic_init_method_unset = -1

    	asic init method unset

    .. data:: asic_init_method_no_reset = 0

    	asic init method no reset

    .. data:: asic_init_method_pon_reset = 1

    	asic init method pon reset

    .. data:: asic_init_method_pon_reset_on_intr = 2

    	asic init method pon reset on intr

    .. data:: asic_init_method_hard_reset = 3

    	asic init method hard reset

    .. data:: asic_init_method_warmboot = 4

    	asic init method warmboot

    .. data:: asic_init_method_issu_wb = 5

    	asic init method issu wb

    .. data:: asic_init_method_pci_shutdown = 6

    	asic init method pci shutdown

    .. data:: asic_init_method_quiesce = 7

    	asic init method quiesce

    .. data:: asic_init_method_issu_started = 8

    	asic init method issu started

    .. data:: asic_init_method_issu_rollback = 9

    	asic init method issu rollback

    .. data:: asic_init_method_issu_abort = 10

    	asic init method issu abort

    .. data:: asic_init_method_slice_cleanup = 11

    	asic init method slice cleanup

    .. data:: asic_init_method_lc_remove = 12

    	asic init method lc remove

    .. data:: asic_init_method_node_down = 13

    	asic init method node down

    .. data:: asic_init_method_intr = 14

    	asic init method intr

    .. data:: asic_init_method_board_reload = 15

    	asic init method board reload

    .. data:: asic_init_method_max = 16

    	asic init method max

    """

    asic_init_method_unset = Enum.YLeaf(-1, "asic-init-method-unset")

    asic_init_method_no_reset = Enum.YLeaf(0, "asic-init-method-no-reset")

    asic_init_method_pon_reset = Enum.YLeaf(1, "asic-init-method-pon-reset")

    asic_init_method_pon_reset_on_intr = Enum.YLeaf(2, "asic-init-method-pon-reset-on-intr")

    asic_init_method_hard_reset = Enum.YLeaf(3, "asic-init-method-hard-reset")

    asic_init_method_warmboot = Enum.YLeaf(4, "asic-init-method-warmboot")

    asic_init_method_issu_wb = Enum.YLeaf(5, "asic-init-method-issu-wb")

    asic_init_method_pci_shutdown = Enum.YLeaf(6, "asic-init-method-pci-shutdown")

    asic_init_method_quiesce = Enum.YLeaf(7, "asic-init-method-quiesce")

    asic_init_method_issu_started = Enum.YLeaf(8, "asic-init-method-issu-started")

    asic_init_method_issu_rollback = Enum.YLeaf(9, "asic-init-method-issu-rollback")

    asic_init_method_issu_abort = Enum.YLeaf(10, "asic-init-method-issu-abort")

    asic_init_method_slice_cleanup = Enum.YLeaf(11, "asic-init-method-slice-cleanup")

    asic_init_method_lc_remove = Enum.YLeaf(12, "asic-init-method-lc-remove")

    asic_init_method_node_down = Enum.YLeaf(13, "asic-init-method-node-down")

    asic_init_method_intr = Enum.YLeaf(14, "asic-init-method-intr")

    asic_init_method_board_reload = Enum.YLeaf(15, "asic-init-method-board-reload")

    asic_init_method_max = Enum.YLeaf(16, "asic-init-method-max")


class AsicOperState(Enum):
    """
    AsicOperState (Enum Class)

    Asic oper state

    .. data:: asic_oper_unset = -1

    	asic oper unset

    .. data:: asic_oper_unknown = 0

    	asic oper unknown

    .. data:: asic_oper_up = 1

    	asic oper up

    .. data:: asic_oper_down = 2

    	asic oper down

    .. data:: asic_card_down = 3

    	asic card down

    """

    asic_oper_unset = Enum.YLeaf(-1, "asic-oper-unset")

    asic_oper_unknown = Enum.YLeaf(0, "asic-oper-unknown")

    asic_oper_up = Enum.YLeaf(1, "asic-oper-up")

    asic_oper_down = Enum.YLeaf(2, "asic-oper-down")

    asic_card_down = Enum.YLeaf(3, "asic-card-down")


class FcMode(Enum):
    """
    FcMode (Enum Class)

    Fc mode

    .. data:: fc_mode_unset = -1

    	fc mode unset

    .. data:: fc_mode_unavail = 0

    	fc mode unavail

    .. data:: fc_mode_inband = 1

    	fc mode inband

    .. data:: fc_mode_oob = 2

    	fc mode oob

    """

    fc_mode_unset = Enum.YLeaf(-1, "fc-mode-unset")

    fc_mode_unavail = Enum.YLeaf(0, "fc-mode-unavail")

    fc_mode_inband = Enum.YLeaf(1, "fc-mode-inband")

    fc_mode_oob = Enum.YLeaf(2, "fc-mode-oob")


class Link(Enum):
    """
    Link (Enum Class)

    Link

    .. data:: link_type_unset = -1

    	link type unset

    .. data:: link_type_unavail = 0

    	link type unavail

    .. data:: link_type_tx = 1

    	link type tx

    .. data:: link_type_rx = 2

    	link type rx

    """

    link_type_unset = Enum.YLeaf(-1, "link-type-unset")

    link_type_unavail = Enum.YLeaf(0, "link-type-unavail")

    link_type_tx = Enum.YLeaf(1, "link-type-tx")

    link_type_rx = Enum.YLeaf(2, "link-type-rx")


class LinkErrorState(Enum):
    """
    LinkErrorState (Enum Class)

    Link error state

    .. data:: link_error_unset = -1

    	link error unset

    .. data:: link_error_none = 0

    	link error none

    .. data:: link_error_shut = 1

    	link error shut

    .. data:: link_error_max = 2

    	link error max

    """

    link_error_unset = Enum.YLeaf(-1, "link-error-unset")

    link_error_none = Enum.YLeaf(0, "link-error-none")

    link_error_shut = Enum.YLeaf(1, "link-error-shut")

    link_error_max = Enum.YLeaf(2, "link-error-max")


class LinkStage(Enum):
    """
    LinkStage (Enum Class)

    Link stage

    .. data:: link_stage_unset = -1

    	link stage unset

    .. data:: link_stage_unused = 0

    	link stage unused

    .. data:: link_stage_fia = 1

    	link stage fia

    .. data:: link_stage_s1 = 2

    	link stage s1

    .. data:: link_stage_s2 = 3

    	link stage s2

    .. data:: link_stage_s3 = 4

    	link stage s3

    .. data:: link_stage_unknown = 5

    	link stage unknown

    """

    link_stage_unset = Enum.YLeaf(-1, "link-stage-unset")

    link_stage_unused = Enum.YLeaf(0, "link-stage-unused")

    link_stage_fia = Enum.YLeaf(1, "link-stage-fia")

    link_stage_s1 = Enum.YLeaf(2, "link-stage-s1")

    link_stage_s2 = Enum.YLeaf(3, "link-stage-s2")

    link_stage_s3 = Enum.YLeaf(4, "link-stage-s3")

    link_stage_unknown = Enum.YLeaf(5, "link-stage-unknown")


class OperState(Enum):
    """
    OperState (Enum Class)

    Oper state

    .. data:: oper_unset = -1

    	oper unset

    .. data:: oper_unknown = 0

    	oper unknown

    .. data:: oper_up = 1

    	oper up

    .. data:: oper_down = 2

    	oper down

    .. data:: card_down = 3

    	card down

    """

    oper_unset = Enum.YLeaf(-1, "oper-unset")

    oper_unknown = Enum.YLeaf(0, "oper-unknown")

    oper_up = Enum.YLeaf(1, "oper-up")

    oper_down = Enum.YLeaf(2, "oper-down")

    card_down = Enum.YLeaf(3, "card-down")


class Rack(Enum):
    """
    Rack (Enum Class)

    Rack

    .. data:: rack_type_unset = -1

    	rack type unset

    .. data:: rack_type_lcc = 0

    	rack type lcc

    .. data:: rack_type_fcc = 1

    	rack type fcc

    """

    rack_type_unset = Enum.YLeaf(-1, "rack-type-unset")

    rack_type_lcc = Enum.YLeaf(0, "rack-type-lcc")

    rack_type_fcc = Enum.YLeaf(1, "rack-type-fcc")


class SliceState(Enum):
    """
    SliceState (Enum Class)

    Slice state

    .. data:: slice_oper_unset = -1

    	slice oper unset

    .. data:: slice_oper_down = 0

    	slice oper down

    .. data:: slice_oper_up = 1

    	slice oper up

    .. data:: slice_oper_na = 2

    	slice oper na

    """

    slice_oper_unset = Enum.YLeaf(-1, "slice-oper-unset")

    slice_oper_down = Enum.YLeaf(0, "slice-oper-down")

    slice_oper_up = Enum.YLeaf(1, "slice-oper-up")

    slice_oper_na = Enum.YLeaf(2, "slice-oper-na")



class Fia(Entity):
    """
    FIA driver operational data
    
    .. attribute:: nodes
    
    	FIA driver operational data for available nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes>`
    
    

    """

    _prefix = 'dnx-driver-oper'
    _revision = '2017-08-29'

    def __init__(self):
        super(Fia, self).__init__()
        self._top_entity = None

        self.yang_name = "fia"
        self.yang_parent_name = "Cisco-IOS-XR-dnx-driver-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Fia.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Fia.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-dnx-driver-oper:fia"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fia, [], name, value)


    class Nodes(Entity):
        """
        FIA driver operational data for available nodes
        
        .. attribute:: node
        
        	FIA operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-driver-oper'
        _revision = '2017-08-29'

        def __init__(self):
            super(Fia.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fia"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Fia.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-oper:fia/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fia.Nodes, [], name, value)


        class Node(Entity):
            """
            FIA operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: rx_link_information
            
            	FIA link rx information
            	**type**\:  :py:class:`RxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation>`
            
            .. attribute:: driver_information
            
            	FIA driver information
            	**type**\:  :py:class:`DriverInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation>`
            
            .. attribute:: clear_statistics
            
            	Clear statistics information
            	**type**\:  :py:class:`ClearStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics>`
            
            .. attribute:: tx_link_information
            
            	FIA link TX information
            	**type**\:  :py:class:`TxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation>`
            
            .. attribute:: diag_shell
            
            	FIA diag shell information
            	**type**\:  :py:class:`DiagShell <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell>`
            
            .. attribute:: oir_history
            
            	FIA operational data of oir history
            	**type**\:  :py:class:`OirHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory>`
            
            .. attribute:: asic_statistics
            
            	FIA asic statistics information
            	**type**\:  :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics>`
            
            

            """

            _prefix = 'dnx-driver-oper'
            _revision = '2017-08-29'

            def __init__(self):
                super(Fia.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("rx-link-information", ("rx_link_information", Fia.Nodes.Node.RxLinkInformation)), ("driver-information", ("driver_information", Fia.Nodes.Node.DriverInformation)), ("clear-statistics", ("clear_statistics", Fia.Nodes.Node.ClearStatistics)), ("tx-link-information", ("tx_link_information", Fia.Nodes.Node.TxLinkInformation)), ("diag-shell", ("diag_shell", Fia.Nodes.Node.DiagShell)), ("oir-history", ("oir_history", Fia.Nodes.Node.OirHistory)), ("asic-statistics", ("asic_statistics", Fia.Nodes.Node.AsicStatistics))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.rx_link_information = Fia.Nodes.Node.RxLinkInformation()
                self.rx_link_information.parent = self
                self._children_name_map["rx_link_information"] = "rx-link-information"

                self.driver_information = Fia.Nodes.Node.DriverInformation()
                self.driver_information.parent = self
                self._children_name_map["driver_information"] = "driver-information"

                self.clear_statistics = Fia.Nodes.Node.ClearStatistics()
                self.clear_statistics.parent = self
                self._children_name_map["clear_statistics"] = "clear-statistics"

                self.tx_link_information = Fia.Nodes.Node.TxLinkInformation()
                self.tx_link_information.parent = self
                self._children_name_map["tx_link_information"] = "tx-link-information"

                self.diag_shell = Fia.Nodes.Node.DiagShell()
                self.diag_shell.parent = self
                self._children_name_map["diag_shell"] = "diag-shell"

                self.oir_history = Fia.Nodes.Node.OirHistory()
                self.oir_history.parent = self
                self._children_name_map["oir_history"] = "oir-history"

                self.asic_statistics = Fia.Nodes.Node.AsicStatistics()
                self.asic_statistics.parent = self
                self._children_name_map["asic_statistics"] = "asic-statistics"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-oper:fia/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fia.Nodes.Node, ['node_name'], name, value)


            class RxLinkInformation(Entity):
                """
                FIA link rx information
                
                .. attribute:: link_options
                
                	Option table for link rx information
                	**type**\:  :py:class:`LinkOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.RxLinkInformation, self).__init__()

                    self.yang_name = "rx-link-information"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("link-options", ("link_options", Fia.Nodes.Node.RxLinkInformation.LinkOptions))])
                    self._leafs = OrderedDict()

                    self.link_options = Fia.Nodes.Node.RxLinkInformation.LinkOptions()
                    self.link_options.parent = self
                    self._children_name_map["link_options"] = "link-options"
                    self._segment_path = lambda: "rx-link-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation, [], name, value)


                class LinkOptions(Entity):
                    """
                    Option table for link rx information
                    
                    .. attribute:: link_option
                    
                    	Option \: topo , flag , stats
                    	**type**\: list of  		 :py:class:`LinkOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions, self).__init__()

                        self.yang_name = "link-options"
                        self.yang_parent_name = "rx-link-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("link-option", ("link_option", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption))])
                        self._leafs = OrderedDict()

                        self.link_option = YList(self)
                        self._segment_path = lambda: "link-options"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions, [], name, value)


                    class LinkOption(Entity):
                        """
                        Option \: topo , flag , stats
                        
                        .. attribute:: option  (key)
                        
                        	Link option
                        	**type**\: str
                        
                        	**pattern:** (flap)\|(topo)
                        
                        .. attribute:: rx_asic_instances
                        
                        	Instance table for rx information
                        	**type**\:  :py:class:`RxAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption, self).__init__()

                            self.yang_name = "link-option"
                            self.yang_parent_name = "link-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['option']
                            self._child_classes = OrderedDict([("rx-asic-instances", ("rx_asic_instances", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances))])
                            self._leafs = OrderedDict([
                                ('option', (YLeaf(YType.str, 'option'), ['str'])),
                            ])
                            self.option = None

                            self.rx_asic_instances = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances()
                            self.rx_asic_instances.parent = self
                            self._children_name_map["rx_asic_instances"] = "rx-asic-instances"
                            self._segment_path = lambda: "link-option" + "[option='" + str(self.option) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption, ['option'], name, value)


                        class RxAsicInstances(Entity):
                            """
                            Instance table for rx information
                            
                            .. attribute:: rx_asic_instance
                            
                            	Instance number for rx link information
                            	**type**\: list of  		 :py:class:`RxAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances, self).__init__()

                                self.yang_name = "rx-asic-instances"
                                self.yang_parent_name = "link-option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("rx-asic-instance", ("rx_asic_instance", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance))])
                                self._leafs = OrderedDict()

                                self.rx_asic_instance = YList(self)
                                self._segment_path = lambda: "rx-asic-instances"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances, [], name, value)


                            class RxAsicInstance(Entity):
                                """
                                Instance number for rx link information
                                
                                .. attribute:: instance  (key)
                                
                                	Receive instance
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rx_links
                                
                                	Link table class for rx information
                                	**type**\:  :py:class:`RxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance, self).__init__()

                                    self.yang_name = "rx-asic-instance"
                                    self.yang_parent_name = "rx-asic-instances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['instance']
                                    self._child_classes = OrderedDict([("rx-links", ("rx_links", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks))])
                                    self._leafs = OrderedDict([
                                        ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                                    ])
                                    self.instance = None

                                    self.rx_links = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks()
                                    self.rx_links.parent = self
                                    self._children_name_map["rx_links"] = "rx-links"
                                    self._segment_path = lambda: "rx-asic-instance" + "[instance='" + str(self.instance) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance, ['instance'], name, value)


                                class RxLinks(Entity):
                                    """
                                    Link table class for rx information
                                    
                                    .. attribute:: rx_link
                                    
                                    	Link number for rx link information
                                    	**type**\: list of  		 :py:class:`RxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks, self).__init__()

                                        self.yang_name = "rx-links"
                                        self.yang_parent_name = "rx-asic-instance"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rx-link", ("rx_link", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink))])
                                        self._leafs = OrderedDict()

                                        self.rx_link = YList(self)
                                        self._segment_path = lambda: "rx-links"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks, [], name, value)


                                    class RxLink(Entity):
                                        """
                                        Link number for rx link information
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: status_option
                                        
                                        	RX link status option
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: rx_link
                                        
                                        	Single link information
                                        	**type**\: list of  		 :py:class:`RxLink_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink, self).__init__()

                                            self.yang_name = "rx-link"
                                            self.yang_parent_name = "rx-links"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("rx-link", ("rx_link", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_))])
                                            self._leafs = OrderedDict([
                                                ('start_number', (YLeaf(YType.uint32, 'start-number'), ['int'])),
                                                ('end_number', (YLeaf(YType.uint32, 'end-number'), ['int'])),
                                                ('status_option', (YLeaf(YType.str, 'status-option'), ['str'])),
                                            ])
                                            self.start_number = None
                                            self.end_number = None
                                            self.status_option = None

                                            self.rx_link = YList(self)
                                            self._segment_path = lambda: "rx-link"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink, ['start_number', 'end_number', 'status_option'], name, value)


                                        class RxLink_(Entity):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  (key)
                                            
                                            	Single link
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:  :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:  :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink>`
                                            
                                            .. attribute:: far_end_link_in_hw
                                            
                                            	far end link in hw
                                            	**type**\:  :py:class:`FarEndLinkInHw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw>`
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	Stage
                                            	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            .. attribute:: flags
                                            
                                            	flags
                                            	**type**\: str
                                            
                                            .. attribute:: flap_cnt
                                            
                                            	flap cnt
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: correctable_errors
                                            
                                            	correctable errors
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: uncorrectable_errors
                                            
                                            	uncorrectable errors
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_, self).__init__()

                                                self.yang_name = "rx-link"
                                                self.yang_parent_name = "rx-link"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['link']
                                                self._child_classes = OrderedDict([("this-link", ("this_link", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink)), ("far-end-link", ("far_end_link", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink)), ("far-end-link-in-hw", ("far_end_link_in_hw", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw)), ("history", ("history", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History))])
                                                self._leafs = OrderedDict([
                                                    ('link', (YLeaf(YType.uint32, 'link'), ['int'])),
                                                    ('speed', (YLeaf(YType.uint32, 'speed'), ['int'])),
                                                    ('stage', (YLeaf(YType.enumeration, 'stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                    ('is_link_valid', (YLeaf(YType.boolean, 'is-link-valid'), ['bool'])),
                                                    ('is_conf_pending', (YLeaf(YType.boolean, 'is-conf-pending'), ['bool'])),
                                                    ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                                                    ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperState', '')])),
                                                    ('error_state', (YLeaf(YType.enumeration, 'error-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorState', '')])),
                                                    ('flags', (YLeaf(YType.str, 'flags'), ['str'])),
                                                    ('flap_cnt', (YLeaf(YType.uint32, 'flap-cnt'), ['int'])),
                                                    ('num_admin_shuts', (YLeaf(YType.uint32, 'num-admin-shuts'), ['int'])),
                                                    ('correctable_errors', (YLeaf(YType.uint64, 'correctable-errors'), ['int'])),
                                                    ('uncorrectable_errors', (YLeaf(YType.uint64, 'uncorrectable-errors'), ['int'])),
                                                ])
                                                self.link = None
                                                self.speed = None
                                                self.stage = None
                                                self.is_link_valid = None
                                                self.is_conf_pending = None
                                                self.admin_state = None
                                                self.oper_state = None
                                                self.error_state = None
                                                self.flags = None
                                                self.flap_cnt = None
                                                self.num_admin_shuts = None
                                                self.correctable_errors = None
                                                self.uncorrectable_errors = None

                                                self.this_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink()
                                                self.this_link.parent = self
                                                self._children_name_map["this_link"] = "this-link"

                                                self.far_end_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink()
                                                self.far_end_link.parent = self
                                                self._children_name_map["far_end_link"] = "far-end-link"

                                                self.far_end_link_in_hw = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw()
                                                self.far_end_link_in_hw.parent = self
                                                self._children_name_map["far_end_link_in_hw"] = "far-end-link-in-hw"

                                                self.history = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History()
                                                self.history.parent = self
                                                self._children_name_map["history"] = "history"
                                                self._segment_path = lambda: "rx-link" + "[link='" + str(self.link) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_, ['link', u'speed', u'stage', u'is_link_valid', u'is_conf_pending', u'admin_state', u'oper_state', u'error_state', u'flags', u'flap_cnt', u'num_admin_shuts', u'correctable_errors', u'uncorrectable_errors'], name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink, self).__init__()

                                                    self.yang_name = "this-link"
                                                    self.yang_parent_name = "rx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Link', '')])),
                                                        ('link_stage', (YLeaf(YType.enumeration, 'link-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                        ('link_num', (YLeaf(YType.uint32, 'link-num'), ['int'])),
                                                        ('phy_link_num', (YLeaf(YType.uint32, 'phy-link-num'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._segment_path = lambda: "this-link"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink, [u'link_type', u'link_stage', u'link_num', u'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "this-link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                            ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                            ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                            ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                            ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                        ])
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None
                                                        self._segment_path = lambda: "asic-id"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink, self).__init__()

                                                    self.yang_name = "far-end-link"
                                                    self.yang_parent_name = "rx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Link', '')])),
                                                        ('link_stage', (YLeaf(YType.enumeration, 'link-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                        ('link_num', (YLeaf(YType.uint32, 'link-num'), ['int'])),
                                                        ('phy_link_num', (YLeaf(YType.uint32, 'phy-link-num'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._segment_path = lambda: "far-end-link"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink, [u'link_type', u'link_stage', u'link_num', u'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                            ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                            ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                            ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                            ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                        ])
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None
                                                        self._segment_path = lambda: "asic-id"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                            class FarEndLinkInHw(Entity):
                                                """
                                                far end link in hw
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw, self).__init__()

                                                    self.yang_name = "far-end-link-in-hw"
                                                    self.yang_parent_name = "rx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Link', '')])),
                                                        ('link_stage', (YLeaf(YType.enumeration, 'link-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                        ('link_num', (YLeaf(YType.uint32, 'link-num'), ['int'])),
                                                        ('phy_link_num', (YLeaf(YType.uint32, 'phy-link-num'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._segment_path = lambda: "far-end-link-in-hw"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw, [u'link_type', u'link_stage', u'link_num', u'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link-in-hw"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                            ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                            ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                            ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                            ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                        ])
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None
                                                        self._segment_path = lambda: "asic-id"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of  		 :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist>`
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History, self).__init__()

                                                    self.yang_name = "history"
                                                    self.yang_parent_name = "rx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("hist", ("hist", Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist))])
                                                    self._leafs = OrderedDict([
                                                        ('histnum', (YLeaf(YType.uint8, 'histnum'), ['int'])),
                                                        ('start_index', (YLeaf(YType.uint8, 'start-index'), ['int'])),
                                                    ])
                                                    self.histnum = None
                                                    self.start_index = None

                                                    self.hist = YList(self)
                                                    self._segment_path = lambda: "history"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History, [u'histnum', u'start_index'], name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist, self).__init__()

                                                        self.yang_name = "hist"
                                                        self.yang_parent_name = "history"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                                                            ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperState', '')])),
                                                            ('error_state', (YLeaf(YType.enumeration, 'error-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorState', '')])),
                                                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                                                            ('reasons', (YLeaf(YType.str, 'reasons'), ['str'])),
                                                        ])
                                                        self.admin_state = None
                                                        self.oper_state = None
                                                        self.error_state = None
                                                        self.timestamp = None
                                                        self.reasons = None
                                                        self._segment_path = lambda: "hist"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist, [u'admin_state', u'oper_state', u'error_state', u'timestamp', u'reasons'], name, value)


            class DriverInformation(Entity):
                """
                FIA driver information
                
                .. attribute:: drv_version
                
                	drv version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: coeff_major_rev
                
                	coeff major rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: coeff_minor_rev
                
                	coeff minor rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: functional_role
                
                	functional role
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: issu_role
                
                	issu role
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: node_id
                
                	node id
                	**type**\: str
                
                .. attribute:: rack_type
                
                	rack type
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rack_num
                
                	rack num
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_driver_ready
                
                	is driver ready
                	**type**\: bool
                
                .. attribute:: card_avail_mask
                
                	card avail mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: asic_avail_mask
                
                	asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: exp_asic_avail_mask
                
                	exp asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ucmc_ratio
                
                	ucmc ratio
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                
                	asic oper notify to fsdb pending bmap
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: is_full_fgid_download_req
                
                	is full fgid download req
                	**type**\: bool
                
                .. attribute:: is_fgid_download_in_progress
                
                	is fgid download in progress
                	**type**\: bool
                
                .. attribute:: is_fgid_download_completed
                
                	is fgid download completed
                	**type**\: bool
                
                .. attribute:: fsdb_conn_active
                
                	fsdb conn active
                	**type**\: bool
                
                .. attribute:: fgid_conn_active
                
                	fgid conn active
                	**type**\: bool
                
                .. attribute:: issu_mgr_conn_active
                
                	issu mgr conn active
                	**type**\: bool
                
                .. attribute:: fsdb_reg_active
                
                	fsdb reg active
                	**type**\: bool
                
                .. attribute:: fgid_reg_active
                
                	fgid reg active
                	**type**\: bool
                
                .. attribute:: issu_mgr_reg_active
                
                	issu mgr reg active
                	**type**\: bool
                
                .. attribute:: num_pm_conn_reqs
                
                	num pm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fsdb_conn_reqs
                
                	num fsdb conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fgid_conn_reqs
                
                	num fgid conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fstats_conn_reqs
                
                	num fstats conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_cm_conn_reqs
                
                	num cm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_issu_mgr_conn_reqs
                
                	num issu mgr conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_peer_fia_conn_reqs
                
                	num peer fia conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_gaspp_registered
                
                	is gaspp registered
                	**type**\: bool
                
                .. attribute:: is_cih_registered
                
                	is cih registered
                	**type**\: bool
                
                .. attribute:: drvr_initial_startup_timestamp
                
                	drvr initial startup timestamp
                	**type**\: str
                
                .. attribute:: drvr_current_startup_timestamp
                
                	drvr current startup timestamp
                	**type**\: str
                
                .. attribute:: num_intf_ports
                
                	num intf ports
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: uc_weight
                
                	uc weight
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: respawn_count
                
                	respawn count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: total_asics
                
                	total asics
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: issu_ready_ntfy_pending
                
                	issu ready ntfy pending
                	**type**\: bool
                
                .. attribute:: issu_abort_sent
                
                	issu abort sent
                	**type**\: bool
                
                .. attribute:: issu_abort_rcvd
                
                	issu abort rcvd
                	**type**\: bool
                
                .. attribute:: fabric_mode
                
                	fabric mode
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: fc_mode
                
                	FC Mode
                	**type**\:  :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                
                .. attribute:: board_rev_id
                
                	board rev id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_wb_insync
                
                	all wb insync
                	**type**\: bool
                
                .. attribute:: all_wb_insync_since
                
                	all wb insync since
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_startup_wb_insync
                
                	all startup wb insync
                	**type**\: bool
                
                .. attribute:: plane_a_bitmap
                
                	planeA bitmap
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: plane_b_bitmap
                
                	planeB bitmap
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_info
                
                	device info
                	**type**\: list of  		 :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo>`
                
                .. attribute:: card_info
                
                	card info
                	**type**\: list of  		 :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.DriverInformation, self).__init__()

                    self.yang_name = "driver-information"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("device-info", ("device_info", Fia.Nodes.Node.DriverInformation.DeviceInfo)), ("card-info", ("card_info", Fia.Nodes.Node.DriverInformation.CardInfo))])
                    self._leafs = OrderedDict([
                        ('drv_version', (YLeaf(YType.uint32, 'drv-version'), ['int'])),
                        ('coeff_major_rev', (YLeaf(YType.uint32, 'coeff-major-rev'), ['int'])),
                        ('coeff_minor_rev', (YLeaf(YType.uint32, 'coeff-minor-rev'), ['int'])),
                        ('functional_role', (YLeaf(YType.uint8, 'functional-role'), ['int'])),
                        ('issu_role', (YLeaf(YType.uint8, 'issu-role'), ['int'])),
                        ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                        ('rack_type', (YLeaf(YType.int32, 'rack-type'), ['int'])),
                        ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                        ('is_driver_ready', (YLeaf(YType.boolean, 'is-driver-ready'), ['bool'])),
                        ('card_avail_mask', (YLeaf(YType.uint32, 'card-avail-mask'), ['int'])),
                        ('asic_avail_mask', (YLeaf(YType.uint64, 'asic-avail-mask'), ['int'])),
                        ('exp_asic_avail_mask', (YLeaf(YType.uint64, 'exp-asic-avail-mask'), ['int'])),
                        ('ucmc_ratio', (YLeaf(YType.uint32, 'ucmc-ratio'), ['int'])),
                        ('asic_oper_notify_to_fsdb_pending_bmap', (YLeaf(YType.uint64, 'asic-oper-notify-to-fsdb-pending-bmap'), ['int'])),
                        ('is_full_fgid_download_req', (YLeaf(YType.boolean, 'is-full-fgid-download-req'), ['bool'])),
                        ('is_fgid_download_in_progress', (YLeaf(YType.boolean, 'is-fgid-download-in-progress'), ['bool'])),
                        ('is_fgid_download_completed', (YLeaf(YType.boolean, 'is-fgid-download-completed'), ['bool'])),
                        ('fsdb_conn_active', (YLeaf(YType.boolean, 'fsdb-conn-active'), ['bool'])),
                        ('fgid_conn_active', (YLeaf(YType.boolean, 'fgid-conn-active'), ['bool'])),
                        ('issu_mgr_conn_active', (YLeaf(YType.boolean, 'issu-mgr-conn-active'), ['bool'])),
                        ('fsdb_reg_active', (YLeaf(YType.boolean, 'fsdb-reg-active'), ['bool'])),
                        ('fgid_reg_active', (YLeaf(YType.boolean, 'fgid-reg-active'), ['bool'])),
                        ('issu_mgr_reg_active', (YLeaf(YType.boolean, 'issu-mgr-reg-active'), ['bool'])),
                        ('num_pm_conn_reqs', (YLeaf(YType.uint8, 'num-pm-conn-reqs'), ['int'])),
                        ('num_fsdb_conn_reqs', (YLeaf(YType.uint8, 'num-fsdb-conn-reqs'), ['int'])),
                        ('num_fgid_conn_reqs', (YLeaf(YType.uint8, 'num-fgid-conn-reqs'), ['int'])),
                        ('num_fstats_conn_reqs', (YLeaf(YType.uint8, 'num-fstats-conn-reqs'), ['int'])),
                        ('num_cm_conn_reqs', (YLeaf(YType.uint8, 'num-cm-conn-reqs'), ['int'])),
                        ('num_issu_mgr_conn_reqs', (YLeaf(YType.uint8, 'num-issu-mgr-conn-reqs'), ['int'])),
                        ('num_peer_fia_conn_reqs', (YLeaf(YType.uint8, 'num-peer-fia-conn-reqs'), ['int'])),
                        ('is_gaspp_registered', (YLeaf(YType.boolean, 'is-gaspp-registered'), ['bool'])),
                        ('is_cih_registered', (YLeaf(YType.boolean, 'is-cih-registered'), ['bool'])),
                        ('drvr_initial_startup_timestamp', (YLeaf(YType.str, 'drvr-initial-startup-timestamp'), ['str'])),
                        ('drvr_current_startup_timestamp', (YLeaf(YType.str, 'drvr-current-startup-timestamp'), ['str'])),
                        ('num_intf_ports', (YLeaf(YType.uint32, 'num-intf-ports'), ['int'])),
                        ('uc_weight', (YLeaf(YType.uint8, 'uc-weight'), ['int'])),
                        ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                        ('total_asics', (YLeaf(YType.uint8, 'total-asics'), ['int'])),
                        ('issu_ready_ntfy_pending', (YLeaf(YType.boolean, 'issu-ready-ntfy-pending'), ['bool'])),
                        ('issu_abort_sent', (YLeaf(YType.boolean, 'issu-abort-sent'), ['bool'])),
                        ('issu_abort_rcvd', (YLeaf(YType.boolean, 'issu-abort-rcvd'), ['bool'])),
                        ('fabric_mode', (YLeaf(YType.uint8, 'fabric-mode'), ['int'])),
                        ('fc_mode', (YLeaf(YType.enumeration, 'fc-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'FcMode', '')])),
                        ('board_rev_id', (YLeaf(YType.uint32, 'board-rev-id'), ['int'])),
                        ('all_wb_insync', (YLeaf(YType.boolean, 'all-wb-insync'), ['bool'])),
                        ('all_wb_insync_since', (YLeaf(YType.uint32, 'all-wb-insync-since'), ['int'])),
                        ('all_startup_wb_insync', (YLeaf(YType.boolean, 'all-startup-wb-insync'), ['bool'])),
                        ('plane_a_bitmap', (YLeaf(YType.uint32, 'plane-a-bitmap'), ['int'])),
                        ('plane_b_bitmap', (YLeaf(YType.uint32, 'plane-b-bitmap'), ['int'])),
                    ])
                    self.drv_version = None
                    self.coeff_major_rev = None
                    self.coeff_minor_rev = None
                    self.functional_role = None
                    self.issu_role = None
                    self.node_id = None
                    self.rack_type = None
                    self.rack_num = None
                    self.is_driver_ready = None
                    self.card_avail_mask = None
                    self.asic_avail_mask = None
                    self.exp_asic_avail_mask = None
                    self.ucmc_ratio = None
                    self.asic_oper_notify_to_fsdb_pending_bmap = None
                    self.is_full_fgid_download_req = None
                    self.is_fgid_download_in_progress = None
                    self.is_fgid_download_completed = None
                    self.fsdb_conn_active = None
                    self.fgid_conn_active = None
                    self.issu_mgr_conn_active = None
                    self.fsdb_reg_active = None
                    self.fgid_reg_active = None
                    self.issu_mgr_reg_active = None
                    self.num_pm_conn_reqs = None
                    self.num_fsdb_conn_reqs = None
                    self.num_fgid_conn_reqs = None
                    self.num_fstats_conn_reqs = None
                    self.num_cm_conn_reqs = None
                    self.num_issu_mgr_conn_reqs = None
                    self.num_peer_fia_conn_reqs = None
                    self.is_gaspp_registered = None
                    self.is_cih_registered = None
                    self.drvr_initial_startup_timestamp = None
                    self.drvr_current_startup_timestamp = None
                    self.num_intf_ports = None
                    self.uc_weight = None
                    self.respawn_count = None
                    self.total_asics = None
                    self.issu_ready_ntfy_pending = None
                    self.issu_abort_sent = None
                    self.issu_abort_rcvd = None
                    self.fabric_mode = None
                    self.fc_mode = None
                    self.board_rev_id = None
                    self.all_wb_insync = None
                    self.all_wb_insync_since = None
                    self.all_startup_wb_insync = None
                    self.plane_a_bitmap = None
                    self.plane_b_bitmap = None

                    self.device_info = YList(self)
                    self.card_info = YList(self)
                    self._segment_path = lambda: "driver-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.DriverInformation, [u'drv_version', u'coeff_major_rev', u'coeff_minor_rev', u'functional_role', u'issu_role', u'node_id', u'rack_type', u'rack_num', u'is_driver_ready', u'card_avail_mask', u'asic_avail_mask', u'exp_asic_avail_mask', u'ucmc_ratio', u'asic_oper_notify_to_fsdb_pending_bmap', u'is_full_fgid_download_req', u'is_fgid_download_in_progress', u'is_fgid_download_completed', u'fsdb_conn_active', u'fgid_conn_active', u'issu_mgr_conn_active', u'fsdb_reg_active', u'fgid_reg_active', u'issu_mgr_reg_active', u'num_pm_conn_reqs', u'num_fsdb_conn_reqs', u'num_fgid_conn_reqs', u'num_fstats_conn_reqs', u'num_cm_conn_reqs', u'num_issu_mgr_conn_reqs', u'num_peer_fia_conn_reqs', u'is_gaspp_registered', u'is_cih_registered', u'drvr_initial_startup_timestamp', u'drvr_current_startup_timestamp', u'num_intf_ports', u'uc_weight', u'respawn_count', u'total_asics', u'issu_ready_ntfy_pending', u'issu_abort_sent', u'issu_abort_rcvd', u'fabric_mode', u'fc_mode', u'board_rev_id', u'all_wb_insync', u'all_wb_insync_since', u'all_startup_wb_insync', u'plane_a_bitmap', u'plane_b_bitmap'], name, value)


                class DeviceInfo(Entity):
                    """
                    device info
                    
                    .. attribute:: asic_id
                    
                    	asic id
                    	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId>`
                    
                    .. attribute:: is_valid
                    
                    	is valid
                    	**type**\: bool
                    
                    .. attribute:: fapid
                    
                    	fapid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hotplug_event
                    
                    	hotplug event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slice_state
                    
                    	Slice State
                    	**type**\:  :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                    
                    .. attribute:: admin_state
                    
                    	Admin State
                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                    
                    .. attribute:: oper_state
                    
                    	Oper State
                    	**type**\:  :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                    
                    .. attribute:: asic_state
                    
                    	Asic State
                    	**type**\:  :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                    
                    .. attribute:: last_init_cause
                    
                    	last init cause
                    	**type**\:  :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                    
                    .. attribute:: num_pon_resets
                    
                    	num pon resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_hard_resets
                    
                    	num hard resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_switch_state
                    
                    	local switch state
                    	**type**\: bool
                    
                    .. attribute:: startup_wb_mtime_str
                    
                    	startup wb mtime str
                    	**type**\: str
                    
                    .. attribute:: startup_wb_outof_sync
                    
                    	startup wb outof sync
                    	**type**\: bool
                    
                    .. attribute:: local_wb_sync_end_str
                    
                    	local wb sync end str
                    	**type**\: str
                    
                    .. attribute:: remote_wb_sync_end_str
                    
                    	remote wb sync end str
                    	**type**\: str
                    
                    .. attribute:: local_wb_sync_pending
                    
                    	local wb sync pending
                    	**type**\: bool
                    
                    .. attribute:: sdk_delay_msec
                    
                    	sdk delay msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.DriverInformation.DeviceInfo, self).__init__()

                        self.yang_name = "device-info"
                        self.yang_parent_name = "driver-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId))])
                        self._leafs = OrderedDict([
                            ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                            ('fapid', (YLeaf(YType.uint32, 'fapid'), ['int'])),
                            ('hotplug_event', (YLeaf(YType.uint32, 'hotplug-event'), ['int'])),
                            ('slice_state', (YLeaf(YType.enumeration, 'slice-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'SliceState', '')])),
                            ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                            ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicOperState', '')])),
                            ('asic_state', (YLeaf(YType.enumeration, 'asic-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicAccessState', '')])),
                            ('last_init_cause', (YLeaf(YType.enumeration, 'last-init-cause'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicInitMethod', '')])),
                            ('num_pon_resets', (YLeaf(YType.uint32, 'num-pon-resets'), ['int'])),
                            ('num_hard_resets', (YLeaf(YType.uint32, 'num-hard-resets'), ['int'])),
                            ('local_switch_state', (YLeaf(YType.boolean, 'local-switch-state'), ['bool'])),
                            ('startup_wb_mtime_str', (YLeaf(YType.str, 'startup-wb-mtime-str'), ['str'])),
                            ('startup_wb_outof_sync', (YLeaf(YType.boolean, 'startup-wb-outof-sync'), ['bool'])),
                            ('local_wb_sync_end_str', (YLeaf(YType.str, 'local-wb-sync-end-str'), ['str'])),
                            ('remote_wb_sync_end_str', (YLeaf(YType.str, 'remote-wb-sync-end-str'), ['str'])),
                            ('local_wb_sync_pending', (YLeaf(YType.boolean, 'local-wb-sync-pending'), ['bool'])),
                            ('sdk_delay_msec', (YLeaf(YType.uint32, 'sdk-delay-msec'), ['int'])),
                        ])
                        self.is_valid = None
                        self.fapid = None
                        self.hotplug_event = None
                        self.slice_state = None
                        self.admin_state = None
                        self.oper_state = None
                        self.asic_state = None
                        self.last_init_cause = None
                        self.num_pon_resets = None
                        self.num_hard_resets = None
                        self.local_switch_state = None
                        self.startup_wb_mtime_str = None
                        self.startup_wb_outof_sync = None
                        self.local_wb_sync_end_str = None
                        self.remote_wb_sync_end_str = None
                        self.local_wb_sync_pending = None
                        self.sdk_delay_msec = None

                        self.asic_id = Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId()
                        self.asic_id.parent = self
                        self._children_name_map["asic_id"] = "asic-id"
                        self._segment_path = lambda: "device-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.DriverInformation.DeviceInfo, [u'is_valid', u'fapid', u'hotplug_event', u'slice_state', u'admin_state', u'oper_state', u'asic_state', u'last_init_cause', u'num_pon_resets', u'num_hard_resets', u'local_switch_state', u'startup_wb_mtime_str', u'startup_wb_outof_sync', u'local_wb_sync_end_str', u'remote_wb_sync_end_str', u'local_wb_sync_pending', u'sdk_delay_msec'], name, value)


                    class AsicId(Entity):
                        """
                        asic id
                        
                        .. attribute:: rack_type
                        
                        	Rack Type
                        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                        
                        .. attribute:: asic_type
                        
                        	Asic Type
                        	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                        
                        .. attribute:: rack_num
                        
                        	rack num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slot_num
                        
                        	slot num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: asic_instance
                        
                        	asic instance
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, self).__init__()

                            self.yang_name = "asic-id"
                            self.yang_parent_name = "device-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                            ])
                            self.rack_type = None
                            self.asic_type = None
                            self.rack_num = None
                            self.slot_num = None
                            self.asic_instance = None
                            self._segment_path = lambda: "asic-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                class CardInfo(Entity):
                    """
                    card info
                    
                    .. attribute:: oir_circular_buffer
                    
                    	oir circular buffer
                    	**type**\:  :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer>`
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_name
                    
                    	card name
                    	**type**\: str
                    
                    .. attribute:: slot_no
                    
                    	slot no
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_flag
                    
                    	card flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evt_flag
                    
                    	evt flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: reg_flag
                    
                    	reg flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: instance
                    
                    	instance
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_state
                    
                    	card state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: exp_num_asics
                    
                    	exp num asics
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: exp_num_asics_per_fsdb
                    
                    	exp num asics per fsdb
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_powered
                    
                    	is powered
                    	**type**\: bool
                    
                    .. attribute:: cxp_avail_bitmap
                    
                    	cxp avail bitmap
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: num_ilkns_per_asic
                    
                    	num ilkns per asic
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_local_ports_per_ilkn
                    
                    	num local ports per ilkn
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_cos_per_port
                    
                    	num cos per port
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.DriverInformation.CardInfo, self).__init__()

                        self.yang_name = "card-info"
                        self.yang_parent_name = "driver-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("oir-circular-buffer", ("oir_circular_buffer", Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer))])
                        self._leafs = OrderedDict([
                            ('card_type', (YLeaf(YType.int32, 'card-type'), ['int'])),
                            ('card_name', (YLeaf(YType.str, 'card-name'), ['str'])),
                            ('slot_no', (YLeaf(YType.int32, 'slot-no'), ['int'])),
                            ('card_flag', (YLeaf(YType.int32, 'card-flag'), ['int'])),
                            ('evt_flag', (YLeaf(YType.int32, 'evt-flag'), ['int'])),
                            ('reg_flag', (YLeaf(YType.int32, 'reg-flag'), ['int'])),
                            ('instance', (YLeaf(YType.int32, 'instance'), ['int'])),
                            ('card_state', (YLeaf(YType.uint8, 'card-state'), ['int'])),
                            ('exp_num_asics', (YLeaf(YType.uint32, 'exp-num-asics'), ['int'])),
                            ('exp_num_asics_per_fsdb', (YLeaf(YType.uint32, 'exp-num-asics-per-fsdb'), ['int'])),
                            ('is_powered', (YLeaf(YType.boolean, 'is-powered'), ['bool'])),
                            ('cxp_avail_bitmap', (YLeaf(YType.uint64, 'cxp-avail-bitmap'), ['int'])),
                            ('num_ilkns_per_asic', (YLeaf(YType.uint32, 'num-ilkns-per-asic'), ['int'])),
                            ('num_local_ports_per_ilkn', (YLeaf(YType.uint32, 'num-local-ports-per-ilkn'), ['int'])),
                            ('num_cos_per_port', (YLeaf(YType.uint8, 'num-cos-per-port'), ['int'])),
                        ])
                        self.card_type = None
                        self.card_name = None
                        self.slot_no = None
                        self.card_flag = None
                        self.evt_flag = None
                        self.reg_flag = None
                        self.instance = None
                        self.card_state = None
                        self.exp_num_asics = None
                        self.exp_num_asics_per_fsdb = None
                        self.is_powered = None
                        self.cxp_avail_bitmap = None
                        self.num_ilkns_per_asic = None
                        self.num_local_ports_per_ilkn = None
                        self.num_cos_per_port = None

                        self.oir_circular_buffer = Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer()
                        self.oir_circular_buffer.parent = self
                        self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                        self._segment_path = lambda: "card-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo, [u'card_type', u'card_name', u'slot_no', u'card_flag', u'evt_flag', u'reg_flag', u'instance', u'card_state', u'exp_num_asics', u'exp_num_asics_per_fsdb', u'is_powered', u'cxp_avail_bitmap', u'num_ilkns_per_asic', u'num_local_ports_per_ilkn', u'num_cos_per_port'], name, value)


                    class OirCircularBuffer(Entity):
                        """
                        oir circular buffer
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: fia_oir_info
                        
                        	fia oir info
                        	**type**\: list of  		 :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, self).__init__()

                            self.yang_name = "oir-circular-buffer"
                            self.yang_parent_name = "card-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("fia-oir-info", ("fia_oir_info", Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo))])
                            self._leafs = OrderedDict([
                                ('count', (YLeaf(YType.int32, 'count'), ['int'])),
                                ('start', (YLeaf(YType.int32, 'start'), ['int'])),
                                ('end', (YLeaf(YType.int32, 'end'), ['int'])),
                            ])
                            self.count = None
                            self.start = None
                            self.end = None

                            self.fia_oir_info = YList(self)
                            self._segment_path = lambda: "oir-circular-buffer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, [u'count', u'start', u'end'], name, value)


                        class FiaOirInfo(Entity):
                            """
                            fia oir info
                            
                            .. attribute:: card_flag
                            
                            	card flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_type
                            
                            	card type
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: reg_flag
                            
                            	reg flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evt_flag
                            
                            	evt flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: instance
                            
                            	instance
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: cur_card_state
                            
                            	cur card state
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, self).__init__()

                                self.yang_name = "fia-oir-info"
                                self.yang_parent_name = "oir-circular-buffer"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('card_flag', (YLeaf(YType.int32, 'card-flag'), ['int'])),
                                    ('card_type', (YLeaf(YType.int32, 'card-type'), ['int'])),
                                    ('reg_flag', (YLeaf(YType.int32, 'reg-flag'), ['int'])),
                                    ('evt_flag', (YLeaf(YType.int32, 'evt-flag'), ['int'])),
                                    ('rack_num', (YLeaf(YType.int32, 'rack-num'), ['int'])),
                                    ('instance', (YLeaf(YType.int32, 'instance'), ['int'])),
                                    ('cur_card_state', (YLeaf(YType.int32, 'cur-card-state'), ['int'])),
                                ])
                                self.card_flag = None
                                self.card_type = None
                                self.reg_flag = None
                                self.evt_flag = None
                                self.rack_num = None
                                self.instance = None
                                self.cur_card_state = None
                                self._segment_path = lambda: "fia-oir-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, [u'card_flag', u'card_type', u'reg_flag', u'evt_flag', u'rack_num', u'instance', u'cur_card_state'], name, value)


            class ClearStatistics(Entity):
                """
                Clear statistics information
                
                .. attribute:: asic_instances
                
                	Instance table for clear statistics information
                	**type**\:  :py:class:`AsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.ClearStatistics, self).__init__()

                    self.yang_name = "clear-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("asic-instances", ("asic_instances", Fia.Nodes.Node.ClearStatistics.AsicInstances))])
                    self._leafs = OrderedDict()

                    self.asic_instances = Fia.Nodes.Node.ClearStatistics.AsicInstances()
                    self.asic_instances.parent = self
                    self._children_name_map["asic_instances"] = "asic-instances"
                    self._segment_path = lambda: "clear-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.ClearStatistics, [], name, value)


                class AsicInstances(Entity):
                    """
                    Instance table for clear statistics
                    information
                    
                    .. attribute:: asic_instance
                    
                    	Asic instance to be cleared
                    	**type**\: list of  		 :py:class:`AsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.ClearStatistics.AsicInstances, self).__init__()

                        self.yang_name = "asic-instances"
                        self.yang_parent_name = "clear-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("asic-instance", ("asic_instance", Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance))])
                        self._leafs = OrderedDict()

                        self.asic_instance = YList(self)
                        self._segment_path = lambda: "asic-instances"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.ClearStatistics.AsicInstances, [], name, value)


                    class AsicInstance(Entity):
                        """
                        Asic instance to be cleared
                        
                        .. attribute:: asic_instance  (key)
                        
                        	Asic instance
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: instance
                        
                        	Clear value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance, self).__init__()

                            self.yang_name = "asic-instance"
                            self.yang_parent_name = "asic-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['asic_instance']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                            ])
                            self.asic_instance = None
                            self.instance = None
                            self._segment_path = lambda: "asic-instance" + "[asic-instance='" + str(self.asic_instance) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance, ['asic_instance', 'instance'], name, value)


            class TxLinkInformation(Entity):
                """
                FIA link TX information
                
                .. attribute:: tx_status_option_table
                
                	Link table for tx information
                	**type**\:  :py:class:`TxStatusOptionTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.TxLinkInformation, self).__init__()

                    self.yang_name = "tx-link-information"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tx-status-option-table", ("tx_status_option_table", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable))])
                    self._leafs = OrderedDict()

                    self.tx_status_option_table = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable()
                    self.tx_status_option_table.parent = self
                    self._children_name_map["tx_status_option_table"] = "tx-status-option-table"
                    self._segment_path = lambda: "tx-link-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation, [], name, value)


                class TxStatusOptionTable(Entity):
                    """
                    Link table for tx information
                    
                    .. attribute:: tx_status_option
                    
                    	Option\: data, ctrl, all\- for now none
                    	**type**\:  :py:class:`TxStatusOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable, self).__init__()

                        self.yang_name = "tx-status-option-table"
                        self.yang_parent_name = "tx-link-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tx-status-option", ("tx_status_option", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption))])
                        self._leafs = OrderedDict()

                        self.tx_status_option = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption()
                        self.tx_status_option.parent = self
                        self._children_name_map["tx_status_option"] = "tx-status-option"
                        self._segment_path = lambda: "tx-status-option-table"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable, [], name, value)


                    class TxStatusOption(Entity):
                        """
                        Option\: data, ctrl, all\- for now none
                        
                        .. attribute:: tx_asic_instances
                        
                        	Instance table for tx information
                        	**type**\:  :py:class:`TxAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption, self).__init__()

                            self.yang_name = "tx-status-option"
                            self.yang_parent_name = "tx-status-option-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tx-asic-instances", ("tx_asic_instances", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances))])
                            self._leafs = OrderedDict()

                            self.tx_asic_instances = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances()
                            self.tx_asic_instances.parent = self
                            self._children_name_map["tx_asic_instances"] = "tx-asic-instances"
                            self._segment_path = lambda: "tx-status-option"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption, [], name, value)


                        class TxAsicInstances(Entity):
                            """
                            Instance table for tx information
                            
                            .. attribute:: tx_asic_instance
                            
                            	Instance number for tx link information
                            	**type**\: list of  		 :py:class:`TxAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances, self).__init__()

                                self.yang_name = "tx-asic-instances"
                                self.yang_parent_name = "tx-status-option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tx-asic-instance", ("tx_asic_instance", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance))])
                                self._leafs = OrderedDict()

                                self.tx_asic_instance = YList(self)
                                self._segment_path = lambda: "tx-asic-instances"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances, [], name, value)


                            class TxAsicInstance(Entity):
                                """
                                Instance number for tx link information
                                
                                .. attribute:: instance  (key)
                                
                                	Transmit instance
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: tx_links
                                
                                	Link table for tx information
                                	**type**\:  :py:class:`TxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance, self).__init__()

                                    self.yang_name = "tx-asic-instance"
                                    self.yang_parent_name = "tx-asic-instances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['instance']
                                    self._child_classes = OrderedDict([("tx-links", ("tx_links", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks))])
                                    self._leafs = OrderedDict([
                                        ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                                    ])
                                    self.instance = None

                                    self.tx_links = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks()
                                    self.tx_links.parent = self
                                    self._children_name_map["tx_links"] = "tx-links"
                                    self._segment_path = lambda: "tx-asic-instance" + "[instance='" + str(self.instance) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance, ['instance'], name, value)


                                class TxLinks(Entity):
                                    """
                                    Link table for tx information
                                    
                                    .. attribute:: tx_link
                                    
                                    	Link number for tx link information
                                    	**type**\: list of  		 :py:class:`TxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks, self).__init__()

                                        self.yang_name = "tx-links"
                                        self.yang_parent_name = "tx-asic-instance"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-link", ("tx_link", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink))])
                                        self._leafs = OrderedDict()

                                        self.tx_link = YList(self)
                                        self._segment_path = lambda: "tx-links"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks, [], name, value)


                                    class TxLink(Entity):
                                        """
                                        Link number for tx link information
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: tx_link
                                        
                                        	Single link information
                                        	**type**\: list of  		 :py:class:`TxLink_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink, self).__init__()

                                            self.yang_name = "tx-link"
                                            self.yang_parent_name = "tx-links"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("tx-link", ("tx_link", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_))])
                                            self._leafs = OrderedDict([
                                                ('start_number', (YLeaf(YType.uint32, 'start-number'), ['int'])),
                                                ('end_number', (YLeaf(YType.uint32, 'end-number'), ['int'])),
                                            ])
                                            self.start_number = None
                                            self.end_number = None

                                            self.tx_link = YList(self)
                                            self._segment_path = lambda: "tx-link"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink, ['start_number', 'end_number'], name, value)


                                        class TxLink_(Entity):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  (key)
                                            
                                            	Single Link
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:  :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:  :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink>`
                                            
                                            .. attribute:: stats
                                            
                                            	stats
                                            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats>`
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	stage
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            .. attribute:: is_power_enabled
                                            
                                            	is power enabled
                                            	**type**\: bool
                                            
                                            .. attribute:: coeff1
                                            
                                            	coeff1
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: coeff2
                                            
                                            	coeff2
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_, self).__init__()

                                                self.yang_name = "tx-link"
                                                self.yang_parent_name = "tx-link"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['link']
                                                self._child_classes = OrderedDict([("this-link", ("this_link", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink)), ("far-end-link", ("far_end_link", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink)), ("stats", ("stats", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats)), ("history", ("history", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History))])
                                                self._leafs = OrderedDict([
                                                    ('link', (YLeaf(YType.uint32, 'link'), ['int'])),
                                                    ('speed', (YLeaf(YType.uint32, 'speed'), ['int'])),
                                                    ('stage', (YLeaf(YType.uint8, 'stage'), ['int'])),
                                                    ('is_link_valid', (YLeaf(YType.boolean, 'is-link-valid'), ['bool'])),
                                                    ('is_conf_pending', (YLeaf(YType.boolean, 'is-conf-pending'), ['bool'])),
                                                    ('is_power_enabled', (YLeaf(YType.boolean, 'is-power-enabled'), ['bool'])),
                                                    ('coeff1', (YLeaf(YType.uint32, 'coeff1'), ['int'])),
                                                    ('coeff2', (YLeaf(YType.uint32, 'coeff2'), ['int'])),
                                                    ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                                                    ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperState', '')])),
                                                    ('error_state', (YLeaf(YType.enumeration, 'error-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorState', '')])),
                                                    ('num_admin_shuts', (YLeaf(YType.uint32, 'num-admin-shuts'), ['int'])),
                                                ])
                                                self.link = None
                                                self.speed = None
                                                self.stage = None
                                                self.is_link_valid = None
                                                self.is_conf_pending = None
                                                self.is_power_enabled = None
                                                self.coeff1 = None
                                                self.coeff2 = None
                                                self.admin_state = None
                                                self.oper_state = None
                                                self.error_state = None
                                                self.num_admin_shuts = None

                                                self.this_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink()
                                                self.this_link.parent = self
                                                self._children_name_map["this_link"] = "this-link"

                                                self.far_end_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink()
                                                self.far_end_link.parent = self
                                                self._children_name_map["far_end_link"] = "far-end-link"

                                                self.stats = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats()
                                                self.stats.parent = self
                                                self._children_name_map["stats"] = "stats"

                                                self.history = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History()
                                                self.history.parent = self
                                                self._children_name_map["history"] = "history"
                                                self._segment_path = lambda: "tx-link" + "[link='" + str(self.link) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_, ['link', u'speed', u'stage', u'is_link_valid', u'is_conf_pending', u'is_power_enabled', u'coeff1', u'coeff2', u'admin_state', u'oper_state', u'error_state', u'num_admin_shuts'], name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink, self).__init__()

                                                    self.yang_name = "this-link"
                                                    self.yang_parent_name = "tx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Link', '')])),
                                                        ('link_stage', (YLeaf(YType.enumeration, 'link-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                        ('link_num', (YLeaf(YType.uint32, 'link-num'), ['int'])),
                                                        ('phy_link_num', (YLeaf(YType.uint32, 'phy-link-num'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None

                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._segment_path = lambda: "this-link"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink, [u'link_type', u'link_stage', u'link_num', u'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "this-link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                            ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                            ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                            ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                            ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                        ])
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None
                                                        self._segment_path = lambda: "asic-id"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink, self).__init__()

                                                    self.yang_name = "far-end-link"
                                                    self.yang_parent_name = "tx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Link', '')])),
                                                        ('link_stage', (YLeaf(YType.enumeration, 'link-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStage', '')])),
                                                        ('link_num', (YLeaf(YType.uint32, 'link-num'), ['int'])),
                                                        ('phy_link_num', (YLeaf(YType.uint32, 'phy-link-num'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None

                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._segment_path = lambda: "far-end-link"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink, [u'link_type', u'link_stage', u'link_num', u'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                            ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                            ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                            ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                            ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                        ])
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None
                                                        self._segment_path = lambda: "asic-id"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                            class Stats(Entity):
                                                """
                                                stats
                                                
                                                .. attribute:: dummy
                                                
                                                	dummy
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats, self).__init__()

                                                    self.yang_name = "stats"
                                                    self.yang_parent_name = "tx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('dummy', (YLeaf(YType.uint32, 'dummy'), ['int'])),
                                                    ])
                                                    self.dummy = None
                                                    self._segment_path = lambda: "stats"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats, [u'dummy'], name, value)


                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of  		 :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist>`
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History, self).__init__()

                                                    self.yang_name = "history"
                                                    self.yang_parent_name = "tx-link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("hist", ("hist", Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist))])
                                                    self._leafs = OrderedDict([
                                                        ('histnum', (YLeaf(YType.uint8, 'histnum'), ['int'])),
                                                        ('start_index', (YLeaf(YType.uint8, 'start-index'), ['int'])),
                                                    ])
                                                    self.histnum = None
                                                    self.start_index = None

                                                    self.hist = YList(self)
                                                    self._segment_path = lambda: "history"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History, [u'histnum', u'start_index'], name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2017-08-29'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist, self).__init__()

                                                        self.yang_name = "hist"
                                                        self.yang_parent_name = "history"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                                                            ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperState', '')])),
                                                            ('error_state', (YLeaf(YType.enumeration, 'error-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorState', '')])),
                                                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                                                            ('reasons', (YLeaf(YType.str, 'reasons'), ['str'])),
                                                        ])
                                                        self.admin_state = None
                                                        self.oper_state = None
                                                        self.error_state = None
                                                        self.timestamp = None
                                                        self.reasons = None
                                                        self._segment_path = lambda: "hist"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist, [u'admin_state', u'oper_state', u'error_state', u'timestamp', u'reasons'], name, value)


            class DiagShell(Entity):
                """
                FIA diag shell information
                
                .. attribute:: diag_shell_units
                
                	Unit table for diag shell
                	**type**\:  :py:class:`DiagShellUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.DiagShell, self).__init__()

                    self.yang_name = "diag-shell"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("diag-shell-units", ("diag_shell_units", Fia.Nodes.Node.DiagShell.DiagShellUnits))])
                    self._leafs = OrderedDict()

                    self.diag_shell_units = Fia.Nodes.Node.DiagShell.DiagShellUnits()
                    self.diag_shell_units.parent = self
                    self._children_name_map["diag_shell_units"] = "diag-shell-units"
                    self._segment_path = lambda: "diag-shell"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.DiagShell, [], name, value)


                class DiagShellUnits(Entity):
                    """
                    Unit table for diag shell
                    
                    .. attribute:: diag_shell_unit
                    
                    	Unit number for diag shell statistics
                    	**type**\: list of  		 :py:class:`DiagShellUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits, self).__init__()

                        self.yang_name = "diag-shell-units"
                        self.yang_parent_name = "diag-shell"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("diag-shell-unit", ("diag_shell_unit", Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit))])
                        self._leafs = OrderedDict()

                        self.diag_shell_unit = YList(self)
                        self._segment_path = lambda: "diag-shell-units"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits, [], name, value)


                    class DiagShellUnit(Entity):
                        """
                        Unit number for diag shell statistics
                        
                        .. attribute:: unit  (key)
                        
                        	Unit number
                        	**type**\: int
                        
                        	**range:** 0..63
                        
                        .. attribute:: commands
                        
                        	Command table for diag shell
                        	**type**\:  :py:class:`Commands <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit, self).__init__()

                            self.yang_name = "diag-shell-unit"
                            self.yang_parent_name = "diag-shell-units"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['unit']
                            self._child_classes = OrderedDict([("commands", ("commands", Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands))])
                            self._leafs = OrderedDict([
                                ('unit', (YLeaf(YType.uint32, 'unit'), ['int'])),
                            ])
                            self.unit = None

                            self.commands = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands()
                            self.commands.parent = self
                            self._children_name_map["commands"] = "commands"
                            self._segment_path = lambda: "diag-shell-unit" + "[unit='" + str(self.unit) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit, ['unit'], name, value)


                        class Commands(Entity):
                            """
                            Command table for diag shell
                            
                            .. attribute:: command
                            
                            	Command for diag shell statistics
                            	**type**\: list of  		 :py:class:`Command <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands, self).__init__()

                                self.yang_name = "commands"
                                self.yang_parent_name = "diag-shell-unit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("command", ("command", Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command))])
                                self._leafs = OrderedDict()

                                self.command = YList(self)
                                self._segment_path = lambda: "commands"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands, [], name, value)


                            class Command(Entity):
                                """
                                Command for diag shell statistics
                                
                                .. attribute:: cmd  (key)
                                
                                	Shell command
                                	**type**\: str
                                
                                .. attribute:: output
                                
                                	Added to support datalist
                                	**type**\: list of  		 :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command, self).__init__()

                                    self.yang_name = "command"
                                    self.yang_parent_name = "commands"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['cmd']
                                    self._child_classes = OrderedDict([("output", ("output", Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output))])
                                    self._leafs = OrderedDict([
                                        ('cmd', (YLeaf(YType.str, 'cmd'), ['str'])),
                                    ])
                                    self.cmd = None

                                    self.output = YList(self)
                                    self._segment_path = lambda: "command" + "[cmd='" + str(self.cmd) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command, ['cmd'], name, value)


                                class Output(Entity):
                                    """
                                    Added to support datalist
                                    
                                    .. attribute:: output  (key)
                                    
                                    	First line
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: output_xr
                                    
                                    	output xr
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, self).__init__()

                                        self.yang_name = "output"
                                        self.yang_parent_name = "command"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['output']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('output', (YLeaf(YType.str, 'output'), ['str'])),
                                            ('output_xr', (YLeaf(YType.str, 'output-xr'), ['str'])),
                                        ])
                                        self.output = None
                                        self.output_xr = None
                                        self._segment_path = lambda: "output" + "[output='" + str(self.output) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, ['output', u'output_xr'], name, value)


            class OirHistory(Entity):
                """
                FIA operational data of oir history
                
                .. attribute:: flags
                
                	Flag table for history
                	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.OirHistory, self).__init__()

                    self.yang_name = "oir-history"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("flags", ("flags", Fia.Nodes.Node.OirHistory.Flags))])
                    self._leafs = OrderedDict()

                    self.flags = Fia.Nodes.Node.OirHistory.Flags()
                    self.flags.parent = self
                    self._children_name_map["flags"] = "flags"
                    self._segment_path = lambda: "oir-history"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.OirHistory, [], name, value)


                class Flags(Entity):
                    """
                    Flag table for history
                    
                    .. attribute:: flag
                    
                    	Flag value for physical location
                    	**type**\: list of  		 :py:class:`Flag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.OirHistory.Flags, self).__init__()

                        self.yang_name = "flags"
                        self.yang_parent_name = "oir-history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flag", ("flag", Fia.Nodes.Node.OirHistory.Flags.Flag))])
                        self._leafs = OrderedDict()

                        self.flag = YList(self)
                        self._segment_path = lambda: "flags"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags, [], name, value)


                    class Flag(Entity):
                        """
                        Flag value for physical location
                        
                        .. attribute:: flag  (key)
                        
                        	Flag value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slots
                        
                        	Slot table for history
                        	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.OirHistory.Flags.Flag, self).__init__()

                            self.yang_name = "flag"
                            self.yang_parent_name = "flags"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flag']
                            self._child_classes = OrderedDict([("slots", ("slots", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots))])
                            self._leafs = OrderedDict([
                                ('flag', (YLeaf(YType.uint32, 'flag'), ['int'])),
                            ])
                            self.flag = None

                            self.slots = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots()
                            self.slots.parent = self
                            self._children_name_map["slots"] = "slots"
                            self._segment_path = lambda: "flag" + "[flag='" + str(self.flag) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag, ['flag'], name, value)


                        class Slots(Entity):
                            """
                            Slot table for history
                            
                            .. attribute:: slot
                            
                            	Slot number for getting history
                            	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots, self).__init__()

                                self.yang_name = "slots"
                                self.yang_parent_name = "flag"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("slot", ("slot", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot))])
                                self._leafs = OrderedDict()

                                self.slot = YList(self)
                                self._segment_path = lambda: "slots"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots, [], name, value)


                            class Slot(Entity):
                                """
                                Slot number for getting history
                                
                                .. attribute:: slot  (key)
                                
                                	Slot number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: drv_version
                                
                                	drv version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: coeff_major_rev
                                
                                	coeff major rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: coeff_minor_rev
                                
                                	coeff minor rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: functional_role
                                
                                	functional role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: issu_role
                                
                                	issu role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: node_id
                                
                                	node id
                                	**type**\: str
                                
                                .. attribute:: rack_type
                                
                                	rack type
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: rack_num
                                
                                	rack num
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: is_driver_ready
                                
                                	is driver ready
                                	**type**\: bool
                                
                                .. attribute:: card_avail_mask
                                
                                	card avail mask
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_avail_mask
                                
                                	asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: exp_asic_avail_mask
                                
                                	exp asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ucmc_ratio
                                
                                	ucmc ratio
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                                
                                	asic oper notify to fsdb pending bmap
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_full_fgid_download_req
                                
                                	is full fgid download req
                                	**type**\: bool
                                
                                .. attribute:: is_fgid_download_in_progress
                                
                                	is fgid download in progress
                                	**type**\: bool
                                
                                .. attribute:: is_fgid_download_completed
                                
                                	is fgid download completed
                                	**type**\: bool
                                
                                .. attribute:: fsdb_conn_active
                                
                                	fsdb conn active
                                	**type**\: bool
                                
                                .. attribute:: fgid_conn_active
                                
                                	fgid conn active
                                	**type**\: bool
                                
                                .. attribute:: issu_mgr_conn_active
                                
                                	issu mgr conn active
                                	**type**\: bool
                                
                                .. attribute:: fsdb_reg_active
                                
                                	fsdb reg active
                                	**type**\: bool
                                
                                .. attribute:: fgid_reg_active
                                
                                	fgid reg active
                                	**type**\: bool
                                
                                .. attribute:: issu_mgr_reg_active
                                
                                	issu mgr reg active
                                	**type**\: bool
                                
                                .. attribute:: num_pm_conn_reqs
                                
                                	num pm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fsdb_conn_reqs
                                
                                	num fsdb conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fgid_conn_reqs
                                
                                	num fgid conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fstats_conn_reqs
                                
                                	num fstats conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_cm_conn_reqs
                                
                                	num cm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_issu_mgr_conn_reqs
                                
                                	num issu mgr conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_peer_fia_conn_reqs
                                
                                	num peer fia conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: is_gaspp_registered
                                
                                	is gaspp registered
                                	**type**\: bool
                                
                                .. attribute:: is_cih_registered
                                
                                	is cih registered
                                	**type**\: bool
                                
                                .. attribute:: drvr_initial_startup_timestamp
                                
                                	drvr initial startup timestamp
                                	**type**\: str
                                
                                .. attribute:: drvr_current_startup_timestamp
                                
                                	drvr current startup timestamp
                                	**type**\: str
                                
                                .. attribute:: num_intf_ports
                                
                                	num intf ports
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: uc_weight
                                
                                	uc weight
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: respawn_count
                                
                                	respawn count
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: total_asics
                                
                                	total asics
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: issu_ready_ntfy_pending
                                
                                	issu ready ntfy pending
                                	**type**\: bool
                                
                                .. attribute:: issu_abort_sent
                                
                                	issu abort sent
                                	**type**\: bool
                                
                                .. attribute:: issu_abort_rcvd
                                
                                	issu abort rcvd
                                	**type**\: bool
                                
                                .. attribute:: fabric_mode
                                
                                	fabric mode
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: fc_mode
                                
                                	FC Mode
                                	**type**\:  :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                                
                                .. attribute:: board_rev_id
                                
                                	board rev id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: all_wb_insync
                                
                                	all wb insync
                                	**type**\: bool
                                
                                .. attribute:: all_wb_insync_since
                                
                                	all wb insync since
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: all_startup_wb_insync
                                
                                	all startup wb insync
                                	**type**\: bool
                                
                                .. attribute:: plane_a_bitmap
                                
                                	planeA bitmap
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: plane_b_bitmap
                                
                                	planeB bitmap
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: device_info
                                
                                	device info
                                	**type**\: list of  		 :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo>`
                                
                                .. attribute:: card_info
                                
                                	card info
                                	**type**\: list of  		 :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, self).__init__()

                                    self.yang_name = "slot"
                                    self.yang_parent_name = "slots"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['slot']
                                    self._child_classes = OrderedDict([("device-info", ("device_info", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo)), ("card-info", ("card_info", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo))])
                                    self._leafs = OrderedDict([
                                        ('slot', (YLeaf(YType.uint32, 'slot'), ['int'])),
                                        ('drv_version', (YLeaf(YType.uint32, 'drv-version'), ['int'])),
                                        ('coeff_major_rev', (YLeaf(YType.uint32, 'coeff-major-rev'), ['int'])),
                                        ('coeff_minor_rev', (YLeaf(YType.uint32, 'coeff-minor-rev'), ['int'])),
                                        ('functional_role', (YLeaf(YType.uint8, 'functional-role'), ['int'])),
                                        ('issu_role', (YLeaf(YType.uint8, 'issu-role'), ['int'])),
                                        ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                        ('rack_type', (YLeaf(YType.int32, 'rack-type'), ['int'])),
                                        ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                                        ('is_driver_ready', (YLeaf(YType.boolean, 'is-driver-ready'), ['bool'])),
                                        ('card_avail_mask', (YLeaf(YType.uint32, 'card-avail-mask'), ['int'])),
                                        ('asic_avail_mask', (YLeaf(YType.uint64, 'asic-avail-mask'), ['int'])),
                                        ('exp_asic_avail_mask', (YLeaf(YType.uint64, 'exp-asic-avail-mask'), ['int'])),
                                        ('ucmc_ratio', (YLeaf(YType.uint32, 'ucmc-ratio'), ['int'])),
                                        ('asic_oper_notify_to_fsdb_pending_bmap', (YLeaf(YType.uint64, 'asic-oper-notify-to-fsdb-pending-bmap'), ['int'])),
                                        ('is_full_fgid_download_req', (YLeaf(YType.boolean, 'is-full-fgid-download-req'), ['bool'])),
                                        ('is_fgid_download_in_progress', (YLeaf(YType.boolean, 'is-fgid-download-in-progress'), ['bool'])),
                                        ('is_fgid_download_completed', (YLeaf(YType.boolean, 'is-fgid-download-completed'), ['bool'])),
                                        ('fsdb_conn_active', (YLeaf(YType.boolean, 'fsdb-conn-active'), ['bool'])),
                                        ('fgid_conn_active', (YLeaf(YType.boolean, 'fgid-conn-active'), ['bool'])),
                                        ('issu_mgr_conn_active', (YLeaf(YType.boolean, 'issu-mgr-conn-active'), ['bool'])),
                                        ('fsdb_reg_active', (YLeaf(YType.boolean, 'fsdb-reg-active'), ['bool'])),
                                        ('fgid_reg_active', (YLeaf(YType.boolean, 'fgid-reg-active'), ['bool'])),
                                        ('issu_mgr_reg_active', (YLeaf(YType.boolean, 'issu-mgr-reg-active'), ['bool'])),
                                        ('num_pm_conn_reqs', (YLeaf(YType.uint8, 'num-pm-conn-reqs'), ['int'])),
                                        ('num_fsdb_conn_reqs', (YLeaf(YType.uint8, 'num-fsdb-conn-reqs'), ['int'])),
                                        ('num_fgid_conn_reqs', (YLeaf(YType.uint8, 'num-fgid-conn-reqs'), ['int'])),
                                        ('num_fstats_conn_reqs', (YLeaf(YType.uint8, 'num-fstats-conn-reqs'), ['int'])),
                                        ('num_cm_conn_reqs', (YLeaf(YType.uint8, 'num-cm-conn-reqs'), ['int'])),
                                        ('num_issu_mgr_conn_reqs', (YLeaf(YType.uint8, 'num-issu-mgr-conn-reqs'), ['int'])),
                                        ('num_peer_fia_conn_reqs', (YLeaf(YType.uint8, 'num-peer-fia-conn-reqs'), ['int'])),
                                        ('is_gaspp_registered', (YLeaf(YType.boolean, 'is-gaspp-registered'), ['bool'])),
                                        ('is_cih_registered', (YLeaf(YType.boolean, 'is-cih-registered'), ['bool'])),
                                        ('drvr_initial_startup_timestamp', (YLeaf(YType.str, 'drvr-initial-startup-timestamp'), ['str'])),
                                        ('drvr_current_startup_timestamp', (YLeaf(YType.str, 'drvr-current-startup-timestamp'), ['str'])),
                                        ('num_intf_ports', (YLeaf(YType.uint32, 'num-intf-ports'), ['int'])),
                                        ('uc_weight', (YLeaf(YType.uint8, 'uc-weight'), ['int'])),
                                        ('respawn_count', (YLeaf(YType.uint8, 'respawn-count'), ['int'])),
                                        ('total_asics', (YLeaf(YType.uint8, 'total-asics'), ['int'])),
                                        ('issu_ready_ntfy_pending', (YLeaf(YType.boolean, 'issu-ready-ntfy-pending'), ['bool'])),
                                        ('issu_abort_sent', (YLeaf(YType.boolean, 'issu-abort-sent'), ['bool'])),
                                        ('issu_abort_rcvd', (YLeaf(YType.boolean, 'issu-abort-rcvd'), ['bool'])),
                                        ('fabric_mode', (YLeaf(YType.uint8, 'fabric-mode'), ['int'])),
                                        ('fc_mode', (YLeaf(YType.enumeration, 'fc-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'FcMode', '')])),
                                        ('board_rev_id', (YLeaf(YType.uint32, 'board-rev-id'), ['int'])),
                                        ('all_wb_insync', (YLeaf(YType.boolean, 'all-wb-insync'), ['bool'])),
                                        ('all_wb_insync_since', (YLeaf(YType.uint32, 'all-wb-insync-since'), ['int'])),
                                        ('all_startup_wb_insync', (YLeaf(YType.boolean, 'all-startup-wb-insync'), ['bool'])),
                                        ('plane_a_bitmap', (YLeaf(YType.uint32, 'plane-a-bitmap'), ['int'])),
                                        ('plane_b_bitmap', (YLeaf(YType.uint32, 'plane-b-bitmap'), ['int'])),
                                    ])
                                    self.slot = None
                                    self.drv_version = None
                                    self.coeff_major_rev = None
                                    self.coeff_minor_rev = None
                                    self.functional_role = None
                                    self.issu_role = None
                                    self.node_id = None
                                    self.rack_type = None
                                    self.rack_num = None
                                    self.is_driver_ready = None
                                    self.card_avail_mask = None
                                    self.asic_avail_mask = None
                                    self.exp_asic_avail_mask = None
                                    self.ucmc_ratio = None
                                    self.asic_oper_notify_to_fsdb_pending_bmap = None
                                    self.is_full_fgid_download_req = None
                                    self.is_fgid_download_in_progress = None
                                    self.is_fgid_download_completed = None
                                    self.fsdb_conn_active = None
                                    self.fgid_conn_active = None
                                    self.issu_mgr_conn_active = None
                                    self.fsdb_reg_active = None
                                    self.fgid_reg_active = None
                                    self.issu_mgr_reg_active = None
                                    self.num_pm_conn_reqs = None
                                    self.num_fsdb_conn_reqs = None
                                    self.num_fgid_conn_reqs = None
                                    self.num_fstats_conn_reqs = None
                                    self.num_cm_conn_reqs = None
                                    self.num_issu_mgr_conn_reqs = None
                                    self.num_peer_fia_conn_reqs = None
                                    self.is_gaspp_registered = None
                                    self.is_cih_registered = None
                                    self.drvr_initial_startup_timestamp = None
                                    self.drvr_current_startup_timestamp = None
                                    self.num_intf_ports = None
                                    self.uc_weight = None
                                    self.respawn_count = None
                                    self.total_asics = None
                                    self.issu_ready_ntfy_pending = None
                                    self.issu_abort_sent = None
                                    self.issu_abort_rcvd = None
                                    self.fabric_mode = None
                                    self.fc_mode = None
                                    self.board_rev_id = None
                                    self.all_wb_insync = None
                                    self.all_wb_insync_since = None
                                    self.all_startup_wb_insync = None
                                    self.plane_a_bitmap = None
                                    self.plane_b_bitmap = None

                                    self.device_info = YList(self)
                                    self.card_info = YList(self)
                                    self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, ['slot', u'drv_version', u'coeff_major_rev', u'coeff_minor_rev', u'functional_role', u'issu_role', u'node_id', u'rack_type', u'rack_num', u'is_driver_ready', u'card_avail_mask', u'asic_avail_mask', u'exp_asic_avail_mask', u'ucmc_ratio', u'asic_oper_notify_to_fsdb_pending_bmap', u'is_full_fgid_download_req', u'is_fgid_download_in_progress', u'is_fgid_download_completed', u'fsdb_conn_active', u'fgid_conn_active', u'issu_mgr_conn_active', u'fsdb_reg_active', u'fgid_reg_active', u'issu_mgr_reg_active', u'num_pm_conn_reqs', u'num_fsdb_conn_reqs', u'num_fgid_conn_reqs', u'num_fstats_conn_reqs', u'num_cm_conn_reqs', u'num_issu_mgr_conn_reqs', u'num_peer_fia_conn_reqs', u'is_gaspp_registered', u'is_cih_registered', u'drvr_initial_startup_timestamp', u'drvr_current_startup_timestamp', u'num_intf_ports', u'uc_weight', u'respawn_count', u'total_asics', u'issu_ready_ntfy_pending', u'issu_abort_sent', u'issu_abort_rcvd', u'fabric_mode', u'fc_mode', u'board_rev_id', u'all_wb_insync', u'all_wb_insync_since', u'all_startup_wb_insync', u'plane_a_bitmap', u'plane_b_bitmap'], name, value)


                                class DeviceInfo(Entity):
                                    """
                                    device info
                                    
                                    .. attribute:: asic_id
                                    
                                    	asic id
                                    	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId>`
                                    
                                    .. attribute:: is_valid
                                    
                                    	is valid
                                    	**type**\: bool
                                    
                                    .. attribute:: fapid
                                    
                                    	fapid
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hotplug_event
                                    
                                    	hotplug event
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: slice_state
                                    
                                    	Slice State
                                    	**type**\:  :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                                    
                                    .. attribute:: admin_state
                                    
                                    	Admin State
                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                    
                                    .. attribute:: oper_state
                                    
                                    	Oper State
                                    	**type**\:  :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                                    
                                    .. attribute:: asic_state
                                    
                                    	Asic State
                                    	**type**\:  :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                                    
                                    .. attribute:: last_init_cause
                                    
                                    	last init cause
                                    	**type**\:  :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                                    
                                    .. attribute:: num_pon_resets
                                    
                                    	num pon resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_hard_resets
                                    
                                    	num hard resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: local_switch_state
                                    
                                    	local switch state
                                    	**type**\: bool
                                    
                                    .. attribute:: startup_wb_mtime_str
                                    
                                    	startup wb mtime str
                                    	**type**\: str
                                    
                                    .. attribute:: startup_wb_outof_sync
                                    
                                    	startup wb outof sync
                                    	**type**\: bool
                                    
                                    .. attribute:: local_wb_sync_end_str
                                    
                                    	local wb sync end str
                                    	**type**\: str
                                    
                                    .. attribute:: remote_wb_sync_end_str
                                    
                                    	remote wb sync end str
                                    	**type**\: str
                                    
                                    .. attribute:: local_wb_sync_pending
                                    
                                    	local wb sync pending
                                    	**type**\: bool
                                    
                                    .. attribute:: sdk_delay_msec
                                    
                                    	sdk delay msec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, self).__init__()

                                        self.yang_name = "device-info"
                                        self.yang_parent_name = "slot"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("asic-id", ("asic_id", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId))])
                                        self._leafs = OrderedDict([
                                            ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                            ('fapid', (YLeaf(YType.uint32, 'fapid'), ['int'])),
                                            ('hotplug_event', (YLeaf(YType.uint32, 'hotplug-event'), ['int'])),
                                            ('slice_state', (YLeaf(YType.enumeration, 'slice-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'SliceState', '')])),
                                            ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminState', '')])),
                                            ('oper_state', (YLeaf(YType.enumeration, 'oper-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicOperState', '')])),
                                            ('asic_state', (YLeaf(YType.enumeration, 'asic-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicAccessState', '')])),
                                            ('last_init_cause', (YLeaf(YType.enumeration, 'last-init-cause'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicInitMethod', '')])),
                                            ('num_pon_resets', (YLeaf(YType.uint32, 'num-pon-resets'), ['int'])),
                                            ('num_hard_resets', (YLeaf(YType.uint32, 'num-hard-resets'), ['int'])),
                                            ('local_switch_state', (YLeaf(YType.boolean, 'local-switch-state'), ['bool'])),
                                            ('startup_wb_mtime_str', (YLeaf(YType.str, 'startup-wb-mtime-str'), ['str'])),
                                            ('startup_wb_outof_sync', (YLeaf(YType.boolean, 'startup-wb-outof-sync'), ['bool'])),
                                            ('local_wb_sync_end_str', (YLeaf(YType.str, 'local-wb-sync-end-str'), ['str'])),
                                            ('remote_wb_sync_end_str', (YLeaf(YType.str, 'remote-wb-sync-end-str'), ['str'])),
                                            ('local_wb_sync_pending', (YLeaf(YType.boolean, 'local-wb-sync-pending'), ['bool'])),
                                            ('sdk_delay_msec', (YLeaf(YType.uint32, 'sdk-delay-msec'), ['int'])),
                                        ])
                                        self.is_valid = None
                                        self.fapid = None
                                        self.hotplug_event = None
                                        self.slice_state = None
                                        self.admin_state = None
                                        self.oper_state = None
                                        self.asic_state = None
                                        self.last_init_cause = None
                                        self.num_pon_resets = None
                                        self.num_hard_resets = None
                                        self.local_switch_state = None
                                        self.startup_wb_mtime_str = None
                                        self.startup_wb_outof_sync = None
                                        self.local_wb_sync_end_str = None
                                        self.remote_wb_sync_end_str = None
                                        self.local_wb_sync_pending = None
                                        self.sdk_delay_msec = None

                                        self.asic_id = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId()
                                        self.asic_id.parent = self
                                        self._children_name_map["asic_id"] = "asic-id"
                                        self._segment_path = lambda: "device-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, [u'is_valid', u'fapid', u'hotplug_event', u'slice_state', u'admin_state', u'oper_state', u'asic_state', u'last_init_cause', u'num_pon_resets', u'num_hard_resets', u'local_switch_state', u'startup_wb_mtime_str', u'startup_wb_outof_sync', u'local_wb_sync_end_str', u'remote_wb_sync_end_str', u'local_wb_sync_pending', u'sdk_delay_msec'], name, value)


                                    class AsicId(Entity):
                                        """
                                        asic id
                                        
                                        .. attribute:: rack_type
                                        
                                        	Rack Type
                                        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                        
                                        .. attribute:: asic_type
                                        
                                        	Asic Type
                                        	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                        
                                        .. attribute:: rack_num
                                        
                                        	rack num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: slot_num
                                        
                                        	slot num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, self).__init__()

                                            self.yang_name = "asic-id"
                                            self.yang_parent_name = "device-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rack_type', (YLeaf(YType.enumeration, 'rack-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Rack', '')])),
                                                ('asic_type', (YLeaf(YType.enumeration, 'asic-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Asic', '')])),
                                                ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                                ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                                                ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                            ])
                                            self.rack_type = None
                                            self.asic_type = None
                                            self.rack_num = None
                                            self.slot_num = None
                                            self.asic_instance = None
                                            self._segment_path = lambda: "asic-id"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, [u'rack_type', u'asic_type', u'rack_num', u'slot_num', u'asic_instance'], name, value)


                                class CardInfo(Entity):
                                    """
                                    card info
                                    
                                    .. attribute:: oir_circular_buffer
                                    
                                    	oir circular buffer
                                    	**type**\:  :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer>`
                                    
                                    .. attribute:: card_type
                                    
                                    	card type
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_name
                                    
                                    	card name
                                    	**type**\: str
                                    
                                    .. attribute:: slot_no
                                    
                                    	slot no
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_flag
                                    
                                    	card flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: evt_flag
                                    
                                    	evt flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: reg_flag
                                    
                                    	reg flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: instance
                                    
                                    	instance
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_state
                                    
                                    	card state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: exp_num_asics
                                    
                                    	exp num asics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: exp_num_asics_per_fsdb
                                    
                                    	exp num asics per fsdb
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_powered
                                    
                                    	is powered
                                    	**type**\: bool
                                    
                                    .. attribute:: cxp_avail_bitmap
                                    
                                    	cxp avail bitmap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: num_ilkns_per_asic
                                    
                                    	num ilkns per asic
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_local_ports_per_ilkn
                                    
                                    	num local ports per ilkn
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_cos_per_port
                                    
                                    	num cos per port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, self).__init__()

                                        self.yang_name = "card-info"
                                        self.yang_parent_name = "slot"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("oir-circular-buffer", ("oir_circular_buffer", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer))])
                                        self._leafs = OrderedDict([
                                            ('card_type', (YLeaf(YType.int32, 'card-type'), ['int'])),
                                            ('card_name', (YLeaf(YType.str, 'card-name'), ['str'])),
                                            ('slot_no', (YLeaf(YType.int32, 'slot-no'), ['int'])),
                                            ('card_flag', (YLeaf(YType.int32, 'card-flag'), ['int'])),
                                            ('evt_flag', (YLeaf(YType.int32, 'evt-flag'), ['int'])),
                                            ('reg_flag', (YLeaf(YType.int32, 'reg-flag'), ['int'])),
                                            ('instance', (YLeaf(YType.int32, 'instance'), ['int'])),
                                            ('card_state', (YLeaf(YType.uint8, 'card-state'), ['int'])),
                                            ('exp_num_asics', (YLeaf(YType.uint32, 'exp-num-asics'), ['int'])),
                                            ('exp_num_asics_per_fsdb', (YLeaf(YType.uint32, 'exp-num-asics-per-fsdb'), ['int'])),
                                            ('is_powered', (YLeaf(YType.boolean, 'is-powered'), ['bool'])),
                                            ('cxp_avail_bitmap', (YLeaf(YType.uint64, 'cxp-avail-bitmap'), ['int'])),
                                            ('num_ilkns_per_asic', (YLeaf(YType.uint32, 'num-ilkns-per-asic'), ['int'])),
                                            ('num_local_ports_per_ilkn', (YLeaf(YType.uint32, 'num-local-ports-per-ilkn'), ['int'])),
                                            ('num_cos_per_port', (YLeaf(YType.uint8, 'num-cos-per-port'), ['int'])),
                                        ])
                                        self.card_type = None
                                        self.card_name = None
                                        self.slot_no = None
                                        self.card_flag = None
                                        self.evt_flag = None
                                        self.reg_flag = None
                                        self.instance = None
                                        self.card_state = None
                                        self.exp_num_asics = None
                                        self.exp_num_asics_per_fsdb = None
                                        self.is_powered = None
                                        self.cxp_avail_bitmap = None
                                        self.num_ilkns_per_asic = None
                                        self.num_local_ports_per_ilkn = None
                                        self.num_cos_per_port = None

                                        self.oir_circular_buffer = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer()
                                        self.oir_circular_buffer.parent = self
                                        self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                                        self._segment_path = lambda: "card-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, [u'card_type', u'card_name', u'slot_no', u'card_flag', u'evt_flag', u'reg_flag', u'instance', u'card_state', u'exp_num_asics', u'exp_num_asics_per_fsdb', u'is_powered', u'cxp_avail_bitmap', u'num_ilkns_per_asic', u'num_local_ports_per_ilkn', u'num_cos_per_port'], name, value)


                                    class OirCircularBuffer(Entity):
                                        """
                                        oir circular buffer
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: start
                                        
                                        	start
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: end
                                        
                                        	end
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: fia_oir_info
                                        
                                        	fia oir info
                                        	**type**\: list of  		 :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, self).__init__()

                                            self.yang_name = "oir-circular-buffer"
                                            self.yang_parent_name = "card-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("fia-oir-info", ("fia_oir_info", Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo))])
                                            self._leafs = OrderedDict([
                                                ('count', (YLeaf(YType.int32, 'count'), ['int'])),
                                                ('start', (YLeaf(YType.int32, 'start'), ['int'])),
                                                ('end', (YLeaf(YType.int32, 'end'), ['int'])),
                                            ])
                                            self.count = None
                                            self.start = None
                                            self.end = None

                                            self.fia_oir_info = YList(self)
                                            self._segment_path = lambda: "oir-circular-buffer"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, [u'count', u'start', u'end'], name, value)


                                        class FiaOirInfo(Entity):
                                            """
                                            fia oir info
                                            
                                            .. attribute:: card_flag
                                            
                                            	card flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_type
                                            
                                            	card type
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: reg_flag
                                            
                                            	reg flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: evt_flag
                                            
                                            	evt flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: rack_num
                                            
                                            	rack num
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: instance
                                            
                                            	instance
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: cur_card_state
                                            
                                            	cur card state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, self).__init__()

                                                self.yang_name = "fia-oir-info"
                                                self.yang_parent_name = "oir-circular-buffer"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('card_flag', (YLeaf(YType.int32, 'card-flag'), ['int'])),
                                                    ('card_type', (YLeaf(YType.int32, 'card-type'), ['int'])),
                                                    ('reg_flag', (YLeaf(YType.int32, 'reg-flag'), ['int'])),
                                                    ('evt_flag', (YLeaf(YType.int32, 'evt-flag'), ['int'])),
                                                    ('rack_num', (YLeaf(YType.int32, 'rack-num'), ['int'])),
                                                    ('instance', (YLeaf(YType.int32, 'instance'), ['int'])),
                                                    ('cur_card_state', (YLeaf(YType.int32, 'cur-card-state'), ['int'])),
                                                ])
                                                self.card_flag = None
                                                self.card_type = None
                                                self.reg_flag = None
                                                self.evt_flag = None
                                                self.rack_num = None
                                                self.instance = None
                                                self.cur_card_state = None
                                                self._segment_path = lambda: "fia-oir-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, [u'card_flag', u'card_type', u'reg_flag', u'evt_flag', u'rack_num', u'instance', u'cur_card_state'], name, value)


            class AsicStatistics(Entity):
                """
                FIA asic statistics information
                
                .. attribute:: statistics_asic_instances
                
                	Instance table for statistics
                	**type**\:  :py:class:`StatisticsAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2017-08-29'

                def __init__(self):
                    super(Fia.Nodes.Node.AsicStatistics, self).__init__()

                    self.yang_name = "asic-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-asic-instances", ("statistics_asic_instances", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances))])
                    self._leafs = OrderedDict()

                    self.statistics_asic_instances = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances()
                    self.statistics_asic_instances.parent = self
                    self._children_name_map["statistics_asic_instances"] = "statistics-asic-instances"
                    self._segment_path = lambda: "asic-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics, [], name, value)


                class StatisticsAsicInstances(Entity):
                    """
                    Instance table for statistics
                    
                    .. attribute:: statistics_asic_instance
                    
                    	Asic instance for statistics
                    	**type**\: list of  		 :py:class:`StatisticsAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2017-08-29'

                    def __init__(self):
                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances, self).__init__()

                        self.yang_name = "statistics-asic-instances"
                        self.yang_parent_name = "asic-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("statistics-asic-instance", ("statistics_asic_instance", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance))])
                        self._leafs = OrderedDict()

                        self.statistics_asic_instance = YList(self)
                        self._segment_path = lambda: "statistics-asic-instances"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances, [], name, value)


                    class StatisticsAsicInstance(Entity):
                        """
                        Asic instance for statistics
                        
                        .. attribute:: instance  (key)
                        
                        	Asic instance
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: pbc_statistics
                        
                        	Packet Byte Counter for a Asic
                        	**type**\:  :py:class:`PbcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics>`
                        
                        .. attribute:: fmac_statistics
                        
                        	Statistics of FMAC
                        	**type**\:  :py:class:`FmacStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2017-08-29'

                        def __init__(self):
                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance, self).__init__()

                            self.yang_name = "statistics-asic-instance"
                            self.yang_parent_name = "statistics-asic-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['instance']
                            self._child_classes = OrderedDict([("pbc-statistics", ("pbc_statistics", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics)), ("fmac-statistics", ("fmac_statistics", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics))])
                            self._leafs = OrderedDict([
                                ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                            ])
                            self.instance = None

                            self.pbc_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics()
                            self.pbc_statistics.parent = self
                            self._children_name_map["pbc_statistics"] = "pbc-statistics"

                            self.fmac_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics()
                            self.fmac_statistics.parent = self
                            self._children_name_map["fmac_statistics"] = "fmac-statistics"
                            self._segment_path = lambda: "statistics-asic-instance" + "[instance='" + str(self.instance) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance, ['instance'], name, value)


                        class PbcStatistics(Entity):
                            """
                            Packet Byte Counter for a Asic
                            
                            .. attribute:: pbc_stats
                            
                            	PBC stats bag
                            	**type**\:  :py:class:`PbcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics, self).__init__()

                                self.yang_name = "pbc-statistics"
                                self.yang_parent_name = "statistics-asic-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("pbc-stats", ("pbc_stats", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats))])
                                self._leafs = OrderedDict()

                                self.pbc_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats()
                                self.pbc_stats.parent = self
                                self._children_name_map["pbc_stats"] = "pbc-stats"
                                self._segment_path = lambda: "pbc-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics, [], name, value)


                            class PbcStats(Entity):
                                """
                                PBC stats bag
                                
                                .. attribute:: stats_info
                                
                                	stats info
                                	**type**\:  :py:class:`StatsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo>`
                                
                                .. attribute:: valid
                                
                                	valid
                                	**type**\: bool
                                
                                .. attribute:: rack_no
                                
                                	rack no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: slot_no
                                
                                	slot no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_instance
                                
                                	asic instance
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chip_ver
                                
                                	chip ver
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, self).__init__()

                                    self.yang_name = "pbc-stats"
                                    self.yang_parent_name = "pbc-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stats-info", ("stats_info", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo))])
                                    self._leafs = OrderedDict([
                                        ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                        ('rack_no', (YLeaf(YType.uint32, 'rack-no'), ['int'])),
                                        ('slot_no', (YLeaf(YType.uint32, 'slot-no'), ['int'])),
                                        ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                        ('chip_ver', (YLeaf(YType.uint16, 'chip-ver'), ['int'])),
                                    ])
                                    self.valid = None
                                    self.rack_no = None
                                    self.slot_no = None
                                    self.asic_instance = None
                                    self.chip_ver = None

                                    self.stats_info = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo()
                                    self.stats_info.parent = self
                                    self._children_name_map["stats_info"] = "stats-info"
                                    self._segment_path = lambda: "pbc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, [u'valid', u'rack_no', u'slot_no', u'asic_instance', u'chip_ver'], name, value)


                                class StatsInfo(Entity):
                                    """
                                    stats info
                                    
                                    .. attribute:: num_blocks
                                    
                                    	Num Blocks
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: block_info
                                    
                                    	block info
                                    	**type**\: list of  		 :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo, self).__init__()

                                        self.yang_name = "stats-info"
                                        self.yang_parent_name = "pbc-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("block-info", ("block_info", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo))])
                                        self._leafs = OrderedDict([
                                            ('num_blocks', (YLeaf(YType.uint8, 'num-blocks'), ['int'])),
                                        ])
                                        self.num_blocks = None

                                        self.block_info = YList(self)
                                        self._segment_path = lambda: "stats-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo, [u'num_blocks'], name, value)


                                    class BlockInfo(Entity):
                                        """
                                        block info
                                        
                                        .. attribute:: block_name
                                        
                                        	Block Name
                                        	**type**\: str
                                        
                                        	**length:** 0..10
                                        
                                        .. attribute:: num_fields
                                        
                                        	Num Fields
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: field_info
                                        
                                        	field info
                                        	**type**\: list of  		 :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo, self).__init__()

                                            self.yang_name = "block-info"
                                            self.yang_parent_name = "stats-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("field-info", ("field_info", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo))])
                                            self._leafs = OrderedDict([
                                                ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                                ('num_fields', (YLeaf(YType.uint8, 'num-fields'), ['int'])),
                                            ])
                                            self.block_name = None
                                            self.num_fields = None

                                            self.field_info = YList(self)
                                            self._segment_path = lambda: "block-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo, [u'block_name', u'num_fields'], name, value)


                                        class FieldInfo(Entity):
                                            """
                                            field info
                                            
                                            .. attribute:: field_name
                                            
                                            	Field Name
                                            	**type**\: str
                                            
                                            	**length:** 0..80
                                            
                                            .. attribute:: field_value
                                            
                                            	Field Value
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: is_ovf
                                            
                                            	Is Ovf
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo, self).__init__()

                                                self.yang_name = "field-info"
                                                self.yang_parent_name = "block-info"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('field_name', (YLeaf(YType.str, 'field-name'), ['str'])),
                                                    ('field_value', (YLeaf(YType.uint64, 'field-value'), ['int'])),
                                                    ('is_ovf', (YLeaf(YType.boolean, 'is-ovf'), ['bool'])),
                                                ])
                                                self.field_name = None
                                                self.field_value = None
                                                self.is_ovf = None
                                                self._segment_path = lambda: "field-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo, [u'field_name', u'field_value', u'is_ovf'], name, value)


                        class FmacStatistics(Entity):
                            """
                            Statistics of FMAC
                            
                            .. attribute:: fmac_links
                            
                            	Link table for statistics
                            	**type**\:  :py:class:`FmacLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2017-08-29'

                            def __init__(self):
                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics, self).__init__()

                                self.yang_name = "fmac-statistics"
                                self.yang_parent_name = "statistics-asic-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("fmac-links", ("fmac_links", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks))])
                                self._leafs = OrderedDict()

                                self.fmac_links = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks()
                                self.fmac_links.parent = self
                                self._children_name_map["fmac_links"] = "fmac-links"
                                self._segment_path = lambda: "fmac-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics, [], name, value)


                            class FmacLinks(Entity):
                                """
                                Link table for statistics
                                
                                .. attribute:: fmac_link
                                
                                	Link number for statistics
                                	**type**\: list of  		 :py:class:`FmacLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2017-08-29'

                                def __init__(self):
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks, self).__init__()

                                    self.yang_name = "fmac-links"
                                    self.yang_parent_name = "fmac-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("fmac-link", ("fmac_link", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink))])
                                    self._leafs = OrderedDict()

                                    self.fmac_link = YList(self)
                                    self._segment_path = lambda: "fmac-links"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks, [], name, value)


                                class FmacLink(Entity):
                                    """
                                    Link number for statistics
                                    
                                    .. attribute:: link  (key)
                                    
                                    	Link number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: fmac_asic
                                    
                                    	Single aisc information
                                    	**type**\: list of  		 :py:class:`FmacAsic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink, self).__init__()

                                        self.yang_name = "fmac-link"
                                        self.yang_parent_name = "fmac-links"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['link']
                                        self._child_classes = OrderedDict([("fmac-asic", ("fmac_asic", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic))])
                                        self._leafs = OrderedDict([
                                            ('link', (YLeaf(YType.uint32, 'link'), ['int'])),
                                        ])
                                        self.link = None

                                        self.fmac_asic = YList(self)
                                        self._segment_path = lambda: "fmac-link" + "[link='" + str(self.link) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink, ['link'], name, value)


                                    class FmacAsic(Entity):
                                        """
                                        Single aisc information
                                        
                                        .. attribute:: asic  (key)
                                        
                                        	Single asic
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: aggr_stats
                                        
                                        	aggr stats
                                        	**type**\:  :py:class:`AggrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats>`
                                        
                                        .. attribute:: incr_stats
                                        
                                        	incr stats
                                        	**type**\:  :py:class:`IncrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats>`
                                        
                                        .. attribute:: valid
                                        
                                        	valid
                                        	**type**\: bool
                                        
                                        .. attribute:: rack_no
                                        
                                        	rack no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: slot_no
                                        
                                        	slot no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: link_no
                                        
                                        	link no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: link_valid
                                        
                                        	link valid
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, self).__init__()

                                            self.yang_name = "fmac-asic"
                                            self.yang_parent_name = "fmac-link"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['asic']
                                            self._child_classes = OrderedDict([("aggr-stats", ("aggr_stats", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats)), ("incr-stats", ("incr_stats", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats))])
                                            self._leafs = OrderedDict([
                                                ('asic', (YLeaf(YType.uint32, 'asic'), ['int'])),
                                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                                ('rack_no', (YLeaf(YType.uint32, 'rack-no'), ['int'])),
                                                ('slot_no', (YLeaf(YType.uint32, 'slot-no'), ['int'])),
                                                ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                                ('link_no', (YLeaf(YType.uint32, 'link-no'), ['int'])),
                                                ('link_valid', (YLeaf(YType.boolean, 'link-valid'), ['bool'])),
                                            ])
                                            self.asic = None
                                            self.valid = None
                                            self.rack_no = None
                                            self.slot_no = None
                                            self.asic_instance = None
                                            self.link_no = None
                                            self.link_valid = None

                                            self.aggr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats()
                                            self.aggr_stats.parent = self
                                            self._children_name_map["aggr_stats"] = "aggr-stats"

                                            self.incr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats()
                                            self.incr_stats.parent = self
                                            self._children_name_map["incr_stats"] = "incr-stats"
                                            self._segment_path = lambda: "fmac-asic" + "[asic='" + str(self.asic) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, ['asic', u'valid', u'rack_no', u'slot_no', u'asic_instance', u'link_no', u'link_valid'], name, value)


                                        class AggrStats(Entity):
                                            """
                                            aggr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:  :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:  :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:  :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats, self).__init__()

                                                self.yang_name = "aggr-stats"
                                                self.yang_parent_name = "fmac-asic"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("link-error-status", ("link_error_status", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus)), ("link-counters", ("link_counters", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters)), ("ovf-status", ("ovf_status", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus))])
                                                self._leafs = OrderedDict()

                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self._children_name_map["link_error_status"] = "link-error-status"

                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self._children_name_map["link_counters"] = "link-counters"

                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus()
                                                self.ovf_status.parent = self
                                                self._children_name_map["ovf_status"] = "ovf-status"
                                                self._segment_path = lambda: "aggr-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats, [], name, value)


                                            class LinkErrorStatus(Entity):
                                                """
                                                link error status
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, self).__init__()

                                                    self.yang_name = "link-error-status"
                                                    self.yang_parent_name = "aggr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('link_crc_error', (YLeaf(YType.uint32, 'link-crc-error'), ['int'])),
                                                        ('link_size_error', (YLeaf(YType.uint32, 'link-size-error'), ['int'])),
                                                        ('link_mis_align_error', (YLeaf(YType.uint32, 'link-mis-align-error'), ['int'])),
                                                        ('link_code_group_error', (YLeaf(YType.uint32, 'link-code-group-error'), ['int'])),
                                                        ('link_no_sig_lock_error', (YLeaf(YType.uint32, 'link-no-sig-lock-error'), ['int'])),
                                                        ('link_no_sig_accept_error', (YLeaf(YType.uint32, 'link-no-sig-accept-error'), ['int'])),
                                                        ('link_tokens_error', (YLeaf(YType.uint32, 'link-tokens-error'), ['int'])),
                                                        ('error_token_count', (YLeaf(YType.uint32, 'error-token-count'), ['int'])),
                                                    ])
                                                    self.link_crc_error = None
                                                    self.link_size_error = None
                                                    self.link_mis_align_error = None
                                                    self.link_code_group_error = None
                                                    self.link_no_sig_lock_error = None
                                                    self.link_no_sig_accept_error = None
                                                    self.link_tokens_error = None
                                                    self.error_token_count = None
                                                    self._segment_path = lambda: "link-error-status"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, [u'link_crc_error', u'link_size_error', u'link_mis_align_error', u'link_code_group_error', u'link_no_sig_lock_error', u'link_no_sig_accept_error', u'link_tokens_error', u'error_token_count'], name, value)


                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, self).__init__()

                                                    self.yang_name = "link-counters"
                                                    self.yang_parent_name = "aggr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tx_control_cells_counter', (YLeaf(YType.uint64, 'tx-control-cells-counter'), ['int'])),
                                                        ('tx_data_cell_counter', (YLeaf(YType.uint64, 'tx-data-cell-counter'), ['int'])),
                                                        ('tx_data_byte_counter', (YLeaf(YType.uint64, 'tx-data-byte-counter'), ['int'])),
                                                        ('rx_crc_errors_counter', (YLeaf(YType.uint64, 'rx-crc-errors-counter'), ['int'])),
                                                        ('rx_lfec_fec_correctable_error', (YLeaf(YType.uint64, 'rx-lfec-fec-correctable-error'), ['int'])),
                                                        ('rx_8b_10b_disparity_errors', (YLeaf(YType.uint64, 'rx-8b-10b-disparity-errors'), ['int'])),
                                                        ('rx_control_cells_counter', (YLeaf(YType.uint64, 'rx-control-cells-counter'), ['int'])),
                                                        ('rx_data_cell_counter', (YLeaf(YType.uint64, 'rx-data-cell-counter'), ['int'])),
                                                        ('rx_data_byte_counter', (YLeaf(YType.uint64, 'rx-data-byte-counter'), ['int'])),
                                                        ('rx_dropped_retransmitted_control', (YLeaf(YType.uint64, 'rx-dropped-retransmitted-control'), ['int'])),
                                                        ('tx_asyn_fifo_rate', (YLeaf(YType.uint64, 'tx-asyn-fifo-rate'), ['int'])),
                                                        ('rx_asyn_fifo_rate', (YLeaf(YType.uint64, 'rx-asyn-fifo-rate'), ['int'])),
                                                        ('rx_lfec_fec_uncorrectable_errors', (YLeaf(YType.uint64, 'rx-lfec-fec-uncorrectable-errors'), ['int'])),
                                                        ('rx_8b_10b_code_errors', (YLeaf(YType.uint64, 'rx-8b-10b-code-errors'), ['int'])),
                                                    ])
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None
                                                    self._segment_path = lambda: "link-counters"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, [u'tx_control_cells_counter', u'tx_data_cell_counter', u'tx_data_byte_counter', u'rx_crc_errors_counter', u'rx_lfec_fec_correctable_error', u'rx_8b_10b_disparity_errors', u'rx_control_cells_counter', u'rx_data_cell_counter', u'rx_data_byte_counter', u'rx_dropped_retransmitted_control', u'tx_asyn_fifo_rate', u'rx_asyn_fifo_rate', u'rx_lfec_fec_uncorrectable_errors', u'rx_8b_10b_code_errors'], name, value)


                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, self).__init__()

                                                    self.yang_name = "ovf-status"
                                                    self.yang_parent_name = "aggr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tx_control_cells_counter', (YLeaf(YType.str, 'tx-control-cells-counter'), ['str'])),
                                                        ('tx_data_cell_counter', (YLeaf(YType.str, 'tx-data-cell-counter'), ['str'])),
                                                        ('tx_data_byte_counter', (YLeaf(YType.str, 'tx-data-byte-counter'), ['str'])),
                                                        ('rx_crc_errors_counter', (YLeaf(YType.str, 'rx-crc-errors-counter'), ['str'])),
                                                        ('rx_lfec_fec_correctable_error', (YLeaf(YType.str, 'rx-lfec-fec-correctable-error'), ['str'])),
                                                        ('rx_8b_10b_disparity_errors', (YLeaf(YType.str, 'rx-8b-10b-disparity-errors'), ['str'])),
                                                        ('rx_control_cells_counter', (YLeaf(YType.str, 'rx-control-cells-counter'), ['str'])),
                                                        ('rx_data_cell_counter', (YLeaf(YType.str, 'rx-data-cell-counter'), ['str'])),
                                                        ('rx_data_byte_counter', (YLeaf(YType.str, 'rx-data-byte-counter'), ['str'])),
                                                        ('rx_dropped_retransmitted_control', (YLeaf(YType.str, 'rx-dropped-retransmitted-control'), ['str'])),
                                                        ('tx_asyn_fifo_rate', (YLeaf(YType.str, 'tx-asyn-fifo-rate'), ['str'])),
                                                        ('rx_asyn_fifo_rate', (YLeaf(YType.str, 'rx-asyn-fifo-rate'), ['str'])),
                                                        ('rx_lfec_fec_uncorrectable_errors', (YLeaf(YType.str, 'rx-lfec-fec-uncorrectable-errors'), ['str'])),
                                                        ('rx_8b_10b_code_errors', (YLeaf(YType.str, 'rx-8b-10b-code-errors'), ['str'])),
                                                    ])
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None
                                                    self._segment_path = lambda: "ovf-status"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, [u'tx_control_cells_counter', u'tx_data_cell_counter', u'tx_data_byte_counter', u'rx_crc_errors_counter', u'rx_lfec_fec_correctable_error', u'rx_8b_10b_disparity_errors', u'rx_control_cells_counter', u'rx_data_cell_counter', u'rx_data_byte_counter', u'rx_dropped_retransmitted_control', u'tx_asyn_fifo_rate', u'rx_asyn_fifo_rate', u'rx_lfec_fec_uncorrectable_errors', u'rx_8b_10b_code_errors'], name, value)


                                        class IncrStats(Entity):
                                            """
                                            incr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:  :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:  :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:  :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2017-08-29'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats, self).__init__()

                                                self.yang_name = "incr-stats"
                                                self.yang_parent_name = "fmac-asic"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("link-error-status", ("link_error_status", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus)), ("link-counters", ("link_counters", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters)), ("ovf-status", ("ovf_status", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus))])
                                                self._leafs = OrderedDict()

                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self._children_name_map["link_error_status"] = "link-error-status"

                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self._children_name_map["link_counters"] = "link-counters"

                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus()
                                                self.ovf_status.parent = self
                                                self._children_name_map["ovf_status"] = "ovf-status"
                                                self._segment_path = lambda: "incr-stats"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats, [], name, value)


                                            class LinkErrorStatus(Entity):
                                                """
                                                link error status
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, self).__init__()

                                                    self.yang_name = "link-error-status"
                                                    self.yang_parent_name = "incr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('link_crc_error', (YLeaf(YType.uint32, 'link-crc-error'), ['int'])),
                                                        ('link_size_error', (YLeaf(YType.uint32, 'link-size-error'), ['int'])),
                                                        ('link_mis_align_error', (YLeaf(YType.uint32, 'link-mis-align-error'), ['int'])),
                                                        ('link_code_group_error', (YLeaf(YType.uint32, 'link-code-group-error'), ['int'])),
                                                        ('link_no_sig_lock_error', (YLeaf(YType.uint32, 'link-no-sig-lock-error'), ['int'])),
                                                        ('link_no_sig_accept_error', (YLeaf(YType.uint32, 'link-no-sig-accept-error'), ['int'])),
                                                        ('link_tokens_error', (YLeaf(YType.uint32, 'link-tokens-error'), ['int'])),
                                                        ('error_token_count', (YLeaf(YType.uint32, 'error-token-count'), ['int'])),
                                                    ])
                                                    self.link_crc_error = None
                                                    self.link_size_error = None
                                                    self.link_mis_align_error = None
                                                    self.link_code_group_error = None
                                                    self.link_no_sig_lock_error = None
                                                    self.link_no_sig_accept_error = None
                                                    self.link_tokens_error = None
                                                    self.error_token_count = None
                                                    self._segment_path = lambda: "link-error-status"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, [u'link_crc_error', u'link_size_error', u'link_mis_align_error', u'link_code_group_error', u'link_no_sig_lock_error', u'link_no_sig_accept_error', u'link_tokens_error', u'error_token_count'], name, value)


                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, self).__init__()

                                                    self.yang_name = "link-counters"
                                                    self.yang_parent_name = "incr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tx_control_cells_counter', (YLeaf(YType.uint64, 'tx-control-cells-counter'), ['int'])),
                                                        ('tx_data_cell_counter', (YLeaf(YType.uint64, 'tx-data-cell-counter'), ['int'])),
                                                        ('tx_data_byte_counter', (YLeaf(YType.uint64, 'tx-data-byte-counter'), ['int'])),
                                                        ('rx_crc_errors_counter', (YLeaf(YType.uint64, 'rx-crc-errors-counter'), ['int'])),
                                                        ('rx_lfec_fec_correctable_error', (YLeaf(YType.uint64, 'rx-lfec-fec-correctable-error'), ['int'])),
                                                        ('rx_8b_10b_disparity_errors', (YLeaf(YType.uint64, 'rx-8b-10b-disparity-errors'), ['int'])),
                                                        ('rx_control_cells_counter', (YLeaf(YType.uint64, 'rx-control-cells-counter'), ['int'])),
                                                        ('rx_data_cell_counter', (YLeaf(YType.uint64, 'rx-data-cell-counter'), ['int'])),
                                                        ('rx_data_byte_counter', (YLeaf(YType.uint64, 'rx-data-byte-counter'), ['int'])),
                                                        ('rx_dropped_retransmitted_control', (YLeaf(YType.uint64, 'rx-dropped-retransmitted-control'), ['int'])),
                                                        ('tx_asyn_fifo_rate', (YLeaf(YType.uint64, 'tx-asyn-fifo-rate'), ['int'])),
                                                        ('rx_asyn_fifo_rate', (YLeaf(YType.uint64, 'rx-asyn-fifo-rate'), ['int'])),
                                                        ('rx_lfec_fec_uncorrectable_errors', (YLeaf(YType.uint64, 'rx-lfec-fec-uncorrectable-errors'), ['int'])),
                                                        ('rx_8b_10b_code_errors', (YLeaf(YType.uint64, 'rx-8b-10b-code-errors'), ['int'])),
                                                    ])
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None
                                                    self._segment_path = lambda: "link-counters"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, [u'tx_control_cells_counter', u'tx_data_cell_counter', u'tx_data_byte_counter', u'rx_crc_errors_counter', u'rx_lfec_fec_correctable_error', u'rx_8b_10b_disparity_errors', u'rx_control_cells_counter', u'rx_data_cell_counter', u'rx_data_byte_counter', u'rx_dropped_retransmitted_control', u'tx_asyn_fifo_rate', u'rx_asyn_fifo_rate', u'rx_lfec_fec_uncorrectable_errors', u'rx_8b_10b_code_errors'], name, value)


                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2017-08-29'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, self).__init__()

                                                    self.yang_name = "ovf-status"
                                                    self.yang_parent_name = "incr-stats"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('tx_control_cells_counter', (YLeaf(YType.str, 'tx-control-cells-counter'), ['str'])),
                                                        ('tx_data_cell_counter', (YLeaf(YType.str, 'tx-data-cell-counter'), ['str'])),
                                                        ('tx_data_byte_counter', (YLeaf(YType.str, 'tx-data-byte-counter'), ['str'])),
                                                        ('rx_crc_errors_counter', (YLeaf(YType.str, 'rx-crc-errors-counter'), ['str'])),
                                                        ('rx_lfec_fec_correctable_error', (YLeaf(YType.str, 'rx-lfec-fec-correctable-error'), ['str'])),
                                                        ('rx_8b_10b_disparity_errors', (YLeaf(YType.str, 'rx-8b-10b-disparity-errors'), ['str'])),
                                                        ('rx_control_cells_counter', (YLeaf(YType.str, 'rx-control-cells-counter'), ['str'])),
                                                        ('rx_data_cell_counter', (YLeaf(YType.str, 'rx-data-cell-counter'), ['str'])),
                                                        ('rx_data_byte_counter', (YLeaf(YType.str, 'rx-data-byte-counter'), ['str'])),
                                                        ('rx_dropped_retransmitted_control', (YLeaf(YType.str, 'rx-dropped-retransmitted-control'), ['str'])),
                                                        ('tx_asyn_fifo_rate', (YLeaf(YType.str, 'tx-asyn-fifo-rate'), ['str'])),
                                                        ('rx_asyn_fifo_rate', (YLeaf(YType.str, 'rx-asyn-fifo-rate'), ['str'])),
                                                        ('rx_lfec_fec_uncorrectable_errors', (YLeaf(YType.str, 'rx-lfec-fec-uncorrectable-errors'), ['str'])),
                                                        ('rx_8b_10b_code_errors', (YLeaf(YType.str, 'rx-8b-10b-code-errors'), ['str'])),
                                                    ])
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None
                                                    self._segment_path = lambda: "ovf-status"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, [u'tx_control_cells_counter', u'tx_data_cell_counter', u'tx_data_byte_counter', u'rx_crc_errors_counter', u'rx_lfec_fec_correctable_error', u'rx_8b_10b_disparity_errors', u'rx_control_cells_counter', u'rx_data_cell_counter', u'rx_data_byte_counter', u'rx_dropped_retransmitted_control', u'tx_asyn_fifo_rate', u'rx_asyn_fifo_rate', u'rx_lfec_fec_uncorrectable_errors', u'rx_8b_10b_code_errors'], name, value)

    def clone_ptr(self):
        self._top_entity = Fia()
        return self._top_entity

