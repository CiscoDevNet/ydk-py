""" Cisco_IOS_XR_dnx_driver_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-driver package operational data.

This module contains definitions
for the following management objects\:
  fia\: FIA driver operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AdminState(Enum):
    """
    AdminState

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
    Asic

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
    AsicAccessState

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
    AsicInitMethod

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
    AsicOperState

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
    FcMode

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
    Link

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
    LinkErrorState

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
    LinkStage

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
    OperState

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
    Rack

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
    SliceState

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes>`
    
    

    """

    _prefix = 'dnx-driver-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fia, self).__init__()
        self._top_entity = None

        self.yang_name = "fia"
        self.yang_parent_name = "Cisco-IOS-XR-dnx-driver-oper"

        self.nodes = Fia.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        FIA driver operational data for available nodes
        
        .. attribute:: node
        
        	FIA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-driver-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fia.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fia"

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
                        super(Fia.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Fia.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            FIA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: asic_statistics
            
            	FIA asic statistics information
            	**type**\:   :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics>`
            
            .. attribute:: clear_statistics
            
            	Clear statistics information
            	**type**\:   :py:class:`ClearStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics>`
            
            .. attribute:: diag_shell
            
            	FIA diag shell information
            	**type**\:   :py:class:`DiagShell <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell>`
            
            .. attribute:: driver_information
            
            	FIA driver information
            	**type**\:   :py:class:`DriverInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation>`
            
            .. attribute:: oir_history
            
            	FIA operational data of oir history
            	**type**\:   :py:class:`OirHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory>`
            
            .. attribute:: rx_link_information
            
            	FIA link rx information
            	**type**\:   :py:class:`RxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation>`
            
            .. attribute:: tx_link_information
            
            	FIA link TX information
            	**type**\:   :py:class:`TxLinkInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation>`
            
            

            """

            _prefix = 'dnx-driver-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fia.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.asic_statistics = Fia.Nodes.Node.AsicStatistics()
                self.asic_statistics.parent = self
                self._children_name_map["asic_statistics"] = "asic-statistics"
                self._children_yang_names.add("asic-statistics")

                self.clear_statistics = Fia.Nodes.Node.ClearStatistics()
                self.clear_statistics.parent = self
                self._children_name_map["clear_statistics"] = "clear-statistics"
                self._children_yang_names.add("clear-statistics")

                self.diag_shell = Fia.Nodes.Node.DiagShell()
                self.diag_shell.parent = self
                self._children_name_map["diag_shell"] = "diag-shell"
                self._children_yang_names.add("diag-shell")

                self.driver_information = Fia.Nodes.Node.DriverInformation()
                self.driver_information.parent = self
                self._children_name_map["driver_information"] = "driver-information"
                self._children_yang_names.add("driver-information")

                self.oir_history = Fia.Nodes.Node.OirHistory()
                self.oir_history.parent = self
                self._children_name_map["oir_history"] = "oir-history"
                self._children_yang_names.add("oir-history")

                self.rx_link_information = Fia.Nodes.Node.RxLinkInformation()
                self.rx_link_information.parent = self
                self._children_name_map["rx_link_information"] = "rx-link-information"
                self._children_yang_names.add("rx-link-information")

                self.tx_link_information = Fia.Nodes.Node.TxLinkInformation()
                self.tx_link_information.parent = self
                self._children_name_map["tx_link_information"] = "tx-link-information"
                self._children_yang_names.add("tx-link-information")

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
                            super(Fia.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Fia.Nodes.Node, self).__setattr__(name, value)


            class RxLinkInformation(Entity):
                """
                FIA link rx information
                
                .. attribute:: link_options
                
                	Option table for link rx information
                	**type**\:   :py:class:`LinkOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.RxLinkInformation, self).__init__()

                    self.yang_name = "rx-link-information"
                    self.yang_parent_name = "node"

                    self.link_options = Fia.Nodes.Node.RxLinkInformation.LinkOptions()
                    self.link_options.parent = self
                    self._children_name_map["link_options"] = "link-options"
                    self._children_yang_names.add("link-options")


                class LinkOptions(Entity):
                    """
                    Option table for link rx information
                    
                    .. attribute:: link_option
                    
                    	Option \: topo , flag , stats
                    	**type**\: list of    :py:class:`LinkOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions, self).__init__()

                        self.yang_name = "link-options"
                        self.yang_parent_name = "rx-link-information"

                        self.link_option = YList(self)

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
                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions, self).__setattr__(name, value)


                    class LinkOption(Entity):
                        """
                        Option \: topo , flag , stats
                        
                        .. attribute:: option  <key>
                        
                        	Link option
                        	**type**\:  str
                        
                        	**pattern:** (flap)\|(topo)
                        
                        .. attribute:: rx_asic_instances
                        
                        	Instance table for rx information
                        	**type**\:   :py:class:`RxAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption, self).__init__()

                            self.yang_name = "link-option"
                            self.yang_parent_name = "link-options"

                            self.option = YLeaf(YType.str, "option")

                            self.rx_asic_instances = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances()
                            self.rx_asic_instances.parent = self
                            self._children_name_map["rx_asic_instances"] = "rx-asic-instances"
                            self._children_yang_names.add("rx-asic-instances")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("option") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption, self).__setattr__(name, value)


                        class RxAsicInstances(Entity):
                            """
                            Instance table for rx information
                            
                            .. attribute:: rx_asic_instance
                            
                            	Instance number for rx link information
                            	**type**\: list of    :py:class:`RxAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances, self).__init__()

                                self.yang_name = "rx-asic-instances"
                                self.yang_parent_name = "link-option"

                                self.rx_asic_instance = YList(self)

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
                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances, self).__setattr__(name, value)


                            class RxAsicInstance(Entity):
                                """
                                Instance number for rx link information
                                
                                .. attribute:: instance  <key>
                                
                                	Receive instance
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rx_links
                                
                                	Link table class for rx information
                                	**type**\:   :py:class:`RxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance, self).__init__()

                                    self.yang_name = "rx-asic-instance"
                                    self.yang_parent_name = "rx-asic-instances"

                                    self.instance = YLeaf(YType.uint32, "instance")

                                    self.rx_links = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks()
                                    self.rx_links.parent = self
                                    self._children_name_map["rx_links"] = "rx-links"
                                    self._children_yang_names.add("rx-links")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("instance") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance, self).__setattr__(name, value)


                                class RxLinks(Entity):
                                    """
                                    Link table class for rx information
                                    
                                    .. attribute:: rx_link
                                    
                                    	Link number for rx link information
                                    	**type**\: list of    :py:class:`RxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks, self).__init__()

                                        self.yang_name = "rx-links"
                                        self.yang_parent_name = "rx-asic-instance"

                                        self.rx_link = YList(self)

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
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks, self).__setattr__(name, value)


                                    class RxLink(Entity):
                                        """
                                        Link number for rx link information
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\:  int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: rx_link
                                        
                                        	Single link information
                                        	**type**\: list of    :py:class:`RxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink>`
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\:  int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: status_option
                                        
                                        	RX link status option
                                        	**type**\:  str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink, self).__init__()

                                            self.yang_name = "rx-link"
                                            self.yang_parent_name = "rx-links"

                                            self.end_number = YLeaf(YType.uint32, "end-number")

                                            self.start_number = YLeaf(YType.uint32, "start-number")

                                            self.status_option = YLeaf(YType.str, "status-option")

                                            self.rx_link = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("end_number",
                                                            "start_number",
                                                            "status_option") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink, self).__setattr__(name, value)


                                        class RxLink(Entity):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  <key>
                                            
                                            	Single link
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            .. attribute:: correctable_errors
                                            
                                            	correctable errors
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:   :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:   :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink>`
                                            
                                            .. attribute:: far_end_link_in_hw
                                            
                                            	far end link in hw
                                            	**type**\:   :py:class:`FarEndLinkInHw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw>`
                                            
                                            .. attribute:: flags
                                            
                                            	flags
                                            	**type**\:  str
                                            
                                            .. attribute:: flap_cnt
                                            
                                            	flap cnt
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History>`
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\:  bool
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:   :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	Stage
                                            	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:   :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink>`
                                            
                                            .. attribute:: uncorrectable_errors
                                            
                                            	uncorrectable errors
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink, self).__init__()

                                                self.yang_name = "rx-link"
                                                self.yang_parent_name = "rx-link"

                                                self.link = YLeaf(YType.int32, "link")

                                                self.admin_state = YLeaf(YType.enumeration, "admin-state")

                                                self.correctable_errors = YLeaf(YType.uint64, "correctable-errors")

                                                self.error_state = YLeaf(YType.enumeration, "error-state")

                                                self.flags = YLeaf(YType.str, "flags")

                                                self.flap_cnt = YLeaf(YType.uint32, "flap-cnt")

                                                self.is_conf_pending = YLeaf(YType.boolean, "is-conf-pending")

                                                self.is_link_valid = YLeaf(YType.boolean, "is-link-valid")

                                                self.num_admin_shuts = YLeaf(YType.uint32, "num-admin-shuts")

                                                self.oper_state = YLeaf(YType.enumeration, "oper-state")

                                                self.speed = YLeaf(YType.uint32, "speed")

                                                self.stage = YLeaf(YType.enumeration, "stage")

                                                self.uncorrectable_errors = YLeaf(YType.uint64, "uncorrectable-errors")

                                                self.far_end_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink()
                                                self.far_end_link.parent = self
                                                self._children_name_map["far_end_link"] = "far-end-link"
                                                self._children_yang_names.add("far-end-link")

                                                self.far_end_link_in_hw = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw()
                                                self.far_end_link_in_hw.parent = self
                                                self._children_name_map["far_end_link_in_hw"] = "far-end-link-in-hw"
                                                self._children_yang_names.add("far-end-link-in-hw")

                                                self.history = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History()
                                                self.history.parent = self
                                                self._children_name_map["history"] = "history"
                                                self._children_yang_names.add("history")

                                                self.this_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink()
                                                self.this_link.parent = self
                                                self._children_name_map["this_link"] = "this-link"
                                                self._children_yang_names.add("this-link")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("link",
                                                                "admin_state",
                                                                "correctable_errors",
                                                                "error_state",
                                                                "flags",
                                                                "flap_cnt",
                                                                "is_conf_pending",
                                                                "is_link_valid",
                                                                "num_admin_shuts",
                                                                "oper_state",
                                                                "speed",
                                                                "stage",
                                                                "uncorrectable_errors") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink, self).__setattr__(name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink, self).__init__()

                                                    self.yang_name = "this-link"
                                                    self.yang_parent_name = "rx-link"

                                                    self.link_num = YLeaf(YType.uint32, "link-num")

                                                    self.link_stage = YLeaf(YType.enumeration, "link-stage")

                                                    self.link_type = YLeaf(YType.enumeration, "link-type")

                                                    self.phy_link_num = YLeaf(YType.uint32, "phy-link-num")

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._children_yang_names.add("asic-id")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("link_num",
                                                                    "link_stage",
                                                                    "link_type",
                                                                    "phy_link_num") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink, self).__setattr__(name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "this-link"

                                                        self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                                        self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                                        self.rack_num = YLeaf(YType.uint32, "rack-num")

                                                        self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                                        self.slot_num = YLeaf(YType.uint32, "slot-num")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("asic_instance",
                                                                        "asic_type",
                                                                        "rack_num",
                                                                        "rack_type",
                                                                        "slot_num") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.asic_instance.is_set or
                                                            self.asic_type.is_set or
                                                            self.rack_num.is_set or
                                                            self.rack_type.is_set or
                                                            self.slot_num.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.asic_instance.yfilter != YFilter.not_set or
                                                            self.asic_type.yfilter != YFilter.not_set or
                                                            self.rack_num.yfilter != YFilter.not_set or
                                                            self.rack_type.yfilter != YFilter.not_set or
                                                            self.slot_num.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "asic-id" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                                        if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_type.get_name_leafdata())
                                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                        if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_type.get_name_leafdata())
                                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.slot_num.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "asic-instance"):
                                                            self.asic_instance = value
                                                            self.asic_instance.value_namespace = name_space
                                                            self.asic_instance.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "asic-type"):
                                                            self.asic_type = value
                                                            self.asic_type.value_namespace = name_space
                                                            self.asic_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-num"):
                                                            self.rack_num = value
                                                            self.rack_num.value_namespace = name_space
                                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-type"):
                                                            self.rack_type = value
                                                            self.rack_type.value_namespace = name_space
                                                            self.rack_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "slot-num"):
                                                            self.slot_num = value
                                                            self.slot_num.value_namespace = name_space
                                                            self.slot_num.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        self.link_num.is_set or
                                                        self.link_stage.is_set or
                                                        self.link_type.is_set or
                                                        self.phy_link_num.is_set or
                                                        (self.asic_id is not None and self.asic_id.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.link_num.yfilter != YFilter.not_set or
                                                        self.link_stage.yfilter != YFilter.not_set or
                                                        self.link_type.yfilter != YFilter.not_set or
                                                        self.phy_link_num.yfilter != YFilter.not_set or
                                                        (self.asic_id is not None and self.asic_id.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "this-link" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.link_num.is_set or self.link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_num.get_name_leafdata())
                                                    if (self.link_stage.is_set or self.link_stage.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_stage.get_name_leafdata())
                                                    if (self.link_type.is_set or self.link_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_type.get_name_leafdata())
                                                    if (self.phy_link_num.is_set or self.phy_link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.phy_link_num.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "asic-id"):
                                                        if (self.asic_id is None):
                                                            self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId()
                                                            self.asic_id.parent = self
                                                            self._children_name_map["asic_id"] = "asic-id"
                                                        return self.asic_id

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "asic-id" or name == "link-num" or name == "link-stage" or name == "link-type" or name == "phy-link-num"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "link-num"):
                                                        self.link_num = value
                                                        self.link_num.value_namespace = name_space
                                                        self.link_num.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-stage"):
                                                        self.link_stage = value
                                                        self.link_stage.value_namespace = name_space
                                                        self.link_stage.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-type"):
                                                        self.link_type = value
                                                        self.link_type.value_namespace = name_space
                                                        self.link_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "phy-link-num"):
                                                        self.phy_link_num = value
                                                        self.phy_link_num.value_namespace = name_space
                                                        self.phy_link_num.value_namespace_prefix = name_space_prefix


                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink, self).__init__()

                                                    self.yang_name = "far-end-link"
                                                    self.yang_parent_name = "rx-link"

                                                    self.link_num = YLeaf(YType.uint32, "link-num")

                                                    self.link_stage = YLeaf(YType.enumeration, "link-stage")

                                                    self.link_type = YLeaf(YType.enumeration, "link-type")

                                                    self.phy_link_num = YLeaf(YType.uint32, "phy-link-num")

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._children_yang_names.add("asic-id")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("link_num",
                                                                    "link_stage",
                                                                    "link_type",
                                                                    "phy_link_num") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink, self).__setattr__(name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link"

                                                        self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                                        self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                                        self.rack_num = YLeaf(YType.uint32, "rack-num")

                                                        self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                                        self.slot_num = YLeaf(YType.uint32, "slot-num")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("asic_instance",
                                                                        "asic_type",
                                                                        "rack_num",
                                                                        "rack_type",
                                                                        "slot_num") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.asic_instance.is_set or
                                                            self.asic_type.is_set or
                                                            self.rack_num.is_set or
                                                            self.rack_type.is_set or
                                                            self.slot_num.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.asic_instance.yfilter != YFilter.not_set or
                                                            self.asic_type.yfilter != YFilter.not_set or
                                                            self.rack_num.yfilter != YFilter.not_set or
                                                            self.rack_type.yfilter != YFilter.not_set or
                                                            self.slot_num.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "asic-id" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                                        if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_type.get_name_leafdata())
                                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                        if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_type.get_name_leafdata())
                                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.slot_num.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "asic-instance"):
                                                            self.asic_instance = value
                                                            self.asic_instance.value_namespace = name_space
                                                            self.asic_instance.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "asic-type"):
                                                            self.asic_type = value
                                                            self.asic_type.value_namespace = name_space
                                                            self.asic_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-num"):
                                                            self.rack_num = value
                                                            self.rack_num.value_namespace = name_space
                                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-type"):
                                                            self.rack_type = value
                                                            self.rack_type.value_namespace = name_space
                                                            self.rack_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "slot-num"):
                                                            self.slot_num = value
                                                            self.slot_num.value_namespace = name_space
                                                            self.slot_num.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        self.link_num.is_set or
                                                        self.link_stage.is_set or
                                                        self.link_type.is_set or
                                                        self.phy_link_num.is_set or
                                                        (self.asic_id is not None and self.asic_id.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.link_num.yfilter != YFilter.not_set or
                                                        self.link_stage.yfilter != YFilter.not_set or
                                                        self.link_type.yfilter != YFilter.not_set or
                                                        self.phy_link_num.yfilter != YFilter.not_set or
                                                        (self.asic_id is not None and self.asic_id.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "far-end-link" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.link_num.is_set or self.link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_num.get_name_leafdata())
                                                    if (self.link_stage.is_set or self.link_stage.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_stage.get_name_leafdata())
                                                    if (self.link_type.is_set or self.link_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_type.get_name_leafdata())
                                                    if (self.phy_link_num.is_set or self.phy_link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.phy_link_num.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "asic-id"):
                                                        if (self.asic_id is None):
                                                            self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId()
                                                            self.asic_id.parent = self
                                                            self._children_name_map["asic_id"] = "asic-id"
                                                        return self.asic_id

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "asic-id" or name == "link-num" or name == "link-stage" or name == "link-type" or name == "phy-link-num"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "link-num"):
                                                        self.link_num = value
                                                        self.link_num.value_namespace = name_space
                                                        self.link_num.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-stage"):
                                                        self.link_stage = value
                                                        self.link_stage.value_namespace = name_space
                                                        self.link_stage.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-type"):
                                                        self.link_type = value
                                                        self.link_type.value_namespace = name_space
                                                        self.link_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "phy-link-num"):
                                                        self.phy_link_num = value
                                                        self.phy_link_num.value_namespace = name_space
                                                        self.phy_link_num.value_namespace_prefix = name_space_prefix


                                            class FarEndLinkInHw(Entity):
                                                """
                                                far end link in hw
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw, self).__init__()

                                                    self.yang_name = "far-end-link-in-hw"
                                                    self.yang_parent_name = "rx-link"

                                                    self.link_num = YLeaf(YType.uint32, "link-num")

                                                    self.link_stage = YLeaf(YType.enumeration, "link-stage")

                                                    self.link_type = YLeaf(YType.enumeration, "link-type")

                                                    self.phy_link_num = YLeaf(YType.uint32, "phy-link-num")

                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._children_yang_names.add("asic-id")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("link_num",
                                                                    "link_stage",
                                                                    "link_type",
                                                                    "phy_link_num") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw, self).__setattr__(name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link-in-hw"

                                                        self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                                        self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                                        self.rack_num = YLeaf(YType.uint32, "rack-num")

                                                        self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                                        self.slot_num = YLeaf(YType.uint32, "slot-num")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("asic_instance",
                                                                        "asic_type",
                                                                        "rack_num",
                                                                        "rack_type",
                                                                        "slot_num") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.asic_instance.is_set or
                                                            self.asic_type.is_set or
                                                            self.rack_num.is_set or
                                                            self.rack_type.is_set or
                                                            self.slot_num.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.asic_instance.yfilter != YFilter.not_set or
                                                            self.asic_type.yfilter != YFilter.not_set or
                                                            self.rack_num.yfilter != YFilter.not_set or
                                                            self.rack_type.yfilter != YFilter.not_set or
                                                            self.slot_num.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "asic-id" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                                        if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_type.get_name_leafdata())
                                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                        if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_type.get_name_leafdata())
                                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.slot_num.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "asic-instance"):
                                                            self.asic_instance = value
                                                            self.asic_instance.value_namespace = name_space
                                                            self.asic_instance.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "asic-type"):
                                                            self.asic_type = value
                                                            self.asic_type.value_namespace = name_space
                                                            self.asic_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-num"):
                                                            self.rack_num = value
                                                            self.rack_num.value_namespace = name_space
                                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-type"):
                                                            self.rack_type = value
                                                            self.rack_type.value_namespace = name_space
                                                            self.rack_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "slot-num"):
                                                            self.slot_num = value
                                                            self.slot_num.value_namespace = name_space
                                                            self.slot_num.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        self.link_num.is_set or
                                                        self.link_stage.is_set or
                                                        self.link_type.is_set or
                                                        self.phy_link_num.is_set or
                                                        (self.asic_id is not None and self.asic_id.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.link_num.yfilter != YFilter.not_set or
                                                        self.link_stage.yfilter != YFilter.not_set or
                                                        self.link_type.yfilter != YFilter.not_set or
                                                        self.phy_link_num.yfilter != YFilter.not_set or
                                                        (self.asic_id is not None and self.asic_id.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "far-end-link-in-hw" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.link_num.is_set or self.link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_num.get_name_leafdata())
                                                    if (self.link_stage.is_set or self.link_stage.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_stage.get_name_leafdata())
                                                    if (self.link_type.is_set or self.link_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_type.get_name_leafdata())
                                                    if (self.phy_link_num.is_set or self.phy_link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.phy_link_num.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "asic-id"):
                                                        if (self.asic_id is None):
                                                            self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId()
                                                            self.asic_id.parent = self
                                                            self._children_name_map["asic_id"] = "asic-id"
                                                        return self.asic_id

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "asic-id" or name == "link-num" or name == "link-stage" or name == "link-type" or name == "phy-link-num"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "link-num"):
                                                        self.link_num = value
                                                        self.link_num.value_namespace = name_space
                                                        self.link_num.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-stage"):
                                                        self.link_stage = value
                                                        self.link_stage.value_namespace = name_space
                                                        self.link_stage.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-type"):
                                                        self.link_type = value
                                                        self.link_type.value_namespace = name_space
                                                        self.link_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "phy-link-num"):
                                                        self.phy_link_num = value
                                                        self.phy_link_num.value_namespace = name_space
                                                        self.phy_link_num.value_namespace_prefix = name_space_prefix


                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of    :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist>`
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History, self).__init__()

                                                    self.yang_name = "history"
                                                    self.yang_parent_name = "rx-link"

                                                    self.histnum = YLeaf(YType.uint8, "histnum")

                                                    self.start_index = YLeaf(YType.uint8, "start-index")

                                                    self.hist = YList(self)

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("histnum",
                                                                    "start_index") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History, self).__setattr__(name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:   :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:   :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist, self).__init__()

                                                        self.yang_name = "hist"
                                                        self.yang_parent_name = "history"

                                                        self.admin_state = YLeaf(YType.enumeration, "admin-state")

                                                        self.error_state = YLeaf(YType.enumeration, "error-state")

                                                        self.oper_state = YLeaf(YType.enumeration, "oper-state")

                                                        self.reasons = YLeaf(YType.str, "reasons")

                                                        self.timestamp = YLeaf(YType.uint64, "timestamp")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("admin_state",
                                                                        "error_state",
                                                                        "oper_state",
                                                                        "reasons",
                                                                        "timestamp") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.admin_state.is_set or
                                                            self.error_state.is_set or
                                                            self.oper_state.is_set or
                                                            self.reasons.is_set or
                                                            self.timestamp.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.admin_state.yfilter != YFilter.not_set or
                                                            self.error_state.yfilter != YFilter.not_set or
                                                            self.oper_state.yfilter != YFilter.not_set or
                                                            self.reasons.yfilter != YFilter.not_set or
                                                            self.timestamp.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "hist" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.admin_state.get_name_leafdata())
                                                        if (self.error_state.is_set or self.error_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.error_state.get_name_leafdata())
                                                        if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.oper_state.get_name_leafdata())
                                                        if (self.reasons.is_set or self.reasons.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.reasons.get_name_leafdata())
                                                        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.timestamp.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "admin-state" or name == "error-state" or name == "oper-state" or name == "reasons" or name == "timestamp"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "admin-state"):
                                                            self.admin_state = value
                                                            self.admin_state.value_namespace = name_space
                                                            self.admin_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "error-state"):
                                                            self.error_state = value
                                                            self.error_state.value_namespace = name_space
                                                            self.error_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "oper-state"):
                                                            self.oper_state = value
                                                            self.oper_state.value_namespace = name_space
                                                            self.oper_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "reasons"):
                                                            self.reasons = value
                                                            self.reasons.value_namespace = name_space
                                                            self.reasons.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "timestamp"):
                                                            self.timestamp = value
                                                            self.timestamp.value_namespace = name_space
                                                            self.timestamp.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    for c in self.hist:
                                                        if (c.has_data()):
                                                            return True
                                                    return (
                                                        self.histnum.is_set or
                                                        self.start_index.is_set)

                                                def has_operation(self):
                                                    for c in self.hist:
                                                        if (c.has_operation()):
                                                            return True
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.histnum.yfilter != YFilter.not_set or
                                                        self.start_index.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "history" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.histnum.is_set or self.histnum.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.histnum.get_name_leafdata())
                                                    if (self.start_index.is_set or self.start_index.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.start_index.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "hist"):
                                                        for c in self.hist:
                                                            segment = c.get_segment_path()
                                                            if (segment_path == segment):
                                                                return c
                                                        c = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist()
                                                        c.parent = self
                                                        local_reference_key = "ydk::seg::%s" % segment_path
                                                        self._local_refs[local_reference_key] = c
                                                        self.hist.append(c)
                                                        return c

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "hist" or name == "histnum" or name == "start-index"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "histnum"):
                                                        self.histnum = value
                                                        self.histnum.value_namespace = name_space
                                                        self.histnum.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "start-index"):
                                                        self.start_index = value
                                                        self.start_index.value_namespace = name_space
                                                        self.start_index.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.link.is_set or
                                                    self.admin_state.is_set or
                                                    self.correctable_errors.is_set or
                                                    self.error_state.is_set or
                                                    self.flags.is_set or
                                                    self.flap_cnt.is_set or
                                                    self.is_conf_pending.is_set or
                                                    self.is_link_valid.is_set or
                                                    self.num_admin_shuts.is_set or
                                                    self.oper_state.is_set or
                                                    self.speed.is_set or
                                                    self.stage.is_set or
                                                    self.uncorrectable_errors.is_set or
                                                    (self.far_end_link is not None and self.far_end_link.has_data()) or
                                                    (self.far_end_link_in_hw is not None and self.far_end_link_in_hw.has_data()) or
                                                    (self.history is not None and self.history.has_data()) or
                                                    (self.this_link is not None and self.this_link.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.link.yfilter != YFilter.not_set or
                                                    self.admin_state.yfilter != YFilter.not_set or
                                                    self.correctable_errors.yfilter != YFilter.not_set or
                                                    self.error_state.yfilter != YFilter.not_set or
                                                    self.flags.yfilter != YFilter.not_set or
                                                    self.flap_cnt.yfilter != YFilter.not_set or
                                                    self.is_conf_pending.yfilter != YFilter.not_set or
                                                    self.is_link_valid.yfilter != YFilter.not_set or
                                                    self.num_admin_shuts.yfilter != YFilter.not_set or
                                                    self.oper_state.yfilter != YFilter.not_set or
                                                    self.speed.yfilter != YFilter.not_set or
                                                    self.stage.yfilter != YFilter.not_set or
                                                    self.uncorrectable_errors.yfilter != YFilter.not_set or
                                                    (self.far_end_link is not None and self.far_end_link.has_operation()) or
                                                    (self.far_end_link_in_hw is not None and self.far_end_link_in_hw.has_operation()) or
                                                    (self.history is not None and self.history.has_operation()) or
                                                    (self.this_link is not None and self.this_link.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "rx-link" + "[link='" + self.link.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.link.is_set or self.link.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.link.get_name_leafdata())
                                                if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.admin_state.get_name_leafdata())
                                                if (self.correctable_errors.is_set or self.correctable_errors.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.correctable_errors.get_name_leafdata())
                                                if (self.error_state.is_set or self.error_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.error_state.get_name_leafdata())
                                                if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.flags.get_name_leafdata())
                                                if (self.flap_cnt.is_set or self.flap_cnt.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.flap_cnt.get_name_leafdata())
                                                if (self.is_conf_pending.is_set or self.is_conf_pending.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_conf_pending.get_name_leafdata())
                                                if (self.is_link_valid.is_set or self.is_link_valid.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_link_valid.get_name_leafdata())
                                                if (self.num_admin_shuts.is_set or self.num_admin_shuts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.num_admin_shuts.get_name_leafdata())
                                                if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.oper_state.get_name_leafdata())
                                                if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.speed.get_name_leafdata())
                                                if (self.stage.is_set or self.stage.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.stage.get_name_leafdata())
                                                if (self.uncorrectable_errors.is_set or self.uncorrectable_errors.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.uncorrectable_errors.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "far-end-link"):
                                                    if (self.far_end_link is None):
                                                        self.far_end_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink()
                                                        self.far_end_link.parent = self
                                                        self._children_name_map["far_end_link"] = "far-end-link"
                                                    return self.far_end_link

                                                if (child_yang_name == "far-end-link-in-hw"):
                                                    if (self.far_end_link_in_hw is None):
                                                        self.far_end_link_in_hw = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw()
                                                        self.far_end_link_in_hw.parent = self
                                                        self._children_name_map["far_end_link_in_hw"] = "far-end-link-in-hw"
                                                    return self.far_end_link_in_hw

                                                if (child_yang_name == "history"):
                                                    if (self.history is None):
                                                        self.history = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History()
                                                        self.history.parent = self
                                                        self._children_name_map["history"] = "history"
                                                    return self.history

                                                if (child_yang_name == "this-link"):
                                                    if (self.this_link is None):
                                                        self.this_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink()
                                                        self.this_link.parent = self
                                                        self._children_name_map["this_link"] = "this-link"
                                                    return self.this_link

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "far-end-link" or name == "far-end-link-in-hw" or name == "history" or name == "this-link" or name == "link" or name == "admin-state" or name == "correctable-errors" or name == "error-state" or name == "flags" or name == "flap-cnt" or name == "is-conf-pending" or name == "is-link-valid" or name == "num-admin-shuts" or name == "oper-state" or name == "speed" or name == "stage" or name == "uncorrectable-errors"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "link"):
                                                    self.link = value
                                                    self.link.value_namespace = name_space
                                                    self.link.value_namespace_prefix = name_space_prefix
                                                if(value_path == "admin-state"):
                                                    self.admin_state = value
                                                    self.admin_state.value_namespace = name_space
                                                    self.admin_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "correctable-errors"):
                                                    self.correctable_errors = value
                                                    self.correctable_errors.value_namespace = name_space
                                                    self.correctable_errors.value_namespace_prefix = name_space_prefix
                                                if(value_path == "error-state"):
                                                    self.error_state = value
                                                    self.error_state.value_namespace = name_space
                                                    self.error_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "flags"):
                                                    self.flags = value
                                                    self.flags.value_namespace = name_space
                                                    self.flags.value_namespace_prefix = name_space_prefix
                                                if(value_path == "flap-cnt"):
                                                    self.flap_cnt = value
                                                    self.flap_cnt.value_namespace = name_space
                                                    self.flap_cnt.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-conf-pending"):
                                                    self.is_conf_pending = value
                                                    self.is_conf_pending.value_namespace = name_space
                                                    self.is_conf_pending.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-link-valid"):
                                                    self.is_link_valid = value
                                                    self.is_link_valid.value_namespace = name_space
                                                    self.is_link_valid.value_namespace_prefix = name_space_prefix
                                                if(value_path == "num-admin-shuts"):
                                                    self.num_admin_shuts = value
                                                    self.num_admin_shuts.value_namespace = name_space
                                                    self.num_admin_shuts.value_namespace_prefix = name_space_prefix
                                                if(value_path == "oper-state"):
                                                    self.oper_state = value
                                                    self.oper_state.value_namespace = name_space
                                                    self.oper_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "speed"):
                                                    self.speed = value
                                                    self.speed.value_namespace = name_space
                                                    self.speed.value_namespace_prefix = name_space_prefix
                                                if(value_path == "stage"):
                                                    self.stage = value
                                                    self.stage.value_namespace = name_space
                                                    self.stage.value_namespace_prefix = name_space_prefix
                                                if(value_path == "uncorrectable-errors"):
                                                    self.uncorrectable_errors = value
                                                    self.uncorrectable_errors.value_namespace = name_space
                                                    self.uncorrectable_errors.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.rx_link:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.end_number.is_set or
                                                self.start_number.is_set or
                                                self.status_option.is_set)

                                        def has_operation(self):
                                            for c in self.rx_link:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.end_number.yfilter != YFilter.not_set or
                                                self.start_number.yfilter != YFilter.not_set or
                                                self.status_option.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "rx-link" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.end_number.is_set or self.end_number.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.end_number.get_name_leafdata())
                                            if (self.start_number.is_set or self.start_number.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.start_number.get_name_leafdata())
                                            if (self.status_option.is_set or self.status_option.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.status_option.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "rx-link"):
                                                for c in self.rx_link:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.rx_link.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "rx-link" or name == "end-number" or name == "start-number" or name == "status-option"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "end-number"):
                                                self.end_number = value
                                                self.end_number.value_namespace = name_space
                                                self.end_number.value_namespace_prefix = name_space_prefix
                                            if(value_path == "start-number"):
                                                self.start_number = value
                                                self.start_number.value_namespace = name_space
                                                self.start_number.value_namespace_prefix = name_space_prefix
                                            if(value_path == "status-option"):
                                                self.status_option = value
                                                self.status_option.value_namespace = name_space
                                                self.status_option.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.rx_link:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.rx_link:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rx-links" + path_buffer

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

                                        if (child_yang_name == "rx-link"):
                                            for c in self.rx_link:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.rx_link.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "rx-link"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.instance.is_set or
                                        (self.rx_links is not None and self.rx_links.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.instance.yfilter != YFilter.not_set or
                                        (self.rx_links is not None and self.rx_links.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "rx-asic-instance" + "[instance='" + self.instance.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.instance.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "rx-links"):
                                        if (self.rx_links is None):
                                            self.rx_links = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks()
                                            self.rx_links.parent = self
                                            self._children_name_map["rx_links"] = "rx-links"
                                        return self.rx_links

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "rx-links" or name == "instance"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "instance"):
                                        self.instance = value
                                        self.instance.value_namespace = name_space
                                        self.instance.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.rx_asic_instance:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.rx_asic_instance:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "rx-asic-instances" + path_buffer

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

                                if (child_yang_name == "rx-asic-instance"):
                                    for c in self.rx_asic_instance:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.rx_asic_instance.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "rx-asic-instance"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.option.is_set or
                                (self.rx_asic_instances is not None and self.rx_asic_instances.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.option.yfilter != YFilter.not_set or
                                (self.rx_asic_instances is not None and self.rx_asic_instances.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "link-option" + "[option='" + self.option.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.option.is_set or self.option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.option.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "rx-asic-instances"):
                                if (self.rx_asic_instances is None):
                                    self.rx_asic_instances = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances()
                                    self.rx_asic_instances.parent = self
                                    self._children_name_map["rx_asic_instances"] = "rx-asic-instances"
                                return self.rx_asic_instances

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "rx-asic-instances" or name == "option"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "option"):
                                self.option = value
                                self.option.value_namespace = name_space
                                self.option.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.link_option:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.link_option:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "link-options" + path_buffer

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

                        if (child_yang_name == "link-option"):
                            for c in self.link_option:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.link_option.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "link-option"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.link_options is not None and self.link_options.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.link_options is not None and self.link_options.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rx-link-information" + path_buffer

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

                    if (child_yang_name == "link-options"):
                        if (self.link_options is None):
                            self.link_options = Fia.Nodes.Node.RxLinkInformation.LinkOptions()
                            self.link_options.parent = self
                            self._children_name_map["link_options"] = "link-options"
                        return self.link_options

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "link-options"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DriverInformation(Entity):
                """
                FIA driver information
                
                .. attribute:: asic_avail_mask
                
                	asic avail mask
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                
                	asic oper notify to fsdb pending bmap
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: board_rev_id
                
                	board rev id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: card_avail_mask
                
                	card avail mask
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: card_info
                
                	card info
                	**type**\: list of    :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo>`
                
                .. attribute:: coeff_major_rev
                
                	coeff major rev
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: coeff_minor_rev
                
                	coeff minor rev
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_info
                
                	device info
                	**type**\: list of    :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo>`
                
                .. attribute:: drv_version
                
                	drv version
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: drvr_current_startup_timestamp
                
                	drvr current startup timestamp
                	**type**\:  str
                
                .. attribute:: drvr_initial_startup_timestamp
                
                	drvr initial startup timestamp
                	**type**\:  str
                
                .. attribute:: exp_asic_avail_mask
                
                	exp asic avail mask
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: fabric_mode
                
                	fabric mode
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: fc_mode
                
                	FC Mode
                	**type**\:   :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                
                .. attribute:: fgid_conn_active
                
                	fgid conn active
                	**type**\:  bool
                
                .. attribute:: fgid_reg_active
                
                	fgid reg active
                	**type**\:  bool
                
                .. attribute:: fsdb_conn_active
                
                	fsdb conn active
                	**type**\:  bool
                
                .. attribute:: fsdb_reg_active
                
                	fsdb reg active
                	**type**\:  bool
                
                .. attribute:: functional_role
                
                	functional role
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: is_cih_registered
                
                	is cih registered
                	**type**\:  bool
                
                .. attribute:: is_driver_ready
                
                	is driver ready
                	**type**\:  bool
                
                .. attribute:: is_fgid_download_completed
                
                	is fgid download completed
                	**type**\:  bool
                
                .. attribute:: is_fgid_download_in_progress
                
                	is fgid download in progress
                	**type**\:  bool
                
                .. attribute:: is_full_fgid_download_req
                
                	is full fgid download req
                	**type**\:  bool
                
                .. attribute:: is_gaspp_registered
                
                	is gaspp registered
                	**type**\:  bool
                
                .. attribute:: issu_abort_rcvd
                
                	issu abort rcvd
                	**type**\:  bool
                
                .. attribute:: issu_abort_sent
                
                	issu abort sent
                	**type**\:  bool
                
                .. attribute:: issu_mgr_conn_active
                
                	issu mgr conn active
                	**type**\:  bool
                
                .. attribute:: issu_mgr_reg_active
                
                	issu mgr reg active
                	**type**\:  bool
                
                .. attribute:: issu_ready_ntfy_pending
                
                	issu ready ntfy pending
                	**type**\:  bool
                
                .. attribute:: issu_role
                
                	issu role
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: node_id
                
                	node id
                	**type**\:  str
                
                .. attribute:: num_cm_conn_reqs
                
                	num cm conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_fgid_conn_reqs
                
                	num fgid conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_fsdb_conn_reqs
                
                	num fsdb conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_fstats_conn_reqs
                
                	num fstats conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_intf_ports
                
                	num intf ports
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_issu_mgr_conn_reqs
                
                	num issu mgr conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_peer_fia_conn_reqs
                
                	num peer fia conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_pm_conn_reqs
                
                	num pm conn reqs
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: rack_num
                
                	rack num
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: rack_type
                
                	rack type
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: respawn_count
                
                	respawn count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: total_asics
                
                	total asics
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: uc_weight
                
                	uc weight
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: ucmc_ratio
                
                	ucmc ratio
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.DriverInformation, self).__init__()

                    self.yang_name = "driver-information"
                    self.yang_parent_name = "node"

                    self.asic_avail_mask = YLeaf(YType.uint64, "asic-avail-mask")

                    self.asic_oper_notify_to_fsdb_pending_bmap = YLeaf(YType.uint64, "asic-oper-notify-to-fsdb-pending-bmap")

                    self.board_rev_id = YLeaf(YType.uint32, "board-rev-id")

                    self.card_avail_mask = YLeaf(YType.uint32, "card-avail-mask")

                    self.coeff_major_rev = YLeaf(YType.uint32, "coeff-major-rev")

                    self.coeff_minor_rev = YLeaf(YType.uint32, "coeff-minor-rev")

                    self.drv_version = YLeaf(YType.uint32, "drv-version")

                    self.drvr_current_startup_timestamp = YLeaf(YType.str, "drvr-current-startup-timestamp")

                    self.drvr_initial_startup_timestamp = YLeaf(YType.str, "drvr-initial-startup-timestamp")

                    self.exp_asic_avail_mask = YLeaf(YType.uint64, "exp-asic-avail-mask")

                    self.fabric_mode = YLeaf(YType.uint8, "fabric-mode")

                    self.fc_mode = YLeaf(YType.enumeration, "fc-mode")

                    self.fgid_conn_active = YLeaf(YType.boolean, "fgid-conn-active")

                    self.fgid_reg_active = YLeaf(YType.boolean, "fgid-reg-active")

                    self.fsdb_conn_active = YLeaf(YType.boolean, "fsdb-conn-active")

                    self.fsdb_reg_active = YLeaf(YType.boolean, "fsdb-reg-active")

                    self.functional_role = YLeaf(YType.uint8, "functional-role")

                    self.is_cih_registered = YLeaf(YType.boolean, "is-cih-registered")

                    self.is_driver_ready = YLeaf(YType.boolean, "is-driver-ready")

                    self.is_fgid_download_completed = YLeaf(YType.boolean, "is-fgid-download-completed")

                    self.is_fgid_download_in_progress = YLeaf(YType.boolean, "is-fgid-download-in-progress")

                    self.is_full_fgid_download_req = YLeaf(YType.boolean, "is-full-fgid-download-req")

                    self.is_gaspp_registered = YLeaf(YType.boolean, "is-gaspp-registered")

                    self.issu_abort_rcvd = YLeaf(YType.boolean, "issu-abort-rcvd")

                    self.issu_abort_sent = YLeaf(YType.boolean, "issu-abort-sent")

                    self.issu_mgr_conn_active = YLeaf(YType.boolean, "issu-mgr-conn-active")

                    self.issu_mgr_reg_active = YLeaf(YType.boolean, "issu-mgr-reg-active")

                    self.issu_ready_ntfy_pending = YLeaf(YType.boolean, "issu-ready-ntfy-pending")

                    self.issu_role = YLeaf(YType.uint8, "issu-role")

                    self.node_id = YLeaf(YType.str, "node-id")

                    self.num_cm_conn_reqs = YLeaf(YType.uint8, "num-cm-conn-reqs")

                    self.num_fgid_conn_reqs = YLeaf(YType.uint8, "num-fgid-conn-reqs")

                    self.num_fsdb_conn_reqs = YLeaf(YType.uint8, "num-fsdb-conn-reqs")

                    self.num_fstats_conn_reqs = YLeaf(YType.uint8, "num-fstats-conn-reqs")

                    self.num_intf_ports = YLeaf(YType.uint32, "num-intf-ports")

                    self.num_issu_mgr_conn_reqs = YLeaf(YType.uint8, "num-issu-mgr-conn-reqs")

                    self.num_peer_fia_conn_reqs = YLeaf(YType.uint8, "num-peer-fia-conn-reqs")

                    self.num_pm_conn_reqs = YLeaf(YType.uint8, "num-pm-conn-reqs")

                    self.rack_num = YLeaf(YType.uint8, "rack-num")

                    self.rack_type = YLeaf(YType.int32, "rack-type")

                    self.respawn_count = YLeaf(YType.uint8, "respawn-count")

                    self.total_asics = YLeaf(YType.uint8, "total-asics")

                    self.uc_weight = YLeaf(YType.uint8, "uc-weight")

                    self.ucmc_ratio = YLeaf(YType.uint32, "ucmc-ratio")

                    self.card_info = YList(self)
                    self.device_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("asic_avail_mask",
                                    "asic_oper_notify_to_fsdb_pending_bmap",
                                    "board_rev_id",
                                    "card_avail_mask",
                                    "coeff_major_rev",
                                    "coeff_minor_rev",
                                    "drv_version",
                                    "drvr_current_startup_timestamp",
                                    "drvr_initial_startup_timestamp",
                                    "exp_asic_avail_mask",
                                    "fabric_mode",
                                    "fc_mode",
                                    "fgid_conn_active",
                                    "fgid_reg_active",
                                    "fsdb_conn_active",
                                    "fsdb_reg_active",
                                    "functional_role",
                                    "is_cih_registered",
                                    "is_driver_ready",
                                    "is_fgid_download_completed",
                                    "is_fgid_download_in_progress",
                                    "is_full_fgid_download_req",
                                    "is_gaspp_registered",
                                    "issu_abort_rcvd",
                                    "issu_abort_sent",
                                    "issu_mgr_conn_active",
                                    "issu_mgr_reg_active",
                                    "issu_ready_ntfy_pending",
                                    "issu_role",
                                    "node_id",
                                    "num_cm_conn_reqs",
                                    "num_fgid_conn_reqs",
                                    "num_fsdb_conn_reqs",
                                    "num_fstats_conn_reqs",
                                    "num_intf_ports",
                                    "num_issu_mgr_conn_reqs",
                                    "num_peer_fia_conn_reqs",
                                    "num_pm_conn_reqs",
                                    "rack_num",
                                    "rack_type",
                                    "respawn_count",
                                    "total_asics",
                                    "uc_weight",
                                    "ucmc_ratio") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Fia.Nodes.Node.DriverInformation, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Fia.Nodes.Node.DriverInformation, self).__setattr__(name, value)


                class DeviceInfo(Entity):
                    """
                    device info
                    
                    .. attribute:: admin_state
                    
                    	Admin State
                    	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                    
                    .. attribute:: asic_id
                    
                    	asic id
                    	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId>`
                    
                    .. attribute:: asic_state
                    
                    	Asic State
                    	**type**\:   :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                    
                    .. attribute:: fapid
                    
                    	fapid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hotplug_event
                    
                    	hotplug event
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_valid
                    
                    	is valid
                    	**type**\:  bool
                    
                    .. attribute:: last_init_cause
                    
                    	last init cause
                    	**type**\:   :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                    
                    .. attribute:: local_switch_state
                    
                    	local switch state
                    	**type**\:  bool
                    
                    .. attribute:: num_hard_resets
                    
                    	num hard resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_pon_resets
                    
                    	num pon resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oper_state
                    
                    	Oper State
                    	**type**\:   :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                    
                    .. attribute:: slice_state
                    
                    	Slice State
                    	**type**\:   :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.DriverInformation.DeviceInfo, self).__init__()

                        self.yang_name = "device-info"
                        self.yang_parent_name = "driver-information"

                        self.admin_state = YLeaf(YType.enumeration, "admin-state")

                        self.asic_state = YLeaf(YType.enumeration, "asic-state")

                        self.fapid = YLeaf(YType.uint32, "fapid")

                        self.hotplug_event = YLeaf(YType.uint32, "hotplug-event")

                        self.is_valid = YLeaf(YType.boolean, "is-valid")

                        self.last_init_cause = YLeaf(YType.enumeration, "last-init-cause")

                        self.local_switch_state = YLeaf(YType.boolean, "local-switch-state")

                        self.num_hard_resets = YLeaf(YType.uint32, "num-hard-resets")

                        self.num_pon_resets = YLeaf(YType.uint32, "num-pon-resets")

                        self.oper_state = YLeaf(YType.enumeration, "oper-state")

                        self.slice_state = YLeaf(YType.enumeration, "slice-state")

                        self.asic_id = Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId()
                        self.asic_id.parent = self
                        self._children_name_map["asic_id"] = "asic-id"
                        self._children_yang_names.add("asic-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("admin_state",
                                        "asic_state",
                                        "fapid",
                                        "hotplug_event",
                                        "is_valid",
                                        "last_init_cause",
                                        "local_switch_state",
                                        "num_hard_resets",
                                        "num_pon_resets",
                                        "oper_state",
                                        "slice_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Fia.Nodes.Node.DriverInformation.DeviceInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.DriverInformation.DeviceInfo, self).__setattr__(name, value)


                    class AsicId(Entity):
                        """
                        asic id
                        
                        .. attribute:: asic_instance
                        
                        	asic instance
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: asic_type
                        
                        	Asic Type
                        	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                        
                        .. attribute:: rack_num
                        
                        	rack num
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rack_type
                        
                        	Rack Type
                        	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                        
                        .. attribute:: slot_num
                        
                        	slot num
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, self).__init__()

                            self.yang_name = "asic-id"
                            self.yang_parent_name = "device-info"

                            self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                            self.asic_type = YLeaf(YType.enumeration, "asic-type")

                            self.rack_num = YLeaf(YType.uint32, "rack-num")

                            self.rack_type = YLeaf(YType.enumeration, "rack-type")

                            self.slot_num = YLeaf(YType.uint32, "slot-num")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("asic_instance",
                                            "asic_type",
                                            "rack_num",
                                            "rack_type",
                                            "slot_num") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.asic_instance.is_set or
                                self.asic_type.is_set or
                                self.rack_num.is_set or
                                self.rack_type.is_set or
                                self.slot_num.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.asic_instance.yfilter != YFilter.not_set or
                                self.asic_type.yfilter != YFilter.not_set or
                                self.rack_num.yfilter != YFilter.not_set or
                                self.rack_type.yfilter != YFilter.not_set or
                                self.slot_num.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "asic-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asic_instance.get_name_leafdata())
                            if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asic_type.get_name_leafdata())
                            if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rack_num.get_name_leafdata())
                            if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rack_type.get_name_leafdata())
                            if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.slot_num.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "asic-instance"):
                                self.asic_instance = value
                                self.asic_instance.value_namespace = name_space
                                self.asic_instance.value_namespace_prefix = name_space_prefix
                            if(value_path == "asic-type"):
                                self.asic_type = value
                                self.asic_type.value_namespace = name_space
                                self.asic_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "rack-num"):
                                self.rack_num = value
                                self.rack_num.value_namespace = name_space
                                self.rack_num.value_namespace_prefix = name_space_prefix
                            if(value_path == "rack-type"):
                                self.rack_type = value
                                self.rack_type.value_namespace = name_space
                                self.rack_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "slot-num"):
                                self.slot_num = value
                                self.slot_num.value_namespace = name_space
                                self.slot_num.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.admin_state.is_set or
                            self.asic_state.is_set or
                            self.fapid.is_set or
                            self.hotplug_event.is_set or
                            self.is_valid.is_set or
                            self.last_init_cause.is_set or
                            self.local_switch_state.is_set or
                            self.num_hard_resets.is_set or
                            self.num_pon_resets.is_set or
                            self.oper_state.is_set or
                            self.slice_state.is_set or
                            (self.asic_id is not None and self.asic_id.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.admin_state.yfilter != YFilter.not_set or
                            self.asic_state.yfilter != YFilter.not_set or
                            self.fapid.yfilter != YFilter.not_set or
                            self.hotplug_event.yfilter != YFilter.not_set or
                            self.is_valid.yfilter != YFilter.not_set or
                            self.last_init_cause.yfilter != YFilter.not_set or
                            self.local_switch_state.yfilter != YFilter.not_set or
                            self.num_hard_resets.yfilter != YFilter.not_set or
                            self.num_pon_resets.yfilter != YFilter.not_set or
                            self.oper_state.yfilter != YFilter.not_set or
                            self.slice_state.yfilter != YFilter.not_set or
                            (self.asic_id is not None and self.asic_id.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "device-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.admin_state.get_name_leafdata())
                        if (self.asic_state.is_set or self.asic_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.asic_state.get_name_leafdata())
                        if (self.fapid.is_set or self.fapid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fapid.get_name_leafdata())
                        if (self.hotplug_event.is_set or self.hotplug_event.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hotplug_event.get_name_leafdata())
                        if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_valid.get_name_leafdata())
                        if (self.last_init_cause.is_set or self.last_init_cause.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_init_cause.get_name_leafdata())
                        if (self.local_switch_state.is_set or self.local_switch_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_switch_state.get_name_leafdata())
                        if (self.num_hard_resets.is_set or self.num_hard_resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_hard_resets.get_name_leafdata())
                        if (self.num_pon_resets.is_set or self.num_pon_resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_pon_resets.get_name_leafdata())
                        if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oper_state.get_name_leafdata())
                        if (self.slice_state.is_set or self.slice_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slice_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "asic-id"):
                            if (self.asic_id is None):
                                self.asic_id = Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId()
                                self.asic_id.parent = self
                                self._children_name_map["asic_id"] = "asic-id"
                            return self.asic_id

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "asic-id" or name == "admin-state" or name == "asic-state" or name == "fapid" or name == "hotplug-event" or name == "is-valid" or name == "last-init-cause" or name == "local-switch-state" or name == "num-hard-resets" or name == "num-pon-resets" or name == "oper-state" or name == "slice-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "admin-state"):
                            self.admin_state = value
                            self.admin_state.value_namespace = name_space
                            self.admin_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "asic-state"):
                            self.asic_state = value
                            self.asic_state.value_namespace = name_space
                            self.asic_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "fapid"):
                            self.fapid = value
                            self.fapid.value_namespace = name_space
                            self.fapid.value_namespace_prefix = name_space_prefix
                        if(value_path == "hotplug-event"):
                            self.hotplug_event = value
                            self.hotplug_event.value_namespace = name_space
                            self.hotplug_event.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-valid"):
                            self.is_valid = value
                            self.is_valid.value_namespace = name_space
                            self.is_valid.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-init-cause"):
                            self.last_init_cause = value
                            self.last_init_cause.value_namespace = name_space
                            self.last_init_cause.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-switch-state"):
                            self.local_switch_state = value
                            self.local_switch_state.value_namespace = name_space
                            self.local_switch_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "num-hard-resets"):
                            self.num_hard_resets = value
                            self.num_hard_resets.value_namespace = name_space
                            self.num_hard_resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "num-pon-resets"):
                            self.num_pon_resets = value
                            self.num_pon_resets.value_namespace = name_space
                            self.num_pon_resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "oper-state"):
                            self.oper_state = value
                            self.oper_state.value_namespace = name_space
                            self.oper_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "slice-state"):
                            self.slice_state = value
                            self.slice_state.value_namespace = name_space
                            self.slice_state.value_namespace_prefix = name_space_prefix


                class CardInfo(Entity):
                    """
                    card info
                    
                    .. attribute:: card_flag
                    
                    	card flag
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_name
                    
                    	card name
                    	**type**\:  str
                    
                    .. attribute:: card_state
                    
                    	card state
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: cxp_avail_bitmap
                    
                    	cxp avail bitmap
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: evt_flag
                    
                    	evt flag
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: exp_num_asics
                    
                    	exp num asics
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: exp_num_asics_per_fsdb
                    
                    	exp num asics per fsdb
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: instance
                    
                    	instance
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_powered
                    
                    	is powered
                    	**type**\:  bool
                    
                    .. attribute:: num_cos_per_port
                    
                    	num cos per port
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: num_ilkns_per_asic
                    
                    	num ilkns per asic
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_local_ports_per_ilkn
                    
                    	num local ports per ilkn
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oir_circular_buffer
                    
                    	oir circular buffer
                    	**type**\:   :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer>`
                    
                    .. attribute:: reg_flag
                    
                    	reg flag
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: slot_no
                    
                    	slot no
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.DriverInformation.CardInfo, self).__init__()

                        self.yang_name = "card-info"
                        self.yang_parent_name = "driver-information"

                        self.card_flag = YLeaf(YType.int32, "card-flag")

                        self.card_name = YLeaf(YType.str, "card-name")

                        self.card_state = YLeaf(YType.uint8, "card-state")

                        self.card_type = YLeaf(YType.int32, "card-type")

                        self.cxp_avail_bitmap = YLeaf(YType.uint64, "cxp-avail-bitmap")

                        self.evt_flag = YLeaf(YType.int32, "evt-flag")

                        self.exp_num_asics = YLeaf(YType.uint32, "exp-num-asics")

                        self.exp_num_asics_per_fsdb = YLeaf(YType.uint32, "exp-num-asics-per-fsdb")

                        self.instance = YLeaf(YType.int32, "instance")

                        self.is_powered = YLeaf(YType.boolean, "is-powered")

                        self.num_cos_per_port = YLeaf(YType.uint8, "num-cos-per-port")

                        self.num_ilkns_per_asic = YLeaf(YType.uint32, "num-ilkns-per-asic")

                        self.num_local_ports_per_ilkn = YLeaf(YType.uint32, "num-local-ports-per-ilkn")

                        self.reg_flag = YLeaf(YType.int32, "reg-flag")

                        self.slot_no = YLeaf(YType.int32, "slot-no")

                        self.oir_circular_buffer = Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer()
                        self.oir_circular_buffer.parent = self
                        self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                        self._children_yang_names.add("oir-circular-buffer")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("card_flag",
                                        "card_name",
                                        "card_state",
                                        "card_type",
                                        "cxp_avail_bitmap",
                                        "evt_flag",
                                        "exp_num_asics",
                                        "exp_num_asics_per_fsdb",
                                        "instance",
                                        "is_powered",
                                        "num_cos_per_port",
                                        "num_ilkns_per_asic",
                                        "num_local_ports_per_ilkn",
                                        "reg_flag",
                                        "slot_no") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Fia.Nodes.Node.DriverInformation.CardInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.DriverInformation.CardInfo, self).__setattr__(name, value)


                    class OirCircularBuffer(Entity):
                        """
                        oir circular buffer
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: fia_oir_info
                        
                        	fia oir info
                        	**type**\: list of    :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo>`
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, self).__init__()

                            self.yang_name = "oir-circular-buffer"
                            self.yang_parent_name = "card-info"

                            self.count = YLeaf(YType.int32, "count")

                            self.end = YLeaf(YType.int32, "end")

                            self.start = YLeaf(YType.int32, "start")

                            self.fia_oir_info = YList(self)

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
                                            "end",
                                            "start") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer, self).__setattr__(name, value)


                        class FiaOirInfo(Entity):
                            """
                            fia oir info
                            
                            .. attribute:: card_flag
                            
                            	card flag
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_type
                            
                            	card type
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: cur_card_state
                            
                            	cur card state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evt_flag
                            
                            	evt flag
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: instance
                            
                            	instance
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: reg_flag
                            
                            	reg flag
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, self).__init__()

                                self.yang_name = "fia-oir-info"
                                self.yang_parent_name = "oir-circular-buffer"

                                self.card_flag = YLeaf(YType.int32, "card-flag")

                                self.card_type = YLeaf(YType.int32, "card-type")

                                self.cur_card_state = YLeaf(YType.int32, "cur-card-state")

                                self.evt_flag = YLeaf(YType.int32, "evt-flag")

                                self.instance = YLeaf(YType.int32, "instance")

                                self.rack_num = YLeaf(YType.int32, "rack-num")

                                self.reg_flag = YLeaf(YType.int32, "reg-flag")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("card_flag",
                                                "card_type",
                                                "cur_card_state",
                                                "evt_flag",
                                                "instance",
                                                "rack_num",
                                                "reg_flag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.card_flag.is_set or
                                    self.card_type.is_set or
                                    self.cur_card_state.is_set or
                                    self.evt_flag.is_set or
                                    self.instance.is_set or
                                    self.rack_num.is_set or
                                    self.reg_flag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.card_flag.yfilter != YFilter.not_set or
                                    self.card_type.yfilter != YFilter.not_set or
                                    self.cur_card_state.yfilter != YFilter.not_set or
                                    self.evt_flag.yfilter != YFilter.not_set or
                                    self.instance.yfilter != YFilter.not_set or
                                    self.rack_num.yfilter != YFilter.not_set or
                                    self.reg_flag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fia-oir-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.card_flag.is_set or self.card_flag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.card_flag.get_name_leafdata())
                                if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.card_type.get_name_leafdata())
                                if (self.cur_card_state.is_set or self.cur_card_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cur_card_state.get_name_leafdata())
                                if (self.evt_flag.is_set or self.evt_flag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.evt_flag.get_name_leafdata())
                                if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.instance.get_name_leafdata())
                                if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rack_num.get_name_leafdata())
                                if (self.reg_flag.is_set or self.reg_flag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reg_flag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "card-flag" or name == "card-type" or name == "cur-card-state" or name == "evt-flag" or name == "instance" or name == "rack-num" or name == "reg-flag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "card-flag"):
                                    self.card_flag = value
                                    self.card_flag.value_namespace = name_space
                                    self.card_flag.value_namespace_prefix = name_space_prefix
                                if(value_path == "card-type"):
                                    self.card_type = value
                                    self.card_type.value_namespace = name_space
                                    self.card_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "cur-card-state"):
                                    self.cur_card_state = value
                                    self.cur_card_state.value_namespace = name_space
                                    self.cur_card_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "evt-flag"):
                                    self.evt_flag = value
                                    self.evt_flag.value_namespace = name_space
                                    self.evt_flag.value_namespace_prefix = name_space_prefix
                                if(value_path == "instance"):
                                    self.instance = value
                                    self.instance.value_namespace = name_space
                                    self.instance.value_namespace_prefix = name_space_prefix
                                if(value_path == "rack-num"):
                                    self.rack_num = value
                                    self.rack_num.value_namespace = name_space
                                    self.rack_num.value_namespace_prefix = name_space_prefix
                                if(value_path == "reg-flag"):
                                    self.reg_flag = value
                                    self.reg_flag.value_namespace = name_space
                                    self.reg_flag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.fia_oir_info:
                                if (c.has_data()):
                                    return True
                            return (
                                self.count.is_set or
                                self.end.is_set or
                                self.start.is_set)

                        def has_operation(self):
                            for c in self.fia_oir_info:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.count.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oir-circular-buffer" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.count.get_name_leafdata())
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "fia-oir-info"):
                                for c in self.fia_oir_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.fia_oir_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fia-oir-info" or name == "count" or name == "end" or name == "start"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "count"):
                                self.count = value
                                self.count.value_namespace = name_space
                                self.count.value_namespace_prefix = name_space_prefix
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.card_flag.is_set or
                            self.card_name.is_set or
                            self.card_state.is_set or
                            self.card_type.is_set or
                            self.cxp_avail_bitmap.is_set or
                            self.evt_flag.is_set or
                            self.exp_num_asics.is_set or
                            self.exp_num_asics_per_fsdb.is_set or
                            self.instance.is_set or
                            self.is_powered.is_set or
                            self.num_cos_per_port.is_set or
                            self.num_ilkns_per_asic.is_set or
                            self.num_local_ports_per_ilkn.is_set or
                            self.reg_flag.is_set or
                            self.slot_no.is_set or
                            (self.oir_circular_buffer is not None and self.oir_circular_buffer.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.card_flag.yfilter != YFilter.not_set or
                            self.card_name.yfilter != YFilter.not_set or
                            self.card_state.yfilter != YFilter.not_set or
                            self.card_type.yfilter != YFilter.not_set or
                            self.cxp_avail_bitmap.yfilter != YFilter.not_set or
                            self.evt_flag.yfilter != YFilter.not_set or
                            self.exp_num_asics.yfilter != YFilter.not_set or
                            self.exp_num_asics_per_fsdb.yfilter != YFilter.not_set or
                            self.instance.yfilter != YFilter.not_set or
                            self.is_powered.yfilter != YFilter.not_set or
                            self.num_cos_per_port.yfilter != YFilter.not_set or
                            self.num_ilkns_per_asic.yfilter != YFilter.not_set or
                            self.num_local_ports_per_ilkn.yfilter != YFilter.not_set or
                            self.reg_flag.yfilter != YFilter.not_set or
                            self.slot_no.yfilter != YFilter.not_set or
                            (self.oir_circular_buffer is not None and self.oir_circular_buffer.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "card-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.card_flag.is_set or self.card_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_flag.get_name_leafdata())
                        if (self.card_name.is_set or self.card_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_name.get_name_leafdata())
                        if (self.card_state.is_set or self.card_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_state.get_name_leafdata())
                        if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_type.get_name_leafdata())
                        if (self.cxp_avail_bitmap.is_set or self.cxp_avail_bitmap.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cxp_avail_bitmap.get_name_leafdata())
                        if (self.evt_flag.is_set or self.evt_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.evt_flag.get_name_leafdata())
                        if (self.exp_num_asics.is_set or self.exp_num_asics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_num_asics.get_name_leafdata())
                        if (self.exp_num_asics_per_fsdb.is_set or self.exp_num_asics_per_fsdb.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_num_asics_per_fsdb.get_name_leafdata())
                        if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance.get_name_leafdata())
                        if (self.is_powered.is_set or self.is_powered.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_powered.get_name_leafdata())
                        if (self.num_cos_per_port.is_set or self.num_cos_per_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_cos_per_port.get_name_leafdata())
                        if (self.num_ilkns_per_asic.is_set or self.num_ilkns_per_asic.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_ilkns_per_asic.get_name_leafdata())
                        if (self.num_local_ports_per_ilkn.is_set or self.num_local_ports_per_ilkn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_local_ports_per_ilkn.get_name_leafdata())
                        if (self.reg_flag.is_set or self.reg_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reg_flag.get_name_leafdata())
                        if (self.slot_no.is_set or self.slot_no.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot_no.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "oir-circular-buffer"):
                            if (self.oir_circular_buffer is None):
                                self.oir_circular_buffer = Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer()
                                self.oir_circular_buffer.parent = self
                                self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                            return self.oir_circular_buffer

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "oir-circular-buffer" or name == "card-flag" or name == "card-name" or name == "card-state" or name == "card-type" or name == "cxp-avail-bitmap" or name == "evt-flag" or name == "exp-num-asics" or name == "exp-num-asics-per-fsdb" or name == "instance" or name == "is-powered" or name == "num-cos-per-port" or name == "num-ilkns-per-asic" or name == "num-local-ports-per-ilkn" or name == "reg-flag" or name == "slot-no"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "card-flag"):
                            self.card_flag = value
                            self.card_flag.value_namespace = name_space
                            self.card_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "card-name"):
                            self.card_name = value
                            self.card_name.value_namespace = name_space
                            self.card_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "card-state"):
                            self.card_state = value
                            self.card_state.value_namespace = name_space
                            self.card_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "card-type"):
                            self.card_type = value
                            self.card_type.value_namespace = name_space
                            self.card_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "cxp-avail-bitmap"):
                            self.cxp_avail_bitmap = value
                            self.cxp_avail_bitmap.value_namespace = name_space
                            self.cxp_avail_bitmap.value_namespace_prefix = name_space_prefix
                        if(value_path == "evt-flag"):
                            self.evt_flag = value
                            self.evt_flag.value_namespace = name_space
                            self.evt_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "exp-num-asics"):
                            self.exp_num_asics = value
                            self.exp_num_asics.value_namespace = name_space
                            self.exp_num_asics.value_namespace_prefix = name_space_prefix
                        if(value_path == "exp-num-asics-per-fsdb"):
                            self.exp_num_asics_per_fsdb = value
                            self.exp_num_asics_per_fsdb.value_namespace = name_space
                            self.exp_num_asics_per_fsdb.value_namespace_prefix = name_space_prefix
                        if(value_path == "instance"):
                            self.instance = value
                            self.instance.value_namespace = name_space
                            self.instance.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-powered"):
                            self.is_powered = value
                            self.is_powered.value_namespace = name_space
                            self.is_powered.value_namespace_prefix = name_space_prefix
                        if(value_path == "num-cos-per-port"):
                            self.num_cos_per_port = value
                            self.num_cos_per_port.value_namespace = name_space
                            self.num_cos_per_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "num-ilkns-per-asic"):
                            self.num_ilkns_per_asic = value
                            self.num_ilkns_per_asic.value_namespace = name_space
                            self.num_ilkns_per_asic.value_namespace_prefix = name_space_prefix
                        if(value_path == "num-local-ports-per-ilkn"):
                            self.num_local_ports_per_ilkn = value
                            self.num_local_ports_per_ilkn.value_namespace = name_space
                            self.num_local_ports_per_ilkn.value_namespace_prefix = name_space_prefix
                        if(value_path == "reg-flag"):
                            self.reg_flag = value
                            self.reg_flag.value_namespace = name_space
                            self.reg_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "slot-no"):
                            self.slot_no = value
                            self.slot_no.value_namespace = name_space
                            self.slot_no.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.card_info:
                        if (c.has_data()):
                            return True
                    for c in self.device_info:
                        if (c.has_data()):
                            return True
                    return (
                        self.asic_avail_mask.is_set or
                        self.asic_oper_notify_to_fsdb_pending_bmap.is_set or
                        self.board_rev_id.is_set or
                        self.card_avail_mask.is_set or
                        self.coeff_major_rev.is_set or
                        self.coeff_minor_rev.is_set or
                        self.drv_version.is_set or
                        self.drvr_current_startup_timestamp.is_set or
                        self.drvr_initial_startup_timestamp.is_set or
                        self.exp_asic_avail_mask.is_set or
                        self.fabric_mode.is_set or
                        self.fc_mode.is_set or
                        self.fgid_conn_active.is_set or
                        self.fgid_reg_active.is_set or
                        self.fsdb_conn_active.is_set or
                        self.fsdb_reg_active.is_set or
                        self.functional_role.is_set or
                        self.is_cih_registered.is_set or
                        self.is_driver_ready.is_set or
                        self.is_fgid_download_completed.is_set or
                        self.is_fgid_download_in_progress.is_set or
                        self.is_full_fgid_download_req.is_set or
                        self.is_gaspp_registered.is_set or
                        self.issu_abort_rcvd.is_set or
                        self.issu_abort_sent.is_set or
                        self.issu_mgr_conn_active.is_set or
                        self.issu_mgr_reg_active.is_set or
                        self.issu_ready_ntfy_pending.is_set or
                        self.issu_role.is_set or
                        self.node_id.is_set or
                        self.num_cm_conn_reqs.is_set or
                        self.num_fgid_conn_reqs.is_set or
                        self.num_fsdb_conn_reqs.is_set or
                        self.num_fstats_conn_reqs.is_set or
                        self.num_intf_ports.is_set or
                        self.num_issu_mgr_conn_reqs.is_set or
                        self.num_peer_fia_conn_reqs.is_set or
                        self.num_pm_conn_reqs.is_set or
                        self.rack_num.is_set or
                        self.rack_type.is_set or
                        self.respawn_count.is_set or
                        self.total_asics.is_set or
                        self.uc_weight.is_set or
                        self.ucmc_ratio.is_set)

                def has_operation(self):
                    for c in self.card_info:
                        if (c.has_operation()):
                            return True
                    for c in self.device_info:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.asic_avail_mask.yfilter != YFilter.not_set or
                        self.asic_oper_notify_to_fsdb_pending_bmap.yfilter != YFilter.not_set or
                        self.board_rev_id.yfilter != YFilter.not_set or
                        self.card_avail_mask.yfilter != YFilter.not_set or
                        self.coeff_major_rev.yfilter != YFilter.not_set or
                        self.coeff_minor_rev.yfilter != YFilter.not_set or
                        self.drv_version.yfilter != YFilter.not_set or
                        self.drvr_current_startup_timestamp.yfilter != YFilter.not_set or
                        self.drvr_initial_startup_timestamp.yfilter != YFilter.not_set or
                        self.exp_asic_avail_mask.yfilter != YFilter.not_set or
                        self.fabric_mode.yfilter != YFilter.not_set or
                        self.fc_mode.yfilter != YFilter.not_set or
                        self.fgid_conn_active.yfilter != YFilter.not_set or
                        self.fgid_reg_active.yfilter != YFilter.not_set or
                        self.fsdb_conn_active.yfilter != YFilter.not_set or
                        self.fsdb_reg_active.yfilter != YFilter.not_set or
                        self.functional_role.yfilter != YFilter.not_set or
                        self.is_cih_registered.yfilter != YFilter.not_set or
                        self.is_driver_ready.yfilter != YFilter.not_set or
                        self.is_fgid_download_completed.yfilter != YFilter.not_set or
                        self.is_fgid_download_in_progress.yfilter != YFilter.not_set or
                        self.is_full_fgid_download_req.yfilter != YFilter.not_set or
                        self.is_gaspp_registered.yfilter != YFilter.not_set or
                        self.issu_abort_rcvd.yfilter != YFilter.not_set or
                        self.issu_abort_sent.yfilter != YFilter.not_set or
                        self.issu_mgr_conn_active.yfilter != YFilter.not_set or
                        self.issu_mgr_reg_active.yfilter != YFilter.not_set or
                        self.issu_ready_ntfy_pending.yfilter != YFilter.not_set or
                        self.issu_role.yfilter != YFilter.not_set or
                        self.node_id.yfilter != YFilter.not_set or
                        self.num_cm_conn_reqs.yfilter != YFilter.not_set or
                        self.num_fgid_conn_reqs.yfilter != YFilter.not_set or
                        self.num_fsdb_conn_reqs.yfilter != YFilter.not_set or
                        self.num_fstats_conn_reqs.yfilter != YFilter.not_set or
                        self.num_intf_ports.yfilter != YFilter.not_set or
                        self.num_issu_mgr_conn_reqs.yfilter != YFilter.not_set or
                        self.num_peer_fia_conn_reqs.yfilter != YFilter.not_set or
                        self.num_pm_conn_reqs.yfilter != YFilter.not_set or
                        self.rack_num.yfilter != YFilter.not_set or
                        self.rack_type.yfilter != YFilter.not_set or
                        self.respawn_count.yfilter != YFilter.not_set or
                        self.total_asics.yfilter != YFilter.not_set or
                        self.uc_weight.yfilter != YFilter.not_set or
                        self.ucmc_ratio.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "driver-information" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.asic_avail_mask.is_set or self.asic_avail_mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.asic_avail_mask.get_name_leafdata())
                    if (self.asic_oper_notify_to_fsdb_pending_bmap.is_set or self.asic_oper_notify_to_fsdb_pending_bmap.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.asic_oper_notify_to_fsdb_pending_bmap.get_name_leafdata())
                    if (self.board_rev_id.is_set or self.board_rev_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.board_rev_id.get_name_leafdata())
                    if (self.card_avail_mask.is_set or self.card_avail_mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.card_avail_mask.get_name_leafdata())
                    if (self.coeff_major_rev.is_set or self.coeff_major_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.coeff_major_rev.get_name_leafdata())
                    if (self.coeff_minor_rev.is_set or self.coeff_minor_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.coeff_minor_rev.get_name_leafdata())
                    if (self.drv_version.is_set or self.drv_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.drv_version.get_name_leafdata())
                    if (self.drvr_current_startup_timestamp.is_set or self.drvr_current_startup_timestamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.drvr_current_startup_timestamp.get_name_leafdata())
                    if (self.drvr_initial_startup_timestamp.is_set or self.drvr_initial_startup_timestamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.drvr_initial_startup_timestamp.get_name_leafdata())
                    if (self.exp_asic_avail_mask.is_set or self.exp_asic_avail_mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.exp_asic_avail_mask.get_name_leafdata())
                    if (self.fabric_mode.is_set or self.fabric_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fabric_mode.get_name_leafdata())
                    if (self.fc_mode.is_set or self.fc_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fc_mode.get_name_leafdata())
                    if (self.fgid_conn_active.is_set or self.fgid_conn_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fgid_conn_active.get_name_leafdata())
                    if (self.fgid_reg_active.is_set or self.fgid_reg_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fgid_reg_active.get_name_leafdata())
                    if (self.fsdb_conn_active.is_set or self.fsdb_conn_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fsdb_conn_active.get_name_leafdata())
                    if (self.fsdb_reg_active.is_set or self.fsdb_reg_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fsdb_reg_active.get_name_leafdata())
                    if (self.functional_role.is_set or self.functional_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.functional_role.get_name_leafdata())
                    if (self.is_cih_registered.is_set or self.is_cih_registered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_cih_registered.get_name_leafdata())
                    if (self.is_driver_ready.is_set or self.is_driver_ready.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_driver_ready.get_name_leafdata())
                    if (self.is_fgid_download_completed.is_set or self.is_fgid_download_completed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_fgid_download_completed.get_name_leafdata())
                    if (self.is_fgid_download_in_progress.is_set or self.is_fgid_download_in_progress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_fgid_download_in_progress.get_name_leafdata())
                    if (self.is_full_fgid_download_req.is_set or self.is_full_fgid_download_req.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_full_fgid_download_req.get_name_leafdata())
                    if (self.is_gaspp_registered.is_set or self.is_gaspp_registered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_gaspp_registered.get_name_leafdata())
                    if (self.issu_abort_rcvd.is_set or self.issu_abort_rcvd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_abort_rcvd.get_name_leafdata())
                    if (self.issu_abort_sent.is_set or self.issu_abort_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_abort_sent.get_name_leafdata())
                    if (self.issu_mgr_conn_active.is_set or self.issu_mgr_conn_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_mgr_conn_active.get_name_leafdata())
                    if (self.issu_mgr_reg_active.is_set or self.issu_mgr_reg_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_mgr_reg_active.get_name_leafdata())
                    if (self.issu_ready_ntfy_pending.is_set or self.issu_ready_ntfy_pending.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_ready_ntfy_pending.get_name_leafdata())
                    if (self.issu_role.is_set or self.issu_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issu_role.get_name_leafdata())
                    if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_id.get_name_leafdata())
                    if (self.num_cm_conn_reqs.is_set or self.num_cm_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_cm_conn_reqs.get_name_leafdata())
                    if (self.num_fgid_conn_reqs.is_set or self.num_fgid_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_fgid_conn_reqs.get_name_leafdata())
                    if (self.num_fsdb_conn_reqs.is_set or self.num_fsdb_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_fsdb_conn_reqs.get_name_leafdata())
                    if (self.num_fstats_conn_reqs.is_set or self.num_fstats_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_fstats_conn_reqs.get_name_leafdata())
                    if (self.num_intf_ports.is_set or self.num_intf_ports.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_intf_ports.get_name_leafdata())
                    if (self.num_issu_mgr_conn_reqs.is_set or self.num_issu_mgr_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_issu_mgr_conn_reqs.get_name_leafdata())
                    if (self.num_peer_fia_conn_reqs.is_set or self.num_peer_fia_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_peer_fia_conn_reqs.get_name_leafdata())
                    if (self.num_pm_conn_reqs.is_set or self.num_pm_conn_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_pm_conn_reqs.get_name_leafdata())
                    if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rack_num.get_name_leafdata())
                    if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rack_type.get_name_leafdata())
                    if (self.respawn_count.is_set or self.respawn_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.respawn_count.get_name_leafdata())
                    if (self.total_asics.is_set or self.total_asics.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_asics.get_name_leafdata())
                    if (self.uc_weight.is_set or self.uc_weight.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.uc_weight.get_name_leafdata())
                    if (self.ucmc_ratio.is_set or self.ucmc_ratio.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ucmc_ratio.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "card-info"):
                        for c in self.card_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Fia.Nodes.Node.DriverInformation.CardInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.card_info.append(c)
                        return c

                    if (child_yang_name == "device-info"):
                        for c in self.device_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Fia.Nodes.Node.DriverInformation.DeviceInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.device_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "card-info" or name == "device-info" or name == "asic-avail-mask" or name == "asic-oper-notify-to-fsdb-pending-bmap" or name == "board-rev-id" or name == "card-avail-mask" or name == "coeff-major-rev" or name == "coeff-minor-rev" or name == "drv-version" or name == "drvr-current-startup-timestamp" or name == "drvr-initial-startup-timestamp" or name == "exp-asic-avail-mask" or name == "fabric-mode" or name == "fc-mode" or name == "fgid-conn-active" or name == "fgid-reg-active" or name == "fsdb-conn-active" or name == "fsdb-reg-active" or name == "functional-role" or name == "is-cih-registered" or name == "is-driver-ready" or name == "is-fgid-download-completed" or name == "is-fgid-download-in-progress" or name == "is-full-fgid-download-req" or name == "is-gaspp-registered" or name == "issu-abort-rcvd" or name == "issu-abort-sent" or name == "issu-mgr-conn-active" or name == "issu-mgr-reg-active" or name == "issu-ready-ntfy-pending" or name == "issu-role" or name == "node-id" or name == "num-cm-conn-reqs" or name == "num-fgid-conn-reqs" or name == "num-fsdb-conn-reqs" or name == "num-fstats-conn-reqs" or name == "num-intf-ports" or name == "num-issu-mgr-conn-reqs" or name == "num-peer-fia-conn-reqs" or name == "num-pm-conn-reqs" or name == "rack-num" or name == "rack-type" or name == "respawn-count" or name == "total-asics" or name == "uc-weight" or name == "ucmc-ratio"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "asic-avail-mask"):
                        self.asic_avail_mask = value
                        self.asic_avail_mask.value_namespace = name_space
                        self.asic_avail_mask.value_namespace_prefix = name_space_prefix
                    if(value_path == "asic-oper-notify-to-fsdb-pending-bmap"):
                        self.asic_oper_notify_to_fsdb_pending_bmap = value
                        self.asic_oper_notify_to_fsdb_pending_bmap.value_namespace = name_space
                        self.asic_oper_notify_to_fsdb_pending_bmap.value_namespace_prefix = name_space_prefix
                    if(value_path == "board-rev-id"):
                        self.board_rev_id = value
                        self.board_rev_id.value_namespace = name_space
                        self.board_rev_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "card-avail-mask"):
                        self.card_avail_mask = value
                        self.card_avail_mask.value_namespace = name_space
                        self.card_avail_mask.value_namespace_prefix = name_space_prefix
                    if(value_path == "coeff-major-rev"):
                        self.coeff_major_rev = value
                        self.coeff_major_rev.value_namespace = name_space
                        self.coeff_major_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "coeff-minor-rev"):
                        self.coeff_minor_rev = value
                        self.coeff_minor_rev.value_namespace = name_space
                        self.coeff_minor_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "drv-version"):
                        self.drv_version = value
                        self.drv_version.value_namespace = name_space
                        self.drv_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "drvr-current-startup-timestamp"):
                        self.drvr_current_startup_timestamp = value
                        self.drvr_current_startup_timestamp.value_namespace = name_space
                        self.drvr_current_startup_timestamp.value_namespace_prefix = name_space_prefix
                    if(value_path == "drvr-initial-startup-timestamp"):
                        self.drvr_initial_startup_timestamp = value
                        self.drvr_initial_startup_timestamp.value_namespace = name_space
                        self.drvr_initial_startup_timestamp.value_namespace_prefix = name_space_prefix
                    if(value_path == "exp-asic-avail-mask"):
                        self.exp_asic_avail_mask = value
                        self.exp_asic_avail_mask.value_namespace = name_space
                        self.exp_asic_avail_mask.value_namespace_prefix = name_space_prefix
                    if(value_path == "fabric-mode"):
                        self.fabric_mode = value
                        self.fabric_mode.value_namespace = name_space
                        self.fabric_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "fc-mode"):
                        self.fc_mode = value
                        self.fc_mode.value_namespace = name_space
                        self.fc_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "fgid-conn-active"):
                        self.fgid_conn_active = value
                        self.fgid_conn_active.value_namespace = name_space
                        self.fgid_conn_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "fgid-reg-active"):
                        self.fgid_reg_active = value
                        self.fgid_reg_active.value_namespace = name_space
                        self.fgid_reg_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "fsdb-conn-active"):
                        self.fsdb_conn_active = value
                        self.fsdb_conn_active.value_namespace = name_space
                        self.fsdb_conn_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "fsdb-reg-active"):
                        self.fsdb_reg_active = value
                        self.fsdb_reg_active.value_namespace = name_space
                        self.fsdb_reg_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "functional-role"):
                        self.functional_role = value
                        self.functional_role.value_namespace = name_space
                        self.functional_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-cih-registered"):
                        self.is_cih_registered = value
                        self.is_cih_registered.value_namespace = name_space
                        self.is_cih_registered.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-driver-ready"):
                        self.is_driver_ready = value
                        self.is_driver_ready.value_namespace = name_space
                        self.is_driver_ready.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-fgid-download-completed"):
                        self.is_fgid_download_completed = value
                        self.is_fgid_download_completed.value_namespace = name_space
                        self.is_fgid_download_completed.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-fgid-download-in-progress"):
                        self.is_fgid_download_in_progress = value
                        self.is_fgid_download_in_progress.value_namespace = name_space
                        self.is_fgid_download_in_progress.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-full-fgid-download-req"):
                        self.is_full_fgid_download_req = value
                        self.is_full_fgid_download_req.value_namespace = name_space
                        self.is_full_fgid_download_req.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-gaspp-registered"):
                        self.is_gaspp_registered = value
                        self.is_gaspp_registered.value_namespace = name_space
                        self.is_gaspp_registered.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-abort-rcvd"):
                        self.issu_abort_rcvd = value
                        self.issu_abort_rcvd.value_namespace = name_space
                        self.issu_abort_rcvd.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-abort-sent"):
                        self.issu_abort_sent = value
                        self.issu_abort_sent.value_namespace = name_space
                        self.issu_abort_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-mgr-conn-active"):
                        self.issu_mgr_conn_active = value
                        self.issu_mgr_conn_active.value_namespace = name_space
                        self.issu_mgr_conn_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-mgr-reg-active"):
                        self.issu_mgr_reg_active = value
                        self.issu_mgr_reg_active.value_namespace = name_space
                        self.issu_mgr_reg_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-ready-ntfy-pending"):
                        self.issu_ready_ntfy_pending = value
                        self.issu_ready_ntfy_pending.value_namespace = name_space
                        self.issu_ready_ntfy_pending.value_namespace_prefix = name_space_prefix
                    if(value_path == "issu-role"):
                        self.issu_role = value
                        self.issu_role.value_namespace = name_space
                        self.issu_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-id"):
                        self.node_id = value
                        self.node_id.value_namespace = name_space
                        self.node_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-cm-conn-reqs"):
                        self.num_cm_conn_reqs = value
                        self.num_cm_conn_reqs.value_namespace = name_space
                        self.num_cm_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-fgid-conn-reqs"):
                        self.num_fgid_conn_reqs = value
                        self.num_fgid_conn_reqs.value_namespace = name_space
                        self.num_fgid_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-fsdb-conn-reqs"):
                        self.num_fsdb_conn_reqs = value
                        self.num_fsdb_conn_reqs.value_namespace = name_space
                        self.num_fsdb_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-fstats-conn-reqs"):
                        self.num_fstats_conn_reqs = value
                        self.num_fstats_conn_reqs.value_namespace = name_space
                        self.num_fstats_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-intf-ports"):
                        self.num_intf_ports = value
                        self.num_intf_ports.value_namespace = name_space
                        self.num_intf_ports.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-issu-mgr-conn-reqs"):
                        self.num_issu_mgr_conn_reqs = value
                        self.num_issu_mgr_conn_reqs.value_namespace = name_space
                        self.num_issu_mgr_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-peer-fia-conn-reqs"):
                        self.num_peer_fia_conn_reqs = value
                        self.num_peer_fia_conn_reqs.value_namespace = name_space
                        self.num_peer_fia_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-pm-conn-reqs"):
                        self.num_pm_conn_reqs = value
                        self.num_pm_conn_reqs.value_namespace = name_space
                        self.num_pm_conn_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "rack-num"):
                        self.rack_num = value
                        self.rack_num.value_namespace = name_space
                        self.rack_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "rack-type"):
                        self.rack_type = value
                        self.rack_type.value_namespace = name_space
                        self.rack_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "respawn-count"):
                        self.respawn_count = value
                        self.respawn_count.value_namespace = name_space
                        self.respawn_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-asics"):
                        self.total_asics = value
                        self.total_asics.value_namespace = name_space
                        self.total_asics.value_namespace_prefix = name_space_prefix
                    if(value_path == "uc-weight"):
                        self.uc_weight = value
                        self.uc_weight.value_namespace = name_space
                        self.uc_weight.value_namespace_prefix = name_space_prefix
                    if(value_path == "ucmc-ratio"):
                        self.ucmc_ratio = value
                        self.ucmc_ratio.value_namespace = name_space
                        self.ucmc_ratio.value_namespace_prefix = name_space_prefix


            class ClearStatistics(Entity):
                """
                Clear statistics information
                
                .. attribute:: asic_instances
                
                	Instance table for clear statistics information
                	**type**\:   :py:class:`AsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.ClearStatistics, self).__init__()

                    self.yang_name = "clear-statistics"
                    self.yang_parent_name = "node"

                    self.asic_instances = Fia.Nodes.Node.ClearStatistics.AsicInstances()
                    self.asic_instances.parent = self
                    self._children_name_map["asic_instances"] = "asic-instances"
                    self._children_yang_names.add("asic-instances")


                class AsicInstances(Entity):
                    """
                    Instance table for clear statistics
                    information
                    
                    .. attribute:: asic_instance
                    
                    	Asic instance to be cleared
                    	**type**\: list of    :py:class:`AsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.ClearStatistics.AsicInstances, self).__init__()

                        self.yang_name = "asic-instances"
                        self.yang_parent_name = "clear-statistics"

                        self.asic_instance = YList(self)

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
                                    super(Fia.Nodes.Node.ClearStatistics.AsicInstances, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.ClearStatistics.AsicInstances, self).__setattr__(name, value)


                    class AsicInstance(Entity):
                        """
                        Asic instance to be cleared
                        
                        .. attribute:: asic_instance  <key>
                        
                        	Asic instance
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: instance
                        
                        	Clear value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance, self).__init__()

                            self.yang_name = "asic-instance"
                            self.yang_parent_name = "asic-instances"

                            self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                            self.instance = YLeaf(YType.int32, "instance")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("asic_instance",
                                            "instance") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.asic_instance.is_set or
                                self.instance.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.asic_instance.yfilter != YFilter.not_set or
                                self.instance.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "asic-instance" + "[asic-instance='" + self.asic_instance.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asic_instance.get_name_leafdata())
                            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instance.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asic-instance" or name == "instance"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "asic-instance"):
                                self.asic_instance = value
                                self.asic_instance.value_namespace = name_space
                                self.asic_instance.value_namespace_prefix = name_space_prefix
                            if(value_path == "instance"):
                                self.instance = value
                                self.instance.value_namespace = name_space
                                self.instance.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.asic_instance:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.asic_instance:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "asic-instances" + path_buffer

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

                        if (child_yang_name == "asic-instance"):
                            for c in self.asic_instance:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.asic_instance.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "asic-instance"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.asic_instances is not None and self.asic_instances.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.asic_instances is not None and self.asic_instances.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "clear-statistics" + path_buffer

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

                    if (child_yang_name == "asic-instances"):
                        if (self.asic_instances is None):
                            self.asic_instances = Fia.Nodes.Node.ClearStatistics.AsicInstances()
                            self.asic_instances.parent = self
                            self._children_name_map["asic_instances"] = "asic-instances"
                        return self.asic_instances

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "asic-instances"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TxLinkInformation(Entity):
                """
                FIA link TX information
                
                .. attribute:: tx_status_option_table
                
                	Link table for tx information
                	**type**\:   :py:class:`TxStatusOptionTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.TxLinkInformation, self).__init__()

                    self.yang_name = "tx-link-information"
                    self.yang_parent_name = "node"

                    self.tx_status_option_table = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable()
                    self.tx_status_option_table.parent = self
                    self._children_name_map["tx_status_option_table"] = "tx-status-option-table"
                    self._children_yang_names.add("tx-status-option-table")


                class TxStatusOptionTable(Entity):
                    """
                    Link table for tx information
                    
                    .. attribute:: tx_status_option
                    
                    	Option\: data, ctrl, all\- for now none
                    	**type**\:   :py:class:`TxStatusOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable, self).__init__()

                        self.yang_name = "tx-status-option-table"
                        self.yang_parent_name = "tx-link-information"

                        self.tx_status_option = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption()
                        self.tx_status_option.parent = self
                        self._children_name_map["tx_status_option"] = "tx-status-option"
                        self._children_yang_names.add("tx-status-option")


                    class TxStatusOption(Entity):
                        """
                        Option\: data, ctrl, all\- for now none
                        
                        .. attribute:: tx_asic_instances
                        
                        	Instance table for tx information
                        	**type**\:   :py:class:`TxAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption, self).__init__()

                            self.yang_name = "tx-status-option"
                            self.yang_parent_name = "tx-status-option-table"

                            self.tx_asic_instances = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances()
                            self.tx_asic_instances.parent = self
                            self._children_name_map["tx_asic_instances"] = "tx-asic-instances"
                            self._children_yang_names.add("tx-asic-instances")


                        class TxAsicInstances(Entity):
                            """
                            Instance table for tx information
                            
                            .. attribute:: tx_asic_instance
                            
                            	Instance number for tx link information
                            	**type**\: list of    :py:class:`TxAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances, self).__init__()

                                self.yang_name = "tx-asic-instances"
                                self.yang_parent_name = "tx-status-option"

                                self.tx_asic_instance = YList(self)

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
                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances, self).__setattr__(name, value)


                            class TxAsicInstance(Entity):
                                """
                                Instance number for tx link information
                                
                                .. attribute:: instance  <key>
                                
                                	Transmit instance
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: tx_links
                                
                                	Link table for tx information
                                	**type**\:   :py:class:`TxLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance, self).__init__()

                                    self.yang_name = "tx-asic-instance"
                                    self.yang_parent_name = "tx-asic-instances"

                                    self.instance = YLeaf(YType.uint32, "instance")

                                    self.tx_links = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks()
                                    self.tx_links.parent = self
                                    self._children_name_map["tx_links"] = "tx-links"
                                    self._children_yang_names.add("tx-links")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("instance") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance, self).__setattr__(name, value)


                                class TxLinks(Entity):
                                    """
                                    Link table for tx information
                                    
                                    .. attribute:: tx_link
                                    
                                    	Link number for tx link information
                                    	**type**\: list of    :py:class:`TxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks, self).__init__()

                                        self.yang_name = "tx-links"
                                        self.yang_parent_name = "tx-asic-instance"

                                        self.tx_link = YList(self)

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
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks, self).__setattr__(name, value)


                                    class TxLink(Entity):
                                        """
                                        Link number for tx link information
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\:  int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\:  int
                                        
                                        	**range:** 0..47
                                        
                                        .. attribute:: tx_link
                                        
                                        	Single link information
                                        	**type**\: list of    :py:class:`TxLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink, self).__init__()

                                            self.yang_name = "tx-link"
                                            self.yang_parent_name = "tx-links"

                                            self.end_number = YLeaf(YType.uint32, "end-number")

                                            self.start_number = YLeaf(YType.uint32, "start-number")

                                            self.tx_link = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("end_number",
                                                            "start_number") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink, self).__setattr__(name, value)


                                        class TxLink(Entity):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  <key>
                                            
                                            	Single Link
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: admin_state
                                            
                                            	Admin State
                                            	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                            
                                            .. attribute:: coeff1
                                            
                                            	coeff1
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: coeff2
                                            
                                            	coeff2
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: error_state
                                            
                                            	Error State
                                            	**type**\:   :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\:   :py:class:`FarEndLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink>`
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History>`
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_power_enabled
                                            
                                            	is power enabled
                                            	**type**\:  bool
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: oper_state
                                            
                                            	Oper State
                                            	**type**\:   :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	stage
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: stats
                                            
                                            	stats
                                            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats>`
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\:   :py:class:`ThisLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink, self).__init__()

                                                self.yang_name = "tx-link"
                                                self.yang_parent_name = "tx-link"

                                                self.link = YLeaf(YType.int32, "link")

                                                self.admin_state = YLeaf(YType.enumeration, "admin-state")

                                                self.coeff1 = YLeaf(YType.uint32, "coeff1")

                                                self.coeff2 = YLeaf(YType.uint32, "coeff2")

                                                self.error_state = YLeaf(YType.enumeration, "error-state")

                                                self.is_conf_pending = YLeaf(YType.boolean, "is-conf-pending")

                                                self.is_link_valid = YLeaf(YType.boolean, "is-link-valid")

                                                self.is_power_enabled = YLeaf(YType.boolean, "is-power-enabled")

                                                self.num_admin_shuts = YLeaf(YType.uint32, "num-admin-shuts")

                                                self.oper_state = YLeaf(YType.enumeration, "oper-state")

                                                self.speed = YLeaf(YType.uint32, "speed")

                                                self.stage = YLeaf(YType.uint8, "stage")

                                                self.far_end_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink()
                                                self.far_end_link.parent = self
                                                self._children_name_map["far_end_link"] = "far-end-link"
                                                self._children_yang_names.add("far-end-link")

                                                self.history = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History()
                                                self.history.parent = self
                                                self._children_name_map["history"] = "history"
                                                self._children_yang_names.add("history")

                                                self.stats = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats()
                                                self.stats.parent = self
                                                self._children_name_map["stats"] = "stats"
                                                self._children_yang_names.add("stats")

                                                self.this_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink()
                                                self.this_link.parent = self
                                                self._children_name_map["this_link"] = "this-link"
                                                self._children_yang_names.add("this-link")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("link",
                                                                "admin_state",
                                                                "coeff1",
                                                                "coeff2",
                                                                "error_state",
                                                                "is_conf_pending",
                                                                "is_link_valid",
                                                                "is_power_enabled",
                                                                "num_admin_shuts",
                                                                "oper_state",
                                                                "speed",
                                                                "stage") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink, self).__setattr__(name, value)


                                            class ThisLink(Entity):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink, self).__init__()

                                                    self.yang_name = "this-link"
                                                    self.yang_parent_name = "tx-link"

                                                    self.link_num = YLeaf(YType.uint32, "link-num")

                                                    self.link_stage = YLeaf(YType.enumeration, "link-stage")

                                                    self.link_type = YLeaf(YType.enumeration, "link-type")

                                                    self.phy_link_num = YLeaf(YType.uint32, "phy-link-num")

                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._children_yang_names.add("asic-id")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("link_num",
                                                                    "link_stage",
                                                                    "link_type",
                                                                    "phy_link_num") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink, self).__setattr__(name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "this-link"

                                                        self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                                        self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                                        self.rack_num = YLeaf(YType.uint32, "rack-num")

                                                        self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                                        self.slot_num = YLeaf(YType.uint32, "slot-num")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("asic_instance",
                                                                        "asic_type",
                                                                        "rack_num",
                                                                        "rack_type",
                                                                        "slot_num") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.asic_instance.is_set or
                                                            self.asic_type.is_set or
                                                            self.rack_num.is_set or
                                                            self.rack_type.is_set or
                                                            self.slot_num.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.asic_instance.yfilter != YFilter.not_set or
                                                            self.asic_type.yfilter != YFilter.not_set or
                                                            self.rack_num.yfilter != YFilter.not_set or
                                                            self.rack_type.yfilter != YFilter.not_set or
                                                            self.slot_num.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "asic-id" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                                        if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_type.get_name_leafdata())
                                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                        if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_type.get_name_leafdata())
                                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.slot_num.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "asic-instance"):
                                                            self.asic_instance = value
                                                            self.asic_instance.value_namespace = name_space
                                                            self.asic_instance.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "asic-type"):
                                                            self.asic_type = value
                                                            self.asic_type.value_namespace = name_space
                                                            self.asic_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-num"):
                                                            self.rack_num = value
                                                            self.rack_num.value_namespace = name_space
                                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-type"):
                                                            self.rack_type = value
                                                            self.rack_type.value_namespace = name_space
                                                            self.rack_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "slot-num"):
                                                            self.slot_num = value
                                                            self.slot_num.value_namespace = name_space
                                                            self.slot_num.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        self.link_num.is_set or
                                                        self.link_stage.is_set or
                                                        self.link_type.is_set or
                                                        self.phy_link_num.is_set or
                                                        (self.asic_id is not None and self.asic_id.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.link_num.yfilter != YFilter.not_set or
                                                        self.link_stage.yfilter != YFilter.not_set or
                                                        self.link_type.yfilter != YFilter.not_set or
                                                        self.phy_link_num.yfilter != YFilter.not_set or
                                                        (self.asic_id is not None and self.asic_id.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "this-link" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.link_num.is_set or self.link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_num.get_name_leafdata())
                                                    if (self.link_stage.is_set or self.link_stage.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_stage.get_name_leafdata())
                                                    if (self.link_type.is_set or self.link_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_type.get_name_leafdata())
                                                    if (self.phy_link_num.is_set or self.phy_link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.phy_link_num.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "asic-id"):
                                                        if (self.asic_id is None):
                                                            self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId()
                                                            self.asic_id.parent = self
                                                            self._children_name_map["asic_id"] = "asic-id"
                                                        return self.asic_id

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "asic-id" or name == "link-num" or name == "link-stage" or name == "link-type" or name == "phy-link-num"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "link-num"):
                                                        self.link_num = value
                                                        self.link_num.value_namespace = name_space
                                                        self.link_num.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-stage"):
                                                        self.link_stage = value
                                                        self.link_stage.value_namespace = name_space
                                                        self.link_stage.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-type"):
                                                        self.link_type = value
                                                        self.link_type.value_namespace = name_space
                                                        self.link_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "phy-link-num"):
                                                        self.phy_link_num = value
                                                        self.phy_link_num.value_namespace = name_space
                                                        self.phy_link_num.value_namespace_prefix = name_space_prefix


                                            class FarEndLink(Entity):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_stage
                                                
                                                	Link Stage
                                                	**type**\:   :py:class:`LinkStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkStage>`
                                                
                                                .. attribute:: link_type
                                                
                                                	Link Type
                                                	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Link>`
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink, self).__init__()

                                                    self.yang_name = "far-end-link"
                                                    self.yang_parent_name = "tx-link"

                                                    self.link_num = YLeaf(YType.uint32, "link-num")

                                                    self.link_stage = YLeaf(YType.enumeration, "link-stage")

                                                    self.link_type = YLeaf(YType.enumeration, "link-type")

                                                    self.phy_link_num = YLeaf(YType.uint32, "phy-link-num")

                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self._children_name_map["asic_id"] = "asic-id"
                                                    self._children_yang_names.add("asic-id")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("link_num",
                                                                    "link_stage",
                                                                    "link_type",
                                                                    "phy_link_num") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink, self).__setattr__(name, value)


                                                class AsicId(Entity):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	Asic Type
                                                    	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	Rack Type
                                                    	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId, self).__init__()

                                                        self.yang_name = "asic-id"
                                                        self.yang_parent_name = "far-end-link"

                                                        self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                                        self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                                        self.rack_num = YLeaf(YType.uint32, "rack-num")

                                                        self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                                        self.slot_num = YLeaf(YType.uint32, "slot-num")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("asic_instance",
                                                                        "asic_type",
                                                                        "rack_num",
                                                                        "rack_type",
                                                                        "slot_num") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.asic_instance.is_set or
                                                            self.asic_type.is_set or
                                                            self.rack_num.is_set or
                                                            self.rack_type.is_set or
                                                            self.slot_num.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.asic_instance.yfilter != YFilter.not_set or
                                                            self.asic_type.yfilter != YFilter.not_set or
                                                            self.rack_num.yfilter != YFilter.not_set or
                                                            self.rack_type.yfilter != YFilter.not_set or
                                                            self.slot_num.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "asic-id" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                                        if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.asic_type.get_name_leafdata())
                                                        if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                        if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.rack_type.get_name_leafdata())
                                                        if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.slot_num.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "asic-instance"):
                                                            self.asic_instance = value
                                                            self.asic_instance.value_namespace = name_space
                                                            self.asic_instance.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "asic-type"):
                                                            self.asic_type = value
                                                            self.asic_type.value_namespace = name_space
                                                            self.asic_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-num"):
                                                            self.rack_num = value
                                                            self.rack_num.value_namespace = name_space
                                                            self.rack_num.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "rack-type"):
                                                            self.rack_type = value
                                                            self.rack_type.value_namespace = name_space
                                                            self.rack_type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "slot-num"):
                                                            self.slot_num = value
                                                            self.slot_num.value_namespace = name_space
                                                            self.slot_num.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        self.link_num.is_set or
                                                        self.link_stage.is_set or
                                                        self.link_type.is_set or
                                                        self.phy_link_num.is_set or
                                                        (self.asic_id is not None and self.asic_id.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.link_num.yfilter != YFilter.not_set or
                                                        self.link_stage.yfilter != YFilter.not_set or
                                                        self.link_type.yfilter != YFilter.not_set or
                                                        self.phy_link_num.yfilter != YFilter.not_set or
                                                        (self.asic_id is not None and self.asic_id.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "far-end-link" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.link_num.is_set or self.link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_num.get_name_leafdata())
                                                    if (self.link_stage.is_set or self.link_stage.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_stage.get_name_leafdata())
                                                    if (self.link_type.is_set or self.link_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_type.get_name_leafdata())
                                                    if (self.phy_link_num.is_set or self.phy_link_num.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.phy_link_num.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "asic-id"):
                                                        if (self.asic_id is None):
                                                            self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId()
                                                            self.asic_id.parent = self
                                                            self._children_name_map["asic_id"] = "asic-id"
                                                        return self.asic_id

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "asic-id" or name == "link-num" or name == "link-stage" or name == "link-type" or name == "phy-link-num"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "link-num"):
                                                        self.link_num = value
                                                        self.link_num.value_namespace = name_space
                                                        self.link_num.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-stage"):
                                                        self.link_stage = value
                                                        self.link_stage.value_namespace = name_space
                                                        self.link_stage.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-type"):
                                                        self.link_type = value
                                                        self.link_type.value_namespace = name_space
                                                        self.link_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "phy-link-num"):
                                                        self.phy_link_num = value
                                                        self.phy_link_num.value_namespace = name_space
                                                        self.phy_link_num.value_namespace_prefix = name_space_prefix


                                            class Stats(Entity):
                                                """
                                                stats
                                                
                                                .. attribute:: dummy
                                                
                                                	dummy
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats, self).__init__()

                                                    self.yang_name = "stats"
                                                    self.yang_parent_name = "tx-link"

                                                    self.dummy = YLeaf(YType.uint32, "dummy")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("dummy") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return self.dummy.is_set

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.dummy.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "stats" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.dummy.is_set or self.dummy.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.dummy.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "dummy"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "dummy"):
                                                        self.dummy = value
                                                        self.dummy.value_namespace = name_space
                                                        self.dummy.value_namespace_prefix = name_space_prefix


                                            class History(Entity):
                                                """
                                                history
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of    :py:class:`Hist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist>`
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History, self).__init__()

                                                    self.yang_name = "history"
                                                    self.yang_parent_name = "tx-link"

                                                    self.histnum = YLeaf(YType.uint8, "histnum")

                                                    self.start_index = YLeaf(YType.uint8, "start-index")

                                                    self.hist = YList(self)

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("histnum",
                                                                    "start_index") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History, self).__setattr__(name, value)


                                                class Hist(Entity):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	Admin State
                                                    	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	Error State
                                                    	**type**\:   :py:class:`LinkErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.LinkErrorState>`
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	Oper State
                                                    	**type**\:   :py:class:`OperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.OperState>`
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist, self).__init__()

                                                        self.yang_name = "hist"
                                                        self.yang_parent_name = "history"

                                                        self.admin_state = YLeaf(YType.enumeration, "admin-state")

                                                        self.error_state = YLeaf(YType.enumeration, "error-state")

                                                        self.oper_state = YLeaf(YType.enumeration, "oper-state")

                                                        self.reasons = YLeaf(YType.str, "reasons")

                                                        self.timestamp = YLeaf(YType.uint64, "timestamp")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("admin_state",
                                                                        "error_state",
                                                                        "oper_state",
                                                                        "reasons",
                                                                        "timestamp") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.admin_state.is_set or
                                                            self.error_state.is_set or
                                                            self.oper_state.is_set or
                                                            self.reasons.is_set or
                                                            self.timestamp.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.admin_state.yfilter != YFilter.not_set or
                                                            self.error_state.yfilter != YFilter.not_set or
                                                            self.oper_state.yfilter != YFilter.not_set or
                                                            self.reasons.yfilter != YFilter.not_set or
                                                            self.timestamp.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "hist" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.admin_state.get_name_leafdata())
                                                        if (self.error_state.is_set or self.error_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.error_state.get_name_leafdata())
                                                        if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.oper_state.get_name_leafdata())
                                                        if (self.reasons.is_set or self.reasons.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.reasons.get_name_leafdata())
                                                        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.timestamp.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "admin-state" or name == "error-state" or name == "oper-state" or name == "reasons" or name == "timestamp"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "admin-state"):
                                                            self.admin_state = value
                                                            self.admin_state.value_namespace = name_space
                                                            self.admin_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "error-state"):
                                                            self.error_state = value
                                                            self.error_state.value_namespace = name_space
                                                            self.error_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "oper-state"):
                                                            self.oper_state = value
                                                            self.oper_state.value_namespace = name_space
                                                            self.oper_state.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "reasons"):
                                                            self.reasons = value
                                                            self.reasons.value_namespace = name_space
                                                            self.reasons.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "timestamp"):
                                                            self.timestamp = value
                                                            self.timestamp.value_namespace = name_space
                                                            self.timestamp.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    for c in self.hist:
                                                        if (c.has_data()):
                                                            return True
                                                    return (
                                                        self.histnum.is_set or
                                                        self.start_index.is_set)

                                                def has_operation(self):
                                                    for c in self.hist:
                                                        if (c.has_operation()):
                                                            return True
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.histnum.yfilter != YFilter.not_set or
                                                        self.start_index.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "history" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.histnum.is_set or self.histnum.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.histnum.get_name_leafdata())
                                                    if (self.start_index.is_set or self.start_index.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.start_index.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "hist"):
                                                        for c in self.hist:
                                                            segment = c.get_segment_path()
                                                            if (segment_path == segment):
                                                                return c
                                                        c = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist()
                                                        c.parent = self
                                                        local_reference_key = "ydk::seg::%s" % segment_path
                                                        self._local_refs[local_reference_key] = c
                                                        self.hist.append(c)
                                                        return c

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "hist" or name == "histnum" or name == "start-index"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "histnum"):
                                                        self.histnum = value
                                                        self.histnum.value_namespace = name_space
                                                        self.histnum.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "start-index"):
                                                        self.start_index = value
                                                        self.start_index.value_namespace = name_space
                                                        self.start_index.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.link.is_set or
                                                    self.admin_state.is_set or
                                                    self.coeff1.is_set or
                                                    self.coeff2.is_set or
                                                    self.error_state.is_set or
                                                    self.is_conf_pending.is_set or
                                                    self.is_link_valid.is_set or
                                                    self.is_power_enabled.is_set or
                                                    self.num_admin_shuts.is_set or
                                                    self.oper_state.is_set or
                                                    self.speed.is_set or
                                                    self.stage.is_set or
                                                    (self.far_end_link is not None and self.far_end_link.has_data()) or
                                                    (self.history is not None and self.history.has_data()) or
                                                    (self.stats is not None and self.stats.has_data()) or
                                                    (self.this_link is not None and self.this_link.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.link.yfilter != YFilter.not_set or
                                                    self.admin_state.yfilter != YFilter.not_set or
                                                    self.coeff1.yfilter != YFilter.not_set or
                                                    self.coeff2.yfilter != YFilter.not_set or
                                                    self.error_state.yfilter != YFilter.not_set or
                                                    self.is_conf_pending.yfilter != YFilter.not_set or
                                                    self.is_link_valid.yfilter != YFilter.not_set or
                                                    self.is_power_enabled.yfilter != YFilter.not_set or
                                                    self.num_admin_shuts.yfilter != YFilter.not_set or
                                                    self.oper_state.yfilter != YFilter.not_set or
                                                    self.speed.yfilter != YFilter.not_set or
                                                    self.stage.yfilter != YFilter.not_set or
                                                    (self.far_end_link is not None and self.far_end_link.has_operation()) or
                                                    (self.history is not None and self.history.has_operation()) or
                                                    (self.stats is not None and self.stats.has_operation()) or
                                                    (self.this_link is not None and self.this_link.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "tx-link" + "[link='" + self.link.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.link.is_set or self.link.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.link.get_name_leafdata())
                                                if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.admin_state.get_name_leafdata())
                                                if (self.coeff1.is_set or self.coeff1.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.coeff1.get_name_leafdata())
                                                if (self.coeff2.is_set or self.coeff2.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.coeff2.get_name_leafdata())
                                                if (self.error_state.is_set or self.error_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.error_state.get_name_leafdata())
                                                if (self.is_conf_pending.is_set or self.is_conf_pending.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_conf_pending.get_name_leafdata())
                                                if (self.is_link_valid.is_set or self.is_link_valid.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_link_valid.get_name_leafdata())
                                                if (self.is_power_enabled.is_set or self.is_power_enabled.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_power_enabled.get_name_leafdata())
                                                if (self.num_admin_shuts.is_set or self.num_admin_shuts.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.num_admin_shuts.get_name_leafdata())
                                                if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.oper_state.get_name_leafdata())
                                                if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.speed.get_name_leafdata())
                                                if (self.stage.is_set or self.stage.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.stage.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "far-end-link"):
                                                    if (self.far_end_link is None):
                                                        self.far_end_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink()
                                                        self.far_end_link.parent = self
                                                        self._children_name_map["far_end_link"] = "far-end-link"
                                                    return self.far_end_link

                                                if (child_yang_name == "history"):
                                                    if (self.history is None):
                                                        self.history = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History()
                                                        self.history.parent = self
                                                        self._children_name_map["history"] = "history"
                                                    return self.history

                                                if (child_yang_name == "stats"):
                                                    if (self.stats is None):
                                                        self.stats = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats()
                                                        self.stats.parent = self
                                                        self._children_name_map["stats"] = "stats"
                                                    return self.stats

                                                if (child_yang_name == "this-link"):
                                                    if (self.this_link is None):
                                                        self.this_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink()
                                                        self.this_link.parent = self
                                                        self._children_name_map["this_link"] = "this-link"
                                                    return self.this_link

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "far-end-link" or name == "history" or name == "stats" or name == "this-link" or name == "link" or name == "admin-state" or name == "coeff1" or name == "coeff2" or name == "error-state" or name == "is-conf-pending" or name == "is-link-valid" or name == "is-power-enabled" or name == "num-admin-shuts" or name == "oper-state" or name == "speed" or name == "stage"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "link"):
                                                    self.link = value
                                                    self.link.value_namespace = name_space
                                                    self.link.value_namespace_prefix = name_space_prefix
                                                if(value_path == "admin-state"):
                                                    self.admin_state = value
                                                    self.admin_state.value_namespace = name_space
                                                    self.admin_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "coeff1"):
                                                    self.coeff1 = value
                                                    self.coeff1.value_namespace = name_space
                                                    self.coeff1.value_namespace_prefix = name_space_prefix
                                                if(value_path == "coeff2"):
                                                    self.coeff2 = value
                                                    self.coeff2.value_namespace = name_space
                                                    self.coeff2.value_namespace_prefix = name_space_prefix
                                                if(value_path == "error-state"):
                                                    self.error_state = value
                                                    self.error_state.value_namespace = name_space
                                                    self.error_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-conf-pending"):
                                                    self.is_conf_pending = value
                                                    self.is_conf_pending.value_namespace = name_space
                                                    self.is_conf_pending.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-link-valid"):
                                                    self.is_link_valid = value
                                                    self.is_link_valid.value_namespace = name_space
                                                    self.is_link_valid.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-power-enabled"):
                                                    self.is_power_enabled = value
                                                    self.is_power_enabled.value_namespace = name_space
                                                    self.is_power_enabled.value_namespace_prefix = name_space_prefix
                                                if(value_path == "num-admin-shuts"):
                                                    self.num_admin_shuts = value
                                                    self.num_admin_shuts.value_namespace = name_space
                                                    self.num_admin_shuts.value_namespace_prefix = name_space_prefix
                                                if(value_path == "oper-state"):
                                                    self.oper_state = value
                                                    self.oper_state.value_namespace = name_space
                                                    self.oper_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "speed"):
                                                    self.speed = value
                                                    self.speed.value_namespace = name_space
                                                    self.speed.value_namespace_prefix = name_space_prefix
                                                if(value_path == "stage"):
                                                    self.stage = value
                                                    self.stage.value_namespace = name_space
                                                    self.stage.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.tx_link:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.end_number.is_set or
                                                self.start_number.is_set)

                                        def has_operation(self):
                                            for c in self.tx_link:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.end_number.yfilter != YFilter.not_set or
                                                self.start_number.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "tx-link" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.end_number.is_set or self.end_number.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.end_number.get_name_leafdata())
                                            if (self.start_number.is_set or self.start_number.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.start_number.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "tx-link"):
                                                for c in self.tx_link:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.tx_link.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "tx-link" or name == "end-number" or name == "start-number"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "end-number"):
                                                self.end_number = value
                                                self.end_number.value_namespace = name_space
                                                self.end_number.value_namespace_prefix = name_space_prefix
                                            if(value_path == "start-number"):
                                                self.start_number = value
                                                self.start_number.value_namespace = name_space
                                                self.start_number.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.tx_link:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.tx_link:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tx-links" + path_buffer

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

                                        if (child_yang_name == "tx-link"):
                                            for c in self.tx_link:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.tx_link.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "tx-link"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.instance.is_set or
                                        (self.tx_links is not None and self.tx_links.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.instance.yfilter != YFilter.not_set or
                                        (self.tx_links is not None and self.tx_links.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tx-asic-instance" + "[instance='" + self.instance.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.instance.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "tx-links"):
                                        if (self.tx_links is None):
                                            self.tx_links = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks()
                                            self.tx_links.parent = self
                                            self._children_name_map["tx_links"] = "tx-links"
                                        return self.tx_links

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tx-links" or name == "instance"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "instance"):
                                        self.instance = value
                                        self.instance.value_namespace = name_space
                                        self.instance.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.tx_asic_instance:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.tx_asic_instance:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tx-asic-instances" + path_buffer

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

                                if (child_yang_name == "tx-asic-instance"):
                                    for c in self.tx_asic_instance:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tx_asic_instance.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tx-asic-instance"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.tx_asic_instances is not None and self.tx_asic_instances.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.tx_asic_instances is not None and self.tx_asic_instances.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx-status-option" + path_buffer

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

                            if (child_yang_name == "tx-asic-instances"):
                                if (self.tx_asic_instances is None):
                                    self.tx_asic_instances = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances()
                                    self.tx_asic_instances.parent = self
                                    self._children_name_map["tx_asic_instances"] = "tx-asic-instances"
                                return self.tx_asic_instances

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "tx-asic-instances"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.tx_status_option is not None and self.tx_status_option.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.tx_status_option is not None and self.tx_status_option.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tx-status-option-table" + path_buffer

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

                        if (child_yang_name == "tx-status-option"):
                            if (self.tx_status_option is None):
                                self.tx_status_option = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption()
                                self.tx_status_option.parent = self
                                self._children_name_map["tx_status_option"] = "tx-status-option"
                            return self.tx_status_option

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tx-status-option"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.tx_status_option_table is not None and self.tx_status_option_table.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.tx_status_option_table is not None and self.tx_status_option_table.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tx-link-information" + path_buffer

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

                    if (child_yang_name == "tx-status-option-table"):
                        if (self.tx_status_option_table is None):
                            self.tx_status_option_table = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable()
                            self.tx_status_option_table.parent = self
                            self._children_name_map["tx_status_option_table"] = "tx-status-option-table"
                        return self.tx_status_option_table

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tx-status-option-table"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DiagShell(Entity):
                """
                FIA diag shell information
                
                .. attribute:: diag_shell_units
                
                	Unit table for diag shell
                	**type**\:   :py:class:`DiagShellUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.DiagShell, self).__init__()

                    self.yang_name = "diag-shell"
                    self.yang_parent_name = "node"

                    self.diag_shell_units = Fia.Nodes.Node.DiagShell.DiagShellUnits()
                    self.diag_shell_units.parent = self
                    self._children_name_map["diag_shell_units"] = "diag-shell-units"
                    self._children_yang_names.add("diag-shell-units")


                class DiagShellUnits(Entity):
                    """
                    Unit table for diag shell
                    
                    .. attribute:: diag_shell_unit
                    
                    	Unit number for diag shell statistics
                    	**type**\: list of    :py:class:`DiagShellUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits, self).__init__()

                        self.yang_name = "diag-shell-units"
                        self.yang_parent_name = "diag-shell"

                        self.diag_shell_unit = YList(self)

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
                                    super(Fia.Nodes.Node.DiagShell.DiagShellUnits, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.DiagShell.DiagShellUnits, self).__setattr__(name, value)


                    class DiagShellUnit(Entity):
                        """
                        Unit number for diag shell statistics
                        
                        .. attribute:: unit  <key>
                        
                        	Unit number
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        .. attribute:: commands
                        
                        	Command table for diag shell
                        	**type**\:   :py:class:`Commands <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit, self).__init__()

                            self.yang_name = "diag-shell-unit"
                            self.yang_parent_name = "diag-shell-units"

                            self.unit = YLeaf(YType.uint32, "unit")

                            self.commands = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands()
                            self.commands.parent = self
                            self._children_name_map["commands"] = "commands"
                            self._children_yang_names.add("commands")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("unit") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit, self).__setattr__(name, value)


                        class Commands(Entity):
                            """
                            Command table for diag shell
                            
                            .. attribute:: command
                            
                            	Command for diag shell statistics
                            	**type**\: list of    :py:class:`Command <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands, self).__init__()

                                self.yang_name = "commands"
                                self.yang_parent_name = "diag-shell-unit"

                                self.command = YList(self)

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
                                            super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands, self).__setattr__(name, value)


                            class Command(Entity):
                                """
                                Command for diag shell statistics
                                
                                .. attribute:: cmd  <key>
                                
                                	Shell command
                                	**type**\:  str
                                
                                .. attribute:: output
                                
                                	Added to support datalist
                                	**type**\: list of    :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command, self).__init__()

                                    self.yang_name = "command"
                                    self.yang_parent_name = "commands"

                                    self.cmd = YLeaf(YType.str, "cmd")

                                    self.output = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("cmd") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command, self).__setattr__(name, value)


                                class Output(Entity):
                                    """
                                    Added to support datalist
                                    
                                    .. attribute:: output  <key>
                                    
                                    	First line
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: output_xr
                                    
                                    	output xr
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, self).__init__()

                                        self.yang_name = "output"
                                        self.yang_parent_name = "command"

                                        self.output = YLeaf(YType.str, "output")

                                        self.output_xr = YLeaf(YType.str, "output-xr")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("output",
                                                        "output_xr") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.output.is_set or
                                            self.output_xr.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.output.yfilter != YFilter.not_set or
                                            self.output_xr.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "output" + "[output='" + self.output.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.output.is_set or self.output.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.output.get_name_leafdata())
                                        if (self.output_xr.is_set or self.output_xr.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.output_xr.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "output" or name == "output-xr"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "output"):
                                            self.output = value
                                            self.output.value_namespace = name_space
                                            self.output.value_namespace_prefix = name_space_prefix
                                        if(value_path == "output-xr"):
                                            self.output_xr = value
                                            self.output_xr.value_namespace = name_space
                                            self.output_xr.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.output:
                                        if (c.has_data()):
                                            return True
                                    return self.cmd.is_set

                                def has_operation(self):
                                    for c in self.output:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.cmd.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "command" + "[cmd='" + self.cmd.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.cmd.is_set or self.cmd.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.cmd.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "output"):
                                        for c in self.output:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.output.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "output" or name == "cmd"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "cmd"):
                                        self.cmd = value
                                        self.cmd.value_namespace = name_space
                                        self.cmd.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.command:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.command:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "commands" + path_buffer

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

                                if (child_yang_name == "command"):
                                    for c in self.command:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.command.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "command"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.unit.is_set or
                                (self.commands is not None and self.commands.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.unit.yfilter != YFilter.not_set or
                                (self.commands is not None and self.commands.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "diag-shell-unit" + "[unit='" + self.unit.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.unit.is_set or self.unit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unit.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "commands"):
                                if (self.commands is None):
                                    self.commands = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands()
                                    self.commands.parent = self
                                    self._children_name_map["commands"] = "commands"
                                return self.commands

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "commands" or name == "unit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "unit"):
                                self.unit = value
                                self.unit.value_namespace = name_space
                                self.unit.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.diag_shell_unit:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.diag_shell_unit:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "diag-shell-units" + path_buffer

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

                        if (child_yang_name == "diag-shell-unit"):
                            for c in self.diag_shell_unit:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.diag_shell_unit.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "diag-shell-unit"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.diag_shell_units is not None and self.diag_shell_units.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.diag_shell_units is not None and self.diag_shell_units.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "diag-shell" + path_buffer

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

                    if (child_yang_name == "diag-shell-units"):
                        if (self.diag_shell_units is None):
                            self.diag_shell_units = Fia.Nodes.Node.DiagShell.DiagShellUnits()
                            self.diag_shell_units.parent = self
                            self._children_name_map["diag_shell_units"] = "diag-shell-units"
                        return self.diag_shell_units

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "diag-shell-units"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OirHistory(Entity):
                """
                FIA operational data of oir history
                
                .. attribute:: flags
                
                	Flag table for history
                	**type**\:   :py:class:`Flags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.OirHistory, self).__init__()

                    self.yang_name = "oir-history"
                    self.yang_parent_name = "node"

                    self.flags = Fia.Nodes.Node.OirHistory.Flags()
                    self.flags.parent = self
                    self._children_name_map["flags"] = "flags"
                    self._children_yang_names.add("flags")


                class Flags(Entity):
                    """
                    Flag table for history
                    
                    .. attribute:: flag
                    
                    	Flag value for physical location
                    	**type**\: list of    :py:class:`Flag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.OirHistory.Flags, self).__init__()

                        self.yang_name = "flags"
                        self.yang_parent_name = "oir-history"

                        self.flag = YList(self)

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
                                    super(Fia.Nodes.Node.OirHistory.Flags, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.OirHistory.Flags, self).__setattr__(name, value)


                    class Flag(Entity):
                        """
                        Flag value for physical location
                        
                        .. attribute:: flag  <key>
                        
                        	Flag value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: slots
                        
                        	Slot table for history
                        	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.OirHistory.Flags.Flag, self).__init__()

                            self.yang_name = "flag"
                            self.yang_parent_name = "flags"

                            self.flag = YLeaf(YType.int32, "flag")

                            self.slots = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots()
                            self.slots.parent = self
                            self._children_name_map["slots"] = "slots"
                            self._children_yang_names.add("slots")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("flag") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag, self).__setattr__(name, value)


                        class Slots(Entity):
                            """
                            Slot table for history
                            
                            .. attribute:: slot
                            
                            	Slot number for getting history
                            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots, self).__init__()

                                self.yang_name = "slots"
                                self.yang_parent_name = "flag"

                                self.slot = YList(self)

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
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots, self).__setattr__(name, value)


                            class Slot(Entity):
                                """
                                Slot number for getting history
                                
                                .. attribute:: slot  <key>
                                
                                	Slot number
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: asic_avail_mask
                                
                                	asic avail mask
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                                
                                	asic oper notify to fsdb pending bmap
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: board_rev_id
                                
                                	board rev id
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: card_avail_mask
                                
                                	card avail mask
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: card_info
                                
                                	card info
                                	**type**\: list of    :py:class:`CardInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo>`
                                
                                .. attribute:: coeff_major_rev
                                
                                	coeff major rev
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: coeff_minor_rev
                                
                                	coeff minor rev
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: device_info
                                
                                	device info
                                	**type**\: list of    :py:class:`DeviceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo>`
                                
                                .. attribute:: drv_version
                                
                                	drv version
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: drvr_current_startup_timestamp
                                
                                	drvr current startup timestamp
                                	**type**\:  str
                                
                                .. attribute:: drvr_initial_startup_timestamp
                                
                                	drvr initial startup timestamp
                                	**type**\:  str
                                
                                .. attribute:: exp_asic_avail_mask
                                
                                	exp asic avail mask
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fabric_mode
                                
                                	fabric mode
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: fc_mode
                                
                                	FC Mode
                                	**type**\:   :py:class:`FcMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.FcMode>`
                                
                                .. attribute:: fgid_conn_active
                                
                                	fgid conn active
                                	**type**\:  bool
                                
                                .. attribute:: fgid_reg_active
                                
                                	fgid reg active
                                	**type**\:  bool
                                
                                .. attribute:: fsdb_conn_active
                                
                                	fsdb conn active
                                	**type**\:  bool
                                
                                .. attribute:: fsdb_reg_active
                                
                                	fsdb reg active
                                	**type**\:  bool
                                
                                .. attribute:: functional_role
                                
                                	functional role
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: is_cih_registered
                                
                                	is cih registered
                                	**type**\:  bool
                                
                                .. attribute:: is_driver_ready
                                
                                	is driver ready
                                	**type**\:  bool
                                
                                .. attribute:: is_fgid_download_completed
                                
                                	is fgid download completed
                                	**type**\:  bool
                                
                                .. attribute:: is_fgid_download_in_progress
                                
                                	is fgid download in progress
                                	**type**\:  bool
                                
                                .. attribute:: is_full_fgid_download_req
                                
                                	is full fgid download req
                                	**type**\:  bool
                                
                                .. attribute:: is_gaspp_registered
                                
                                	is gaspp registered
                                	**type**\:  bool
                                
                                .. attribute:: issu_abort_rcvd
                                
                                	issu abort rcvd
                                	**type**\:  bool
                                
                                .. attribute:: issu_abort_sent
                                
                                	issu abort sent
                                	**type**\:  bool
                                
                                .. attribute:: issu_mgr_conn_active
                                
                                	issu mgr conn active
                                	**type**\:  bool
                                
                                .. attribute:: issu_mgr_reg_active
                                
                                	issu mgr reg active
                                	**type**\:  bool
                                
                                .. attribute:: issu_ready_ntfy_pending
                                
                                	issu ready ntfy pending
                                	**type**\:  bool
                                
                                .. attribute:: issu_role
                                
                                	issu role
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: node_id
                                
                                	node id
                                	**type**\:  str
                                
                                .. attribute:: num_cm_conn_reqs
                                
                                	num cm conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fgid_conn_reqs
                                
                                	num fgid conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fsdb_conn_reqs
                                
                                	num fsdb conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fstats_conn_reqs
                                
                                	num fstats conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_intf_ports
                                
                                	num intf ports
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: num_issu_mgr_conn_reqs
                                
                                	num issu mgr conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_peer_fia_conn_reqs
                                
                                	num peer fia conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_pm_conn_reqs
                                
                                	num pm conn reqs
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rack_num
                                
                                	rack num
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rack_type
                                
                                	rack type
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: respawn_count
                                
                                	respawn count
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: total_asics
                                
                                	total asics
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: uc_weight
                                
                                	uc weight
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ucmc_ratio
                                
                                	ucmc ratio
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, self).__init__()

                                    self.yang_name = "slot"
                                    self.yang_parent_name = "slots"

                                    self.slot = YLeaf(YType.int32, "slot")

                                    self.asic_avail_mask = YLeaf(YType.uint64, "asic-avail-mask")

                                    self.asic_oper_notify_to_fsdb_pending_bmap = YLeaf(YType.uint64, "asic-oper-notify-to-fsdb-pending-bmap")

                                    self.board_rev_id = YLeaf(YType.uint32, "board-rev-id")

                                    self.card_avail_mask = YLeaf(YType.uint32, "card-avail-mask")

                                    self.coeff_major_rev = YLeaf(YType.uint32, "coeff-major-rev")

                                    self.coeff_minor_rev = YLeaf(YType.uint32, "coeff-minor-rev")

                                    self.drv_version = YLeaf(YType.uint32, "drv-version")

                                    self.drvr_current_startup_timestamp = YLeaf(YType.str, "drvr-current-startup-timestamp")

                                    self.drvr_initial_startup_timestamp = YLeaf(YType.str, "drvr-initial-startup-timestamp")

                                    self.exp_asic_avail_mask = YLeaf(YType.uint64, "exp-asic-avail-mask")

                                    self.fabric_mode = YLeaf(YType.uint8, "fabric-mode")

                                    self.fc_mode = YLeaf(YType.enumeration, "fc-mode")

                                    self.fgid_conn_active = YLeaf(YType.boolean, "fgid-conn-active")

                                    self.fgid_reg_active = YLeaf(YType.boolean, "fgid-reg-active")

                                    self.fsdb_conn_active = YLeaf(YType.boolean, "fsdb-conn-active")

                                    self.fsdb_reg_active = YLeaf(YType.boolean, "fsdb-reg-active")

                                    self.functional_role = YLeaf(YType.uint8, "functional-role")

                                    self.is_cih_registered = YLeaf(YType.boolean, "is-cih-registered")

                                    self.is_driver_ready = YLeaf(YType.boolean, "is-driver-ready")

                                    self.is_fgid_download_completed = YLeaf(YType.boolean, "is-fgid-download-completed")

                                    self.is_fgid_download_in_progress = YLeaf(YType.boolean, "is-fgid-download-in-progress")

                                    self.is_full_fgid_download_req = YLeaf(YType.boolean, "is-full-fgid-download-req")

                                    self.is_gaspp_registered = YLeaf(YType.boolean, "is-gaspp-registered")

                                    self.issu_abort_rcvd = YLeaf(YType.boolean, "issu-abort-rcvd")

                                    self.issu_abort_sent = YLeaf(YType.boolean, "issu-abort-sent")

                                    self.issu_mgr_conn_active = YLeaf(YType.boolean, "issu-mgr-conn-active")

                                    self.issu_mgr_reg_active = YLeaf(YType.boolean, "issu-mgr-reg-active")

                                    self.issu_ready_ntfy_pending = YLeaf(YType.boolean, "issu-ready-ntfy-pending")

                                    self.issu_role = YLeaf(YType.uint8, "issu-role")

                                    self.node_id = YLeaf(YType.str, "node-id")

                                    self.num_cm_conn_reqs = YLeaf(YType.uint8, "num-cm-conn-reqs")

                                    self.num_fgid_conn_reqs = YLeaf(YType.uint8, "num-fgid-conn-reqs")

                                    self.num_fsdb_conn_reqs = YLeaf(YType.uint8, "num-fsdb-conn-reqs")

                                    self.num_fstats_conn_reqs = YLeaf(YType.uint8, "num-fstats-conn-reqs")

                                    self.num_intf_ports = YLeaf(YType.uint32, "num-intf-ports")

                                    self.num_issu_mgr_conn_reqs = YLeaf(YType.uint8, "num-issu-mgr-conn-reqs")

                                    self.num_peer_fia_conn_reqs = YLeaf(YType.uint8, "num-peer-fia-conn-reqs")

                                    self.num_pm_conn_reqs = YLeaf(YType.uint8, "num-pm-conn-reqs")

                                    self.rack_num = YLeaf(YType.uint8, "rack-num")

                                    self.rack_type = YLeaf(YType.int32, "rack-type")

                                    self.respawn_count = YLeaf(YType.uint8, "respawn-count")

                                    self.total_asics = YLeaf(YType.uint8, "total-asics")

                                    self.uc_weight = YLeaf(YType.uint8, "uc-weight")

                                    self.ucmc_ratio = YLeaf(YType.uint32, "ucmc-ratio")

                                    self.card_info = YList(self)
                                    self.device_info = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("slot",
                                                    "asic_avail_mask",
                                                    "asic_oper_notify_to_fsdb_pending_bmap",
                                                    "board_rev_id",
                                                    "card_avail_mask",
                                                    "coeff_major_rev",
                                                    "coeff_minor_rev",
                                                    "drv_version",
                                                    "drvr_current_startup_timestamp",
                                                    "drvr_initial_startup_timestamp",
                                                    "exp_asic_avail_mask",
                                                    "fabric_mode",
                                                    "fc_mode",
                                                    "fgid_conn_active",
                                                    "fgid_reg_active",
                                                    "fsdb_conn_active",
                                                    "fsdb_reg_active",
                                                    "functional_role",
                                                    "is_cih_registered",
                                                    "is_driver_ready",
                                                    "is_fgid_download_completed",
                                                    "is_fgid_download_in_progress",
                                                    "is_full_fgid_download_req",
                                                    "is_gaspp_registered",
                                                    "issu_abort_rcvd",
                                                    "issu_abort_sent",
                                                    "issu_mgr_conn_active",
                                                    "issu_mgr_reg_active",
                                                    "issu_ready_ntfy_pending",
                                                    "issu_role",
                                                    "node_id",
                                                    "num_cm_conn_reqs",
                                                    "num_fgid_conn_reqs",
                                                    "num_fsdb_conn_reqs",
                                                    "num_fstats_conn_reqs",
                                                    "num_intf_ports",
                                                    "num_issu_mgr_conn_reqs",
                                                    "num_peer_fia_conn_reqs",
                                                    "num_pm_conn_reqs",
                                                    "rack_num",
                                                    "rack_type",
                                                    "respawn_count",
                                                    "total_asics",
                                                    "uc_weight",
                                                    "ucmc_ratio") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot, self).__setattr__(name, value)


                                class DeviceInfo(Entity):
                                    """
                                    device info
                                    
                                    .. attribute:: admin_state
                                    
                                    	Admin State
                                    	**type**\:   :py:class:`AdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AdminState>`
                                    
                                    .. attribute:: asic_id
                                    
                                    	asic id
                                    	**type**\:   :py:class:`AsicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId>`
                                    
                                    .. attribute:: asic_state
                                    
                                    	Asic State
                                    	**type**\:   :py:class:`AsicAccessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicAccessState>`
                                    
                                    .. attribute:: fapid
                                    
                                    	fapid
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hotplug_event
                                    
                                    	hotplug event
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_valid
                                    
                                    	is valid
                                    	**type**\:  bool
                                    
                                    .. attribute:: last_init_cause
                                    
                                    	last init cause
                                    	**type**\:   :py:class:`AsicInitMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicInitMethod>`
                                    
                                    .. attribute:: local_switch_state
                                    
                                    	local switch state
                                    	**type**\:  bool
                                    
                                    .. attribute:: num_hard_resets
                                    
                                    	num hard resets
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_pon_resets
                                    
                                    	num pon resets
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: oper_state
                                    
                                    	Oper State
                                    	**type**\:   :py:class:`AsicOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.AsicOperState>`
                                    
                                    .. attribute:: slice_state
                                    
                                    	Slice State
                                    	**type**\:   :py:class:`SliceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.SliceState>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, self).__init__()

                                        self.yang_name = "device-info"
                                        self.yang_parent_name = "slot"

                                        self.admin_state = YLeaf(YType.enumeration, "admin-state")

                                        self.asic_state = YLeaf(YType.enumeration, "asic-state")

                                        self.fapid = YLeaf(YType.uint32, "fapid")

                                        self.hotplug_event = YLeaf(YType.uint32, "hotplug-event")

                                        self.is_valid = YLeaf(YType.boolean, "is-valid")

                                        self.last_init_cause = YLeaf(YType.enumeration, "last-init-cause")

                                        self.local_switch_state = YLeaf(YType.boolean, "local-switch-state")

                                        self.num_hard_resets = YLeaf(YType.uint32, "num-hard-resets")

                                        self.num_pon_resets = YLeaf(YType.uint32, "num-pon-resets")

                                        self.oper_state = YLeaf(YType.enumeration, "oper-state")

                                        self.slice_state = YLeaf(YType.enumeration, "slice-state")

                                        self.asic_id = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId()
                                        self.asic_id.parent = self
                                        self._children_name_map["asic_id"] = "asic-id"
                                        self._children_yang_names.add("asic-id")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("admin_state",
                                                        "asic_state",
                                                        "fapid",
                                                        "hotplug_event",
                                                        "is_valid",
                                                        "last_init_cause",
                                                        "local_switch_state",
                                                        "num_hard_resets",
                                                        "num_pon_resets",
                                                        "oper_state",
                                                        "slice_state") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo, self).__setattr__(name, value)


                                    class AsicId(Entity):
                                        """
                                        asic id
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_type
                                        
                                        	Asic Type
                                        	**type**\:   :py:class:`Asic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Asic>`
                                        
                                        .. attribute:: rack_num
                                        
                                        	rack num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: rack_type
                                        
                                        	Rack Type
                                        	**type**\:   :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Rack>`
                                        
                                        .. attribute:: slot_num
                                        
                                        	slot num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, self).__init__()

                                            self.yang_name = "asic-id"
                                            self.yang_parent_name = "device-info"

                                            self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                            self.asic_type = YLeaf(YType.enumeration, "asic-type")

                                            self.rack_num = YLeaf(YType.uint32, "rack-num")

                                            self.rack_type = YLeaf(YType.enumeration, "rack-type")

                                            self.slot_num = YLeaf(YType.uint32, "slot-num")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("asic_instance",
                                                            "asic_type",
                                                            "rack_num",
                                                            "rack_type",
                                                            "slot_num") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.asic_instance.is_set or
                                                self.asic_type.is_set or
                                                self.rack_num.is_set or
                                                self.rack_type.is_set or
                                                self.slot_num.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.asic_instance.yfilter != YFilter.not_set or
                                                self.asic_type.yfilter != YFilter.not_set or
                                                self.rack_num.yfilter != YFilter.not_set or
                                                self.rack_type.yfilter != YFilter.not_set or
                                                self.slot_num.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "asic-id" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                            if (self.asic_type.is_set or self.asic_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.asic_type.get_name_leafdata())
                                            if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rack_num.get_name_leafdata())
                                            if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rack_type.get_name_leafdata())
                                            if (self.slot_num.is_set or self.slot_num.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.slot_num.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "asic-instance" or name == "asic-type" or name == "rack-num" or name == "rack-type" or name == "slot-num"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "asic-instance"):
                                                self.asic_instance = value
                                                self.asic_instance.value_namespace = name_space
                                                self.asic_instance.value_namespace_prefix = name_space_prefix
                                            if(value_path == "asic-type"):
                                                self.asic_type = value
                                                self.asic_type.value_namespace = name_space
                                                self.asic_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rack-num"):
                                                self.rack_num = value
                                                self.rack_num.value_namespace = name_space
                                                self.rack_num.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rack-type"):
                                                self.rack_type = value
                                                self.rack_type.value_namespace = name_space
                                                self.rack_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "slot-num"):
                                                self.slot_num = value
                                                self.slot_num.value_namespace = name_space
                                                self.slot_num.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.admin_state.is_set or
                                            self.asic_state.is_set or
                                            self.fapid.is_set or
                                            self.hotplug_event.is_set or
                                            self.is_valid.is_set or
                                            self.last_init_cause.is_set or
                                            self.local_switch_state.is_set or
                                            self.num_hard_resets.is_set or
                                            self.num_pon_resets.is_set or
                                            self.oper_state.is_set or
                                            self.slice_state.is_set or
                                            (self.asic_id is not None and self.asic_id.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.admin_state.yfilter != YFilter.not_set or
                                            self.asic_state.yfilter != YFilter.not_set or
                                            self.fapid.yfilter != YFilter.not_set or
                                            self.hotplug_event.yfilter != YFilter.not_set or
                                            self.is_valid.yfilter != YFilter.not_set or
                                            self.last_init_cause.yfilter != YFilter.not_set or
                                            self.local_switch_state.yfilter != YFilter.not_set or
                                            self.num_hard_resets.yfilter != YFilter.not_set or
                                            self.num_pon_resets.yfilter != YFilter.not_set or
                                            self.oper_state.yfilter != YFilter.not_set or
                                            self.slice_state.yfilter != YFilter.not_set or
                                            (self.asic_id is not None and self.asic_id.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "device-info" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.admin_state.get_name_leafdata())
                                        if (self.asic_state.is_set or self.asic_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.asic_state.get_name_leafdata())
                                        if (self.fapid.is_set or self.fapid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.fapid.get_name_leafdata())
                                        if (self.hotplug_event.is_set or self.hotplug_event.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hotplug_event.get_name_leafdata())
                                        if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_valid.get_name_leafdata())
                                        if (self.last_init_cause.is_set or self.last_init_cause.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_init_cause.get_name_leafdata())
                                        if (self.local_switch_state.is_set or self.local_switch_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.local_switch_state.get_name_leafdata())
                                        if (self.num_hard_resets.is_set or self.num_hard_resets.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_hard_resets.get_name_leafdata())
                                        if (self.num_pon_resets.is_set or self.num_pon_resets.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_pon_resets.get_name_leafdata())
                                        if (self.oper_state.is_set or self.oper_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.oper_state.get_name_leafdata())
                                        if (self.slice_state.is_set or self.slice_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.slice_state.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "asic-id"):
                                            if (self.asic_id is None):
                                                self.asic_id = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId()
                                                self.asic_id.parent = self
                                                self._children_name_map["asic_id"] = "asic-id"
                                            return self.asic_id

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "asic-id" or name == "admin-state" or name == "asic-state" or name == "fapid" or name == "hotplug-event" or name == "is-valid" or name == "last-init-cause" or name == "local-switch-state" or name == "num-hard-resets" or name == "num-pon-resets" or name == "oper-state" or name == "slice-state"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "admin-state"):
                                            self.admin_state = value
                                            self.admin_state.value_namespace = name_space
                                            self.admin_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "asic-state"):
                                            self.asic_state = value
                                            self.asic_state.value_namespace = name_space
                                            self.asic_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "fapid"):
                                            self.fapid = value
                                            self.fapid.value_namespace = name_space
                                            self.fapid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hotplug-event"):
                                            self.hotplug_event = value
                                            self.hotplug_event.value_namespace = name_space
                                            self.hotplug_event.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-valid"):
                                            self.is_valid = value
                                            self.is_valid.value_namespace = name_space
                                            self.is_valid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-init-cause"):
                                            self.last_init_cause = value
                                            self.last_init_cause.value_namespace = name_space
                                            self.last_init_cause.value_namespace_prefix = name_space_prefix
                                        if(value_path == "local-switch-state"):
                                            self.local_switch_state = value
                                            self.local_switch_state.value_namespace = name_space
                                            self.local_switch_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-hard-resets"):
                                            self.num_hard_resets = value
                                            self.num_hard_resets.value_namespace = name_space
                                            self.num_hard_resets.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-pon-resets"):
                                            self.num_pon_resets = value
                                            self.num_pon_resets.value_namespace = name_space
                                            self.num_pon_resets.value_namespace_prefix = name_space_prefix
                                        if(value_path == "oper-state"):
                                            self.oper_state = value
                                            self.oper_state.value_namespace = name_space
                                            self.oper_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "slice-state"):
                                            self.slice_state = value
                                            self.slice_state.value_namespace = name_space
                                            self.slice_state.value_namespace_prefix = name_space_prefix


                                class CardInfo(Entity):
                                    """
                                    card info
                                    
                                    .. attribute:: card_flag
                                    
                                    	card flag
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_name
                                    
                                    	card name
                                    	**type**\:  str
                                    
                                    .. attribute:: card_state
                                    
                                    	card state
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: card_type
                                    
                                    	card type
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: cxp_avail_bitmap
                                    
                                    	cxp avail bitmap
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: evt_flag
                                    
                                    	evt flag
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: exp_num_asics
                                    
                                    	exp num asics
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: exp_num_asics_per_fsdb
                                    
                                    	exp num asics per fsdb
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: instance
                                    
                                    	instance
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: is_powered
                                    
                                    	is powered
                                    	**type**\:  bool
                                    
                                    .. attribute:: num_cos_per_port
                                    
                                    	num cos per port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: num_ilkns_per_asic
                                    
                                    	num ilkns per asic
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_local_ports_per_ilkn
                                    
                                    	num local ports per ilkn
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: oir_circular_buffer
                                    
                                    	oir circular buffer
                                    	**type**\:   :py:class:`OirCircularBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer>`
                                    
                                    .. attribute:: reg_flag
                                    
                                    	reg flag
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: slot_no
                                    
                                    	slot no
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, self).__init__()

                                        self.yang_name = "card-info"
                                        self.yang_parent_name = "slot"

                                        self.card_flag = YLeaf(YType.int32, "card-flag")

                                        self.card_name = YLeaf(YType.str, "card-name")

                                        self.card_state = YLeaf(YType.uint8, "card-state")

                                        self.card_type = YLeaf(YType.int32, "card-type")

                                        self.cxp_avail_bitmap = YLeaf(YType.uint64, "cxp-avail-bitmap")

                                        self.evt_flag = YLeaf(YType.int32, "evt-flag")

                                        self.exp_num_asics = YLeaf(YType.uint32, "exp-num-asics")

                                        self.exp_num_asics_per_fsdb = YLeaf(YType.uint32, "exp-num-asics-per-fsdb")

                                        self.instance = YLeaf(YType.int32, "instance")

                                        self.is_powered = YLeaf(YType.boolean, "is-powered")

                                        self.num_cos_per_port = YLeaf(YType.uint8, "num-cos-per-port")

                                        self.num_ilkns_per_asic = YLeaf(YType.uint32, "num-ilkns-per-asic")

                                        self.num_local_ports_per_ilkn = YLeaf(YType.uint32, "num-local-ports-per-ilkn")

                                        self.reg_flag = YLeaf(YType.int32, "reg-flag")

                                        self.slot_no = YLeaf(YType.int32, "slot-no")

                                        self.oir_circular_buffer = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer()
                                        self.oir_circular_buffer.parent = self
                                        self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                                        self._children_yang_names.add("oir-circular-buffer")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("card_flag",
                                                        "card_name",
                                                        "card_state",
                                                        "card_type",
                                                        "cxp_avail_bitmap",
                                                        "evt_flag",
                                                        "exp_num_asics",
                                                        "exp_num_asics_per_fsdb",
                                                        "instance",
                                                        "is_powered",
                                                        "num_cos_per_port",
                                                        "num_ilkns_per_asic",
                                                        "num_local_ports_per_ilkn",
                                                        "reg_flag",
                                                        "slot_no") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo, self).__setattr__(name, value)


                                    class OirCircularBuffer(Entity):
                                        """
                                        oir circular buffer
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: end
                                        
                                        	end
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: fia_oir_info
                                        
                                        	fia oir info
                                        	**type**\: list of    :py:class:`FiaOirInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo>`
                                        
                                        .. attribute:: start
                                        
                                        	start
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, self).__init__()

                                            self.yang_name = "oir-circular-buffer"
                                            self.yang_parent_name = "card-info"

                                            self.count = YLeaf(YType.int32, "count")

                                            self.end = YLeaf(YType.int32, "end")

                                            self.start = YLeaf(YType.int32, "start")

                                            self.fia_oir_info = YList(self)

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
                                                            "end",
                                                            "start") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer, self).__setattr__(name, value)


                                        class FiaOirInfo(Entity):
                                            """
                                            fia oir info
                                            
                                            .. attribute:: card_flag
                                            
                                            	card flag
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_type
                                            
                                            	card type
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: cur_card_state
                                            
                                            	cur card state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: evt_flag
                                            
                                            	evt flag
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: instance
                                            
                                            	instance
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: rack_num
                                            
                                            	rack num
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: reg_flag
                                            
                                            	reg flag
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, self).__init__()

                                                self.yang_name = "fia-oir-info"
                                                self.yang_parent_name = "oir-circular-buffer"

                                                self.card_flag = YLeaf(YType.int32, "card-flag")

                                                self.card_type = YLeaf(YType.int32, "card-type")

                                                self.cur_card_state = YLeaf(YType.int32, "cur-card-state")

                                                self.evt_flag = YLeaf(YType.int32, "evt-flag")

                                                self.instance = YLeaf(YType.int32, "instance")

                                                self.rack_num = YLeaf(YType.int32, "rack-num")

                                                self.reg_flag = YLeaf(YType.int32, "reg-flag")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("card_flag",
                                                                "card_type",
                                                                "cur_card_state",
                                                                "evt_flag",
                                                                "instance",
                                                                "rack_num",
                                                                "reg_flag") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.card_flag.is_set or
                                                    self.card_type.is_set or
                                                    self.cur_card_state.is_set or
                                                    self.evt_flag.is_set or
                                                    self.instance.is_set or
                                                    self.rack_num.is_set or
                                                    self.reg_flag.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.card_flag.yfilter != YFilter.not_set or
                                                    self.card_type.yfilter != YFilter.not_set or
                                                    self.cur_card_state.yfilter != YFilter.not_set or
                                                    self.evt_flag.yfilter != YFilter.not_set or
                                                    self.instance.yfilter != YFilter.not_set or
                                                    self.rack_num.yfilter != YFilter.not_set or
                                                    self.reg_flag.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "fia-oir-info" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.card_flag.is_set or self.card_flag.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.card_flag.get_name_leafdata())
                                                if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.card_type.get_name_leafdata())
                                                if (self.cur_card_state.is_set or self.cur_card_state.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.cur_card_state.get_name_leafdata())
                                                if (self.evt_flag.is_set or self.evt_flag.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.evt_flag.get_name_leafdata())
                                                if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.instance.get_name_leafdata())
                                                if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.rack_num.get_name_leafdata())
                                                if (self.reg_flag.is_set or self.reg_flag.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.reg_flag.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "card-flag" or name == "card-type" or name == "cur-card-state" or name == "evt-flag" or name == "instance" or name == "rack-num" or name == "reg-flag"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "card-flag"):
                                                    self.card_flag = value
                                                    self.card_flag.value_namespace = name_space
                                                    self.card_flag.value_namespace_prefix = name_space_prefix
                                                if(value_path == "card-type"):
                                                    self.card_type = value
                                                    self.card_type.value_namespace = name_space
                                                    self.card_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "cur-card-state"):
                                                    self.cur_card_state = value
                                                    self.cur_card_state.value_namespace = name_space
                                                    self.cur_card_state.value_namespace_prefix = name_space_prefix
                                                if(value_path == "evt-flag"):
                                                    self.evt_flag = value
                                                    self.evt_flag.value_namespace = name_space
                                                    self.evt_flag.value_namespace_prefix = name_space_prefix
                                                if(value_path == "instance"):
                                                    self.instance = value
                                                    self.instance.value_namespace = name_space
                                                    self.instance.value_namespace_prefix = name_space_prefix
                                                if(value_path == "rack-num"):
                                                    self.rack_num = value
                                                    self.rack_num.value_namespace = name_space
                                                    self.rack_num.value_namespace_prefix = name_space_prefix
                                                if(value_path == "reg-flag"):
                                                    self.reg_flag = value
                                                    self.reg_flag.value_namespace = name_space
                                                    self.reg_flag.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.fia_oir_info:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.count.is_set or
                                                self.end.is_set or
                                                self.start.is_set)

                                        def has_operation(self):
                                            for c in self.fia_oir_info:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.count.yfilter != YFilter.not_set or
                                                self.end.yfilter != YFilter.not_set or
                                                self.start.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "oir-circular-buffer" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.count.get_name_leafdata())
                                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.end.get_name_leafdata())
                                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.start.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "fia-oir-info"):
                                                for c in self.fia_oir_info:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.fia_oir_info.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "fia-oir-info" or name == "count" or name == "end" or name == "start"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "count"):
                                                self.count = value
                                                self.count.value_namespace = name_space
                                                self.count.value_namespace_prefix = name_space_prefix
                                            if(value_path == "end"):
                                                self.end = value
                                                self.end.value_namespace = name_space
                                                self.end.value_namespace_prefix = name_space_prefix
                                            if(value_path == "start"):
                                                self.start = value
                                                self.start.value_namespace = name_space
                                                self.start.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.card_flag.is_set or
                                            self.card_name.is_set or
                                            self.card_state.is_set or
                                            self.card_type.is_set or
                                            self.cxp_avail_bitmap.is_set or
                                            self.evt_flag.is_set or
                                            self.exp_num_asics.is_set or
                                            self.exp_num_asics_per_fsdb.is_set or
                                            self.instance.is_set or
                                            self.is_powered.is_set or
                                            self.num_cos_per_port.is_set or
                                            self.num_ilkns_per_asic.is_set or
                                            self.num_local_ports_per_ilkn.is_set or
                                            self.reg_flag.is_set or
                                            self.slot_no.is_set or
                                            (self.oir_circular_buffer is not None and self.oir_circular_buffer.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.card_flag.yfilter != YFilter.not_set or
                                            self.card_name.yfilter != YFilter.not_set or
                                            self.card_state.yfilter != YFilter.not_set or
                                            self.card_type.yfilter != YFilter.not_set or
                                            self.cxp_avail_bitmap.yfilter != YFilter.not_set or
                                            self.evt_flag.yfilter != YFilter.not_set or
                                            self.exp_num_asics.yfilter != YFilter.not_set or
                                            self.exp_num_asics_per_fsdb.yfilter != YFilter.not_set or
                                            self.instance.yfilter != YFilter.not_set or
                                            self.is_powered.yfilter != YFilter.not_set or
                                            self.num_cos_per_port.yfilter != YFilter.not_set or
                                            self.num_ilkns_per_asic.yfilter != YFilter.not_set or
                                            self.num_local_ports_per_ilkn.yfilter != YFilter.not_set or
                                            self.reg_flag.yfilter != YFilter.not_set or
                                            self.slot_no.yfilter != YFilter.not_set or
                                            (self.oir_circular_buffer is not None and self.oir_circular_buffer.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "card-info" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.card_flag.is_set or self.card_flag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.card_flag.get_name_leafdata())
                                        if (self.card_name.is_set or self.card_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.card_name.get_name_leafdata())
                                        if (self.card_state.is_set or self.card_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.card_state.get_name_leafdata())
                                        if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.card_type.get_name_leafdata())
                                        if (self.cxp_avail_bitmap.is_set or self.cxp_avail_bitmap.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.cxp_avail_bitmap.get_name_leafdata())
                                        if (self.evt_flag.is_set or self.evt_flag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.evt_flag.get_name_leafdata())
                                        if (self.exp_num_asics.is_set or self.exp_num_asics.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.exp_num_asics.get_name_leafdata())
                                        if (self.exp_num_asics_per_fsdb.is_set or self.exp_num_asics_per_fsdb.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.exp_num_asics_per_fsdb.get_name_leafdata())
                                        if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.instance.get_name_leafdata())
                                        if (self.is_powered.is_set or self.is_powered.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_powered.get_name_leafdata())
                                        if (self.num_cos_per_port.is_set or self.num_cos_per_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_cos_per_port.get_name_leafdata())
                                        if (self.num_ilkns_per_asic.is_set or self.num_ilkns_per_asic.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_ilkns_per_asic.get_name_leafdata())
                                        if (self.num_local_ports_per_ilkn.is_set or self.num_local_ports_per_ilkn.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_local_ports_per_ilkn.get_name_leafdata())
                                        if (self.reg_flag.is_set or self.reg_flag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.reg_flag.get_name_leafdata())
                                        if (self.slot_no.is_set or self.slot_no.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.slot_no.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "oir-circular-buffer"):
                                            if (self.oir_circular_buffer is None):
                                                self.oir_circular_buffer = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer()
                                                self.oir_circular_buffer.parent = self
                                                self._children_name_map["oir_circular_buffer"] = "oir-circular-buffer"
                                            return self.oir_circular_buffer

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "oir-circular-buffer" or name == "card-flag" or name == "card-name" or name == "card-state" or name == "card-type" or name == "cxp-avail-bitmap" or name == "evt-flag" or name == "exp-num-asics" or name == "exp-num-asics-per-fsdb" or name == "instance" or name == "is-powered" or name == "num-cos-per-port" or name == "num-ilkns-per-asic" or name == "num-local-ports-per-ilkn" or name == "reg-flag" or name == "slot-no"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "card-flag"):
                                            self.card_flag = value
                                            self.card_flag.value_namespace = name_space
                                            self.card_flag.value_namespace_prefix = name_space_prefix
                                        if(value_path == "card-name"):
                                            self.card_name = value
                                            self.card_name.value_namespace = name_space
                                            self.card_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "card-state"):
                                            self.card_state = value
                                            self.card_state.value_namespace = name_space
                                            self.card_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "card-type"):
                                            self.card_type = value
                                            self.card_type.value_namespace = name_space
                                            self.card_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "cxp-avail-bitmap"):
                                            self.cxp_avail_bitmap = value
                                            self.cxp_avail_bitmap.value_namespace = name_space
                                            self.cxp_avail_bitmap.value_namespace_prefix = name_space_prefix
                                        if(value_path == "evt-flag"):
                                            self.evt_flag = value
                                            self.evt_flag.value_namespace = name_space
                                            self.evt_flag.value_namespace_prefix = name_space_prefix
                                        if(value_path == "exp-num-asics"):
                                            self.exp_num_asics = value
                                            self.exp_num_asics.value_namespace = name_space
                                            self.exp_num_asics.value_namespace_prefix = name_space_prefix
                                        if(value_path == "exp-num-asics-per-fsdb"):
                                            self.exp_num_asics_per_fsdb = value
                                            self.exp_num_asics_per_fsdb.value_namespace = name_space
                                            self.exp_num_asics_per_fsdb.value_namespace_prefix = name_space_prefix
                                        if(value_path == "instance"):
                                            self.instance = value
                                            self.instance.value_namespace = name_space
                                            self.instance.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-powered"):
                                            self.is_powered = value
                                            self.is_powered.value_namespace = name_space
                                            self.is_powered.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-cos-per-port"):
                                            self.num_cos_per_port = value
                                            self.num_cos_per_port.value_namespace = name_space
                                            self.num_cos_per_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-ilkns-per-asic"):
                                            self.num_ilkns_per_asic = value
                                            self.num_ilkns_per_asic.value_namespace = name_space
                                            self.num_ilkns_per_asic.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-local-ports-per-ilkn"):
                                            self.num_local_ports_per_ilkn = value
                                            self.num_local_ports_per_ilkn.value_namespace = name_space
                                            self.num_local_ports_per_ilkn.value_namespace_prefix = name_space_prefix
                                        if(value_path == "reg-flag"):
                                            self.reg_flag = value
                                            self.reg_flag.value_namespace = name_space
                                            self.reg_flag.value_namespace_prefix = name_space_prefix
                                        if(value_path == "slot-no"):
                                            self.slot_no = value
                                            self.slot_no.value_namespace = name_space
                                            self.slot_no.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.card_info:
                                        if (c.has_data()):
                                            return True
                                    for c in self.device_info:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.slot.is_set or
                                        self.asic_avail_mask.is_set or
                                        self.asic_oper_notify_to_fsdb_pending_bmap.is_set or
                                        self.board_rev_id.is_set or
                                        self.card_avail_mask.is_set or
                                        self.coeff_major_rev.is_set or
                                        self.coeff_minor_rev.is_set or
                                        self.drv_version.is_set or
                                        self.drvr_current_startup_timestamp.is_set or
                                        self.drvr_initial_startup_timestamp.is_set or
                                        self.exp_asic_avail_mask.is_set or
                                        self.fabric_mode.is_set or
                                        self.fc_mode.is_set or
                                        self.fgid_conn_active.is_set or
                                        self.fgid_reg_active.is_set or
                                        self.fsdb_conn_active.is_set or
                                        self.fsdb_reg_active.is_set or
                                        self.functional_role.is_set or
                                        self.is_cih_registered.is_set or
                                        self.is_driver_ready.is_set or
                                        self.is_fgid_download_completed.is_set or
                                        self.is_fgid_download_in_progress.is_set or
                                        self.is_full_fgid_download_req.is_set or
                                        self.is_gaspp_registered.is_set or
                                        self.issu_abort_rcvd.is_set or
                                        self.issu_abort_sent.is_set or
                                        self.issu_mgr_conn_active.is_set or
                                        self.issu_mgr_reg_active.is_set or
                                        self.issu_ready_ntfy_pending.is_set or
                                        self.issu_role.is_set or
                                        self.node_id.is_set or
                                        self.num_cm_conn_reqs.is_set or
                                        self.num_fgid_conn_reqs.is_set or
                                        self.num_fsdb_conn_reqs.is_set or
                                        self.num_fstats_conn_reqs.is_set or
                                        self.num_intf_ports.is_set or
                                        self.num_issu_mgr_conn_reqs.is_set or
                                        self.num_peer_fia_conn_reqs.is_set or
                                        self.num_pm_conn_reqs.is_set or
                                        self.rack_num.is_set or
                                        self.rack_type.is_set or
                                        self.respawn_count.is_set or
                                        self.total_asics.is_set or
                                        self.uc_weight.is_set or
                                        self.ucmc_ratio.is_set)

                                def has_operation(self):
                                    for c in self.card_info:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.device_info:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.slot.yfilter != YFilter.not_set or
                                        self.asic_avail_mask.yfilter != YFilter.not_set or
                                        self.asic_oper_notify_to_fsdb_pending_bmap.yfilter != YFilter.not_set or
                                        self.board_rev_id.yfilter != YFilter.not_set or
                                        self.card_avail_mask.yfilter != YFilter.not_set or
                                        self.coeff_major_rev.yfilter != YFilter.not_set or
                                        self.coeff_minor_rev.yfilter != YFilter.not_set or
                                        self.drv_version.yfilter != YFilter.not_set or
                                        self.drvr_current_startup_timestamp.yfilter != YFilter.not_set or
                                        self.drvr_initial_startup_timestamp.yfilter != YFilter.not_set or
                                        self.exp_asic_avail_mask.yfilter != YFilter.not_set or
                                        self.fabric_mode.yfilter != YFilter.not_set or
                                        self.fc_mode.yfilter != YFilter.not_set or
                                        self.fgid_conn_active.yfilter != YFilter.not_set or
                                        self.fgid_reg_active.yfilter != YFilter.not_set or
                                        self.fsdb_conn_active.yfilter != YFilter.not_set or
                                        self.fsdb_reg_active.yfilter != YFilter.not_set or
                                        self.functional_role.yfilter != YFilter.not_set or
                                        self.is_cih_registered.yfilter != YFilter.not_set or
                                        self.is_driver_ready.yfilter != YFilter.not_set or
                                        self.is_fgid_download_completed.yfilter != YFilter.not_set or
                                        self.is_fgid_download_in_progress.yfilter != YFilter.not_set or
                                        self.is_full_fgid_download_req.yfilter != YFilter.not_set or
                                        self.is_gaspp_registered.yfilter != YFilter.not_set or
                                        self.issu_abort_rcvd.yfilter != YFilter.not_set or
                                        self.issu_abort_sent.yfilter != YFilter.not_set or
                                        self.issu_mgr_conn_active.yfilter != YFilter.not_set or
                                        self.issu_mgr_reg_active.yfilter != YFilter.not_set or
                                        self.issu_ready_ntfy_pending.yfilter != YFilter.not_set or
                                        self.issu_role.yfilter != YFilter.not_set or
                                        self.node_id.yfilter != YFilter.not_set or
                                        self.num_cm_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_fgid_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_fsdb_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_fstats_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_intf_ports.yfilter != YFilter.not_set or
                                        self.num_issu_mgr_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_peer_fia_conn_reqs.yfilter != YFilter.not_set or
                                        self.num_pm_conn_reqs.yfilter != YFilter.not_set or
                                        self.rack_num.yfilter != YFilter.not_set or
                                        self.rack_type.yfilter != YFilter.not_set or
                                        self.respawn_count.yfilter != YFilter.not_set or
                                        self.total_asics.yfilter != YFilter.not_set or
                                        self.uc_weight.yfilter != YFilter.not_set or
                                        self.ucmc_ratio.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.slot.get_name_leafdata())
                                    if (self.asic_avail_mask.is_set or self.asic_avail_mask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asic_avail_mask.get_name_leafdata())
                                    if (self.asic_oper_notify_to_fsdb_pending_bmap.is_set or self.asic_oper_notify_to_fsdb_pending_bmap.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asic_oper_notify_to_fsdb_pending_bmap.get_name_leafdata())
                                    if (self.board_rev_id.is_set or self.board_rev_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.board_rev_id.get_name_leafdata())
                                    if (self.card_avail_mask.is_set or self.card_avail_mask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.card_avail_mask.get_name_leafdata())
                                    if (self.coeff_major_rev.is_set or self.coeff_major_rev.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.coeff_major_rev.get_name_leafdata())
                                    if (self.coeff_minor_rev.is_set or self.coeff_minor_rev.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.coeff_minor_rev.get_name_leafdata())
                                    if (self.drv_version.is_set or self.drv_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.drv_version.get_name_leafdata())
                                    if (self.drvr_current_startup_timestamp.is_set or self.drvr_current_startup_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.drvr_current_startup_timestamp.get_name_leafdata())
                                    if (self.drvr_initial_startup_timestamp.is_set or self.drvr_initial_startup_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.drvr_initial_startup_timestamp.get_name_leafdata())
                                    if (self.exp_asic_avail_mask.is_set or self.exp_asic_avail_mask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.exp_asic_avail_mask.get_name_leafdata())
                                    if (self.fabric_mode.is_set or self.fabric_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fabric_mode.get_name_leafdata())
                                    if (self.fc_mode.is_set or self.fc_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fc_mode.get_name_leafdata())
                                    if (self.fgid_conn_active.is_set or self.fgid_conn_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fgid_conn_active.get_name_leafdata())
                                    if (self.fgid_reg_active.is_set or self.fgid_reg_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fgid_reg_active.get_name_leafdata())
                                    if (self.fsdb_conn_active.is_set or self.fsdb_conn_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fsdb_conn_active.get_name_leafdata())
                                    if (self.fsdb_reg_active.is_set or self.fsdb_reg_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fsdb_reg_active.get_name_leafdata())
                                    if (self.functional_role.is_set or self.functional_role.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.functional_role.get_name_leafdata())
                                    if (self.is_cih_registered.is_set or self.is_cih_registered.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_cih_registered.get_name_leafdata())
                                    if (self.is_driver_ready.is_set or self.is_driver_ready.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_driver_ready.get_name_leafdata())
                                    if (self.is_fgid_download_completed.is_set or self.is_fgid_download_completed.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_fgid_download_completed.get_name_leafdata())
                                    if (self.is_fgid_download_in_progress.is_set or self.is_fgid_download_in_progress.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_fgid_download_in_progress.get_name_leafdata())
                                    if (self.is_full_fgid_download_req.is_set or self.is_full_fgid_download_req.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_full_fgid_download_req.get_name_leafdata())
                                    if (self.is_gaspp_registered.is_set or self.is_gaspp_registered.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_gaspp_registered.get_name_leafdata())
                                    if (self.issu_abort_rcvd.is_set or self.issu_abort_rcvd.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_abort_rcvd.get_name_leafdata())
                                    if (self.issu_abort_sent.is_set or self.issu_abort_sent.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_abort_sent.get_name_leafdata())
                                    if (self.issu_mgr_conn_active.is_set or self.issu_mgr_conn_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_mgr_conn_active.get_name_leafdata())
                                    if (self.issu_mgr_reg_active.is_set or self.issu_mgr_reg_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_mgr_reg_active.get_name_leafdata())
                                    if (self.issu_ready_ntfy_pending.is_set or self.issu_ready_ntfy_pending.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_ready_ntfy_pending.get_name_leafdata())
                                    if (self.issu_role.is_set or self.issu_role.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.issu_role.get_name_leafdata())
                                    if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.node_id.get_name_leafdata())
                                    if (self.num_cm_conn_reqs.is_set or self.num_cm_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_cm_conn_reqs.get_name_leafdata())
                                    if (self.num_fgid_conn_reqs.is_set or self.num_fgid_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_fgid_conn_reqs.get_name_leafdata())
                                    if (self.num_fsdb_conn_reqs.is_set or self.num_fsdb_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_fsdb_conn_reqs.get_name_leafdata())
                                    if (self.num_fstats_conn_reqs.is_set or self.num_fstats_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_fstats_conn_reqs.get_name_leafdata())
                                    if (self.num_intf_ports.is_set or self.num_intf_ports.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_intf_ports.get_name_leafdata())
                                    if (self.num_issu_mgr_conn_reqs.is_set or self.num_issu_mgr_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_issu_mgr_conn_reqs.get_name_leafdata())
                                    if (self.num_peer_fia_conn_reqs.is_set or self.num_peer_fia_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_peer_fia_conn_reqs.get_name_leafdata())
                                    if (self.num_pm_conn_reqs.is_set or self.num_pm_conn_reqs.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.num_pm_conn_reqs.get_name_leafdata())
                                    if (self.rack_num.is_set or self.rack_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rack_num.get_name_leafdata())
                                    if (self.rack_type.is_set or self.rack_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rack_type.get_name_leafdata())
                                    if (self.respawn_count.is_set or self.respawn_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.respawn_count.get_name_leafdata())
                                    if (self.total_asics.is_set or self.total_asics.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.total_asics.get_name_leafdata())
                                    if (self.uc_weight.is_set or self.uc_weight.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.uc_weight.get_name_leafdata())
                                    if (self.ucmc_ratio.is_set or self.ucmc_ratio.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ucmc_ratio.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "card-info"):
                                        for c in self.card_info:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.card_info.append(c)
                                        return c

                                    if (child_yang_name == "device-info"):
                                        for c in self.device_info:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.device_info.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "card-info" or name == "device-info" or name == "slot" or name == "asic-avail-mask" or name == "asic-oper-notify-to-fsdb-pending-bmap" or name == "board-rev-id" or name == "card-avail-mask" or name == "coeff-major-rev" or name == "coeff-minor-rev" or name == "drv-version" or name == "drvr-current-startup-timestamp" or name == "drvr-initial-startup-timestamp" or name == "exp-asic-avail-mask" or name == "fabric-mode" or name == "fc-mode" or name == "fgid-conn-active" or name == "fgid-reg-active" or name == "fsdb-conn-active" or name == "fsdb-reg-active" or name == "functional-role" or name == "is-cih-registered" or name == "is-driver-ready" or name == "is-fgid-download-completed" or name == "is-fgid-download-in-progress" or name == "is-full-fgid-download-req" or name == "is-gaspp-registered" or name == "issu-abort-rcvd" or name == "issu-abort-sent" or name == "issu-mgr-conn-active" or name == "issu-mgr-reg-active" or name == "issu-ready-ntfy-pending" or name == "issu-role" or name == "node-id" or name == "num-cm-conn-reqs" or name == "num-fgid-conn-reqs" or name == "num-fsdb-conn-reqs" or name == "num-fstats-conn-reqs" or name == "num-intf-ports" or name == "num-issu-mgr-conn-reqs" or name == "num-peer-fia-conn-reqs" or name == "num-pm-conn-reqs" or name == "rack-num" or name == "rack-type" or name == "respawn-count" or name == "total-asics" or name == "uc-weight" or name == "ucmc-ratio"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "slot"):
                                        self.slot = value
                                        self.slot.value_namespace = name_space
                                        self.slot.value_namespace_prefix = name_space_prefix
                                    if(value_path == "asic-avail-mask"):
                                        self.asic_avail_mask = value
                                        self.asic_avail_mask.value_namespace = name_space
                                        self.asic_avail_mask.value_namespace_prefix = name_space_prefix
                                    if(value_path == "asic-oper-notify-to-fsdb-pending-bmap"):
                                        self.asic_oper_notify_to_fsdb_pending_bmap = value
                                        self.asic_oper_notify_to_fsdb_pending_bmap.value_namespace = name_space
                                        self.asic_oper_notify_to_fsdb_pending_bmap.value_namespace_prefix = name_space_prefix
                                    if(value_path == "board-rev-id"):
                                        self.board_rev_id = value
                                        self.board_rev_id.value_namespace = name_space
                                        self.board_rev_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "card-avail-mask"):
                                        self.card_avail_mask = value
                                        self.card_avail_mask.value_namespace = name_space
                                        self.card_avail_mask.value_namespace_prefix = name_space_prefix
                                    if(value_path == "coeff-major-rev"):
                                        self.coeff_major_rev = value
                                        self.coeff_major_rev.value_namespace = name_space
                                        self.coeff_major_rev.value_namespace_prefix = name_space_prefix
                                    if(value_path == "coeff-minor-rev"):
                                        self.coeff_minor_rev = value
                                        self.coeff_minor_rev.value_namespace = name_space
                                        self.coeff_minor_rev.value_namespace_prefix = name_space_prefix
                                    if(value_path == "drv-version"):
                                        self.drv_version = value
                                        self.drv_version.value_namespace = name_space
                                        self.drv_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "drvr-current-startup-timestamp"):
                                        self.drvr_current_startup_timestamp = value
                                        self.drvr_current_startup_timestamp.value_namespace = name_space
                                        self.drvr_current_startup_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "drvr-initial-startup-timestamp"):
                                        self.drvr_initial_startup_timestamp = value
                                        self.drvr_initial_startup_timestamp.value_namespace = name_space
                                        self.drvr_initial_startup_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "exp-asic-avail-mask"):
                                        self.exp_asic_avail_mask = value
                                        self.exp_asic_avail_mask.value_namespace = name_space
                                        self.exp_asic_avail_mask.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fabric-mode"):
                                        self.fabric_mode = value
                                        self.fabric_mode.value_namespace = name_space
                                        self.fabric_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fc-mode"):
                                        self.fc_mode = value
                                        self.fc_mode.value_namespace = name_space
                                        self.fc_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fgid-conn-active"):
                                        self.fgid_conn_active = value
                                        self.fgid_conn_active.value_namespace = name_space
                                        self.fgid_conn_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fgid-reg-active"):
                                        self.fgid_reg_active = value
                                        self.fgid_reg_active.value_namespace = name_space
                                        self.fgid_reg_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fsdb-conn-active"):
                                        self.fsdb_conn_active = value
                                        self.fsdb_conn_active.value_namespace = name_space
                                        self.fsdb_conn_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fsdb-reg-active"):
                                        self.fsdb_reg_active = value
                                        self.fsdb_reg_active.value_namespace = name_space
                                        self.fsdb_reg_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "functional-role"):
                                        self.functional_role = value
                                        self.functional_role.value_namespace = name_space
                                        self.functional_role.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-cih-registered"):
                                        self.is_cih_registered = value
                                        self.is_cih_registered.value_namespace = name_space
                                        self.is_cih_registered.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-driver-ready"):
                                        self.is_driver_ready = value
                                        self.is_driver_ready.value_namespace = name_space
                                        self.is_driver_ready.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-fgid-download-completed"):
                                        self.is_fgid_download_completed = value
                                        self.is_fgid_download_completed.value_namespace = name_space
                                        self.is_fgid_download_completed.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-fgid-download-in-progress"):
                                        self.is_fgid_download_in_progress = value
                                        self.is_fgid_download_in_progress.value_namespace = name_space
                                        self.is_fgid_download_in_progress.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-full-fgid-download-req"):
                                        self.is_full_fgid_download_req = value
                                        self.is_full_fgid_download_req.value_namespace = name_space
                                        self.is_full_fgid_download_req.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-gaspp-registered"):
                                        self.is_gaspp_registered = value
                                        self.is_gaspp_registered.value_namespace = name_space
                                        self.is_gaspp_registered.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-abort-rcvd"):
                                        self.issu_abort_rcvd = value
                                        self.issu_abort_rcvd.value_namespace = name_space
                                        self.issu_abort_rcvd.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-abort-sent"):
                                        self.issu_abort_sent = value
                                        self.issu_abort_sent.value_namespace = name_space
                                        self.issu_abort_sent.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-mgr-conn-active"):
                                        self.issu_mgr_conn_active = value
                                        self.issu_mgr_conn_active.value_namespace = name_space
                                        self.issu_mgr_conn_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-mgr-reg-active"):
                                        self.issu_mgr_reg_active = value
                                        self.issu_mgr_reg_active.value_namespace = name_space
                                        self.issu_mgr_reg_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-ready-ntfy-pending"):
                                        self.issu_ready_ntfy_pending = value
                                        self.issu_ready_ntfy_pending.value_namespace = name_space
                                        self.issu_ready_ntfy_pending.value_namespace_prefix = name_space_prefix
                                    if(value_path == "issu-role"):
                                        self.issu_role = value
                                        self.issu_role.value_namespace = name_space
                                        self.issu_role.value_namespace_prefix = name_space_prefix
                                    if(value_path == "node-id"):
                                        self.node_id = value
                                        self.node_id.value_namespace = name_space
                                        self.node_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-cm-conn-reqs"):
                                        self.num_cm_conn_reqs = value
                                        self.num_cm_conn_reqs.value_namespace = name_space
                                        self.num_cm_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-fgid-conn-reqs"):
                                        self.num_fgid_conn_reqs = value
                                        self.num_fgid_conn_reqs.value_namespace = name_space
                                        self.num_fgid_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-fsdb-conn-reqs"):
                                        self.num_fsdb_conn_reqs = value
                                        self.num_fsdb_conn_reqs.value_namespace = name_space
                                        self.num_fsdb_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-fstats-conn-reqs"):
                                        self.num_fstats_conn_reqs = value
                                        self.num_fstats_conn_reqs.value_namespace = name_space
                                        self.num_fstats_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-intf-ports"):
                                        self.num_intf_ports = value
                                        self.num_intf_ports.value_namespace = name_space
                                        self.num_intf_ports.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-issu-mgr-conn-reqs"):
                                        self.num_issu_mgr_conn_reqs = value
                                        self.num_issu_mgr_conn_reqs.value_namespace = name_space
                                        self.num_issu_mgr_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-peer-fia-conn-reqs"):
                                        self.num_peer_fia_conn_reqs = value
                                        self.num_peer_fia_conn_reqs.value_namespace = name_space
                                        self.num_peer_fia_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "num-pm-conn-reqs"):
                                        self.num_pm_conn_reqs = value
                                        self.num_pm_conn_reqs.value_namespace = name_space
                                        self.num_pm_conn_reqs.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rack-num"):
                                        self.rack_num = value
                                        self.rack_num.value_namespace = name_space
                                        self.rack_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rack-type"):
                                        self.rack_type = value
                                        self.rack_type.value_namespace = name_space
                                        self.rack_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "respawn-count"):
                                        self.respawn_count = value
                                        self.respawn_count.value_namespace = name_space
                                        self.respawn_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "total-asics"):
                                        self.total_asics = value
                                        self.total_asics.value_namespace = name_space
                                        self.total_asics.value_namespace_prefix = name_space_prefix
                                    if(value_path == "uc-weight"):
                                        self.uc_weight = value
                                        self.uc_weight.value_namespace = name_space
                                        self.uc_weight.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ucmc-ratio"):
                                        self.ucmc_ratio = value
                                        self.ucmc_ratio.value_namespace = name_space
                                        self.ucmc_ratio.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.slot:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.slot:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "slots" + path_buffer

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

                                if (child_yang_name == "slot"):
                                    for c in self.slot:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.slot.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "slot"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.flag.is_set or
                                (self.slots is not None and self.slots.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.flag.yfilter != YFilter.not_set or
                                (self.slots is not None and self.slots.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flag" + "[flag='" + self.flag.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.flag.is_set or self.flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flag.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "slots"):
                                if (self.slots is None):
                                    self.slots = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots()
                                    self.slots.parent = self
                                    self._children_name_map["slots"] = "slots"
                                return self.slots

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "slots" or name == "flag"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "flag"):
                                self.flag = value
                                self.flag.value_namespace = name_space
                                self.flag.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.flag:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.flag:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flags" + path_buffer

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

                        if (child_yang_name == "flag"):
                            for c in self.flag:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Fia.Nodes.Node.OirHistory.Flags.Flag()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.flag.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flag"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.flags is not None and self.flags.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.flags is not None and self.flags.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oir-history" + path_buffer

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

                    if (child_yang_name == "flags"):
                        if (self.flags is None):
                            self.flags = Fia.Nodes.Node.OirHistory.Flags()
                            self.flags.parent = self
                            self._children_name_map["flags"] = "flags"
                        return self.flags

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flags"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AsicStatistics(Entity):
                """
                FIA asic statistics information
                
                .. attribute:: statistics_asic_instances
                
                	Instance table for statistics
                	**type**\:   :py:class:`StatisticsAsicInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fia.Nodes.Node.AsicStatistics, self).__init__()

                    self.yang_name = "asic-statistics"
                    self.yang_parent_name = "node"

                    self.statistics_asic_instances = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances()
                    self.statistics_asic_instances.parent = self
                    self._children_name_map["statistics_asic_instances"] = "statistics-asic-instances"
                    self._children_yang_names.add("statistics-asic-instances")


                class StatisticsAsicInstances(Entity):
                    """
                    Instance table for statistics
                    
                    .. attribute:: statistics_asic_instance
                    
                    	Asic instance for statistics
                    	**type**\: list of    :py:class:`StatisticsAsicInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances, self).__init__()

                        self.yang_name = "statistics-asic-instances"
                        self.yang_parent_name = "asic-statistics"

                        self.statistics_asic_instance = YList(self)

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
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances, self).__setattr__(name, value)


                    class StatisticsAsicInstance(Entity):
                        """
                        Asic instance for statistics
                        
                        .. attribute:: instance  <key>
                        
                        	Asic instance
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: fmac_statistics
                        
                        	Statistics of FMAC
                        	**type**\:   :py:class:`FmacStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics>`
                        
                        .. attribute:: pbc_statistics
                        
                        	Packet Byte Counter for a Asic
                        	**type**\:   :py:class:`PbcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance, self).__init__()

                            self.yang_name = "statistics-asic-instance"
                            self.yang_parent_name = "statistics-asic-instances"

                            self.instance = YLeaf(YType.uint32, "instance")

                            self.fmac_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics()
                            self.fmac_statistics.parent = self
                            self._children_name_map["fmac_statistics"] = "fmac-statistics"
                            self._children_yang_names.add("fmac-statistics")

                            self.pbc_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics()
                            self.pbc_statistics.parent = self
                            self._children_name_map["pbc_statistics"] = "pbc-statistics"
                            self._children_yang_names.add("pbc-statistics")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("instance") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance, self).__setattr__(name, value)


                        class PbcStatistics(Entity):
                            """
                            Packet Byte Counter for a Asic
                            
                            .. attribute:: pbc_stats
                            
                            	PBC stats bag
                            	**type**\:   :py:class:`PbcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics, self).__init__()

                                self.yang_name = "pbc-statistics"
                                self.yang_parent_name = "statistics-asic-instance"

                                self.pbc_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats()
                                self.pbc_stats.parent = self
                                self._children_name_map["pbc_stats"] = "pbc-stats"
                                self._children_yang_names.add("pbc-stats")


                            class PbcStats(Entity):
                                """
                                PBC stats bag
                                
                                .. attribute:: asic_instance
                                
                                	asic instance
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chip_ver
                                
                                	chip ver
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: rack_no
                                
                                	rack no
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: slot_no
                                
                                	slot no
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: stats_info
                                
                                	stats info
                                	**type**\:   :py:class:`StatsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo>`
                                
                                .. attribute:: valid
                                
                                	valid
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, self).__init__()

                                    self.yang_name = "pbc-stats"
                                    self.yang_parent_name = "pbc-statistics"

                                    self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                    self.chip_ver = YLeaf(YType.uint16, "chip-ver")

                                    self.rack_no = YLeaf(YType.uint32, "rack-no")

                                    self.slot_no = YLeaf(YType.uint32, "slot-no")

                                    self.valid = YLeaf(YType.boolean, "valid")

                                    self.stats_info = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo()
                                    self.stats_info.parent = self
                                    self._children_name_map["stats_info"] = "stats-info"
                                    self._children_yang_names.add("stats-info")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("asic_instance",
                                                    "chip_ver",
                                                    "rack_no",
                                                    "slot_no",
                                                    "valid") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats, self).__setattr__(name, value)


                                class StatsInfo(Entity):
                                    """
                                    stats info
                                    
                                    .. attribute:: block_info
                                    
                                    	block info
                                    	**type**\: list of    :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo>`
                                    
                                    .. attribute:: num_blocks
                                    
                                    	Num Blocks
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo, self).__init__()

                                        self.yang_name = "stats-info"
                                        self.yang_parent_name = "pbc-stats"

                                        self.num_blocks = YLeaf(YType.uint8, "num-blocks")

                                        self.block_info = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_blocks") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo, self).__setattr__(name, value)


                                    class BlockInfo(Entity):
                                        """
                                        block info
                                        
                                        .. attribute:: block_name
                                        
                                        	Block Name
                                        	**type**\:  str
                                        
                                        	**length:** 0..10
                                        
                                        .. attribute:: field_info
                                        
                                        	field info
                                        	**type**\: list of    :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo>`
                                        
                                        .. attribute:: num_fields
                                        
                                        	Num Fields
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo, self).__init__()

                                            self.yang_name = "block-info"
                                            self.yang_parent_name = "stats-info"

                                            self.block_name = YLeaf(YType.str, "block-name")

                                            self.num_fields = YLeaf(YType.uint8, "num-fields")

                                            self.field_info = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("block_name",
                                                            "num_fields") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo, self).__setattr__(name, value)


                                        class FieldInfo(Entity):
                                            """
                                            field info
                                            
                                            .. attribute:: field_name
                                            
                                            	Field Name
                                            	**type**\:  str
                                            
                                            	**length:** 0..80
                                            
                                            .. attribute:: field_value
                                            
                                            	Field Value
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: is_ovf
                                            
                                            	Is Ovf
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo, self).__init__()

                                                self.yang_name = "field-info"
                                                self.yang_parent_name = "block-info"

                                                self.field_name = YLeaf(YType.str, "field-name")

                                                self.field_value = YLeaf(YType.uint64, "field-value")

                                                self.is_ovf = YLeaf(YType.boolean, "is-ovf")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("field_name",
                                                                "field_value",
                                                                "is_ovf") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.field_name.is_set or
                                                    self.field_value.is_set or
                                                    self.is_ovf.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.field_name.yfilter != YFilter.not_set or
                                                    self.field_value.yfilter != YFilter.not_set or
                                                    self.is_ovf.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "field-info" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.field_name.is_set or self.field_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.field_name.get_name_leafdata())
                                                if (self.field_value.is_set or self.field_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.field_value.get_name_leafdata())
                                                if (self.is_ovf.is_set or self.is_ovf.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_ovf.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "field-name" or name == "field-value" or name == "is-ovf"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "field-name"):
                                                    self.field_name = value
                                                    self.field_name.value_namespace = name_space
                                                    self.field_name.value_namespace_prefix = name_space_prefix
                                                if(value_path == "field-value"):
                                                    self.field_value = value
                                                    self.field_value.value_namespace = name_space
                                                    self.field_value.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-ovf"):
                                                    self.is_ovf = value
                                                    self.is_ovf.value_namespace = name_space
                                                    self.is_ovf.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.field_info:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.block_name.is_set or
                                                self.num_fields.is_set)

                                        def has_operation(self):
                                            for c in self.field_info:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.block_name.yfilter != YFilter.not_set or
                                                self.num_fields.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "block-info" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.block_name.is_set or self.block_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.block_name.get_name_leafdata())
                                            if (self.num_fields.is_set or self.num_fields.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.num_fields.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "field-info"):
                                                for c in self.field_info:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.field_info.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "field-info" or name == "block-name" or name == "num-fields"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "block-name"):
                                                self.block_name = value
                                                self.block_name.value_namespace = name_space
                                                self.block_name.value_namespace_prefix = name_space_prefix
                                            if(value_path == "num-fields"):
                                                self.num_fields = value
                                                self.num_fields.value_namespace = name_space
                                                self.num_fields.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.block_info:
                                            if (c.has_data()):
                                                return True
                                        return self.num_blocks.is_set

                                    def has_operation(self):
                                        for c in self.block_info:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_blocks.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stats-info" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_blocks.is_set or self.num_blocks.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_blocks.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "block-info"):
                                            for c in self.block_info:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.block_info.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "block-info" or name == "num-blocks"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-blocks"):
                                            self.num_blocks = value
                                            self.num_blocks.value_namespace = name_space
                                            self.num_blocks.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.asic_instance.is_set or
                                        self.chip_ver.is_set or
                                        self.rack_no.is_set or
                                        self.slot_no.is_set or
                                        self.valid.is_set or
                                        (self.stats_info is not None and self.stats_info.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.asic_instance.yfilter != YFilter.not_set or
                                        self.chip_ver.yfilter != YFilter.not_set or
                                        self.rack_no.yfilter != YFilter.not_set or
                                        self.slot_no.yfilter != YFilter.not_set or
                                        self.valid.yfilter != YFilter.not_set or
                                        (self.stats_info is not None and self.stats_info.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "pbc-stats" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                    if (self.chip_ver.is_set or self.chip_ver.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chip_ver.get_name_leafdata())
                                    if (self.rack_no.is_set or self.rack_no.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rack_no.get_name_leafdata())
                                    if (self.slot_no.is_set or self.slot_no.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.slot_no.get_name_leafdata())
                                    if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.valid.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "stats-info"):
                                        if (self.stats_info is None):
                                            self.stats_info = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo()
                                            self.stats_info.parent = self
                                            self._children_name_map["stats_info"] = "stats-info"
                                        return self.stats_info

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stats-info" or name == "asic-instance" or name == "chip-ver" or name == "rack-no" or name == "slot-no" or name == "valid"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "asic-instance"):
                                        self.asic_instance = value
                                        self.asic_instance.value_namespace = name_space
                                        self.asic_instance.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chip-ver"):
                                        self.chip_ver = value
                                        self.chip_ver.value_namespace = name_space
                                        self.chip_ver.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rack-no"):
                                        self.rack_no = value
                                        self.rack_no.value_namespace = name_space
                                        self.rack_no.value_namespace_prefix = name_space_prefix
                                    if(value_path == "slot-no"):
                                        self.slot_no = value
                                        self.slot_no.value_namespace = name_space
                                        self.slot_no.value_namespace_prefix = name_space_prefix
                                    if(value_path == "valid"):
                                        self.valid = value
                                        self.valid.value_namespace = name_space
                                        self.valid.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.pbc_stats is not None and self.pbc_stats.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.pbc_stats is not None and self.pbc_stats.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbc-statistics" + path_buffer

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

                                if (child_yang_name == "pbc-stats"):
                                    if (self.pbc_stats is None):
                                        self.pbc_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats()
                                        self.pbc_stats.parent = self
                                        self._children_name_map["pbc_stats"] = "pbc-stats"
                                    return self.pbc_stats

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "pbc-stats"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class FmacStatistics(Entity):
                            """
                            Statistics of FMAC
                            
                            .. attribute:: fmac_links
                            
                            	Link table for statistics
                            	**type**\:   :py:class:`FmacLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics, self).__init__()

                                self.yang_name = "fmac-statistics"
                                self.yang_parent_name = "statistics-asic-instance"

                                self.fmac_links = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks()
                                self.fmac_links.parent = self
                                self._children_name_map["fmac_links"] = "fmac-links"
                                self._children_yang_names.add("fmac-links")


                            class FmacLinks(Entity):
                                """
                                Link table for statistics
                                
                                .. attribute:: fmac_link
                                
                                	Link number for statistics
                                	**type**\: list of    :py:class:`FmacLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks, self).__init__()

                                    self.yang_name = "fmac-links"
                                    self.yang_parent_name = "fmac-statistics"

                                    self.fmac_link = YList(self)

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
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks, self).__setattr__(name, value)


                                class FmacLink(Entity):
                                    """
                                    Link number for statistics
                                    
                                    .. attribute:: link  <key>
                                    
                                    	Link number
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: fmac_asic
                                    
                                    	Single aisc information
                                    	**type**\: list of    :py:class:`FmacAsic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink, self).__init__()

                                        self.yang_name = "fmac-link"
                                        self.yang_parent_name = "fmac-links"

                                        self.link = YLeaf(YType.int32, "link")

                                        self.fmac_asic = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("link") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink, self).__setattr__(name, value)


                                    class FmacAsic(Entity):
                                        """
                                        Single aisc information
                                        
                                        .. attribute:: asic  <key>
                                        
                                        	Single asic
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: aggr_stats
                                        
                                        	aggr stats
                                        	**type**\:   :py:class:`AggrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats>`
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: incr_stats
                                        
                                        	incr stats
                                        	**type**\:   :py:class:`IncrStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats>`
                                        
                                        .. attribute:: link_no
                                        
                                        	link no
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: link_valid
                                        
                                        	link valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: rack_no
                                        
                                        	rack no
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: slot_no
                                        
                                        	slot no
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: valid
                                        
                                        	valid
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, self).__init__()

                                            self.yang_name = "fmac-asic"
                                            self.yang_parent_name = "fmac-link"

                                            self.asic = YLeaf(YType.int32, "asic")

                                            self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                            self.link_no = YLeaf(YType.uint32, "link-no")

                                            self.link_valid = YLeaf(YType.boolean, "link-valid")

                                            self.rack_no = YLeaf(YType.uint32, "rack-no")

                                            self.slot_no = YLeaf(YType.uint32, "slot-no")

                                            self.valid = YLeaf(YType.boolean, "valid")

                                            self.aggr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats()
                                            self.aggr_stats.parent = self
                                            self._children_name_map["aggr_stats"] = "aggr-stats"
                                            self._children_yang_names.add("aggr-stats")

                                            self.incr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats()
                                            self.incr_stats.parent = self
                                            self._children_name_map["incr_stats"] = "incr-stats"
                                            self._children_yang_names.add("incr-stats")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("asic",
                                                            "asic_instance",
                                                            "link_no",
                                                            "link_valid",
                                                            "rack_no",
                                                            "slot_no",
                                                            "valid") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic, self).__setattr__(name, value)


                                        class AggrStats(Entity):
                                            """
                                            aggr stats
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:   :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters>`
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:   :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:   :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats, self).__init__()

                                                self.yang_name = "aggr-stats"
                                                self.yang_parent_name = "fmac-asic"

                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self._children_name_map["link_counters"] = "link-counters"
                                                self._children_yang_names.add("link-counters")

                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self._children_name_map["link_error_status"] = "link-error-status"
                                                self._children_yang_names.add("link-error-status")

                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus()
                                                self.ovf_status.parent = self
                                                self._children_name_map["ovf_status"] = "ovf-status"
                                                self._children_yang_names.add("ovf-status")


                                            class LinkErrorStatus(Entity):
                                                """
                                                link error status
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, self).__init__()

                                                    self.yang_name = "link-error-status"
                                                    self.yang_parent_name = "aggr-stats"

                                                    self.error_token_count = YLeaf(YType.uint32, "error-token-count")

                                                    self.link_code_group_error = YLeaf(YType.uint32, "link-code-group-error")

                                                    self.link_crc_error = YLeaf(YType.uint32, "link-crc-error")

                                                    self.link_mis_align_error = YLeaf(YType.uint32, "link-mis-align-error")

                                                    self.link_no_sig_accept_error = YLeaf(YType.uint32, "link-no-sig-accept-error")

                                                    self.link_no_sig_lock_error = YLeaf(YType.uint32, "link-no-sig-lock-error")

                                                    self.link_size_error = YLeaf(YType.uint32, "link-size-error")

                                                    self.link_tokens_error = YLeaf(YType.uint32, "link-tokens-error")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("error_token_count",
                                                                    "link_code_group_error",
                                                                    "link_crc_error",
                                                                    "link_mis_align_error",
                                                                    "link_no_sig_accept_error",
                                                                    "link_no_sig_lock_error",
                                                                    "link_size_error",
                                                                    "link_tokens_error") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.error_token_count.is_set or
                                                        self.link_code_group_error.is_set or
                                                        self.link_crc_error.is_set or
                                                        self.link_mis_align_error.is_set or
                                                        self.link_no_sig_accept_error.is_set or
                                                        self.link_no_sig_lock_error.is_set or
                                                        self.link_size_error.is_set or
                                                        self.link_tokens_error.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.error_token_count.yfilter != YFilter.not_set or
                                                        self.link_code_group_error.yfilter != YFilter.not_set or
                                                        self.link_crc_error.yfilter != YFilter.not_set or
                                                        self.link_mis_align_error.yfilter != YFilter.not_set or
                                                        self.link_no_sig_accept_error.yfilter != YFilter.not_set or
                                                        self.link_no_sig_lock_error.yfilter != YFilter.not_set or
                                                        self.link_size_error.yfilter != YFilter.not_set or
                                                        self.link_tokens_error.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "link-error-status" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.error_token_count.is_set or self.error_token_count.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.error_token_count.get_name_leafdata())
                                                    if (self.link_code_group_error.is_set or self.link_code_group_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_code_group_error.get_name_leafdata())
                                                    if (self.link_crc_error.is_set or self.link_crc_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_crc_error.get_name_leafdata())
                                                    if (self.link_mis_align_error.is_set or self.link_mis_align_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_mis_align_error.get_name_leafdata())
                                                    if (self.link_no_sig_accept_error.is_set or self.link_no_sig_accept_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_no_sig_accept_error.get_name_leafdata())
                                                    if (self.link_no_sig_lock_error.is_set or self.link_no_sig_lock_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_no_sig_lock_error.get_name_leafdata())
                                                    if (self.link_size_error.is_set or self.link_size_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_size_error.get_name_leafdata())
                                                    if (self.link_tokens_error.is_set or self.link_tokens_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_tokens_error.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "error-token-count" or name == "link-code-group-error" or name == "link-crc-error" or name == "link-mis-align-error" or name == "link-no-sig-accept-error" or name == "link-no-sig-lock-error" or name == "link-size-error" or name == "link-tokens-error"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "error-token-count"):
                                                        self.error_token_count = value
                                                        self.error_token_count.value_namespace = name_space
                                                        self.error_token_count.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-code-group-error"):
                                                        self.link_code_group_error = value
                                                        self.link_code_group_error.value_namespace = name_space
                                                        self.link_code_group_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-crc-error"):
                                                        self.link_crc_error = value
                                                        self.link_crc_error.value_namespace = name_space
                                                        self.link_crc_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-mis-align-error"):
                                                        self.link_mis_align_error = value
                                                        self.link_mis_align_error.value_namespace = name_space
                                                        self.link_mis_align_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-no-sig-accept-error"):
                                                        self.link_no_sig_accept_error = value
                                                        self.link_no_sig_accept_error.value_namespace = name_space
                                                        self.link_no_sig_accept_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-no-sig-lock-error"):
                                                        self.link_no_sig_lock_error = value
                                                        self.link_no_sig_lock_error.value_namespace = name_space
                                                        self.link_no_sig_lock_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-size-error"):
                                                        self.link_size_error = value
                                                        self.link_size_error.value_namespace = name_space
                                                        self.link_size_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-tokens-error"):
                                                        self.link_tokens_error = value
                                                        self.link_tokens_error.value_namespace = name_space
                                                        self.link_tokens_error.value_namespace_prefix = name_space_prefix


                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, self).__init__()

                                                    self.yang_name = "link-counters"
                                                    self.yang_parent_name = "aggr-stats"

                                                    self.rx_8b_10b_code_errors = YLeaf(YType.uint64, "rx-8b-10b-code-errors")

                                                    self.rx_8b_10b_disparity_errors = YLeaf(YType.uint64, "rx-8b-10b-disparity-errors")

                                                    self.rx_asyn_fifo_rate = YLeaf(YType.uint64, "rx-asyn-fifo-rate")

                                                    self.rx_control_cells_counter = YLeaf(YType.uint64, "rx-control-cells-counter")

                                                    self.rx_crc_errors_counter = YLeaf(YType.uint64, "rx-crc-errors-counter")

                                                    self.rx_data_byte_counter = YLeaf(YType.uint64, "rx-data-byte-counter")

                                                    self.rx_data_cell_counter = YLeaf(YType.uint64, "rx-data-cell-counter")

                                                    self.rx_dropped_retransmitted_control = YLeaf(YType.uint64, "rx-dropped-retransmitted-control")

                                                    self.rx_lfec_fec_correctable_error = YLeaf(YType.uint64, "rx-lfec-fec-correctable-error")

                                                    self.rx_lfec_fec_uncorrectable_errors = YLeaf(YType.uint64, "rx-lfec-fec-uncorrectable-errors")

                                                    self.tx_asyn_fifo_rate = YLeaf(YType.uint64, "tx-asyn-fifo-rate")

                                                    self.tx_control_cells_counter = YLeaf(YType.uint64, "tx-control-cells-counter")

                                                    self.tx_data_byte_counter = YLeaf(YType.uint64, "tx-data-byte-counter")

                                                    self.tx_data_cell_counter = YLeaf(YType.uint64, "tx-data-cell-counter")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("rx_8b_10b_code_errors",
                                                                    "rx_8b_10b_disparity_errors",
                                                                    "rx_asyn_fifo_rate",
                                                                    "rx_control_cells_counter",
                                                                    "rx_crc_errors_counter",
                                                                    "rx_data_byte_counter",
                                                                    "rx_data_cell_counter",
                                                                    "rx_dropped_retransmitted_control",
                                                                    "rx_lfec_fec_correctable_error",
                                                                    "rx_lfec_fec_uncorrectable_errors",
                                                                    "tx_asyn_fifo_rate",
                                                                    "tx_control_cells_counter",
                                                                    "tx_data_byte_counter",
                                                                    "tx_data_cell_counter") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.rx_8b_10b_code_errors.is_set or
                                                        self.rx_8b_10b_disparity_errors.is_set or
                                                        self.rx_asyn_fifo_rate.is_set or
                                                        self.rx_control_cells_counter.is_set or
                                                        self.rx_crc_errors_counter.is_set or
                                                        self.rx_data_byte_counter.is_set or
                                                        self.rx_data_cell_counter.is_set or
                                                        self.rx_dropped_retransmitted_control.is_set or
                                                        self.rx_lfec_fec_correctable_error.is_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.is_set or
                                                        self.tx_asyn_fifo_rate.is_set or
                                                        self.tx_control_cells_counter.is_set or
                                                        self.tx_data_byte_counter.is_set or
                                                        self.tx_data_cell_counter.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_code_errors.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set or
                                                        self.rx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.rx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.rx_crc_errors_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_cell_counter.yfilter != YFilter.not_set or
                                                        self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set or
                                                        self.tx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.tx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_cell_counter.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "link-counters" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.rx_8b_10b_code_errors.is_set or self.rx_8b_10b_code_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_code_errors.get_name_leafdata())
                                                    if (self.rx_8b_10b_disparity_errors.is_set or self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_disparity_errors.get_name_leafdata())
                                                    if (self.rx_asyn_fifo_rate.is_set or self.rx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.rx_control_cells_counter.is_set or self.rx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_control_cells_counter.get_name_leafdata())
                                                    if (self.rx_crc_errors_counter.is_set or self.rx_crc_errors_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_crc_errors_counter.get_name_leafdata())
                                                    if (self.rx_data_byte_counter.is_set or self.rx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_byte_counter.get_name_leafdata())
                                                    if (self.rx_data_cell_counter.is_set or self.rx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_cell_counter.get_name_leafdata())
                                                    if (self.rx_dropped_retransmitted_control.is_set or self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_dropped_retransmitted_control.get_name_leafdata())
                                                    if (self.rx_lfec_fec_correctable_error.is_set or self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_correctable_error.get_name_leafdata())
                                                    if (self.rx_lfec_fec_uncorrectable_errors.is_set or self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_uncorrectable_errors.get_name_leafdata())
                                                    if (self.tx_asyn_fifo_rate.is_set or self.tx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.tx_control_cells_counter.is_set or self.tx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_control_cells_counter.get_name_leafdata())
                                                    if (self.tx_data_byte_counter.is_set or self.tx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_byte_counter.get_name_leafdata())
                                                    if (self.tx_data_cell_counter.is_set or self.tx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_cell_counter.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "rx-8b-10b-code-errors" or name == "rx-8b-10b-disparity-errors" or name == "rx-asyn-fifo-rate" or name == "rx-control-cells-counter" or name == "rx-crc-errors-counter" or name == "rx-data-byte-counter" or name == "rx-data-cell-counter" or name == "rx-dropped-retransmitted-control" or name == "rx-lfec-fec-correctable-error" or name == "rx-lfec-fec-uncorrectable-errors" or name == "tx-asyn-fifo-rate" or name == "tx-control-cells-counter" or name == "tx-data-byte-counter" or name == "tx-data-cell-counter"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "rx-8b-10b-code-errors"):
                                                        self.rx_8b_10b_code_errors = value
                                                        self.rx_8b_10b_code_errors.value_namespace = name_space
                                                        self.rx_8b_10b_code_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-8b-10b-disparity-errors"):
                                                        self.rx_8b_10b_disparity_errors = value
                                                        self.rx_8b_10b_disparity_errors.value_namespace = name_space
                                                        self.rx_8b_10b_disparity_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-asyn-fifo-rate"):
                                                        self.rx_asyn_fifo_rate = value
                                                        self.rx_asyn_fifo_rate.value_namespace = name_space
                                                        self.rx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-control-cells-counter"):
                                                        self.rx_control_cells_counter = value
                                                        self.rx_control_cells_counter.value_namespace = name_space
                                                        self.rx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-crc-errors-counter"):
                                                        self.rx_crc_errors_counter = value
                                                        self.rx_crc_errors_counter.value_namespace = name_space
                                                        self.rx_crc_errors_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-byte-counter"):
                                                        self.rx_data_byte_counter = value
                                                        self.rx_data_byte_counter.value_namespace = name_space
                                                        self.rx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-cell-counter"):
                                                        self.rx_data_cell_counter = value
                                                        self.rx_data_cell_counter.value_namespace = name_space
                                                        self.rx_data_cell_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-dropped-retransmitted-control"):
                                                        self.rx_dropped_retransmitted_control = value
                                                        self.rx_dropped_retransmitted_control.value_namespace = name_space
                                                        self.rx_dropped_retransmitted_control.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-correctable-error"):
                                                        self.rx_lfec_fec_correctable_error = value
                                                        self.rx_lfec_fec_correctable_error.value_namespace = name_space
                                                        self.rx_lfec_fec_correctable_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-uncorrectable-errors"):
                                                        self.rx_lfec_fec_uncorrectable_errors = value
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace = name_space
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-asyn-fifo-rate"):
                                                        self.tx_asyn_fifo_rate = value
                                                        self.tx_asyn_fifo_rate.value_namespace = name_space
                                                        self.tx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-control-cells-counter"):
                                                        self.tx_control_cells_counter = value
                                                        self.tx_control_cells_counter.value_namespace = name_space
                                                        self.tx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-byte-counter"):
                                                        self.tx_data_byte_counter = value
                                                        self.tx_data_byte_counter.value_namespace = name_space
                                                        self.tx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-cell-counter"):
                                                        self.tx_data_cell_counter = value
                                                        self.tx_data_cell_counter.value_namespace = name_space
                                                        self.tx_data_cell_counter.value_namespace_prefix = name_space_prefix


                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, self).__init__()

                                                    self.yang_name = "ovf-status"
                                                    self.yang_parent_name = "aggr-stats"

                                                    self.rx_8b_10b_code_errors = YLeaf(YType.str, "rx-8b-10b-code-errors")

                                                    self.rx_8b_10b_disparity_errors = YLeaf(YType.str, "rx-8b-10b-disparity-errors")

                                                    self.rx_asyn_fifo_rate = YLeaf(YType.str, "rx-asyn-fifo-rate")

                                                    self.rx_control_cells_counter = YLeaf(YType.str, "rx-control-cells-counter")

                                                    self.rx_crc_errors_counter = YLeaf(YType.str, "rx-crc-errors-counter")

                                                    self.rx_data_byte_counter = YLeaf(YType.str, "rx-data-byte-counter")

                                                    self.rx_data_cell_counter = YLeaf(YType.str, "rx-data-cell-counter")

                                                    self.rx_dropped_retransmitted_control = YLeaf(YType.str, "rx-dropped-retransmitted-control")

                                                    self.rx_lfec_fec_correctable_error = YLeaf(YType.str, "rx-lfec-fec-correctable-error")

                                                    self.rx_lfec_fec_uncorrectable_errors = YLeaf(YType.str, "rx-lfec-fec-uncorrectable-errors")

                                                    self.tx_asyn_fifo_rate = YLeaf(YType.str, "tx-asyn-fifo-rate")

                                                    self.tx_control_cells_counter = YLeaf(YType.str, "tx-control-cells-counter")

                                                    self.tx_data_byte_counter = YLeaf(YType.str, "tx-data-byte-counter")

                                                    self.tx_data_cell_counter = YLeaf(YType.str, "tx-data-cell-counter")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("rx_8b_10b_code_errors",
                                                                    "rx_8b_10b_disparity_errors",
                                                                    "rx_asyn_fifo_rate",
                                                                    "rx_control_cells_counter",
                                                                    "rx_crc_errors_counter",
                                                                    "rx_data_byte_counter",
                                                                    "rx_data_cell_counter",
                                                                    "rx_dropped_retransmitted_control",
                                                                    "rx_lfec_fec_correctable_error",
                                                                    "rx_lfec_fec_uncorrectable_errors",
                                                                    "tx_asyn_fifo_rate",
                                                                    "tx_control_cells_counter",
                                                                    "tx_data_byte_counter",
                                                                    "tx_data_cell_counter") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.rx_8b_10b_code_errors.is_set or
                                                        self.rx_8b_10b_disparity_errors.is_set or
                                                        self.rx_asyn_fifo_rate.is_set or
                                                        self.rx_control_cells_counter.is_set or
                                                        self.rx_crc_errors_counter.is_set or
                                                        self.rx_data_byte_counter.is_set or
                                                        self.rx_data_cell_counter.is_set or
                                                        self.rx_dropped_retransmitted_control.is_set or
                                                        self.rx_lfec_fec_correctable_error.is_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.is_set or
                                                        self.tx_asyn_fifo_rate.is_set or
                                                        self.tx_control_cells_counter.is_set or
                                                        self.tx_data_byte_counter.is_set or
                                                        self.tx_data_cell_counter.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_code_errors.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set or
                                                        self.rx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.rx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.rx_crc_errors_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_cell_counter.yfilter != YFilter.not_set or
                                                        self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set or
                                                        self.tx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.tx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_cell_counter.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "ovf-status" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.rx_8b_10b_code_errors.is_set or self.rx_8b_10b_code_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_code_errors.get_name_leafdata())
                                                    if (self.rx_8b_10b_disparity_errors.is_set or self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_disparity_errors.get_name_leafdata())
                                                    if (self.rx_asyn_fifo_rate.is_set or self.rx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.rx_control_cells_counter.is_set or self.rx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_control_cells_counter.get_name_leafdata())
                                                    if (self.rx_crc_errors_counter.is_set or self.rx_crc_errors_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_crc_errors_counter.get_name_leafdata())
                                                    if (self.rx_data_byte_counter.is_set or self.rx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_byte_counter.get_name_leafdata())
                                                    if (self.rx_data_cell_counter.is_set or self.rx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_cell_counter.get_name_leafdata())
                                                    if (self.rx_dropped_retransmitted_control.is_set or self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_dropped_retransmitted_control.get_name_leafdata())
                                                    if (self.rx_lfec_fec_correctable_error.is_set or self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_correctable_error.get_name_leafdata())
                                                    if (self.rx_lfec_fec_uncorrectable_errors.is_set or self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_uncorrectable_errors.get_name_leafdata())
                                                    if (self.tx_asyn_fifo_rate.is_set or self.tx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.tx_control_cells_counter.is_set or self.tx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_control_cells_counter.get_name_leafdata())
                                                    if (self.tx_data_byte_counter.is_set or self.tx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_byte_counter.get_name_leafdata())
                                                    if (self.tx_data_cell_counter.is_set or self.tx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_cell_counter.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "rx-8b-10b-code-errors" or name == "rx-8b-10b-disparity-errors" or name == "rx-asyn-fifo-rate" or name == "rx-control-cells-counter" or name == "rx-crc-errors-counter" or name == "rx-data-byte-counter" or name == "rx-data-cell-counter" or name == "rx-dropped-retransmitted-control" or name == "rx-lfec-fec-correctable-error" or name == "rx-lfec-fec-uncorrectable-errors" or name == "tx-asyn-fifo-rate" or name == "tx-control-cells-counter" or name == "tx-data-byte-counter" or name == "tx-data-cell-counter"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "rx-8b-10b-code-errors"):
                                                        self.rx_8b_10b_code_errors = value
                                                        self.rx_8b_10b_code_errors.value_namespace = name_space
                                                        self.rx_8b_10b_code_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-8b-10b-disparity-errors"):
                                                        self.rx_8b_10b_disparity_errors = value
                                                        self.rx_8b_10b_disparity_errors.value_namespace = name_space
                                                        self.rx_8b_10b_disparity_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-asyn-fifo-rate"):
                                                        self.rx_asyn_fifo_rate = value
                                                        self.rx_asyn_fifo_rate.value_namespace = name_space
                                                        self.rx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-control-cells-counter"):
                                                        self.rx_control_cells_counter = value
                                                        self.rx_control_cells_counter.value_namespace = name_space
                                                        self.rx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-crc-errors-counter"):
                                                        self.rx_crc_errors_counter = value
                                                        self.rx_crc_errors_counter.value_namespace = name_space
                                                        self.rx_crc_errors_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-byte-counter"):
                                                        self.rx_data_byte_counter = value
                                                        self.rx_data_byte_counter.value_namespace = name_space
                                                        self.rx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-cell-counter"):
                                                        self.rx_data_cell_counter = value
                                                        self.rx_data_cell_counter.value_namespace = name_space
                                                        self.rx_data_cell_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-dropped-retransmitted-control"):
                                                        self.rx_dropped_retransmitted_control = value
                                                        self.rx_dropped_retransmitted_control.value_namespace = name_space
                                                        self.rx_dropped_retransmitted_control.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-correctable-error"):
                                                        self.rx_lfec_fec_correctable_error = value
                                                        self.rx_lfec_fec_correctable_error.value_namespace = name_space
                                                        self.rx_lfec_fec_correctable_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-uncorrectable-errors"):
                                                        self.rx_lfec_fec_uncorrectable_errors = value
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace = name_space
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-asyn-fifo-rate"):
                                                        self.tx_asyn_fifo_rate = value
                                                        self.tx_asyn_fifo_rate.value_namespace = name_space
                                                        self.tx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-control-cells-counter"):
                                                        self.tx_control_cells_counter = value
                                                        self.tx_control_cells_counter.value_namespace = name_space
                                                        self.tx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-byte-counter"):
                                                        self.tx_data_byte_counter = value
                                                        self.tx_data_byte_counter.value_namespace = name_space
                                                        self.tx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-cell-counter"):
                                                        self.tx_data_cell_counter = value
                                                        self.tx_data_cell_counter.value_namespace = name_space
                                                        self.tx_data_cell_counter.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    (self.link_counters is not None and self.link_counters.has_data()) or
                                                    (self.link_error_status is not None and self.link_error_status.has_data()) or
                                                    (self.ovf_status is not None and self.ovf_status.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.link_counters is not None and self.link_counters.has_operation()) or
                                                    (self.link_error_status is not None and self.link_error_status.has_operation()) or
                                                    (self.ovf_status is not None and self.ovf_status.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggr-stats" + path_buffer

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

                                                if (child_yang_name == "link-counters"):
                                                    if (self.link_counters is None):
                                                        self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters()
                                                        self.link_counters.parent = self
                                                        self._children_name_map["link_counters"] = "link-counters"
                                                    return self.link_counters

                                                if (child_yang_name == "link-error-status"):
                                                    if (self.link_error_status is None):
                                                        self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus()
                                                        self.link_error_status.parent = self
                                                        self._children_name_map["link_error_status"] = "link-error-status"
                                                    return self.link_error_status

                                                if (child_yang_name == "ovf-status"):
                                                    if (self.ovf_status is None):
                                                        self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus()
                                                        self.ovf_status.parent = self
                                                        self._children_name_map["ovf_status"] = "ovf-status"
                                                    return self.ovf_status

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "link-counters" or name == "link-error-status" or name == "ovf-status"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass


                                        class IncrStats(Entity):
                                            """
                                            incr stats
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\:   :py:class:`LinkCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters>`
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\:   :py:class:`LinkErrorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\:   :py:class:`OvfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats, self).__init__()

                                                self.yang_name = "incr-stats"
                                                self.yang_parent_name = "fmac-asic"

                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self._children_name_map["link_counters"] = "link-counters"
                                                self._children_yang_names.add("link-counters")

                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self._children_name_map["link_error_status"] = "link-error-status"
                                                self._children_yang_names.add("link-error-status")

                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus()
                                                self.ovf_status.parent = self
                                                self._children_name_map["ovf_status"] = "ovf-status"
                                                self._children_yang_names.add("ovf-status")


                                            class LinkErrorStatus(Entity):
                                                """
                                                link error status
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, self).__init__()

                                                    self.yang_name = "link-error-status"
                                                    self.yang_parent_name = "incr-stats"

                                                    self.error_token_count = YLeaf(YType.uint32, "error-token-count")

                                                    self.link_code_group_error = YLeaf(YType.uint32, "link-code-group-error")

                                                    self.link_crc_error = YLeaf(YType.uint32, "link-crc-error")

                                                    self.link_mis_align_error = YLeaf(YType.uint32, "link-mis-align-error")

                                                    self.link_no_sig_accept_error = YLeaf(YType.uint32, "link-no-sig-accept-error")

                                                    self.link_no_sig_lock_error = YLeaf(YType.uint32, "link-no-sig-lock-error")

                                                    self.link_size_error = YLeaf(YType.uint32, "link-size-error")

                                                    self.link_tokens_error = YLeaf(YType.uint32, "link-tokens-error")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("error_token_count",
                                                                    "link_code_group_error",
                                                                    "link_crc_error",
                                                                    "link_mis_align_error",
                                                                    "link_no_sig_accept_error",
                                                                    "link_no_sig_lock_error",
                                                                    "link_size_error",
                                                                    "link_tokens_error") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.error_token_count.is_set or
                                                        self.link_code_group_error.is_set or
                                                        self.link_crc_error.is_set or
                                                        self.link_mis_align_error.is_set or
                                                        self.link_no_sig_accept_error.is_set or
                                                        self.link_no_sig_lock_error.is_set or
                                                        self.link_size_error.is_set or
                                                        self.link_tokens_error.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.error_token_count.yfilter != YFilter.not_set or
                                                        self.link_code_group_error.yfilter != YFilter.not_set or
                                                        self.link_crc_error.yfilter != YFilter.not_set or
                                                        self.link_mis_align_error.yfilter != YFilter.not_set or
                                                        self.link_no_sig_accept_error.yfilter != YFilter.not_set or
                                                        self.link_no_sig_lock_error.yfilter != YFilter.not_set or
                                                        self.link_size_error.yfilter != YFilter.not_set or
                                                        self.link_tokens_error.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "link-error-status" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.error_token_count.is_set or self.error_token_count.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.error_token_count.get_name_leafdata())
                                                    if (self.link_code_group_error.is_set or self.link_code_group_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_code_group_error.get_name_leafdata())
                                                    if (self.link_crc_error.is_set or self.link_crc_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_crc_error.get_name_leafdata())
                                                    if (self.link_mis_align_error.is_set or self.link_mis_align_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_mis_align_error.get_name_leafdata())
                                                    if (self.link_no_sig_accept_error.is_set or self.link_no_sig_accept_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_no_sig_accept_error.get_name_leafdata())
                                                    if (self.link_no_sig_lock_error.is_set or self.link_no_sig_lock_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_no_sig_lock_error.get_name_leafdata())
                                                    if (self.link_size_error.is_set or self.link_size_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_size_error.get_name_leafdata())
                                                    if (self.link_tokens_error.is_set or self.link_tokens_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.link_tokens_error.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "error-token-count" or name == "link-code-group-error" or name == "link-crc-error" or name == "link-mis-align-error" or name == "link-no-sig-accept-error" or name == "link-no-sig-lock-error" or name == "link-size-error" or name == "link-tokens-error"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "error-token-count"):
                                                        self.error_token_count = value
                                                        self.error_token_count.value_namespace = name_space
                                                        self.error_token_count.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-code-group-error"):
                                                        self.link_code_group_error = value
                                                        self.link_code_group_error.value_namespace = name_space
                                                        self.link_code_group_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-crc-error"):
                                                        self.link_crc_error = value
                                                        self.link_crc_error.value_namespace = name_space
                                                        self.link_crc_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-mis-align-error"):
                                                        self.link_mis_align_error = value
                                                        self.link_mis_align_error.value_namespace = name_space
                                                        self.link_mis_align_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-no-sig-accept-error"):
                                                        self.link_no_sig_accept_error = value
                                                        self.link_no_sig_accept_error.value_namespace = name_space
                                                        self.link_no_sig_accept_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-no-sig-lock-error"):
                                                        self.link_no_sig_lock_error = value
                                                        self.link_no_sig_lock_error.value_namespace = name_space
                                                        self.link_no_sig_lock_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-size-error"):
                                                        self.link_size_error = value
                                                        self.link_size_error.value_namespace = name_space
                                                        self.link_size_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "link-tokens-error"):
                                                        self.link_tokens_error = value
                                                        self.link_tokens_error.value_namespace = name_space
                                                        self.link_tokens_error.value_namespace_prefix = name_space_prefix


                                            class LinkCounters(Entity):
                                                """
                                                link counters
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, self).__init__()

                                                    self.yang_name = "link-counters"
                                                    self.yang_parent_name = "incr-stats"

                                                    self.rx_8b_10b_code_errors = YLeaf(YType.uint64, "rx-8b-10b-code-errors")

                                                    self.rx_8b_10b_disparity_errors = YLeaf(YType.uint64, "rx-8b-10b-disparity-errors")

                                                    self.rx_asyn_fifo_rate = YLeaf(YType.uint64, "rx-asyn-fifo-rate")

                                                    self.rx_control_cells_counter = YLeaf(YType.uint64, "rx-control-cells-counter")

                                                    self.rx_crc_errors_counter = YLeaf(YType.uint64, "rx-crc-errors-counter")

                                                    self.rx_data_byte_counter = YLeaf(YType.uint64, "rx-data-byte-counter")

                                                    self.rx_data_cell_counter = YLeaf(YType.uint64, "rx-data-cell-counter")

                                                    self.rx_dropped_retransmitted_control = YLeaf(YType.uint64, "rx-dropped-retransmitted-control")

                                                    self.rx_lfec_fec_correctable_error = YLeaf(YType.uint64, "rx-lfec-fec-correctable-error")

                                                    self.rx_lfec_fec_uncorrectable_errors = YLeaf(YType.uint64, "rx-lfec-fec-uncorrectable-errors")

                                                    self.tx_asyn_fifo_rate = YLeaf(YType.uint64, "tx-asyn-fifo-rate")

                                                    self.tx_control_cells_counter = YLeaf(YType.uint64, "tx-control-cells-counter")

                                                    self.tx_data_byte_counter = YLeaf(YType.uint64, "tx-data-byte-counter")

                                                    self.tx_data_cell_counter = YLeaf(YType.uint64, "tx-data-cell-counter")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("rx_8b_10b_code_errors",
                                                                    "rx_8b_10b_disparity_errors",
                                                                    "rx_asyn_fifo_rate",
                                                                    "rx_control_cells_counter",
                                                                    "rx_crc_errors_counter",
                                                                    "rx_data_byte_counter",
                                                                    "rx_data_cell_counter",
                                                                    "rx_dropped_retransmitted_control",
                                                                    "rx_lfec_fec_correctable_error",
                                                                    "rx_lfec_fec_uncorrectable_errors",
                                                                    "tx_asyn_fifo_rate",
                                                                    "tx_control_cells_counter",
                                                                    "tx_data_byte_counter",
                                                                    "tx_data_cell_counter") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.rx_8b_10b_code_errors.is_set or
                                                        self.rx_8b_10b_disparity_errors.is_set or
                                                        self.rx_asyn_fifo_rate.is_set or
                                                        self.rx_control_cells_counter.is_set or
                                                        self.rx_crc_errors_counter.is_set or
                                                        self.rx_data_byte_counter.is_set or
                                                        self.rx_data_cell_counter.is_set or
                                                        self.rx_dropped_retransmitted_control.is_set or
                                                        self.rx_lfec_fec_correctable_error.is_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.is_set or
                                                        self.tx_asyn_fifo_rate.is_set or
                                                        self.tx_control_cells_counter.is_set or
                                                        self.tx_data_byte_counter.is_set or
                                                        self.tx_data_cell_counter.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_code_errors.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set or
                                                        self.rx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.rx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.rx_crc_errors_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_cell_counter.yfilter != YFilter.not_set or
                                                        self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set or
                                                        self.tx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.tx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_cell_counter.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "link-counters" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.rx_8b_10b_code_errors.is_set or self.rx_8b_10b_code_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_code_errors.get_name_leafdata())
                                                    if (self.rx_8b_10b_disparity_errors.is_set or self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_disparity_errors.get_name_leafdata())
                                                    if (self.rx_asyn_fifo_rate.is_set or self.rx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.rx_control_cells_counter.is_set or self.rx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_control_cells_counter.get_name_leafdata())
                                                    if (self.rx_crc_errors_counter.is_set or self.rx_crc_errors_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_crc_errors_counter.get_name_leafdata())
                                                    if (self.rx_data_byte_counter.is_set or self.rx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_byte_counter.get_name_leafdata())
                                                    if (self.rx_data_cell_counter.is_set or self.rx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_cell_counter.get_name_leafdata())
                                                    if (self.rx_dropped_retransmitted_control.is_set or self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_dropped_retransmitted_control.get_name_leafdata())
                                                    if (self.rx_lfec_fec_correctable_error.is_set or self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_correctable_error.get_name_leafdata())
                                                    if (self.rx_lfec_fec_uncorrectable_errors.is_set or self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_uncorrectable_errors.get_name_leafdata())
                                                    if (self.tx_asyn_fifo_rate.is_set or self.tx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.tx_control_cells_counter.is_set or self.tx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_control_cells_counter.get_name_leafdata())
                                                    if (self.tx_data_byte_counter.is_set or self.tx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_byte_counter.get_name_leafdata())
                                                    if (self.tx_data_cell_counter.is_set or self.tx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_cell_counter.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "rx-8b-10b-code-errors" or name == "rx-8b-10b-disparity-errors" or name == "rx-asyn-fifo-rate" or name == "rx-control-cells-counter" or name == "rx-crc-errors-counter" or name == "rx-data-byte-counter" or name == "rx-data-cell-counter" or name == "rx-dropped-retransmitted-control" or name == "rx-lfec-fec-correctable-error" or name == "rx-lfec-fec-uncorrectable-errors" or name == "tx-asyn-fifo-rate" or name == "tx-control-cells-counter" or name == "tx-data-byte-counter" or name == "tx-data-cell-counter"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "rx-8b-10b-code-errors"):
                                                        self.rx_8b_10b_code_errors = value
                                                        self.rx_8b_10b_code_errors.value_namespace = name_space
                                                        self.rx_8b_10b_code_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-8b-10b-disparity-errors"):
                                                        self.rx_8b_10b_disparity_errors = value
                                                        self.rx_8b_10b_disparity_errors.value_namespace = name_space
                                                        self.rx_8b_10b_disparity_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-asyn-fifo-rate"):
                                                        self.rx_asyn_fifo_rate = value
                                                        self.rx_asyn_fifo_rate.value_namespace = name_space
                                                        self.rx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-control-cells-counter"):
                                                        self.rx_control_cells_counter = value
                                                        self.rx_control_cells_counter.value_namespace = name_space
                                                        self.rx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-crc-errors-counter"):
                                                        self.rx_crc_errors_counter = value
                                                        self.rx_crc_errors_counter.value_namespace = name_space
                                                        self.rx_crc_errors_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-byte-counter"):
                                                        self.rx_data_byte_counter = value
                                                        self.rx_data_byte_counter.value_namespace = name_space
                                                        self.rx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-cell-counter"):
                                                        self.rx_data_cell_counter = value
                                                        self.rx_data_cell_counter.value_namespace = name_space
                                                        self.rx_data_cell_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-dropped-retransmitted-control"):
                                                        self.rx_dropped_retransmitted_control = value
                                                        self.rx_dropped_retransmitted_control.value_namespace = name_space
                                                        self.rx_dropped_retransmitted_control.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-correctable-error"):
                                                        self.rx_lfec_fec_correctable_error = value
                                                        self.rx_lfec_fec_correctable_error.value_namespace = name_space
                                                        self.rx_lfec_fec_correctable_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-uncorrectable-errors"):
                                                        self.rx_lfec_fec_uncorrectable_errors = value
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace = name_space
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-asyn-fifo-rate"):
                                                        self.tx_asyn_fifo_rate = value
                                                        self.tx_asyn_fifo_rate.value_namespace = name_space
                                                        self.tx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-control-cells-counter"):
                                                        self.tx_control_cells_counter = value
                                                        self.tx_control_cells_counter.value_namespace = name_space
                                                        self.tx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-byte-counter"):
                                                        self.tx_data_byte_counter = value
                                                        self.tx_data_byte_counter.value_namespace = name_space
                                                        self.tx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-cell-counter"):
                                                        self.tx_data_cell_counter = value
                                                        self.tx_data_cell_counter.value_namespace = name_space
                                                        self.tx_data_cell_counter.value_namespace_prefix = name_space_prefix


                                            class OvfStatus(Entity):
                                                """
                                                ovf status
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\:  str
                                                
                                                	**length:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, self).__init__()

                                                    self.yang_name = "ovf-status"
                                                    self.yang_parent_name = "incr-stats"

                                                    self.rx_8b_10b_code_errors = YLeaf(YType.str, "rx-8b-10b-code-errors")

                                                    self.rx_8b_10b_disparity_errors = YLeaf(YType.str, "rx-8b-10b-disparity-errors")

                                                    self.rx_asyn_fifo_rate = YLeaf(YType.str, "rx-asyn-fifo-rate")

                                                    self.rx_control_cells_counter = YLeaf(YType.str, "rx-control-cells-counter")

                                                    self.rx_crc_errors_counter = YLeaf(YType.str, "rx-crc-errors-counter")

                                                    self.rx_data_byte_counter = YLeaf(YType.str, "rx-data-byte-counter")

                                                    self.rx_data_cell_counter = YLeaf(YType.str, "rx-data-cell-counter")

                                                    self.rx_dropped_retransmitted_control = YLeaf(YType.str, "rx-dropped-retransmitted-control")

                                                    self.rx_lfec_fec_correctable_error = YLeaf(YType.str, "rx-lfec-fec-correctable-error")

                                                    self.rx_lfec_fec_uncorrectable_errors = YLeaf(YType.str, "rx-lfec-fec-uncorrectable-errors")

                                                    self.tx_asyn_fifo_rate = YLeaf(YType.str, "tx-asyn-fifo-rate")

                                                    self.tx_control_cells_counter = YLeaf(YType.str, "tx-control-cells-counter")

                                                    self.tx_data_byte_counter = YLeaf(YType.str, "tx-data-byte-counter")

                                                    self.tx_data_cell_counter = YLeaf(YType.str, "tx-data-cell-counter")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("rx_8b_10b_code_errors",
                                                                    "rx_8b_10b_disparity_errors",
                                                                    "rx_asyn_fifo_rate",
                                                                    "rx_control_cells_counter",
                                                                    "rx_crc_errors_counter",
                                                                    "rx_data_byte_counter",
                                                                    "rx_data_cell_counter",
                                                                    "rx_dropped_retransmitted_control",
                                                                    "rx_lfec_fec_correctable_error",
                                                                    "rx_lfec_fec_uncorrectable_errors",
                                                                    "tx_asyn_fifo_rate",
                                                                    "tx_control_cells_counter",
                                                                    "tx_data_byte_counter",
                                                                    "tx_data_cell_counter") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.rx_8b_10b_code_errors.is_set or
                                                        self.rx_8b_10b_disparity_errors.is_set or
                                                        self.rx_asyn_fifo_rate.is_set or
                                                        self.rx_control_cells_counter.is_set or
                                                        self.rx_crc_errors_counter.is_set or
                                                        self.rx_data_byte_counter.is_set or
                                                        self.rx_data_cell_counter.is_set or
                                                        self.rx_dropped_retransmitted_control.is_set or
                                                        self.rx_lfec_fec_correctable_error.is_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.is_set or
                                                        self.tx_asyn_fifo_rate.is_set or
                                                        self.tx_control_cells_counter.is_set or
                                                        self.tx_data_byte_counter.is_set or
                                                        self.tx_data_cell_counter.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_code_errors.yfilter != YFilter.not_set or
                                                        self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set or
                                                        self.rx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.rx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.rx_crc_errors_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.rx_data_cell_counter.yfilter != YFilter.not_set or
                                                        self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set or
                                                        self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set or
                                                        self.tx_asyn_fifo_rate.yfilter != YFilter.not_set or
                                                        self.tx_control_cells_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_byte_counter.yfilter != YFilter.not_set or
                                                        self.tx_data_cell_counter.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "ovf-status" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.rx_8b_10b_code_errors.is_set or self.rx_8b_10b_code_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_code_errors.get_name_leafdata())
                                                    if (self.rx_8b_10b_disparity_errors.is_set or self.rx_8b_10b_disparity_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_8b_10b_disparity_errors.get_name_leafdata())
                                                    if (self.rx_asyn_fifo_rate.is_set or self.rx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.rx_control_cells_counter.is_set or self.rx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_control_cells_counter.get_name_leafdata())
                                                    if (self.rx_crc_errors_counter.is_set or self.rx_crc_errors_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_crc_errors_counter.get_name_leafdata())
                                                    if (self.rx_data_byte_counter.is_set or self.rx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_byte_counter.get_name_leafdata())
                                                    if (self.rx_data_cell_counter.is_set or self.rx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_data_cell_counter.get_name_leafdata())
                                                    if (self.rx_dropped_retransmitted_control.is_set or self.rx_dropped_retransmitted_control.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_dropped_retransmitted_control.get_name_leafdata())
                                                    if (self.rx_lfec_fec_correctable_error.is_set or self.rx_lfec_fec_correctable_error.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_correctable_error.get_name_leafdata())
                                                    if (self.rx_lfec_fec_uncorrectable_errors.is_set or self.rx_lfec_fec_uncorrectable_errors.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rx_lfec_fec_uncorrectable_errors.get_name_leafdata())
                                                    if (self.tx_asyn_fifo_rate.is_set or self.tx_asyn_fifo_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_asyn_fifo_rate.get_name_leafdata())
                                                    if (self.tx_control_cells_counter.is_set or self.tx_control_cells_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_control_cells_counter.get_name_leafdata())
                                                    if (self.tx_data_byte_counter.is_set or self.tx_data_byte_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_byte_counter.get_name_leafdata())
                                                    if (self.tx_data_cell_counter.is_set or self.tx_data_cell_counter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.tx_data_cell_counter.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "rx-8b-10b-code-errors" or name == "rx-8b-10b-disparity-errors" or name == "rx-asyn-fifo-rate" or name == "rx-control-cells-counter" or name == "rx-crc-errors-counter" or name == "rx-data-byte-counter" or name == "rx-data-cell-counter" or name == "rx-dropped-retransmitted-control" or name == "rx-lfec-fec-correctable-error" or name == "rx-lfec-fec-uncorrectable-errors" or name == "tx-asyn-fifo-rate" or name == "tx-control-cells-counter" or name == "tx-data-byte-counter" or name == "tx-data-cell-counter"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "rx-8b-10b-code-errors"):
                                                        self.rx_8b_10b_code_errors = value
                                                        self.rx_8b_10b_code_errors.value_namespace = name_space
                                                        self.rx_8b_10b_code_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-8b-10b-disparity-errors"):
                                                        self.rx_8b_10b_disparity_errors = value
                                                        self.rx_8b_10b_disparity_errors.value_namespace = name_space
                                                        self.rx_8b_10b_disparity_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-asyn-fifo-rate"):
                                                        self.rx_asyn_fifo_rate = value
                                                        self.rx_asyn_fifo_rate.value_namespace = name_space
                                                        self.rx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-control-cells-counter"):
                                                        self.rx_control_cells_counter = value
                                                        self.rx_control_cells_counter.value_namespace = name_space
                                                        self.rx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-crc-errors-counter"):
                                                        self.rx_crc_errors_counter = value
                                                        self.rx_crc_errors_counter.value_namespace = name_space
                                                        self.rx_crc_errors_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-byte-counter"):
                                                        self.rx_data_byte_counter = value
                                                        self.rx_data_byte_counter.value_namespace = name_space
                                                        self.rx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-data-cell-counter"):
                                                        self.rx_data_cell_counter = value
                                                        self.rx_data_cell_counter.value_namespace = name_space
                                                        self.rx_data_cell_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-dropped-retransmitted-control"):
                                                        self.rx_dropped_retransmitted_control = value
                                                        self.rx_dropped_retransmitted_control.value_namespace = name_space
                                                        self.rx_dropped_retransmitted_control.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-correctable-error"):
                                                        self.rx_lfec_fec_correctable_error = value
                                                        self.rx_lfec_fec_correctable_error.value_namespace = name_space
                                                        self.rx_lfec_fec_correctable_error.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rx-lfec-fec-uncorrectable-errors"):
                                                        self.rx_lfec_fec_uncorrectable_errors = value
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace = name_space
                                                        self.rx_lfec_fec_uncorrectable_errors.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-asyn-fifo-rate"):
                                                        self.tx_asyn_fifo_rate = value
                                                        self.tx_asyn_fifo_rate.value_namespace = name_space
                                                        self.tx_asyn_fifo_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-control-cells-counter"):
                                                        self.tx_control_cells_counter = value
                                                        self.tx_control_cells_counter.value_namespace = name_space
                                                        self.tx_control_cells_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-byte-counter"):
                                                        self.tx_data_byte_counter = value
                                                        self.tx_data_byte_counter.value_namespace = name_space
                                                        self.tx_data_byte_counter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "tx-data-cell-counter"):
                                                        self.tx_data_cell_counter = value
                                                        self.tx_data_cell_counter.value_namespace = name_space
                                                        self.tx_data_cell_counter.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    (self.link_counters is not None and self.link_counters.has_data()) or
                                                    (self.link_error_status is not None and self.link_error_status.has_data()) or
                                                    (self.ovf_status is not None and self.ovf_status.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.link_counters is not None and self.link_counters.has_operation()) or
                                                    (self.link_error_status is not None and self.link_error_status.has_operation()) or
                                                    (self.ovf_status is not None and self.ovf_status.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "incr-stats" + path_buffer

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

                                                if (child_yang_name == "link-counters"):
                                                    if (self.link_counters is None):
                                                        self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters()
                                                        self.link_counters.parent = self
                                                        self._children_name_map["link_counters"] = "link-counters"
                                                    return self.link_counters

                                                if (child_yang_name == "link-error-status"):
                                                    if (self.link_error_status is None):
                                                        self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus()
                                                        self.link_error_status.parent = self
                                                        self._children_name_map["link_error_status"] = "link-error-status"
                                                    return self.link_error_status

                                                if (child_yang_name == "ovf-status"):
                                                    if (self.ovf_status is None):
                                                        self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus()
                                                        self.ovf_status.parent = self
                                                        self._children_name_map["ovf_status"] = "ovf-status"
                                                    return self.ovf_status

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "link-counters" or name == "link-error-status" or name == "ovf-status"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass

                                        def has_data(self):
                                            return (
                                                self.asic.is_set or
                                                self.asic_instance.is_set or
                                                self.link_no.is_set or
                                                self.link_valid.is_set or
                                                self.rack_no.is_set or
                                                self.slot_no.is_set or
                                                self.valid.is_set or
                                                (self.aggr_stats is not None and self.aggr_stats.has_data()) or
                                                (self.incr_stats is not None and self.incr_stats.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.asic.yfilter != YFilter.not_set or
                                                self.asic_instance.yfilter != YFilter.not_set or
                                                self.link_no.yfilter != YFilter.not_set or
                                                self.link_valid.yfilter != YFilter.not_set or
                                                self.rack_no.yfilter != YFilter.not_set or
                                                self.slot_no.yfilter != YFilter.not_set or
                                                self.valid.yfilter != YFilter.not_set or
                                                (self.aggr_stats is not None and self.aggr_stats.has_operation()) or
                                                (self.incr_stats is not None and self.incr_stats.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "fmac-asic" + "[asic='" + self.asic.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.asic.is_set or self.asic.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.asic.get_name_leafdata())
                                            if (self.asic_instance.is_set or self.asic_instance.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.asic_instance.get_name_leafdata())
                                            if (self.link_no.is_set or self.link_no.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.link_no.get_name_leafdata())
                                            if (self.link_valid.is_set or self.link_valid.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.link_valid.get_name_leafdata())
                                            if (self.rack_no.is_set or self.rack_no.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rack_no.get_name_leafdata())
                                            if (self.slot_no.is_set or self.slot_no.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.slot_no.get_name_leafdata())
                                            if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.valid.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggr-stats"):
                                                if (self.aggr_stats is None):
                                                    self.aggr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats()
                                                    self.aggr_stats.parent = self
                                                    self._children_name_map["aggr_stats"] = "aggr-stats"
                                                return self.aggr_stats

                                            if (child_yang_name == "incr-stats"):
                                                if (self.incr_stats is None):
                                                    self.incr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats()
                                                    self.incr_stats.parent = self
                                                    self._children_name_map["incr_stats"] = "incr-stats"
                                                return self.incr_stats

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggr-stats" or name == "incr-stats" or name == "asic" or name == "asic-instance" or name == "link-no" or name == "link-valid" or name == "rack-no" or name == "slot-no" or name == "valid"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "asic"):
                                                self.asic = value
                                                self.asic.value_namespace = name_space
                                                self.asic.value_namespace_prefix = name_space_prefix
                                            if(value_path == "asic-instance"):
                                                self.asic_instance = value
                                                self.asic_instance.value_namespace = name_space
                                                self.asic_instance.value_namespace_prefix = name_space_prefix
                                            if(value_path == "link-no"):
                                                self.link_no = value
                                                self.link_no.value_namespace = name_space
                                                self.link_no.value_namespace_prefix = name_space_prefix
                                            if(value_path == "link-valid"):
                                                self.link_valid = value
                                                self.link_valid.value_namespace = name_space
                                                self.link_valid.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rack-no"):
                                                self.rack_no = value
                                                self.rack_no.value_namespace = name_space
                                                self.rack_no.value_namespace_prefix = name_space_prefix
                                            if(value_path == "slot-no"):
                                                self.slot_no = value
                                                self.slot_no.value_namespace = name_space
                                                self.slot_no.value_namespace_prefix = name_space_prefix
                                            if(value_path == "valid"):
                                                self.valid = value
                                                self.valid.value_namespace = name_space
                                                self.valid.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.fmac_asic:
                                            if (c.has_data()):
                                                return True
                                        return self.link.is_set

                                    def has_operation(self):
                                        for c in self.fmac_asic:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.link.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fmac-link" + "[link='" + self.link.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.link.is_set or self.link.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.link.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "fmac-asic"):
                                            for c in self.fmac_asic:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.fmac_asic.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "fmac-asic" or name == "link"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "link"):
                                            self.link = value
                                            self.link.value_namespace = name_space
                                            self.link.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.fmac_link:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.fmac_link:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "fmac-links" + path_buffer

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

                                    if (child_yang_name == "fmac-link"):
                                        for c in self.fmac_link:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.fmac_link.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "fmac-link"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.fmac_links is not None and self.fmac_links.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.fmac_links is not None and self.fmac_links.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fmac-statistics" + path_buffer

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

                                if (child_yang_name == "fmac-links"):
                                    if (self.fmac_links is None):
                                        self.fmac_links = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks()
                                        self.fmac_links.parent = self
                                        self._children_name_map["fmac_links"] = "fmac-links"
                                    return self.fmac_links

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fmac-links"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.instance.is_set or
                                (self.fmac_statistics is not None and self.fmac_statistics.has_data()) or
                                (self.pbc_statistics is not None and self.pbc_statistics.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.instance.yfilter != YFilter.not_set or
                                (self.fmac_statistics is not None and self.fmac_statistics.has_operation()) or
                                (self.pbc_statistics is not None and self.pbc_statistics.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "statistics-asic-instance" + "[instance='" + self.instance.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.instance.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "fmac-statistics"):
                                if (self.fmac_statistics is None):
                                    self.fmac_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics()
                                    self.fmac_statistics.parent = self
                                    self._children_name_map["fmac_statistics"] = "fmac-statistics"
                                return self.fmac_statistics

                            if (child_yang_name == "pbc-statistics"):
                                if (self.pbc_statistics is None):
                                    self.pbc_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics()
                                    self.pbc_statistics.parent = self
                                    self._children_name_map["pbc_statistics"] = "pbc-statistics"
                                return self.pbc_statistics

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fmac-statistics" or name == "pbc-statistics" or name == "instance"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "instance"):
                                self.instance = value
                                self.instance.value_namespace = name_space
                                self.instance.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.statistics_asic_instance:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.statistics_asic_instance:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics-asic-instances" + path_buffer

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

                        if (child_yang_name == "statistics-asic-instance"):
                            for c in self.statistics_asic_instance:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.statistics_asic_instance.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "statistics-asic-instance"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.statistics_asic_instances is not None and self.statistics_asic_instances.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.statistics_asic_instances is not None and self.statistics_asic_instances.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "asic-statistics" + path_buffer

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

                    if (child_yang_name == "statistics-asic-instances"):
                        if (self.statistics_asic_instances is None):
                            self.statistics_asic_instances = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances()
                            self.statistics_asic_instances.parent = self
                            self._children_name_map["statistics_asic_instances"] = "statistics-asic-instances"
                        return self.statistics_asic_instances

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics-asic-instances"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.asic_statistics is not None and self.asic_statistics.has_data()) or
                    (self.clear_statistics is not None and self.clear_statistics.has_data()) or
                    (self.diag_shell is not None and self.diag_shell.has_data()) or
                    (self.driver_information is not None and self.driver_information.has_data()) or
                    (self.oir_history is not None and self.oir_history.has_data()) or
                    (self.rx_link_information is not None and self.rx_link_information.has_data()) or
                    (self.tx_link_information is not None and self.tx_link_information.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.asic_statistics is not None and self.asic_statistics.has_operation()) or
                    (self.clear_statistics is not None and self.clear_statistics.has_operation()) or
                    (self.diag_shell is not None and self.diag_shell.has_operation()) or
                    (self.driver_information is not None and self.driver_information.has_operation()) or
                    (self.oir_history is not None and self.oir_history.has_operation()) or
                    (self.rx_link_information is not None and self.rx_link_information.has_operation()) or
                    (self.tx_link_information is not None and self.tx_link_information.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-dnx-driver-oper:fia/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "asic-statistics"):
                    if (self.asic_statistics is None):
                        self.asic_statistics = Fia.Nodes.Node.AsicStatistics()
                        self.asic_statistics.parent = self
                        self._children_name_map["asic_statistics"] = "asic-statistics"
                    return self.asic_statistics

                if (child_yang_name == "clear-statistics"):
                    if (self.clear_statistics is None):
                        self.clear_statistics = Fia.Nodes.Node.ClearStatistics()
                        self.clear_statistics.parent = self
                        self._children_name_map["clear_statistics"] = "clear-statistics"
                    return self.clear_statistics

                if (child_yang_name == "diag-shell"):
                    if (self.diag_shell is None):
                        self.diag_shell = Fia.Nodes.Node.DiagShell()
                        self.diag_shell.parent = self
                        self._children_name_map["diag_shell"] = "diag-shell"
                    return self.diag_shell

                if (child_yang_name == "driver-information"):
                    if (self.driver_information is None):
                        self.driver_information = Fia.Nodes.Node.DriverInformation()
                        self.driver_information.parent = self
                        self._children_name_map["driver_information"] = "driver-information"
                    return self.driver_information

                if (child_yang_name == "oir-history"):
                    if (self.oir_history is None):
                        self.oir_history = Fia.Nodes.Node.OirHistory()
                        self.oir_history.parent = self
                        self._children_name_map["oir_history"] = "oir-history"
                    return self.oir_history

                if (child_yang_name == "rx-link-information"):
                    if (self.rx_link_information is None):
                        self.rx_link_information = Fia.Nodes.Node.RxLinkInformation()
                        self.rx_link_information.parent = self
                        self._children_name_map["rx_link_information"] = "rx-link-information"
                    return self.rx_link_information

                if (child_yang_name == "tx-link-information"):
                    if (self.tx_link_information is None):
                        self.tx_link_information = Fia.Nodes.Node.TxLinkInformation()
                        self.tx_link_information.parent = self
                        self._children_name_map["tx_link_information"] = "tx-link-information"
                    return self.tx_link_information

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "asic-statistics" or name == "clear-statistics" or name == "diag-shell" or name == "driver-information" or name == "oir-history" or name == "rx-link-information" or name == "tx-link-information" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-dnx-driver-oper:fia/%s" % self.get_segment_path()
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
                c = Fia.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-dnx-driver-oper:fia" + path_buffer

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
                self.nodes = Fia.Nodes()
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
        self._top_entity = Fia()
        return self._top_entity

