""" Cisco_IOS_XR_plat_chas_invmgr_ng_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR plat\-chas\-invmgr\-ng package operational data.

This module contains definitions
for the following management objects\:
  platform\: Platform information
  platform\-inventory\: platform inventory

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CardRedundancyState(Enum):
    """
    CardRedundancyState (Enum Class)

    Redundancy state detail

    .. data:: active = 1

    	Active

    .. data:: standby = 2

    	Standby

    """

    active = Enum.YLeaf(1, "active")

    standby = Enum.YLeaf(2, "standby")


class InvAdminState(Enum):
    """
    InvAdminState (Enum Class)

    Inv admin state

    .. data:: admin_state_invalid = 0

    	admin state invalid

    .. data:: admin_up = 1

    	admin up

    .. data:: admin_down = 2

    	admin down

    """

    admin_state_invalid = Enum.YLeaf(0, "admin-state-invalid")

    admin_up = Enum.YLeaf(1, "admin-up")

    admin_down = Enum.YLeaf(2, "admin-down")


class InvCardState(Enum):
    """
    InvCardState (Enum Class)

    Inv card state

    .. data:: inv_card_not_present = 0

    	inv card not present

    .. data:: inv_card_present = 1

    	inv card present

    .. data:: inv_card_reset = 2

    	inv card reset

    .. data:: inv_card_booting = 3

    	inv card booting

    .. data:: inv_card_mbi_booting = 4

    	inv card mbi booting

    .. data:: inv_card_running_mbi = 5

    	inv card running mbi

    .. data:: inv_card_running_ena = 6

    	inv card running ena

    .. data:: inv_card_bring_down = 7

    	inv card bring down

    .. data:: inv_card_ena_failure = 8

    	inv card ena failure

    .. data:: inv_card_f_diag_run = 9

    	inv card f diag run

    .. data:: inv_card_f_diag_failure = 10

    	inv card f diag failure

    .. data:: inv_card_powered = 11

    	inv card powered

    .. data:: inv_card_unpowered = 12

    	inv card unpowered

    .. data:: inv_card_mdr = 13

    	inv card mdr

    .. data:: inv_card_mdr_running_mbi = 14

    	inv card mdr running mbi

    .. data:: inv_card_main_t_mode = 15

    	inv card main t mode

    .. data:: inv_card_admin_down = 16

    	inv card admin down

    .. data:: inv_card_no_mon = 17

    	inv card no mon

    .. data:: inv_card_unknown = 18

    	inv card unknown

    .. data:: inv_card_failed = 19

    	inv card failed

    .. data:: inv_card_ok = 20

    	inv card ok

    .. data:: inv_card_missing = 21

    	inv card missing

    .. data:: inv_card_field_diag_downloading = 22

    	inv card field diag downloading

    .. data:: inv_card_field_diag_unmonitor = 23

    	inv card field diag unmonitor

    .. data:: inv_card_fabric_field_diag_unmonitor = 24

    	inv card fabric field diag unmonitor

    .. data:: inv_card_field_diag_rp_launching = 25

    	inv card field diag rp launching

    .. data:: inv_card_field_diag_running = 26

    	inv card field diag running

    .. data:: inv_card_field_diag_pass = 27

    	inv card field diag pass

    .. data:: inv_card_field_diag_fail = 28

    	inv card field diag fail

    .. data:: inv_card_field_diag_timeout = 29

    	inv card field diag timeout

    .. data:: inv_card_disabled = 30

    	inv card disabled

    .. data:: inv_card_spa_booting = 31

    	inv card spa booting

    .. data:: inv_card_not_allowed_online = 32

    	inv card not allowed online

    .. data:: inv_card_stopped = 33

    	inv card stopped

    .. data:: inv_card_incompatible_fw_ver = 34

    	inv card incompatible fw ver

    .. data:: inv_card_fpd_hold = 35

    	inv card fpd hold

    .. data:: inv_card_node_prep = 36

    	inv card node prep

    .. data:: inv_card_updating_fpd = 37

    	inv card updating fpd

    .. data:: inv_card_num_states = 38

    	inv card num states

    """

    inv_card_not_present = Enum.YLeaf(0, "inv-card-not-present")

    inv_card_present = Enum.YLeaf(1, "inv-card-present")

    inv_card_reset = Enum.YLeaf(2, "inv-card-reset")

    inv_card_booting = Enum.YLeaf(3, "inv-card-booting")

    inv_card_mbi_booting = Enum.YLeaf(4, "inv-card-mbi-booting")

    inv_card_running_mbi = Enum.YLeaf(5, "inv-card-running-mbi")

    inv_card_running_ena = Enum.YLeaf(6, "inv-card-running-ena")

    inv_card_bring_down = Enum.YLeaf(7, "inv-card-bring-down")

    inv_card_ena_failure = Enum.YLeaf(8, "inv-card-ena-failure")

    inv_card_f_diag_run = Enum.YLeaf(9, "inv-card-f-diag-run")

    inv_card_f_diag_failure = Enum.YLeaf(10, "inv-card-f-diag-failure")

    inv_card_powered = Enum.YLeaf(11, "inv-card-powered")

    inv_card_unpowered = Enum.YLeaf(12, "inv-card-unpowered")

    inv_card_mdr = Enum.YLeaf(13, "inv-card-mdr")

    inv_card_mdr_running_mbi = Enum.YLeaf(14, "inv-card-mdr-running-mbi")

    inv_card_main_t_mode = Enum.YLeaf(15, "inv-card-main-t-mode")

    inv_card_admin_down = Enum.YLeaf(16, "inv-card-admin-down")

    inv_card_no_mon = Enum.YLeaf(17, "inv-card-no-mon")

    inv_card_unknown = Enum.YLeaf(18, "inv-card-unknown")

    inv_card_failed = Enum.YLeaf(19, "inv-card-failed")

    inv_card_ok = Enum.YLeaf(20, "inv-card-ok")

    inv_card_missing = Enum.YLeaf(21, "inv-card-missing")

    inv_card_field_diag_downloading = Enum.YLeaf(22, "inv-card-field-diag-downloading")

    inv_card_field_diag_unmonitor = Enum.YLeaf(23, "inv-card-field-diag-unmonitor")

    inv_card_fabric_field_diag_unmonitor = Enum.YLeaf(24, "inv-card-fabric-field-diag-unmonitor")

    inv_card_field_diag_rp_launching = Enum.YLeaf(25, "inv-card-field-diag-rp-launching")

    inv_card_field_diag_running = Enum.YLeaf(26, "inv-card-field-diag-running")

    inv_card_field_diag_pass = Enum.YLeaf(27, "inv-card-field-diag-pass")

    inv_card_field_diag_fail = Enum.YLeaf(28, "inv-card-field-diag-fail")

    inv_card_field_diag_timeout = Enum.YLeaf(29, "inv-card-field-diag-timeout")

    inv_card_disabled = Enum.YLeaf(30, "inv-card-disabled")

    inv_card_spa_booting = Enum.YLeaf(31, "inv-card-spa-booting")

    inv_card_not_allowed_online = Enum.YLeaf(32, "inv-card-not-allowed-online")

    inv_card_stopped = Enum.YLeaf(33, "inv-card-stopped")

    inv_card_incompatible_fw_ver = Enum.YLeaf(34, "inv-card-incompatible-fw-ver")

    inv_card_fpd_hold = Enum.YLeaf(35, "inv-card-fpd-hold")

    inv_card_node_prep = Enum.YLeaf(36, "inv-card-node-prep")

    inv_card_updating_fpd = Enum.YLeaf(37, "inv-card-updating-fpd")

    inv_card_num_states = Enum.YLeaf(38, "inv-card-num-states")


class InvMonitorState(Enum):
    """
    InvMonitorState (Enum Class)

    Inv monitor state

    .. data:: unmonitored = 0

    	unmonitored

    .. data:: monitored = 1

    	monitored

    """

    unmonitored = Enum.YLeaf(0, "unmonitored")

    monitored = Enum.YLeaf(1, "monitored")


class InvPowerAdminState(Enum):
    """
    InvPowerAdminState (Enum Class)

    Inv power admin state

    .. data:: admin_power_invalid = 0

    	admin power invalid

    .. data:: admin_on = 2

    	admin on

    .. data:: admin_off = 3

    	admin off

    """

    admin_power_invalid = Enum.YLeaf(0, "admin-power-invalid")

    admin_on = Enum.YLeaf(2, "admin-on")

    admin_off = Enum.YLeaf(3, "admin-off")


class InvResetReason(Enum):
    """
    InvResetReason (Enum Class)

    Inv reset reason

    .. data:: module_reset_reason_unknown = 0

    	module reset reason unknown

    .. data:: module_reset_reason_powerup = 1

    	module reset reason powerup

    .. data:: module_reset_reason_user_shutdown = 2

    	module reset reason user shutdown

    .. data:: module_reset_reason_user_reload = 3

    	module reset reason user reload

    .. data:: module_reset_reason_auto_reload = 4

    	module reset reason auto reload

    .. data:: module_reset_reason_environment = 5

    	module reset reason environment

    .. data:: module_reset_reason_user_unpower = 6

    	module reset reason user unpower

    """

    module_reset_reason_unknown = Enum.YLeaf(0, "module-reset-reason-unknown")

    module_reset_reason_powerup = Enum.YLeaf(1, "module-reset-reason-powerup")

    module_reset_reason_user_shutdown = Enum.YLeaf(2, "module-reset-reason-user-shutdown")

    module_reset_reason_user_reload = Enum.YLeaf(3, "module-reset-reason-user-reload")

    module_reset_reason_auto_reload = Enum.YLeaf(4, "module-reset-reason-auto-reload")

    module_reset_reason_environment = Enum.YLeaf(5, "module-reset-reason-environment")

    module_reset_reason_user_unpower = Enum.YLeaf(6, "module-reset-reason-user-unpower")


class NodeState(Enum):
    """
    NodeState (Enum Class)

    Node state detail

    .. data:: not_present = 0

    	Not present

    .. data:: present = 1

    	Present

    .. data:: reset = 2

    	Reset

    .. data:: rommon = 3

    	Card booting or rommon

    .. data:: mbi_boot = 4

    	MBI booting

    .. data:: mbi_run = 5

    	Running MBI

    .. data:: xr_run = 6

    	Running ENA

    .. data:: bring_down = 7

    	Bringdown

    .. data:: xr_fail = 8

    	ENA failure

    .. data:: fdiag_run = 9

    	Running FDIAG

    .. data:: fdiag_fail = 10

    	FDIAG failure

    .. data:: power = 11

    	Powered

    .. data:: unpower = 12

    	Unpowered

    .. data:: mdr_warm_reload = 13

    	MDR warm reload

    .. data:: mdr_mbi_run = 14

    	MDR running MBI

    .. data:: maintenance_mode = 15

    	Maintenance mode

    .. data:: admin_down = 16

    	Admin down

    .. data:: not_monitor = 17

    	No MON

    .. data:: unknown_card = 18

    	Unknown

    .. data:: failed = 19

    	Failed

    .. data:: ok = 20

    	OK

    .. data:: missing = 21

    	Missing

    .. data:: diag_download = 22

    	Field diag downloading

    .. data:: diag_not_monitor = 23

    	Field diag unmonitor

    .. data:: fabric_diag_not_monitor = 24

    	Fabric field diag unmonitor

    .. data:: diag_rp_launch = 25

    	Field diag RP launching

    .. data:: diag_run = 26

    	Field diag running

    .. data:: diag_pass = 27

    	Field diag pass

    .. data:: diag_fail = 28

    	Field diag fail

    .. data:: diag_timeout = 29

    	Field diag timeout

    .. data:: disable = 30

    	Disable

    .. data:: spa_boot = 31

    	SPA booting

    .. data:: not_allowed_online = 32

    	Not allowed online

    .. data:: stop = 33

    	Stopped

    .. data:: incomp_version = 34

    	Incompatible FW version

    .. data:: fpd_hold = 35

    	FPD hold

    .. data:: xr_preparation = 36

    	XR preparation

    .. data:: sync_ready = 37

    	Sync ready state

    .. data:: xr_isolate = 38

    	Node isolate state

    .. data:: ready = 39

    	Ready

    .. data:: invalid = 40

    	Invalid

    .. data:: operational = 41

    	Operational

    .. data:: operational_lock = 42

    	Operational lock

    .. data:: going_down = 43

    	Going down

    .. data:: going_offline = 44

    	Going offline

    .. data:: going_online = 45

    	Going online

    .. data:: offline = 46

    	Offline

    .. data:: up = 47

    	Up

    .. data:: down = 48

    	Down

    .. data:: max = 49

    	Max

    .. data:: unknown = 50

    	Unknown

    """

    not_present = Enum.YLeaf(0, "not-present")

    present = Enum.YLeaf(1, "present")

    reset = Enum.YLeaf(2, "reset")

    rommon = Enum.YLeaf(3, "rommon")

    mbi_boot = Enum.YLeaf(4, "mbi-boot")

    mbi_run = Enum.YLeaf(5, "mbi-run")

    xr_run = Enum.YLeaf(6, "xr-run")

    bring_down = Enum.YLeaf(7, "bring-down")

    xr_fail = Enum.YLeaf(8, "xr-fail")

    fdiag_run = Enum.YLeaf(9, "fdiag-run")

    fdiag_fail = Enum.YLeaf(10, "fdiag-fail")

    power = Enum.YLeaf(11, "power")

    unpower = Enum.YLeaf(12, "unpower")

    mdr_warm_reload = Enum.YLeaf(13, "mdr-warm-reload")

    mdr_mbi_run = Enum.YLeaf(14, "mdr-mbi-run")

    maintenance_mode = Enum.YLeaf(15, "maintenance-mode")

    admin_down = Enum.YLeaf(16, "admin-down")

    not_monitor = Enum.YLeaf(17, "not-monitor")

    unknown_card = Enum.YLeaf(18, "unknown-card")

    failed = Enum.YLeaf(19, "failed")

    ok = Enum.YLeaf(20, "ok")

    missing = Enum.YLeaf(21, "missing")

    diag_download = Enum.YLeaf(22, "diag-download")

    diag_not_monitor = Enum.YLeaf(23, "diag-not-monitor")

    fabric_diag_not_monitor = Enum.YLeaf(24, "fabric-diag-not-monitor")

    diag_rp_launch = Enum.YLeaf(25, "diag-rp-launch")

    diag_run = Enum.YLeaf(26, "diag-run")

    diag_pass = Enum.YLeaf(27, "diag-pass")

    diag_fail = Enum.YLeaf(28, "diag-fail")

    diag_timeout = Enum.YLeaf(29, "diag-timeout")

    disable = Enum.YLeaf(30, "disable")

    spa_boot = Enum.YLeaf(31, "spa-boot")

    not_allowed_online = Enum.YLeaf(32, "not-allowed-online")

    stop = Enum.YLeaf(33, "stop")

    incomp_version = Enum.YLeaf(34, "incomp-version")

    fpd_hold = Enum.YLeaf(35, "fpd-hold")

    xr_preparation = Enum.YLeaf(36, "xr-preparation")

    sync_ready = Enum.YLeaf(37, "sync-ready")

    xr_isolate = Enum.YLeaf(38, "xr-isolate")

    ready = Enum.YLeaf(39, "ready")

    invalid = Enum.YLeaf(40, "invalid")

    operational = Enum.YLeaf(41, "operational")

    operational_lock = Enum.YLeaf(42, "operational-lock")

    going_down = Enum.YLeaf(43, "going-down")

    going_offline = Enum.YLeaf(44, "going-offline")

    going_online = Enum.YLeaf(45, "going-online")

    offline = Enum.YLeaf(46, "offline")

    up = Enum.YLeaf(47, "up")

    down = Enum.YLeaf(48, "down")

    max = Enum.YLeaf(49, "max")

    unknown = Enum.YLeaf(50, "unknown")



class Platform(Entity):
    """
    Platform information
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks>`
    
    

    """

    _prefix = 'plat-chas-invmgr-ng-oper'
    _revision = '2018-01-22'

    def __init__(self):
        super(Platform, self).__init__()
        self._top_entity = None

        self.yang_name = "platform"
        self.yang_parent_name = "Cisco-IOS-XR-plat-chas-invmgr-ng-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", Platform.Racks))])
        self._leafs = OrderedDict()

        self.racks = Platform.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Platform, [], name, value)


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack>`
        
        

        """

        _prefix = 'plat-chas-invmgr-ng-oper'
        _revision = '2018-01-22'

        def __init__(self):
            super(Platform.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", Platform.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Platform.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: rack_name  (key)
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'plat-chas-invmgr-ng-oper'
            _revision = '2018-01-22'

            def __init__(self):
                super(Platform.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack_name']
                self._child_classes = OrderedDict([("slots", ("slots", Platform.Racks.Rack.Slots))])
                self._leafs = OrderedDict([
                    ('rack_name', (YLeaf(YType.str, 'rack-name'), ['str'])),
                ])
                self.rack_name = None

                self.slots = Platform.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._segment_path = lambda: "rack" + "[rack-name='" + str(self.rack_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Platform.Racks.Rack, ['rack_name'], name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'plat-chas-invmgr-ng-oper'
                _revision = '2018-01-22'

                def __init__(self):
                    super(Platform.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", Platform.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Platform.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Slot name
                    
                    .. attribute:: slot_name  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: instances
                    
                    	Table of Instances
                    	**type**\:  :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot.Instances>`
                    
                    .. attribute:: vm
                    
                    	VM information
                    	**type**\:  :py:class:`Vm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot.Vm>`
                    
                    .. attribute:: state
                    
                    	State information
                    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot.State>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-ng-oper'
                    _revision = '2018-01-22'

                    def __init__(self):
                        super(Platform.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot_name']
                        self._child_classes = OrderedDict([("instances", ("instances", Platform.Racks.Rack.Slots.Slot.Instances)), ("vm", ("vm", Platform.Racks.Rack.Slots.Slot.Vm)), ("state", ("state", Platform.Racks.Rack.Slots.Slot.State))])
                        self._leafs = OrderedDict([
                            ('slot_name', (YLeaf(YType.str, 'slot-name'), ['str'])),
                        ])
                        self.slot_name = None

                        self.instances = Platform.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"

                        self.vm = Platform.Racks.Rack.Slots.Slot.Vm()
                        self.vm.parent = self
                        self._children_name_map["vm"] = "vm"

                        self.state = Platform.Racks.Rack.Slots.Slot.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "slot" + "[slot-name='" + str(self.slot_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Platform.Racks.Rack.Slots.Slot, ['slot_name'], name, value)


                    class Instances(Entity):
                        """
                        Table of Instances
                        
                        .. attribute:: instance
                        
                        	Instance name
                        	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(Platform.Racks.Rack.Slots.Slot.Instances, self).__init__()

                            self.yang_name = "instances"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("instance", ("instance", Platform.Racks.Rack.Slots.Slot.Instances.Instance))])
                            self._leafs = OrderedDict()

                            self.instance = YList(self)
                            self._segment_path = lambda: "instances"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Platform.Racks.Rack.Slots.Slot.Instances, [], name, value)


                        class Instance(Entity):
                            """
                            Instance name
                            
                            .. attribute:: instance_name  (key)
                            
                            	Instance name
                            	**type**\: str
                            
                            .. attribute:: state
                            
                            	State information
                            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.Platform.Racks.Rack.Slots.Slot.Instances.Instance.State>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-ng-oper'
                            _revision = '2018-01-22'

                            def __init__(self):
                                super(Platform.Racks.Rack.Slots.Slot.Instances.Instance, self).__init__()

                                self.yang_name = "instance"
                                self.yang_parent_name = "instances"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['instance_name']
                                self._child_classes = OrderedDict([("state", ("state", Platform.Racks.Rack.Slots.Slot.Instances.Instance.State))])
                                self._leafs = OrderedDict([
                                    ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                                ])
                                self.instance_name = None

                                self.state = Platform.Racks.Rack.Slots.Slot.Instances.Instance.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "instance" + "[instance-name='" + str(self.instance_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Platform.Racks.Rack.Slots.Slot.Instances.Instance, ['instance_name'], name, value)


                            class State(Entity):
                                """
                                State information
                                
                                .. attribute:: card_type
                                
                                	Card type
                                	**type**\: str
                                
                                .. attribute:: card_redundancy_state
                                
                                	Redundancy state
                                	**type**\:  :py:class:`CardRedundancyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.CardRedundancyState>`
                                
                                .. attribute:: plim
                                
                                	PLIM
                                	**type**\: str
                                
                                .. attribute:: state
                                
                                	State
                                	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.NodeState>`
                                
                                .. attribute:: is_monitored
                                
                                	True if power state is active
                                	**type**\: bool
                                
                                .. attribute:: is_powered
                                
                                	True if monitor state is active
                                	**type**\: bool
                                
                                .. attribute:: is_shutdown
                                
                                	True if shutdown state is active
                                	**type**\: bool
                                
                                .. attribute:: admin_state
                                
                                	Admin state
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(Platform.Racks.Rack.Slots.Slot.Instances.Instance.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "instance"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                                        ('card_redundancy_state', (YLeaf(YType.enumeration, 'card-redundancy-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'CardRedundancyState', '')])),
                                        ('plim', (YLeaf(YType.str, 'plim'), ['str'])),
                                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'NodeState', '')])),
                                        ('is_monitored', (YLeaf(YType.boolean, 'is-monitored'), ['bool'])),
                                        ('is_powered', (YLeaf(YType.boolean, 'is-powered'), ['bool'])),
                                        ('is_shutdown', (YLeaf(YType.boolean, 'is-shutdown'), ['bool'])),
                                        ('admin_state', (YLeaf(YType.str, 'admin-state'), ['str'])),
                                    ])
                                    self.card_type = None
                                    self.card_redundancy_state = None
                                    self.plim = None
                                    self.state = None
                                    self.is_monitored = None
                                    self.is_powered = None
                                    self.is_shutdown = None
                                    self.admin_state = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Platform.Racks.Rack.Slots.Slot.Instances.Instance.State, ['card_type', 'card_redundancy_state', 'plim', 'state', 'is_monitored', 'is_powered', 'is_shutdown', 'admin_state'], name, value)


                    class Vm(Entity):
                        """
                        VM information
                        
                        .. attribute:: node_description
                        
                        	Node Type
                        	**type**\: str
                        
                        .. attribute:: red_role
                        
                        	Node Redundency Role
                        	**type**\: str
                        
                        .. attribute:: partner_name
                        
                        	Partner Name
                        	**type**\: str
                        
                        .. attribute:: software_status
                        
                        	SW status
                        	**type**\: str
                        
                        .. attribute:: node_ip
                        
                        	Node IP Address
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(Platform.Racks.Rack.Slots.Slot.Vm, self).__init__()

                            self.yang_name = "vm"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_description', (YLeaf(YType.str, 'node-description'), ['str'])),
                                ('red_role', (YLeaf(YType.str, 'red-role'), ['str'])),
                                ('partner_name', (YLeaf(YType.str, 'partner-name'), ['str'])),
                                ('software_status', (YLeaf(YType.str, 'software-status'), ['str'])),
                                ('node_ip', (YLeaf(YType.str, 'node-ip'), ['str'])),
                            ])
                            self.node_description = None
                            self.red_role = None
                            self.partner_name = None
                            self.software_status = None
                            self.node_ip = None
                            self._segment_path = lambda: "vm"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Platform.Racks.Rack.Slots.Slot.Vm, ['node_description', 'red_role', 'partner_name', 'software_status', 'node_ip'], name, value)


                    class State(Entity):
                        """
                        State information
                        
                        .. attribute:: card_type
                        
                        	Card type
                        	**type**\: str
                        
                        .. attribute:: card_redundancy_state
                        
                        	Redundancy state
                        	**type**\:  :py:class:`CardRedundancyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.CardRedundancyState>`
                        
                        .. attribute:: plim
                        
                        	PLIM
                        	**type**\: str
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.NodeState>`
                        
                        .. attribute:: is_monitored
                        
                        	True if power state is active
                        	**type**\: bool
                        
                        .. attribute:: is_powered
                        
                        	True if monitor state is active
                        	**type**\: bool
                        
                        .. attribute:: is_shutdown
                        
                        	True if shutdown state is active
                        	**type**\: bool
                        
                        .. attribute:: admin_state
                        
                        	Admin state
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(Platform.Racks.Rack.Slots.Slot.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                                ('card_redundancy_state', (YLeaf(YType.enumeration, 'card-redundancy-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'CardRedundancyState', '')])),
                                ('plim', (YLeaf(YType.str, 'plim'), ['str'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'NodeState', '')])),
                                ('is_monitored', (YLeaf(YType.boolean, 'is-monitored'), ['bool'])),
                                ('is_powered', (YLeaf(YType.boolean, 'is-powered'), ['bool'])),
                                ('is_shutdown', (YLeaf(YType.boolean, 'is-shutdown'), ['bool'])),
                                ('admin_state', (YLeaf(YType.str, 'admin-state'), ['str'])),
                            ])
                            self.card_type = None
                            self.card_redundancy_state = None
                            self.plim = None
                            self.state = None
                            self.is_monitored = None
                            self.is_powered = None
                            self.is_shutdown = None
                            self.admin_state = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Platform.Racks.Rack.Slots.Slot.State, ['card_type', 'card_redundancy_state', 'plim', 'state', 'is_monitored', 'is_powered', 'is_shutdown', 'admin_state'], name, value)

    def clone_ptr(self):
        self._top_entity = Platform()
        return self._top_entity

class PlatformInventory(Entity):
    """
    platform inventory
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks>`
    
    

    """

    _prefix = 'plat-chas-invmgr-ng-oper'
    _revision = '2018-01-22'

    def __init__(self):
        super(PlatformInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-plat-chas-invmgr-ng-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", PlatformInventory.Racks))])
        self._leafs = OrderedDict()

        self.racks = PlatformInventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformInventory, [], name, value)


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack>`
        
        

        """

        _prefix = 'plat-chas-invmgr-ng-oper'
        _revision = '2018-01-22'

        def __init__(self):
            super(PlatformInventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "platform-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", PlatformInventory.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformInventory.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: name  (key)
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots>`
            
            .. attribute:: attributes
            
            	Attributes
            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Attributes>`
            
            

            """

            _prefix = 'plat-chas-invmgr-ng-oper'
            _revision = '2018-01-22'

            def __init__(self):
                super(PlatformInventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("slots", ("slots", PlatformInventory.Racks.Rack.Slots)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Attributes))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.slots = PlatformInventory.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"

                self.attributes = PlatformInventory.Racks.Rack.Attributes()
                self.attributes.parent = self
                self._children_name_map["attributes"] = "attributes"
                self._segment_path = lambda: "rack" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-plat-chas-invmgr-ng-oper:platform-inventory/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformInventory.Racks.Rack, ['name'], name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'plat-chas-invmgr-ng-oper'
                _revision = '2018-01-22'

                def __init__(self):
                    super(PlatformInventory.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", PlatformInventory.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Slot name
                    
                    .. attribute:: name  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: cards
                    
                    	Table of cards
                    	**type**\:  :py:class:`Cards <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards>`
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-ng-oper'
                    _revision = '2018-01-22'

                    def __init__(self):
                        super(PlatformInventory.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("cards", ("cards", PlatformInventory.Racks.Rack.Slots.Slot.Cards)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Attributes))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.cards = PlatformInventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self
                        self._children_name_map["cards"] = "cards"

                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Attributes()
                        self.attributes.parent = self
                        self._children_name_map["attributes"] = "attributes"
                        self._segment_path = lambda: "slot" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot, ['name'], name, value)


                    class Cards(Entity):
                        """
                        Table of cards
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of  		 :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards, self).__init__()

                            self.yang_name = "cards"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("card", ("card", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card))])
                            self._leafs = OrderedDict()

                            self.card = YList(self)
                            self._segment_path = lambda: "cards"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards, [], name, value)


                        class Card(Entity):
                            """
                            Card number
                            
                            .. attribute:: name  (key)
                            
                            	Card name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: hardware_information
                            
                            	HardwareInformationDir
                            	**type**\:  :py:class:`HardwareInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation>`
                            
                            .. attribute:: sub_slots
                            
                            	Table of subslots
                            	**type**\:  :py:class:`SubSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots>`
                            
                            .. attribute:: portses
                            
                            	Table of port slots
                            	**type**\:  :py:class:`Portses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses>`
                            
                            .. attribute:: port_slots
                            
                            	Table of port slots
                            	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots>`
                            
                            .. attribute:: hw_components
                            
                            	Table of  HW components 
                            	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents>`
                            
                            .. attribute:: sensors
                            
                            	Table of sensors
                            	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors>`
                            
                            .. attribute:: attributes
                            
                            	Attributes
                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-ng-oper'
                            _revision = '2018-01-22'

                            def __init__(self):
                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "cards"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_classes = OrderedDict([("hardware-information", ("hardware_information", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation)), ("sub-slots", ("sub_slots", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots)), ("portses", ("portses", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses)), ("port-slots", ("port_slots", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots)), ("hw-components", ("hw_components", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes))])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.name = None

                                self.hardware_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation()
                                self.hardware_information.parent = self
                                self._children_name_map["hardware_information"] = "hardware-information"

                                self.sub_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self
                                self._children_name_map["sub_slots"] = "sub-slots"

                                self.portses = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses()
                                self.portses.parent = self
                                self._children_name_map["portses"] = "portses"

                                self.port_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self._children_name_map["port_slots"] = "port-slots"

                                self.hw_components = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self._children_name_map["hw_components"] = "hw-components"

                                self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self._children_name_map["sensors"] = "sensors"

                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                                self._segment_path = lambda: "card" + "[name='" + str(self.name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card, ['name'], name, value)


                            class HardwareInformation(Entity):
                                """
                                HardwareInformationDir
                                
                                .. attribute:: processor_information
                                
                                	ProcesorInformation
                                	**type**\:  :py:class:`ProcessorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation>`
                                
                                .. attribute:: motherboard_information
                                
                                	MotherboardInformation
                                	**type**\:  :py:class:`MotherboardInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation>`
                                
                                .. attribute:: bootflash_information
                                
                                	BootflashInformation
                                	**type**\:  :py:class:`BootflashInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation>`
                                
                                .. attribute:: disk_information
                                
                                	DiskInformation
                                	**type**\:  :py:class:`DiskInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation, self).__init__()

                                    self.yang_name = "hardware-information"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("processor-information", ("processor_information", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation)), ("motherboard-information", ("motherboard_information", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation)), ("bootflash-information", ("bootflash_information", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation)), ("disk-information", ("disk_information", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation))])
                                    self._leafs = OrderedDict()

                                    self.processor_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation()
                                    self.processor_information.parent = self
                                    self._children_name_map["processor_information"] = "processor-information"

                                    self.motherboard_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation()
                                    self.motherboard_information.parent = self
                                    self._children_name_map["motherboard_information"] = "motherboard-information"

                                    self.bootflash_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation()
                                    self.bootflash_information.parent = self
                                    self._children_name_map["bootflash_information"] = "bootflash-information"

                                    self.disk_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation()
                                    self.disk_information.parent = self
                                    self._children_name_map["disk_information"] = "disk-information"
                                    self._segment_path = lambda: "hardware-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation, [], name, value)


                                class ProcessorInformation(Entity):
                                    """
                                    ProcesorInformation
                                    
                                    .. attribute:: processor_type
                                    
                                    	Type e.g. 7457
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: speed
                                    
                                    	Speed e.g. 1197Mhz
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: revision
                                    
                                    	Revision. e.g 1.1
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation, self).__init__()

                                        self.yang_name = "processor-information"
                                        self.yang_parent_name = "hardware-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processor_type', (YLeaf(YType.str, 'processor-type'), ['str'])),
                                            ('speed', (YLeaf(YType.str, 'speed'), ['str'])),
                                            ('revision', (YLeaf(YType.str, 'revision'), ['str'])),
                                        ])
                                        self.processor_type = None
                                        self.speed = None
                                        self.revision = None
                                        self._segment_path = lambda: "processor-information"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation, [u'processor_type', u'speed', u'revision'], name, value)


                                class MotherboardInformation(Entity):
                                    """
                                    MotherboardInformation
                                    
                                    .. attribute:: rom
                                    
                                    	ROM information
                                    	**type**\:  :py:class:`Rom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom>`
                                    
                                    .. attribute:: bootflash
                                    
                                    	Bootflash information
                                    	**type**\:  :py:class:`Bootflash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash>`
                                    
                                    .. attribute:: processor
                                    
                                    	Processor information
                                    	**type**\:  :py:class:`Processor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor>`
                                    
                                    .. attribute:: main_memory_size
                                    
                                    	Memory size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: nvram_size
                                    
                                    	NVRAM size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation, self).__init__()

                                        self.yang_name = "motherboard-information"
                                        self.yang_parent_name = "hardware-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rom", ("rom", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom)), ("bootflash", ("bootflash", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash)), ("processor", ("processor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor))])
                                        self._leafs = OrderedDict([
                                            ('main_memory_size', (YLeaf(YType.uint64, 'main-memory-size'), ['int'])),
                                            ('nvram_size', (YLeaf(YType.uint64, 'nvram-size'), ['int'])),
                                        ])
                                        self.main_memory_size = None
                                        self.nvram_size = None

                                        self.rom = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom()
                                        self.rom.parent = self
                                        self._children_name_map["rom"] = "rom"

                                        self.bootflash = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash()
                                        self.bootflash.parent = self
                                        self._children_name_map["bootflash"] = "bootflash"

                                        self.processor = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor()
                                        self.processor.parent = self
                                        self._children_name_map["processor"] = "processor"
                                        self._segment_path = lambda: "motherboard-information"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation, [u'main_memory_size', u'nvram_size'], name, value)


                                    class Rom(Entity):
                                        """
                                        ROM information
                                        
                                        .. attribute:: image_name
                                        
                                        	Image name
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: major_version
                                        
                                        	Major version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_version
                                        
                                        	Minor version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: micro_image_version
                                        
                                        	Micro image version
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: platform_specific
                                        
                                        	Platform specific text
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: release_type
                                        
                                        	Release type
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom, self).__init__()

                                            self.yang_name = "rom"
                                            self.yang_parent_name = "motherboard-information"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('image_name', (YLeaf(YType.str, 'image-name'), ['str'])),
                                                ('major_version', (YLeaf(YType.uint32, 'major-version'), ['int'])),
                                                ('minor_version', (YLeaf(YType.uint32, 'minor-version'), ['int'])),
                                                ('micro_image_version', (YLeaf(YType.str, 'micro-image-version'), ['str'])),
                                                ('platform_specific', (YLeaf(YType.str, 'platform-specific'), ['str'])),
                                                ('release_type', (YLeaf(YType.str, 'release-type'), ['str'])),
                                            ])
                                            self.image_name = None
                                            self.major_version = None
                                            self.minor_version = None
                                            self.micro_image_version = None
                                            self.platform_specific = None
                                            self.release_type = None
                                            self._segment_path = lambda: "rom"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom, [u'image_name', u'major_version', u'minor_version', u'micro_image_version', u'platform_specific', u'release_type'], name, value)


                                    class Bootflash(Entity):
                                        """
                                        Bootflash information
                                        
                                        .. attribute:: image_name
                                        
                                        	Image name
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: platform_type
                                        
                                        	Platform Type
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: major_version
                                        
                                        	Major version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_version
                                        
                                        	Minor version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: micro_image_version
                                        
                                        	Micro image version
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: platform_specific
                                        
                                        	Platform specific text
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: release_type
                                        
                                        	Release type
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: bootflash_type
                                        
                                        	Bootflash type e.g. SIMM
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: bootflash_size
                                        
                                        	Bootflash size in kilo\-bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: kilobyte
                                        
                                        .. attribute:: sector_size
                                        
                                        	Sector size in bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash, self).__init__()

                                            self.yang_name = "bootflash"
                                            self.yang_parent_name = "motherboard-information"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('image_name', (YLeaf(YType.str, 'image-name'), ['str'])),
                                                ('platform_type', (YLeaf(YType.str, 'platform-type'), ['str'])),
                                                ('major_version', (YLeaf(YType.uint32, 'major-version'), ['int'])),
                                                ('minor_version', (YLeaf(YType.uint32, 'minor-version'), ['int'])),
                                                ('micro_image_version', (YLeaf(YType.str, 'micro-image-version'), ['str'])),
                                                ('platform_specific', (YLeaf(YType.str, 'platform-specific'), ['str'])),
                                                ('release_type', (YLeaf(YType.str, 'release-type'), ['str'])),
                                                ('bootflash_type', (YLeaf(YType.str, 'bootflash-type'), ['str'])),
                                                ('bootflash_size', (YLeaf(YType.uint32, 'bootflash-size'), ['int'])),
                                                ('sector_size', (YLeaf(YType.uint32, 'sector-size'), ['int'])),
                                            ])
                                            self.image_name = None
                                            self.platform_type = None
                                            self.major_version = None
                                            self.minor_version = None
                                            self.micro_image_version = None
                                            self.platform_specific = None
                                            self.release_type = None
                                            self.bootflash_type = None
                                            self.bootflash_size = None
                                            self.sector_size = None
                                            self._segment_path = lambda: "bootflash"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash, [u'image_name', u'platform_type', u'major_version', u'minor_version', u'micro_image_version', u'platform_specific', u'release_type', u'bootflash_type', u'bootflash_size', u'sector_size'], name, value)


                                    class Processor(Entity):
                                        """
                                        Processor information
                                        
                                        .. attribute:: processor_type
                                        
                                        	Type e.g. 7457
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: speed
                                        
                                        	Speed e.g. 1197Mhz
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: revision
                                        
                                        	Revision. e.g 1.1
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor, self).__init__()

                                            self.yang_name = "processor"
                                            self.yang_parent_name = "motherboard-information"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processor_type', (YLeaf(YType.str, 'processor-type'), ['str'])),
                                                ('speed', (YLeaf(YType.str, 'speed'), ['str'])),
                                                ('revision', (YLeaf(YType.str, 'revision'), ['str'])),
                                            ])
                                            self.processor_type = None
                                            self.speed = None
                                            self.revision = None
                                            self._segment_path = lambda: "processor"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor, [u'processor_type', u'speed', u'revision'], name, value)


                                class BootflashInformation(Entity):
                                    """
                                    BootflashInformation
                                    
                                    .. attribute:: image_name
                                    
                                    	Image name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: platform_type
                                    
                                    	Platform Type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: major_version
                                    
                                    	Major version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minor_version
                                    
                                    	Minor version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: micro_image_version
                                    
                                    	Micro image version
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: platform_specific
                                    
                                    	Platform specific text
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: release_type
                                    
                                    	Release type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: bootflash_type
                                    
                                    	Bootflash type e.g. SIMM
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: bootflash_size
                                    
                                    	Bootflash size in kilo\-bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kilobyte
                                    
                                    .. attribute:: sector_size
                                    
                                    	Sector size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation, self).__init__()

                                        self.yang_name = "bootflash-information"
                                        self.yang_parent_name = "hardware-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('image_name', (YLeaf(YType.str, 'image-name'), ['str'])),
                                            ('platform_type', (YLeaf(YType.str, 'platform-type'), ['str'])),
                                            ('major_version', (YLeaf(YType.uint32, 'major-version'), ['int'])),
                                            ('minor_version', (YLeaf(YType.uint32, 'minor-version'), ['int'])),
                                            ('micro_image_version', (YLeaf(YType.str, 'micro-image-version'), ['str'])),
                                            ('platform_specific', (YLeaf(YType.str, 'platform-specific'), ['str'])),
                                            ('release_type', (YLeaf(YType.str, 'release-type'), ['str'])),
                                            ('bootflash_type', (YLeaf(YType.str, 'bootflash-type'), ['str'])),
                                            ('bootflash_size', (YLeaf(YType.uint32, 'bootflash-size'), ['int'])),
                                            ('sector_size', (YLeaf(YType.uint32, 'sector-size'), ['int'])),
                                        ])
                                        self.image_name = None
                                        self.platform_type = None
                                        self.major_version = None
                                        self.minor_version = None
                                        self.micro_image_version = None
                                        self.platform_specific = None
                                        self.release_type = None
                                        self.bootflash_type = None
                                        self.bootflash_size = None
                                        self.sector_size = None
                                        self._segment_path = lambda: "bootflash-information"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation, [u'image_name', u'platform_type', u'major_version', u'minor_version', u'micro_image_version', u'platform_specific', u'release_type', u'bootflash_type', u'bootflash_size', u'sector_size'], name, value)


                                class DiskInformation(Entity):
                                    """
                                    DiskInformation
                                    
                                    .. attribute:: disk_name
                                    
                                    	(Deprecated) Disk name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: disk_size
                                    
                                    	(Deprecated) Disk size in mega\-bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: megabyte
                                    
                                    .. attribute:: sector_size
                                    
                                    	(Deprecated) Disk sector size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: disks
                                    
                                    	Disk attributes
                                    	**type**\: list of  		 :py:class:`Disks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation, self).__init__()

                                        self.yang_name = "disk-information"
                                        self.yang_parent_name = "hardware-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("disks", ("disks", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks))])
                                        self._leafs = OrderedDict([
                                            ('disk_name', (YLeaf(YType.str, 'disk-name'), ['str'])),
                                            ('disk_size', (YLeaf(YType.uint32, 'disk-size'), ['int'])),
                                            ('sector_size', (YLeaf(YType.uint32, 'sector-size'), ['int'])),
                                        ])
                                        self.disk_name = None
                                        self.disk_size = None
                                        self.sector_size = None

                                        self.disks = YList(self)
                                        self._segment_path = lambda: "disk-information"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation, [u'disk_name', u'disk_size', u'sector_size'], name, value)


                                    class Disks(Entity):
                                        """
                                        Disk attributes
                                        
                                        .. attribute:: disk_name
                                        
                                        	Disk name
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: disk_size
                                        
                                        	Disk size in mega\-bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: megabyte
                                        
                                        .. attribute:: sector_size
                                        
                                        	Disk sector size in bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks, self).__init__()

                                            self.yang_name = "disks"
                                            self.yang_parent_name = "disk-information"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('disk_name', (YLeaf(YType.str, 'disk-name'), ['str'])),
                                                ('disk_size', (YLeaf(YType.uint32, 'disk-size'), ['int'])),
                                                ('sector_size', (YLeaf(YType.uint32, 'sector-size'), ['int'])),
                                            ])
                                            self.disk_name = None
                                            self.disk_size = None
                                            self.sector_size = None
                                            self._segment_path = lambda: "disks"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks, [u'disk_name', u'disk_size', u'sector_size'], name, value)


                            class SubSlots(Entity):
                                """
                                Table of subslots
                                
                                .. attribute:: sub_slot
                                
                                	Subslot number
                                	**type**\: list of  		 :py:class:`SubSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, self).__init__()

                                    self.yang_name = "sub-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sub-slot", ("sub_slot", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot))])
                                    self._leafs = OrderedDict()

                                    self.sub_slot = YList(self)
                                    self._segment_path = lambda: "sub-slots"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, [], name, value)


                                class SubSlot(Entity):
                                    """
                                    Subslot number
                                    
                                    .. attribute:: name  (key)
                                    
                                    	Subslot name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: module
                                    
                                    	Module of a subslot
                                    	**type**\:  :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module>`
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, self).__init__()

                                        self.yang_name = "sub-slot"
                                        self.yang_parent_name = "sub-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([("module", ("module", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None

                                        self.module = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self
                                        self._children_name_map["module"] = "module"

                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._segment_path = lambda: "sub-slot" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, ['name'], name, value)


                                    class Module(Entity):
                                        """
                                        Module of a subslot
                                        
                                        .. attribute:: port_slots
                                        
                                        	Table of port slots
                                        	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots>`
                                        
                                        .. attribute:: sensors
                                        
                                        	Table of sensors
                                        	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors>`
                                        
                                        .. attribute:: attributes
                                        
                                        	Attributes
                                        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, self).__init__()

                                            self.yang_name = "module"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("port-slots", ("port_slots", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes))])
                                            self._leafs = OrderedDict()

                                            self.port_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self._children_name_map["port_slots"] = "port-slots"

                                            self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self
                                            self._children_name_map["sensors"] = "sensors"

                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes()
                                            self.attributes.parent = self
                                            self._children_name_map["attributes"] = "attributes"
                                            self._segment_path = lambda: "module"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, [], name, value)


                                        class PortSlots(Entity):
                                            """
                                            Table of port slots
                                            
                                            .. attribute:: port_slot
                                            
                                            	Port slot number
                                            	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, self).__init__()

                                                self.yang_name = "port-slots"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("port-slot", ("port_slot", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot))])
                                                self._leafs = OrderedDict()

                                                self.port_slot = YList(self)
                                                self._segment_path = lambda: "port-slots"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, [], name, value)


                                            class PortSlot(Entity):
                                                """
                                                Port slot number
                                                
                                                .. attribute:: name  (key)
                                                
                                                	Port slot name
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: portses
                                                
                                                	Table of port slots
                                                	**type**\:  :py:class:`Portses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses>`
                                                
                                                .. attribute:: sensors
                                                
                                                	Table of sensors
                                                	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors>`
                                                
                                                .. attribute:: attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, self).__init__()

                                                    self.yang_name = "port-slot"
                                                    self.yang_parent_name = "port-slots"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['name']
                                                    self._child_classes = OrderedDict([("portses", ("portses", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes))])
                                                    self._leafs = OrderedDict([
                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ])
                                                    self.name = None

                                                    self.portses = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses()
                                                    self.portses.parent = self
                                                    self._children_name_map["portses"] = "portses"

                                                    self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors()
                                                    self.sensors.parent = self
                                                    self._children_name_map["sensors"] = "sensors"

                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes()
                                                    self.attributes.parent = self
                                                    self._children_name_map["attributes"] = "attributes"
                                                    self._segment_path = lambda: "port-slot" + "[name='" + str(self.name) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, ['name'], name, value)


                                                class Portses(Entity):
                                                    """
                                                    Table of port slots
                                                    
                                                    .. attribute:: ports
                                                    
                                                    	Port number
                                                    	**type**\: list of  		 :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses, self).__init__()

                                                        self.yang_name = "portses"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("ports", ("ports", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports))])
                                                        self._leafs = OrderedDict()

                                                        self.ports = YList(self)
                                                        self._segment_path = lambda: "portses"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses, [], name, value)


                                                    class Ports(Entity):
                                                        """
                                                        Port number
                                                        
                                                        .. attribute:: name  (key)
                                                        
                                                        	Port name
                                                        	**type**\: str
                                                        
                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                        
                                                        .. attribute:: hw_components
                                                        
                                                        	Table of  HW components 
                                                        	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents>`
                                                        
                                                        .. attribute:: sensors
                                                        
                                                        	Table of sensors
                                                        	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors>`
                                                        
                                                        .. attribute:: attributes
                                                        
                                                        	Attributes
                                                        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports, self).__init__()

                                                            self.yang_name = "ports"
                                                            self.yang_parent_name = "portses"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['name']
                                                            self._child_classes = OrderedDict([("hw-components", ("hw_components", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes))])
                                                            self._leafs = OrderedDict([
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ])
                                                            self.name = None

                                                            self.hw_components = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents()
                                                            self.hw_components.parent = self
                                                            self._children_name_map["hw_components"] = "hw-components"

                                                            self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors()
                                                            self.sensors.parent = self
                                                            self._children_name_map["sensors"] = "sensors"

                                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes()
                                                            self.attributes.parent = self
                                                            self._children_name_map["attributes"] = "attributes"
                                                            self._segment_path = lambda: "ports" + "[name='" + str(self.name) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports, ['name'], name, value)


                                                        class HwComponents(Entity):
                                                            """
                                                            Table of  HW components 
                                                            
                                                            .. attribute:: hw_component
                                                            
                                                            	HW component number
                                                            	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents, self).__init__()

                                                                self.yang_name = "hw-components"
                                                                self.yang_parent_name = "ports"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("hw-component", ("hw_component", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent))])
                                                                self._leafs = OrderedDict()

                                                                self.hw_component = YList(self)
                                                                self._segment_path = lambda: "hw-components"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents, [], name, value)


                                                            class HwComponent(Entity):
                                                                """
                                                                HW component number
                                                                
                                                                .. attribute:: name  (key)
                                                                
                                                                	HW component name
                                                                	**type**\: str
                                                                
                                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                                
                                                                .. attribute:: sensors
                                                                
                                                                	Table of sensors
                                                                	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors>`
                                                                
                                                                .. attribute:: attributes
                                                                
                                                                	Attributes
                                                                	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent, self).__init__()

                                                                    self.yang_name = "hw-component"
                                                                    self.yang_parent_name = "hw-components"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = ['name']
                                                                    self._child_classes = OrderedDict([("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes))])
                                                                    self._leafs = OrderedDict([
                                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ])
                                                                    self.name = None

                                                                    self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors()
                                                                    self.sensors.parent = self
                                                                    self._children_name_map["sensors"] = "sensors"

                                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes()
                                                                    self.attributes.parent = self
                                                                    self._children_name_map["attributes"] = "attributes"
                                                                    self._segment_path = lambda: "hw-component" + "[name='" + str(self.name) + "']"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent, ['name'], name, value)


                                                                class Sensors(Entity):
                                                                    """
                                                                    Table of sensors
                                                                    
                                                                    .. attribute:: sensor
                                                                    
                                                                    	Sensor number
                                                                    	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor>`
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors, self).__init__()

                                                                        self.yang_name = "sensors"
                                                                        self.yang_parent_name = "hw-component"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor))])
                                                                        self._leafs = OrderedDict()

                                                                        self.sensor = YList(self)
                                                                        self._segment_path = lambda: "sensors"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors, [], name, value)


                                                                    class Sensor(Entity):
                                                                        """
                                                                        Sensor number
                                                                        
                                                                        .. attribute:: name  (key)
                                                                        
                                                                        	Sensor name
                                                                        	**type**\: str
                                                                        
                                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                                        
                                                                        .. attribute:: attributes
                                                                        
                                                                        	Attributes
                                                                        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes>`
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                                            self.yang_name = "sensor"
                                                                            self.yang_parent_name = "sensors"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = ['name']
                                                                            self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes))])
                                                                            self._leafs = OrderedDict([
                                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                            ])
                                                                            self.name = None

                                                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes()
                                                                            self.attributes.parent = self
                                                                            self._children_name_map["attributes"] = "attributes"
                                                                            self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, ['name'], name, value)


                                                                        class Attributes(Entity):
                                                                            """
                                                                            Attributes
                                                                            
                                                                            .. attribute:: basic_info
                                                                            
                                                                            	Entity attributes
                                                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo>`
                                                                            
                                                                            .. attribute:: fru_info
                                                                            
                                                                            	Field Replaceable Unit (FRU) attributes
                                                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo>`
                                                                            
                                                                            

                                                                            """

                                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                                            _revision = '2018-01-22'

                                                                            def __init__(self):
                                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, self).__init__()

                                                                                self.yang_name = "attributes"
                                                                                self.yang_parent_name = "sensor"
                                                                                self.is_top_level_class = False
                                                                                self.has_list_ancestor = True
                                                                                self.ylist_key_names = []
                                                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo))])
                                                                                self._leafs = OrderedDict()

                                                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo()
                                                                                self.basic_info.parent = self
                                                                                self._children_name_map["basic_info"] = "basic-info"

                                                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo()
                                                                                self.fru_info.parent = self
                                                                                self._children_name_map["fru_info"] = "fru-info"
                                                                                self._segment_path = lambda: "attributes"
                                                                                self._is_frozen = True

                                                                            def __setattr__(self, name, value):
                                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, [], name, value)


                                                                            class BasicInfo(Entity):
                                                                                """
                                                                                Entity attributes
                                                                                
                                                                                .. attribute:: name
                                                                                
                                                                                	name string for the entity
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: description
                                                                                
                                                                                	describes in user\-readable terms                 what the entity in question does
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: model_name
                                                                                
                                                                                	model name
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: hardware_revision
                                                                                
                                                                                	hw revision string
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: serial_number
                                                                                
                                                                                	serial number
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: firmware_revision
                                                                                
                                                                                	firmware revision string
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: software_revision
                                                                                
                                                                                	software revision string
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: vendor_type
                                                                                
                                                                                	maps to the vendor OID string
                                                                                	**type**\: str
                                                                                
                                                                                	**length:** 0..255
                                                                                
                                                                                .. attribute:: is_field_replaceable_unit
                                                                                
                                                                                	1 if Field Replaceable Unit 0, if not
                                                                                	**type**\: bool
                                                                                
                                                                                

                                                                                """

                                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                                _revision = '2018-01-22'

                                                                                def __init__(self):
                                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                                    self.yang_name = "basic-info"
                                                                                    self.yang_parent_name = "attributes"
                                                                                    self.is_top_level_class = False
                                                                                    self.has_list_ancestor = True
                                                                                    self.ylist_key_names = []
                                                                                    self._child_classes = OrderedDict([])
                                                                                    self._leafs = OrderedDict([
                                                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                                    ])
                                                                                    self.name = None
                                                                                    self.description = None
                                                                                    self.model_name = None
                                                                                    self.hardware_revision = None
                                                                                    self.serial_number = None
                                                                                    self.firmware_revision = None
                                                                                    self.software_revision = None
                                                                                    self.vendor_type = None
                                                                                    self.is_field_replaceable_unit = None
                                                                                    self._segment_path = lambda: "basic-info"
                                                                                    self._is_frozen = True

                                                                                def __setattr__(self, name, value):
                                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                                            class FruInfo(Entity):
                                                                                """
                                                                                Field Replaceable Unit (FRU) attributes
                                                                                
                                                                                .. attribute:: last_operational_state_change
                                                                                
                                                                                	Time operational state is   last changed
                                                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                                                
                                                                                .. attribute:: module_up_time
                                                                                
                                                                                	Module up time
                                                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                                                
                                                                                .. attribute:: module_administrative_state
                                                                                
                                                                                	Administrative    state
                                                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                                
                                                                                .. attribute:: module_power_administrative_state
                                                                                
                                                                                	Power administrative state
                                                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                                
                                                                                .. attribute:: module_operational_state
                                                                                
                                                                                	Operation state
                                                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                                
                                                                                .. attribute:: module_monitor_state
                                                                                
                                                                                	Monitor state
                                                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                                
                                                                                .. attribute:: module_reset_reason
                                                                                
                                                                                	Reset reason
                                                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                                
                                                                                

                                                                                """

                                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                                _revision = '2018-01-22'

                                                                                def __init__(self):
                                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                                    self.yang_name = "fru-info"
                                                                                    self.yang_parent_name = "attributes"
                                                                                    self.is_top_level_class = False
                                                                                    self.has_list_ancestor = True
                                                                                    self.ylist_key_names = []
                                                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                                    self._leafs = OrderedDict([
                                                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                                    ])
                                                                                    self.module_administrative_state = None
                                                                                    self.module_power_administrative_state = None
                                                                                    self.module_operational_state = None
                                                                                    self.module_monitor_state = None
                                                                                    self.module_reset_reason = None

                                                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                                    self.last_operational_state_change.parent = self
                                                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                                    self.module_up_time.parent = self
                                                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                                                    self._segment_path = lambda: "fru-info"
                                                                                    self._is_frozen = True

                                                                                def __setattr__(self, name, value):
                                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                                class LastOperationalStateChange(Entity):
                                                                                    """
                                                                                    Time operational state is   last changed
                                                                                    
                                                                                    .. attribute:: time_in_seconds
                                                                                    
                                                                                    	Time Value in Seconds
                                                                                    	**type**\: int
                                                                                    
                                                                                    	**range:** \-2147483648..2147483647
                                                                                    
                                                                                    	**units**\: second
                                                                                    
                                                                                    .. attribute:: time_in_nano_seconds
                                                                                    
                                                                                    	Time Value in Nano\-seconds
                                                                                    	**type**\: int
                                                                                    
                                                                                    	**range:** \-2147483648..2147483647
                                                                                    
                                                                                    	**units**\: nanosecond
                                                                                    
                                                                                    

                                                                                    """

                                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                                    _revision = '2018-01-22'

                                                                                    def __init__(self):
                                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                                        self.yang_name = "last-operational-state-change"
                                                                                        self.yang_parent_name = "fru-info"
                                                                                        self.is_top_level_class = False
                                                                                        self.has_list_ancestor = True
                                                                                        self.ylist_key_names = []
                                                                                        self._child_classes = OrderedDict([])
                                                                                        self._leafs = OrderedDict([
                                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                        ])
                                                                                        self.time_in_seconds = None
                                                                                        self.time_in_nano_seconds = None
                                                                                        self._segment_path = lambda: "last-operational-state-change"
                                                                                        self._is_frozen = True

                                                                                    def __setattr__(self, name, value):
                                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                                class ModuleUpTime(Entity):
                                                                                    """
                                                                                    Module up time
                                                                                    
                                                                                    .. attribute:: time_in_seconds
                                                                                    
                                                                                    	Time Value in Seconds
                                                                                    	**type**\: int
                                                                                    
                                                                                    	**range:** \-2147483648..2147483647
                                                                                    
                                                                                    	**units**\: second
                                                                                    
                                                                                    .. attribute:: time_in_nano_seconds
                                                                                    
                                                                                    	Time Value in Nano\-seconds
                                                                                    	**type**\: int
                                                                                    
                                                                                    	**range:** \-2147483648..2147483647
                                                                                    
                                                                                    	**units**\: nanosecond
                                                                                    
                                                                                    

                                                                                    """

                                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                                    _revision = '2018-01-22'

                                                                                    def __init__(self):
                                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                                        self.yang_name = "module-up-time"
                                                                                        self.yang_parent_name = "fru-info"
                                                                                        self.is_top_level_class = False
                                                                                        self.has_list_ancestor = True
                                                                                        self.ylist_key_names = []
                                                                                        self._child_classes = OrderedDict([])
                                                                                        self._leafs = OrderedDict([
                                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                        ])
                                                                                        self.time_in_seconds = None
                                                                                        self.time_in_nano_seconds = None
                                                                                        self._segment_path = lambda: "module-up-time"
                                                                                        self._is_frozen = True

                                                                                    def __setattr__(self, name, value):
                                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                class Attributes(Entity):
                                                                    """
                                                                    Attributes
                                                                    
                                                                    .. attribute:: basic_info
                                                                    
                                                                    	Entity attributes
                                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo>`
                                                                    
                                                                    .. attribute:: fru_info
                                                                    
                                                                    	Field Replaceable Unit (FRU) attributes
                                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo>`
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes, self).__init__()

                                                                        self.yang_name = "attributes"
                                                                        self.yang_parent_name = "hw-component"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo))])
                                                                        self._leafs = OrderedDict()

                                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo()
                                                                        self.basic_info.parent = self
                                                                        self._children_name_map["basic_info"] = "basic-info"

                                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo()
                                                                        self.fru_info.parent = self
                                                                        self._children_name_map["fru_info"] = "fru-info"
                                                                        self._segment_path = lambda: "attributes"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes, [], name, value)


                                                                    class BasicInfo(Entity):
                                                                        """
                                                                        Entity attributes
                                                                        
                                                                        .. attribute:: name
                                                                        
                                                                        	name string for the entity
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: description
                                                                        
                                                                        	describes in user\-readable terms                 what the entity in question does
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: model_name
                                                                        
                                                                        	model name
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: hardware_revision
                                                                        
                                                                        	hw revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: serial_number
                                                                        
                                                                        	serial number
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: firmware_revision
                                                                        
                                                                        	firmware revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: software_revision
                                                                        
                                                                        	software revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: vendor_type
                                                                        
                                                                        	maps to the vendor OID string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: is_field_replaceable_unit
                                                                        
                                                                        	1 if Field Replaceable Unit 0, if not
                                                                        	**type**\: bool
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, self).__init__()

                                                                            self.yang_name = "basic-info"
                                                                            self.yang_parent_name = "attributes"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([])
                                                                            self._leafs = OrderedDict([
                                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                            ])
                                                                            self.name = None
                                                                            self.description = None
                                                                            self.model_name = None
                                                                            self.hardware_revision = None
                                                                            self.serial_number = None
                                                                            self.firmware_revision = None
                                                                            self.software_revision = None
                                                                            self.vendor_type = None
                                                                            self.is_field_replaceable_unit = None
                                                                            self._segment_path = lambda: "basic-info"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                                    class FruInfo(Entity):
                                                                        """
                                                                        Field Replaceable Unit (FRU) attributes
                                                                        
                                                                        .. attribute:: last_operational_state_change
                                                                        
                                                                        	Time operational state is   last changed
                                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange>`
                                                                        
                                                                        .. attribute:: module_up_time
                                                                        
                                                                        	Module up time
                                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime>`
                                                                        
                                                                        .. attribute:: module_administrative_state
                                                                        
                                                                        	Administrative    state
                                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                        
                                                                        .. attribute:: module_power_administrative_state
                                                                        
                                                                        	Power administrative state
                                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                        
                                                                        .. attribute:: module_operational_state
                                                                        
                                                                        	Operation state
                                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                        
                                                                        .. attribute:: module_monitor_state
                                                                        
                                                                        	Monitor state
                                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                        
                                                                        .. attribute:: module_reset_reason
                                                                        
                                                                        	Reset reason
                                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, self).__init__()

                                                                            self.yang_name = "fru-info"
                                                                            self.yang_parent_name = "attributes"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime))])
                                                                            self._leafs = OrderedDict([
                                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                            ])
                                                                            self.module_administrative_state = None
                                                                            self.module_power_administrative_state = None
                                                                            self.module_operational_state = None
                                                                            self.module_monitor_state = None
                                                                            self.module_reset_reason = None

                                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange()
                                                                            self.last_operational_state_change.parent = self
                                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime()
                                                                            self.module_up_time.parent = self
                                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                                            self._segment_path = lambda: "fru-info"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                        class LastOperationalStateChange(Entity):
                                                                            """
                                                                            Time operational state is   last changed
                                                                            
                                                                            .. attribute:: time_in_seconds
                                                                            
                                                                            	Time Value in Seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: second
                                                                            
                                                                            .. attribute:: time_in_nano_seconds
                                                                            
                                                                            	Time Value in Nano\-seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: nanosecond
                                                                            
                                                                            

                                                                            """

                                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                                            _revision = '2018-01-22'

                                                                            def __init__(self):
                                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                                self.yang_name = "last-operational-state-change"
                                                                                self.yang_parent_name = "fru-info"
                                                                                self.is_top_level_class = False
                                                                                self.has_list_ancestor = True
                                                                                self.ylist_key_names = []
                                                                                self._child_classes = OrderedDict([])
                                                                                self._leafs = OrderedDict([
                                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                ])
                                                                                self.time_in_seconds = None
                                                                                self.time_in_nano_seconds = None
                                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                                self._is_frozen = True

                                                                            def __setattr__(self, name, value):
                                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                        class ModuleUpTime(Entity):
                                                                            """
                                                                            Module up time
                                                                            
                                                                            .. attribute:: time_in_seconds
                                                                            
                                                                            	Time Value in Seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: second
                                                                            
                                                                            .. attribute:: time_in_nano_seconds
                                                                            
                                                                            	Time Value in Nano\-seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: nanosecond
                                                                            
                                                                            

                                                                            """

                                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                                            _revision = '2018-01-22'

                                                                            def __init__(self):
                                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                                self.yang_name = "module-up-time"
                                                                                self.yang_parent_name = "fru-info"
                                                                                self.is_top_level_class = False
                                                                                self.has_list_ancestor = True
                                                                                self.ylist_key_names = []
                                                                                self._child_classes = OrderedDict([])
                                                                                self._leafs = OrderedDict([
                                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                ])
                                                                                self.time_in_seconds = None
                                                                                self.time_in_nano_seconds = None
                                                                                self._segment_path = lambda: "module-up-time"
                                                                                self._is_frozen = True

                                                                            def __setattr__(self, name, value):
                                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                        class Sensors(Entity):
                                                            """
                                                            Table of sensors
                                                            
                                                            .. attribute:: sensor
                                                            
                                                            	Sensor number
                                                            	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors, self).__init__()

                                                                self.yang_name = "sensors"
                                                                self.yang_parent_name = "ports"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor))])
                                                                self._leafs = OrderedDict()

                                                                self.sensor = YList(self)
                                                                self._segment_path = lambda: "sensors"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors, [], name, value)


                                                            class Sensor(Entity):
                                                                """
                                                                Sensor number
                                                                
                                                                .. attribute:: name  (key)
                                                                
                                                                	Sensor name
                                                                	**type**\: str
                                                                
                                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                                
                                                                .. attribute:: attributes
                                                                
                                                                	Attributes
                                                                	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor, self).__init__()

                                                                    self.yang_name = "sensor"
                                                                    self.yang_parent_name = "sensors"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = ['name']
                                                                    self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes))])
                                                                    self._leafs = OrderedDict([
                                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ])
                                                                    self.name = None

                                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes()
                                                                    self.attributes.parent = self
                                                                    self._children_name_map["attributes"] = "attributes"
                                                                    self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor, ['name'], name, value)


                                                                class Attributes(Entity):
                                                                    """
                                                                    Attributes
                                                                    
                                                                    .. attribute:: basic_info
                                                                    
                                                                    	Entity attributes
                                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo>`
                                                                    
                                                                    .. attribute:: fru_info
                                                                    
                                                                    	Field Replaceable Unit (FRU) attributes
                                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo>`
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes, self).__init__()

                                                                        self.yang_name = "attributes"
                                                                        self.yang_parent_name = "sensor"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo))])
                                                                        self._leafs = OrderedDict()

                                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo()
                                                                        self.basic_info.parent = self
                                                                        self._children_name_map["basic_info"] = "basic-info"

                                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo()
                                                                        self.fru_info.parent = self
                                                                        self._children_name_map["fru_info"] = "fru-info"
                                                                        self._segment_path = lambda: "attributes"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes, [], name, value)


                                                                    class BasicInfo(Entity):
                                                                        """
                                                                        Entity attributes
                                                                        
                                                                        .. attribute:: name
                                                                        
                                                                        	name string for the entity
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: description
                                                                        
                                                                        	describes in user\-readable terms                 what the entity in question does
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: model_name
                                                                        
                                                                        	model name
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: hardware_revision
                                                                        
                                                                        	hw revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: serial_number
                                                                        
                                                                        	serial number
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: firmware_revision
                                                                        
                                                                        	firmware revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: software_revision
                                                                        
                                                                        	software revision string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: vendor_type
                                                                        
                                                                        	maps to the vendor OID string
                                                                        	**type**\: str
                                                                        
                                                                        	**length:** 0..255
                                                                        
                                                                        .. attribute:: is_field_replaceable_unit
                                                                        
                                                                        	1 if Field Replaceable Unit 0, if not
                                                                        	**type**\: bool
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                            self.yang_name = "basic-info"
                                                                            self.yang_parent_name = "attributes"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([])
                                                                            self._leafs = OrderedDict([
                                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                            ])
                                                                            self.name = None
                                                                            self.description = None
                                                                            self.model_name = None
                                                                            self.hardware_revision = None
                                                                            self.serial_number = None
                                                                            self.firmware_revision = None
                                                                            self.software_revision = None
                                                                            self.vendor_type = None
                                                                            self.is_field_replaceable_unit = None
                                                                            self._segment_path = lambda: "basic-info"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                                    class FruInfo(Entity):
                                                                        """
                                                                        Field Replaceable Unit (FRU) attributes
                                                                        
                                                                        .. attribute:: last_operational_state_change
                                                                        
                                                                        	Time operational state is   last changed
                                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                                        
                                                                        .. attribute:: module_up_time
                                                                        
                                                                        	Module up time
                                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                                        
                                                                        .. attribute:: module_administrative_state
                                                                        
                                                                        	Administrative    state
                                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                        
                                                                        .. attribute:: module_power_administrative_state
                                                                        
                                                                        	Power administrative state
                                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                        
                                                                        .. attribute:: module_operational_state
                                                                        
                                                                        	Operation state
                                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                        
                                                                        .. attribute:: module_monitor_state
                                                                        
                                                                        	Monitor state
                                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                        
                                                                        .. attribute:: module_reset_reason
                                                                        
                                                                        	Reset reason
                                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                            self.yang_name = "fru-info"
                                                                            self.yang_parent_name = "attributes"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                            self._leafs = OrderedDict([
                                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                            ])
                                                                            self.module_administrative_state = None
                                                                            self.module_power_administrative_state = None
                                                                            self.module_operational_state = None
                                                                            self.module_monitor_state = None
                                                                            self.module_reset_reason = None

                                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                            self.last_operational_state_change.parent = self
                                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                            self.module_up_time.parent = self
                                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                                            self._segment_path = lambda: "fru-info"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                        class LastOperationalStateChange(Entity):
                                                                            """
                                                                            Time operational state is   last changed
                                                                            
                                                                            .. attribute:: time_in_seconds
                                                                            
                                                                            	Time Value in Seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: second
                                                                            
                                                                            .. attribute:: time_in_nano_seconds
                                                                            
                                                                            	Time Value in Nano\-seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: nanosecond
                                                                            
                                                                            

                                                                            """

                                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                                            _revision = '2018-01-22'

                                                                            def __init__(self):
                                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                                self.yang_name = "last-operational-state-change"
                                                                                self.yang_parent_name = "fru-info"
                                                                                self.is_top_level_class = False
                                                                                self.has_list_ancestor = True
                                                                                self.ylist_key_names = []
                                                                                self._child_classes = OrderedDict([])
                                                                                self._leafs = OrderedDict([
                                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                ])
                                                                                self.time_in_seconds = None
                                                                                self.time_in_nano_seconds = None
                                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                                self._is_frozen = True

                                                                            def __setattr__(self, name, value):
                                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                        class ModuleUpTime(Entity):
                                                                            """
                                                                            Module up time
                                                                            
                                                                            .. attribute:: time_in_seconds
                                                                            
                                                                            	Time Value in Seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: second
                                                                            
                                                                            .. attribute:: time_in_nano_seconds
                                                                            
                                                                            	Time Value in Nano\-seconds
                                                                            	**type**\: int
                                                                            
                                                                            	**range:** \-2147483648..2147483647
                                                                            
                                                                            	**units**\: nanosecond
                                                                            
                                                                            

                                                                            """

                                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                                            _revision = '2018-01-22'

                                                                            def __init__(self):
                                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                                self.yang_name = "module-up-time"
                                                                                self.yang_parent_name = "fru-info"
                                                                                self.is_top_level_class = False
                                                                                self.has_list_ancestor = True
                                                                                self.ylist_key_names = []
                                                                                self._child_classes = OrderedDict([])
                                                                                self._leafs = OrderedDict([
                                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                                ])
                                                                                self.time_in_seconds = None
                                                                                self.time_in_nano_seconds = None
                                                                                self._segment_path = lambda: "module-up-time"
                                                                                self._is_frozen = True

                                                                            def __setattr__(self, name, value):
                                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                        class Attributes(Entity):
                                                            """
                                                            Attributes
                                                            
                                                            .. attribute:: basic_info
                                                            
                                                            	Entity attributes
                                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo>`
                                                            
                                                            .. attribute:: fru_info
                                                            
                                                            	Field Replaceable Unit (FRU) attributes
                                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes, self).__init__()

                                                                self.yang_name = "attributes"
                                                                self.yang_parent_name = "ports"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo))])
                                                                self._leafs = OrderedDict()

                                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo()
                                                                self.basic_info.parent = self
                                                                self._children_name_map["basic_info"] = "basic-info"

                                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo()
                                                                self.fru_info.parent = self
                                                                self._children_name_map["fru_info"] = "fru-info"
                                                                self._segment_path = lambda: "attributes"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes, [], name, value)


                                                            class BasicInfo(Entity):
                                                                """
                                                                Entity attributes
                                                                
                                                                .. attribute:: name
                                                                
                                                                	name string for the entity
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: description
                                                                
                                                                	describes in user\-readable terms                 what the entity in question does
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: model_name
                                                                
                                                                	model name
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: hardware_revision
                                                                
                                                                	hw revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: serial_number
                                                                
                                                                	serial number
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: firmware_revision
                                                                
                                                                	firmware revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: software_revision
                                                                
                                                                	software revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: vendor_type
                                                                
                                                                	maps to the vendor OID string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: is_field_replaceable_unit
                                                                
                                                                	1 if Field Replaceable Unit 0, if not
                                                                	**type**\: bool
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo, self).__init__()

                                                                    self.yang_name = "basic-info"
                                                                    self.yang_parent_name = "attributes"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                    ])
                                                                    self.name = None
                                                                    self.description = None
                                                                    self.model_name = None
                                                                    self.hardware_revision = None
                                                                    self.serial_number = None
                                                                    self.firmware_revision = None
                                                                    self.software_revision = None
                                                                    self.vendor_type = None
                                                                    self.is_field_replaceable_unit = None
                                                                    self._segment_path = lambda: "basic-info"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                            class FruInfo(Entity):
                                                                """
                                                                Field Replaceable Unit (FRU) attributes
                                                                
                                                                .. attribute:: last_operational_state_change
                                                                
                                                                	Time operational state is   last changed
                                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange>`
                                                                
                                                                .. attribute:: module_up_time
                                                                
                                                                	Module up time
                                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime>`
                                                                
                                                                .. attribute:: module_administrative_state
                                                                
                                                                	Administrative    state
                                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                
                                                                .. attribute:: module_power_administrative_state
                                                                
                                                                	Power administrative state
                                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                
                                                                .. attribute:: module_operational_state
                                                                
                                                                	Operation state
                                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                
                                                                .. attribute:: module_monitor_state
                                                                
                                                                	Monitor state
                                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                
                                                                .. attribute:: module_reset_reason
                                                                
                                                                	Reset reason
                                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo, self).__init__()

                                                                    self.yang_name = "fru-info"
                                                                    self.yang_parent_name = "attributes"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime))])
                                                                    self._leafs = OrderedDict([
                                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                    ])
                                                                    self.module_administrative_state = None
                                                                    self.module_power_administrative_state = None
                                                                    self.module_operational_state = None
                                                                    self.module_monitor_state = None
                                                                    self.module_reset_reason = None

                                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange()
                                                                    self.last_operational_state_change.parent = self
                                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime()
                                                                    self.module_up_time.parent = self
                                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                                    self._segment_path = lambda: "fru-info"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                class LastOperationalStateChange(Entity):
                                                                    """
                                                                    Time operational state is   last changed
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: second
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: nanosecond
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                        self.yang_name = "last-operational-state-change"
                                                                        self.yang_parent_name = "fru-info"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                        ])
                                                                        self.time_in_seconds = None
                                                                        self.time_in_nano_seconds = None
                                                                        self._segment_path = lambda: "last-operational-state-change"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                class ModuleUpTime(Entity):
                                                                    """
                                                                    Module up time
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: second
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: nanosecond
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                        self.yang_name = "module-up-time"
                                                                        self.yang_parent_name = "fru-info"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                        ])
                                                                        self.time_in_seconds = None
                                                                        self.time_in_nano_seconds = None
                                                                        self._segment_path = lambda: "module-up-time"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                class Sensors(Entity):
                                                    """
                                                    Table of sensors
                                                    
                                                    .. attribute:: sensor
                                                    
                                                    	Sensor number
                                                    	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors, self).__init__()

                                                        self.yang_name = "sensors"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor))])
                                                        self._leafs = OrderedDict()

                                                        self.sensor = YList(self)
                                                        self._segment_path = lambda: "sensors"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors, [], name, value)


                                                    class Sensor(Entity):
                                                        """
                                                        Sensor number
                                                        
                                                        .. attribute:: name  (key)
                                                        
                                                        	Sensor name
                                                        	**type**\: str
                                                        
                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                        
                                                        .. attribute:: attributes
                                                        
                                                        	Attributes
                                                        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor, self).__init__()

                                                            self.yang_name = "sensor"
                                                            self.yang_parent_name = "sensors"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['name']
                                                            self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes))])
                                                            self._leafs = OrderedDict([
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ])
                                                            self.name = None

                                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes()
                                                            self.attributes.parent = self
                                                            self._children_name_map["attributes"] = "attributes"
                                                            self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor, ['name'], name, value)


                                                        class Attributes(Entity):
                                                            """
                                                            Attributes
                                                            
                                                            .. attribute:: basic_info
                                                            
                                                            	Entity attributes
                                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo>`
                                                            
                                                            .. attribute:: fru_info
                                                            
                                                            	Field Replaceable Unit (FRU) attributes
                                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes, self).__init__()

                                                                self.yang_name = "attributes"
                                                                self.yang_parent_name = "sensor"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo))])
                                                                self._leafs = OrderedDict()

                                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo()
                                                                self.basic_info.parent = self
                                                                self._children_name_map["basic_info"] = "basic-info"

                                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo()
                                                                self.fru_info.parent = self
                                                                self._children_name_map["fru_info"] = "fru-info"
                                                                self._segment_path = lambda: "attributes"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes, [], name, value)


                                                            class BasicInfo(Entity):
                                                                """
                                                                Entity attributes
                                                                
                                                                .. attribute:: name
                                                                
                                                                	name string for the entity
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: description
                                                                
                                                                	describes in user\-readable terms                 what the entity in question does
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: model_name
                                                                
                                                                	model name
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: hardware_revision
                                                                
                                                                	hw revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: serial_number
                                                                
                                                                	serial number
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: firmware_revision
                                                                
                                                                	firmware revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: software_revision
                                                                
                                                                	software revision string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: vendor_type
                                                                
                                                                	maps to the vendor OID string
                                                                	**type**\: str
                                                                
                                                                	**length:** 0..255
                                                                
                                                                .. attribute:: is_field_replaceable_unit
                                                                
                                                                	1 if Field Replaceable Unit 0, if not
                                                                	**type**\: bool
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                    self.yang_name = "basic-info"
                                                                    self.yang_parent_name = "attributes"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                    ])
                                                                    self.name = None
                                                                    self.description = None
                                                                    self.model_name = None
                                                                    self.hardware_revision = None
                                                                    self.serial_number = None
                                                                    self.firmware_revision = None
                                                                    self.software_revision = None
                                                                    self.vendor_type = None
                                                                    self.is_field_replaceable_unit = None
                                                                    self._segment_path = lambda: "basic-info"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                            class FruInfo(Entity):
                                                                """
                                                                Field Replaceable Unit (FRU) attributes
                                                                
                                                                .. attribute:: last_operational_state_change
                                                                
                                                                	Time operational state is   last changed
                                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                                
                                                                .. attribute:: module_up_time
                                                                
                                                                	Module up time
                                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                                
                                                                .. attribute:: module_administrative_state
                                                                
                                                                	Administrative    state
                                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                
                                                                .. attribute:: module_power_administrative_state
                                                                
                                                                	Power administrative state
                                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                
                                                                .. attribute:: module_operational_state
                                                                
                                                                	Operation state
                                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                
                                                                .. attribute:: module_monitor_state
                                                                
                                                                	Monitor state
                                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                
                                                                .. attribute:: module_reset_reason
                                                                
                                                                	Reset reason
                                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                    self.yang_name = "fru-info"
                                                                    self.yang_parent_name = "attributes"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                    self._leafs = OrderedDict([
                                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                    ])
                                                                    self.module_administrative_state = None
                                                                    self.module_power_administrative_state = None
                                                                    self.module_operational_state = None
                                                                    self.module_monitor_state = None
                                                                    self.module_reset_reason = None

                                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                    self.last_operational_state_change.parent = self
                                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                    self.module_up_time.parent = self
                                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                                    self._segment_path = lambda: "fru-info"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                class LastOperationalStateChange(Entity):
                                                                    """
                                                                    Time operational state is   last changed
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: second
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: nanosecond
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                        self.yang_name = "last-operational-state-change"
                                                                        self.yang_parent_name = "fru-info"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                        ])
                                                                        self.time_in_seconds = None
                                                                        self.time_in_nano_seconds = None
                                                                        self._segment_path = lambda: "last-operational-state-change"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                class ModuleUpTime(Entity):
                                                                    """
                                                                    Module up time
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: second
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    	**units**\: nanosecond
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                        self.yang_name = "module-up-time"
                                                                        self.yang_parent_name = "fru-info"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                        ])
                                                                        self.time_in_seconds = None
                                                                        self.time_in_nano_seconds = None
                                                                        self._segment_path = lambda: "module-up-time"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                class Attributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Entity attributes
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) attributes
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes, self).__init__()

                                                        self.yang_name = "attributes"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo))])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"

                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._segment_path = lambda: "attributes"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes, [], name, value)


                                                    class BasicInfo(Entity):
                                                        """
                                                        Entity attributes
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms                 what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                            ])
                                                            self.name = None
                                                            self.description = None
                                                            self.model_name = None
                                                            self.hardware_revision = None
                                                            self.serial_number = None
                                                            self.firmware_revision = None
                                                            self.software_revision = None
                                                            self.vendor_type = None
                                                            self.is_field_replaceable_unit = None
                                                            self._segment_path = lambda: "basic-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) attributes
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime>`
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime))])
                                                            self._leafs = OrderedDict([
                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                            ])
                                                            self.module_administrative_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_operational_state = None
                                                            self.module_monitor_state = None
                                                            self.module_reset_reason = None

                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self
                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                            self._segment_path = lambda: "fru-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                        class ModuleUpTime(Entity):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                self.yang_name = "module-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "module-up-time"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                        class Sensors(Entity):
                                            """
                                            Table of sensors
                                            
                                            .. attribute:: sensor
                                            
                                            	Sensor number
                                            	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, self).__init__()

                                                self.yang_name = "sensors"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor))])
                                                self._leafs = OrderedDict()

                                                self.sensor = YList(self)
                                                self._segment_path = lambda: "sensors"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, [], name, value)


                                            class Sensor(Entity):
                                                """
                                                Sensor number
                                                
                                                .. attribute:: name  (key)
                                                
                                                	Sensor name
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, self).__init__()

                                                    self.yang_name = "sensor"
                                                    self.yang_parent_name = "sensors"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['name']
                                                    self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes))])
                                                    self._leafs = OrderedDict([
                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ])
                                                    self.name = None

                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes()
                                                    self.attributes.parent = self
                                                    self._children_name_map["attributes"] = "attributes"
                                                    self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, ['name'], name, value)


                                                class Attributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Entity attributes
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) attributes
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes, self).__init__()

                                                        self.yang_name = "attributes"
                                                        self.yang_parent_name = "sensor"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo))])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"

                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._segment_path = lambda: "attributes"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes, [], name, value)


                                                    class BasicInfo(Entity):
                                                        """
                                                        Entity attributes
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms                 what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                            ])
                                                            self.name = None
                                                            self.description = None
                                                            self.model_name = None
                                                            self.hardware_revision = None
                                                            self.serial_number = None
                                                            self.firmware_revision = None
                                                            self.software_revision = None
                                                            self.vendor_type = None
                                                            self.is_field_replaceable_unit = None
                                                            self._segment_path = lambda: "basic-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) attributes
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                            self._leafs = OrderedDict([
                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                            ])
                                                            self.module_administrative_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_operational_state = None
                                                            self.module_monitor_state = None
                                                            self.module_reset_reason = None

                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self
                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                            self._segment_path = lambda: "fru-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                        class ModuleUpTime(Entity):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                self.yang_name = "module-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "module-up-time"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                        class Attributes(Entity):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Entity attributes
                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) attributes
                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes, self).__init__()

                                                self.yang_name = "attributes"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo))])
                                                self._leafs = OrderedDict()

                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self._children_name_map["basic_info"] = "basic-info"

                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo()
                                                self.fru_info.parent = self
                                                self._children_name_map["fru_info"] = "fru-info"
                                                self._segment_path = lambda: "attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes, [], name, value)


                                            class BasicInfo(Entity):
                                                """
                                                Entity attributes
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms                 what the entity in question does
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                    ])
                                                    self.name = None
                                                    self.description = None
                                                    self.model_name = None
                                                    self.hardware_revision = None
                                                    self.serial_number = None
                                                    self.firmware_revision = None
                                                    self.software_revision = None
                                                    self.vendor_type = None
                                                    self.is_field_replaceable_unit = None
                                                    self._segment_path = lambda: "basic-info"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                            class FruInfo(Entity):
                                                """
                                                Field Replaceable Unit (FRU) attributes
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	Time operational state is   last changed
                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: module_up_time
                                                
                                                	Module up time
                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime>`
                                                
                                                .. attribute:: module_administrative_state
                                                
                                                	Administrative    state
                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                
                                                .. attribute:: module_power_administrative_state
                                                
                                                	Power administrative state
                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                
                                                .. attribute:: module_operational_state
                                                
                                                	Operation state
                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                
                                                .. attribute:: module_monitor_state
                                                
                                                	Monitor state
                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                
                                                .. attribute:: module_reset_reason
                                                
                                                	Reset reason
                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime))])
                                                    self._leafs = OrderedDict([
                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                    ])
                                                    self.module_administrative_state = None
                                                    self.module_power_administrative_state = None
                                                    self.module_operational_state = None
                                                    self.module_monitor_state = None
                                                    self.module_reset_reason = None

                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime()
                                                    self.module_up_time.parent = self
                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                    self._segment_path = lambda: "fru-info"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                class LastOperationalStateChange(Entity):
                                                    """
                                                    Time operational state is   last changed
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "last-operational-state-change"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                class ModuleUpTime(Entity):
                                                    """
                                                    Module up time
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                        self.yang_name = "module-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "module-up-time"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                ])
                                                self.name = None
                                                self.description = None
                                                self.model_name = None
                                                self.hardware_revision = None
                                                self.serial_number = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.vendor_type = None
                                                self.is_field_replaceable_unit = None
                                                self._segment_path = lambda: "basic-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class Portses(Entity):
                                """
                                Table of port slots
                                
                                .. attribute:: ports
                                
                                	Port number
                                	**type**\: list of  		 :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses, self).__init__()

                                    self.yang_name = "portses"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("ports", ("ports", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports))])
                                    self._leafs = OrderedDict()

                                    self.ports = YList(self)
                                    self._segment_path = lambda: "portses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses, [], name, value)


                                class Ports(Entity):
                                    """
                                    Port number
                                    
                                    .. attribute:: name  (key)
                                    
                                    	Port name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: hw_components
                                    
                                    	Table of  HW components 
                                    	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents>`
                                    
                                    .. attribute:: sensors
                                    
                                    	Table of sensors
                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors>`
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports, self).__init__()

                                        self.yang_name = "ports"
                                        self.yang_parent_name = "portses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([("hw-components", ("hw_components", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None

                                        self.hw_components = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents()
                                        self.hw_components.parent = self
                                        self._children_name_map["hw_components"] = "hw-components"

                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"

                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._segment_path = lambda: "ports" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports, ['name'], name, value)


                                    class HwComponents(Entity):
                                        """
                                        Table of  HW components 
                                        
                                        .. attribute:: hw_component
                                        
                                        	HW component number
                                        	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents, self).__init__()

                                            self.yang_name = "hw-components"
                                            self.yang_parent_name = "ports"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("hw-component", ("hw_component", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent))])
                                            self._leafs = OrderedDict()

                                            self.hw_component = YList(self)
                                            self._segment_path = lambda: "hw-components"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents, [], name, value)


                                        class HwComponent(Entity):
                                            """
                                            HW component number
                                            
                                            .. attribute:: name  (key)
                                            
                                            	HW component name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: sensors
                                            
                                            	Table of sensors
                                            	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors>`
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent, self).__init__()

                                                self.yang_name = "hw-component"
                                                self.yang_parent_name = "hw-components"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ])
                                                self.name = None

                                                self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors()
                                                self.sensors.parent = self
                                                self._children_name_map["sensors"] = "sensors"

                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                                self._segment_path = lambda: "hw-component" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent, ['name'], name, value)


                                            class Sensors(Entity):
                                                """
                                                Table of sensors
                                                
                                                .. attribute:: sensor
                                                
                                                	Sensor number
                                                	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors, self).__init__()

                                                    self.yang_name = "sensors"
                                                    self.yang_parent_name = "hw-component"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor))])
                                                    self._leafs = OrderedDict()

                                                    self.sensor = YList(self)
                                                    self._segment_path = lambda: "sensors"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors, [], name, value)


                                                class Sensor(Entity):
                                                    """
                                                    Sensor number
                                                    
                                                    .. attribute:: name  (key)
                                                    
                                                    	Sensor name
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: attributes
                                                    
                                                    	Attributes
                                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                        self.yang_name = "sensor"
                                                        self.yang_parent_name = "sensors"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['name']
                                                        self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes))])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ])
                                                        self.name = None

                                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes()
                                                        self.attributes.parent = self
                                                        self._children_name_map["attributes"] = "attributes"
                                                        self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, ['name'], name, value)


                                                    class Attributes(Entity):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Entity attributes
                                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) attributes
                                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, self).__init__()

                                                            self.yang_name = "attributes"
                                                            self.yang_parent_name = "sensor"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo))])
                                                            self._leafs = OrderedDict()

                                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self._children_name_map["basic_info"] = "basic-info"

                                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo()
                                                            self.fru_info.parent = self
                                                            self._children_name_map["fru_info"] = "fru-info"
                                                            self._segment_path = lambda: "attributes"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, [], name, value)


                                                        class BasicInfo(Entity):
                                                            """
                                                            Entity attributes
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms                 what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                ])
                                                                self.name = None
                                                                self.description = None
                                                                self.model_name = None
                                                                self.hardware_revision = None
                                                                self.serial_number = None
                                                                self.firmware_revision = None
                                                                self.software_revision = None
                                                                self.vendor_type = None
                                                                self.is_field_replaceable_unit = None
                                                                self._segment_path = lambda: "basic-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                        class FruInfo(Entity):
                                                            """
                                                            Field Replaceable Unit (FRU) attributes
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	Time operational state is   last changed
                                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: module_up_time
                                                            
                                                            	Module up time
                                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                            
                                                            .. attribute:: module_administrative_state
                                                            
                                                            	Administrative    state
                                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                            
                                                            .. attribute:: module_power_administrative_state
                                                            
                                                            	Power administrative state
                                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                            
                                                            .. attribute:: module_operational_state
                                                            
                                                            	Operation state
                                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                            
                                                            .. attribute:: module_monitor_state
                                                            
                                                            	Monitor state
                                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                            
                                                            .. attribute:: module_reset_reason
                                                            
                                                            	Reset reason
                                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                self._leafs = OrderedDict([
                                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                ])
                                                                self.module_administrative_state = None
                                                                self.module_power_administrative_state = None
                                                                self.module_operational_state = None
                                                                self.module_monitor_state = None
                                                                self.module_reset_reason = None

                                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                self.module_up_time.parent = self
                                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                                self._segment_path = lambda: "fru-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                            class LastOperationalStateChange(Entity):
                                                                """
                                                                Time operational state is   last changed
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "last-operational-state-change"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                            class ModuleUpTime(Entity):
                                                                """
                                                                Module up time
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                    self.yang_name = "module-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "module-up-time"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class Attributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes, self).__init__()

                                                    self.yang_name = "attributes"
                                                    self.yang_parent_name = "hw-component"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ])
                                                        self.name = None
                                                        self.description = None
                                                        self.model_name = None
                                                        self.hardware_revision = None
                                                        self.serial_number = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.vendor_type = None
                                                        self.is_field_replaceable_unit = None
                                                        self._segment_path = lambda: "basic-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Sensors(Entity):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number
                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "ports"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor))])
                                            self._leafs = OrderedDict()

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors, [], name, value)


                                        class Sensor(Entity):
                                            """
                                            Sensor number
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ])
                                                self.name = None

                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                                self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor, ['name'], name, value)


                                            class Attributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes, self).__init__()

                                                    self.yang_name = "attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ])
                                                        self.name = None
                                                        self.description = None
                                                        self.model_name = None
                                                        self.hardware_revision = None
                                                        self.serial_number = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.vendor_type = None
                                                        self.is_field_replaceable_unit = None
                                                        self._segment_path = lambda: "basic-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "ports"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                ])
                                                self.name = None
                                                self.description = None
                                                self.model_name = None
                                                self.hardware_revision = None
                                                self.serial_number = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.vendor_type = None
                                                self.is_field_replaceable_unit = None
                                                self._segment_path = lambda: "basic-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class PortSlots(Entity):
                                """
                                Table of port slots
                                
                                .. attribute:: port_slot
                                
                                	Port slot number
                                	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, self).__init__()

                                    self.yang_name = "port-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("port-slot", ("port_slot", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot))])
                                    self._leafs = OrderedDict()

                                    self.port_slot = YList(self)
                                    self._segment_path = lambda: "port-slots"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, [], name, value)


                                class PortSlot(Entity):
                                    """
                                    Port slot number
                                    
                                    .. attribute:: name  (key)
                                    
                                    	Port slot name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: portses
                                    
                                    	Table of port slots
                                    	**type**\:  :py:class:`Portses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses>`
                                    
                                    .. attribute:: sensors
                                    
                                    	Table of sensors
                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors>`
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, self).__init__()

                                        self.yang_name = "port-slot"
                                        self.yang_parent_name = "port-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([("portses", ("portses", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None

                                        self.portses = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses()
                                        self.portses.parent = self
                                        self._children_name_map["portses"] = "portses"

                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"

                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._segment_path = lambda: "port-slot" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, ['name'], name, value)


                                    class Portses(Entity):
                                        """
                                        Table of port slots
                                        
                                        .. attribute:: ports
                                        
                                        	Port number
                                        	**type**\: list of  		 :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses, self).__init__()

                                            self.yang_name = "portses"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ports", ("ports", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports))])
                                            self._leafs = OrderedDict()

                                            self.ports = YList(self)
                                            self._segment_path = lambda: "portses"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses, [], name, value)


                                        class Ports(Entity):
                                            """
                                            Port number
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Port name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: hw_components
                                            
                                            	Table of  HW components 
                                            	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents>`
                                            
                                            .. attribute:: sensors
                                            
                                            	Table of sensors
                                            	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors>`
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports, self).__init__()

                                                self.yang_name = "ports"
                                                self.yang_parent_name = "portses"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("hw-components", ("hw_components", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents)), ("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ])
                                                self.name = None

                                                self.hw_components = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents()
                                                self.hw_components.parent = self
                                                self._children_name_map["hw_components"] = "hw-components"

                                                self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors()
                                                self.sensors.parent = self
                                                self._children_name_map["sensors"] = "sensors"

                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                                self._segment_path = lambda: "ports" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports, ['name'], name, value)


                                            class HwComponents(Entity):
                                                """
                                                Table of  HW components 
                                                
                                                .. attribute:: hw_component
                                                
                                                	HW component number
                                                	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents, self).__init__()

                                                    self.yang_name = "hw-components"
                                                    self.yang_parent_name = "ports"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("hw-component", ("hw_component", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent))])
                                                    self._leafs = OrderedDict()

                                                    self.hw_component = YList(self)
                                                    self._segment_path = lambda: "hw-components"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents, [], name, value)


                                                class HwComponent(Entity):
                                                    """
                                                    HW component number
                                                    
                                                    .. attribute:: name  (key)
                                                    
                                                    	HW component name
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: sensors
                                                    
                                                    	Table of sensors
                                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors>`
                                                    
                                                    .. attribute:: attributes
                                                    
                                                    	Attributes
                                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent, self).__init__()

                                                        self.yang_name = "hw-component"
                                                        self.yang_parent_name = "hw-components"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['name']
                                                        self._child_classes = OrderedDict([("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes))])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ])
                                                        self.name = None

                                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors()
                                                        self.sensors.parent = self
                                                        self._children_name_map["sensors"] = "sensors"

                                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes()
                                                        self.attributes.parent = self
                                                        self._children_name_map["attributes"] = "attributes"
                                                        self._segment_path = lambda: "hw-component" + "[name='" + str(self.name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent, ['name'], name, value)


                                                    class Sensors(Entity):
                                                        """
                                                        Table of sensors
                                                        
                                                        .. attribute:: sensor
                                                        
                                                        	Sensor number
                                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors, self).__init__()

                                                            self.yang_name = "sensors"
                                                            self.yang_parent_name = "hw-component"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor))])
                                                            self._leafs = OrderedDict()

                                                            self.sensor = YList(self)
                                                            self._segment_path = lambda: "sensors"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors, [], name, value)


                                                        class Sensor(Entity):
                                                            """
                                                            Sensor number
                                                            
                                                            .. attribute:: name  (key)
                                                            
                                                            	Sensor name
                                                            	**type**\: str
                                                            
                                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                            
                                                            .. attribute:: attributes
                                                            
                                                            	Attributes
                                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                                self.yang_name = "sensor"
                                                                self.yang_parent_name = "sensors"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = ['name']
                                                                self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes))])
                                                                self._leafs = OrderedDict([
                                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                ])
                                                                self.name = None

                                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes()
                                                                self.attributes.parent = self
                                                                self._children_name_map["attributes"] = "attributes"
                                                                self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor, ['name'], name, value)


                                                            class Attributes(Entity):
                                                                """
                                                                Attributes
                                                                
                                                                .. attribute:: basic_info
                                                                
                                                                	Entity attributes
                                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo>`
                                                                
                                                                .. attribute:: fru_info
                                                                
                                                                	Field Replaceable Unit (FRU) attributes
                                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, self).__init__()

                                                                    self.yang_name = "attributes"
                                                                    self.yang_parent_name = "sensor"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo))])
                                                                    self._leafs = OrderedDict()

                                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo()
                                                                    self.basic_info.parent = self
                                                                    self._children_name_map["basic_info"] = "basic-info"

                                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo()
                                                                    self.fru_info.parent = self
                                                                    self._children_name_map["fru_info"] = "fru-info"
                                                                    self._segment_path = lambda: "attributes"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes, [], name, value)


                                                                class BasicInfo(Entity):
                                                                    """
                                                                    Entity attributes
                                                                    
                                                                    .. attribute:: name
                                                                    
                                                                    	name string for the entity
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: description
                                                                    
                                                                    	describes in user\-readable terms                 what the entity in question does
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: model_name
                                                                    
                                                                    	model name
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: hardware_revision
                                                                    
                                                                    	hw revision string
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: serial_number
                                                                    
                                                                    	serial number
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: firmware_revision
                                                                    
                                                                    	firmware revision string
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: software_revision
                                                                    
                                                                    	software revision string
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: vendor_type
                                                                    
                                                                    	maps to the vendor OID string
                                                                    	**type**\: str
                                                                    
                                                                    	**length:** 0..255
                                                                    
                                                                    .. attribute:: is_field_replaceable_unit
                                                                    
                                                                    	1 if Field Replaceable Unit 0, if not
                                                                    	**type**\: bool
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                        self.yang_name = "basic-info"
                                                                        self.yang_parent_name = "attributes"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([])
                                                                        self._leafs = OrderedDict([
                                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                        ])
                                                                        self.name = None
                                                                        self.description = None
                                                                        self.model_name = None
                                                                        self.hardware_revision = None
                                                                        self.serial_number = None
                                                                        self.firmware_revision = None
                                                                        self.software_revision = None
                                                                        self.vendor_type = None
                                                                        self.is_field_replaceable_unit = None
                                                                        self._segment_path = lambda: "basic-info"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                                class FruInfo(Entity):
                                                                    """
                                                                    Field Replaceable Unit (FRU) attributes
                                                                    
                                                                    .. attribute:: last_operational_state_change
                                                                    
                                                                    	Time operational state is   last changed
                                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                                    
                                                                    .. attribute:: module_up_time
                                                                    
                                                                    	Module up time
                                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                                    
                                                                    .. attribute:: module_administrative_state
                                                                    
                                                                    	Administrative    state
                                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                                    
                                                                    .. attribute:: module_power_administrative_state
                                                                    
                                                                    	Power administrative state
                                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                                    
                                                                    .. attribute:: module_operational_state
                                                                    
                                                                    	Operation state
                                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                                    
                                                                    .. attribute:: module_monitor_state
                                                                    
                                                                    	Monitor state
                                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                                    
                                                                    .. attribute:: module_reset_reason
                                                                    
                                                                    	Reset reason
                                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                                    _revision = '2018-01-22'

                                                                    def __init__(self):
                                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                        self.yang_name = "fru-info"
                                                                        self.yang_parent_name = "attributes"
                                                                        self.is_top_level_class = False
                                                                        self.has_list_ancestor = True
                                                                        self.ylist_key_names = []
                                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                        self._leafs = OrderedDict([
                                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                        ])
                                                                        self.module_administrative_state = None
                                                                        self.module_power_administrative_state = None
                                                                        self.module_operational_state = None
                                                                        self.module_monitor_state = None
                                                                        self.module_reset_reason = None

                                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                        self.last_operational_state_change.parent = self
                                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                        self.module_up_time.parent = self
                                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                                        self._segment_path = lambda: "fru-info"
                                                                        self._is_frozen = True

                                                                    def __setattr__(self, name, value):
                                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                                    class LastOperationalStateChange(Entity):
                                                                        """
                                                                        Time operational state is   last changed
                                                                        
                                                                        .. attribute:: time_in_seconds
                                                                        
                                                                        	Time Value in Seconds
                                                                        	**type**\: int
                                                                        
                                                                        	**range:** \-2147483648..2147483647
                                                                        
                                                                        	**units**\: second
                                                                        
                                                                        .. attribute:: time_in_nano_seconds
                                                                        
                                                                        	Time Value in Nano\-seconds
                                                                        	**type**\: int
                                                                        
                                                                        	**range:** \-2147483648..2147483647
                                                                        
                                                                        	**units**\: nanosecond
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                            self.yang_name = "last-operational-state-change"
                                                                            self.yang_parent_name = "fru-info"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([])
                                                                            self._leafs = OrderedDict([
                                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                            ])
                                                                            self.time_in_seconds = None
                                                                            self.time_in_nano_seconds = None
                                                                            self._segment_path = lambda: "last-operational-state-change"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                                    class ModuleUpTime(Entity):
                                                                        """
                                                                        Module up time
                                                                        
                                                                        .. attribute:: time_in_seconds
                                                                        
                                                                        	Time Value in Seconds
                                                                        	**type**\: int
                                                                        
                                                                        	**range:** \-2147483648..2147483647
                                                                        
                                                                        	**units**\: second
                                                                        
                                                                        .. attribute:: time_in_nano_seconds
                                                                        
                                                                        	Time Value in Nano\-seconds
                                                                        	**type**\: int
                                                                        
                                                                        	**range:** \-2147483648..2147483647
                                                                        
                                                                        	**units**\: nanosecond
                                                                        
                                                                        

                                                                        """

                                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                                        _revision = '2018-01-22'

                                                                        def __init__(self):
                                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                            self.yang_name = "module-up-time"
                                                                            self.yang_parent_name = "fru-info"
                                                                            self.is_top_level_class = False
                                                                            self.has_list_ancestor = True
                                                                            self.ylist_key_names = []
                                                                            self._child_classes = OrderedDict([])
                                                                            self._leafs = OrderedDict([
                                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                            ])
                                                                            self.time_in_seconds = None
                                                                            self.time_in_nano_seconds = None
                                                                            self._segment_path = lambda: "module-up-time"
                                                                            self._is_frozen = True

                                                                        def __setattr__(self, name, value):
                                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class Attributes(Entity):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Entity attributes
                                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) attributes
                                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes, self).__init__()

                                                            self.yang_name = "attributes"
                                                            self.yang_parent_name = "hw-component"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo))])
                                                            self._leafs = OrderedDict()

                                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self._children_name_map["basic_info"] = "basic-info"

                                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo()
                                                            self.fru_info.parent = self
                                                            self._children_name_map["fru_info"] = "fru-info"
                                                            self._segment_path = lambda: "attributes"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes, [], name, value)


                                                        class BasicInfo(Entity):
                                                            """
                                                            Entity attributes
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms                 what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                ])
                                                                self.name = None
                                                                self.description = None
                                                                self.model_name = None
                                                                self.hardware_revision = None
                                                                self.serial_number = None
                                                                self.firmware_revision = None
                                                                self.software_revision = None
                                                                self.vendor_type = None
                                                                self.is_field_replaceable_unit = None
                                                                self._segment_path = lambda: "basic-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                        class FruInfo(Entity):
                                                            """
                                                            Field Replaceable Unit (FRU) attributes
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	Time operational state is   last changed
                                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: module_up_time
                                                            
                                                            	Module up time
                                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime>`
                                                            
                                                            .. attribute:: module_administrative_state
                                                            
                                                            	Administrative    state
                                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                            
                                                            .. attribute:: module_power_administrative_state
                                                            
                                                            	Power administrative state
                                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                            
                                                            .. attribute:: module_operational_state
                                                            
                                                            	Operation state
                                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                            
                                                            .. attribute:: module_monitor_state
                                                            
                                                            	Monitor state
                                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                            
                                                            .. attribute:: module_reset_reason
                                                            
                                                            	Reset reason
                                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime))])
                                                                self._leafs = OrderedDict([
                                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                ])
                                                                self.module_administrative_state = None
                                                                self.module_power_administrative_state = None
                                                                self.module_operational_state = None
                                                                self.module_monitor_state = None
                                                                self.module_reset_reason = None

                                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime()
                                                                self.module_up_time.parent = self
                                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                                self._segment_path = lambda: "fru-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                            class LastOperationalStateChange(Entity):
                                                                """
                                                                Time operational state is   last changed
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "last-operational-state-change"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                            class ModuleUpTime(Entity):
                                                                """
                                                                Module up time
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                    self.yang_name = "module-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "module-up-time"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class Sensors(Entity):
                                                """
                                                Table of sensors
                                                
                                                .. attribute:: sensor
                                                
                                                	Sensor number
                                                	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors, self).__init__()

                                                    self.yang_name = "sensors"
                                                    self.yang_parent_name = "ports"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor))])
                                                    self._leafs = OrderedDict()

                                                    self.sensor = YList(self)
                                                    self._segment_path = lambda: "sensors"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors, [], name, value)


                                                class Sensor(Entity):
                                                    """
                                                    Sensor number
                                                    
                                                    .. attribute:: name  (key)
                                                    
                                                    	Sensor name
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: attributes
                                                    
                                                    	Attributes
                                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor, self).__init__()

                                                        self.yang_name = "sensor"
                                                        self.yang_parent_name = "sensors"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['name']
                                                        self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes))])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ])
                                                        self.name = None

                                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes()
                                                        self.attributes.parent = self
                                                        self._children_name_map["attributes"] = "attributes"
                                                        self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor, ['name'], name, value)


                                                    class Attributes(Entity):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Entity attributes
                                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) attributes
                                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes, self).__init__()

                                                            self.yang_name = "attributes"
                                                            self.yang_parent_name = "sensor"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo))])
                                                            self._leafs = OrderedDict()

                                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self._children_name_map["basic_info"] = "basic-info"

                                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo()
                                                            self.fru_info.parent = self
                                                            self._children_name_map["fru_info"] = "fru-info"
                                                            self._segment_path = lambda: "attributes"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes, [], name, value)


                                                        class BasicInfo(Entity):
                                                            """
                                                            Entity attributes
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms                 what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                ])
                                                                self.name = None
                                                                self.description = None
                                                                self.model_name = None
                                                                self.hardware_revision = None
                                                                self.serial_number = None
                                                                self.firmware_revision = None
                                                                self.software_revision = None
                                                                self.vendor_type = None
                                                                self.is_field_replaceable_unit = None
                                                                self._segment_path = lambda: "basic-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                        class FruInfo(Entity):
                                                            """
                                                            Field Replaceable Unit (FRU) attributes
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	Time operational state is   last changed
                                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: module_up_time
                                                            
                                                            	Module up time
                                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                            
                                                            .. attribute:: module_administrative_state
                                                            
                                                            	Administrative    state
                                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                            
                                                            .. attribute:: module_power_administrative_state
                                                            
                                                            	Power administrative state
                                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                            
                                                            .. attribute:: module_operational_state
                                                            
                                                            	Operation state
                                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                            
                                                            .. attribute:: module_monitor_state
                                                            
                                                            	Monitor state
                                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                            
                                                            .. attribute:: module_reset_reason
                                                            
                                                            	Reset reason
                                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                                            _revision = '2018-01-22'

                                                            def __init__(self):
                                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                                self._leafs = OrderedDict([
                                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                                ])
                                                                self.module_administrative_state = None
                                                                self.module_power_administrative_state = None
                                                                self.module_operational_state = None
                                                                self.module_monitor_state = None
                                                                self.module_reset_reason = None

                                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                self.module_up_time.parent = self
                                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                                self._segment_path = lambda: "fru-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                            class LastOperationalStateChange(Entity):
                                                                """
                                                                Time operational state is   last changed
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "last-operational-state-change"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                            class ModuleUpTime(Entity):
                                                                """
                                                                Module up time
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                                _revision = '2018-01-22'

                                                                def __init__(self):
                                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                                    self.yang_name = "module-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "module-up-time"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class Attributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes, self).__init__()

                                                    self.yang_name = "attributes"
                                                    self.yang_parent_name = "ports"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ])
                                                        self.name = None
                                                        self.description = None
                                                        self.model_name = None
                                                        self.hardware_revision = None
                                                        self.serial_number = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.vendor_type = None
                                                        self.is_field_replaceable_unit = None
                                                        self._segment_path = lambda: "basic-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Sensors(Entity):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number
                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor))])
                                            self._leafs = OrderedDict()

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors, [], name, value)


                                        class Sensor(Entity):
                                            """
                                            Sensor number
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ])
                                                self.name = None

                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                                self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor, ['name'], name, value)


                                            class Attributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes, self).__init__()

                                                    self.yang_name = "attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ])
                                                        self.name = None
                                                        self.description = None
                                                        self.model_name = None
                                                        self.hardware_revision = None
                                                        self.serial_number = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.vendor_type = None
                                                        self.is_field_replaceable_unit = None
                                                        self._segment_path = lambda: "basic-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                ])
                                                self.name = None
                                                self.description = None
                                                self.model_name = None
                                                self.hardware_revision = None
                                                self.serial_number = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.vendor_type = None
                                                self.is_field_replaceable_unit = None
                                                self._segment_path = lambda: "basic-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class HwComponents(Entity):
                                """
                                Table of  HW components 
                                
                                .. attribute:: hw_component
                                
                                	HW component number
                                	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, self).__init__()

                                    self.yang_name = "hw-components"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("hw-component", ("hw_component", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent))])
                                    self._leafs = OrderedDict()

                                    self.hw_component = YList(self)
                                    self._segment_path = lambda: "hw-components"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, [], name, value)


                                class HwComponent(Entity):
                                    """
                                    HW component number
                                    
                                    .. attribute:: name  (key)
                                    
                                    	HW component name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: sensors
                                    
                                    	Table of sensors
                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors>`
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, self).__init__()

                                        self.yang_name = "hw-component"
                                        self.yang_parent_name = "hw-components"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([("sensors", ("sensors", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors)), ("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None

                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"

                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._segment_path = lambda: "hw-component" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, ['name'], name, value)


                                    class Sensors(Entity):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number
                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor))])
                                            self._leafs = OrderedDict()

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, [], name, value)


                                        class Sensor(Entity):
                                            """
                                            Sensor number
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ])
                                                self.name = None

                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                                self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, ['name'], name, value)


                                            class Attributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes, self).__init__()

                                                    self.yang_name = "attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ])
                                                        self.name = None
                                                        self.description = None
                                                        self.model_name = None
                                                        self.hardware_revision = None
                                                        self.serial_number = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.vendor_type = None
                                                        self.is_field_replaceable_unit = None
                                                        self._segment_path = lambda: "basic-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                                    _revision = '2018-01-22'

                                                    def __init__(self):
                                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                                        _revision = '2018-01-22'

                                                        def __init__(self):
                                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                ])
                                                self.name = None
                                                self.description = None
                                                self.model_name = None
                                                self.hardware_revision = None
                                                self.serial_number = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.vendor_type = None
                                                self.is_field_replaceable_unit = None
                                                self._segment_path = lambda: "basic-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class Sensors(Entity):
                                """
                                Table of sensors
                                
                                .. attribute:: sensor
                                
                                	Sensor number
                                	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, self).__init__()

                                    self.yang_name = "sensors"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sensor", ("sensor", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor))])
                                    self._leafs = OrderedDict()

                                    self.sensor = YList(self)
                                    self._segment_path = lambda: "sensors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, [], name, value)


                                class Sensor(Entity):
                                    """
                                    Sensor number
                                    
                                    .. attribute:: name  (key)
                                    
                                    	Sensor name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, self).__init__()

                                        self.yang_name = "sensor"
                                        self.yang_parent_name = "sensors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([("attributes", ("attributes", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None

                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._segment_path = lambda: "sensor" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, ['name'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "sensor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                ])
                                                self.name = None
                                                self.description = None
                                                self.model_name = None
                                                self.hardware_revision = None
                                                self.serial_number = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.vendor_type = None
                                                self.is_field_replaceable_unit = None
                                                self._segment_path = lambda: "basic-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-ng-oper'
                                            _revision = '2018-01-22'

                                            def __init__(self):
                                                super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-ng-oper'
                                                _revision = '2018-01-22'

                                                def __init__(self):
                                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class Attributes(Entity):
                                """
                                Attributes
                                
                                .. attribute:: basic_info
                                
                                	Entity attributes
                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo>`
                                
                                .. attribute:: fru_info
                                
                                	Field Replaceable Unit (FRU) attributes
                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes, self).__init__()

                                    self.yang_name = "attributes"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo))])
                                    self._leafs = OrderedDict()

                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo()
                                    self.basic_info.parent = self
                                    self._children_name_map["basic_info"] = "basic-info"

                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo()
                                    self.fru_info.parent = self
                                    self._children_name_map["fru_info"] = "fru-info"
                                    self._segment_path = lambda: "attributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes, [], name, value)


                                class BasicInfo(Entity):
                                    """
                                    Entity attributes
                                    
                                    .. attribute:: name
                                    
                                    	name string for the entity
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: description
                                    
                                    	describes in user\-readable terms                 what the entity in question does
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: model_name
                                    
                                    	model name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	hw revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: serial_number
                                    
                                    	serial number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: firmware_revision
                                    
                                    	firmware revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: software_revision
                                    
                                    	software revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: vendor_type
                                    
                                    	maps to the vendor OID string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: is_field_replaceable_unit
                                    
                                    	1 if Field Replaceable Unit 0, if not
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo, self).__init__()

                                        self.yang_name = "basic-info"
                                        self.yang_parent_name = "attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                        ])
                                        self.name = None
                                        self.description = None
                                        self.model_name = None
                                        self.hardware_revision = None
                                        self.serial_number = None
                                        self.firmware_revision = None
                                        self.software_revision = None
                                        self.vendor_type = None
                                        self.is_field_replaceable_unit = None
                                        self._segment_path = lambda: "basic-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                                class FruInfo(Entity):
                                    """
                                    Field Replaceable Unit (FRU) attributes
                                    
                                    .. attribute:: last_operational_state_change
                                    
                                    	Time operational state is   last changed
                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange>`
                                    
                                    .. attribute:: module_up_time
                                    
                                    	Module up time
                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime>`
                                    
                                    .. attribute:: module_administrative_state
                                    
                                    	Administrative    state
                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                                    
                                    .. attribute:: module_power_administrative_state
                                    
                                    	Power administrative state
                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                                    
                                    .. attribute:: module_operational_state
                                    
                                    	Operation state
                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                                    
                                    .. attribute:: module_monitor_state
                                    
                                    	Monitor state
                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                                    
                                    .. attribute:: module_reset_reason
                                    
                                    	Reset reason
                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-ng-oper'
                                    _revision = '2018-01-22'

                                    def __init__(self):
                                        super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo, self).__init__()

                                        self.yang_name = "fru-info"
                                        self.yang_parent_name = "attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime))])
                                        self._leafs = OrderedDict([
                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                        ])
                                        self.module_administrative_state = None
                                        self.module_power_administrative_state = None
                                        self.module_operational_state = None
                                        self.module_monitor_state = None
                                        self.module_reset_reason = None

                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime()
                                        self.module_up_time.parent = self
                                        self._children_name_map["module_up_time"] = "module-up-time"
                                        self._segment_path = lambda: "fru-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                    class LastOperationalStateChange(Entity):
                                        """
                                        Time operational state is   last changed
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                            self.yang_name = "last-operational-state-change"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "last-operational-state-change"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                                    class ModuleUpTime(Entity):
                                        """
                                        Module up time
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-ng-oper'
                                        _revision = '2018-01-22'

                                        def __init__(self):
                                            super(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                            self.yang_name = "module-up-time"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "module-up-time"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                    class Attributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Entity attributes
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo>`
                        
                        .. attribute:: fru_info
                        
                        	Field Replaceable Unit (FRU) attributes
                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(PlatformInventory.Racks.Rack.Slots.Slot.Attributes, self).__init__()

                            self.yang_name = "attributes"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo))])
                            self._leafs = OrderedDict()

                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo()
                            self.fru_info.parent = self
                            self._children_name_map["fru_info"] = "fru-info"
                            self._segment_path = lambda: "attributes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Attributes, [], name, value)


                        class BasicInfo(Entity):
                            """
                            Entity attributes
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms                 what the entity in question does
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-ng-oper'
                            _revision = '2018-01-22'

                            def __init__(self):
                                super(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                ])
                                self.name = None
                                self.description = None
                                self.model_name = None
                                self.hardware_revision = None
                                self.serial_number = None
                                self.firmware_revision = None
                                self.software_revision = None
                                self.vendor_type = None
                                self.is_field_replaceable_unit = None
                                self._segment_path = lambda: "basic-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                        class FruInfo(Entity):
                            """
                            Field Replaceable Unit (FRU) attributes
                            
                            .. attribute:: last_operational_state_change
                            
                            	Time operational state is   last changed
                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange>`
                            
                            .. attribute:: module_up_time
                            
                            	Module up time
                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime>`
                            
                            .. attribute:: module_administrative_state
                            
                            	Administrative    state
                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                            
                            .. attribute:: module_power_administrative_state
                            
                            	Power administrative state
                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                            
                            .. attribute:: module_operational_state
                            
                            	Operation state
                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                            
                            .. attribute:: module_monitor_state
                            
                            	Monitor state
                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                            
                            .. attribute:: module_reset_reason
                            
                            	Reset reason
                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-ng-oper'
                            _revision = '2018-01-22'

                            def __init__(self):
                                super(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo, self).__init__()

                                self.yang_name = "fru-info"
                                self.yang_parent_name = "attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime))])
                                self._leafs = OrderedDict([
                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                                ])
                                self.module_administrative_state = None
                                self.module_power_administrative_state = None
                                self.module_operational_state = None
                                self.module_monitor_state = None
                                self.module_reset_reason = None

                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime()
                                self.module_up_time.parent = self
                                self._children_name_map["module_up_time"] = "module-up-time"
                                self._segment_path = lambda: "fru-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                            class LastOperationalStateChange(Entity):
                                """
                                Time operational state is   last changed
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                                    self.yang_name = "last-operational-state-change"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "last-operational-state-change"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                            class ModuleUpTime(Entity):
                                """
                                Module up time
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-ng-oper'
                                _revision = '2018-01-22'

                                def __init__(self):
                                    super(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime, self).__init__()

                                    self.yang_name = "module-up-time"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "module-up-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


            class Attributes(Entity):
                """
                Attributes
                
                .. attribute:: basic_info
                
                	Entity attributes
                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Attributes.BasicInfo>`
                
                .. attribute:: fru_info
                
                	Field Replaceable Unit (FRU) attributes
                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo>`
                
                

                """

                _prefix = 'plat-chas-invmgr-ng-oper'
                _revision = '2018-01-22'

                def __init__(self):
                    super(PlatformInventory.Racks.Rack.Attributes, self).__init__()

                    self.yang_name = "attributes"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("basic-info", ("basic_info", PlatformInventory.Racks.Rack.Attributes.BasicInfo)), ("fru-info", ("fru_info", PlatformInventory.Racks.Rack.Attributes.FruInfo))])
                    self._leafs = OrderedDict()

                    self.basic_info = PlatformInventory.Racks.Rack.Attributes.BasicInfo()
                    self.basic_info.parent = self
                    self._children_name_map["basic_info"] = "basic-info"

                    self.fru_info = PlatformInventory.Racks.Rack.Attributes.FruInfo()
                    self.fru_info.parent = self
                    self._children_name_map["fru_info"] = "fru-info"
                    self._segment_path = lambda: "attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformInventory.Racks.Rack.Attributes, [], name, value)


                class BasicInfo(Entity):
                    """
                    Entity attributes
                    
                    .. attribute:: name
                    
                    	name string for the entity
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: description
                    
                    	describes in user\-readable terms                 what the entity in question does
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: model_name
                    
                    	model name
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: hardware_revision
                    
                    	hw revision string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: serial_number
                    
                    	serial number
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: firmware_revision
                    
                    	firmware revision string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: software_revision
                    
                    	software revision string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: vendor_type
                    
                    	maps to the vendor OID string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: is_field_replaceable_unit
                    
                    	1 if Field Replaceable Unit 0, if not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-ng-oper'
                    _revision = '2018-01-22'

                    def __init__(self):
                        super(PlatformInventory.Racks.Rack.Attributes.BasicInfo, self).__init__()

                        self.yang_name = "basic-info"
                        self.yang_parent_name = "attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                        ])
                        self.name = None
                        self.description = None
                        self.model_name = None
                        self.hardware_revision = None
                        self.serial_number = None
                        self.firmware_revision = None
                        self.software_revision = None
                        self.vendor_type = None
                        self.is_field_replaceable_unit = None
                        self._segment_path = lambda: "basic-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformInventory.Racks.Rack.Attributes.BasicInfo, [u'name', u'description', u'model_name', u'hardware_revision', u'serial_number', u'firmware_revision', u'software_revision', u'vendor_type', u'is_field_replaceable_unit'], name, value)


                class FruInfo(Entity):
                    """
                    Field Replaceable Unit (FRU) attributes
                    
                    .. attribute:: last_operational_state_change
                    
                    	Time operational state is   last changed
                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange>`
                    
                    .. attribute:: module_up_time
                    
                    	Module up time
                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime>`
                    
                    .. attribute:: module_administrative_state
                    
                    	Administrative    state
                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvAdminState>`
                    
                    .. attribute:: module_power_administrative_state
                    
                    	Power administrative state
                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvPowerAdminState>`
                    
                    .. attribute:: module_operational_state
                    
                    	Operation state
                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvCardState>`
                    
                    .. attribute:: module_monitor_state
                    
                    	Monitor state
                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvMonitorState>`
                    
                    .. attribute:: module_reset_reason
                    
                    	Reset reason
                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper.InvResetReason>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-ng-oper'
                    _revision = '2018-01-22'

                    def __init__(self):
                        super(PlatformInventory.Racks.Rack.Attributes.FruInfo, self).__init__()

                        self.yang_name = "fru-info"
                        self.yang_parent_name = "attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime))])
                        self._leafs = OrderedDict([
                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvAdminState', '')])),
                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvPowerAdminState', '')])),
                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvCardState', '')])),
                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvMonitorState', '')])),
                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_ng_oper', 'InvResetReason', '')])),
                        ])
                        self.module_administrative_state = None
                        self.module_power_administrative_state = None
                        self.module_operational_state = None
                        self.module_monitor_state = None
                        self.module_reset_reason = None

                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange()
                        self.last_operational_state_change.parent = self
                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                        self.module_up_time = PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime()
                        self.module_up_time.parent = self
                        self._children_name_map["module_up_time"] = "module-up-time"
                        self._segment_path = lambda: "fru-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformInventory.Racks.Rack.Attributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                    class LastOperationalStateChange(Entity):
                        """
                        Time operational state is   last changed
                        
                        .. attribute:: time_in_seconds
                        
                        	Time Value in Seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: second
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Time Value in Nano\-seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange, self).__init__()

                            self.yang_name = "last-operational-state-change"
                            self.yang_parent_name = "fru-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                            ])
                            self.time_in_seconds = None
                            self.time_in_nano_seconds = None
                            self._segment_path = lambda: "last-operational-state-change"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)


                    class ModuleUpTime(Entity):
                        """
                        Module up time
                        
                        .. attribute:: time_in_seconds
                        
                        	Time Value in Seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: second
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Time Value in Nano\-seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-ng-oper'
                        _revision = '2018-01-22'

                        def __init__(self):
                            super(PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime, self).__init__()

                            self.yang_name = "module-up-time"
                            self.yang_parent_name = "fru-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                            ])
                            self.time_in_seconds = None
                            self.time_in_nano_seconds = None
                            self._segment_path = lambda: "module-up-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformInventory()
        return self._top_entity

