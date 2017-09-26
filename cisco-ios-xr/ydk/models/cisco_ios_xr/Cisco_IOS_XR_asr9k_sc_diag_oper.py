""" Cisco_IOS_XR_asr9k_sc_diag_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-diag package operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag admin operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DiagNode(Enum):
    """
    DiagNode

    Node types

    .. data:: node = 0

    	Node type is node

    .. data:: spa = 1

    	Node type is SPA

    """

    node = Enum.YLeaf(0, "node")

    spa = Enum.YLeaf(1, "spa")


class DiagProcessor(Enum):
    """
    DiagProcessor

    Processor types

    .. data:: mpc8614d = 0

    	Processor type 8614D

    """

    mpc8614d = Enum.YLeaf(0, "mpc8614d")


class DiagSlot(Enum):
    """
    DiagSlot

    Slot types

    .. data:: fan_tray = 0

    	Slot type is fan tray

    .. data:: power_module = 1

    	Slot type is power module

    .. data:: module = 2

    	Slot type is module

    """

    fan_tray = Enum.YLeaf(0, "fan-tray")

    power_module = Enum.YLeaf(1, "power-module")

    module = Enum.YLeaf(2, "module")


class NodeState(Enum):
    """
    NodeState

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



class Diag(Entity):
    """
    Diag admin operational data
    
    .. attribute:: racks
    
    	Diag operational data for available racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-diag-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Diag, self).__init__()
        self._top_entity = None

        self.yang_name = "diag"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-diag-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"racks" : ("racks", Diag.Racks)}
        self._child_list_classes = {}

        self.racks = Diag.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-oper:diag"


    class Racks(Entity):
        """
        Diag operational data for available racks
        
        .. attribute:: rack
        
        	Diag operational data for a particular rack
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-diag-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Diag.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rack" : ("rack", Diag.Racks.Rack)}

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-oper:diag/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Racks, [], name, value)


        class Rack(Entity):
            """
            Diag operational data for a particular rack
            
            .. attribute:: rack_name  <key>
            
            	Rack name
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slots
            
            	Diag operational data for all available slots
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots>`
            
            .. attribute:: summary
            
            	Summary information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Summary>`
            
            

            """

            _prefix = 'asr9k-sc-diag-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Diag.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"slots" : ("slots", Diag.Racks.Rack.Slots), "summary" : ("summary", Diag.Racks.Rack.Summary)}
                self._child_list_classes = {}

                self.rack_name = YLeaf(YType.int32, "rack-name")

                self.slots = Diag.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")

                self.summary = Diag.Racks.Rack.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
                self._segment_path = lambda: "rack" + "[rack-name='" + self.rack_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-oper:diag/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Racks.Rack, ['rack_name'], name, value)


            class Slots(Entity):
                """
                Diag operational data for all available slots
                
                .. attribute:: slot
                
                	Diag operational data for a particular slot
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"slot" : ("slot", Diag.Racks.Rack.Slots.Slot)}

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Diag operational data for a particular slot
                    
                    .. attribute:: slot_name  <key>
                    
                    	Slot name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: detail
                    
                    	Slot detailed information
                    	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail>`
                    
                    .. attribute:: instances
                    
                    	Diag operational data for all available instances
                    	**type**\:   :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"detail" : ("detail", Diag.Racks.Rack.Slots.Slot.Detail), "instances" : ("instances", Diag.Racks.Rack.Slots.Slot.Instances)}
                        self._child_list_classes = {}

                        self.slot_name = YLeaf(YType.str, "slot-name")

                        self.detail = Diag.Racks.Rack.Slots.Slot.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")

                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"
                        self._children_yang_names.add("instances")
                        self._segment_path = lambda: "slot" + "[slot-name='" + self.slot_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot, ['slot_name'], name, value)


                    class Detail(Entity):
                        """
                        Slot detailed information
                        
                        .. attribute:: node_detail
                        
                        	Detail information for slot
                        	**type**\: list of    :py:class:`NodeDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail>`
                        
                        .. attribute:: spa_detail
                        
                        	Detail information for spa
                        	**type**\: list of    :py:class:`SpaDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"node-detail" : ("node_detail", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail), "spa-detail" : ("spa_detail", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail)}

                            self.node_detail = YList(self)
                            self.spa_detail = YList(self)
                            self._segment_path = lambda: "detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail, [], name, value)


                        class NodeDetail(Entity):
                            """
                            Detail information for slot
                            
                            .. attribute:: board_state
                            
                            	Module operational state
                            	**type**\:   :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.NodeState>`
                            
                            .. attribute:: cbc_active_partition
                            
                            	CBC active partition
                            	**type**\:   :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition>`
                            
                            .. attribute:: cbc_inactive_partition
                            
                            	CBC inactive partition
                            	**type**\:   :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition>`
                            
                            .. attribute:: chip_hardware_revision
                            
                            	Chip hardware revision
                            	**type**\:  str
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\:  str
                            
                            .. attribute:: cpu0
                            
                            	Processor type
                            	**type**\:   :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.DiagProcessor>`
                            
                            .. attribute:: description
                            
                            	Describes in user\-readable terms
                            	**type**\:  str
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:   :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision>`
                            
                            .. attribute:: monlib
                            
                            	MONLIB version
                            	**type**\:  str
                            
                            .. attribute:: new_deviation_number
                            
                            	New deviation number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\:  str
                            
                            .. attribute:: pld
                            
                            	Programmable logic device information
                            	**type**\:   :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld>`
                            
                            .. attribute:: pld_motherboard
                            
                            	Motherboard PLD version
                            	**type**\:  str
                            
                            .. attribute:: pld_power
                            
                            	Power PLD version
                            	**type**\:  str
                            
                            .. attribute:: rommon
                            
                            	ROMMON version
                            	**type**\:  str
                            
                            .. attribute:: serial_number
                            
                            	Main serial number
                            	**type**\:  str
                            
                            .. attribute:: tan
                            
                            	Top assembly number
                            	**type**\:  str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail, self).__init__()

                                self.yang_name = "node-detail"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"cbc-active-partition" : ("cbc_active_partition", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition), "cbc-inactive-partition" : ("cbc_inactive_partition", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition), "hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision), "pld" : ("pld", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld)}
                                self._child_list_classes = {}

                                self.board_state = YLeaf(YType.enumeration, "board-state")

                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                self.clei = YLeaf(YType.str, "clei")

                                self.cpu0 = YLeaf(YType.enumeration, "cpu0")

                                self.description = YLeaf(YType.str, "description")

                                self.monlib = YLeaf(YType.str, "monlib")

                                self.new_deviation_number = YLeaf(YType.uint32, "new-deviation-number")

                                self.pid = YLeaf(YType.str, "pid")

                                self.pld_motherboard = YLeaf(YType.str, "pld-motherboard")

                                self.pld_power = YLeaf(YType.str, "pld-power")

                                self.rommon = YLeaf(YType.str, "rommon")

                                self.serial_number = YLeaf(YType.str, "serial-number")

                                self.tan = YLeaf(YType.str, "tan")

                                self.vid = YLeaf(YType.str, "vid")

                                self.cbc_active_partition = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition()
                                self.cbc_active_partition.parent = self
                                self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                self._children_yang_names.add("cbc-active-partition")

                                self.cbc_inactive_partition = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition()
                                self.cbc_inactive_partition.parent = self
                                self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                self._children_yang_names.add("cbc-inactive-partition")

                                self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")

                                self.pld = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld()
                                self.pld.parent = self
                                self._children_name_map["pld"] = "pld"
                                self._children_yang_names.add("pld")
                                self._segment_path = lambda: "node-detail"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail, ['board_state', 'chip_hardware_revision', 'clei', 'cpu0', 'description', 'monlib', 'new_deviation_number', 'pid', 'pld_motherboard', 'pld_power', 'rommon', 'serial_number', 'tan', 'vid'], name, value)


                            class CbcActivePartition(Entity):
                                """
                                CBC active partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition, self).__init__()

                                    self.yang_name = "cbc-active-partition"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                    self._segment_path = lambda: "cbc-active-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                            class CbcInactivePartition(Entity):
                                """
                                CBC inactive partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition, self).__init__()

                                    self.yang_name = "cbc-inactive-partition"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                    self._segment_path = lambda: "cbc-inactive-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of    :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision)}

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision, [], name, value)


                                class HardwareRevision(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:   :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.DimmRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:   :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.FwRev>`
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:   :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.HwRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\:  str
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:   :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SsdRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:   :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SwRev>`
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"dimm-rev" : ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.DimmRev), "fw-rev" : ("fw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.FwRev), "hw-rev" : ("hw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.HwRev), "ssd-rev" : ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SsdRev), "sw-rev" : ("sw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SwRev)}
                                        self._child_list_classes = {}

                                        self.node_description = YLeaf(YType.str, "node-description")

                                        self.version = YLeaf(YType.str, "version")

                                        self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.fw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.hw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")

                                        self.sw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision, ['node_description', 'version'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\:  str
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.cas = YLeaf(YType.uint32, "cas")

                                            self.locator = YLeaf(YType.str, "locator")

                                            self.size = YLeaf(YType.uint32, "size")

                                            self.speed = YLeaf(YType.uint32, "speed")
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.DimmRev, ['cas', 'locator', 'size', 'speed'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\:  str
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\:  str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.fw_rev = YLeaf(YType.str, "fw-rev")

                                            self.number = YLeaf(YType.str, "number")

                                            self.serial_number = YLeaf(YType.str, "serial-number")
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SsdRev, ['fw_rev', 'number', 'serial_number'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision.SwRev, ['major_revision', 'minor_revision'], name, value)


                            class Pld(Entity):
                                """
                                Programmable logic device information
                                
                                .. attribute:: processor_higher_version
                                
                                	HigherVerion
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_lower_version
                                
                                	LowerVersion
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Processor PLD version
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld, self).__init__()

                                    self.yang_name = "pld"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.processor_higher_version = YLeaf(YType.uint32, "processor-higher-version")

                                    self.processor_lower_version = YLeaf(YType.uint32, "processor-lower-version")

                                    self.type = YLeaf(YType.uint32, "type")
                                    self._segment_path = lambda: "pld"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld, ['processor_higher_version', 'processor_lower_version', 'type'], name, value)


                        class SpaDetail(Entity):
                            """
                            Detail information for spa
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\:  str
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:   :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision>`
                            
                            .. attribute:: main
                            
                            	Main
                            	**type**\:   :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main>`
                            
                            .. attribute:: name
                            
                            	SPA name
                            	**type**\:  str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: node_state
                            
                            	Node state
                            	**type**\:   :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.NodeState>`
                            
                            .. attribute:: pca_revision
                            
                            	PCA revision information
                            	**type**\:  str
                            
                            .. attribute:: pca_unit_number
                            
                            	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                            	**type**\:  str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\:  str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail, self).__init__()

                                self.yang_name = "spa-detail"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision), "main" : ("main", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main)}
                                self._child_list_classes = {}

                                self.clei = YLeaf(YType.str, "clei")

                                self.name = YLeaf(YType.str, "name")

                                self.node = YLeaf(YType.str, "node")

                                self.node_state = YLeaf(YType.enumeration, "node-state")

                                self.pca_revision = YLeaf(YType.str, "pca-revision")

                                self.pca_unit_number = YLeaf(YType.str, "pca-unit-number")

                                self.pid = YLeaf(YType.str, "pid")

                                self.vid = YLeaf(YType.str, "vid")

                                self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")

                                self.main = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main()
                                self.main.parent = self
                                self._children_name_map["main"] = "main"
                                self._children_yang_names.add("main")
                                self._segment_path = lambda: "spa-detail"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail, ['clei', 'name', 'node', 'node_state', 'pca_revision', 'pca_unit_number', 'pid', 'vid'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of    :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "spa-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision)}

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision, [], name, value)


                                class HardwareRevision(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:   :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.DimmRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:   :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.FwRev>`
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:   :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.HwRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\:  str
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:   :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SsdRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:   :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SwRev>`
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"dimm-rev" : ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.DimmRev), "fw-rev" : ("fw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.FwRev), "hw-rev" : ("hw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.HwRev), "ssd-rev" : ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SsdRev), "sw-rev" : ("sw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SwRev)}
                                        self._child_list_classes = {}

                                        self.node_description = YLeaf(YType.str, "node-description")

                                        self.version = YLeaf(YType.str, "version")

                                        self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.fw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.hw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")

                                        self.sw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision, ['node_description', 'version'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\:  str
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.cas = YLeaf(YType.uint32, "cas")

                                            self.locator = YLeaf(YType.str, "locator")

                                            self.size = YLeaf(YType.uint32, "size")

                                            self.speed = YLeaf(YType.uint32, "speed")
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.DimmRev, ['cas', 'locator', 'size', 'speed'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\:  str
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\:  str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.fw_rev = YLeaf(YType.str, "fw-rev")

                                            self.number = YLeaf(YType.str, "number")

                                            self.serial_number = YLeaf(YType.str, "serial-number")
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SsdRev, ['fw_rev', 'number', 'serial_number'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision.SwRev, ['major_revision', 'minor_revision'], name, value)


                            class Main(Entity):
                                """
                                Main
                                
                                .. attribute:: board_type
                                
                                	Board type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: deviation_number
                                
                                	Deviation number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: serial_number
                                
                                	Serial number
                                	**type**\:  str
                                
                                .. attribute:: tan
                                
                                	Top assembly number
                                	**type**\:  str
                                
                                .. attribute:: tan_revision
                                
                                	Top assembly number revision
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main, self).__init__()

                                    self.yang_name = "main"
                                    self.yang_parent_name = "spa-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.board_type = YLeaf(YType.uint32, "board-type")

                                    self.deviation_number = YLeaf(YType.uint32, "deviation-number")

                                    self.serial_number = YLeaf(YType.str, "serial-number")

                                    self.tan = YLeaf(YType.str, "tan")

                                    self.tan_revision = YLeaf(YType.str, "tan-revision")
                                    self._segment_path = lambda: "main"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main, ['board_type', 'deviation_number', 'serial_number', 'tan', 'tan_revision'], name, value)


                    class Instances(Entity):
                        """
                        Diag operational data for all available
                        instances
                        
                        .. attribute:: instance
                        
                        	Diag operational data for a particular instance
                        	**type**\: list of    :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Instances, self).__init__()

                            self.yang_name = "instances"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"instance" : ("instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance)}

                            self.instance = YList(self)
                            self._segment_path = lambda: "instances"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances, [], name, value)


                        class Instance(Entity):
                            """
                            Diag operational data for a particular
                            instance
                            
                            .. attribute:: instance_name  <key>
                            
                            	Instance name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: detail
                            
                            	Diag detailed information
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__init__()

                                self.yang_name = "instance"
                                self.yang_parent_name = "instances"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"detail" : ("detail", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail)}
                                self._child_list_classes = {}

                                self.instance_name = YLeaf(YType.str, "instance-name")

                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")
                                self._segment_path = lambda: "instance" + "[instance-name='" + self.instance_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance, ['instance_name'], name, value)


                            class Detail(Entity):
                                """
                                Diag detailed information
                                
                                .. attribute:: node
                                
                                	Node information
                                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node>`
                                
                                .. attribute:: spa
                                
                                	SPA information
                                	**type**\:   :py:class:`Spa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "instance"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"node" : ("node", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node), "spa" : ("spa", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa)}
                                    self._child_list_classes = {}

                                    self.node = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node()
                                    self.node.parent = self
                                    self._children_name_map["node"] = "node"
                                    self._children_yang_names.add("node")

                                    self.spa = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa()
                                    self.spa.parent = self
                                    self._children_name_map["spa"] = "spa"
                                    self._children_yang_names.add("spa")
                                    self._segment_path = lambda: "detail"


                                class Node(Entity):
                                    """
                                    Node information
                                    
                                    .. attribute:: board_state
                                    
                                    	Module operational state
                                    	**type**\:   :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.NodeState>`
                                    
                                    .. attribute:: cbc_active_partition
                                    
                                    	CBC active partition
                                    	**type**\:   :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition>`
                                    
                                    .. attribute:: cbc_inactive_partition
                                    
                                    	CBC inactive partition
                                    	**type**\:   :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition>`
                                    
                                    .. attribute:: chip_hardware_revision
                                    
                                    	Chip hardware revision
                                    	**type**\:  str
                                    
                                    .. attribute:: clei
                                    
                                    	CLEI
                                    	**type**\:  str
                                    
                                    .. attribute:: cpu0
                                    
                                    	Processor type
                                    	**type**\:   :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.DiagProcessor>`
                                    
                                    .. attribute:: description
                                    
                                    	Describes in user\-readable terms
                                    	**type**\:  str
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	Hardware revision
                                    	**type**\:   :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision>`
                                    
                                    .. attribute:: monlib
                                    
                                    	MONLIB version
                                    	**type**\:  str
                                    
                                    .. attribute:: new_deviation_number
                                    
                                    	New deviation number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pid
                                    
                                    	PID
                                    	**type**\:  str
                                    
                                    .. attribute:: pld
                                    
                                    	Programmable logic device information
                                    	**type**\:   :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld>`
                                    
                                    .. attribute:: pld_motherboard
                                    
                                    	Motherboard PLD version
                                    	**type**\:  str
                                    
                                    .. attribute:: pld_power
                                    
                                    	Power PLD version
                                    	**type**\:  str
                                    
                                    .. attribute:: rommon
                                    
                                    	ROMMON version
                                    	**type**\:  str
                                    
                                    .. attribute:: serial_number
                                    
                                    	Main serial number
                                    	**type**\:  str
                                    
                                    .. attribute:: tan
                                    
                                    	Top assembly number
                                    	**type**\:  str
                                    
                                    .. attribute:: vid
                                    
                                    	VID
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node, self).__init__()

                                        self.yang_name = "node"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"cbc-active-partition" : ("cbc_active_partition", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition), "cbc-inactive-partition" : ("cbc_inactive_partition", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition), "hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision), "pld" : ("pld", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld)}
                                        self._child_list_classes = {}

                                        self.board_state = YLeaf(YType.enumeration, "board-state")

                                        self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                        self.clei = YLeaf(YType.str, "clei")

                                        self.cpu0 = YLeaf(YType.enumeration, "cpu0")

                                        self.description = YLeaf(YType.str, "description")

                                        self.monlib = YLeaf(YType.str, "monlib")

                                        self.new_deviation_number = YLeaf(YType.uint32, "new-deviation-number")

                                        self.pid = YLeaf(YType.str, "pid")

                                        self.pld_motherboard = YLeaf(YType.str, "pld-motherboard")

                                        self.pld_power = YLeaf(YType.str, "pld-power")

                                        self.rommon = YLeaf(YType.str, "rommon")

                                        self.serial_number = YLeaf(YType.str, "serial-number")

                                        self.tan = YLeaf(YType.str, "tan")

                                        self.vid = YLeaf(YType.str, "vid")

                                        self.cbc_active_partition = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition()
                                        self.cbc_active_partition.parent = self
                                        self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                        self._children_yang_names.add("cbc-active-partition")

                                        self.cbc_inactive_partition = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition()
                                        self.cbc_inactive_partition.parent = self
                                        self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                        self._children_yang_names.add("cbc-inactive-partition")

                                        self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision()
                                        self.hardware_revision.parent = self
                                        self._children_name_map["hardware_revision"] = "hardware-revision"
                                        self._children_yang_names.add("hardware-revision")

                                        self.pld = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld()
                                        self.pld.parent = self
                                        self._children_name_map["pld"] = "pld"
                                        self._children_yang_names.add("pld")
                                        self._segment_path = lambda: "node"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node, ['board_state', 'chip_hardware_revision', 'clei', 'cpu0', 'description', 'monlib', 'new_deviation_number', 'pid', 'pld_motherboard', 'pld_power', 'rommon', 'serial_number', 'tan', 'vid'], name, value)


                                    class CbcActivePartition(Entity):
                                        """
                                        CBC active partition
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition, self).__init__()

                                            self.yang_name = "cbc-active-partition"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "cbc-active-partition"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                                    class CbcInactivePartition(Entity):
                                        """
                                        CBC inactive partition
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition, self).__init__()

                                            self.yang_name = "cbc-inactive-partition"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.major_revision = YLeaf(YType.uint32, "major-revision")

                                            self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                            self._segment_path = lambda: "cbc-inactive-partition"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                                    class HardwareRevision(Entity):
                                        """
                                        Hardware revision
                                        
                                        .. attribute:: hardware_revision
                                        
                                        	Board FPGA/CPLD/ASIC hardware revision
                                        	**type**\: list of    :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision, self).__init__()

                                            self.yang_name = "hardware-revision"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision)}

                                            self.hardware_revision = YList(self)
                                            self._segment_path = lambda: "hardware-revision"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision, [], name, value)


                                        class HardwareRevision(Entity):
                                            """
                                            Board FPGA/CPLD/ASIC hardware revision
                                            
                                            .. attribute:: dimm_rev
                                            
                                            	DIMM version information
                                            	**type**\:   :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.DimmRev>`
                                            
                                            .. attribute:: fw_rev
                                            
                                            	Firmware version
                                            	**type**\:   :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.FwRev>`
                                            
                                            .. attribute:: hw_rev
                                            
                                            	Hardware version
                                            	**type**\:   :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.HwRev>`
                                            
                                            .. attribute:: node_description
                                            
                                            	Node decsription
                                            	**type**\:  str
                                            
                                            .. attribute:: ssd_rev
                                            
                                            	SSD version information
                                            	**type**\:   :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SsdRev>`
                                            
                                            .. attribute:: sw_rev
                                            
                                            	Software version
                                            	**type**\:   :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SwRev>`
                                            
                                            .. attribute:: version
                                            
                                            	Version information
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-diag-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision, self).__init__()

                                                self.yang_name = "hardware-revision"
                                                self.yang_parent_name = "hardware-revision"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"dimm-rev" : ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.DimmRev), "fw-rev" : ("fw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.FwRev), "hw-rev" : ("hw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.HwRev), "ssd-rev" : ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SsdRev), "sw-rev" : ("sw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SwRev)}
                                                self._child_list_classes = {}

                                                self.node_description = YLeaf(YType.str, "node-description")

                                                self.version = YLeaf(YType.str, "version")

                                                self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.DimmRev()
                                                self.dimm_rev.parent = self
                                                self._children_name_map["dimm_rev"] = "dimm-rev"
                                                self._children_yang_names.add("dimm-rev")

                                                self.fw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.FwRev()
                                                self.fw_rev.parent = self
                                                self._children_name_map["fw_rev"] = "fw-rev"
                                                self._children_yang_names.add("fw-rev")

                                                self.hw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.HwRev()
                                                self.hw_rev.parent = self
                                                self._children_name_map["hw_rev"] = "hw-rev"
                                                self._children_yang_names.add("hw-rev")

                                                self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SsdRev()
                                                self.ssd_rev.parent = self
                                                self._children_name_map["ssd_rev"] = "ssd-rev"
                                                self._children_yang_names.add("ssd-rev")

                                                self.sw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SwRev()
                                                self.sw_rev.parent = self
                                                self._children_name_map["sw_rev"] = "sw-rev"
                                                self._children_yang_names.add("sw-rev")
                                                self._segment_path = lambda: "hardware-revision"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision, ['node_description', 'version'], name, value)


                                            class DimmRev(Entity):
                                                """
                                                DIMM version information
                                                
                                                .. attribute:: cas
                                                
                                                	Column address strobe latency in clock cycles
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: locator
                                                
                                                	Locator information
                                                	**type**\:  str
                                                
                                                .. attribute:: size
                                                
                                                	Size in MB
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: speed
                                                
                                                	Speed in MHz
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.DimmRev, self).__init__()

                                                    self.yang_name = "dimm-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.cas = YLeaf(YType.uint32, "cas")

                                                    self.locator = YLeaf(YType.str, "locator")

                                                    self.size = YLeaf(YType.uint32, "size")

                                                    self.speed = YLeaf(YType.uint32, "speed")
                                                    self._segment_path = lambda: "dimm-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.DimmRev, ['cas', 'locator', 'size', 'speed'], name, value)


                                            class FwRev(Entity):
                                                """
                                                Firmware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.FwRev, self).__init__()

                                                    self.yang_name = "fw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "fw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.FwRev, ['major_revision', 'minor_revision'], name, value)


                                            class HwRev(Entity):
                                                """
                                                Hardware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.HwRev, self).__init__()

                                                    self.yang_name = "hw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "hw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.HwRev, ['major_revision', 'minor_revision'], name, value)


                                            class SsdRev(Entity):
                                                """
                                                SSD version information
                                                
                                                .. attribute:: fw_rev
                                                
                                                	Firmware revision
                                                	**type**\:  str
                                                
                                                .. attribute:: number
                                                
                                                	SSD number
                                                	**type**\:  str
                                                
                                                .. attribute:: serial_number
                                                
                                                	Serial number
                                                	**type**\:  str
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SsdRev, self).__init__()

                                                    self.yang_name = "ssd-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.fw_rev = YLeaf(YType.str, "fw-rev")

                                                    self.number = YLeaf(YType.str, "number")

                                                    self.serial_number = YLeaf(YType.str, "serial-number")
                                                    self._segment_path = lambda: "ssd-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SsdRev, ['fw_rev', 'number', 'serial_number'], name, value)


                                            class SwRev(Entity):
                                                """
                                                Software version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SwRev, self).__init__()

                                                    self.yang_name = "sw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "sw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class Pld(Entity):
                                        """
                                        Programmable logic device information
                                        
                                        .. attribute:: processor_higher_version
                                        
                                        	HigherVerion
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: processor_lower_version
                                        
                                        	LowerVersion
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: type
                                        
                                        	Processor PLD version
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld, self).__init__()

                                            self.yang_name = "pld"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.processor_higher_version = YLeaf(YType.uint32, "processor-higher-version")

                                            self.processor_lower_version = YLeaf(YType.uint32, "processor-lower-version")

                                            self.type = YLeaf(YType.uint32, "type")
                                            self._segment_path = lambda: "pld"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld, ['processor_higher_version', 'processor_lower_version', 'type'], name, value)


                                class Spa(Entity):
                                    """
                                    SPA information
                                    
                                    .. attribute:: clei
                                    
                                    	CLEI
                                    	**type**\:  str
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	Hardware revision
                                    	**type**\:   :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision>`
                                    
                                    .. attribute:: main
                                    
                                    	Main
                                    	**type**\:   :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main>`
                                    
                                    .. attribute:: name
                                    
                                    	SPA name
                                    	**type**\:  str
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\:  str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    .. attribute:: node_state
                                    
                                    	Node state
                                    	**type**\:   :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.NodeState>`
                                    
                                    .. attribute:: pca_revision
                                    
                                    	PCA revision information
                                    	**type**\:  str
                                    
                                    .. attribute:: pca_unit_number
                                    
                                    	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                                    	**type**\:  str
                                    
                                    .. attribute:: pid
                                    
                                    	PID
                                    	**type**\:  str
                                    
                                    .. attribute:: vid
                                    
                                    	VID
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa, self).__init__()

                                        self.yang_name = "spa"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision), "main" : ("main", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main)}
                                        self._child_list_classes = {}

                                        self.clei = YLeaf(YType.str, "clei")

                                        self.name = YLeaf(YType.str, "name")

                                        self.node = YLeaf(YType.str, "node")

                                        self.node_state = YLeaf(YType.enumeration, "node-state")

                                        self.pca_revision = YLeaf(YType.str, "pca-revision")

                                        self.pca_unit_number = YLeaf(YType.str, "pca-unit-number")

                                        self.pid = YLeaf(YType.str, "pid")

                                        self.vid = YLeaf(YType.str, "vid")

                                        self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision()
                                        self.hardware_revision.parent = self
                                        self._children_name_map["hardware_revision"] = "hardware-revision"
                                        self._children_yang_names.add("hardware-revision")

                                        self.main = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main()
                                        self.main.parent = self
                                        self._children_name_map["main"] = "main"
                                        self._children_yang_names.add("main")
                                        self._segment_path = lambda: "spa"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa, ['clei', 'name', 'node', 'node_state', 'pca_revision', 'pca_unit_number', 'pid', 'vid'], name, value)


                                    class HardwareRevision(Entity):
                                        """
                                        Hardware revision
                                        
                                        .. attribute:: hardware_revision
                                        
                                        	Board FPGA/CPLD/ASIC hardware revision
                                        	**type**\: list of    :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision, self).__init__()

                                            self.yang_name = "hardware-revision"
                                            self.yang_parent_name = "spa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"hardware-revision" : ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision)}

                                            self.hardware_revision = YList(self)
                                            self._segment_path = lambda: "hardware-revision"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision, [], name, value)


                                        class HardwareRevision(Entity):
                                            """
                                            Board FPGA/CPLD/ASIC hardware revision
                                            
                                            .. attribute:: dimm_rev
                                            
                                            	DIMM version information
                                            	**type**\:   :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.DimmRev>`
                                            
                                            .. attribute:: fw_rev
                                            
                                            	Firmware version
                                            	**type**\:   :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.FwRev>`
                                            
                                            .. attribute:: hw_rev
                                            
                                            	Hardware version
                                            	**type**\:   :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.HwRev>`
                                            
                                            .. attribute:: node_description
                                            
                                            	Node decsription
                                            	**type**\:  str
                                            
                                            .. attribute:: ssd_rev
                                            
                                            	SSD version information
                                            	**type**\:   :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SsdRev>`
                                            
                                            .. attribute:: sw_rev
                                            
                                            	Software version
                                            	**type**\:   :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SwRev>`
                                            
                                            .. attribute:: version
                                            
                                            	Version information
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-diag-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision, self).__init__()

                                                self.yang_name = "hardware-revision"
                                                self.yang_parent_name = "hardware-revision"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"dimm-rev" : ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.DimmRev), "fw-rev" : ("fw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.FwRev), "hw-rev" : ("hw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.HwRev), "ssd-rev" : ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SsdRev), "sw-rev" : ("sw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SwRev)}
                                                self._child_list_classes = {}

                                                self.node_description = YLeaf(YType.str, "node-description")

                                                self.version = YLeaf(YType.str, "version")

                                                self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.DimmRev()
                                                self.dimm_rev.parent = self
                                                self._children_name_map["dimm_rev"] = "dimm-rev"
                                                self._children_yang_names.add("dimm-rev")

                                                self.fw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.FwRev()
                                                self.fw_rev.parent = self
                                                self._children_name_map["fw_rev"] = "fw-rev"
                                                self._children_yang_names.add("fw-rev")

                                                self.hw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.HwRev()
                                                self.hw_rev.parent = self
                                                self._children_name_map["hw_rev"] = "hw-rev"
                                                self._children_yang_names.add("hw-rev")

                                                self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SsdRev()
                                                self.ssd_rev.parent = self
                                                self._children_name_map["ssd_rev"] = "ssd-rev"
                                                self._children_yang_names.add("ssd-rev")

                                                self.sw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SwRev()
                                                self.sw_rev.parent = self
                                                self._children_name_map["sw_rev"] = "sw-rev"
                                                self._children_yang_names.add("sw-rev")
                                                self._segment_path = lambda: "hardware-revision"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision, ['node_description', 'version'], name, value)


                                            class DimmRev(Entity):
                                                """
                                                DIMM version information
                                                
                                                .. attribute:: cas
                                                
                                                	Column address strobe latency in clock cycles
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: locator
                                                
                                                	Locator information
                                                	**type**\:  str
                                                
                                                .. attribute:: size
                                                
                                                	Size in MB
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: speed
                                                
                                                	Speed in MHz
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.DimmRev, self).__init__()

                                                    self.yang_name = "dimm-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.cas = YLeaf(YType.uint32, "cas")

                                                    self.locator = YLeaf(YType.str, "locator")

                                                    self.size = YLeaf(YType.uint32, "size")

                                                    self.speed = YLeaf(YType.uint32, "speed")
                                                    self._segment_path = lambda: "dimm-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.DimmRev, ['cas', 'locator', 'size', 'speed'], name, value)


                                            class FwRev(Entity):
                                                """
                                                Firmware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.FwRev, self).__init__()

                                                    self.yang_name = "fw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "fw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.FwRev, ['major_revision', 'minor_revision'], name, value)


                                            class HwRev(Entity):
                                                """
                                                Hardware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.HwRev, self).__init__()

                                                    self.yang_name = "hw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "hw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.HwRev, ['major_revision', 'minor_revision'], name, value)


                                            class SsdRev(Entity):
                                                """
                                                SSD version information
                                                
                                                .. attribute:: fw_rev
                                                
                                                	Firmware revision
                                                	**type**\:  str
                                                
                                                .. attribute:: number
                                                
                                                	SSD number
                                                	**type**\:  str
                                                
                                                .. attribute:: serial_number
                                                
                                                	Serial number
                                                	**type**\:  str
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SsdRev, self).__init__()

                                                    self.yang_name = "ssd-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.fw_rev = YLeaf(YType.str, "fw-rev")

                                                    self.number = YLeaf(YType.str, "number")

                                                    self.serial_number = YLeaf(YType.str, "serial-number")
                                                    self._segment_path = lambda: "ssd-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SsdRev, ['fw_rev', 'number', 'serial_number'], name, value)


                                            class SwRev(Entity):
                                                """
                                                Software version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SwRev, self).__init__()

                                                    self.yang_name = "sw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.major_revision = YLeaf(YType.uint32, "major-revision")

                                                    self.minor_revision = YLeaf(YType.uint32, "minor-revision")
                                                    self._segment_path = lambda: "sw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class Main(Entity):
                                        """
                                        Main
                                        
                                        .. attribute:: board_type
                                        
                                        	Board type
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: deviation_number
                                        
                                        	Deviation number
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\:  str
                                        
                                        .. attribute:: tan
                                        
                                        	Top assembly number
                                        	**type**\:  str
                                        
                                        .. attribute:: tan_revision
                                        
                                        	Top assembly number revision
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main, self).__init__()

                                            self.yang_name = "main"
                                            self.yang_parent_name = "spa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.board_type = YLeaf(YType.uint32, "board-type")

                                            self.deviation_number = YLeaf(YType.uint32, "deviation-number")

                                            self.serial_number = YLeaf(YType.str, "serial-number")

                                            self.tan = YLeaf(YType.str, "tan")

                                            self.tan_revision = YLeaf(YType.str, "tan-revision")
                                            self._segment_path = lambda: "main"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main, ['board_type', 'deviation_number', 'serial_number', 'tan', 'tan_revision'], name, value)


            class Summary(Entity):
                """
                Summary information
                
                .. attribute:: summary
                
                	Summary data
                	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.Diag.Racks.Rack.Summary.Summary>`
                
                

                """

                _prefix = 'asr9k-sc-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"summary" : ("summary", Diag.Racks.Rack.Summary.Summary)}

                    self.summary = YList(self)
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Summary, [], name, value)


                class Summary(Entity):
                    """
                    Summary data
                    
                    .. attribute:: description
                    
                    	Description
                    	**type**\:  str
                    
                    .. attribute:: node
                    
                    	Node ID
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: slot_type
                    
                    	Slot type
                    	**type**\:   :py:class:`DiagSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.DiagSlot>`
                    
                    .. attribute:: type
                    
                    	Node type
                    	**type**\:   :py:class:`DiagNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_oper.DiagNode>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Summary.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.description = YLeaf(YType.str, "description")

                        self.node = YLeaf(YType.str, "node")

                        self.slot_type = YLeaf(YType.enumeration, "slot-type")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Summary.Summary, ['description', 'node', 'slot_type', 'type'], name, value)

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

