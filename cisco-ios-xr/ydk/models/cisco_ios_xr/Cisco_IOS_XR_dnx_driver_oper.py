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
    
    	**config**\: False
    
    

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
        
        	**config**\: False
        
        

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
            
            	**config**\: False
            
            .. attribute:: rx_link_information
            
            	FIA link rx information
            	**type**\:  :py:class:`RxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation>`
            
            	**config**\: False
            
            .. attribute:: driver_information
            
            	FIA driver information
            	**type**\:  :py:class:`DriverInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation>`
            
            	**config**\: False
            
            .. attribute:: clear_statistics
            
            	Clear statistics information
            	**type**\:  :py:class:`ClearStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics>`
            
            	**config**\: False
            
            .. attribute:: tx_link_information
            
            	FIA link TX information
            	**type**\:  :py:class:`TxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation>`
            
            	**config**\: False
            
            .. attribute:: diag_shell
            
            	FIA diag shell information
            	**type**\:  :py:class:`DiagShell <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell>`
            
            	**config**\: False
            
            .. attribute:: oir_history
            
            	FIA operational data of oir history
            	**type**\:  :py:class:`OirHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory>`
            
            	**config**\: False
            
            .. attribute:: asic_statistics
            
            	FIA asic statistics information
            	**type**\:  :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics>`
            
            	**config**\: False
            
            

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
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        .. attribute:: rx_asic_instances
                        
                        	Instance table for rx information
                        	**type**\:  :py:class:`RxAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances>`
                        
                        	**config**\: False
                        
                        

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
                            
                            	**config**\: False
                            
                            

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
                                
                                	**config**\: False
                                
                                .. attribute:: rx_links
                                
                                	Link table class for rx information
                                	**type**\:  :py:class:`RxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks>`
                                
                                	**config**\: False
                                
                                

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
                                    
                                    	**config**\: False
                                    
                                    

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
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: status_option
                                        
                                        	RX link status option
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: rx_link
                                        
                                        	Single link information
                                        	**type**\: list of  		 :py:class:`RxLink_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_>`
                                        
                                        	**config**\: False
                                        
                                        

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
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:  :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:  :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: far_end_link_in_hw
                                            
                                            	far end link in hw
                                            	**type**\:  :py:class:`FarEndLinkInHw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stage
                                            
                                            	Stage
                                            	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: flags
                                            
                                            	flags
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: flap_cnt
                                            
                                            	flap cnt
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: correctable_errors
                                            
                                            	correctable errors
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: uncorrectable_errors
                                            
                                            	uncorrectable errors
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            

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
                                                self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_, ['link', 'speed', 'stage', 'is_link_valid', 'is_conf_pending', 'admin_state', 'oper_state', 'error_state', 'flags', 'flap_cnt', 'num_admin_shuts', 'correctable_errors', 'uncorrectable_errors'], name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink, ['link_type', 'link_stage', 'link_num', 'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink, ['link_type', 'link_stage', 'link_num', 'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                            class FarEndLinkInHw(Entity):
                                                """
                                                far end link in hw
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw, ['link_type', 'link_stage', 'link_num', 'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of  		 :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist>`
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History, ['histnum', 'start_index'], name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist, ['admin_state', 'oper_state', 'error_state', 'timestamp', 'reasons'], name, value)












            class DriverInformation(Entity):
                """
                FIA driver information
                
                .. attribute:: drv_version
                
                	drv version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: coeff_major_rev
                
                	coeff major rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: coeff_minor_rev
                
                	coeff minor rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: functional_role
                
                	functional role
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: issu_role
                
                	issu role
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: node_id
                
                	node id
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rack_type
                
                	rack type
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**config**\: False
                
                .. attribute:: rack_num
                
                	rack num
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: is_driver_ready
                
                	is driver ready
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: card_avail_mask
                
                	card avail mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: asic_avail_mask
                
                	asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: exp_asic_avail_mask
                
                	exp asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: ucmc_ratio
                
                	ucmc ratio
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                
                	asic oper notify to fsdb pending bmap
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: is_full_fgid_download_req
                
                	is full fgid download req
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_fgid_download_in_progress
                
                	is fgid download in progress
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_fgid_download_completed
                
                	is fgid download completed
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fsdb_conn_active
                
                	fsdb conn active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fgid_conn_active
                
                	fgid conn active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_mgr_conn_active
                
                	issu mgr conn active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fsdb_reg_active
                
                	fsdb reg active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fgid_reg_active
                
                	fgid reg active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_mgr_reg_active
                
                	issu mgr reg active
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: num_pm_conn_reqs
                
                	num pm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_fsdb_conn_reqs
                
                	num fsdb conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_fgid_conn_reqs
                
                	num fgid conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_fstats_conn_reqs
                
                	num fstats conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_cm_conn_reqs
                
                	num cm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_issu_mgr_conn_reqs
                
                	num issu mgr conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: num_peer_fia_conn_reqs
                
                	num peer fia conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: is_gaspp_registered
                
                	is gaspp registered
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_cih_registered
                
                	is cih registered
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: drvr_initial_startup_timestamp
                
                	drvr initial startup timestamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: drvr_current_startup_timestamp
                
                	drvr current startup timestamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: num_intf_ports
                
                	num intf ports
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: uc_weight
                
                	uc weight
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: respawn_count
                
                	respawn count
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: total_asics
                
                	total asics
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: issu_ready_ntfy_pending
                
                	issu ready ntfy pending
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_abort_sent
                
                	issu abort sent
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_abort_rcvd
                
                	issu abort rcvd
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fabric_mode
                
                	fabric mode
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: fc_mode
                
                	FC Mode
                	**type**\:  :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                
                	**config**\: False
                
                .. attribute:: board_rev_id
                
                	board rev id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: all_wb_insync
                
                	all wb insync
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: all_wb_insync_since
                
                	all wb insync since
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: all_startup_wb_insync
                
                	all startup wb insync
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: plane_a_bitmap
                
                	planeA bitmap
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: plane_b_bitmap
                
                	planeB bitmap
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: device_info
                
                	device info
                	**type**\: list of  		 :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo>`
                
                	**config**\: False
                
                .. attribute:: card_info
                
                	card info
                	**type**\: list of  		 :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo>`
                
                	**config**\: False
                
                

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
                    self._perform_setattr(Fia.Nodes.Node.DriverInformation, ['drv_version', 'coeff_major_rev', 'coeff_minor_rev', 'functional_role', 'issu_role', 'node_id', 'rack_type', 'rack_num', 'is_driver_ready', 'card_avail_mask', 'asic_avail_mask', 'exp_asic_avail_mask', 'ucmc_ratio', 'asic_oper_notify_to_fsdb_pending_bmap', 'is_full_fgid_download_req', 'is_fgid_download_in_progress', 'is_fgid_download_completed', 'fsdb_conn_active', 'fgid_conn_active', 'issu_mgr_conn_active', 'fsdb_reg_active', 'fgid_reg_active', 'issu_mgr_reg_active', 'num_pm_conn_reqs', 'num_fsdb_conn_reqs', 'num_fgid_conn_reqs', 'num_fstats_conn_reqs', 'num_cm_conn_reqs', 'num_issu_mgr_conn_reqs', 'num_peer_fia_conn_reqs', 'is_gaspp_registered', 'is_cih_registered', 'drvr_initial_startup_timestamp', 'drvr_current_startup_timestamp', 'num_intf_ports', 'uc_weight', 'respawn_count', 'total_asics', 'issu_ready_ntfy_pending', 'issu_abort_sent', 'issu_abort_rcvd', 'fabric_mode', 'fc_mode', 'board_rev_id', 'all_wb_insync', 'all_wb_insync_since', 'all_startup_wb_insync', 'plane_a_bitmap', 'plane_b_bitmap'], name, value)


                class DeviceInfo(Entity):
                    """
                    device info
                    
                    .. attribute:: asic_id
                    
                    	asic id
                    	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_valid
                    
                    	is valid
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: fapid
                    
                    	fapid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: hotplug_event
                    
                    	hotplug event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: slice_state
                    
                    	Slice State
                    	**type**\:  :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: admin_state
                    
                    	Admin State
                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                    
                    	**config**\: False
                    
                    .. attribute:: oper_state
                    
                    	Oper State
                    	**type**\:  :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                    
                    	**config**\: False
                    
                    .. attribute:: asic_state
                    
                    	Asic State
                    	**type**\:  :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_init_cause
                    
                    	last init cause
                    	**type**\:  :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                    
                    	**config**\: False
                    
                    .. attribute:: num_pon_resets
                    
                    	num pon resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: num_hard_resets
                    
                    	num hard resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_switch_state
                    
                    	local switch state
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: startup_wb_mtime_str
                    
                    	startup wb mtime str
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: startup_wb_outof_sync
                    
                    	startup wb outof sync
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: local_wb_sync_end_str
                    
                    	local wb sync end str
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_wb_sync_end_str
                    
                    	remote wb sync end str
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: local_wb_sync_pending
                    
                    	local wb sync pending
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: sdk_delay_msec
                    
                    	sdk delay msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

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
                        self._perform_setattr(Fia.Nodes.Node.DriverInformation.DeviceInfo, ['is_valid', 'fapid', 'hotplug_event', 'slice_state', 'admin_state', 'oper_state', 'asic_state', 'last_init_cause', 'num_pon_resets', 'num_hard_resets', 'local_switch_state', 'startup_wb_mtime_str', 'startup_wb_outof_sync', 'local_wb_sync_end_str', 'remote_wb_sync_end_str', 'local_wb_sync_pending', 'sdk_delay_msec'], name, value)


                    class AsicId(Entity):
                        """
                        asic id
                        
                        .. attribute:: rack_type
                        
                        	Rack Type
                        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                        
                        	**config**\: False
                        
                        .. attribute:: asic_type
                        
                        	Asic Type
                        	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                        
                        	**config**\: False
                        
                        .. attribute:: rack_num
                        
                        	rack num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: slot_num
                        
                        	slot num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: asic_instance
                        
                        	asic instance
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

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
                            self._perform_setattr(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                class CardInfo(Entity):
                    """
                    card info
                    
                    .. attribute:: oir_circular_buffer
                    
                    	oir circular buffer
                    	**type**\:  :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer>`
                    
                    	**config**\: False
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: card_name
                    
                    	card name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: slot_no
                    
                    	slot no
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: card_flag
                    
                    	card flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: evt_flag
                    
                    	evt flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: reg_flag
                    
                    	reg flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: instance
                    
                    	instance
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: card_state
                    
                    	card state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: exp_num_asics
                    
                    	exp num asics
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: exp_num_asics_per_fsdb
                    
                    	exp num asics per fsdb
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_powered
                    
                    	is powered
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: cxp_avail_bitmap
                    
                    	cxp avail bitmap
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: num_ilkns_per_asic
                    
                    	num ilkns per asic
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: num_local_ports_per_ilkn
                    
                    	num local ports per ilkn
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: num_cos_per_port
                    
                    	num cos per port
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

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
                        self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo, ['card_type', 'card_name', 'slot_no', 'card_flag', 'evt_flag', 'reg_flag', 'instance', 'card_state', 'exp_num_asics', 'exp_num_asics_per_fsdb', 'is_powered', 'cxp_avail_bitmap', 'num_ilkns_per_asic', 'num_local_ports_per_ilkn', 'num_cos_per_port'], name, value)


                    class OirCircularBuffer(Entity):
                        """
                        oir circular buffer
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: fia_oir_info
                        
                        	fia oir info
                        	**type**\: list of  		 :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo>`
                        
                        	**config**\: False
                        
                        

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
                            self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, ['count', 'start', 'end'], name, value)


                        class FiaOirInfo(Entity):
                            """
                            fia oir info
                            
                            .. attribute:: card_flag
                            
                            	card flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: card_type
                            
                            	card type
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: reg_flag
                            
                            	reg flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: evt_flag
                            
                            	evt flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: instance
                            
                            	instance
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: cur_card_state
                            
                            	cur card state
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

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
                                self._perform_setattr(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, ['card_flag', 'card_type', 'reg_flag', 'evt_flag', 'rack_num', 'instance', 'cur_card_state'], name, value)






            class ClearStatistics(Entity):
                """
                Clear statistics information
                
                .. attribute:: asic_instances
                
                	Instance table for clear statistics information
                	**type**\:  :py:class:`AsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances>`
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        .. attribute:: instance
                        
                        	Clear value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        

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
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        

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
                            
                            	**config**\: False
                            
                            

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
                                
                                	**config**\: False
                                
                                .. attribute:: tx_links
                                
                                	Link table for tx information
                                	**type**\:  :py:class:`TxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks>`
                                
                                	**config**\: False
                                
                                

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
                                    
                                    	**config**\: False
                                    
                                    

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
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..47
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: tx_link
                                        
                                        	Single link information
                                        	**type**\: list of  		 :py:class:`TxLink_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_>`
                                        
                                        	**config**\: False
                                        
                                        

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
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:  :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:  :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stats
                                            
                                            	stats
                                            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stage
                                            
                                            	stage
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_power_enabled
                                            
                                            	is power enabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: coeff1
                                            
                                            	coeff1
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: coeff2
                                            
                                            	coeff2
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

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
                                                self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_, ['link', 'speed', 'stage', 'is_link_valid', 'is_conf_pending', 'is_power_enabled', 'coeff1', 'coeff2', 'admin_state', 'oper_state', 'error_state', 'num_admin_shuts'], name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink, ['link_type', 'link_stage', 'link_num', 'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:  :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink, ['link_type', 'link_stage', 'link_num', 'phy_link_num'], name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                            class Stats(Entity):
                                                """
                                                stats
                                                
                                                .. attribute:: dummy
                                                
                                                	dummy
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats, ['dummy'], name, value)



                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of  		 :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist>`
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History, ['histnum', 'start_index'], name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:  :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    

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
                                                        self._perform_setattr(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist, ['admin_state', 'oper_state', 'error_state', 'timestamp', 'reasons'], name, value)












            class DiagShell(Entity):
                """
                FIA diag shell information
                
                .. attribute:: diag_shell_units
                
                	Unit table for diag shell
                	**type**\:  :py:class:`DiagShellUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits>`
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        .. attribute:: commands
                        
                        	Command table for diag shell
                        	**type**\:  :py:class:`Commands <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands>`
                        
                        	**config**\: False
                        
                        

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
                            
                            	**config**\: False
                            
                            

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
                                
                                	**config**\: False
                                
                                .. attribute:: output
                                
                                	Added to support datalist
                                	**type**\: list of  		 :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output>`
                                
                                	**config**\: False
                                
                                

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
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: output_xr
                                    
                                    	output xr
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._perform_setattr(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, ['output', 'output_xr'], name, value)








            class OirHistory(Entity):
                """
                FIA operational data of oir history
                
                .. attribute:: flags
                
                	Flag table for history
                	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags>`
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        .. attribute:: slots
                        
                        	Slot table for history
                        	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots>`
                        
                        	**config**\: False
                        
                        

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
                            
                            	**config**\: False
                            
                            

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
                                
                                	**config**\: False
                                
                                .. attribute:: drv_version
                                
                                	drv version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: coeff_major_rev
                                
                                	coeff major rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: coeff_minor_rev
                                
                                	coeff minor rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: functional_role
                                
                                	functional role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: issu_role
                                
                                	issu role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: node_id
                                
                                	node id
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: rack_type
                                
                                	rack type
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: rack_num
                                
                                	rack num
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: is_driver_ready
                                
                                	is driver ready
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: card_avail_mask
                                
                                	card avail mask
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: asic_avail_mask
                                
                                	asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: exp_asic_avail_mask
                                
                                	exp asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ucmc_ratio
                                
                                	ucmc ratio
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                                
                                	asic oper notify to fsdb pending bmap
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: is_full_fgid_download_req
                                
                                	is full fgid download req
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_fgid_download_in_progress
                                
                                	is fgid download in progress
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_fgid_download_completed
                                
                                	is fgid download completed
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: fsdb_conn_active
                                
                                	fsdb conn active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: fgid_conn_active
                                
                                	fgid conn active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: issu_mgr_conn_active
                                
                                	issu mgr conn active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: fsdb_reg_active
                                
                                	fsdb reg active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: fgid_reg_active
                                
                                	fgid reg active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: issu_mgr_reg_active
                                
                                	issu mgr reg active
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: num_pm_conn_reqs
                                
                                	num pm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_fsdb_conn_reqs
                                
                                	num fsdb conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_fgid_conn_reqs
                                
                                	num fgid conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_fstats_conn_reqs
                                
                                	num fstats conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_cm_conn_reqs
                                
                                	num cm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_issu_mgr_conn_reqs
                                
                                	num issu mgr conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: num_peer_fia_conn_reqs
                                
                                	num peer fia conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: is_gaspp_registered
                                
                                	is gaspp registered
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_cih_registered
                                
                                	is cih registered
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: drvr_initial_startup_timestamp
                                
                                	drvr initial startup timestamp
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: drvr_current_startup_timestamp
                                
                                	drvr current startup timestamp
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: num_intf_ports
                                
                                	num intf ports
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: uc_weight
                                
                                	uc weight
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: respawn_count
                                
                                	respawn count
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: total_asics
                                
                                	total asics
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: issu_ready_ntfy_pending
                                
                                	issu ready ntfy pending
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: issu_abort_sent
                                
                                	issu abort sent
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: issu_abort_rcvd
                                
                                	issu abort rcvd
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: fabric_mode
                                
                                	fabric mode
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: fc_mode
                                
                                	FC Mode
                                	**type**\:  :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                                
                                	**config**\: False
                                
                                .. attribute:: board_rev_id
                                
                                	board rev id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: all_wb_insync
                                
                                	all wb insync
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: all_wb_insync_since
                                
                                	all wb insync since
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: all_startup_wb_insync
                                
                                	all startup wb insync
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: plane_a_bitmap
                                
                                	planeA bitmap
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: plane_b_bitmap
                                
                                	planeB bitmap
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: device_info
                                
                                	device info
                                	**type**\: list of  		 :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo>`
                                
                                	**config**\: False
                                
                                .. attribute:: card_info
                                
                                	card info
                                	**type**\: list of  		 :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo>`
                                
                                	**config**\: False
                                
                                

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
                                    self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, ['slot', 'drv_version', 'coeff_major_rev', 'coeff_minor_rev', 'functional_role', 'issu_role', 'node_id', 'rack_type', 'rack_num', 'is_driver_ready', 'card_avail_mask', 'asic_avail_mask', 'exp_asic_avail_mask', 'ucmc_ratio', 'asic_oper_notify_to_fsdb_pending_bmap', 'is_full_fgid_download_req', 'is_fgid_download_in_progress', 'is_fgid_download_completed', 'fsdb_conn_active', 'fgid_conn_active', 'issu_mgr_conn_active', 'fsdb_reg_active', 'fgid_reg_active', 'issu_mgr_reg_active', 'num_pm_conn_reqs', 'num_fsdb_conn_reqs', 'num_fgid_conn_reqs', 'num_fstats_conn_reqs', 'num_cm_conn_reqs', 'num_issu_mgr_conn_reqs', 'num_peer_fia_conn_reqs', 'is_gaspp_registered', 'is_cih_registered', 'drvr_initial_startup_timestamp', 'drvr_current_startup_timestamp', 'num_intf_ports', 'uc_weight', 'respawn_count', 'total_asics', 'issu_ready_ntfy_pending', 'issu_abort_sent', 'issu_abort_rcvd', 'fabric_mode', 'fc_mode', 'board_rev_id', 'all_wb_insync', 'all_wb_insync_since', 'all_startup_wb_insync', 'plane_a_bitmap', 'plane_b_bitmap'], name, value)


                                class DeviceInfo(Entity):
                                    """
                                    device info
                                    
                                    .. attribute:: asic_id
                                    
                                    	asic id
                                    	**type**\:  :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_valid
                                    
                                    	is valid
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fapid
                                    
                                    	fapid
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hotplug_event
                                    
                                    	hotplug event
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slice_state
                                    
                                    	Slice State
                                    	**type**\:  :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: admin_state
                                    
                                    	Admin State
                                    	**type**\:  :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oper_state
                                    
                                    	Oper State
                                    	**type**\:  :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: asic_state
                                    
                                    	Asic State
                                    	**type**\:  :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_init_cause
                                    
                                    	last init cause
                                    	**type**\:  :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_pon_resets
                                    
                                    	num pon resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_hard_resets
                                    
                                    	num hard resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: local_switch_state
                                    
                                    	local switch state
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: startup_wb_mtime_str
                                    
                                    	startup wb mtime str
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: startup_wb_outof_sync
                                    
                                    	startup wb outof sync
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: local_wb_sync_end_str
                                    
                                    	local wb sync end str
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: remote_wb_sync_end_str
                                    
                                    	remote wb sync end str
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: local_wb_sync_pending
                                    
                                    	local wb sync pending
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sdk_delay_msec
                                    
                                    	sdk delay msec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, ['is_valid', 'fapid', 'hotplug_event', 'slice_state', 'admin_state', 'oper_state', 'asic_state', 'last_init_cause', 'num_pon_resets', 'num_hard_resets', 'local_switch_state', 'startup_wb_mtime_str', 'startup_wb_outof_sync', 'local_wb_sync_end_str', 'remote_wb_sync_end_str', 'local_wb_sync_pending', 'sdk_delay_msec'], name, value)


                                    class AsicId(Entity):
                                        """
                                        asic id
                                        
                                        .. attribute:: rack_type
                                        
                                        	Rack Type
                                        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: asic_type
                                        
                                        	Asic Type
                                        	**type**\:  :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: rack_num
                                        
                                        	rack num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: slot_num
                                        
                                        	slot num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

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
                                            self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, ['rack_type', 'asic_type', 'rack_num', 'slot_num', 'asic_instance'], name, value)




                                class CardInfo(Entity):
                                    """
                                    card info
                                    
                                    .. attribute:: oir_circular_buffer
                                    
                                    	oir circular buffer
                                    	**type**\:  :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: card_type
                                    
                                    	card type
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: card_name
                                    
                                    	card name
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slot_no
                                    
                                    	slot no
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: card_flag
                                    
                                    	card flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: evt_flag
                                    
                                    	evt flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: reg_flag
                                    
                                    	reg flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: instance
                                    
                                    	instance
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: card_state
                                    
                                    	card state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: exp_num_asics
                                    
                                    	exp num asics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: exp_num_asics_per_fsdb
                                    
                                    	exp num asics per fsdb
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_powered
                                    
                                    	is powered
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cxp_avail_bitmap
                                    
                                    	cxp avail bitmap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_ilkns_per_asic
                                    
                                    	num ilkns per asic
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_local_ports_per_ilkn
                                    
                                    	num local ports per ilkn
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_cos_per_port
                                    
                                    	num cos per port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, ['card_type', 'card_name', 'slot_no', 'card_flag', 'evt_flag', 'reg_flag', 'instance', 'card_state', 'exp_num_asics', 'exp_num_asics_per_fsdb', 'is_powered', 'cxp_avail_bitmap', 'num_ilkns_per_asic', 'num_local_ports_per_ilkn', 'num_cos_per_port'], name, value)


                                    class OirCircularBuffer(Entity):
                                        """
                                        oir circular buffer
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: start
                                        
                                        	start
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: end
                                        
                                        	end
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fia_oir_info
                                        
                                        	fia oir info
                                        	**type**\: list of  		 :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo>`
                                        
                                        	**config**\: False
                                        
                                        

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
                                            self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, ['count', 'start', 'end'], name, value)


                                        class FiaOirInfo(Entity):
                                            """
                                            fia oir info
                                            
                                            .. attribute:: card_flag
                                            
                                            	card flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: card_type
                                            
                                            	card type
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reg_flag
                                            
                                            	reg flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: evt_flag
                                            
                                            	evt flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: rack_num
                                            
                                            	rack num
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: instance
                                            
                                            	instance
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cur_card_state
                                            
                                            	cur card state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

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
                                                self._perform_setattr(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, ['card_flag', 'card_type', 'reg_flag', 'evt_flag', 'rack_num', 'instance', 'cur_card_state'], name, value)










            class AsicStatistics(Entity):
                """
                FIA asic statistics information
                
                .. attribute:: statistics_asic_instances
                
                	Instance table for statistics
                	**type**\:  :py:class:`StatisticsAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances>`
                
                	**config**\: False
                
                

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
                    
                    	**config**\: False
                    
                    

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
                        
                        	**config**\: False
                        
                        .. attribute:: pbc_statistics
                        
                        	Packet Byte Counter for a Asic
                        	**type**\:  :py:class:`PbcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics>`
                        
                        	**config**\: False
                        
                        .. attribute:: fmac_statistics
                        
                        	Statistics of FMAC
                        	**type**\:  :py:class:`FmacStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics>`
                        
                        	**config**\: False
                        
                        

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
                            
                            	**config**\: False
                            
                            

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
                                
                                .. attribute:: aggr_stats
                                
                                	aggr stats
                                	**type**\:  :py:class:`AggrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats>`
                                
                                	**config**\: False
                                
                                .. attribute:: ovf_status
                                
                                	ovf status
                                	**type**\:  :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.OvfStatus>`
                                
                                	**config**\: False
                                
                                .. attribute:: valid
                                
                                	valid
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rack_no
                                
                                	rack no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: slot_no
                                
                                	slot no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: asic_instance
                                
                                	asic instance
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: chip_ver
                                
                                	chip ver
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([("aggr-stats", ("aggr_stats", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats)), ("ovf-status", ("ovf_status", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.OvfStatus))])
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

                                    self.aggr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats()
                                    self.aggr_stats.parent = self
                                    self._children_name_map["aggr_stats"] = "aggr-stats"

                                    self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.OvfStatus()
                                    self.ovf_status.parent = self
                                    self._children_name_map["ovf_status"] = "ovf-status"
                                    self._segment_path = lambda: "pbc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, ['valid', 'rack_no', 'slot_no', 'asic_instance', 'chip_ver'], name, value)


                                class AggrStats(Entity):
                                    """
                                    aggr stats
                                    
                                    .. attribute:: rx_internal_error
                                    
                                    	RxInternalError
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rx_internal_drop
                                    
                                    	RxInternalDrop
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: tx_internal_error
                                    
                                    	TxInternalError
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: tx_internal_drop
                                    
                                    	TxInternalDrop
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cmic_cmc0_pkt_count_tx_pkt
                                    
                                    	CMIC Cmc0PktCountTxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cmic_cmc0_pkt_count_rx_pkt
                                    
                                    	CMIC Cmc0PktCountRxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_rx_bursts_err_cnt
                                    
                                    	NBI StatRxBurstsErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_ecc_1b_err_cnt
                                    
                                    	NBI Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_ecc_2b_err_cnt
                                    
                                    	NBI Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_parity_err_cnt
                                    
                                    	NBI ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn_crc32_err_cnt
                                    
                                    	NBI RxIlknCrc32ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_crc24_err_cnt
                                    
                                    	NBI RxIlkn0Crc24ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_burst_err_cnt
                                    
                                    	NBI RxIlkn0BurstErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_miss_sop_err_cnt
                                    
                                    	NBI RxIlkn0MissSopErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_miss_eop_err_cnt
                                    
                                    	NBI RxIlkn0MissEopErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_misaligned_cnt
                                    
                                    	NBI RxIlkn0MisalignedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_crc24_err_cnt
                                    
                                    	NBI RxIlkn1Crc24ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_burst_err_cnt
                                    
                                    	NBI RxIlkn1BurstErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_miss_sop_err_cnt
                                    
                                    	NBI RxIlkn1MissSopErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_miss_eop_err_cnt
                                    
                                    	NBI RxIlkn1MissEopErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_misaligned_cnt
                                    
                                    	NBI RxIlkn1MisalignedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_tx_ilkn1_flushed_bursts_cnt
                                    
                                    	NBI TxIlkn1FlushedBurstsCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_crc24_err_cnt
                                    
                                    	NBI RxIlkn0RetransCRC24ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_retry_err_cnt
                                    
                                    	NBI RxIlkn0RetransRetryErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wdog_err_cnt
                                    
                                    	NBI RxIlkn0RetransWdogErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt
                                    
                                    	NBI RxIlkn0RetransWrapAfterDiscErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt
                                    
                                    	NBI RxIlkn0RetransWrapB4DiscErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_reached_timeout_err_cnt
                                    
                                    	NBI RxIlkn0RetransReachedTimeoutErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_crc24_err_cnt
                                    
                                    	NBI RxIlkn1RetransCRC24ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_retry_err_cnt
                                    
                                    	NBI RxIlkn1RetransRetryErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wdog_err_cnt
                                    
                                    	NBI RxIlkn1RetransWdogErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt
                                    
                                    	NBI RxIlkn1RetransWrapAfterDiscErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt
                                    
                                    	NBI RxIlkn1RetransWrapB4DiscErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_reached_timeout_err_cnt
                                    
                                    	NBI RxIlkn1RetransReachedTimeoutErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_rx_frame_err_cnt
                                    
                                    	NBI StatRxFrameErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_frame_err_cnt
                                    
                                    	NBI StatTxFrameErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_elk_err_bursts_cnt
                                    
                                    	NBI RxElkErrBurstsCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_num_thrown_eops
                                    
                                    	NBI RxNumThrownEops
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_num_runts
                                    
                                    	NBI RxNumRunts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_tx_crc_err_bursts_cnt
                                    
                                    	NBI BistTxCrcErrBurstsCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_length_bursts_cnt
                                    
                                    	NBI BistRxErrLengthBurstsCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_burst_index_cnt
                                    
                                    	NBI BistRxErrBurstIndexCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_bct_cnt
                                    
                                    	NBI BistRxErrBctCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_data_cnt
                                    
                                    	NBI BistRxErrDataCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_in_crc_err_cnt
                                    
                                    	NBI BistRxErrInCrcErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_sob_cnt
                                    
                                    	NBI BistRxErrSobCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_bursts_cnt
                                    
                                    	NBI StatTxBurstsCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_total_leng_cnt
                                    
                                    	NBI StatTxTotalLengCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_total_tx_pkt_count
                                    
                                    	RXAUI TotalTxPktCount
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_total_rx_pkt_count
                                    
                                    	RXAUI TotalRxPktCount
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_bcast_pkt
                                    
                                    	RXAUI RxPktCountBcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_bcast_pkt
                                    
                                    	RXAUI TxPktCountBcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_mcast_pkt
                                    
                                    	RXAUI RxPktCountMcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_mcast_pkt
                                    
                                    	RXAUI TxPktCountMcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_ucast_pkt
                                    
                                    	RXAUI RxPktCountUcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_ucast_pkt
                                    
                                    	RXAUI TxPktCountUcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_err_drop_pkt_cnt
                                    
                                    	RXAUI RxErrDropPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_err_drop_pkt_cnt
                                    
                                    	RXAUI TxErrDropPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_byte_count_tx_pkt
                                    
                                    	RXAUI ByteCountTxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_byte_count_rx_pkt
                                    
                                    	RXAUI ByteCountRxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_dscrd_pkt_cnt
                                    
                                    	RXAUI RxDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_dscrd_pkt_cnt
                                    
                                    	RXAUI TxDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ire_nif_packet_counter
                                    
                                    	IRE NifPacketCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_total_rx_pkt_count
                                    
                                    	IL TotalRxPktCount
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_total_tx_pkt_count
                                    
                                    	IL TotalTxPktCount
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_err_drop_pkt_cnt
                                    
                                    	IL RxErrDropPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_err_drop_pkt_cnt
                                    
                                    	IL TxErrDropPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_byte_count_tx_pkt
                                    
                                    	IL ByteCountTxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_byte_count_rx_pkt
                                    
                                    	IL ByteCountRxPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_dscrd_pkt_cnt
                                    
                                    	IL RxDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_dscrd_pkt_cnt
                                    
                                    	IL TxDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_bcast_pkt
                                    
                                    	IL RxPktCountBcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_bcast_pkt
                                    
                                    	IL TxPktCountBcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_mcast_pkt
                                    
                                    	IL RxPktCountMcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_mcast_pkt
                                    
                                    	IL TxPktCountMcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_ucast_pkt
                                    
                                    	IL RxPktCountUcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_ucast_pkt
                                    
                                    	IL TxPktCountUcastPkt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_enq_pkt_cnt
                                    
                                    	IQM EnqPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_enq_byte_cnt
                                    
                                    	IQM EnqByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_pkt_cnt
                                    
                                    	IQM DeqPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_byte_cnt
                                    
                                    	IQM DeqByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_tot_dscrd_pkt_cnt
                                    
                                    	IQM TotDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_tot_dscrd_byte_cnt
                                    
                                    	IQM TotDscrdByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecc_1b_err_cnt
                                    
                                    	IQM Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecc_2b_err_cnt
                                    
                                    	IQM Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_parity_err_cnt
                                    
                                    	IQM ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_delete_pkt_cnt
                                    
                                    	IQM DeqDeletePktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecn_dscrd_msk_pkt_cnt
                                    
                                    	IQM EcnDscrdMskPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_q_tot_dscrd_pkt_cnt
                                    
                                    	IQM QTotDscrdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_q_deq_delete_pkt_cnt
                                    
                                    	IQM QDeqDeletePktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_db_pkt_cnt
                                    
                                    	IQM RjctDbPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_bdb_pkt_cnt
                                    
                                    	IQM RjctBdbPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_bdb_protct_pkt_cnt
                                    
                                    	IQM RjctBdbProtctPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_oc_bd_pkt_cnt
                                    
                                    	IQM RjctOcBdPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_sn_err_pkt_cnt
                                    
                                    	IQM RjctSnErrPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_mc_err_pkt_cnt
                                    
                                    	IQM RjctMcErrPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_rsrc_err_pkt_cnt
                                    
                                    	IQM RjctRsrcErrPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_qnvalid_err_pkt_cnt
                                    
                                    	IQM RjctQnvalidErrPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_cnm_pkt_cnt
                                    
                                    	IQM RjctCnmPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_dyn_space_pkt_cnt
                                    
                                    	IQM RjctDynSpacePktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_fdt_pkt_cnt
                                    
                                    	IPT FdtPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_ecc_1b_err_cnt
                                    
                                    	IPT Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_ecc_2b_err_cnt
                                    
                                    	IPT Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_parity_err_cnt
                                    
                                    	IPT ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_cnt
                                    
                                    	IPT CrcErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_del_buff_cnt
                                    
                                    	IPT CrcErrDelBuffCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_cpu_del_buff_cnt
                                    
                                    	IPT CpuDelBuffCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_cpu_rel_buff_cnt
                                    
                                    	IPT CpuRelBuffCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_buff_fifo_full_cnt
                                    
                                    	IPT CrcErrBuffFifoFullCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_data_cell_cnt
                                    
                                    	FDT DataCellCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_data_byte_cnt
                                    
                                    	FDT DataByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_crc_dropped_pck_cnt
                                    
                                    	FDT CrcDroppedPckCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_invalid_destq_drop_cell_cnt
                                    
                                    	FDT invalid destq drop cell cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_indirect_command_count
                                    
                                    	FDT IndirectCommandCount
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_ecc_1b_err_cnt
                                    
                                    	FDT Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_ecc_2b_err_cnt
                                    
                                    	FDT Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_parity_err_cnt
                                    
                                    	FDT ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_crc_dropped_cell_cnt
                                    
                                    	FDT CrcDroppedCellCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_control_cell_cnt
                                    
                                    	FCR ControlCellCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_cell_drop_cnt
                                    
                                    	FCR CellDropCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_credit_cell_drop_cnt
                                    
                                    	FCR CreditCellDropCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_fs_cell_drop_cnt
                                    
                                    	FCR FSCellDropCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_rt_cell_drop_cnt
                                    
                                    	FCR RTCellDropCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_ecc_1b_err_cnt
                                    
                                    	FCR Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_ecc_2b_err_cnt
                                    
                                    	FCR Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_data_cell_cnt
                                    
                                    	FDR DataCellCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_data_byte_cnt
                                    
                                    	FDR DataByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_crc_dropped_pck_cnt
                                    
                                    	FDR CrcDroppedPckCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_p_pkt_cnt
                                    
                                    	FDR PPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_error_filter_cnt
                                    
                                    	FDR PrmErrorFilterCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_error_filter_cnt
                                    
                                    	FDR SecErrorFilterCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_ecc_1b_err_cnt
                                    
                                    	FDR PrmEcc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_ecc_2b_err_cnt
                                    
                                    	FDR PrmEcc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_ecc_1b_err_cnt
                                    
                                    	FDR SecEcc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_ecc_2b_err_cnt
                                    
                                    	FDR SecEcc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ecc_1b_err_cnt
                                    
                                    	EGQ Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ecc_2b_err_cnt
                                    
                                    	EGQ Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_parity_err_cnt
                                    
                                    	EGQ ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_dbf_ecc_1b_err_cnt
                                    
                                    	EGQ DbfEcc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_dbf_ecc_2b_err_cnt
                                    
                                    	EGQ DbfEcc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_empty_mcid_counter
                                    
                                    	EGQ EmptyMcidCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_rqp_discard_packet_counter
                                    
                                    	EGQ RqpDiscardPacketCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ehp_discard_packet_counter
                                    
                                    	EGQ EhpDiscardPacketCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ipt_pkt_cnt
                                    
                                    	EGQ IptPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_pkt_cnt
                                    
                                    	EPNI EpePktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_byte_cnt
                                    
                                    	EPNI EpeByteCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_discard_pkt_cnt
                                    
                                    	EPNI EpeDiscardPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_ecc_1b_err_cnt
                                    
                                    	EPNI Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_ecc_2b_err_cnt
                                    
                                    	EPNI Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_parity_err_cnt
                                    
                                    	EPNI ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_pkt_cnt
                                    
                                    	EGQ PqpUcastPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_h_pkt_cnt
                                    
                                    	EGQ PqpUcastHPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_l_pkt_cnt
                                    
                                    	EGQ PqpUcastLPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_bytes_cnt
                                    
                                    	EGQ PqpUcastBytesCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_discard_pkt_cnt
                                    
                                    	EGQ PqpUcastDiscardPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_pkt_cnt
                                    
                                    	EGQ PqpMcastPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_h_pkt_cnt
                                    
                                    	EGQ PqpMcastHPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_l_pkt_cnt
                                    
                                    	EGQ PqpMcastLPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_bytes_cnt
                                    
                                    	EGQ PqpMcastBytesCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_discard_pkt_cnt
                                    
                                    	EGQ PqpMcastDiscardPktCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fct_control_cell_cnt
                                    
                                    	FCT ControlCellCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fct_unrch_crdt_cnt
                                    
                                    	FCT UnrchCrdtCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_reassembly_errors
                                    
                                    	IDR ReassemblyErrors
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_mmu_ecc_1b_err_cnt
                                    
                                    	IDR MmuEcc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_mmu_ecc_2b_err_cnt
                                    
                                    	IDR MmuEcc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets0_cnt
                                    
                                    	IDR DiscardedPackets0Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets1_cnt
                                    
                                    	IDR DiscardedPackets1Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets2_cnt
                                    
                                    	IDR DiscardedPackets2Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets3_cnt
                                    
                                    	IDR DiscardedPackets3Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets0_cnt
                                    
                                    	IDR DiscardedOctets0Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets1_cnt
                                    
                                    	IDR DiscardedOctets1Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets2_cnt
                                    
                                    	IDR DiscardedOctets2Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets3_cnt
                                    
                                    	IDR DiscardedOctets3Cnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mmu_ecc_1b_err_cnt
                                    
                                    	MMU Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mmu_ecc_2b_err_cnt
                                    
                                    	MMU Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_parity_err_cnt
                                    
                                    	OAMP ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_ecc_1b_err_cnt
                                    
                                    	OAMP Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_ecc_2b_err_cnt
                                    
                                    	OAMP Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: crps_parity_err_cnt
                                    
                                    	CRPS ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs0TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs1TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs2TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs3TstRxErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst0_err_cnt
                                    
                                    	FMAC0 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst0_err_cnt
                                    
                                    	FMAC1 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst0_err_cnt
                                    
                                    	FMAC2 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst0_err_cnt
                                    
                                    	FMAC3 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst0_err_cnt
                                    
                                    	FMAC4 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst0_err_cnt
                                    
                                    	FMAC5 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst0_err_cnt
                                    
                                    	FMAC6 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst0_err_cnt
                                    
                                    	FMAC7 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst0_err_cnt
                                    
                                    	FMAC8 Tst0ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst1_err_cnt
                                    
                                    	FMAC0 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst1_err_cnt
                                    
                                    	FMAC1 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst1_err_cnt
                                    
                                    	FMAC2 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst1_err_cnt
                                    
                                    	FMAC3 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst1_err_cnt
                                    
                                    	FMAC4 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst1_err_cnt
                                    
                                    	FMAC5 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst1_err_cnt
                                    
                                    	FMAC6 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst1_err_cnt
                                    
                                    	FMAC7 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst1_err_cnt
                                    
                                    	FMAC8 Tst1ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst2_err_cnt
                                    
                                    	FMAC0 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst2_err_cnt
                                    
                                    	FMAC1 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst2_err_cnt
                                    
                                    	FMAC2 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst2_err_cnt
                                    
                                    	FMAC3 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst2_err_cnt
                                    
                                    	FMAC4 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst2_err_cnt
                                    
                                    	FMAC5 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst2_err_cnt
                                    
                                    	FMAC6 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst2_err_cnt
                                    
                                    	FMAC7 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst2_err_cnt
                                    
                                    	FMAC8 Tst2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst3_err_cnt
                                    
                                    	FMAC0 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst3_err_cnt
                                    
                                    	FMAC1 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst3_err_cnt
                                    
                                    	FMAC2 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst3_err_cnt
                                    
                                    	FMAC3 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst3_err_cnt
                                    
                                    	FMAC4 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst3_err_cnt
                                    
                                    	FMAC5 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst3_err_cnt
                                    
                                    	FMAC6 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst3_err_cnt
                                    
                                    	FMAC7 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst3_err_cnt
                                    
                                    	FMAC8 Tst3ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_ecc_1b_err_cnt
                                    
                                    	FMAC0 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_ecc_1b_err_cnt
                                    
                                    	FMAC1 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_ecc_1b_err_cnt
                                    
                                    	FMAC2 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_ecc_1b_err_cnt
                                    
                                    	FMAC3 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_ecc_1b_err_cnt
                                    
                                    	FMAC4 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_ecc_1b_err_cnt
                                    
                                    	FMAC5 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_ecc_1b_err_cnt
                                    
                                    	FMAC6 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_ecc_1b_err_cnt
                                    
                                    	FMAC7 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_ecc_1b_err_cnt
                                    
                                    	FMAC8 Ecc 1bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_ecc_2b_err_cnt
                                    
                                    	FMAC0 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_ecc_2b_err_cnt
                                    
                                    	FMAC1 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_ecc_2b_err_cnt
                                    
                                    	FMAC2 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_ecc_2b_err_cnt
                                    
                                    	FMAC3 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_ecc_2b_err_cnt
                                    
                                    	FMAC4 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_ecc_2b_err_cnt
                                    
                                    	FMAC5 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_ecc_2b_err_cnt
                                    
                                    	FMAC6 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_ecc_2b_err_cnt
                                    
                                    	FMAC7 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_ecc_2b_err_cnt
                                    
                                    	FMAC8 Ecc 2bErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: olp_incoming_bad_identifier_counter
                                    
                                    	OLP IncomingBadIdentifierCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: olp_incoming_bad_reassembly_counter
                                    
                                    	OLP IncomingBadReassemblyCounter
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_parity_err_cnt
                                    
                                    	CFC ParityErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_ilkn0_oob_rx_crc_err_cntr
                                    
                                    	CFC Ilkn0OobRxCrcErrCntr
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_ilkn1_oob_rx_crc_err_cntr
                                    
                                    	CFC Ilkn1OobRxCrcErrCntr
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx0_frm_err_cnt
                                    
                                    	CFC SpiOobRx0FrmErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx0_dip2_err_cnt
                                    
                                    	CFC SpiOobRx0Dip2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx1_frm_err_cnt
                                    
                                    	CFC SpiOobRx1FrmErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx1_dip2_err_cnt
                                    
                                    	CFC SpiOobRx1Dip2ErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_pd_dropped_cnt
                                    
                                    	CGM CgmUcPdDroppedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_rep_pd_dropped_cnt
                                    
                                    	CGM CgmMcRepPdDroppedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_db_dropped_by_rqp_cnt
                                    
                                    	CGM CgmUcDbDroppedByRqpCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_db_dropped_by_pqp_cnt
                                    
                                    	CGM CgmUcDbDroppedByPqpCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_rep_db_dropped_cnt
                                    
                                    	CGM CgmMcRepDbDroppedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_db_dropped_cnt
                                    
                                    	CGM CgmMcDbDroppedCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_full_err_cnt
                                    
                                    	DRCA FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_single_err_cnt
                                    
                                    	DRCA SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_calib_bist_full_err_cnt
                                    
                                    	DRCA CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_loopback_full_err_cnt
                                    
                                    	DRCA LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_full_err_cnt
                                    
                                    	DRCB FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_single_err_cnt
                                    
                                    	DRCB SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_calib_bist_full_err_cnt
                                    
                                    	DRCB CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_loopback_full_err_cnt
                                    
                                    	DRCB LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_full_err_cnt
                                    
                                    	DRCC FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_single_err_cnt
                                    
                                    	DRCC SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_calib_bist_full_err_cnt
                                    
                                    	DRCC CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_loopback_full_err_cnt
                                    
                                    	DRCC LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_full_err_cnt
                                    
                                    	DRCD FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_single_err_cnt
                                    
                                    	DRCD SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_calib_bist_full_err_cnt
                                    
                                    	DRCD CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_loopback_full_err_cnt
                                    
                                    	DRCD LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_full_err_cnt
                                    
                                    	DRCE FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_single_err_cnt
                                    
                                    	DRCE SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_calib_bist_full_err_cnt
                                    
                                    	DRCE CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_loopback_full_err_cnt
                                    
                                    	DRCE LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_full_err_cnt
                                    
                                    	DRCF FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_single_err_cnt
                                    
                                    	DRCF SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_calib_bist_full_err_cnt
                                    
                                    	DRCF CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_loopback_full_err_cnt
                                    
                                    	DRCF LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_full_err_cnt
                                    
                                    	DRCG FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_single_err_cnt
                                    
                                    	DRCG SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_calib_bist_full_err_cnt
                                    
                                    	DRCG CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_loopback_full_err_cnt
                                    
                                    	DRCG LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_full_err_cnt
                                    
                                    	DRCH FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_single_err_cnt
                                    
                                    	DRCH SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_calib_bist_full_err_cnt
                                    
                                    	DRCH CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_loopback_full_err_cnt
                                    
                                    	DRCH LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_full_err_cnt
                                    
                                    	DRCBROADCAST FullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_single_err_cnt
                                    
                                    	DRCBROADCAST SingleErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_calib_bist_full_err_cnt
                                    
                                    	DRCBROADCAST CalibBistFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_loopback_full_err_cnt
                                    
                                    	DRCBROADCAST LoopbackFullErrCnt
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: otn_mode
                                    
                                    	otn mode
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_ports
                                    
                                    	num ports
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: aggr_stats_otn
                                    
                                    	aggr stats otn
                                    	**type**\: list of  		 :py:class:`AggrStatsOtn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats.AggrStatsOtn>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats, self).__init__()

                                        self.yang_name = "aggr-stats"
                                        self.yang_parent_name = "pbc-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("aggr-stats-otn", ("aggr_stats_otn", Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats.AggrStatsOtn))])
                                        self._leafs = OrderedDict([
                                            ('rx_internal_error', (YLeaf(YType.uint64, 'rx-internal-error'), ['int'])),
                                            ('rx_internal_drop', (YLeaf(YType.uint64, 'rx-internal-drop'), ['int'])),
                                            ('tx_internal_error', (YLeaf(YType.uint64, 'tx-internal-error'), ['int'])),
                                            ('tx_internal_drop', (YLeaf(YType.uint64, 'tx-internal-drop'), ['int'])),
                                            ('cmic_cmc0_pkt_count_tx_pkt', (YLeaf(YType.uint64, 'cmic-cmc0-pkt-count-tx-pkt'), ['int'])),
                                            ('cmic_cmc0_pkt_count_rx_pkt', (YLeaf(YType.uint64, 'cmic-cmc0-pkt-count-rx-pkt'), ['int'])),
                                            ('nbi_stat_rx_bursts_err_cnt', (YLeaf(YType.uint64, 'nbi-stat-rx-bursts-err-cnt'), ['int'])),
                                            ('nbi_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'nbi-ecc-1b-err-cnt'), ['int'])),
                                            ('nbi_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'nbi-ecc-2b-err-cnt'), ['int'])),
                                            ('nbi_parity_err_cnt', (YLeaf(YType.uint64, 'nbi-parity-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn_crc32_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn-crc32-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_crc24_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-crc24-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_burst_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-burst-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_miss_sop_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-miss-sop-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_miss_eop_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-miss-eop-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_misaligned_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-misaligned-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_crc24_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-crc24-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_burst_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-burst-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_miss_sop_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-miss-sop-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_miss_eop_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-miss-eop-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_misaligned_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-misaligned-cnt'), ['int'])),
                                            ('nbi_tx_ilkn1_flushed_bursts_cnt', (YLeaf(YType.uint64, 'nbi-tx-ilkn1-flushed-bursts-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_crc24_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-crc24-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_retry_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-retry-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_wdog_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-wdog-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-wrap-after-disc-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-wrap-b4-disc-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn0_retrans_reached_timeout_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn0-retrans-reached-timeout-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_crc24_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-crc24-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_retry_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-retry-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_wdog_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-wdog-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-wrap-after-disc-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-wrap-b4-disc-err-cnt'), ['int'])),
                                            ('nbi_rx_ilkn1_retrans_reached_timeout_err_cnt', (YLeaf(YType.uint64, 'nbi-rx-ilkn1-retrans-reached-timeout-err-cnt'), ['int'])),
                                            ('nbi_stat_rx_frame_err_cnt', (YLeaf(YType.uint64, 'nbi-stat-rx-frame-err-cnt'), ['int'])),
                                            ('nbi_stat_tx_frame_err_cnt', (YLeaf(YType.uint64, 'nbi-stat-tx-frame-err-cnt'), ['int'])),
                                            ('nbi_rx_elk_err_bursts_cnt', (YLeaf(YType.uint64, 'nbi-rx-elk-err-bursts-cnt'), ['int'])),
                                            ('nbi_rx_num_thrown_eops', (YLeaf(YType.uint64, 'nbi-rx-num-thrown-eops'), ['int'])),
                                            ('nbi_rx_num_runts', (YLeaf(YType.uint64, 'nbi-rx-num-runts'), ['int'])),
                                            ('nbi_bist_tx_crc_err_bursts_cnt', (YLeaf(YType.uint64, 'nbi-bist-tx-crc-err-bursts-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_length_bursts_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-length-bursts-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_burst_index_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-burst-index-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_bct_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-bct-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_data_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-data-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_in_crc_err_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-in-crc-err-cnt'), ['int'])),
                                            ('nbi_bist_rx_err_sob_cnt', (YLeaf(YType.uint64, 'nbi-bist-rx-err-sob-cnt'), ['int'])),
                                            ('nbi_stat_tx_bursts_cnt', (YLeaf(YType.uint64, 'nbi-stat-tx-bursts-cnt'), ['int'])),
                                            ('nbi_stat_tx_total_leng_cnt', (YLeaf(YType.uint64, 'nbi-stat-tx-total-leng-cnt'), ['int'])),
                                            ('rxaui_total_tx_pkt_count', (YLeaf(YType.uint64, 'rxaui-total-tx-pkt-count'), ['int'])),
                                            ('rxaui_total_rx_pkt_count', (YLeaf(YType.uint64, 'rxaui-total-rx-pkt-count'), ['int'])),
                                            ('rxaui_rx_pkt_count_bcast_pkt', (YLeaf(YType.uint64, 'rxaui-rx-pkt-count-bcast-pkt'), ['int'])),
                                            ('rxaui_tx_pkt_count_bcast_pkt', (YLeaf(YType.uint64, 'rxaui-tx-pkt-count-bcast-pkt'), ['int'])),
                                            ('rxaui_rx_pkt_count_mcast_pkt', (YLeaf(YType.uint64, 'rxaui-rx-pkt-count-mcast-pkt'), ['int'])),
                                            ('rxaui_tx_pkt_count_mcast_pkt', (YLeaf(YType.uint64, 'rxaui-tx-pkt-count-mcast-pkt'), ['int'])),
                                            ('rxaui_rx_pkt_count_ucast_pkt', (YLeaf(YType.uint64, 'rxaui-rx-pkt-count-ucast-pkt'), ['int'])),
                                            ('rxaui_tx_pkt_count_ucast_pkt', (YLeaf(YType.uint64, 'rxaui-tx-pkt-count-ucast-pkt'), ['int'])),
                                            ('rxaui_rx_err_drop_pkt_cnt', (YLeaf(YType.uint64, 'rxaui-rx-err-drop-pkt-cnt'), ['int'])),
                                            ('rxaui_tx_err_drop_pkt_cnt', (YLeaf(YType.uint64, 'rxaui-tx-err-drop-pkt-cnt'), ['int'])),
                                            ('rxaui_byte_count_tx_pkt', (YLeaf(YType.uint64, 'rxaui-byte-count-tx-pkt'), ['int'])),
                                            ('rxaui_byte_count_rx_pkt', (YLeaf(YType.uint64, 'rxaui-byte-count-rx-pkt'), ['int'])),
                                            ('rxaui_rx_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'rxaui-rx-dscrd-pkt-cnt'), ['int'])),
                                            ('rxaui_tx_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'rxaui-tx-dscrd-pkt-cnt'), ['int'])),
                                            ('ire_nif_packet_counter', (YLeaf(YType.uint64, 'ire-nif-packet-counter'), ['int'])),
                                            ('il_total_rx_pkt_count', (YLeaf(YType.uint64, 'il-total-rx-pkt-count'), ['int'])),
                                            ('il_total_tx_pkt_count', (YLeaf(YType.uint64, 'il-total-tx-pkt-count'), ['int'])),
                                            ('il_rx_err_drop_pkt_cnt', (YLeaf(YType.uint64, 'il-rx-err-drop-pkt-cnt'), ['int'])),
                                            ('il_tx_err_drop_pkt_cnt', (YLeaf(YType.uint64, 'il-tx-err-drop-pkt-cnt'), ['int'])),
                                            ('il_byte_count_tx_pkt', (YLeaf(YType.uint64, 'il-byte-count-tx-pkt'), ['int'])),
                                            ('il_byte_count_rx_pkt', (YLeaf(YType.uint64, 'il-byte-count-rx-pkt'), ['int'])),
                                            ('il_rx_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'il-rx-dscrd-pkt-cnt'), ['int'])),
                                            ('il_tx_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'il-tx-dscrd-pkt-cnt'), ['int'])),
                                            ('il_rx_pkt_count_bcast_pkt', (YLeaf(YType.uint64, 'il-rx-pkt-count-bcast-pkt'), ['int'])),
                                            ('il_tx_pkt_count_bcast_pkt', (YLeaf(YType.uint64, 'il-tx-pkt-count-bcast-pkt'), ['int'])),
                                            ('il_rx_pkt_count_mcast_pkt', (YLeaf(YType.uint64, 'il-rx-pkt-count-mcast-pkt'), ['int'])),
                                            ('il_tx_pkt_count_mcast_pkt', (YLeaf(YType.uint64, 'il-tx-pkt-count-mcast-pkt'), ['int'])),
                                            ('il_rx_pkt_count_ucast_pkt', (YLeaf(YType.uint64, 'il-rx-pkt-count-ucast-pkt'), ['int'])),
                                            ('il_tx_pkt_count_ucast_pkt', (YLeaf(YType.uint64, 'il-tx-pkt-count-ucast-pkt'), ['int'])),
                                            ('iqm_enq_pkt_cnt', (YLeaf(YType.uint64, 'iqm-enq-pkt-cnt'), ['int'])),
                                            ('iqm_enq_byte_cnt', (YLeaf(YType.uint64, 'iqm-enq-byte-cnt'), ['int'])),
                                            ('iqm_deq_pkt_cnt', (YLeaf(YType.uint64, 'iqm-deq-pkt-cnt'), ['int'])),
                                            ('iqm_deq_byte_cnt', (YLeaf(YType.uint64, 'iqm-deq-byte-cnt'), ['int'])),
                                            ('iqm_tot_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'iqm-tot-dscrd-pkt-cnt'), ['int'])),
                                            ('iqm_tot_dscrd_byte_cnt', (YLeaf(YType.uint64, 'iqm-tot-dscrd-byte-cnt'), ['int'])),
                                            ('iqm_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'iqm-ecc-1b-err-cnt'), ['int'])),
                                            ('iqm_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'iqm-ecc-2b-err-cnt'), ['int'])),
                                            ('iqm_parity_err_cnt', (YLeaf(YType.uint64, 'iqm-parity-err-cnt'), ['int'])),
                                            ('iqm_deq_delete_pkt_cnt', (YLeaf(YType.uint64, 'iqm-deq-delete-pkt-cnt'), ['int'])),
                                            ('iqm_ecn_dscrd_msk_pkt_cnt', (YLeaf(YType.uint64, 'iqm-ecn-dscrd-msk-pkt-cnt'), ['int'])),
                                            ('iqm_q_tot_dscrd_pkt_cnt', (YLeaf(YType.uint64, 'iqm-q-tot-dscrd-pkt-cnt'), ['int'])),
                                            ('iqm_q_deq_delete_pkt_cnt', (YLeaf(YType.uint64, 'iqm-q-deq-delete-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_db_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-db-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_bdb_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-bdb-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_bdb_protct_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-bdb-protct-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_oc_bd_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-oc-bd-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_sn_err_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-sn-err-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_mc_err_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-mc-err-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_rsrc_err_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-rsrc-err-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_qnvalid_err_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-qnvalid-err-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_cnm_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-cnm-pkt-cnt'), ['int'])),
                                            ('iqm_rjct_dyn_space_pkt_cnt', (YLeaf(YType.uint64, 'iqm-rjct-dyn-space-pkt-cnt'), ['int'])),
                                            ('ipt_fdt_pkt_cnt', (YLeaf(YType.uint64, 'ipt-fdt-pkt-cnt'), ['int'])),
                                            ('ipt_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'ipt-ecc-1b-err-cnt'), ['int'])),
                                            ('ipt_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'ipt-ecc-2b-err-cnt'), ['int'])),
                                            ('ipt_parity_err_cnt', (YLeaf(YType.uint64, 'ipt-parity-err-cnt'), ['int'])),
                                            ('ipt_crc_err_cnt', (YLeaf(YType.uint64, 'ipt-crc-err-cnt'), ['int'])),
                                            ('ipt_crc_err_del_buff_cnt', (YLeaf(YType.uint64, 'ipt-crc-err-del-buff-cnt'), ['int'])),
                                            ('ipt_cpu_del_buff_cnt', (YLeaf(YType.uint64, 'ipt-cpu-del-buff-cnt'), ['int'])),
                                            ('ipt_cpu_rel_buff_cnt', (YLeaf(YType.uint64, 'ipt-cpu-rel-buff-cnt'), ['int'])),
                                            ('ipt_crc_err_buff_fifo_full_cnt', (YLeaf(YType.uint64, 'ipt-crc-err-buff-fifo-full-cnt'), ['int'])),
                                            ('fdt_data_cell_cnt', (YLeaf(YType.uint64, 'fdt-data-cell-cnt'), ['int'])),
                                            ('fdt_data_byte_cnt', (YLeaf(YType.uint64, 'fdt-data-byte-cnt'), ['int'])),
                                            ('fdt_crc_dropped_pck_cnt', (YLeaf(YType.uint64, 'fdt-crc-dropped-pck-cnt'), ['int'])),
                                            ('fdt_invalid_destq_drop_cell_cnt', (YLeaf(YType.uint64, 'fdt-invalid-destq-drop-cell-cnt'), ['int'])),
                                            ('fdt_indirect_command_count', (YLeaf(YType.uint64, 'fdt-indirect-command-count'), ['int'])),
                                            ('fdt_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fdt-ecc-1b-err-cnt'), ['int'])),
                                            ('fdt_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fdt-ecc-2b-err-cnt'), ['int'])),
                                            ('fdt_parity_err_cnt', (YLeaf(YType.uint64, 'fdt-parity-err-cnt'), ['int'])),
                                            ('fdt_crc_dropped_cell_cnt', (YLeaf(YType.uint64, 'fdt-crc-dropped-cell-cnt'), ['int'])),
                                            ('fcr_control_cell_cnt', (YLeaf(YType.uint64, 'fcr-control-cell-cnt'), ['int'])),
                                            ('fcr_cell_drop_cnt', (YLeaf(YType.uint64, 'fcr-cell-drop-cnt'), ['int'])),
                                            ('fcr_credit_cell_drop_cnt', (YLeaf(YType.uint64, 'fcr-credit-cell-drop-cnt'), ['int'])),
                                            ('fcr_fs_cell_drop_cnt', (YLeaf(YType.uint64, 'fcr-fs-cell-drop-cnt'), ['int'])),
                                            ('fcr_rt_cell_drop_cnt', (YLeaf(YType.uint64, 'fcr-rt-cell-drop-cnt'), ['int'])),
                                            ('fcr_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fcr-ecc-1b-err-cnt'), ['int'])),
                                            ('fcr_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fcr-ecc-2b-err-cnt'), ['int'])),
                                            ('fdr_data_cell_cnt', (YLeaf(YType.uint64, 'fdr-data-cell-cnt'), ['int'])),
                                            ('fdr_data_byte_cnt', (YLeaf(YType.uint64, 'fdr-data-byte-cnt'), ['int'])),
                                            ('fdr_crc_dropped_pck_cnt', (YLeaf(YType.uint64, 'fdr-crc-dropped-pck-cnt'), ['int'])),
                                            ('fdr_p_pkt_cnt', (YLeaf(YType.uint64, 'fdr-p-pkt-cnt'), ['int'])),
                                            ('fdr_prm_error_filter_cnt', (YLeaf(YType.uint64, 'fdr-prm-error-filter-cnt'), ['int'])),
                                            ('fdr_sec_error_filter_cnt', (YLeaf(YType.uint64, 'fdr-sec-error-filter-cnt'), ['int'])),
                                            ('fdr_prm_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fdr-prm-ecc-1b-err-cnt'), ['int'])),
                                            ('fdr_prm_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fdr-prm-ecc-2b-err-cnt'), ['int'])),
                                            ('fdr_sec_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fdr-sec-ecc-1b-err-cnt'), ['int'])),
                                            ('fdr_sec_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fdr-sec-ecc-2b-err-cnt'), ['int'])),
                                            ('egq_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'egq-ecc-1b-err-cnt'), ['int'])),
                                            ('egq_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'egq-ecc-2b-err-cnt'), ['int'])),
                                            ('egq_parity_err_cnt', (YLeaf(YType.uint64, 'egq-parity-err-cnt'), ['int'])),
                                            ('egq_dbf_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'egq-dbf-ecc-1b-err-cnt'), ['int'])),
                                            ('egq_dbf_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'egq-dbf-ecc-2b-err-cnt'), ['int'])),
                                            ('egq_empty_mcid_counter', (YLeaf(YType.uint64, 'egq-empty-mcid-counter'), ['int'])),
                                            ('egq_rqp_discard_packet_counter', (YLeaf(YType.uint64, 'egq-rqp-discard-packet-counter'), ['int'])),
                                            ('egq_ehp_discard_packet_counter', (YLeaf(YType.uint64, 'egq-ehp-discard-packet-counter'), ['int'])),
                                            ('egq_ipt_pkt_cnt', (YLeaf(YType.uint64, 'egq-ipt-pkt-cnt'), ['int'])),
                                            ('epni_epe_pkt_cnt', (YLeaf(YType.uint64, 'epni-epe-pkt-cnt'), ['int'])),
                                            ('epni_epe_byte_cnt', (YLeaf(YType.uint64, 'epni-epe-byte-cnt'), ['int'])),
                                            ('epni_epe_discard_pkt_cnt', (YLeaf(YType.uint64, 'epni-epe-discard-pkt-cnt'), ['int'])),
                                            ('epni_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'epni-ecc-1b-err-cnt'), ['int'])),
                                            ('epni_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'epni-ecc-2b-err-cnt'), ['int'])),
                                            ('epni_parity_err_cnt', (YLeaf(YType.uint64, 'epni-parity-err-cnt'), ['int'])),
                                            ('egq_pqp_ucast_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-ucast-pkt-cnt'), ['int'])),
                                            ('egq_pqp_ucast_h_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-ucast-h-pkt-cnt'), ['int'])),
                                            ('egq_pqp_ucast_l_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-ucast-l-pkt-cnt'), ['int'])),
                                            ('egq_pqp_ucast_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-ucast-bytes-cnt'), ['int'])),
                                            ('egq_pqp_ucast_discard_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-ucast-discard-pkt-cnt'), ['int'])),
                                            ('egq_pqp_mcast_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mcast-pkt-cnt'), ['int'])),
                                            ('egq_pqp_mcast_h_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mcast-h-pkt-cnt'), ['int'])),
                                            ('egq_pqp_mcast_l_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mcast-l-pkt-cnt'), ['int'])),
                                            ('egq_pqp_mcast_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-mcast-bytes-cnt'), ['int'])),
                                            ('egq_pqp_mcast_discard_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mcast-discard-pkt-cnt'), ['int'])),
                                            ('fct_control_cell_cnt', (YLeaf(YType.uint64, 'fct-control-cell-cnt'), ['int'])),
                                            ('fct_unrch_crdt_cnt', (YLeaf(YType.uint64, 'fct-unrch-crdt-cnt'), ['int'])),
                                            ('idr_reassembly_errors', (YLeaf(YType.uint64, 'idr-reassembly-errors'), ['int'])),
                                            ('idr_mmu_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'idr-mmu-ecc-1b-err-cnt'), ['int'])),
                                            ('idr_mmu_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'idr-mmu-ecc-2b-err-cnt'), ['int'])),
                                            ('idr_discarded_packets0_cnt', (YLeaf(YType.uint64, 'idr-discarded-packets0-cnt'), ['int'])),
                                            ('idr_discarded_packets1_cnt', (YLeaf(YType.uint64, 'idr-discarded-packets1-cnt'), ['int'])),
                                            ('idr_discarded_packets2_cnt', (YLeaf(YType.uint64, 'idr-discarded-packets2-cnt'), ['int'])),
                                            ('idr_discarded_packets3_cnt', (YLeaf(YType.uint64, 'idr-discarded-packets3-cnt'), ['int'])),
                                            ('idr_discarded_octets0_cnt', (YLeaf(YType.uint64, 'idr-discarded-octets0-cnt'), ['int'])),
                                            ('idr_discarded_octets1_cnt', (YLeaf(YType.uint64, 'idr-discarded-octets1-cnt'), ['int'])),
                                            ('idr_discarded_octets2_cnt', (YLeaf(YType.uint64, 'idr-discarded-octets2-cnt'), ['int'])),
                                            ('idr_discarded_octets3_cnt', (YLeaf(YType.uint64, 'idr-discarded-octets3-cnt'), ['int'])),
                                            ('mmu_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'mmu-ecc-1b-err-cnt'), ['int'])),
                                            ('mmu_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'mmu-ecc-2b-err-cnt'), ['int'])),
                                            ('oamp_parity_err_cnt', (YLeaf(YType.uint64, 'oamp-parity-err-cnt'), ['int'])),
                                            ('oamp_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'oamp-ecc-1b-err-cnt'), ['int'])),
                                            ('oamp_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'oamp-ecc-2b-err-cnt'), ['int'])),
                                            ('crps_parity_err_cnt', (YLeaf(YType.uint64, 'crps-parity-err-cnt'), ['int'])),
                                            ('fmac0_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac0-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac1_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac1-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac2_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac2-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac3_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac3-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac4_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac4-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac5_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac5-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac6_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac6-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac7_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac7-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac8_kpcs0_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac8-kpcs0-tst-rx-err-cnt'), ['int'])),
                                            ('fmac0_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac0-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac1_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac1-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac2_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac2-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac3_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac3-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac4_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac4-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac5_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac5-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac6_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac6-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac7_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac7-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac8_kpcs1_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac8-kpcs1-tst-rx-err-cnt'), ['int'])),
                                            ('fmac0_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac0-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac1_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac1-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac2_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac2-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac3_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac3-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac4_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac4-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac5_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac5-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac6_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac6-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac7_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac7-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac8_kpcs2_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac8-kpcs2-tst-rx-err-cnt'), ['int'])),
                                            ('fmac0_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac0-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac1_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac1-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac2_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac2-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac3_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac3-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac4_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac4-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac5_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac5-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac6_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac6-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac7_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac7-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac8_kpcs3_tst_rx_err_cnt', (YLeaf(YType.uint64, 'fmac8-kpcs3-tst-rx-err-cnt'), ['int'])),
                                            ('fmac0_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac0-tst0-err-cnt'), ['int'])),
                                            ('fmac1_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac1-tst0-err-cnt'), ['int'])),
                                            ('fmac2_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac2-tst0-err-cnt'), ['int'])),
                                            ('fmac3_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac3-tst0-err-cnt'), ['int'])),
                                            ('fmac4_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac4-tst0-err-cnt'), ['int'])),
                                            ('fmac5_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac5-tst0-err-cnt'), ['int'])),
                                            ('fmac6_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac6-tst0-err-cnt'), ['int'])),
                                            ('fmac7_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac7-tst0-err-cnt'), ['int'])),
                                            ('fmac8_tst0_err_cnt', (YLeaf(YType.uint64, 'fmac8-tst0-err-cnt'), ['int'])),
                                            ('fmac0_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac0-tst1-err-cnt'), ['int'])),
                                            ('fmac1_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac1-tst1-err-cnt'), ['int'])),
                                            ('fmac2_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac2-tst1-err-cnt'), ['int'])),
                                            ('fmac3_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac3-tst1-err-cnt'), ['int'])),
                                            ('fmac4_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac4-tst1-err-cnt'), ['int'])),
                                            ('fmac5_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac5-tst1-err-cnt'), ['int'])),
                                            ('fmac6_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac6-tst1-err-cnt'), ['int'])),
                                            ('fmac7_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac7-tst1-err-cnt'), ['int'])),
                                            ('fmac8_tst1_err_cnt', (YLeaf(YType.uint64, 'fmac8-tst1-err-cnt'), ['int'])),
                                            ('fmac0_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac0-tst2-err-cnt'), ['int'])),
                                            ('fmac1_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac1-tst2-err-cnt'), ['int'])),
                                            ('fmac2_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac2-tst2-err-cnt'), ['int'])),
                                            ('fmac3_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac3-tst2-err-cnt'), ['int'])),
                                            ('fmac4_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac4-tst2-err-cnt'), ['int'])),
                                            ('fmac5_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac5-tst2-err-cnt'), ['int'])),
                                            ('fmac6_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac6-tst2-err-cnt'), ['int'])),
                                            ('fmac7_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac7-tst2-err-cnt'), ['int'])),
                                            ('fmac8_tst2_err_cnt', (YLeaf(YType.uint64, 'fmac8-tst2-err-cnt'), ['int'])),
                                            ('fmac0_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac0-tst3-err-cnt'), ['int'])),
                                            ('fmac1_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac1-tst3-err-cnt'), ['int'])),
                                            ('fmac2_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac2-tst3-err-cnt'), ['int'])),
                                            ('fmac3_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac3-tst3-err-cnt'), ['int'])),
                                            ('fmac4_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac4-tst3-err-cnt'), ['int'])),
                                            ('fmac5_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac5-tst3-err-cnt'), ['int'])),
                                            ('fmac6_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac6-tst3-err-cnt'), ['int'])),
                                            ('fmac7_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac7-tst3-err-cnt'), ['int'])),
                                            ('fmac8_tst3_err_cnt', (YLeaf(YType.uint64, 'fmac8-tst3-err-cnt'), ['int'])),
                                            ('fmac0_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac0-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac1_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac1-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac2_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac2-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac3_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac3-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac4_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac4-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac5_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac5-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac6_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac6-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac7_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac7-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac8_ecc_1b_err_cnt', (YLeaf(YType.uint64, 'fmac8-ecc-1b-err-cnt'), ['int'])),
                                            ('fmac0_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac0-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac1_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac1-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac2_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac2-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac3_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac3-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac4_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac4-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac5_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac5-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac6_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac6-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac7_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac7-ecc-2b-err-cnt'), ['int'])),
                                            ('fmac8_ecc_2b_err_cnt', (YLeaf(YType.uint64, 'fmac8-ecc-2b-err-cnt'), ['int'])),
                                            ('olp_incoming_bad_identifier_counter', (YLeaf(YType.uint64, 'olp-incoming-bad-identifier-counter'), ['int'])),
                                            ('olp_incoming_bad_reassembly_counter', (YLeaf(YType.uint64, 'olp-incoming-bad-reassembly-counter'), ['int'])),
                                            ('cfc_parity_err_cnt', (YLeaf(YType.uint64, 'cfc-parity-err-cnt'), ['int'])),
                                            ('cfc_ilkn0_oob_rx_crc_err_cntr', (YLeaf(YType.uint64, 'cfc-ilkn0-oob-rx-crc-err-cntr'), ['int'])),
                                            ('cfc_ilkn1_oob_rx_crc_err_cntr', (YLeaf(YType.uint64, 'cfc-ilkn1-oob-rx-crc-err-cntr'), ['int'])),
                                            ('cfc_spi_oob_rx0_frm_err_cnt', (YLeaf(YType.uint64, 'cfc-spi-oob-rx0-frm-err-cnt'), ['int'])),
                                            ('cfc_spi_oob_rx0_dip2_err_cnt', (YLeaf(YType.uint64, 'cfc-spi-oob-rx0-dip2-err-cnt'), ['int'])),
                                            ('cfc_spi_oob_rx1_frm_err_cnt', (YLeaf(YType.uint64, 'cfc-spi-oob-rx1-frm-err-cnt'), ['int'])),
                                            ('cfc_spi_oob_rx1_dip2_err_cnt', (YLeaf(YType.uint64, 'cfc-spi-oob-rx1-dip2-err-cnt'), ['int'])),
                                            ('cgm_cgm_uc_pd_dropped_cnt', (YLeaf(YType.uint64, 'cgm-cgm-uc-pd-dropped-cnt'), ['int'])),
                                            ('cgm_cgm_mc_rep_pd_dropped_cnt', (YLeaf(YType.uint64, 'cgm-cgm-mc-rep-pd-dropped-cnt'), ['int'])),
                                            ('cgm_cgm_uc_db_dropped_by_rqp_cnt', (YLeaf(YType.uint64, 'cgm-cgm-uc-db-dropped-by-rqp-cnt'), ['int'])),
                                            ('cgm_cgm_uc_db_dropped_by_pqp_cnt', (YLeaf(YType.uint64, 'cgm-cgm-uc-db-dropped-by-pqp-cnt'), ['int'])),
                                            ('cgm_cgm_mc_rep_db_dropped_cnt', (YLeaf(YType.uint64, 'cgm-cgm-mc-rep-db-dropped-cnt'), ['int'])),
                                            ('cgm_cgm_mc_db_dropped_cnt', (YLeaf(YType.uint64, 'cgm-cgm-mc-db-dropped-cnt'), ['int'])),
                                            ('drca_full_err_cnt', (YLeaf(YType.uint64, 'drca-full-err-cnt'), ['int'])),
                                            ('drca_single_err_cnt', (YLeaf(YType.uint64, 'drca-single-err-cnt'), ['int'])),
                                            ('drca_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drca-calib-bist-full-err-cnt'), ['int'])),
                                            ('drca_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drca-loopback-full-err-cnt'), ['int'])),
                                            ('drcb_full_err_cnt', (YLeaf(YType.uint64, 'drcb-full-err-cnt'), ['int'])),
                                            ('drcb_single_err_cnt', (YLeaf(YType.uint64, 'drcb-single-err-cnt'), ['int'])),
                                            ('drcb_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcb-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcb_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcb-loopback-full-err-cnt'), ['int'])),
                                            ('drcc_full_err_cnt', (YLeaf(YType.uint64, 'drcc-full-err-cnt'), ['int'])),
                                            ('drcc_single_err_cnt', (YLeaf(YType.uint64, 'drcc-single-err-cnt'), ['int'])),
                                            ('drcc_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcc-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcc_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcc-loopback-full-err-cnt'), ['int'])),
                                            ('drcd_full_err_cnt', (YLeaf(YType.uint64, 'drcd-full-err-cnt'), ['int'])),
                                            ('drcd_single_err_cnt', (YLeaf(YType.uint64, 'drcd-single-err-cnt'), ['int'])),
                                            ('drcd_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcd-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcd_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcd-loopback-full-err-cnt'), ['int'])),
                                            ('drce_full_err_cnt', (YLeaf(YType.uint64, 'drce-full-err-cnt'), ['int'])),
                                            ('drce_single_err_cnt', (YLeaf(YType.uint64, 'drce-single-err-cnt'), ['int'])),
                                            ('drce_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drce-calib-bist-full-err-cnt'), ['int'])),
                                            ('drce_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drce-loopback-full-err-cnt'), ['int'])),
                                            ('drcf_full_err_cnt', (YLeaf(YType.uint64, 'drcf-full-err-cnt'), ['int'])),
                                            ('drcf_single_err_cnt', (YLeaf(YType.uint64, 'drcf-single-err-cnt'), ['int'])),
                                            ('drcf_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcf-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcf_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcf-loopback-full-err-cnt'), ['int'])),
                                            ('drcg_full_err_cnt', (YLeaf(YType.uint64, 'drcg-full-err-cnt'), ['int'])),
                                            ('drcg_single_err_cnt', (YLeaf(YType.uint64, 'drcg-single-err-cnt'), ['int'])),
                                            ('drcg_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcg-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcg_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcg-loopback-full-err-cnt'), ['int'])),
                                            ('drch_full_err_cnt', (YLeaf(YType.uint64, 'drch-full-err-cnt'), ['int'])),
                                            ('drch_single_err_cnt', (YLeaf(YType.uint64, 'drch-single-err-cnt'), ['int'])),
                                            ('drch_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drch-calib-bist-full-err-cnt'), ['int'])),
                                            ('drch_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drch-loopback-full-err-cnt'), ['int'])),
                                            ('drcbroadcast_full_err_cnt', (YLeaf(YType.uint64, 'drcbroadcast-full-err-cnt'), ['int'])),
                                            ('drcbroadcast_single_err_cnt', (YLeaf(YType.uint64, 'drcbroadcast-single-err-cnt'), ['int'])),
                                            ('drcbroadcast_calib_bist_full_err_cnt', (YLeaf(YType.uint64, 'drcbroadcast-calib-bist-full-err-cnt'), ['int'])),
                                            ('drcbroadcast_loopback_full_err_cnt', (YLeaf(YType.uint64, 'drcbroadcast-loopback-full-err-cnt'), ['int'])),
                                            ('otn_mode', (YLeaf(YType.uint32, 'otn-mode'), ['int'])),
                                            ('num_ports', (YLeaf(YType.uint32, 'num-ports'), ['int'])),
                                        ])
                                        self.rx_internal_error = None
                                        self.rx_internal_drop = None
                                        self.tx_internal_error = None
                                        self.tx_internal_drop = None
                                        self.cmic_cmc0_pkt_count_tx_pkt = None
                                        self.cmic_cmc0_pkt_count_rx_pkt = None
                                        self.nbi_stat_rx_bursts_err_cnt = None
                                        self.nbi_ecc_1b_err_cnt = None
                                        self.nbi_ecc_2b_err_cnt = None
                                        self.nbi_parity_err_cnt = None
                                        self.nbi_rx_ilkn_crc32_err_cnt = None
                                        self.nbi_rx_ilkn0_crc24_err_cnt = None
                                        self.nbi_rx_ilkn0_burst_err_cnt = None
                                        self.nbi_rx_ilkn0_miss_sop_err_cnt = None
                                        self.nbi_rx_ilkn0_miss_eop_err_cnt = None
                                        self.nbi_rx_ilkn0_misaligned_cnt = None
                                        self.nbi_rx_ilkn1_crc24_err_cnt = None
                                        self.nbi_rx_ilkn1_burst_err_cnt = None
                                        self.nbi_rx_ilkn1_miss_sop_err_cnt = None
                                        self.nbi_rx_ilkn1_miss_eop_err_cnt = None
                                        self.nbi_rx_ilkn1_misaligned_cnt = None
                                        self.nbi_tx_ilkn1_flushed_bursts_cnt = None
                                        self.nbi_rx_ilkn0_retrans_crc24_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_retry_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wdog_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_reached_timeout_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_crc24_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_retry_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wdog_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_reached_timeout_err_cnt = None
                                        self.nbi_stat_rx_frame_err_cnt = None
                                        self.nbi_stat_tx_frame_err_cnt = None
                                        self.nbi_rx_elk_err_bursts_cnt = None
                                        self.nbi_rx_num_thrown_eops = None
                                        self.nbi_rx_num_runts = None
                                        self.nbi_bist_tx_crc_err_bursts_cnt = None
                                        self.nbi_bist_rx_err_length_bursts_cnt = None
                                        self.nbi_bist_rx_err_burst_index_cnt = None
                                        self.nbi_bist_rx_err_bct_cnt = None
                                        self.nbi_bist_rx_err_data_cnt = None
                                        self.nbi_bist_rx_err_in_crc_err_cnt = None
                                        self.nbi_bist_rx_err_sob_cnt = None
                                        self.nbi_stat_tx_bursts_cnt = None
                                        self.nbi_stat_tx_total_leng_cnt = None
                                        self.rxaui_total_tx_pkt_count = None
                                        self.rxaui_total_rx_pkt_count = None
                                        self.rxaui_rx_pkt_count_bcast_pkt = None
                                        self.rxaui_tx_pkt_count_bcast_pkt = None
                                        self.rxaui_rx_pkt_count_mcast_pkt = None
                                        self.rxaui_tx_pkt_count_mcast_pkt = None
                                        self.rxaui_rx_pkt_count_ucast_pkt = None
                                        self.rxaui_tx_pkt_count_ucast_pkt = None
                                        self.rxaui_rx_err_drop_pkt_cnt = None
                                        self.rxaui_tx_err_drop_pkt_cnt = None
                                        self.rxaui_byte_count_tx_pkt = None
                                        self.rxaui_byte_count_rx_pkt = None
                                        self.rxaui_rx_dscrd_pkt_cnt = None
                                        self.rxaui_tx_dscrd_pkt_cnt = None
                                        self.ire_nif_packet_counter = None
                                        self.il_total_rx_pkt_count = None
                                        self.il_total_tx_pkt_count = None
                                        self.il_rx_err_drop_pkt_cnt = None
                                        self.il_tx_err_drop_pkt_cnt = None
                                        self.il_byte_count_tx_pkt = None
                                        self.il_byte_count_rx_pkt = None
                                        self.il_rx_dscrd_pkt_cnt = None
                                        self.il_tx_dscrd_pkt_cnt = None
                                        self.il_rx_pkt_count_bcast_pkt = None
                                        self.il_tx_pkt_count_bcast_pkt = None
                                        self.il_rx_pkt_count_mcast_pkt = None
                                        self.il_tx_pkt_count_mcast_pkt = None
                                        self.il_rx_pkt_count_ucast_pkt = None
                                        self.il_tx_pkt_count_ucast_pkt = None
                                        self.iqm_enq_pkt_cnt = None
                                        self.iqm_enq_byte_cnt = None
                                        self.iqm_deq_pkt_cnt = None
                                        self.iqm_deq_byte_cnt = None
                                        self.iqm_tot_dscrd_pkt_cnt = None
                                        self.iqm_tot_dscrd_byte_cnt = None
                                        self.iqm_ecc_1b_err_cnt = None
                                        self.iqm_ecc_2b_err_cnt = None
                                        self.iqm_parity_err_cnt = None
                                        self.iqm_deq_delete_pkt_cnt = None
                                        self.iqm_ecn_dscrd_msk_pkt_cnt = None
                                        self.iqm_q_tot_dscrd_pkt_cnt = None
                                        self.iqm_q_deq_delete_pkt_cnt = None
                                        self.iqm_rjct_db_pkt_cnt = None
                                        self.iqm_rjct_bdb_pkt_cnt = None
                                        self.iqm_rjct_bdb_protct_pkt_cnt = None
                                        self.iqm_rjct_oc_bd_pkt_cnt = None
                                        self.iqm_rjct_sn_err_pkt_cnt = None
                                        self.iqm_rjct_mc_err_pkt_cnt = None
                                        self.iqm_rjct_rsrc_err_pkt_cnt = None
                                        self.iqm_rjct_qnvalid_err_pkt_cnt = None
                                        self.iqm_rjct_cnm_pkt_cnt = None
                                        self.iqm_rjct_dyn_space_pkt_cnt = None
                                        self.ipt_fdt_pkt_cnt = None
                                        self.ipt_ecc_1b_err_cnt = None
                                        self.ipt_ecc_2b_err_cnt = None
                                        self.ipt_parity_err_cnt = None
                                        self.ipt_crc_err_cnt = None
                                        self.ipt_crc_err_del_buff_cnt = None
                                        self.ipt_cpu_del_buff_cnt = None
                                        self.ipt_cpu_rel_buff_cnt = None
                                        self.ipt_crc_err_buff_fifo_full_cnt = None
                                        self.fdt_data_cell_cnt = None
                                        self.fdt_data_byte_cnt = None
                                        self.fdt_crc_dropped_pck_cnt = None
                                        self.fdt_invalid_destq_drop_cell_cnt = None
                                        self.fdt_indirect_command_count = None
                                        self.fdt_ecc_1b_err_cnt = None
                                        self.fdt_ecc_2b_err_cnt = None
                                        self.fdt_parity_err_cnt = None
                                        self.fdt_crc_dropped_cell_cnt = None
                                        self.fcr_control_cell_cnt = None
                                        self.fcr_cell_drop_cnt = None
                                        self.fcr_credit_cell_drop_cnt = None
                                        self.fcr_fs_cell_drop_cnt = None
                                        self.fcr_rt_cell_drop_cnt = None
                                        self.fcr_ecc_1b_err_cnt = None
                                        self.fcr_ecc_2b_err_cnt = None
                                        self.fdr_data_cell_cnt = None
                                        self.fdr_data_byte_cnt = None
                                        self.fdr_crc_dropped_pck_cnt = None
                                        self.fdr_p_pkt_cnt = None
                                        self.fdr_prm_error_filter_cnt = None
                                        self.fdr_sec_error_filter_cnt = None
                                        self.fdr_prm_ecc_1b_err_cnt = None
                                        self.fdr_prm_ecc_2b_err_cnt = None
                                        self.fdr_sec_ecc_1b_err_cnt = None
                                        self.fdr_sec_ecc_2b_err_cnt = None
                                        self.egq_ecc_1b_err_cnt = None
                                        self.egq_ecc_2b_err_cnt = None
                                        self.egq_parity_err_cnt = None
                                        self.egq_dbf_ecc_1b_err_cnt = None
                                        self.egq_dbf_ecc_2b_err_cnt = None
                                        self.egq_empty_mcid_counter = None
                                        self.egq_rqp_discard_packet_counter = None
                                        self.egq_ehp_discard_packet_counter = None
                                        self.egq_ipt_pkt_cnt = None
                                        self.epni_epe_pkt_cnt = None
                                        self.epni_epe_byte_cnt = None
                                        self.epni_epe_discard_pkt_cnt = None
                                        self.epni_ecc_1b_err_cnt = None
                                        self.epni_ecc_2b_err_cnt = None
                                        self.epni_parity_err_cnt = None
                                        self.egq_pqp_ucast_pkt_cnt = None
                                        self.egq_pqp_ucast_h_pkt_cnt = None
                                        self.egq_pqp_ucast_l_pkt_cnt = None
                                        self.egq_pqp_ucast_bytes_cnt = None
                                        self.egq_pqp_ucast_discard_pkt_cnt = None
                                        self.egq_pqp_mcast_pkt_cnt = None
                                        self.egq_pqp_mcast_h_pkt_cnt = None
                                        self.egq_pqp_mcast_l_pkt_cnt = None
                                        self.egq_pqp_mcast_bytes_cnt = None
                                        self.egq_pqp_mcast_discard_pkt_cnt = None
                                        self.fct_control_cell_cnt = None
                                        self.fct_unrch_crdt_cnt = None
                                        self.idr_reassembly_errors = None
                                        self.idr_mmu_ecc_1b_err_cnt = None
                                        self.idr_mmu_ecc_2b_err_cnt = None
                                        self.idr_discarded_packets0_cnt = None
                                        self.idr_discarded_packets1_cnt = None
                                        self.idr_discarded_packets2_cnt = None
                                        self.idr_discarded_packets3_cnt = None
                                        self.idr_discarded_octets0_cnt = None
                                        self.idr_discarded_octets1_cnt = None
                                        self.idr_discarded_octets2_cnt = None
                                        self.idr_discarded_octets3_cnt = None
                                        self.mmu_ecc_1b_err_cnt = None
                                        self.mmu_ecc_2b_err_cnt = None
                                        self.oamp_parity_err_cnt = None
                                        self.oamp_ecc_1b_err_cnt = None
                                        self.oamp_ecc_2b_err_cnt = None
                                        self.crps_parity_err_cnt = None
                                        self.fmac0_kpcs0_tst_rx_err_cnt = None
                                        self.fmac1_kpcs0_tst_rx_err_cnt = None
                                        self.fmac2_kpcs0_tst_rx_err_cnt = None
                                        self.fmac3_kpcs0_tst_rx_err_cnt = None
                                        self.fmac4_kpcs0_tst_rx_err_cnt = None
                                        self.fmac5_kpcs0_tst_rx_err_cnt = None
                                        self.fmac6_kpcs0_tst_rx_err_cnt = None
                                        self.fmac7_kpcs0_tst_rx_err_cnt = None
                                        self.fmac8_kpcs0_tst_rx_err_cnt = None
                                        self.fmac0_kpcs1_tst_rx_err_cnt = None
                                        self.fmac1_kpcs1_tst_rx_err_cnt = None
                                        self.fmac2_kpcs1_tst_rx_err_cnt = None
                                        self.fmac3_kpcs1_tst_rx_err_cnt = None
                                        self.fmac4_kpcs1_tst_rx_err_cnt = None
                                        self.fmac5_kpcs1_tst_rx_err_cnt = None
                                        self.fmac6_kpcs1_tst_rx_err_cnt = None
                                        self.fmac7_kpcs1_tst_rx_err_cnt = None
                                        self.fmac8_kpcs1_tst_rx_err_cnt = None
                                        self.fmac0_kpcs2_tst_rx_err_cnt = None
                                        self.fmac1_kpcs2_tst_rx_err_cnt = None
                                        self.fmac2_kpcs2_tst_rx_err_cnt = None
                                        self.fmac3_kpcs2_tst_rx_err_cnt = None
                                        self.fmac4_kpcs2_tst_rx_err_cnt = None
                                        self.fmac5_kpcs2_tst_rx_err_cnt = None
                                        self.fmac6_kpcs2_tst_rx_err_cnt = None
                                        self.fmac7_kpcs2_tst_rx_err_cnt = None
                                        self.fmac8_kpcs2_tst_rx_err_cnt = None
                                        self.fmac0_kpcs3_tst_rx_err_cnt = None
                                        self.fmac1_kpcs3_tst_rx_err_cnt = None
                                        self.fmac2_kpcs3_tst_rx_err_cnt = None
                                        self.fmac3_kpcs3_tst_rx_err_cnt = None
                                        self.fmac4_kpcs3_tst_rx_err_cnt = None
                                        self.fmac5_kpcs3_tst_rx_err_cnt = None
                                        self.fmac6_kpcs3_tst_rx_err_cnt = None
                                        self.fmac7_kpcs3_tst_rx_err_cnt = None
                                        self.fmac8_kpcs3_tst_rx_err_cnt = None
                                        self.fmac0_tst0_err_cnt = None
                                        self.fmac1_tst0_err_cnt = None
                                        self.fmac2_tst0_err_cnt = None
                                        self.fmac3_tst0_err_cnt = None
                                        self.fmac4_tst0_err_cnt = None
                                        self.fmac5_tst0_err_cnt = None
                                        self.fmac6_tst0_err_cnt = None
                                        self.fmac7_tst0_err_cnt = None
                                        self.fmac8_tst0_err_cnt = None
                                        self.fmac0_tst1_err_cnt = None
                                        self.fmac1_tst1_err_cnt = None
                                        self.fmac2_tst1_err_cnt = None
                                        self.fmac3_tst1_err_cnt = None
                                        self.fmac4_tst1_err_cnt = None
                                        self.fmac5_tst1_err_cnt = None
                                        self.fmac6_tst1_err_cnt = None
                                        self.fmac7_tst1_err_cnt = None
                                        self.fmac8_tst1_err_cnt = None
                                        self.fmac0_tst2_err_cnt = None
                                        self.fmac1_tst2_err_cnt = None
                                        self.fmac2_tst2_err_cnt = None
                                        self.fmac3_tst2_err_cnt = None
                                        self.fmac4_tst2_err_cnt = None
                                        self.fmac5_tst2_err_cnt = None
                                        self.fmac6_tst2_err_cnt = None
                                        self.fmac7_tst2_err_cnt = None
                                        self.fmac8_tst2_err_cnt = None
                                        self.fmac0_tst3_err_cnt = None
                                        self.fmac1_tst3_err_cnt = None
                                        self.fmac2_tst3_err_cnt = None
                                        self.fmac3_tst3_err_cnt = None
                                        self.fmac4_tst3_err_cnt = None
                                        self.fmac5_tst3_err_cnt = None
                                        self.fmac6_tst3_err_cnt = None
                                        self.fmac7_tst3_err_cnt = None
                                        self.fmac8_tst3_err_cnt = None
                                        self.fmac0_ecc_1b_err_cnt = None
                                        self.fmac1_ecc_1b_err_cnt = None
                                        self.fmac2_ecc_1b_err_cnt = None
                                        self.fmac3_ecc_1b_err_cnt = None
                                        self.fmac4_ecc_1b_err_cnt = None
                                        self.fmac5_ecc_1b_err_cnt = None
                                        self.fmac6_ecc_1b_err_cnt = None
                                        self.fmac7_ecc_1b_err_cnt = None
                                        self.fmac8_ecc_1b_err_cnt = None
                                        self.fmac0_ecc_2b_err_cnt = None
                                        self.fmac1_ecc_2b_err_cnt = None
                                        self.fmac2_ecc_2b_err_cnt = None
                                        self.fmac3_ecc_2b_err_cnt = None
                                        self.fmac4_ecc_2b_err_cnt = None
                                        self.fmac5_ecc_2b_err_cnt = None
                                        self.fmac6_ecc_2b_err_cnt = None
                                        self.fmac7_ecc_2b_err_cnt = None
                                        self.fmac8_ecc_2b_err_cnt = None
                                        self.olp_incoming_bad_identifier_counter = None
                                        self.olp_incoming_bad_reassembly_counter = None
                                        self.cfc_parity_err_cnt = None
                                        self.cfc_ilkn0_oob_rx_crc_err_cntr = None
                                        self.cfc_ilkn1_oob_rx_crc_err_cntr = None
                                        self.cfc_spi_oob_rx0_frm_err_cnt = None
                                        self.cfc_spi_oob_rx0_dip2_err_cnt = None
                                        self.cfc_spi_oob_rx1_frm_err_cnt = None
                                        self.cfc_spi_oob_rx1_dip2_err_cnt = None
                                        self.cgm_cgm_uc_pd_dropped_cnt = None
                                        self.cgm_cgm_mc_rep_pd_dropped_cnt = None
                                        self.cgm_cgm_uc_db_dropped_by_rqp_cnt = None
                                        self.cgm_cgm_uc_db_dropped_by_pqp_cnt = None
                                        self.cgm_cgm_mc_rep_db_dropped_cnt = None
                                        self.cgm_cgm_mc_db_dropped_cnt = None
                                        self.drca_full_err_cnt = None
                                        self.drca_single_err_cnt = None
                                        self.drca_calib_bist_full_err_cnt = None
                                        self.drca_loopback_full_err_cnt = None
                                        self.drcb_full_err_cnt = None
                                        self.drcb_single_err_cnt = None
                                        self.drcb_calib_bist_full_err_cnt = None
                                        self.drcb_loopback_full_err_cnt = None
                                        self.drcc_full_err_cnt = None
                                        self.drcc_single_err_cnt = None
                                        self.drcc_calib_bist_full_err_cnt = None
                                        self.drcc_loopback_full_err_cnt = None
                                        self.drcd_full_err_cnt = None
                                        self.drcd_single_err_cnt = None
                                        self.drcd_calib_bist_full_err_cnt = None
                                        self.drcd_loopback_full_err_cnt = None
                                        self.drce_full_err_cnt = None
                                        self.drce_single_err_cnt = None
                                        self.drce_calib_bist_full_err_cnt = None
                                        self.drce_loopback_full_err_cnt = None
                                        self.drcf_full_err_cnt = None
                                        self.drcf_single_err_cnt = None
                                        self.drcf_calib_bist_full_err_cnt = None
                                        self.drcf_loopback_full_err_cnt = None
                                        self.drcg_full_err_cnt = None
                                        self.drcg_single_err_cnt = None
                                        self.drcg_calib_bist_full_err_cnt = None
                                        self.drcg_loopback_full_err_cnt = None
                                        self.drch_full_err_cnt = None
                                        self.drch_single_err_cnt = None
                                        self.drch_calib_bist_full_err_cnt = None
                                        self.drch_loopback_full_err_cnt = None
                                        self.drcbroadcast_full_err_cnt = None
                                        self.drcbroadcast_single_err_cnt = None
                                        self.drcbroadcast_calib_bist_full_err_cnt = None
                                        self.drcbroadcast_loopback_full_err_cnt = None
                                        self.otn_mode = None
                                        self.num_ports = None

                                        self.aggr_stats_otn = YList(self)
                                        self._segment_path = lambda: "aggr-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats, ['rx_internal_error', 'rx_internal_drop', 'tx_internal_error', 'tx_internal_drop', 'cmic_cmc0_pkt_count_tx_pkt', 'cmic_cmc0_pkt_count_rx_pkt', 'nbi_stat_rx_bursts_err_cnt', 'nbi_ecc_1b_err_cnt', 'nbi_ecc_2b_err_cnt', 'nbi_parity_err_cnt', 'nbi_rx_ilkn_crc32_err_cnt', 'nbi_rx_ilkn0_crc24_err_cnt', 'nbi_rx_ilkn0_burst_err_cnt', 'nbi_rx_ilkn0_miss_sop_err_cnt', 'nbi_rx_ilkn0_miss_eop_err_cnt', 'nbi_rx_ilkn0_misaligned_cnt', 'nbi_rx_ilkn1_crc24_err_cnt', 'nbi_rx_ilkn1_burst_err_cnt', 'nbi_rx_ilkn1_miss_sop_err_cnt', 'nbi_rx_ilkn1_miss_eop_err_cnt', 'nbi_rx_ilkn1_misaligned_cnt', 'nbi_tx_ilkn1_flushed_bursts_cnt', 'nbi_rx_ilkn0_retrans_crc24_err_cnt', 'nbi_rx_ilkn0_retrans_retry_err_cnt', 'nbi_rx_ilkn0_retrans_wdog_err_cnt', 'nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt', 'nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt', 'nbi_rx_ilkn0_retrans_reached_timeout_err_cnt', 'nbi_rx_ilkn1_retrans_crc24_err_cnt', 'nbi_rx_ilkn1_retrans_retry_err_cnt', 'nbi_rx_ilkn1_retrans_wdog_err_cnt', 'nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt', 'nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt', 'nbi_rx_ilkn1_retrans_reached_timeout_err_cnt', 'nbi_stat_rx_frame_err_cnt', 'nbi_stat_tx_frame_err_cnt', 'nbi_rx_elk_err_bursts_cnt', 'nbi_rx_num_thrown_eops', 'nbi_rx_num_runts', 'nbi_bist_tx_crc_err_bursts_cnt', 'nbi_bist_rx_err_length_bursts_cnt', 'nbi_bist_rx_err_burst_index_cnt', 'nbi_bist_rx_err_bct_cnt', 'nbi_bist_rx_err_data_cnt', 'nbi_bist_rx_err_in_crc_err_cnt', 'nbi_bist_rx_err_sob_cnt', 'nbi_stat_tx_bursts_cnt', 'nbi_stat_tx_total_leng_cnt', 'rxaui_total_tx_pkt_count', 'rxaui_total_rx_pkt_count', 'rxaui_rx_pkt_count_bcast_pkt', 'rxaui_tx_pkt_count_bcast_pkt', 'rxaui_rx_pkt_count_mcast_pkt', 'rxaui_tx_pkt_count_mcast_pkt', 'rxaui_rx_pkt_count_ucast_pkt', 'rxaui_tx_pkt_count_ucast_pkt', 'rxaui_rx_err_drop_pkt_cnt', 'rxaui_tx_err_drop_pkt_cnt', 'rxaui_byte_count_tx_pkt', 'rxaui_byte_count_rx_pkt', 'rxaui_rx_dscrd_pkt_cnt', 'rxaui_tx_dscrd_pkt_cnt', 'ire_nif_packet_counter', 'il_total_rx_pkt_count', 'il_total_tx_pkt_count', 'il_rx_err_drop_pkt_cnt', 'il_tx_err_drop_pkt_cnt', 'il_byte_count_tx_pkt', 'il_byte_count_rx_pkt', 'il_rx_dscrd_pkt_cnt', 'il_tx_dscrd_pkt_cnt', 'il_rx_pkt_count_bcast_pkt', 'il_tx_pkt_count_bcast_pkt', 'il_rx_pkt_count_mcast_pkt', 'il_tx_pkt_count_mcast_pkt', 'il_rx_pkt_count_ucast_pkt', 'il_tx_pkt_count_ucast_pkt', 'iqm_enq_pkt_cnt', 'iqm_enq_byte_cnt', 'iqm_deq_pkt_cnt', 'iqm_deq_byte_cnt', 'iqm_tot_dscrd_pkt_cnt', 'iqm_tot_dscrd_byte_cnt', 'iqm_ecc_1b_err_cnt', 'iqm_ecc_2b_err_cnt', 'iqm_parity_err_cnt', 'iqm_deq_delete_pkt_cnt', 'iqm_ecn_dscrd_msk_pkt_cnt', 'iqm_q_tot_dscrd_pkt_cnt', 'iqm_q_deq_delete_pkt_cnt', 'iqm_rjct_db_pkt_cnt', 'iqm_rjct_bdb_pkt_cnt', 'iqm_rjct_bdb_protct_pkt_cnt', 'iqm_rjct_oc_bd_pkt_cnt', 'iqm_rjct_sn_err_pkt_cnt', 'iqm_rjct_mc_err_pkt_cnt', 'iqm_rjct_rsrc_err_pkt_cnt', 'iqm_rjct_qnvalid_err_pkt_cnt', 'iqm_rjct_cnm_pkt_cnt', 'iqm_rjct_dyn_space_pkt_cnt', 'ipt_fdt_pkt_cnt', 'ipt_ecc_1b_err_cnt', 'ipt_ecc_2b_err_cnt', 'ipt_parity_err_cnt', 'ipt_crc_err_cnt', 'ipt_crc_err_del_buff_cnt', 'ipt_cpu_del_buff_cnt', 'ipt_cpu_rel_buff_cnt', 'ipt_crc_err_buff_fifo_full_cnt', 'fdt_data_cell_cnt', 'fdt_data_byte_cnt', 'fdt_crc_dropped_pck_cnt', 'fdt_invalid_destq_drop_cell_cnt', 'fdt_indirect_command_count', 'fdt_ecc_1b_err_cnt', 'fdt_ecc_2b_err_cnt', 'fdt_parity_err_cnt', 'fdt_crc_dropped_cell_cnt', 'fcr_control_cell_cnt', 'fcr_cell_drop_cnt', 'fcr_credit_cell_drop_cnt', 'fcr_fs_cell_drop_cnt', 'fcr_rt_cell_drop_cnt', 'fcr_ecc_1b_err_cnt', 'fcr_ecc_2b_err_cnt', 'fdr_data_cell_cnt', 'fdr_data_byte_cnt', 'fdr_crc_dropped_pck_cnt', 'fdr_p_pkt_cnt', 'fdr_prm_error_filter_cnt', 'fdr_sec_error_filter_cnt', 'fdr_prm_ecc_1b_err_cnt', 'fdr_prm_ecc_2b_err_cnt', 'fdr_sec_ecc_1b_err_cnt', 'fdr_sec_ecc_2b_err_cnt', 'egq_ecc_1b_err_cnt', 'egq_ecc_2b_err_cnt', 'egq_parity_err_cnt', 'egq_dbf_ecc_1b_err_cnt', 'egq_dbf_ecc_2b_err_cnt', 'egq_empty_mcid_counter', 'egq_rqp_discard_packet_counter', 'egq_ehp_discard_packet_counter', 'egq_ipt_pkt_cnt', 'epni_epe_pkt_cnt', 'epni_epe_byte_cnt', 'epni_epe_discard_pkt_cnt', 'epni_ecc_1b_err_cnt', 'epni_ecc_2b_err_cnt', 'epni_parity_err_cnt', 'egq_pqp_ucast_pkt_cnt', 'egq_pqp_ucast_h_pkt_cnt', 'egq_pqp_ucast_l_pkt_cnt', 'egq_pqp_ucast_bytes_cnt', 'egq_pqp_ucast_discard_pkt_cnt', 'egq_pqp_mcast_pkt_cnt', 'egq_pqp_mcast_h_pkt_cnt', 'egq_pqp_mcast_l_pkt_cnt', 'egq_pqp_mcast_bytes_cnt', 'egq_pqp_mcast_discard_pkt_cnt', 'fct_control_cell_cnt', 'fct_unrch_crdt_cnt', 'idr_reassembly_errors', 'idr_mmu_ecc_1b_err_cnt', 'idr_mmu_ecc_2b_err_cnt', 'idr_discarded_packets0_cnt', 'idr_discarded_packets1_cnt', 'idr_discarded_packets2_cnt', 'idr_discarded_packets3_cnt', 'idr_discarded_octets0_cnt', 'idr_discarded_octets1_cnt', 'idr_discarded_octets2_cnt', 'idr_discarded_octets3_cnt', 'mmu_ecc_1b_err_cnt', 'mmu_ecc_2b_err_cnt', 'oamp_parity_err_cnt', 'oamp_ecc_1b_err_cnt', 'oamp_ecc_2b_err_cnt', 'crps_parity_err_cnt', 'fmac0_kpcs0_tst_rx_err_cnt', 'fmac1_kpcs0_tst_rx_err_cnt', 'fmac2_kpcs0_tst_rx_err_cnt', 'fmac3_kpcs0_tst_rx_err_cnt', 'fmac4_kpcs0_tst_rx_err_cnt', 'fmac5_kpcs0_tst_rx_err_cnt', 'fmac6_kpcs0_tst_rx_err_cnt', 'fmac7_kpcs0_tst_rx_err_cnt', 'fmac8_kpcs0_tst_rx_err_cnt', 'fmac0_kpcs1_tst_rx_err_cnt', 'fmac1_kpcs1_tst_rx_err_cnt', 'fmac2_kpcs1_tst_rx_err_cnt', 'fmac3_kpcs1_tst_rx_err_cnt', 'fmac4_kpcs1_tst_rx_err_cnt', 'fmac5_kpcs1_tst_rx_err_cnt', 'fmac6_kpcs1_tst_rx_err_cnt', 'fmac7_kpcs1_tst_rx_err_cnt', 'fmac8_kpcs1_tst_rx_err_cnt', 'fmac0_kpcs2_tst_rx_err_cnt', 'fmac1_kpcs2_tst_rx_err_cnt', 'fmac2_kpcs2_tst_rx_err_cnt', 'fmac3_kpcs2_tst_rx_err_cnt', 'fmac4_kpcs2_tst_rx_err_cnt', 'fmac5_kpcs2_tst_rx_err_cnt', 'fmac6_kpcs2_tst_rx_err_cnt', 'fmac7_kpcs2_tst_rx_err_cnt', 'fmac8_kpcs2_tst_rx_err_cnt', 'fmac0_kpcs3_tst_rx_err_cnt', 'fmac1_kpcs3_tst_rx_err_cnt', 'fmac2_kpcs3_tst_rx_err_cnt', 'fmac3_kpcs3_tst_rx_err_cnt', 'fmac4_kpcs3_tst_rx_err_cnt', 'fmac5_kpcs3_tst_rx_err_cnt', 'fmac6_kpcs3_tst_rx_err_cnt', 'fmac7_kpcs3_tst_rx_err_cnt', 'fmac8_kpcs3_tst_rx_err_cnt', 'fmac0_tst0_err_cnt', 'fmac1_tst0_err_cnt', 'fmac2_tst0_err_cnt', 'fmac3_tst0_err_cnt', 'fmac4_tst0_err_cnt', 'fmac5_tst0_err_cnt', 'fmac6_tst0_err_cnt', 'fmac7_tst0_err_cnt', 'fmac8_tst0_err_cnt', 'fmac0_tst1_err_cnt', 'fmac1_tst1_err_cnt', 'fmac2_tst1_err_cnt', 'fmac3_tst1_err_cnt', 'fmac4_tst1_err_cnt', 'fmac5_tst1_err_cnt', 'fmac6_tst1_err_cnt', 'fmac7_tst1_err_cnt', 'fmac8_tst1_err_cnt', 'fmac0_tst2_err_cnt', 'fmac1_tst2_err_cnt', 'fmac2_tst2_err_cnt', 'fmac3_tst2_err_cnt', 'fmac4_tst2_err_cnt', 'fmac5_tst2_err_cnt', 'fmac6_tst2_err_cnt', 'fmac7_tst2_err_cnt', 'fmac8_tst2_err_cnt', 'fmac0_tst3_err_cnt', 'fmac1_tst3_err_cnt', 'fmac2_tst3_err_cnt', 'fmac3_tst3_err_cnt', 'fmac4_tst3_err_cnt', 'fmac5_tst3_err_cnt', 'fmac6_tst3_err_cnt', 'fmac7_tst3_err_cnt', 'fmac8_tst3_err_cnt', 'fmac0_ecc_1b_err_cnt', 'fmac1_ecc_1b_err_cnt', 'fmac2_ecc_1b_err_cnt', 'fmac3_ecc_1b_err_cnt', 'fmac4_ecc_1b_err_cnt', 'fmac5_ecc_1b_err_cnt', 'fmac6_ecc_1b_err_cnt', 'fmac7_ecc_1b_err_cnt', 'fmac8_ecc_1b_err_cnt', 'fmac0_ecc_2b_err_cnt', 'fmac1_ecc_2b_err_cnt', 'fmac2_ecc_2b_err_cnt', 'fmac3_ecc_2b_err_cnt', 'fmac4_ecc_2b_err_cnt', 'fmac5_ecc_2b_err_cnt', 'fmac6_ecc_2b_err_cnt', 'fmac7_ecc_2b_err_cnt', 'fmac8_ecc_2b_err_cnt', 'olp_incoming_bad_identifier_counter', 'olp_incoming_bad_reassembly_counter', 'cfc_parity_err_cnt', 'cfc_ilkn0_oob_rx_crc_err_cntr', 'cfc_ilkn1_oob_rx_crc_err_cntr', 'cfc_spi_oob_rx0_frm_err_cnt', 'cfc_spi_oob_rx0_dip2_err_cnt', 'cfc_spi_oob_rx1_frm_err_cnt', 'cfc_spi_oob_rx1_dip2_err_cnt', 'cgm_cgm_uc_pd_dropped_cnt', 'cgm_cgm_mc_rep_pd_dropped_cnt', 'cgm_cgm_uc_db_dropped_by_rqp_cnt', 'cgm_cgm_uc_db_dropped_by_pqp_cnt', 'cgm_cgm_mc_rep_db_dropped_cnt', 'cgm_cgm_mc_db_dropped_cnt', 'drca_full_err_cnt', 'drca_single_err_cnt', 'drca_calib_bist_full_err_cnt', 'drca_loopback_full_err_cnt', 'drcb_full_err_cnt', 'drcb_single_err_cnt', 'drcb_calib_bist_full_err_cnt', 'drcb_loopback_full_err_cnt', 'drcc_full_err_cnt', 'drcc_single_err_cnt', 'drcc_calib_bist_full_err_cnt', 'drcc_loopback_full_err_cnt', 'drcd_full_err_cnt', 'drcd_single_err_cnt', 'drcd_calib_bist_full_err_cnt', 'drcd_loopback_full_err_cnt', 'drce_full_err_cnt', 'drce_single_err_cnt', 'drce_calib_bist_full_err_cnt', 'drce_loopback_full_err_cnt', 'drcf_full_err_cnt', 'drcf_single_err_cnt', 'drcf_calib_bist_full_err_cnt', 'drcf_loopback_full_err_cnt', 'drcg_full_err_cnt', 'drcg_single_err_cnt', 'drcg_calib_bist_full_err_cnt', 'drcg_loopback_full_err_cnt', 'drch_full_err_cnt', 'drch_single_err_cnt', 'drch_calib_bist_full_err_cnt', 'drch_loopback_full_err_cnt', 'drcbroadcast_full_err_cnt', 'drcbroadcast_single_err_cnt', 'drcbroadcast_calib_bist_full_err_cnt', 'drcbroadcast_loopback_full_err_cnt', 'otn_mode', 'num_ports'], name, value)


                                    class AggrStatsOtn(Entity):
                                        """
                                        aggr stats otn
                                        
                                        .. attribute:: il_total_rx_pkt_count
                                        
                                        	IL TotalRxPktCount
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: il_total_tx_pkt_count
                                        
                                        	IL TotalTxPktCount
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2017-08-29'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats.AggrStatsOtn, self).__init__()

                                            self.yang_name = "aggr-stats-otn"
                                            self.yang_parent_name = "aggr-stats"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('il_total_rx_pkt_count', (YLeaf(YType.uint64, 'il-total-rx-pkt-count'), ['int'])),
                                                ('il_total_tx_pkt_count', (YLeaf(YType.uint64, 'il-total-tx-pkt-count'), ['int'])),
                                            ])
                                            self.il_total_rx_pkt_count = None
                                            self.il_total_tx_pkt_count = None
                                            self._segment_path = lambda: "aggr-stats-otn"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.AggrStats.AggrStatsOtn, ['il_total_rx_pkt_count', 'il_total_tx_pkt_count'], name, value)




                                class OvfStatus(Entity):
                                    """
                                    ovf status
                                    
                                    .. attribute:: cmic_cmc0_pkt_count_tx_pkt
                                    
                                    	CMIC Cmc0PktCountTxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cmic_cmc0_pkt_count_rx_pkt
                                    
                                    	CMIC Cmc0PktCountRxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_rx_bursts_err_cnt
                                    
                                    	NBI StatRxBurstsErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_ecc_1b_err_cnt
                                    
                                    	NBI Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_ecc_2b_err_cnt
                                    
                                    	NBI Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_parity_err_cnt
                                    
                                    	NBI ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn_crc32_err_cnt
                                    
                                    	NBI RxIlknCrc32ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_crc24_err_cnt
                                    
                                    	NBI RxIlkn0Crc24ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_burst_err_cnt
                                    
                                    	NBI RxIlkn0BurstErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_miss_sop_err_cnt
                                    
                                    	NBI RxIlkn0MissSopErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_miss_eop_err_cnt
                                    
                                    	NBI RxIlkn0MissEopErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_misaligned_cnt
                                    
                                    	NBI RxIlkn0MisalignedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_crc24_err_cnt
                                    
                                    	NBI RxIlkn1Crc24ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_burst_err_cnt
                                    
                                    	NBI RxIlkn1BurstErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_miss_sop_err_cnt
                                    
                                    	NBI RxIlkn1MissSopErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_miss_eop_err_cnt
                                    
                                    	NBI RxIlkn1MissEopErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_misaligned_cnt
                                    
                                    	NBI RxIlkn1MisalignedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_tx_ilkn1_flushed_bursts_cnt
                                    
                                    	NBI TxIlkn1FlushedBurstsCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_crc24_err_cnt
                                    
                                    	NBI RxIlkn0RetransCRC24ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_retry_err_cnt
                                    
                                    	NBI RxIlkn0RetransRetryErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wdog_err_cnt
                                    
                                    	NBI RxIlkn0RetransWdogErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt
                                    
                                    	NBI RxIlkn0RetransWrapAfterDiscErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt
                                    
                                    	NBI RxIlkn0RetransWrapB4DiscErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn0_retrans_reached_timeout_err_cnt
                                    
                                    	NBI RxIlkn0RetransReachedTimeoutErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_crc24_err_cnt
                                    
                                    	NBI RxIlkn1RetransCRC24ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_retry_err_cnt
                                    
                                    	NBI RxIlkn1RetransRetryErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wdog_err_cnt
                                    
                                    	NBI RxIlkn1RetransWdogErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt
                                    
                                    	NBI RxIlkn1RetransWrapAfterDiscErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt
                                    
                                    	NBI RxIlkn1RetransWrapB4DiscErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_ilkn1_retrans_reached_timeout_err_cnt
                                    
                                    	NBI RxIlkn1RetransReachedTimeoutErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_rx_frame_err_cnt
                                    
                                    	NBI StatRxFrameErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_frame_err_cnt
                                    
                                    	NBI StatTxFrameErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_elk_err_bursts_cnt
                                    
                                    	NBI RxElkErrBurstsCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_num_thrown_eops
                                    
                                    	NBI RxNumThrownEops
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_rx_num_runts
                                    
                                    	NBI RxNumRunts
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_tx_crc_err_bursts_cnt
                                    
                                    	NBI BistTxCrcErrBurstsCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_length_bursts_cnt
                                    
                                    	NBI BistRxErrLengthBurstsCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_burst_index_cnt
                                    
                                    	NBI BistRxErrBurstIndexCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_bct_cnt
                                    
                                    	NBI BistRxErrBctCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_data_cnt
                                    
                                    	NBI BistRxErrDataCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_in_crc_err_cnt
                                    
                                    	NBI BistRxErrInCrcErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_bist_rx_err_sob_cnt
                                    
                                    	NBI BistRxErrSobCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_bursts_cnt
                                    
                                    	NBI StatTxBurstsCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nbi_stat_tx_total_leng_cnt
                                    
                                    	NBI StatTxTotalLengCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_total_tx_pkt_count
                                    
                                    	RXAUI TotalTxPktCount
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_total_rx_pkt_count
                                    
                                    	RXAUI TotalRxPktCount
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_bcast_pkt
                                    
                                    	RXAUI RxPktCountBcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_bcast_pkt
                                    
                                    	RXAUI TxPktCountBcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_mcast_pkt
                                    
                                    	RXAUI RxPktCountMcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_mcast_pkt
                                    
                                    	RXAUI TxPktCountMcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_pkt_count_ucast_pkt
                                    
                                    	RXAUI RxPktCountUcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_pkt_count_ucast_pkt
                                    
                                    	RXAUI TxPktCountUcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_err_drop_pkt_cnt
                                    
                                    	RXAUI RxErrDropPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_err_drop_pkt_cnt
                                    
                                    	RXAUI TxErrDropPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_byte_count_tx_pkt
                                    
                                    	RXAUI ByteCountTxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_byte_count_rx_pkt
                                    
                                    	RXAUI ByteCountRxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_rx_dscrd_pkt_cnt
                                    
                                    	RXAUI RxDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rxaui_tx_dscrd_pkt_cnt
                                    
                                    	RXAUI TxDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ire_nif_packet_counter
                                    
                                    	IRE NifPacketCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_total_rx_pkt_count
                                    
                                    	IL TotalRxPktCount
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_total_tx_pkt_count
                                    
                                    	IL TotalTxPktCount
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_err_drop_pkt_cnt
                                    
                                    	IL RxErrDropPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_err_drop_pkt_cnt
                                    
                                    	IL TxErrDropPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_byte_count_tx_pkt
                                    
                                    	IL ByteCountTxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_byte_count_rx_pkt
                                    
                                    	IL ByteCountRxPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_dscrd_pkt_cnt
                                    
                                    	IL RxDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_dscrd_pkt_cnt
                                    
                                    	IL TxDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_bcast_pkt
                                    
                                    	IL RxPktCountBcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_bcast_pkt
                                    
                                    	IL TxPktCountBcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_mcast_pkt
                                    
                                    	IL RxPktCountMcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_mcast_pkt
                                    
                                    	IL TxPktCountMcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_rx_pkt_count_ucast_pkt
                                    
                                    	IL RxPktCountUcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: il_tx_pkt_count_ucast_pkt
                                    
                                    	IL TxPktCountUcastPkt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_enq_pkt_cnt
                                    
                                    	IQM EnqPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_enq_byte_cnt
                                    
                                    	IQM EnqByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_pkt_cnt
                                    
                                    	IQM DeqPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_byte_cnt
                                    
                                    	IQM DeqByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_tot_dscrd_pkt_cnt
                                    
                                    	IQM TotDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_tot_dscrd_byte_cnt
                                    
                                    	IQM TotDscrdByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecc_1b_err_cnt
                                    
                                    	IQM Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecc_2b_err_cnt
                                    
                                    	IQM Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_parity_err_cnt
                                    
                                    	IQM ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_deq_delete_pkt_cnt
                                    
                                    	IQM DeqDeletePktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_ecn_dscrd_msk_pkt_cnt
                                    
                                    	IQM EcnDscrdMskPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_q_tot_dscrd_pkt_cnt
                                    
                                    	IQM QTotDscrdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_q_deq_delete_pkt_cnt
                                    
                                    	IQM QDeqDeletePktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_db_pkt_cnt
                                    
                                    	IQM RjctDbPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_bdb_pkt_cnt
                                    
                                    	IQM RjctBdbPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_bdb_protct_pkt_cnt
                                    
                                    	IQM RjctBdbProtctPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_oc_bd_pkt_cnt
                                    
                                    	IQM RjctOcBdPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_sn_err_pkt_cnt
                                    
                                    	IQM RjctSnErrPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_mc_err_pkt_cnt
                                    
                                    	IQM RjctMcErrPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_rsrc_err_pkt_cnt
                                    
                                    	IQM RjctRsrcErrPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_qnvalid_err_pkt_cnt
                                    
                                    	IQM RjctQnvalidErrPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_cnm_pkt_cnt
                                    
                                    	IQM RjctCnmPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: iqm_rjct_dyn_space_pkt_cnt
                                    
                                    	IQM RjctDynSpacePktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_fdt_pkt_cnt
                                    
                                    	IPT FdtPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_ecc_1b_err_cnt
                                    
                                    	IPT Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_ecc_2b_err_cnt
                                    
                                    	IPT Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_parity_err_cnt
                                    
                                    	IPT ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_cnt
                                    
                                    	IPT CrcErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_del_buff_cnt
                                    
                                    	IPT CrcErrDelBuffCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_cpu_del_buff_cnt
                                    
                                    	IPT CpuDelBuffCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_cpu_rel_buff_cnt
                                    
                                    	IPT CpuRelBuffCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipt_crc_err_buff_fifo_full_cnt
                                    
                                    	IPT CrcErrBuffFifoFullCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_data_cell_cnt
                                    
                                    	FDT DataCellCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_data_byte_cnt
                                    
                                    	FDT DataByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_crc_dropped_pck_cnt
                                    
                                    	FDT CrcDroppedPckCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_invalid_destq_drop_cell_cnt
                                    
                                    	FDT invalid destq drop cell cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_indirect_command_count
                                    
                                    	FDT IndirectCommandCount
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_ecc_1b_err_cnt
                                    
                                    	FDT Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_ecc_2b_err_cnt
                                    
                                    	FDT Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_parity_err_cnt
                                    
                                    	FDT ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdt_crc_dropped_cell_cnt
                                    
                                    	FDT CrcDroppedCellCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_control_cell_cnt
                                    
                                    	FCR ControlCellCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_cell_drop_cnt
                                    
                                    	FCR CellDropCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_credit_cell_drop_cnt
                                    
                                    	FCR CreditCellDropCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_fs_cell_drop_cnt
                                    
                                    	FCR FSCellDropCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_rt_cell_drop_cnt
                                    
                                    	FCR RTCellDropCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_ecc_1b_err_cnt
                                    
                                    	FCR Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fcr_ecc_2b_err_cnt
                                    
                                    	FCR Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_data_cell_cnt
                                    
                                    	FDR DataCellCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_data_byte_cnt
                                    
                                    	FDR DataByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_crc_dropped_pck_cnt
                                    
                                    	FDR CrcDroppedPckCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_p_pkt_cnt
                                    
                                    	FDR PPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_error_filter_cnt
                                    
                                    	FDR PrmErrorFilterCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_error_filter_cnt
                                    
                                    	FDR SecErrorFilterCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_ecc_1b_err_cnt
                                    
                                    	FDR PrmEcc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_prm_ecc_2b_err_cnt
                                    
                                    	FDR PrmEcc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_ecc_1b_err_cnt
                                    
                                    	FDR SecEcc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fdr_sec_ecc_2b_err_cnt
                                    
                                    	FDR SecEcc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ecc_1b_err_cnt
                                    
                                    	EGQ Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ecc_2b_err_cnt
                                    
                                    	EGQ Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_parity_err_cnt
                                    
                                    	EGQ ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_dbf_ecc_1b_err_cnt
                                    
                                    	EGQ DbfEcc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_dbf_ecc_2b_err_cnt
                                    
                                    	EGQ DbfEcc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_empty_mcid_counter
                                    
                                    	EGQ EmptyMcidCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_rqp_discard_packet_counter
                                    
                                    	EGQ RqpDiscardPacketCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ehp_discard_packet_counter
                                    
                                    	EGQ EhpDiscardPacketCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_ipt_pkt_cnt
                                    
                                    	EGQ IptPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_pkt_cnt
                                    
                                    	EPNI EpePktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_byte_cnt
                                    
                                    	EPNI EpeByteCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_epe_discard_pkt_cnt
                                    
                                    	EPNI EpeDiscardPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_ecc_1b_err_cnt
                                    
                                    	EPNI Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_ecc_2b_err_cnt
                                    
                                    	EPNI Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: epni_parity_err_cnt
                                    
                                    	EPNI ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_pkt_cnt
                                    
                                    	EGQ PqpUcastPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_h_pkt_cnt
                                    
                                    	EGQ PqpUcastHPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_l_pkt_cnt
                                    
                                    	EGQ PqpUcastLPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_bytes_cnt
                                    
                                    	EGQ PqpUcastBytesCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_ucast_discard_pkt_cnt
                                    
                                    	EGQ PqpUcastDiscardPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_pkt_cnt
                                    
                                    	EGQ PqpMcastPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_h_pkt_cnt
                                    
                                    	EGQ PqpMcastHPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_l_pkt_cnt
                                    
                                    	EGQ PqpMcastLPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_bytes_cnt
                                    
                                    	EGQ PqpMcastBytesCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: egq_pqp_mcast_discard_pkt_cnt
                                    
                                    	EGQ PqpMcastDiscardPktCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fct_control_cell_cnt
                                    
                                    	FCT ControlCellCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fct_unrch_crdt_cnt
                                    
                                    	FCT UnrchCrdtCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_reassembly_errors
                                    
                                    	IDR ReassemblyErrors
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_mmu_ecc_1b_err_cnt
                                    
                                    	IDR MmuEcc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_mmu_ecc_2b_err_cnt
                                    
                                    	IDR MmuEcc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets0_cnt
                                    
                                    	IDR DiscardedPackets0Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets1_cnt
                                    
                                    	IDR DiscardedPackets1Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets2_cnt
                                    
                                    	IDR DiscardedPackets2Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_packets3_cnt
                                    
                                    	IDR DiscardedPackets3Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets0_cnt
                                    
                                    	IDR DiscardedOctets0Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets1_cnt
                                    
                                    	IDR DiscardedOctets1Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets2_cnt
                                    
                                    	IDR DiscardedOctets2Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: idr_discarded_octets3_cnt
                                    
                                    	IDR DiscardedOctets3Cnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mmu_ecc_1b_err_cnt
                                    
                                    	MMU Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mmu_ecc_2b_err_cnt
                                    
                                    	MMU Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_parity_err_cnt
                                    
                                    	OAMP ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_ecc_1b_err_cnt
                                    
                                    	OAMP Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: oamp_ecc_2b_err_cnt
                                    
                                    	OAMP Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: crps_parity_err_cnt
                                    
                                    	CRPS ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs0_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs0TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs1_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs1TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs2_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs2TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC0 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC1 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC2 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC3 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC4 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC5 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC6 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC7 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_kpcs3_tst_rx_err_cnt
                                    
                                    	FMAC8 Kpcs3TstRxErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst0_err_cnt
                                    
                                    	FMAC0 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst0_err_cnt
                                    
                                    	FMAC1 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst0_err_cnt
                                    
                                    	FMAC2 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst0_err_cnt
                                    
                                    	FMAC3 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst0_err_cnt
                                    
                                    	FMAC4 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst0_err_cnt
                                    
                                    	FMAC5 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst0_err_cnt
                                    
                                    	FMAC6 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst0_err_cnt
                                    
                                    	FMAC7 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst0_err_cnt
                                    
                                    	FMAC8 Tst0ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst1_err_cnt
                                    
                                    	FMAC0 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst1_err_cnt
                                    
                                    	FMAC1 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst1_err_cnt
                                    
                                    	FMAC2 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst1_err_cnt
                                    
                                    	FMAC3 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst1_err_cnt
                                    
                                    	FMAC4 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst1_err_cnt
                                    
                                    	FMAC5 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst1_err_cnt
                                    
                                    	FMAC6 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst1_err_cnt
                                    
                                    	FMAC7 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst1_err_cnt
                                    
                                    	FMAC8 Tst1ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst2_err_cnt
                                    
                                    	FMAC0 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst2_err_cnt
                                    
                                    	FMAC1 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst2_err_cnt
                                    
                                    	FMAC2 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst2_err_cnt
                                    
                                    	FMAC3 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst2_err_cnt
                                    
                                    	FMAC4 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst2_err_cnt
                                    
                                    	FMAC5 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst2_err_cnt
                                    
                                    	FMAC6 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst2_err_cnt
                                    
                                    	FMAC7 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst2_err_cnt
                                    
                                    	FMAC8 Tst2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_tst3_err_cnt
                                    
                                    	FMAC0 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_tst3_err_cnt
                                    
                                    	FMAC1 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_tst3_err_cnt
                                    
                                    	FMAC2 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_tst3_err_cnt
                                    
                                    	FMAC3 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_tst3_err_cnt
                                    
                                    	FMAC4 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_tst3_err_cnt
                                    
                                    	FMAC5 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_tst3_err_cnt
                                    
                                    	FMAC6 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_tst3_err_cnt
                                    
                                    	FMAC7 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_tst3_err_cnt
                                    
                                    	FMAC8 Tst3ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_ecc_1b_err_cnt
                                    
                                    	FMAC0 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_ecc_1b_err_cnt
                                    
                                    	FMAC1 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_ecc_1b_err_cnt
                                    
                                    	FMAC2 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_ecc_1b_err_cnt
                                    
                                    	FMAC3 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_ecc_1b_err_cnt
                                    
                                    	FMAC4 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_ecc_1b_err_cnt
                                    
                                    	FMAC5 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_ecc_1b_err_cnt
                                    
                                    	FMAC6 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_ecc_1b_err_cnt
                                    
                                    	FMAC7 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_ecc_1b_err_cnt
                                    
                                    	FMAC8 Ecc 1bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac0_ecc_2b_err_cnt
                                    
                                    	FMAC0 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac1_ecc_2b_err_cnt
                                    
                                    	FMAC1 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac2_ecc_2b_err_cnt
                                    
                                    	FMAC2 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac3_ecc_2b_err_cnt
                                    
                                    	FMAC3 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac4_ecc_2b_err_cnt
                                    
                                    	FMAC4 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac5_ecc_2b_err_cnt
                                    
                                    	FMAC5 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac6_ecc_2b_err_cnt
                                    
                                    	FMAC6 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac7_ecc_2b_err_cnt
                                    
                                    	FMAC7 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac8_ecc_2b_err_cnt
                                    
                                    	FMAC8 Ecc 2bErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: olp_incoming_bad_identifier_counter
                                    
                                    	OLP IncomingBadIdentifierCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: olp_incoming_bad_reassembly_counter
                                    
                                    	OLP IncomingBadReassemblyCounter
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_parity_err_cnt
                                    
                                    	CFC ParityErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_ilkn0_oob_rx_crc_err_cntr
                                    
                                    	CFC Ilkn0OobRxCrcErrCntr
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_ilkn1_oob_rx_crc_err_cntr
                                    
                                    	CFC Ilkn1OobRxCrcErrCntr
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx0_frm_err_cnt
                                    
                                    	CFC SpiOobRx0FrmErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx0_dip2_err_cnt
                                    
                                    	CFC SpiOobRx0Dip2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx1_frm_err_cnt
                                    
                                    	CFC SpiOobRx1FrmErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cfc_spi_oob_rx1_dip2_err_cnt
                                    
                                    	CFC SpiOobRx1Dip2ErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_pd_dropped_cnt
                                    
                                    	CGM CgmUcPdDroppedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_rep_pd_dropped_cnt
                                    
                                    	CGM CgmMcRepPdDroppedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_db_dropped_by_rqp_cnt
                                    
                                    	CGM CgmUcDbDroppedByRqpCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_uc_db_dropped_by_pqp_cnt
                                    
                                    	CGM CgmUcDbDroppedByPqpCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_rep_db_dropped_cnt
                                    
                                    	CGM CgmMcRepDbDroppedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cgm_cgm_mc_db_dropped_cnt
                                    
                                    	CGM CgmMcDbDroppedCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_full_err_cnt
                                    
                                    	DRCA FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_single_err_cnt
                                    
                                    	DRCA SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_calib_bist_full_err_cnt
                                    
                                    	DRCA CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drca_loopback_full_err_cnt
                                    
                                    	DRCA LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_full_err_cnt
                                    
                                    	DRCB FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_single_err_cnt
                                    
                                    	DRCB SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_calib_bist_full_err_cnt
                                    
                                    	DRCB CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcb_loopback_full_err_cnt
                                    
                                    	DRCB LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_full_err_cnt
                                    
                                    	DRCC FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_single_err_cnt
                                    
                                    	DRCC SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_calib_bist_full_err_cnt
                                    
                                    	DRCC CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcc_loopback_full_err_cnt
                                    
                                    	DRCC LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_full_err_cnt
                                    
                                    	DRCD FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_single_err_cnt
                                    
                                    	DRCD SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_calib_bist_full_err_cnt
                                    
                                    	DRCD CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcd_loopback_full_err_cnt
                                    
                                    	DRCD LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_full_err_cnt
                                    
                                    	DRCE FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_single_err_cnt
                                    
                                    	DRCE SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_calib_bist_full_err_cnt
                                    
                                    	DRCE CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drce_loopback_full_err_cnt
                                    
                                    	DRCE LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_full_err_cnt
                                    
                                    	DRCF FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_single_err_cnt
                                    
                                    	DRCF SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_calib_bist_full_err_cnt
                                    
                                    	DRCF CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcf_loopback_full_err_cnt
                                    
                                    	DRCF LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_full_err_cnt
                                    
                                    	DRCG FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_single_err_cnt
                                    
                                    	DRCG SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_calib_bist_full_err_cnt
                                    
                                    	DRCG CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcg_loopback_full_err_cnt
                                    
                                    	DRCG LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_full_err_cnt
                                    
                                    	DRCH FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_single_err_cnt
                                    
                                    	DRCH SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_calib_bist_full_err_cnt
                                    
                                    	DRCH CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drch_loopback_full_err_cnt
                                    
                                    	DRCH LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_full_err_cnt
                                    
                                    	DRCBROADCAST FullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_single_err_cnt
                                    
                                    	DRCBROADCAST SingleErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_calib_bist_full_err_cnt
                                    
                                    	DRCBROADCAST CalibBistFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: drcbroadcast_loopback_full_err_cnt
                                    
                                    	DRCBROADCAST LoopbackFullErrCnt
                                    	**type**\: str
                                    
                                    	**length:** 0..6
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2017-08-29'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.OvfStatus, self).__init__()

                                        self.yang_name = "ovf-status"
                                        self.yang_parent_name = "pbc-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('cmic_cmc0_pkt_count_tx_pkt', (YLeaf(YType.str, 'cmic-cmc0-pkt-count-tx-pkt'), ['str'])),
                                            ('cmic_cmc0_pkt_count_rx_pkt', (YLeaf(YType.str, 'cmic-cmc0-pkt-count-rx-pkt'), ['str'])),
                                            ('nbi_stat_rx_bursts_err_cnt', (YLeaf(YType.str, 'nbi-stat-rx-bursts-err-cnt'), ['str'])),
                                            ('nbi_ecc_1b_err_cnt', (YLeaf(YType.str, 'nbi-ecc-1b-err-cnt'), ['str'])),
                                            ('nbi_ecc_2b_err_cnt', (YLeaf(YType.str, 'nbi-ecc-2b-err-cnt'), ['str'])),
                                            ('nbi_parity_err_cnt', (YLeaf(YType.str, 'nbi-parity-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn_crc32_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn-crc32-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_crc24_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-crc24-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_burst_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-burst-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_miss_sop_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-miss-sop-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_miss_eop_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-miss-eop-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_misaligned_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-misaligned-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_crc24_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-crc24-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_burst_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-burst-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_miss_sop_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-miss-sop-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_miss_eop_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-miss-eop-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_misaligned_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-misaligned-cnt'), ['str'])),
                                            ('nbi_tx_ilkn1_flushed_bursts_cnt', (YLeaf(YType.str, 'nbi-tx-ilkn1-flushed-bursts-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_crc24_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-crc24-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_retry_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-retry-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_wdog_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-wdog-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-wrap-after-disc-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-wrap-b4-disc-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn0_retrans_reached_timeout_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn0-retrans-reached-timeout-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_crc24_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-crc24-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_retry_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-retry-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_wdog_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-wdog-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-wrap-after-disc-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-wrap-b4-disc-err-cnt'), ['str'])),
                                            ('nbi_rx_ilkn1_retrans_reached_timeout_err_cnt', (YLeaf(YType.str, 'nbi-rx-ilkn1-retrans-reached-timeout-err-cnt'), ['str'])),
                                            ('nbi_stat_rx_frame_err_cnt', (YLeaf(YType.str, 'nbi-stat-rx-frame-err-cnt'), ['str'])),
                                            ('nbi_stat_tx_frame_err_cnt', (YLeaf(YType.str, 'nbi-stat-tx-frame-err-cnt'), ['str'])),
                                            ('nbi_rx_elk_err_bursts_cnt', (YLeaf(YType.str, 'nbi-rx-elk-err-bursts-cnt'), ['str'])),
                                            ('nbi_rx_num_thrown_eops', (YLeaf(YType.str, 'nbi-rx-num-thrown-eops'), ['str'])),
                                            ('nbi_rx_num_runts', (YLeaf(YType.str, 'nbi-rx-num-runts'), ['str'])),
                                            ('nbi_bist_tx_crc_err_bursts_cnt', (YLeaf(YType.str, 'nbi-bist-tx-crc-err-bursts-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_length_bursts_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-length-bursts-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_burst_index_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-burst-index-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_bct_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-bct-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_data_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-data-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_in_crc_err_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-in-crc-err-cnt'), ['str'])),
                                            ('nbi_bist_rx_err_sob_cnt', (YLeaf(YType.str, 'nbi-bist-rx-err-sob-cnt'), ['str'])),
                                            ('nbi_stat_tx_bursts_cnt', (YLeaf(YType.str, 'nbi-stat-tx-bursts-cnt'), ['str'])),
                                            ('nbi_stat_tx_total_leng_cnt', (YLeaf(YType.str, 'nbi-stat-tx-total-leng-cnt'), ['str'])),
                                            ('rxaui_total_tx_pkt_count', (YLeaf(YType.str, 'rxaui-total-tx-pkt-count'), ['str'])),
                                            ('rxaui_total_rx_pkt_count', (YLeaf(YType.str, 'rxaui-total-rx-pkt-count'), ['str'])),
                                            ('rxaui_rx_pkt_count_bcast_pkt', (YLeaf(YType.str, 'rxaui-rx-pkt-count-bcast-pkt'), ['str'])),
                                            ('rxaui_tx_pkt_count_bcast_pkt', (YLeaf(YType.str, 'rxaui-tx-pkt-count-bcast-pkt'), ['str'])),
                                            ('rxaui_rx_pkt_count_mcast_pkt', (YLeaf(YType.str, 'rxaui-rx-pkt-count-mcast-pkt'), ['str'])),
                                            ('rxaui_tx_pkt_count_mcast_pkt', (YLeaf(YType.str, 'rxaui-tx-pkt-count-mcast-pkt'), ['str'])),
                                            ('rxaui_rx_pkt_count_ucast_pkt', (YLeaf(YType.str, 'rxaui-rx-pkt-count-ucast-pkt'), ['str'])),
                                            ('rxaui_tx_pkt_count_ucast_pkt', (YLeaf(YType.str, 'rxaui-tx-pkt-count-ucast-pkt'), ['str'])),
                                            ('rxaui_rx_err_drop_pkt_cnt', (YLeaf(YType.str, 'rxaui-rx-err-drop-pkt-cnt'), ['str'])),
                                            ('rxaui_tx_err_drop_pkt_cnt', (YLeaf(YType.str, 'rxaui-tx-err-drop-pkt-cnt'), ['str'])),
                                            ('rxaui_byte_count_tx_pkt', (YLeaf(YType.str, 'rxaui-byte-count-tx-pkt'), ['str'])),
                                            ('rxaui_byte_count_rx_pkt', (YLeaf(YType.str, 'rxaui-byte-count-rx-pkt'), ['str'])),
                                            ('rxaui_rx_dscrd_pkt_cnt', (YLeaf(YType.str, 'rxaui-rx-dscrd-pkt-cnt'), ['str'])),
                                            ('rxaui_tx_dscrd_pkt_cnt', (YLeaf(YType.str, 'rxaui-tx-dscrd-pkt-cnt'), ['str'])),
                                            ('ire_nif_packet_counter', (YLeaf(YType.str, 'ire-nif-packet-counter'), ['str'])),
                                            ('il_total_rx_pkt_count', (YLeaf(YType.str, 'il-total-rx-pkt-count'), ['str'])),
                                            ('il_total_tx_pkt_count', (YLeaf(YType.str, 'il-total-tx-pkt-count'), ['str'])),
                                            ('il_rx_err_drop_pkt_cnt', (YLeaf(YType.str, 'il-rx-err-drop-pkt-cnt'), ['str'])),
                                            ('il_tx_err_drop_pkt_cnt', (YLeaf(YType.str, 'il-tx-err-drop-pkt-cnt'), ['str'])),
                                            ('il_byte_count_tx_pkt', (YLeaf(YType.str, 'il-byte-count-tx-pkt'), ['str'])),
                                            ('il_byte_count_rx_pkt', (YLeaf(YType.str, 'il-byte-count-rx-pkt'), ['str'])),
                                            ('il_rx_dscrd_pkt_cnt', (YLeaf(YType.str, 'il-rx-dscrd-pkt-cnt'), ['str'])),
                                            ('il_tx_dscrd_pkt_cnt', (YLeaf(YType.str, 'il-tx-dscrd-pkt-cnt'), ['str'])),
                                            ('il_rx_pkt_count_bcast_pkt', (YLeaf(YType.str, 'il-rx-pkt-count-bcast-pkt'), ['str'])),
                                            ('il_tx_pkt_count_bcast_pkt', (YLeaf(YType.str, 'il-tx-pkt-count-bcast-pkt'), ['str'])),
                                            ('il_rx_pkt_count_mcast_pkt', (YLeaf(YType.str, 'il-rx-pkt-count-mcast-pkt'), ['str'])),
                                            ('il_tx_pkt_count_mcast_pkt', (YLeaf(YType.str, 'il-tx-pkt-count-mcast-pkt'), ['str'])),
                                            ('il_rx_pkt_count_ucast_pkt', (YLeaf(YType.str, 'il-rx-pkt-count-ucast-pkt'), ['str'])),
                                            ('il_tx_pkt_count_ucast_pkt', (YLeaf(YType.str, 'il-tx-pkt-count-ucast-pkt'), ['str'])),
                                            ('iqm_enq_pkt_cnt', (YLeaf(YType.str, 'iqm-enq-pkt-cnt'), ['str'])),
                                            ('iqm_enq_byte_cnt', (YLeaf(YType.str, 'iqm-enq-byte-cnt'), ['str'])),
                                            ('iqm_deq_pkt_cnt', (YLeaf(YType.str, 'iqm-deq-pkt-cnt'), ['str'])),
                                            ('iqm_deq_byte_cnt', (YLeaf(YType.str, 'iqm-deq-byte-cnt'), ['str'])),
                                            ('iqm_tot_dscrd_pkt_cnt', (YLeaf(YType.str, 'iqm-tot-dscrd-pkt-cnt'), ['str'])),
                                            ('iqm_tot_dscrd_byte_cnt', (YLeaf(YType.str, 'iqm-tot-dscrd-byte-cnt'), ['str'])),
                                            ('iqm_ecc_1b_err_cnt', (YLeaf(YType.str, 'iqm-ecc-1b-err-cnt'), ['str'])),
                                            ('iqm_ecc_2b_err_cnt', (YLeaf(YType.str, 'iqm-ecc-2b-err-cnt'), ['str'])),
                                            ('iqm_parity_err_cnt', (YLeaf(YType.str, 'iqm-parity-err-cnt'), ['str'])),
                                            ('iqm_deq_delete_pkt_cnt', (YLeaf(YType.str, 'iqm-deq-delete-pkt-cnt'), ['str'])),
                                            ('iqm_ecn_dscrd_msk_pkt_cnt', (YLeaf(YType.str, 'iqm-ecn-dscrd-msk-pkt-cnt'), ['str'])),
                                            ('iqm_q_tot_dscrd_pkt_cnt', (YLeaf(YType.str, 'iqm-q-tot-dscrd-pkt-cnt'), ['str'])),
                                            ('iqm_q_deq_delete_pkt_cnt', (YLeaf(YType.str, 'iqm-q-deq-delete-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_db_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-db-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_bdb_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-bdb-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_bdb_protct_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-bdb-protct-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_oc_bd_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-oc-bd-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_sn_err_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-sn-err-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_mc_err_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-mc-err-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_rsrc_err_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-rsrc-err-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_qnvalid_err_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-qnvalid-err-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_cnm_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-cnm-pkt-cnt'), ['str'])),
                                            ('iqm_rjct_dyn_space_pkt_cnt', (YLeaf(YType.str, 'iqm-rjct-dyn-space-pkt-cnt'), ['str'])),
                                            ('ipt_fdt_pkt_cnt', (YLeaf(YType.str, 'ipt-fdt-pkt-cnt'), ['str'])),
                                            ('ipt_ecc_1b_err_cnt', (YLeaf(YType.str, 'ipt-ecc-1b-err-cnt'), ['str'])),
                                            ('ipt_ecc_2b_err_cnt', (YLeaf(YType.str, 'ipt-ecc-2b-err-cnt'), ['str'])),
                                            ('ipt_parity_err_cnt', (YLeaf(YType.str, 'ipt-parity-err-cnt'), ['str'])),
                                            ('ipt_crc_err_cnt', (YLeaf(YType.str, 'ipt-crc-err-cnt'), ['str'])),
                                            ('ipt_crc_err_del_buff_cnt', (YLeaf(YType.str, 'ipt-crc-err-del-buff-cnt'), ['str'])),
                                            ('ipt_cpu_del_buff_cnt', (YLeaf(YType.str, 'ipt-cpu-del-buff-cnt'), ['str'])),
                                            ('ipt_cpu_rel_buff_cnt', (YLeaf(YType.str, 'ipt-cpu-rel-buff-cnt'), ['str'])),
                                            ('ipt_crc_err_buff_fifo_full_cnt', (YLeaf(YType.str, 'ipt-crc-err-buff-fifo-full-cnt'), ['str'])),
                                            ('fdt_data_cell_cnt', (YLeaf(YType.str, 'fdt-data-cell-cnt'), ['str'])),
                                            ('fdt_data_byte_cnt', (YLeaf(YType.str, 'fdt-data-byte-cnt'), ['str'])),
                                            ('fdt_crc_dropped_pck_cnt', (YLeaf(YType.str, 'fdt-crc-dropped-pck-cnt'), ['str'])),
                                            ('fdt_invalid_destq_drop_cell_cnt', (YLeaf(YType.str, 'fdt-invalid-destq-drop-cell-cnt'), ['str'])),
                                            ('fdt_indirect_command_count', (YLeaf(YType.str, 'fdt-indirect-command-count'), ['str'])),
                                            ('fdt_ecc_1b_err_cnt', (YLeaf(YType.str, 'fdt-ecc-1b-err-cnt'), ['str'])),
                                            ('fdt_ecc_2b_err_cnt', (YLeaf(YType.str, 'fdt-ecc-2b-err-cnt'), ['str'])),
                                            ('fdt_parity_err_cnt', (YLeaf(YType.str, 'fdt-parity-err-cnt'), ['str'])),
                                            ('fdt_crc_dropped_cell_cnt', (YLeaf(YType.str, 'fdt-crc-dropped-cell-cnt'), ['str'])),
                                            ('fcr_control_cell_cnt', (YLeaf(YType.str, 'fcr-control-cell-cnt'), ['str'])),
                                            ('fcr_cell_drop_cnt', (YLeaf(YType.str, 'fcr-cell-drop-cnt'), ['str'])),
                                            ('fcr_credit_cell_drop_cnt', (YLeaf(YType.str, 'fcr-credit-cell-drop-cnt'), ['str'])),
                                            ('fcr_fs_cell_drop_cnt', (YLeaf(YType.str, 'fcr-fs-cell-drop-cnt'), ['str'])),
                                            ('fcr_rt_cell_drop_cnt', (YLeaf(YType.str, 'fcr-rt-cell-drop-cnt'), ['str'])),
                                            ('fcr_ecc_1b_err_cnt', (YLeaf(YType.str, 'fcr-ecc-1b-err-cnt'), ['str'])),
                                            ('fcr_ecc_2b_err_cnt', (YLeaf(YType.str, 'fcr-ecc-2b-err-cnt'), ['str'])),
                                            ('fdr_data_cell_cnt', (YLeaf(YType.str, 'fdr-data-cell-cnt'), ['str'])),
                                            ('fdr_data_byte_cnt', (YLeaf(YType.str, 'fdr-data-byte-cnt'), ['str'])),
                                            ('fdr_crc_dropped_pck_cnt', (YLeaf(YType.str, 'fdr-crc-dropped-pck-cnt'), ['str'])),
                                            ('fdr_p_pkt_cnt', (YLeaf(YType.str, 'fdr-p-pkt-cnt'), ['str'])),
                                            ('fdr_prm_error_filter_cnt', (YLeaf(YType.str, 'fdr-prm-error-filter-cnt'), ['str'])),
                                            ('fdr_sec_error_filter_cnt', (YLeaf(YType.str, 'fdr-sec-error-filter-cnt'), ['str'])),
                                            ('fdr_prm_ecc_1b_err_cnt', (YLeaf(YType.str, 'fdr-prm-ecc-1b-err-cnt'), ['str'])),
                                            ('fdr_prm_ecc_2b_err_cnt', (YLeaf(YType.str, 'fdr-prm-ecc-2b-err-cnt'), ['str'])),
                                            ('fdr_sec_ecc_1b_err_cnt', (YLeaf(YType.str, 'fdr-sec-ecc-1b-err-cnt'), ['str'])),
                                            ('fdr_sec_ecc_2b_err_cnt', (YLeaf(YType.str, 'fdr-sec-ecc-2b-err-cnt'), ['str'])),
                                            ('egq_ecc_1b_err_cnt', (YLeaf(YType.str, 'egq-ecc-1b-err-cnt'), ['str'])),
                                            ('egq_ecc_2b_err_cnt', (YLeaf(YType.str, 'egq-ecc-2b-err-cnt'), ['str'])),
                                            ('egq_parity_err_cnt', (YLeaf(YType.str, 'egq-parity-err-cnt'), ['str'])),
                                            ('egq_dbf_ecc_1b_err_cnt', (YLeaf(YType.str, 'egq-dbf-ecc-1b-err-cnt'), ['str'])),
                                            ('egq_dbf_ecc_2b_err_cnt', (YLeaf(YType.str, 'egq-dbf-ecc-2b-err-cnt'), ['str'])),
                                            ('egq_empty_mcid_counter', (YLeaf(YType.str, 'egq-empty-mcid-counter'), ['str'])),
                                            ('egq_rqp_discard_packet_counter', (YLeaf(YType.str, 'egq-rqp-discard-packet-counter'), ['str'])),
                                            ('egq_ehp_discard_packet_counter', (YLeaf(YType.str, 'egq-ehp-discard-packet-counter'), ['str'])),
                                            ('egq_ipt_pkt_cnt', (YLeaf(YType.str, 'egq-ipt-pkt-cnt'), ['str'])),
                                            ('epni_epe_pkt_cnt', (YLeaf(YType.str, 'epni-epe-pkt-cnt'), ['str'])),
                                            ('epni_epe_byte_cnt', (YLeaf(YType.str, 'epni-epe-byte-cnt'), ['str'])),
                                            ('epni_epe_discard_pkt_cnt', (YLeaf(YType.str, 'epni-epe-discard-pkt-cnt'), ['str'])),
                                            ('epni_ecc_1b_err_cnt', (YLeaf(YType.str, 'epni-ecc-1b-err-cnt'), ['str'])),
                                            ('epni_ecc_2b_err_cnt', (YLeaf(YType.str, 'epni-ecc-2b-err-cnt'), ['str'])),
                                            ('epni_parity_err_cnt', (YLeaf(YType.str, 'epni-parity-err-cnt'), ['str'])),
                                            ('egq_pqp_ucast_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-ucast-pkt-cnt'), ['str'])),
                                            ('egq_pqp_ucast_h_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-ucast-h-pkt-cnt'), ['str'])),
                                            ('egq_pqp_ucast_l_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-ucast-l-pkt-cnt'), ['str'])),
                                            ('egq_pqp_ucast_bytes_cnt', (YLeaf(YType.str, 'egq-pqp-ucast-bytes-cnt'), ['str'])),
                                            ('egq_pqp_ucast_discard_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-ucast-discard-pkt-cnt'), ['str'])),
                                            ('egq_pqp_mcast_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-mcast-pkt-cnt'), ['str'])),
                                            ('egq_pqp_mcast_h_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-mcast-h-pkt-cnt'), ['str'])),
                                            ('egq_pqp_mcast_l_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-mcast-l-pkt-cnt'), ['str'])),
                                            ('egq_pqp_mcast_bytes_cnt', (YLeaf(YType.str, 'egq-pqp-mcast-bytes-cnt'), ['str'])),
                                            ('egq_pqp_mcast_discard_pkt_cnt', (YLeaf(YType.str, 'egq-pqp-mcast-discard-pkt-cnt'), ['str'])),
                                            ('fct_control_cell_cnt', (YLeaf(YType.str, 'fct-control-cell-cnt'), ['str'])),
                                            ('fct_unrch_crdt_cnt', (YLeaf(YType.str, 'fct-unrch-crdt-cnt'), ['str'])),
                                            ('idr_reassembly_errors', (YLeaf(YType.str, 'idr-reassembly-errors'), ['str'])),
                                            ('idr_mmu_ecc_1b_err_cnt', (YLeaf(YType.str, 'idr-mmu-ecc-1b-err-cnt'), ['str'])),
                                            ('idr_mmu_ecc_2b_err_cnt', (YLeaf(YType.str, 'idr-mmu-ecc-2b-err-cnt'), ['str'])),
                                            ('idr_discarded_packets0_cnt', (YLeaf(YType.str, 'idr-discarded-packets0-cnt'), ['str'])),
                                            ('idr_discarded_packets1_cnt', (YLeaf(YType.str, 'idr-discarded-packets1-cnt'), ['str'])),
                                            ('idr_discarded_packets2_cnt', (YLeaf(YType.str, 'idr-discarded-packets2-cnt'), ['str'])),
                                            ('idr_discarded_packets3_cnt', (YLeaf(YType.str, 'idr-discarded-packets3-cnt'), ['str'])),
                                            ('idr_discarded_octets0_cnt', (YLeaf(YType.str, 'idr-discarded-octets0-cnt'), ['str'])),
                                            ('idr_discarded_octets1_cnt', (YLeaf(YType.str, 'idr-discarded-octets1-cnt'), ['str'])),
                                            ('idr_discarded_octets2_cnt', (YLeaf(YType.str, 'idr-discarded-octets2-cnt'), ['str'])),
                                            ('idr_discarded_octets3_cnt', (YLeaf(YType.str, 'idr-discarded-octets3-cnt'), ['str'])),
                                            ('mmu_ecc_1b_err_cnt', (YLeaf(YType.str, 'mmu-ecc-1b-err-cnt'), ['str'])),
                                            ('mmu_ecc_2b_err_cnt', (YLeaf(YType.str, 'mmu-ecc-2b-err-cnt'), ['str'])),
                                            ('oamp_parity_err_cnt', (YLeaf(YType.str, 'oamp-parity-err-cnt'), ['str'])),
                                            ('oamp_ecc_1b_err_cnt', (YLeaf(YType.str, 'oamp-ecc-1b-err-cnt'), ['str'])),
                                            ('oamp_ecc_2b_err_cnt', (YLeaf(YType.str, 'oamp-ecc-2b-err-cnt'), ['str'])),
                                            ('crps_parity_err_cnt', (YLeaf(YType.str, 'crps-parity-err-cnt'), ['str'])),
                                            ('fmac0_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac0-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac1_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac1-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac2_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac2-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac3_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac3-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac4_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac4-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac5_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac5-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac6_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac6-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac7_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac7-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac8_kpcs0_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac8-kpcs0-tst-rx-err-cnt'), ['str'])),
                                            ('fmac0_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac0-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac1_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac1-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac2_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac2-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac3_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac3-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac4_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac4-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac5_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac5-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac6_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac6-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac7_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac7-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac8_kpcs1_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac8-kpcs1-tst-rx-err-cnt'), ['str'])),
                                            ('fmac0_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac0-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac1_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac1-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac2_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac2-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac3_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac3-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac4_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac4-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac5_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac5-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac6_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac6-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac7_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac7-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac8_kpcs2_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac8-kpcs2-tst-rx-err-cnt'), ['str'])),
                                            ('fmac0_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac0-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac1_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac1-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac2_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac2-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac3_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac3-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac4_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac4-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac5_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac5-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac6_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac6-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac7_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac7-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac8_kpcs3_tst_rx_err_cnt', (YLeaf(YType.str, 'fmac8-kpcs3-tst-rx-err-cnt'), ['str'])),
                                            ('fmac0_tst0_err_cnt', (YLeaf(YType.str, 'fmac0-tst0-err-cnt'), ['str'])),
                                            ('fmac1_tst0_err_cnt', (YLeaf(YType.str, 'fmac1-tst0-err-cnt'), ['str'])),
                                            ('fmac2_tst0_err_cnt', (YLeaf(YType.str, 'fmac2-tst0-err-cnt'), ['str'])),
                                            ('fmac3_tst0_err_cnt', (YLeaf(YType.str, 'fmac3-tst0-err-cnt'), ['str'])),
                                            ('fmac4_tst0_err_cnt', (YLeaf(YType.str, 'fmac4-tst0-err-cnt'), ['str'])),
                                            ('fmac5_tst0_err_cnt', (YLeaf(YType.str, 'fmac5-tst0-err-cnt'), ['str'])),
                                            ('fmac6_tst0_err_cnt', (YLeaf(YType.str, 'fmac6-tst0-err-cnt'), ['str'])),
                                            ('fmac7_tst0_err_cnt', (YLeaf(YType.str, 'fmac7-tst0-err-cnt'), ['str'])),
                                            ('fmac8_tst0_err_cnt', (YLeaf(YType.str, 'fmac8-tst0-err-cnt'), ['str'])),
                                            ('fmac0_tst1_err_cnt', (YLeaf(YType.str, 'fmac0-tst1-err-cnt'), ['str'])),
                                            ('fmac1_tst1_err_cnt', (YLeaf(YType.str, 'fmac1-tst1-err-cnt'), ['str'])),
                                            ('fmac2_tst1_err_cnt', (YLeaf(YType.str, 'fmac2-tst1-err-cnt'), ['str'])),
                                            ('fmac3_tst1_err_cnt', (YLeaf(YType.str, 'fmac3-tst1-err-cnt'), ['str'])),
                                            ('fmac4_tst1_err_cnt', (YLeaf(YType.str, 'fmac4-tst1-err-cnt'), ['str'])),
                                            ('fmac5_tst1_err_cnt', (YLeaf(YType.str, 'fmac5-tst1-err-cnt'), ['str'])),
                                            ('fmac6_tst1_err_cnt', (YLeaf(YType.str, 'fmac6-tst1-err-cnt'), ['str'])),
                                            ('fmac7_tst1_err_cnt', (YLeaf(YType.str, 'fmac7-tst1-err-cnt'), ['str'])),
                                            ('fmac8_tst1_err_cnt', (YLeaf(YType.str, 'fmac8-tst1-err-cnt'), ['str'])),
                                            ('fmac0_tst2_err_cnt', (YLeaf(YType.str, 'fmac0-tst2-err-cnt'), ['str'])),
                                            ('fmac1_tst2_err_cnt', (YLeaf(YType.str, 'fmac1-tst2-err-cnt'), ['str'])),
                                            ('fmac2_tst2_err_cnt', (YLeaf(YType.str, 'fmac2-tst2-err-cnt'), ['str'])),
                                            ('fmac3_tst2_err_cnt', (YLeaf(YType.str, 'fmac3-tst2-err-cnt'), ['str'])),
                                            ('fmac4_tst2_err_cnt', (YLeaf(YType.str, 'fmac4-tst2-err-cnt'), ['str'])),
                                            ('fmac5_tst2_err_cnt', (YLeaf(YType.str, 'fmac5-tst2-err-cnt'), ['str'])),
                                            ('fmac6_tst2_err_cnt', (YLeaf(YType.str, 'fmac6-tst2-err-cnt'), ['str'])),
                                            ('fmac7_tst2_err_cnt', (YLeaf(YType.str, 'fmac7-tst2-err-cnt'), ['str'])),
                                            ('fmac8_tst2_err_cnt', (YLeaf(YType.str, 'fmac8-tst2-err-cnt'), ['str'])),
                                            ('fmac0_tst3_err_cnt', (YLeaf(YType.str, 'fmac0-tst3-err-cnt'), ['str'])),
                                            ('fmac1_tst3_err_cnt', (YLeaf(YType.str, 'fmac1-tst3-err-cnt'), ['str'])),
                                            ('fmac2_tst3_err_cnt', (YLeaf(YType.str, 'fmac2-tst3-err-cnt'), ['str'])),
                                            ('fmac3_tst3_err_cnt', (YLeaf(YType.str, 'fmac3-tst3-err-cnt'), ['str'])),
                                            ('fmac4_tst3_err_cnt', (YLeaf(YType.str, 'fmac4-tst3-err-cnt'), ['str'])),
                                            ('fmac5_tst3_err_cnt', (YLeaf(YType.str, 'fmac5-tst3-err-cnt'), ['str'])),
                                            ('fmac6_tst3_err_cnt', (YLeaf(YType.str, 'fmac6-tst3-err-cnt'), ['str'])),
                                            ('fmac7_tst3_err_cnt', (YLeaf(YType.str, 'fmac7-tst3-err-cnt'), ['str'])),
                                            ('fmac8_tst3_err_cnt', (YLeaf(YType.str, 'fmac8-tst3-err-cnt'), ['str'])),
                                            ('fmac0_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac0-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac1_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac1-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac2_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac2-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac3_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac3-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac4_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac4-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac5_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac5-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac6_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac6-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac7_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac7-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac8_ecc_1b_err_cnt', (YLeaf(YType.str, 'fmac8-ecc-1b-err-cnt'), ['str'])),
                                            ('fmac0_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac0-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac1_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac1-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac2_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac2-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac3_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac3-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac4_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac4-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac5_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac5-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac6_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac6-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac7_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac7-ecc-2b-err-cnt'), ['str'])),
                                            ('fmac8_ecc_2b_err_cnt', (YLeaf(YType.str, 'fmac8-ecc-2b-err-cnt'), ['str'])),
                                            ('olp_incoming_bad_identifier_counter', (YLeaf(YType.str, 'olp-incoming-bad-identifier-counter'), ['str'])),
                                            ('olp_incoming_bad_reassembly_counter', (YLeaf(YType.str, 'olp-incoming-bad-reassembly-counter'), ['str'])),
                                            ('cfc_parity_err_cnt', (YLeaf(YType.str, 'cfc-parity-err-cnt'), ['str'])),
                                            ('cfc_ilkn0_oob_rx_crc_err_cntr', (YLeaf(YType.str, 'cfc-ilkn0-oob-rx-crc-err-cntr'), ['str'])),
                                            ('cfc_ilkn1_oob_rx_crc_err_cntr', (YLeaf(YType.str, 'cfc-ilkn1-oob-rx-crc-err-cntr'), ['str'])),
                                            ('cfc_spi_oob_rx0_frm_err_cnt', (YLeaf(YType.str, 'cfc-spi-oob-rx0-frm-err-cnt'), ['str'])),
                                            ('cfc_spi_oob_rx0_dip2_err_cnt', (YLeaf(YType.str, 'cfc-spi-oob-rx0-dip2-err-cnt'), ['str'])),
                                            ('cfc_spi_oob_rx1_frm_err_cnt', (YLeaf(YType.str, 'cfc-spi-oob-rx1-frm-err-cnt'), ['str'])),
                                            ('cfc_spi_oob_rx1_dip2_err_cnt', (YLeaf(YType.str, 'cfc-spi-oob-rx1-dip2-err-cnt'), ['str'])),
                                            ('cgm_cgm_uc_pd_dropped_cnt', (YLeaf(YType.str, 'cgm-cgm-uc-pd-dropped-cnt'), ['str'])),
                                            ('cgm_cgm_mc_rep_pd_dropped_cnt', (YLeaf(YType.str, 'cgm-cgm-mc-rep-pd-dropped-cnt'), ['str'])),
                                            ('cgm_cgm_uc_db_dropped_by_rqp_cnt', (YLeaf(YType.str, 'cgm-cgm-uc-db-dropped-by-rqp-cnt'), ['str'])),
                                            ('cgm_cgm_uc_db_dropped_by_pqp_cnt', (YLeaf(YType.str, 'cgm-cgm-uc-db-dropped-by-pqp-cnt'), ['str'])),
                                            ('cgm_cgm_mc_rep_db_dropped_cnt', (YLeaf(YType.str, 'cgm-cgm-mc-rep-db-dropped-cnt'), ['str'])),
                                            ('cgm_cgm_mc_db_dropped_cnt', (YLeaf(YType.str, 'cgm-cgm-mc-db-dropped-cnt'), ['str'])),
                                            ('drca_full_err_cnt', (YLeaf(YType.str, 'drca-full-err-cnt'), ['str'])),
                                            ('drca_single_err_cnt', (YLeaf(YType.str, 'drca-single-err-cnt'), ['str'])),
                                            ('drca_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drca-calib-bist-full-err-cnt'), ['str'])),
                                            ('drca_loopback_full_err_cnt', (YLeaf(YType.str, 'drca-loopback-full-err-cnt'), ['str'])),
                                            ('drcb_full_err_cnt', (YLeaf(YType.str, 'drcb-full-err-cnt'), ['str'])),
                                            ('drcb_single_err_cnt', (YLeaf(YType.str, 'drcb-single-err-cnt'), ['str'])),
                                            ('drcb_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcb-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcb_loopback_full_err_cnt', (YLeaf(YType.str, 'drcb-loopback-full-err-cnt'), ['str'])),
                                            ('drcc_full_err_cnt', (YLeaf(YType.str, 'drcc-full-err-cnt'), ['str'])),
                                            ('drcc_single_err_cnt', (YLeaf(YType.str, 'drcc-single-err-cnt'), ['str'])),
                                            ('drcc_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcc-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcc_loopback_full_err_cnt', (YLeaf(YType.str, 'drcc-loopback-full-err-cnt'), ['str'])),
                                            ('drcd_full_err_cnt', (YLeaf(YType.str, 'drcd-full-err-cnt'), ['str'])),
                                            ('drcd_single_err_cnt', (YLeaf(YType.str, 'drcd-single-err-cnt'), ['str'])),
                                            ('drcd_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcd-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcd_loopback_full_err_cnt', (YLeaf(YType.str, 'drcd-loopback-full-err-cnt'), ['str'])),
                                            ('drce_full_err_cnt', (YLeaf(YType.str, 'drce-full-err-cnt'), ['str'])),
                                            ('drce_single_err_cnt', (YLeaf(YType.str, 'drce-single-err-cnt'), ['str'])),
                                            ('drce_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drce-calib-bist-full-err-cnt'), ['str'])),
                                            ('drce_loopback_full_err_cnt', (YLeaf(YType.str, 'drce-loopback-full-err-cnt'), ['str'])),
                                            ('drcf_full_err_cnt', (YLeaf(YType.str, 'drcf-full-err-cnt'), ['str'])),
                                            ('drcf_single_err_cnt', (YLeaf(YType.str, 'drcf-single-err-cnt'), ['str'])),
                                            ('drcf_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcf-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcf_loopback_full_err_cnt', (YLeaf(YType.str, 'drcf-loopback-full-err-cnt'), ['str'])),
                                            ('drcg_full_err_cnt', (YLeaf(YType.str, 'drcg-full-err-cnt'), ['str'])),
                                            ('drcg_single_err_cnt', (YLeaf(YType.str, 'drcg-single-err-cnt'), ['str'])),
                                            ('drcg_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcg-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcg_loopback_full_err_cnt', (YLeaf(YType.str, 'drcg-loopback-full-err-cnt'), ['str'])),
                                            ('drch_full_err_cnt', (YLeaf(YType.str, 'drch-full-err-cnt'), ['str'])),
                                            ('drch_single_err_cnt', (YLeaf(YType.str, 'drch-single-err-cnt'), ['str'])),
                                            ('drch_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drch-calib-bist-full-err-cnt'), ['str'])),
                                            ('drch_loopback_full_err_cnt', (YLeaf(YType.str, 'drch-loopback-full-err-cnt'), ['str'])),
                                            ('drcbroadcast_full_err_cnt', (YLeaf(YType.str, 'drcbroadcast-full-err-cnt'), ['str'])),
                                            ('drcbroadcast_single_err_cnt', (YLeaf(YType.str, 'drcbroadcast-single-err-cnt'), ['str'])),
                                            ('drcbroadcast_calib_bist_full_err_cnt', (YLeaf(YType.str, 'drcbroadcast-calib-bist-full-err-cnt'), ['str'])),
                                            ('drcbroadcast_loopback_full_err_cnt', (YLeaf(YType.str, 'drcbroadcast-loopback-full-err-cnt'), ['str'])),
                                        ])
                                        self.cmic_cmc0_pkt_count_tx_pkt = None
                                        self.cmic_cmc0_pkt_count_rx_pkt = None
                                        self.nbi_stat_rx_bursts_err_cnt = None
                                        self.nbi_ecc_1b_err_cnt = None
                                        self.nbi_ecc_2b_err_cnt = None
                                        self.nbi_parity_err_cnt = None
                                        self.nbi_rx_ilkn_crc32_err_cnt = None
                                        self.nbi_rx_ilkn0_crc24_err_cnt = None
                                        self.nbi_rx_ilkn0_burst_err_cnt = None
                                        self.nbi_rx_ilkn0_miss_sop_err_cnt = None
                                        self.nbi_rx_ilkn0_miss_eop_err_cnt = None
                                        self.nbi_rx_ilkn0_misaligned_cnt = None
                                        self.nbi_rx_ilkn1_crc24_err_cnt = None
                                        self.nbi_rx_ilkn1_burst_err_cnt = None
                                        self.nbi_rx_ilkn1_miss_sop_err_cnt = None
                                        self.nbi_rx_ilkn1_miss_eop_err_cnt = None
                                        self.nbi_rx_ilkn1_misaligned_cnt = None
                                        self.nbi_tx_ilkn1_flushed_bursts_cnt = None
                                        self.nbi_rx_ilkn0_retrans_crc24_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_retry_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wdog_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt = None
                                        self.nbi_rx_ilkn0_retrans_reached_timeout_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_crc24_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_retry_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wdog_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt = None
                                        self.nbi_rx_ilkn1_retrans_reached_timeout_err_cnt = None
                                        self.nbi_stat_rx_frame_err_cnt = None
                                        self.nbi_stat_tx_frame_err_cnt = None
                                        self.nbi_rx_elk_err_bursts_cnt = None
                                        self.nbi_rx_num_thrown_eops = None
                                        self.nbi_rx_num_runts = None
                                        self.nbi_bist_tx_crc_err_bursts_cnt = None
                                        self.nbi_bist_rx_err_length_bursts_cnt = None
                                        self.nbi_bist_rx_err_burst_index_cnt = None
                                        self.nbi_bist_rx_err_bct_cnt = None
                                        self.nbi_bist_rx_err_data_cnt = None
                                        self.nbi_bist_rx_err_in_crc_err_cnt = None
                                        self.nbi_bist_rx_err_sob_cnt = None
                                        self.nbi_stat_tx_bursts_cnt = None
                                        self.nbi_stat_tx_total_leng_cnt = None
                                        self.rxaui_total_tx_pkt_count = None
                                        self.rxaui_total_rx_pkt_count = None
                                        self.rxaui_rx_pkt_count_bcast_pkt = None
                                        self.rxaui_tx_pkt_count_bcast_pkt = None
                                        self.rxaui_rx_pkt_count_mcast_pkt = None
                                        self.rxaui_tx_pkt_count_mcast_pkt = None
                                        self.rxaui_rx_pkt_count_ucast_pkt = None
                                        self.rxaui_tx_pkt_count_ucast_pkt = None
                                        self.rxaui_rx_err_drop_pkt_cnt = None
                                        self.rxaui_tx_err_drop_pkt_cnt = None
                                        self.rxaui_byte_count_tx_pkt = None
                                        self.rxaui_byte_count_rx_pkt = None
                                        self.rxaui_rx_dscrd_pkt_cnt = None
                                        self.rxaui_tx_dscrd_pkt_cnt = None
                                        self.ire_nif_packet_counter = None
                                        self.il_total_rx_pkt_count = None
                                        self.il_total_tx_pkt_count = None
                                        self.il_rx_err_drop_pkt_cnt = None
                                        self.il_tx_err_drop_pkt_cnt = None
                                        self.il_byte_count_tx_pkt = None
                                        self.il_byte_count_rx_pkt = None
                                        self.il_rx_dscrd_pkt_cnt = None
                                        self.il_tx_dscrd_pkt_cnt = None
                                        self.il_rx_pkt_count_bcast_pkt = None
                                        self.il_tx_pkt_count_bcast_pkt = None
                                        self.il_rx_pkt_count_mcast_pkt = None
                                        self.il_tx_pkt_count_mcast_pkt = None
                                        self.il_rx_pkt_count_ucast_pkt = None
                                        self.il_tx_pkt_count_ucast_pkt = None
                                        self.iqm_enq_pkt_cnt = None
                                        self.iqm_enq_byte_cnt = None
                                        self.iqm_deq_pkt_cnt = None
                                        self.iqm_deq_byte_cnt = None
                                        self.iqm_tot_dscrd_pkt_cnt = None
                                        self.iqm_tot_dscrd_byte_cnt = None
                                        self.iqm_ecc_1b_err_cnt = None
                                        self.iqm_ecc_2b_err_cnt = None
                                        self.iqm_parity_err_cnt = None
                                        self.iqm_deq_delete_pkt_cnt = None
                                        self.iqm_ecn_dscrd_msk_pkt_cnt = None
                                        self.iqm_q_tot_dscrd_pkt_cnt = None
                                        self.iqm_q_deq_delete_pkt_cnt = None
                                        self.iqm_rjct_db_pkt_cnt = None
                                        self.iqm_rjct_bdb_pkt_cnt = None
                                        self.iqm_rjct_bdb_protct_pkt_cnt = None
                                        self.iqm_rjct_oc_bd_pkt_cnt = None
                                        self.iqm_rjct_sn_err_pkt_cnt = None
                                        self.iqm_rjct_mc_err_pkt_cnt = None
                                        self.iqm_rjct_rsrc_err_pkt_cnt = None
                                        self.iqm_rjct_qnvalid_err_pkt_cnt = None
                                        self.iqm_rjct_cnm_pkt_cnt = None
                                        self.iqm_rjct_dyn_space_pkt_cnt = None
                                        self.ipt_fdt_pkt_cnt = None
                                        self.ipt_ecc_1b_err_cnt = None
                                        self.ipt_ecc_2b_err_cnt = None
                                        self.ipt_parity_err_cnt = None
                                        self.ipt_crc_err_cnt = None
                                        self.ipt_crc_err_del_buff_cnt = None
                                        self.ipt_cpu_del_buff_cnt = None
                                        self.ipt_cpu_rel_buff_cnt = None
                                        self.ipt_crc_err_buff_fifo_full_cnt = None
                                        self.fdt_data_cell_cnt = None
                                        self.fdt_data_byte_cnt = None
                                        self.fdt_crc_dropped_pck_cnt = None
                                        self.fdt_invalid_destq_drop_cell_cnt = None
                                        self.fdt_indirect_command_count = None
                                        self.fdt_ecc_1b_err_cnt = None
                                        self.fdt_ecc_2b_err_cnt = None
                                        self.fdt_parity_err_cnt = None
                                        self.fdt_crc_dropped_cell_cnt = None
                                        self.fcr_control_cell_cnt = None
                                        self.fcr_cell_drop_cnt = None
                                        self.fcr_credit_cell_drop_cnt = None
                                        self.fcr_fs_cell_drop_cnt = None
                                        self.fcr_rt_cell_drop_cnt = None
                                        self.fcr_ecc_1b_err_cnt = None
                                        self.fcr_ecc_2b_err_cnt = None
                                        self.fdr_data_cell_cnt = None
                                        self.fdr_data_byte_cnt = None
                                        self.fdr_crc_dropped_pck_cnt = None
                                        self.fdr_p_pkt_cnt = None
                                        self.fdr_prm_error_filter_cnt = None
                                        self.fdr_sec_error_filter_cnt = None
                                        self.fdr_prm_ecc_1b_err_cnt = None
                                        self.fdr_prm_ecc_2b_err_cnt = None
                                        self.fdr_sec_ecc_1b_err_cnt = None
                                        self.fdr_sec_ecc_2b_err_cnt = None
                                        self.egq_ecc_1b_err_cnt = None
                                        self.egq_ecc_2b_err_cnt = None
                                        self.egq_parity_err_cnt = None
                                        self.egq_dbf_ecc_1b_err_cnt = None
                                        self.egq_dbf_ecc_2b_err_cnt = None
                                        self.egq_empty_mcid_counter = None
                                        self.egq_rqp_discard_packet_counter = None
                                        self.egq_ehp_discard_packet_counter = None
                                        self.egq_ipt_pkt_cnt = None
                                        self.epni_epe_pkt_cnt = None
                                        self.epni_epe_byte_cnt = None
                                        self.epni_epe_discard_pkt_cnt = None
                                        self.epni_ecc_1b_err_cnt = None
                                        self.epni_ecc_2b_err_cnt = None
                                        self.epni_parity_err_cnt = None
                                        self.egq_pqp_ucast_pkt_cnt = None
                                        self.egq_pqp_ucast_h_pkt_cnt = None
                                        self.egq_pqp_ucast_l_pkt_cnt = None
                                        self.egq_pqp_ucast_bytes_cnt = None
                                        self.egq_pqp_ucast_discard_pkt_cnt = None
                                        self.egq_pqp_mcast_pkt_cnt = None
                                        self.egq_pqp_mcast_h_pkt_cnt = None
                                        self.egq_pqp_mcast_l_pkt_cnt = None
                                        self.egq_pqp_mcast_bytes_cnt = None
                                        self.egq_pqp_mcast_discard_pkt_cnt = None
                                        self.fct_control_cell_cnt = None
                                        self.fct_unrch_crdt_cnt = None
                                        self.idr_reassembly_errors = None
                                        self.idr_mmu_ecc_1b_err_cnt = None
                                        self.idr_mmu_ecc_2b_err_cnt = None
                                        self.idr_discarded_packets0_cnt = None
                                        self.idr_discarded_packets1_cnt = None
                                        self.idr_discarded_packets2_cnt = None
                                        self.idr_discarded_packets3_cnt = None
                                        self.idr_discarded_octets0_cnt = None
                                        self.idr_discarded_octets1_cnt = None
                                        self.idr_discarded_octets2_cnt = None
                                        self.idr_discarded_octets3_cnt = None
                                        self.mmu_ecc_1b_err_cnt = None
                                        self.mmu_ecc_2b_err_cnt = None
                                        self.oamp_parity_err_cnt = None
                                        self.oamp_ecc_1b_err_cnt = None
                                        self.oamp_ecc_2b_err_cnt = None
                                        self.crps_parity_err_cnt = None
                                        self.fmac0_kpcs0_tst_rx_err_cnt = None
                                        self.fmac1_kpcs0_tst_rx_err_cnt = None
                                        self.fmac2_kpcs0_tst_rx_err_cnt = None
                                        self.fmac3_kpcs0_tst_rx_err_cnt = None
                                        self.fmac4_kpcs0_tst_rx_err_cnt = None
                                        self.fmac5_kpcs0_tst_rx_err_cnt = None
                                        self.fmac6_kpcs0_tst_rx_err_cnt = None
                                        self.fmac7_kpcs0_tst_rx_err_cnt = None
                                        self.fmac8_kpcs0_tst_rx_err_cnt = None
                                        self.fmac0_kpcs1_tst_rx_err_cnt = None
                                        self.fmac1_kpcs1_tst_rx_err_cnt = None
                                        self.fmac2_kpcs1_tst_rx_err_cnt = None
                                        self.fmac3_kpcs1_tst_rx_err_cnt = None
                                        self.fmac4_kpcs1_tst_rx_err_cnt = None
                                        self.fmac5_kpcs1_tst_rx_err_cnt = None
                                        self.fmac6_kpcs1_tst_rx_err_cnt = None
                                        self.fmac7_kpcs1_tst_rx_err_cnt = None
                                        self.fmac8_kpcs1_tst_rx_err_cnt = None
                                        self.fmac0_kpcs2_tst_rx_err_cnt = None
                                        self.fmac1_kpcs2_tst_rx_err_cnt = None
                                        self.fmac2_kpcs2_tst_rx_err_cnt = None
                                        self.fmac3_kpcs2_tst_rx_err_cnt = None
                                        self.fmac4_kpcs2_tst_rx_err_cnt = None
                                        self.fmac5_kpcs2_tst_rx_err_cnt = None
                                        self.fmac6_kpcs2_tst_rx_err_cnt = None
                                        self.fmac7_kpcs2_tst_rx_err_cnt = None
                                        self.fmac8_kpcs2_tst_rx_err_cnt = None
                                        self.fmac0_kpcs3_tst_rx_err_cnt = None
                                        self.fmac1_kpcs3_tst_rx_err_cnt = None
                                        self.fmac2_kpcs3_tst_rx_err_cnt = None
                                        self.fmac3_kpcs3_tst_rx_err_cnt = None
                                        self.fmac4_kpcs3_tst_rx_err_cnt = None
                                        self.fmac5_kpcs3_tst_rx_err_cnt = None
                                        self.fmac6_kpcs3_tst_rx_err_cnt = None
                                        self.fmac7_kpcs3_tst_rx_err_cnt = None
                                        self.fmac8_kpcs3_tst_rx_err_cnt = None
                                        self.fmac0_tst0_err_cnt = None
                                        self.fmac1_tst0_err_cnt = None
                                        self.fmac2_tst0_err_cnt = None
                                        self.fmac3_tst0_err_cnt = None
                                        self.fmac4_tst0_err_cnt = None
                                        self.fmac5_tst0_err_cnt = None
                                        self.fmac6_tst0_err_cnt = None
                                        self.fmac7_tst0_err_cnt = None
                                        self.fmac8_tst0_err_cnt = None
                                        self.fmac0_tst1_err_cnt = None
                                        self.fmac1_tst1_err_cnt = None
                                        self.fmac2_tst1_err_cnt = None
                                        self.fmac3_tst1_err_cnt = None
                                        self.fmac4_tst1_err_cnt = None
                                        self.fmac5_tst1_err_cnt = None
                                        self.fmac6_tst1_err_cnt = None
                                        self.fmac7_tst1_err_cnt = None
                                        self.fmac8_tst1_err_cnt = None
                                        self.fmac0_tst2_err_cnt = None
                                        self.fmac1_tst2_err_cnt = None
                                        self.fmac2_tst2_err_cnt = None
                                        self.fmac3_tst2_err_cnt = None
                                        self.fmac4_tst2_err_cnt = None
                                        self.fmac5_tst2_err_cnt = None
                                        self.fmac6_tst2_err_cnt = None
                                        self.fmac7_tst2_err_cnt = None
                                        self.fmac8_tst2_err_cnt = None
                                        self.fmac0_tst3_err_cnt = None
                                        self.fmac1_tst3_err_cnt = None
                                        self.fmac2_tst3_err_cnt = None
                                        self.fmac3_tst3_err_cnt = None
                                        self.fmac4_tst3_err_cnt = None
                                        self.fmac5_tst3_err_cnt = None
                                        self.fmac6_tst3_err_cnt = None
                                        self.fmac7_tst3_err_cnt = None
                                        self.fmac8_tst3_err_cnt = None
                                        self.fmac0_ecc_1b_err_cnt = None
                                        self.fmac1_ecc_1b_err_cnt = None
                                        self.fmac2_ecc_1b_err_cnt = None
                                        self.fmac3_ecc_1b_err_cnt = None
                                        self.fmac4_ecc_1b_err_cnt = None
                                        self.fmac5_ecc_1b_err_cnt = None
                                        self.fmac6_ecc_1b_err_cnt = None
                                        self.fmac7_ecc_1b_err_cnt = None
                                        self.fmac8_ecc_1b_err_cnt = None
                                        self.fmac0_ecc_2b_err_cnt = None
                                        self.fmac1_ecc_2b_err_cnt = None
                                        self.fmac2_ecc_2b_err_cnt = None
                                        self.fmac3_ecc_2b_err_cnt = None
                                        self.fmac4_ecc_2b_err_cnt = None
                                        self.fmac5_ecc_2b_err_cnt = None
                                        self.fmac6_ecc_2b_err_cnt = None
                                        self.fmac7_ecc_2b_err_cnt = None
                                        self.fmac8_ecc_2b_err_cnt = None
                                        self.olp_incoming_bad_identifier_counter = None
                                        self.olp_incoming_bad_reassembly_counter = None
                                        self.cfc_parity_err_cnt = None
                                        self.cfc_ilkn0_oob_rx_crc_err_cntr = None
                                        self.cfc_ilkn1_oob_rx_crc_err_cntr = None
                                        self.cfc_spi_oob_rx0_frm_err_cnt = None
                                        self.cfc_spi_oob_rx0_dip2_err_cnt = None
                                        self.cfc_spi_oob_rx1_frm_err_cnt = None
                                        self.cfc_spi_oob_rx1_dip2_err_cnt = None
                                        self.cgm_cgm_uc_pd_dropped_cnt = None
                                        self.cgm_cgm_mc_rep_pd_dropped_cnt = None
                                        self.cgm_cgm_uc_db_dropped_by_rqp_cnt = None
                                        self.cgm_cgm_uc_db_dropped_by_pqp_cnt = None
                                        self.cgm_cgm_mc_rep_db_dropped_cnt = None
                                        self.cgm_cgm_mc_db_dropped_cnt = None
                                        self.drca_full_err_cnt = None
                                        self.drca_single_err_cnt = None
                                        self.drca_calib_bist_full_err_cnt = None
                                        self.drca_loopback_full_err_cnt = None
                                        self.drcb_full_err_cnt = None
                                        self.drcb_single_err_cnt = None
                                        self.drcb_calib_bist_full_err_cnt = None
                                        self.drcb_loopback_full_err_cnt = None
                                        self.drcc_full_err_cnt = None
                                        self.drcc_single_err_cnt = None
                                        self.drcc_calib_bist_full_err_cnt = None
                                        self.drcc_loopback_full_err_cnt = None
                                        self.drcd_full_err_cnt = None
                                        self.drcd_single_err_cnt = None
                                        self.drcd_calib_bist_full_err_cnt = None
                                        self.drcd_loopback_full_err_cnt = None
                                        self.drce_full_err_cnt = None
                                        self.drce_single_err_cnt = None
                                        self.drce_calib_bist_full_err_cnt = None
                                        self.drce_loopback_full_err_cnt = None
                                        self.drcf_full_err_cnt = None
                                        self.drcf_single_err_cnt = None
                                        self.drcf_calib_bist_full_err_cnt = None
                                        self.drcf_loopback_full_err_cnt = None
                                        self.drcg_full_err_cnt = None
                                        self.drcg_single_err_cnt = None
                                        self.drcg_calib_bist_full_err_cnt = None
                                        self.drcg_loopback_full_err_cnt = None
                                        self.drch_full_err_cnt = None
                                        self.drch_single_err_cnt = None
                                        self.drch_calib_bist_full_err_cnt = None
                                        self.drch_loopback_full_err_cnt = None
                                        self.drcbroadcast_full_err_cnt = None
                                        self.drcbroadcast_single_err_cnt = None
                                        self.drcbroadcast_calib_bist_full_err_cnt = None
                                        self.drcbroadcast_loopback_full_err_cnt = None
                                        self._segment_path = lambda: "ovf-status"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.OvfStatus, ['cmic_cmc0_pkt_count_tx_pkt', 'cmic_cmc0_pkt_count_rx_pkt', 'nbi_stat_rx_bursts_err_cnt', 'nbi_ecc_1b_err_cnt', 'nbi_ecc_2b_err_cnt', 'nbi_parity_err_cnt', 'nbi_rx_ilkn_crc32_err_cnt', 'nbi_rx_ilkn0_crc24_err_cnt', 'nbi_rx_ilkn0_burst_err_cnt', 'nbi_rx_ilkn0_miss_sop_err_cnt', 'nbi_rx_ilkn0_miss_eop_err_cnt', 'nbi_rx_ilkn0_misaligned_cnt', 'nbi_rx_ilkn1_crc24_err_cnt', 'nbi_rx_ilkn1_burst_err_cnt', 'nbi_rx_ilkn1_miss_sop_err_cnt', 'nbi_rx_ilkn1_miss_eop_err_cnt', 'nbi_rx_ilkn1_misaligned_cnt', 'nbi_tx_ilkn1_flushed_bursts_cnt', 'nbi_rx_ilkn0_retrans_crc24_err_cnt', 'nbi_rx_ilkn0_retrans_retry_err_cnt', 'nbi_rx_ilkn0_retrans_wdog_err_cnt', 'nbi_rx_ilkn0_retrans_wrap_after_disc_err_cnt', 'nbi_rx_ilkn0_retrans_wrap_b4_disc_err_cnt', 'nbi_rx_ilkn0_retrans_reached_timeout_err_cnt', 'nbi_rx_ilkn1_retrans_crc24_err_cnt', 'nbi_rx_ilkn1_retrans_retry_err_cnt', 'nbi_rx_ilkn1_retrans_wdog_err_cnt', 'nbi_rx_ilkn1_retrans_wrap_after_disc_err_cnt', 'nbi_rx_ilkn1_retrans_wrap_b4_disc_err_cnt', 'nbi_rx_ilkn1_retrans_reached_timeout_err_cnt', 'nbi_stat_rx_frame_err_cnt', 'nbi_stat_tx_frame_err_cnt', 'nbi_rx_elk_err_bursts_cnt', 'nbi_rx_num_thrown_eops', 'nbi_rx_num_runts', 'nbi_bist_tx_crc_err_bursts_cnt', 'nbi_bist_rx_err_length_bursts_cnt', 'nbi_bist_rx_err_burst_index_cnt', 'nbi_bist_rx_err_bct_cnt', 'nbi_bist_rx_err_data_cnt', 'nbi_bist_rx_err_in_crc_err_cnt', 'nbi_bist_rx_err_sob_cnt', 'nbi_stat_tx_bursts_cnt', 'nbi_stat_tx_total_leng_cnt', 'rxaui_total_tx_pkt_count', 'rxaui_total_rx_pkt_count', 'rxaui_rx_pkt_count_bcast_pkt', 'rxaui_tx_pkt_count_bcast_pkt', 'rxaui_rx_pkt_count_mcast_pkt', 'rxaui_tx_pkt_count_mcast_pkt', 'rxaui_rx_pkt_count_ucast_pkt', 'rxaui_tx_pkt_count_ucast_pkt', 'rxaui_rx_err_drop_pkt_cnt', 'rxaui_tx_err_drop_pkt_cnt', 'rxaui_byte_count_tx_pkt', 'rxaui_byte_count_rx_pkt', 'rxaui_rx_dscrd_pkt_cnt', 'rxaui_tx_dscrd_pkt_cnt', 'ire_nif_packet_counter', 'il_total_rx_pkt_count', 'il_total_tx_pkt_count', 'il_rx_err_drop_pkt_cnt', 'il_tx_err_drop_pkt_cnt', 'il_byte_count_tx_pkt', 'il_byte_count_rx_pkt', 'il_rx_dscrd_pkt_cnt', 'il_tx_dscrd_pkt_cnt', 'il_rx_pkt_count_bcast_pkt', 'il_tx_pkt_count_bcast_pkt', 'il_rx_pkt_count_mcast_pkt', 'il_tx_pkt_count_mcast_pkt', 'il_rx_pkt_count_ucast_pkt', 'il_tx_pkt_count_ucast_pkt', 'iqm_enq_pkt_cnt', 'iqm_enq_byte_cnt', 'iqm_deq_pkt_cnt', 'iqm_deq_byte_cnt', 'iqm_tot_dscrd_pkt_cnt', 'iqm_tot_dscrd_byte_cnt', 'iqm_ecc_1b_err_cnt', 'iqm_ecc_2b_err_cnt', 'iqm_parity_err_cnt', 'iqm_deq_delete_pkt_cnt', 'iqm_ecn_dscrd_msk_pkt_cnt', 'iqm_q_tot_dscrd_pkt_cnt', 'iqm_q_deq_delete_pkt_cnt', 'iqm_rjct_db_pkt_cnt', 'iqm_rjct_bdb_pkt_cnt', 'iqm_rjct_bdb_protct_pkt_cnt', 'iqm_rjct_oc_bd_pkt_cnt', 'iqm_rjct_sn_err_pkt_cnt', 'iqm_rjct_mc_err_pkt_cnt', 'iqm_rjct_rsrc_err_pkt_cnt', 'iqm_rjct_qnvalid_err_pkt_cnt', 'iqm_rjct_cnm_pkt_cnt', 'iqm_rjct_dyn_space_pkt_cnt', 'ipt_fdt_pkt_cnt', 'ipt_ecc_1b_err_cnt', 'ipt_ecc_2b_err_cnt', 'ipt_parity_err_cnt', 'ipt_crc_err_cnt', 'ipt_crc_err_del_buff_cnt', 'ipt_cpu_del_buff_cnt', 'ipt_cpu_rel_buff_cnt', 'ipt_crc_err_buff_fifo_full_cnt', 'fdt_data_cell_cnt', 'fdt_data_byte_cnt', 'fdt_crc_dropped_pck_cnt', 'fdt_invalid_destq_drop_cell_cnt', 'fdt_indirect_command_count', 'fdt_ecc_1b_err_cnt', 'fdt_ecc_2b_err_cnt', 'fdt_parity_err_cnt', 'fdt_crc_dropped_cell_cnt', 'fcr_control_cell_cnt', 'fcr_cell_drop_cnt', 'fcr_credit_cell_drop_cnt', 'fcr_fs_cell_drop_cnt', 'fcr_rt_cell_drop_cnt', 'fcr_ecc_1b_err_cnt', 'fcr_ecc_2b_err_cnt', 'fdr_data_cell_cnt', 'fdr_data_byte_cnt', 'fdr_crc_dropped_pck_cnt', 'fdr_p_pkt_cnt', 'fdr_prm_error_filter_cnt', 'fdr_sec_error_filter_cnt', 'fdr_prm_ecc_1b_err_cnt', 'fdr_prm_ecc_2b_err_cnt', 'fdr_sec_ecc_1b_err_cnt', 'fdr_sec_ecc_2b_err_cnt', 'egq_ecc_1b_err_cnt', 'egq_ecc_2b_err_cnt', 'egq_parity_err_cnt', 'egq_dbf_ecc_1b_err_cnt', 'egq_dbf_ecc_2b_err_cnt', 'egq_empty_mcid_counter', 'egq_rqp_discard_packet_counter', 'egq_ehp_discard_packet_counter', 'egq_ipt_pkt_cnt', 'epni_epe_pkt_cnt', 'epni_epe_byte_cnt', 'epni_epe_discard_pkt_cnt', 'epni_ecc_1b_err_cnt', 'epni_ecc_2b_err_cnt', 'epni_parity_err_cnt', 'egq_pqp_ucast_pkt_cnt', 'egq_pqp_ucast_h_pkt_cnt', 'egq_pqp_ucast_l_pkt_cnt', 'egq_pqp_ucast_bytes_cnt', 'egq_pqp_ucast_discard_pkt_cnt', 'egq_pqp_mcast_pkt_cnt', 'egq_pqp_mcast_h_pkt_cnt', 'egq_pqp_mcast_l_pkt_cnt', 'egq_pqp_mcast_bytes_cnt', 'egq_pqp_mcast_discard_pkt_cnt', 'fct_control_cell_cnt', 'fct_unrch_crdt_cnt', 'idr_reassembly_errors', 'idr_mmu_ecc_1b_err_cnt', 'idr_mmu_ecc_2b_err_cnt', 'idr_discarded_packets0_cnt', 'idr_discarded_packets1_cnt', 'idr_discarded_packets2_cnt', 'idr_discarded_packets3_cnt', 'idr_discarded_octets0_cnt', 'idr_discarded_octets1_cnt', 'idr_discarded_octets2_cnt', 'idr_discarded_octets3_cnt', 'mmu_ecc_1b_err_cnt', 'mmu_ecc_2b_err_cnt', 'oamp_parity_err_cnt', 'oamp_ecc_1b_err_cnt', 'oamp_ecc_2b_err_cnt', 'crps_parity_err_cnt', 'fmac0_kpcs0_tst_rx_err_cnt', 'fmac1_kpcs0_tst_rx_err_cnt', 'fmac2_kpcs0_tst_rx_err_cnt', 'fmac3_kpcs0_tst_rx_err_cnt', 'fmac4_kpcs0_tst_rx_err_cnt', 'fmac5_kpcs0_tst_rx_err_cnt', 'fmac6_kpcs0_tst_rx_err_cnt', 'fmac7_kpcs0_tst_rx_err_cnt', 'fmac8_kpcs0_tst_rx_err_cnt', 'fmac0_kpcs1_tst_rx_err_cnt', 'fmac1_kpcs1_tst_rx_err_cnt', 'fmac2_kpcs1_tst_rx_err_cnt', 'fmac3_kpcs1_tst_rx_err_cnt', 'fmac4_kpcs1_tst_rx_err_cnt', 'fmac5_kpcs1_tst_rx_err_cnt', 'fmac6_kpcs1_tst_rx_err_cnt', 'fmac7_kpcs1_tst_rx_err_cnt', 'fmac8_kpcs1_tst_rx_err_cnt', 'fmac0_kpcs2_tst_rx_err_cnt', 'fmac1_kpcs2_tst_rx_err_cnt', 'fmac2_kpcs2_tst_rx_err_cnt', 'fmac3_kpcs2_tst_rx_err_cnt', 'fmac4_kpcs2_tst_rx_err_cnt', 'fmac5_kpcs2_tst_rx_err_cnt', 'fmac6_kpcs2_tst_rx_err_cnt', 'fmac7_kpcs2_tst_rx_err_cnt', 'fmac8_kpcs2_tst_rx_err_cnt', 'fmac0_kpcs3_tst_rx_err_cnt', 'fmac1_kpcs3_tst_rx_err_cnt', 'fmac2_kpcs3_tst_rx_err_cnt', 'fmac3_kpcs3_tst_rx_err_cnt', 'fmac4_kpcs3_tst_rx_err_cnt', 'fmac5_kpcs3_tst_rx_err_cnt', 'fmac6_kpcs3_tst_rx_err_cnt', 'fmac7_kpcs3_tst_rx_err_cnt', 'fmac8_kpcs3_tst_rx_err_cnt', 'fmac0_tst0_err_cnt', 'fmac1_tst0_err_cnt', 'fmac2_tst0_err_cnt', 'fmac3_tst0_err_cnt', 'fmac4_tst0_err_cnt', 'fmac5_tst0_err_cnt', 'fmac6_tst0_err_cnt', 'fmac7_tst0_err_cnt', 'fmac8_tst0_err_cnt', 'fmac0_tst1_err_cnt', 'fmac1_tst1_err_cnt', 'fmac2_tst1_err_cnt', 'fmac3_tst1_err_cnt', 'fmac4_tst1_err_cnt', 'fmac5_tst1_err_cnt', 'fmac6_tst1_err_cnt', 'fmac7_tst1_err_cnt', 'fmac8_tst1_err_cnt', 'fmac0_tst2_err_cnt', 'fmac1_tst2_err_cnt', 'fmac2_tst2_err_cnt', 'fmac3_tst2_err_cnt', 'fmac4_tst2_err_cnt', 'fmac5_tst2_err_cnt', 'fmac6_tst2_err_cnt', 'fmac7_tst2_err_cnt', 'fmac8_tst2_err_cnt', 'fmac0_tst3_err_cnt', 'fmac1_tst3_err_cnt', 'fmac2_tst3_err_cnt', 'fmac3_tst3_err_cnt', 'fmac4_tst3_err_cnt', 'fmac5_tst3_err_cnt', 'fmac6_tst3_err_cnt', 'fmac7_tst3_err_cnt', 'fmac8_tst3_err_cnt', 'fmac0_ecc_1b_err_cnt', 'fmac1_ecc_1b_err_cnt', 'fmac2_ecc_1b_err_cnt', 'fmac3_ecc_1b_err_cnt', 'fmac4_ecc_1b_err_cnt', 'fmac5_ecc_1b_err_cnt', 'fmac6_ecc_1b_err_cnt', 'fmac7_ecc_1b_err_cnt', 'fmac8_ecc_1b_err_cnt', 'fmac0_ecc_2b_err_cnt', 'fmac1_ecc_2b_err_cnt', 'fmac2_ecc_2b_err_cnt', 'fmac3_ecc_2b_err_cnt', 'fmac4_ecc_2b_err_cnt', 'fmac5_ecc_2b_err_cnt', 'fmac6_ecc_2b_err_cnt', 'fmac7_ecc_2b_err_cnt', 'fmac8_ecc_2b_err_cnt', 'olp_incoming_bad_identifier_counter', 'olp_incoming_bad_reassembly_counter', 'cfc_parity_err_cnt', 'cfc_ilkn0_oob_rx_crc_err_cntr', 'cfc_ilkn1_oob_rx_crc_err_cntr', 'cfc_spi_oob_rx0_frm_err_cnt', 'cfc_spi_oob_rx0_dip2_err_cnt', 'cfc_spi_oob_rx1_frm_err_cnt', 'cfc_spi_oob_rx1_dip2_err_cnt', 'cgm_cgm_uc_pd_dropped_cnt', 'cgm_cgm_mc_rep_pd_dropped_cnt', 'cgm_cgm_uc_db_dropped_by_rqp_cnt', 'cgm_cgm_uc_db_dropped_by_pqp_cnt', 'cgm_cgm_mc_rep_db_dropped_cnt', 'cgm_cgm_mc_db_dropped_cnt', 'drca_full_err_cnt', 'drca_single_err_cnt', 'drca_calib_bist_full_err_cnt', 'drca_loopback_full_err_cnt', 'drcb_full_err_cnt', 'drcb_single_err_cnt', 'drcb_calib_bist_full_err_cnt', 'drcb_loopback_full_err_cnt', 'drcc_full_err_cnt', 'drcc_single_err_cnt', 'drcc_calib_bist_full_err_cnt', 'drcc_loopback_full_err_cnt', 'drcd_full_err_cnt', 'drcd_single_err_cnt', 'drcd_calib_bist_full_err_cnt', 'drcd_loopback_full_err_cnt', 'drce_full_err_cnt', 'drce_single_err_cnt', 'drce_calib_bist_full_err_cnt', 'drce_loopback_full_err_cnt', 'drcf_full_err_cnt', 'drcf_single_err_cnt', 'drcf_calib_bist_full_err_cnt', 'drcf_loopback_full_err_cnt', 'drcg_full_err_cnt', 'drcg_single_err_cnt', 'drcg_calib_bist_full_err_cnt', 'drcg_loopback_full_err_cnt', 'drch_full_err_cnt', 'drch_single_err_cnt', 'drch_calib_bist_full_err_cnt', 'drch_loopback_full_err_cnt', 'drcbroadcast_full_err_cnt', 'drcbroadcast_single_err_cnt', 'drcbroadcast_calib_bist_full_err_cnt', 'drcbroadcast_loopback_full_err_cnt'], name, value)





                        class FmacStatistics(Entity):
                            """
                            Statistics of FMAC
                            
                            .. attribute:: fmac_links
                            
                            	Link table for statistics
                            	**type**\:  :py:class:`FmacLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks>`
                            
                            	**config**\: False
                            
                            

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
                                
                                	**config**\: False
                                
                                

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
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fmac_asic
                                    
                                    	Single aisc information
                                    	**type**\: list of  		 :py:class:`FmacAsic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic>`
                                    
                                    	**config**\: False
                                    
                                    

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
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggr_stats
                                        
                                        	aggr stats
                                        	**type**\:  :py:class:`AggrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: incr_stats
                                        
                                        	incr stats
                                        	**type**\:  :py:class:`IncrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: valid
                                        
                                        	valid
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: rack_no
                                        
                                        	rack no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: slot_no
                                        
                                        	slot no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: link_no
                                        
                                        	link no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: link_valid
                                        
                                        	link valid
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

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
                                            self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, ['asic', 'valid', 'rack_no', 'slot_no', 'asic_instance', 'link_no', 'link_valid'], name, value)


                                        class AggrStats(Entity):
                                            """
                                            aggr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:  :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:  :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:  :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus>`
                                            
                                            	**config**\: False
                                            
                                            

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
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, ['link_crc_error', 'link_size_error', 'link_mis_align_error', 'link_code_group_error', 'link_no_sig_lock_error', 'link_no_sig_accept_error', 'link_tokens_error', 'error_token_count'], name, value)



                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, ['tx_control_cells_counter', 'tx_data_cell_counter', 'tx_data_byte_counter', 'rx_crc_errors_counter', 'rx_lfec_fec_correctable_error', 'rx_8b_10b_disparity_errors', 'rx_control_cells_counter', 'rx_data_cell_counter', 'rx_data_byte_counter', 'rx_dropped_retransmitted_control', 'tx_asyn_fifo_rate', 'rx_asyn_fifo_rate', 'rx_lfec_fec_uncorrectable_errors', 'rx_8b_10b_code_errors'], name, value)



                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, ['tx_control_cells_counter', 'tx_data_cell_counter', 'tx_data_byte_counter', 'rx_crc_errors_counter', 'rx_lfec_fec_correctable_error', 'rx_8b_10b_disparity_errors', 'rx_control_cells_counter', 'rx_data_cell_counter', 'rx_data_byte_counter', 'rx_dropped_retransmitted_control', 'tx_asyn_fifo_rate', 'rx_asyn_fifo_rate', 'rx_lfec_fec_uncorrectable_errors', 'rx_8b_10b_code_errors'], name, value)




                                        class IncrStats(Entity):
                                            """
                                            incr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:  :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:  :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:  :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus>`
                                            
                                            	**config**\: False
                                            
                                            

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
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, ['link_crc_error', 'link_size_error', 'link_mis_align_error', 'link_code_group_error', 'link_no_sig_lock_error', 'link_no_sig_accept_error', 'link_tokens_error', 'error_token_count'], name, value)



                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, ['tx_control_cells_counter', 'tx_data_cell_counter', 'tx_data_byte_counter', 'rx_crc_errors_counter', 'rx_lfec_fec_correctable_error', 'rx_8b_10b_disparity_errors', 'rx_control_cells_counter', 'rx_data_cell_counter', 'rx_data_byte_counter', 'rx_dropped_retransmitted_control', 'tx_asyn_fifo_rate', 'rx_asyn_fifo_rate', 'rx_lfec_fec_uncorrectable_errors', 'rx_8b_10b_code_errors'], name, value)



                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**length:** 0..6
                                                
                                                	**config**\: False
                                                
                                                

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
                                                    self._perform_setattr(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, ['tx_control_cells_counter', 'tx_data_cell_counter', 'tx_data_byte_counter', 'rx_crc_errors_counter', 'rx_lfec_fec_correctable_error', 'rx_8b_10b_disparity_errors', 'rx_control_cells_counter', 'rx_data_cell_counter', 'rx_data_byte_counter', 'rx_dropped_retransmitted_control', 'tx_asyn_fifo_rate', 'rx_asyn_fifo_rate', 'rx_lfec_fec_uncorrectable_errors', 'rx_8b_10b_code_errors'], name, value)












    def clone_ptr(self):
        self._top_entity = Fia()
        return self._top_entity



