""" Cisco_IOS_XR_asr9k_sc_diag_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-diag package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag admin operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DiagNode(Enum):
    """
    DiagNode (Enum Class)

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
    DiagProcessor (Enum Class)

    Processor types

    .. data:: mpc8614d = 0

    	Processor type 8614D

    """

    mpc8614d = Enum.YLeaf(0, "mpc8614d")


class DiagSlot(Enum):
    """
    DiagSlot (Enum Class)

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



class Diag(Entity):
    """
    Diag admin operational data
    
    .. attribute:: racks
    
    	Diag operational data for available racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-diag-admin-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Diag, self).__init__()
        self._top_entity = None

        self.yang_name = "diag"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-diag-admin-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("racks", ("racks", Diag.Racks))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.racks = Diag.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-admin-oper:diag"


    class Racks(Entity):
        """
        Diag operational data for available racks
        
        .. attribute:: rack
        
        	Diag operational data for a particular rack
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-diag-admin-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Diag.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rack", ("rack", Diag.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-admin-oper:diag/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Racks, [], name, value)


        class Rack(Entity):
            """
            Diag operational data for a particular rack
            
            .. attribute:: rack_name  (key)
            
            	Rack name
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: fan_traies
            
            	Fan tray table operational data
            	**type**\:  :py:class:`FanTraies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies>`
            
            .. attribute:: power_supplies
            
            	Power supply table operational data
            	**type**\:  :py:class:`PowerSupplies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies>`
            
            .. attribute:: slots
            
            	Diag operational data for all available slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots>`
            
            .. attribute:: chassis
            
            	Chassis information
            	**type**\:  :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Chassis>`
            
            .. attribute:: summary
            
            	Summary information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Summary>`
            
            

            """

            _prefix = 'asr9k-sc-diag-admin-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Diag.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack_name']
                self._child_container_classes = OrderedDict([("fan-traies", ("fan_traies", Diag.Racks.Rack.FanTraies)), ("power-supplies", ("power_supplies", Diag.Racks.Rack.PowerSupplies)), ("slots", ("slots", Diag.Racks.Rack.Slots)), ("chassis", ("chassis", Diag.Racks.Rack.Chassis)), ("summary", ("summary", Diag.Racks.Rack.Summary))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rack_name', YLeaf(YType.int32, 'rack-name')),
                ])
                self.rack_name = None

                self.fan_traies = Diag.Racks.Rack.FanTraies()
                self.fan_traies.parent = self
                self._children_name_map["fan_traies"] = "fan-traies"
                self._children_yang_names.add("fan-traies")

                self.power_supplies = Diag.Racks.Rack.PowerSupplies()
                self.power_supplies.parent = self
                self._children_name_map["power_supplies"] = "power-supplies"
                self._children_yang_names.add("power-supplies")

                self.slots = Diag.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")

                self.chassis = Diag.Racks.Rack.Chassis()
                self.chassis.parent = self
                self._children_name_map["chassis"] = "chassis"
                self._children_yang_names.add("chassis")

                self.summary = Diag.Racks.Rack.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
                self._segment_path = lambda: "rack" + "[rack-name='" + str(self.rack_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-diag-admin-oper:diag/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Racks.Rack, ['rack_name'], name, value)


            class FanTraies(Entity):
                """
                Fan tray table operational data
                
                .. attribute:: fan_tray
                
                	Fan tray operational data
                	**type**\: list of  		 :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray>`
                
                

                """

                _prefix = 'asr9k-sc-diag-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.FanTraies, self).__init__()

                    self.yang_name = "fan-traies"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("fan-tray", ("fan_tray", Diag.Racks.Rack.FanTraies.FanTray))])
                    self._leafs = OrderedDict()

                    self.fan_tray = YList(self)
                    self._segment_path = lambda: "fan-traies"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.FanTraies, [], name, value)


                class FanTray(Entity):
                    """
                    Fan tray operational data
                    
                    .. attribute:: fan_tray_name  (key)
                    
                    	Fan tray name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: detail
                    
                    	Diag detailed information
                    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.FanTraies.FanTray, self).__init__()

                        self.yang_name = "fan-tray"
                        self.yang_parent_name = "fan-traies"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fan_tray_name']
                        self._child_container_classes = OrderedDict([("detail", ("detail", Diag.Racks.Rack.FanTraies.FanTray.Detail))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fan_tray_name', YLeaf(YType.str, 'fan-tray-name')),
                        ])
                        self.fan_tray_name = None

                        self.detail = Diag.Racks.Rack.FanTraies.FanTray.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")
                        self._segment_path = lambda: "fan-tray" + "[fan-tray-name='" + str(self.fan_tray_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray, ['fan_tray_name'], name, value)


                    class Detail(Entity):
                        """
                        Diag detailed information
                        
                        .. attribute:: node
                        
                        	Node information
                        	**type**\:  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node>`
                        
                        .. attribute:: spa
                        
                        	SPA information
                        	**type**\:  :py:class:`Spa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "fan-tray"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("node", ("node", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node)), ("spa", ("spa", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.node = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                            self._children_yang_names.add("node")

                            self.spa = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa()
                            self.spa.parent = self
                            self._children_name_map["spa"] = "spa"
                            self._children_yang_names.add("spa")
                            self._segment_path = lambda: "detail"


                        class Node(Entity):
                            """
                            Node information
                            
                            .. attribute:: pld
                            
                            	Programmable logic device information
                            	**type**\:  :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.Pld>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision>`
                            
                            .. attribute:: cbc_active_partition
                            
                            	CBC active partition
                            	**type**\:  :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcActivePartition>`
                            
                            .. attribute:: cbc_inactive_partition
                            
                            	CBC inactive partition
                            	**type**\:  :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcInactivePartition>`
                            
                            .. attribute:: description
                            
                            	Describes in user\-readable terms
                            	**type**\: str
                            
                            .. attribute:: serial_number
                            
                            	Main serial number
                            	**type**\: str
                            
                            .. attribute:: tan
                            
                            	Top assembly number
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: chip_hardware_revision
                            
                            	Chip hardware revision
                            	**type**\: str
                            
                            .. attribute:: new_deviation_number
                            
                            	New deviation number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: board_state
                            
                            	Module operational state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            .. attribute:: pld_motherboard
                            
                            	Motherboard PLD version
                            	**type**\: str
                            
                            .. attribute:: pld_power
                            
                            	Power PLD version
                            	**type**\: str
                            
                            .. attribute:: monlib
                            
                            	MONLIB version
                            	**type**\: str
                            
                            .. attribute:: rommon
                            
                            	ROMMON version
                            	**type**\: str
                            
                            .. attribute:: cpu0
                            
                            	Processor type
                            	**type**\:  :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagProcessor>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("pld", ("pld", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.Pld)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision)), ("cbc-active-partition", ("cbc_active_partition", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcActivePartition)), ("cbc-inactive-partition", ("cbc_inactive_partition", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcInactivePartition))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('description', YLeaf(YType.str, 'description')),
                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ('tan', YLeaf(YType.str, 'tan')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                    ('new_deviation_number', YLeaf(YType.uint32, 'new-deviation-number')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('board_state', YLeaf(YType.enumeration, 'board-state')),
                                    ('pld_motherboard', YLeaf(YType.str, 'pld-motherboard')),
                                    ('pld_power', YLeaf(YType.str, 'pld-power')),
                                    ('monlib', YLeaf(YType.str, 'monlib')),
                                    ('rommon', YLeaf(YType.str, 'rommon')),
                                    ('cpu0', YLeaf(YType.enumeration, 'cpu0')),
                                ])
                                self.description = None
                                self.serial_number = None
                                self.tan = None
                                self.pid = None
                                self.vid = None
                                self.chip_hardware_revision = None
                                self.new_deviation_number = None
                                self.clei = None
                                self.board_state = None
                                self.pld_motherboard = None
                                self.pld_power = None
                                self.monlib = None
                                self.rommon = None
                                self.cpu0 = None

                                self.pld = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.Pld()
                                self.pld.parent = self
                                self._children_name_map["pld"] = "pld"
                                self._children_yang_names.add("pld")

                                self.hardware_revision = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")

                                self.cbc_active_partition = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcActivePartition()
                                self.cbc_active_partition.parent = self
                                self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                self._children_yang_names.add("cbc-active-partition")

                                self.cbc_inactive_partition = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcInactivePartition()
                                self.cbc_inactive_partition.parent = self
                                self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                self._children_yang_names.add("cbc-inactive-partition")
                                self._segment_path = lambda: "node"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node, ['description', 'serial_number', 'tan', 'pid', 'vid', 'chip_hardware_revision', 'new_deviation_number', 'clei', 'board_state', 'pld_motherboard', 'pld_power', 'monlib', 'rommon', 'cpu0'], name, value)


                            class Pld(Entity):
                                """
                                Programmable logic device information
                                
                                .. attribute:: type
                                
                                	Processor PLD version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_higher_version
                                
                                	HigherVerion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_lower_version
                                
                                	LowerVersion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.Pld, self).__init__()

                                    self.yang_name = "pld"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.uint32, 'type')),
                                        ('processor_higher_version', YLeaf(YType.uint32, 'processor-higher-version')),
                                        ('processor_lower_version', YLeaf(YType.uint32, 'processor-lower-version')),
                                    ])
                                    self.type = None
                                    self.processor_higher_version = None
                                    self.processor_lower_version = None
                                    self._segment_path = lambda: "pld"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.Pld, ['type', 'processor_higher_version', 'processor_lower_version'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


                            class CbcActivePartition(Entity):
                                """
                                CBC active partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcActivePartition, self).__init__()

                                    self.yang_name = "cbc-active-partition"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-active-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                            class CbcInactivePartition(Entity):
                                """
                                CBC inactive partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcInactivePartition, self).__init__()

                                    self.yang_name = "cbc-inactive-partition"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-inactive-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Node.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                        class Spa(Entity):
                            """
                            SPA information
                            
                            .. attribute:: main
                            
                            	Main
                            	**type**\:  :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.Main>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision>`
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: name
                            
                            	SPA name
                            	**type**\: str
                            
                            .. attribute:: pca_unit_number
                            
                            	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                            	**type**\: str
                            
                            .. attribute:: pca_revision
                            
                            	PCA revision information
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: node_state
                            
                            	Node state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa, self).__init__()

                                self.yang_name = "spa"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("main", ("main", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.Main)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', YLeaf(YType.str, 'node')),
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('pca_unit_number', YLeaf(YType.str, 'pca-unit-number')),
                                    ('pca_revision', YLeaf(YType.str, 'pca-revision')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('node_state', YLeaf(YType.enumeration, 'node-state')),
                                ])
                                self.node = None
                                self.name = None
                                self.pca_unit_number = None
                                self.pca_revision = None
                                self.pid = None
                                self.vid = None
                                self.clei = None
                                self.node_state = None

                                self.main = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.Main()
                                self.main.parent = self
                                self._children_name_map["main"] = "main"
                                self._children_yang_names.add("main")

                                self.hardware_revision = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")
                                self._segment_path = lambda: "spa"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa, ['node', 'name', 'pca_unit_number', 'pca_revision', 'pid', 'vid', 'clei', 'node_state'], name, value)


                            class Main(Entity):
                                """
                                Main
                                
                                .. attribute:: board_type
                                
                                	Board type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: tan
                                
                                	Top assembly number
                                	**type**\: str
                                
                                .. attribute:: tan_revision
                                
                                	Top assembly number revision
                                	**type**\: str
                                
                                .. attribute:: deviation_number
                                
                                	Deviation number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: serial_number
                                
                                	Serial number
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.Main, self).__init__()

                                    self.yang_name = "main"
                                    self.yang_parent_name = "spa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('board_type', YLeaf(YType.uint32, 'board-type')),
                                        ('tan', YLeaf(YType.str, 'tan')),
                                        ('tan_revision', YLeaf(YType.str, 'tan-revision')),
                                        ('deviation_number', YLeaf(YType.uint32, 'deviation-number')),
                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ])
                                    self.board_type = None
                                    self.tan = None
                                    self.tan_revision = None
                                    self.deviation_number = None
                                    self.serial_number = None
                                    self._segment_path = lambda: "main"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.Main, ['board_type', 'tan', 'tan_revision', 'deviation_number', 'serial_number'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "spa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


            class PowerSupplies(Entity):
                """
                Power supply table operational data
                
                .. attribute:: power_supply
                
                	Power supply operational data
                	**type**\: list of  		 :py:class:`PowerSupply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply>`
                
                

                """

                _prefix = 'asr9k-sc-diag-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.PowerSupplies, self).__init__()

                    self.yang_name = "power-supplies"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("power-supply", ("power_supply", Diag.Racks.Rack.PowerSupplies.PowerSupply))])
                    self._leafs = OrderedDict()

                    self.power_supply = YList(self)
                    self._segment_path = lambda: "power-supplies"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies, [], name, value)


                class PowerSupply(Entity):
                    """
                    Power supply operational data
                    
                    .. attribute:: power_supply_name  (key)
                    
                    	Power supply name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: detail
                    
                    	Diag detailed information
                    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.PowerSupplies.PowerSupply, self).__init__()

                        self.yang_name = "power-supply"
                        self.yang_parent_name = "power-supplies"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['power_supply_name']
                        self._child_container_classes = OrderedDict([("detail", ("detail", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('power_supply_name', YLeaf(YType.str, 'power-supply-name')),
                        ])
                        self.power_supply_name = None

                        self.detail = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")
                        self._segment_path = lambda: "power-supply" + "[power-supply-name='" + str(self.power_supply_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply, ['power_supply_name'], name, value)


                    class Detail(Entity):
                        """
                        Diag detailed information
                        
                        .. attribute:: node
                        
                        	Node information
                        	**type**\:  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node>`
                        
                        .. attribute:: spa
                        
                        	SPA information
                        	**type**\:  :py:class:`Spa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "power-supply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("node", ("node", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node)), ("spa", ("spa", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.node = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                            self._children_yang_names.add("node")

                            self.spa = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa()
                            self.spa.parent = self
                            self._children_name_map["spa"] = "spa"
                            self._children_yang_names.add("spa")
                            self._segment_path = lambda: "detail"


                        class Node(Entity):
                            """
                            Node information
                            
                            .. attribute:: pld
                            
                            	Programmable logic device information
                            	**type**\:  :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.Pld>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision>`
                            
                            .. attribute:: cbc_active_partition
                            
                            	CBC active partition
                            	**type**\:  :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcActivePartition>`
                            
                            .. attribute:: cbc_inactive_partition
                            
                            	CBC inactive partition
                            	**type**\:  :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcInactivePartition>`
                            
                            .. attribute:: description
                            
                            	Describes in user\-readable terms
                            	**type**\: str
                            
                            .. attribute:: serial_number
                            
                            	Main serial number
                            	**type**\: str
                            
                            .. attribute:: tan
                            
                            	Top assembly number
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: chip_hardware_revision
                            
                            	Chip hardware revision
                            	**type**\: str
                            
                            .. attribute:: new_deviation_number
                            
                            	New deviation number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: board_state
                            
                            	Module operational state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            .. attribute:: pld_motherboard
                            
                            	Motherboard PLD version
                            	**type**\: str
                            
                            .. attribute:: pld_power
                            
                            	Power PLD version
                            	**type**\: str
                            
                            .. attribute:: monlib
                            
                            	MONLIB version
                            	**type**\: str
                            
                            .. attribute:: rommon
                            
                            	ROMMON version
                            	**type**\: str
                            
                            .. attribute:: cpu0
                            
                            	Processor type
                            	**type**\:  :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagProcessor>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("pld", ("pld", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.Pld)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision)), ("cbc-active-partition", ("cbc_active_partition", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcActivePartition)), ("cbc-inactive-partition", ("cbc_inactive_partition", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcInactivePartition))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('description', YLeaf(YType.str, 'description')),
                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ('tan', YLeaf(YType.str, 'tan')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                    ('new_deviation_number', YLeaf(YType.uint32, 'new-deviation-number')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('board_state', YLeaf(YType.enumeration, 'board-state')),
                                    ('pld_motherboard', YLeaf(YType.str, 'pld-motherboard')),
                                    ('pld_power', YLeaf(YType.str, 'pld-power')),
                                    ('monlib', YLeaf(YType.str, 'monlib')),
                                    ('rommon', YLeaf(YType.str, 'rommon')),
                                    ('cpu0', YLeaf(YType.enumeration, 'cpu0')),
                                ])
                                self.description = None
                                self.serial_number = None
                                self.tan = None
                                self.pid = None
                                self.vid = None
                                self.chip_hardware_revision = None
                                self.new_deviation_number = None
                                self.clei = None
                                self.board_state = None
                                self.pld_motherboard = None
                                self.pld_power = None
                                self.monlib = None
                                self.rommon = None
                                self.cpu0 = None

                                self.pld = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.Pld()
                                self.pld.parent = self
                                self._children_name_map["pld"] = "pld"
                                self._children_yang_names.add("pld")

                                self.hardware_revision = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")

                                self.cbc_active_partition = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcActivePartition()
                                self.cbc_active_partition.parent = self
                                self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                self._children_yang_names.add("cbc-active-partition")

                                self.cbc_inactive_partition = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcInactivePartition()
                                self.cbc_inactive_partition.parent = self
                                self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                self._children_yang_names.add("cbc-inactive-partition")
                                self._segment_path = lambda: "node"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node, ['description', 'serial_number', 'tan', 'pid', 'vid', 'chip_hardware_revision', 'new_deviation_number', 'clei', 'board_state', 'pld_motherboard', 'pld_power', 'monlib', 'rommon', 'cpu0'], name, value)


                            class Pld(Entity):
                                """
                                Programmable logic device information
                                
                                .. attribute:: type
                                
                                	Processor PLD version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_higher_version
                                
                                	HigherVerion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_lower_version
                                
                                	LowerVersion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.Pld, self).__init__()

                                    self.yang_name = "pld"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.uint32, 'type')),
                                        ('processor_higher_version', YLeaf(YType.uint32, 'processor-higher-version')),
                                        ('processor_lower_version', YLeaf(YType.uint32, 'processor-lower-version')),
                                    ])
                                    self.type = None
                                    self.processor_higher_version = None
                                    self.processor_lower_version = None
                                    self._segment_path = lambda: "pld"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.Pld, ['type', 'processor_higher_version', 'processor_lower_version'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


                            class CbcActivePartition(Entity):
                                """
                                CBC active partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcActivePartition, self).__init__()

                                    self.yang_name = "cbc-active-partition"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-active-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                            class CbcInactivePartition(Entity):
                                """
                                CBC inactive partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcInactivePartition, self).__init__()

                                    self.yang_name = "cbc-inactive-partition"
                                    self.yang_parent_name = "node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-inactive-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Node.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                        class Spa(Entity):
                            """
                            SPA information
                            
                            .. attribute:: main
                            
                            	Main
                            	**type**\:  :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.Main>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision>`
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: name
                            
                            	SPA name
                            	**type**\: str
                            
                            .. attribute:: pca_unit_number
                            
                            	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                            	**type**\: str
                            
                            .. attribute:: pca_revision
                            
                            	PCA revision information
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: node_state
                            
                            	Node state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa, self).__init__()

                                self.yang_name = "spa"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("main", ("main", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.Main)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', YLeaf(YType.str, 'node')),
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('pca_unit_number', YLeaf(YType.str, 'pca-unit-number')),
                                    ('pca_revision', YLeaf(YType.str, 'pca-revision')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('node_state', YLeaf(YType.enumeration, 'node-state')),
                                ])
                                self.node = None
                                self.name = None
                                self.pca_unit_number = None
                                self.pca_revision = None
                                self.pid = None
                                self.vid = None
                                self.clei = None
                                self.node_state = None

                                self.main = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.Main()
                                self.main.parent = self
                                self._children_name_map["main"] = "main"
                                self._children_yang_names.add("main")

                                self.hardware_revision = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")
                                self._segment_path = lambda: "spa"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa, ['node', 'name', 'pca_unit_number', 'pca_revision', 'pid', 'vid', 'clei', 'node_state'], name, value)


                            class Main(Entity):
                                """
                                Main
                                
                                .. attribute:: board_type
                                
                                	Board type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: tan
                                
                                	Top assembly number
                                	**type**\: str
                                
                                .. attribute:: tan_revision
                                
                                	Top assembly number revision
                                	**type**\: str
                                
                                .. attribute:: deviation_number
                                
                                	Deviation number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: serial_number
                                
                                	Serial number
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.Main, self).__init__()

                                    self.yang_name = "main"
                                    self.yang_parent_name = "spa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('board_type', YLeaf(YType.uint32, 'board-type')),
                                        ('tan', YLeaf(YType.str, 'tan')),
                                        ('tan_revision', YLeaf(YType.str, 'tan-revision')),
                                        ('deviation_number', YLeaf(YType.uint32, 'deviation-number')),
                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ])
                                    self.board_type = None
                                    self.tan = None
                                    self.tan_revision = None
                                    self.deviation_number = None
                                    self.serial_number = None
                                    self._segment_path = lambda: "main"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.Main, ['board_type', 'tan', 'tan_revision', 'deviation_number', 'serial_number'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "spa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.PowerSupplies.PowerSupply.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


            class Slots(Entity):
                """
                Diag operational data for all available slots
                
                .. attribute:: slot
                
                	Diag operational data for a particular slot
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-diag-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("slot", ("slot", Diag.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Diag operational data for a particular slot
                    
                    .. attribute:: slot_name  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: detail
                    
                    	Slot detailed information
                    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail>`
                    
                    .. attribute:: instances
                    
                    	Diag operational data for all available instances
                    	**type**\:  :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot_name']
                        self._child_container_classes = OrderedDict([("detail", ("detail", Diag.Racks.Rack.Slots.Slot.Detail)), ("instances", ("instances", Diag.Racks.Rack.Slots.Slot.Instances))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('slot_name', YLeaf(YType.str, 'slot-name')),
                        ])
                        self.slot_name = None

                        self.detail = Diag.Racks.Rack.Slots.Slot.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")

                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"
                        self._children_yang_names.add("instances")
                        self._segment_path = lambda: "slot" + "[slot-name='" + str(self.slot_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot, ['slot_name'], name, value)


                    class Detail(Entity):
                        """
                        Slot detailed information
                        
                        .. attribute:: node_detail
                        
                        	Detail information for slot
                        	**type**\: list of  		 :py:class:`NodeDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail>`
                        
                        .. attribute:: spa_detail
                        
                        	Detail information for spa
                        	**type**\: list of  		 :py:class:`SpaDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("node-detail", ("node_detail", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail)), ("spa-detail", ("spa_detail", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail))])
                            self._leafs = OrderedDict()

                            self.node_detail = YList(self)
                            self.spa_detail = YList(self)
                            self._segment_path = lambda: "detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail, [], name, value)


                        class NodeDetail(Entity):
                            """
                            Detail information for slot
                            
                            .. attribute:: pld
                            
                            	Programmable logic device information
                            	**type**\:  :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision>`
                            
                            .. attribute:: cbc_active_partition
                            
                            	CBC active partition
                            	**type**\:  :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition>`
                            
                            .. attribute:: cbc_inactive_partition
                            
                            	CBC inactive partition
                            	**type**\:  :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition>`
                            
                            .. attribute:: description
                            
                            	Describes in user\-readable terms
                            	**type**\: str
                            
                            .. attribute:: serial_number
                            
                            	Main serial number
                            	**type**\: str
                            
                            .. attribute:: tan
                            
                            	Top assembly number
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: chip_hardware_revision
                            
                            	Chip hardware revision
                            	**type**\: str
                            
                            .. attribute:: new_deviation_number
                            
                            	New deviation number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: board_state
                            
                            	Module operational state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            .. attribute:: pld_motherboard
                            
                            	Motherboard PLD version
                            	**type**\: str
                            
                            .. attribute:: pld_power
                            
                            	Power PLD version
                            	**type**\: str
                            
                            .. attribute:: monlib
                            
                            	MONLIB version
                            	**type**\: str
                            
                            .. attribute:: rommon
                            
                            	ROMMON version
                            	**type**\: str
                            
                            .. attribute:: cpu0
                            
                            	Processor type
                            	**type**\:  :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagProcessor>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail, self).__init__()

                                self.yang_name = "node-detail"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("pld", ("pld", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision)), ("cbc-active-partition", ("cbc_active_partition", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition)), ("cbc-inactive-partition", ("cbc_inactive_partition", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('description', YLeaf(YType.str, 'description')),
                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ('tan', YLeaf(YType.str, 'tan')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                    ('new_deviation_number', YLeaf(YType.uint32, 'new-deviation-number')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('board_state', YLeaf(YType.enumeration, 'board-state')),
                                    ('pld_motherboard', YLeaf(YType.str, 'pld-motherboard')),
                                    ('pld_power', YLeaf(YType.str, 'pld-power')),
                                    ('monlib', YLeaf(YType.str, 'monlib')),
                                    ('rommon', YLeaf(YType.str, 'rommon')),
                                    ('cpu0', YLeaf(YType.enumeration, 'cpu0')),
                                ])
                                self.description = None
                                self.serial_number = None
                                self.tan = None
                                self.pid = None
                                self.vid = None
                                self.chip_hardware_revision = None
                                self.new_deviation_number = None
                                self.clei = None
                                self.board_state = None
                                self.pld_motherboard = None
                                self.pld_power = None
                                self.monlib = None
                                self.rommon = None
                                self.cpu0 = None

                                self.pld = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld()
                                self.pld.parent = self
                                self._children_name_map["pld"] = "pld"
                                self._children_yang_names.add("pld")

                                self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")

                                self.cbc_active_partition = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition()
                                self.cbc_active_partition.parent = self
                                self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                self._children_yang_names.add("cbc-active-partition")

                                self.cbc_inactive_partition = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition()
                                self.cbc_inactive_partition.parent = self
                                self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                self._children_yang_names.add("cbc-inactive-partition")
                                self._segment_path = lambda: "node-detail"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail, ['description', 'serial_number', 'tan', 'pid', 'vid', 'chip_hardware_revision', 'new_deviation_number', 'clei', 'board_state', 'pld_motherboard', 'pld_power', 'monlib', 'rommon', 'cpu0'], name, value)


                            class Pld(Entity):
                                """
                                Programmable logic device information
                                
                                .. attribute:: type
                                
                                	Processor PLD version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_higher_version
                                
                                	HigherVerion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: processor_lower_version
                                
                                	LowerVersion
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld, self).__init__()

                                    self.yang_name = "pld"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.uint32, 'type')),
                                        ('processor_higher_version', YLeaf(YType.uint32, 'processor-higher-version')),
                                        ('processor_lower_version', YLeaf(YType.uint32, 'processor-lower-version')),
                                    ])
                                    self.type = None
                                    self.processor_higher_version = None
                                    self.processor_lower_version = None
                                    self._segment_path = lambda: "pld"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.Pld, ['type', 'processor_higher_version', 'processor_lower_version'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


                            class CbcActivePartition(Entity):
                                """
                                CBC active partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition, self).__init__()

                                    self.yang_name = "cbc-active-partition"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-active-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                            class CbcInactivePartition(Entity):
                                """
                                CBC inactive partition
                                
                                .. attribute:: major_revision
                                
                                	Major revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: minor_revision
                                
                                	Minor revision
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition, self).__init__()

                                    self.yang_name = "cbc-inactive-partition"
                                    self.yang_parent_name = "node-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                    ])
                                    self.major_revision = None
                                    self.minor_revision = None
                                    self._segment_path = lambda: "cbc-inactive-partition"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.NodeDetail.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                        class SpaDetail(Entity):
                            """
                            Detail information for spa
                            
                            .. attribute:: main
                            
                            	Main
                            	**type**\:  :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main>`
                            
                            .. attribute:: hardware_revision
                            
                            	Hardware revision
                            	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision>`
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: name
                            
                            	SPA name
                            	**type**\: str
                            
                            .. attribute:: pca_unit_number
                            
                            	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                            	**type**\: str
                            
                            .. attribute:: pca_revision
                            
                            	PCA revision information
                            	**type**\: str
                            
                            .. attribute:: pid
                            
                            	PID
                            	**type**\: str
                            
                            .. attribute:: vid
                            
                            	VID
                            	**type**\: str
                            
                            .. attribute:: clei
                            
                            	CLEI
                            	**type**\: str
                            
                            .. attribute:: node_state
                            
                            	Node state
                            	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail, self).__init__()

                                self.yang_name = "spa-detail"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("main", ("main", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', YLeaf(YType.str, 'node')),
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('pca_unit_number', YLeaf(YType.str, 'pca-unit-number')),
                                    ('pca_revision', YLeaf(YType.str, 'pca-revision')),
                                    ('pid', YLeaf(YType.str, 'pid')),
                                    ('vid', YLeaf(YType.str, 'vid')),
                                    ('clei', YLeaf(YType.str, 'clei')),
                                    ('node_state', YLeaf(YType.enumeration, 'node-state')),
                                ])
                                self.node = None
                                self.name = None
                                self.pca_unit_number = None
                                self.pca_revision = None
                                self.pid = None
                                self.vid = None
                                self.clei = None
                                self.node_state = None

                                self.main = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main()
                                self.main.parent = self
                                self._children_name_map["main"] = "main"
                                self._children_yang_names.add("main")

                                self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision()
                                self.hardware_revision.parent = self
                                self._children_name_map["hardware_revision"] = "hardware-revision"
                                self._children_yang_names.add("hardware-revision")
                                self._segment_path = lambda: "spa-detail"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail, ['node', 'name', 'pca_unit_number', 'pca_revision', 'pid', 'vid', 'clei', 'node_state'], name, value)


                            class Main(Entity):
                                """
                                Main
                                
                                .. attribute:: board_type
                                
                                	Board type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: tan
                                
                                	Top assembly number
                                	**type**\: str
                                
                                .. attribute:: tan_revision
                                
                                	Top assembly number revision
                                	**type**\: str
                                
                                .. attribute:: deviation_number
                                
                                	Deviation number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: serial_number
                                
                                	Serial number
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main, self).__init__()

                                    self.yang_name = "main"
                                    self.yang_parent_name = "spa-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('board_type', YLeaf(YType.uint32, 'board-type')),
                                        ('tan', YLeaf(YType.str, 'tan')),
                                        ('tan_revision', YLeaf(YType.str, 'tan-revision')),
                                        ('deviation_number', YLeaf(YType.uint32, 'deviation-number')),
                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ])
                                    self.board_type = None
                                    self.tan = None
                                    self.tan_revision = None
                                    self.deviation_number = None
                                    self.serial_number = None
                                    self._segment_path = lambda: "main"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.Main, ['board_type', 'tan', 'tan_revision', 'deviation_number', 'serial_number'], name, value)


                            class HardwareRevision(Entity):
                                """
                                Hardware revision
                                
                                .. attribute:: hardware_revision
                                
                                	Board FPGA/CPLD/ASIC hardware revision
                                	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision, self).__init__()

                                    self.yang_name = "hardware-revision"
                                    self.yang_parent_name = "spa-detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_))])
                                    self._leafs = OrderedDict()

                                    self.hardware_revision = YList(self)
                                    self._segment_path = lambda: "hardware-revision"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision, [], name, value)


                                class HardwareRevision_(Entity):
                                    """
                                    Board FPGA/CPLD/ASIC hardware revision
                                    
                                    .. attribute:: hw_rev
                                    
                                    	Hardware version
                                    	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.HwRev>`
                                    
                                    .. attribute:: fw_rev
                                    
                                    	Firmware version
                                    	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.FwRev>`
                                    
                                    .. attribute:: sw_rev
                                    
                                    	Software version
                                    	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SwRev>`
                                    
                                    .. attribute:: dimm_rev
                                    
                                    	DIMM version information
                                    	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.DimmRev>`
                                    
                                    .. attribute:: ssd_rev
                                    
                                    	SSD version information
                                    	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SsdRev>`
                                    
                                    .. attribute:: node_description
                                    
                                    	Node decsription
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Version information
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_, self).__init__()

                                        self.yang_name = "hardware-revision"
                                        self.yang_parent_name = "hardware-revision"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SsdRev))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_description', YLeaf(YType.str, 'node-description')),
                                            ('version', YLeaf(YType.str, 'version')),
                                        ])
                                        self.node_description = None
                                        self.version = None

                                        self.hw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.HwRev()
                                        self.hw_rev.parent = self
                                        self._children_name_map["hw_rev"] = "hw-rev"
                                        self._children_yang_names.add("hw-rev")

                                        self.fw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.FwRev()
                                        self.fw_rev.parent = self
                                        self._children_name_map["fw_rev"] = "fw-rev"
                                        self._children_yang_names.add("fw-rev")

                                        self.sw_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SwRev()
                                        self.sw_rev.parent = self
                                        self._children_name_map["sw_rev"] = "sw-rev"
                                        self._children_yang_names.add("sw-rev")

                                        self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.DimmRev()
                                        self.dimm_rev.parent = self
                                        self._children_name_map["dimm_rev"] = "dimm-rev"
                                        self._children_yang_names.add("dimm-rev")

                                        self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SsdRev()
                                        self.ssd_rev.parent = self
                                        self._children_name_map["ssd_rev"] = "ssd-rev"
                                        self._children_yang_names.add("ssd-rev")
                                        self._segment_path = lambda: "hardware-revision"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                    class HwRev(Entity):
                                        """
                                        Hardware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                            self.yang_name = "hw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "hw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                    class FwRev(Entity):
                                        """
                                        Firmware version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                            self.yang_name = "fw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "fw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                    class SwRev(Entity):
                                        """
                                        Software version
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                            self.yang_name = "sw-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "sw-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                    class DimmRev(Entity):
                                        """
                                        DIMM version information
                                        
                                        .. attribute:: size
                                        
                                        	Size in MB
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: speed
                                        
                                        	Speed in MHz
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: locator
                                        
                                        	Locator information
                                        	**type**\: str
                                        
                                        .. attribute:: cas
                                        
                                        	Column address strobe latency in clock cycles
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                            self.yang_name = "dimm-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('size', YLeaf(YType.uint32, 'size')),
                                                ('speed', YLeaf(YType.uint32, 'speed')),
                                                ('locator', YLeaf(YType.str, 'locator')),
                                                ('cas', YLeaf(YType.uint32, 'cas')),
                                            ])
                                            self.size = None
                                            self.speed = None
                                            self.locator = None
                                            self.cas = None
                                            self._segment_path = lambda: "dimm-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                    class SsdRev(Entity):
                                        """
                                        SSD version information
                                        
                                        .. attribute:: number
                                        
                                        	SSD number
                                        	**type**\: str
                                        
                                        .. attribute:: fw_rev
                                        
                                        	Firmware revision
                                        	**type**\: str
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                            self.yang_name = "ssd-rev"
                                            self.yang_parent_name = "hardware-revision"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('number', YLeaf(YType.str, 'number')),
                                                ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.number = None
                                            self.fw_rev = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "ssd-rev"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Detail.SpaDetail.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


                    class Instances(Entity):
                        """
                        Diag operational data for all available
                        instances
                        
                        .. attribute:: instance
                        
                        	Diag operational data for a particular instance
                        	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-diag-admin-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Instances, self).__init__()

                            self.yang_name = "instances"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("instance", ("instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance))])
                            self._leafs = OrderedDict()

                            self.instance = YList(self)
                            self._segment_path = lambda: "instances"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances, [], name, value)


                        class Instance(Entity):
                            """
                            Diag operational data for a particular
                            instance
                            
                            .. attribute:: instance_name  (key)
                            
                            	Instance name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: detail
                            
                            	Diag detailed information
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-diag-admin-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__init__()

                                self.yang_name = "instance"
                                self.yang_parent_name = "instances"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['instance_name']
                                self._child_container_classes = OrderedDict([("detail", ("detail", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instance_name', YLeaf(YType.str, 'instance-name')),
                                ])
                                self.instance_name = None

                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")
                                self._segment_path = lambda: "instance" + "[instance-name='" + str(self.instance_name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance, ['instance_name'], name, value)


                            class Detail(Entity):
                                """
                                Diag detailed information
                                
                                .. attribute:: node
                                
                                	Node information
                                	**type**\:  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node>`
                                
                                .. attribute:: spa
                                
                                	SPA information
                                	**type**\:  :py:class:`Spa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-diag-admin-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "instance"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("node", ("node", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node)), ("spa", ("spa", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

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
                                    
                                    .. attribute:: pld
                                    
                                    	Programmable logic device information
                                    	**type**\:  :py:class:`Pld <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld>`
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	Hardware revision
                                    	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision>`
                                    
                                    .. attribute:: cbc_active_partition
                                    
                                    	CBC active partition
                                    	**type**\:  :py:class:`CbcActivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition>`
                                    
                                    .. attribute:: cbc_inactive_partition
                                    
                                    	CBC inactive partition
                                    	**type**\:  :py:class:`CbcInactivePartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition>`
                                    
                                    .. attribute:: description
                                    
                                    	Describes in user\-readable terms
                                    	**type**\: str
                                    
                                    .. attribute:: serial_number
                                    
                                    	Main serial number
                                    	**type**\: str
                                    
                                    .. attribute:: tan
                                    
                                    	Top assembly number
                                    	**type**\: str
                                    
                                    .. attribute:: pid
                                    
                                    	PID
                                    	**type**\: str
                                    
                                    .. attribute:: vid
                                    
                                    	VID
                                    	**type**\: str
                                    
                                    .. attribute:: chip_hardware_revision
                                    
                                    	Chip hardware revision
                                    	**type**\: str
                                    
                                    .. attribute:: new_deviation_number
                                    
                                    	New deviation number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: clei
                                    
                                    	CLEI
                                    	**type**\: str
                                    
                                    .. attribute:: board_state
                                    
                                    	Module operational state
                                    	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                                    
                                    .. attribute:: pld_motherboard
                                    
                                    	Motherboard PLD version
                                    	**type**\: str
                                    
                                    .. attribute:: pld_power
                                    
                                    	Power PLD version
                                    	**type**\: str
                                    
                                    .. attribute:: monlib
                                    
                                    	MONLIB version
                                    	**type**\: str
                                    
                                    .. attribute:: rommon
                                    
                                    	ROMMON version
                                    	**type**\: str
                                    
                                    .. attribute:: cpu0
                                    
                                    	Processor type
                                    	**type**\:  :py:class:`DiagProcessor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagProcessor>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node, self).__init__()

                                        self.yang_name = "node"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("pld", ("pld", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision)), ("cbc-active-partition", ("cbc_active_partition", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition)), ("cbc-inactive-partition", ("cbc_inactive_partition", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('description', YLeaf(YType.str, 'description')),
                                            ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ('tan', YLeaf(YType.str, 'tan')),
                                            ('pid', YLeaf(YType.str, 'pid')),
                                            ('vid', YLeaf(YType.str, 'vid')),
                                            ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                            ('new_deviation_number', YLeaf(YType.uint32, 'new-deviation-number')),
                                            ('clei', YLeaf(YType.str, 'clei')),
                                            ('board_state', YLeaf(YType.enumeration, 'board-state')),
                                            ('pld_motherboard', YLeaf(YType.str, 'pld-motherboard')),
                                            ('pld_power', YLeaf(YType.str, 'pld-power')),
                                            ('monlib', YLeaf(YType.str, 'monlib')),
                                            ('rommon', YLeaf(YType.str, 'rommon')),
                                            ('cpu0', YLeaf(YType.enumeration, 'cpu0')),
                                        ])
                                        self.description = None
                                        self.serial_number = None
                                        self.tan = None
                                        self.pid = None
                                        self.vid = None
                                        self.chip_hardware_revision = None
                                        self.new_deviation_number = None
                                        self.clei = None
                                        self.board_state = None
                                        self.pld_motherboard = None
                                        self.pld_power = None
                                        self.monlib = None
                                        self.rommon = None
                                        self.cpu0 = None

                                        self.pld = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld()
                                        self.pld.parent = self
                                        self._children_name_map["pld"] = "pld"
                                        self._children_yang_names.add("pld")

                                        self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision()
                                        self.hardware_revision.parent = self
                                        self._children_name_map["hardware_revision"] = "hardware-revision"
                                        self._children_yang_names.add("hardware-revision")

                                        self.cbc_active_partition = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition()
                                        self.cbc_active_partition.parent = self
                                        self._children_name_map["cbc_active_partition"] = "cbc-active-partition"
                                        self._children_yang_names.add("cbc-active-partition")

                                        self.cbc_inactive_partition = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition()
                                        self.cbc_inactive_partition.parent = self
                                        self._children_name_map["cbc_inactive_partition"] = "cbc-inactive-partition"
                                        self._children_yang_names.add("cbc-inactive-partition")
                                        self._segment_path = lambda: "node"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node, ['description', 'serial_number', 'tan', 'pid', 'vid', 'chip_hardware_revision', 'new_deviation_number', 'clei', 'board_state', 'pld_motherboard', 'pld_power', 'monlib', 'rommon', 'cpu0'], name, value)


                                    class Pld(Entity):
                                        """
                                        Programmable logic device information
                                        
                                        .. attribute:: type
                                        
                                        	Processor PLD version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: processor_higher_version
                                        
                                        	HigherVerion
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: processor_lower_version
                                        
                                        	LowerVersion
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld, self).__init__()

                                            self.yang_name = "pld"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', YLeaf(YType.uint32, 'type')),
                                                ('processor_higher_version', YLeaf(YType.uint32, 'processor-higher-version')),
                                                ('processor_lower_version', YLeaf(YType.uint32, 'processor-lower-version')),
                                            ])
                                            self.type = None
                                            self.processor_higher_version = None
                                            self.processor_lower_version = None
                                            self._segment_path = lambda: "pld"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.Pld, ['type', 'processor_higher_version', 'processor_lower_version'], name, value)


                                    class HardwareRevision(Entity):
                                        """
                                        Hardware revision
                                        
                                        .. attribute:: hardware_revision
                                        
                                        	Board FPGA/CPLD/ASIC hardware revision
                                        	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision, self).__init__()

                                            self.yang_name = "hardware-revision"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_))])
                                            self._leafs = OrderedDict()

                                            self.hardware_revision = YList(self)
                                            self._segment_path = lambda: "hardware-revision"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision, [], name, value)


                                        class HardwareRevision_(Entity):
                                            """
                                            Board FPGA/CPLD/ASIC hardware revision
                                            
                                            .. attribute:: hw_rev
                                            
                                            	Hardware version
                                            	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.HwRev>`
                                            
                                            .. attribute:: fw_rev
                                            
                                            	Firmware version
                                            	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.FwRev>`
                                            
                                            .. attribute:: sw_rev
                                            
                                            	Software version
                                            	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SwRev>`
                                            
                                            .. attribute:: dimm_rev
                                            
                                            	DIMM version information
                                            	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev>`
                                            
                                            .. attribute:: ssd_rev
                                            
                                            	SSD version information
                                            	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev>`
                                            
                                            .. attribute:: node_description
                                            
                                            	Node decsription
                                            	**type**\: str
                                            
                                            .. attribute:: version
                                            
                                            	Version information
                                            	**type**\: str
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-diag-admin-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_, self).__init__()

                                                self.yang_name = "hardware-revision"
                                                self.yang_parent_name = "hardware-revision"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('node_description', YLeaf(YType.str, 'node-description')),
                                                    ('version', YLeaf(YType.str, 'version')),
                                                ])
                                                self.node_description = None
                                                self.version = None

                                                self.hw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.HwRev()
                                                self.hw_rev.parent = self
                                                self._children_name_map["hw_rev"] = "hw-rev"
                                                self._children_yang_names.add("hw-rev")

                                                self.fw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.FwRev()
                                                self.fw_rev.parent = self
                                                self._children_name_map["fw_rev"] = "fw-rev"
                                                self._children_yang_names.add("fw-rev")

                                                self.sw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SwRev()
                                                self.sw_rev.parent = self
                                                self._children_name_map["sw_rev"] = "sw-rev"
                                                self._children_yang_names.add("sw-rev")

                                                self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev()
                                                self.dimm_rev.parent = self
                                                self._children_name_map["dimm_rev"] = "dimm-rev"
                                                self._children_yang_names.add("dimm-rev")

                                                self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev()
                                                self.ssd_rev.parent = self
                                                self._children_name_map["ssd_rev"] = "ssd-rev"
                                                self._children_yang_names.add("ssd-rev")
                                                self._segment_path = lambda: "hardware-revision"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                            class HwRev(Entity):
                                                """
                                                Hardware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                                    self.yang_name = "hw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "hw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                            class FwRev(Entity):
                                                """
                                                Firmware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                                    self.yang_name = "fw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "fw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                            class SwRev(Entity):
                                                """
                                                Software version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                                    self.yang_name = "sw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "sw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                            class DimmRev(Entity):
                                                """
                                                DIMM version information
                                                
                                                .. attribute:: size
                                                
                                                	Size in MB
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: speed
                                                
                                                	Speed in MHz
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: locator
                                                
                                                	Locator information
                                                	**type**\: str
                                                
                                                .. attribute:: cas
                                                
                                                	Column address strobe latency in clock cycles
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                                    self.yang_name = "dimm-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('size', YLeaf(YType.uint32, 'size')),
                                                        ('speed', YLeaf(YType.uint32, 'speed')),
                                                        ('locator', YLeaf(YType.str, 'locator')),
                                                        ('cas', YLeaf(YType.uint32, 'cas')),
                                                    ])
                                                    self.size = None
                                                    self.speed = None
                                                    self.locator = None
                                                    self.cas = None
                                                    self._segment_path = lambda: "dimm-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                            class SsdRev(Entity):
                                                """
                                                SSD version information
                                                
                                                .. attribute:: number
                                                
                                                	SSD number
                                                	**type**\: str
                                                
                                                .. attribute:: fw_rev
                                                
                                                	Firmware revision
                                                	**type**\: str
                                                
                                                .. attribute:: serial_number
                                                
                                                	Serial number
                                                	**type**\: str
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                                    self.yang_name = "ssd-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('number', YLeaf(YType.str, 'number')),
                                                        ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ])
                                                    self.number = None
                                                    self.fw_rev = None
                                                    self.serial_number = None
                                                    self._segment_path = lambda: "ssd-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


                                    class CbcActivePartition(Entity):
                                        """
                                        CBC active partition
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition, self).__init__()

                                            self.yang_name = "cbc-active-partition"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "cbc-active-partition"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcActivePartition, ['major_revision', 'minor_revision'], name, value)


                                    class CbcInactivePartition(Entity):
                                        """
                                        CBC inactive partition
                                        
                                        .. attribute:: major_revision
                                        
                                        	Major revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: minor_revision
                                        
                                        	Minor revision
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition, self).__init__()

                                            self.yang_name = "cbc-inactive-partition"
                                            self.yang_parent_name = "node"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                            ])
                                            self.major_revision = None
                                            self.minor_revision = None
                                            self._segment_path = lambda: "cbc-inactive-partition"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Node.CbcInactivePartition, ['major_revision', 'minor_revision'], name, value)


                                class Spa(Entity):
                                    """
                                    SPA information
                                    
                                    .. attribute:: main
                                    
                                    	Main
                                    	**type**\:  :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main>`
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	Hardware revision
                                    	**type**\:  :py:class:`HardwareRevision <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision>`
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    .. attribute:: name
                                    
                                    	SPA name
                                    	**type**\: str
                                    
                                    .. attribute:: pca_unit_number
                                    
                                    	Format is C\-BN\-V where C = Class Code, BN = Base Number, and V = Version
                                    	**type**\: str
                                    
                                    .. attribute:: pca_revision
                                    
                                    	PCA revision information
                                    	**type**\: str
                                    
                                    .. attribute:: pid
                                    
                                    	PID
                                    	**type**\: str
                                    
                                    .. attribute:: vid
                                    
                                    	VID
                                    	**type**\: str
                                    
                                    .. attribute:: clei
                                    
                                    	CLEI
                                    	**type**\: str
                                    
                                    .. attribute:: node_state
                                    
                                    	Node state
                                    	**type**\:  :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.NodeState>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-diag-admin-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa, self).__init__()

                                        self.yang_name = "spa"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("main", ("main", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main)), ("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node', YLeaf(YType.str, 'node')),
                                            ('name', YLeaf(YType.str, 'name')),
                                            ('pca_unit_number', YLeaf(YType.str, 'pca-unit-number')),
                                            ('pca_revision', YLeaf(YType.str, 'pca-revision')),
                                            ('pid', YLeaf(YType.str, 'pid')),
                                            ('vid', YLeaf(YType.str, 'vid')),
                                            ('clei', YLeaf(YType.str, 'clei')),
                                            ('node_state', YLeaf(YType.enumeration, 'node-state')),
                                        ])
                                        self.node = None
                                        self.name = None
                                        self.pca_unit_number = None
                                        self.pca_revision = None
                                        self.pid = None
                                        self.vid = None
                                        self.clei = None
                                        self.node_state = None

                                        self.main = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main()
                                        self.main.parent = self
                                        self._children_name_map["main"] = "main"
                                        self._children_yang_names.add("main")

                                        self.hardware_revision = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision()
                                        self.hardware_revision.parent = self
                                        self._children_name_map["hardware_revision"] = "hardware-revision"
                                        self._children_yang_names.add("hardware-revision")
                                        self._segment_path = lambda: "spa"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa, ['node', 'name', 'pca_unit_number', 'pca_revision', 'pid', 'vid', 'clei', 'node_state'], name, value)


                                    class Main(Entity):
                                        """
                                        Main
                                        
                                        .. attribute:: board_type
                                        
                                        	Board type
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tan
                                        
                                        	Top assembly number
                                        	**type**\: str
                                        
                                        .. attribute:: tan_revision
                                        
                                        	Top assembly number revision
                                        	**type**\: str
                                        
                                        .. attribute:: deviation_number
                                        
                                        	Deviation number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: serial_number
                                        
                                        	Serial number
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main, self).__init__()

                                            self.yang_name = "main"
                                            self.yang_parent_name = "spa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('board_type', YLeaf(YType.uint32, 'board-type')),
                                                ('tan', YLeaf(YType.str, 'tan')),
                                                ('tan_revision', YLeaf(YType.str, 'tan-revision')),
                                                ('deviation_number', YLeaf(YType.uint32, 'deviation-number')),
                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ])
                                            self.board_type = None
                                            self.tan = None
                                            self.tan_revision = None
                                            self.deviation_number = None
                                            self.serial_number = None
                                            self._segment_path = lambda: "main"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.Main, ['board_type', 'tan', 'tan_revision', 'deviation_number', 'serial_number'], name, value)


                                    class HardwareRevision(Entity):
                                        """
                                        Hardware revision
                                        
                                        .. attribute:: hardware_revision
                                        
                                        	Board FPGA/CPLD/ASIC hardware revision
                                        	**type**\: list of  		 :py:class:`HardwareRevision_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-diag-admin-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision, self).__init__()

                                            self.yang_name = "hardware-revision"
                                            self.yang_parent_name = "spa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("hardware-revision", ("hardware_revision", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_))])
                                            self._leafs = OrderedDict()

                                            self.hardware_revision = YList(self)
                                            self._segment_path = lambda: "hardware-revision"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision, [], name, value)


                                        class HardwareRevision_(Entity):
                                            """
                                            Board FPGA/CPLD/ASIC hardware revision
                                            
                                            .. attribute:: hw_rev
                                            
                                            	Hardware version
                                            	**type**\:  :py:class:`HwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev>`
                                            
                                            .. attribute:: fw_rev
                                            
                                            	Firmware version
                                            	**type**\:  :py:class:`FwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev>`
                                            
                                            .. attribute:: sw_rev
                                            
                                            	Software version
                                            	**type**\:  :py:class:`SwRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev>`
                                            
                                            .. attribute:: dimm_rev
                                            
                                            	DIMM version information
                                            	**type**\:  :py:class:`DimmRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev>`
                                            
                                            .. attribute:: ssd_rev
                                            
                                            	SSD version information
                                            	**type**\:  :py:class:`SsdRev <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev>`
                                            
                                            .. attribute:: node_description
                                            
                                            	Node decsription
                                            	**type**\: str
                                            
                                            .. attribute:: version
                                            
                                            	Version information
                                            	**type**\: str
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-diag-admin-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_, self).__init__()

                                                self.yang_name = "hardware-revision"
                                                self.yang_parent_name = "hardware-revision"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("hw-rev", ("hw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev)), ("fw-rev", ("fw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev)), ("sw-rev", ("sw_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev)), ("dimm-rev", ("dimm_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev)), ("ssd-rev", ("ssd_rev", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('node_description', YLeaf(YType.str, 'node-description')),
                                                    ('version', YLeaf(YType.str, 'version')),
                                                ])
                                                self.node_description = None
                                                self.version = None

                                                self.hw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev()
                                                self.hw_rev.parent = self
                                                self._children_name_map["hw_rev"] = "hw-rev"
                                                self._children_yang_names.add("hw-rev")

                                                self.fw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev()
                                                self.fw_rev.parent = self
                                                self._children_name_map["fw_rev"] = "fw-rev"
                                                self._children_yang_names.add("fw-rev")

                                                self.sw_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev()
                                                self.sw_rev.parent = self
                                                self._children_name_map["sw_rev"] = "sw-rev"
                                                self._children_yang_names.add("sw-rev")

                                                self.dimm_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev()
                                                self.dimm_rev.parent = self
                                                self._children_name_map["dimm_rev"] = "dimm-rev"
                                                self._children_yang_names.add("dimm-rev")

                                                self.ssd_rev = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev()
                                                self.ssd_rev.parent = self
                                                self._children_name_map["ssd_rev"] = "ssd-rev"
                                                self._children_yang_names.add("ssd-rev")
                                                self._segment_path = lambda: "hardware-revision"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_, ['node_description', 'version'], name, value)


                                            class HwRev(Entity):
                                                """
                                                Hardware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, self).__init__()

                                                    self.yang_name = "hw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "hw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.HwRev, ['major_revision', 'minor_revision'], name, value)


                                            class FwRev(Entity):
                                                """
                                                Firmware version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, self).__init__()

                                                    self.yang_name = "fw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "fw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.FwRev, ['major_revision', 'minor_revision'], name, value)


                                            class SwRev(Entity):
                                                """
                                                Software version
                                                
                                                .. attribute:: major_revision
                                                
                                                	Major revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: minor_revision
                                                
                                                	Minor revision
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, self).__init__()

                                                    self.yang_name = "sw-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('major_revision', YLeaf(YType.uint32, 'major-revision')),
                                                        ('minor_revision', YLeaf(YType.uint32, 'minor-revision')),
                                                    ])
                                                    self.major_revision = None
                                                    self.minor_revision = None
                                                    self._segment_path = lambda: "sw-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SwRev, ['major_revision', 'minor_revision'], name, value)


                                            class DimmRev(Entity):
                                                """
                                                DIMM version information
                                                
                                                .. attribute:: size
                                                
                                                	Size in MB
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: speed
                                                
                                                	Speed in MHz
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: locator
                                                
                                                	Locator information
                                                	**type**\: str
                                                
                                                .. attribute:: cas
                                                
                                                	Column address strobe latency in clock cycles
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, self).__init__()

                                                    self.yang_name = "dimm-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('size', YLeaf(YType.uint32, 'size')),
                                                        ('speed', YLeaf(YType.uint32, 'speed')),
                                                        ('locator', YLeaf(YType.str, 'locator')),
                                                        ('cas', YLeaf(YType.uint32, 'cas')),
                                                    ])
                                                    self.size = None
                                                    self.speed = None
                                                    self.locator = None
                                                    self.cas = None
                                                    self._segment_path = lambda: "dimm-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.DimmRev, ['size', 'speed', 'locator', 'cas'], name, value)


                                            class SsdRev(Entity):
                                                """
                                                SSD version information
                                                
                                                .. attribute:: number
                                                
                                                	SSD number
                                                	**type**\: str
                                                
                                                .. attribute:: fw_rev
                                                
                                                	Firmware revision
                                                	**type**\: str
                                                
                                                .. attribute:: serial_number
                                                
                                                	Serial number
                                                	**type**\: str
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-diag-admin-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, self).__init__()

                                                    self.yang_name = "ssd-rev"
                                                    self.yang_parent_name = "hardware-revision"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('number', YLeaf(YType.str, 'number')),
                                                        ('fw_rev', YLeaf(YType.str, 'fw-rev')),
                                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ])
                                                    self.number = None
                                                    self.fw_rev = None
                                                    self.serial_number = None
                                                    self._segment_path = lambda: "ssd-rev"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.Spa.HardwareRevision.HardwareRevision_.SsdRev, ['number', 'fw_rev', 'serial_number'], name, value)


            class Chassis(Entity):
                """
                Chassis information
                
                .. attribute:: serial_number
                
                	Serial number
                	**type**\: str
                
                .. attribute:: pid
                
                	PID
                	**type**\: str
                
                .. attribute:: vid
                
                	VID
                	**type**\: str
                
                .. attribute:: description
                
                	Describes in user\-readable terms
                	**type**\: str
                
                .. attribute:: clei
                
                	CLEI
                	**type**\: str
                
                .. attribute:: tan
                
                	Top assembly number
                	**type**\: str
                
                

                """

                _prefix = 'asr9k-sc-diag-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Chassis, self).__init__()

                    self.yang_name = "chassis"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                        ('pid', YLeaf(YType.str, 'pid')),
                        ('vid', YLeaf(YType.str, 'vid')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('clei', YLeaf(YType.str, 'clei')),
                        ('tan', YLeaf(YType.str, 'tan')),
                    ])
                    self.serial_number = None
                    self.pid = None
                    self.vid = None
                    self.description = None
                    self.clei = None
                    self.tan = None
                    self._segment_path = lambda: "chassis"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Chassis, ['serial_number', 'pid', 'vid', 'description', 'clei', 'tan'], name, value)


            class Summary(Entity):
                """
                Summary information
                
                .. attribute:: summary
                
                	Summary data
                	**type**\: list of  		 :py:class:`Summary_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.Diag.Racks.Rack.Summary.Summary_>`
                
                

                """

                _prefix = 'asr9k-sc-diag-admin-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("summary", ("summary", Diag.Racks.Rack.Summary.Summary_))])
                    self._leafs = OrderedDict()

                    self.summary = YList(self)
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Summary, [], name, value)


                class Summary_(Entity):
                    """
                    Summary data
                    
                    .. attribute:: type
                    
                    	Node type
                    	**type**\:  :py:class:`DiagNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagNode>`
                    
                    .. attribute:: node
                    
                    	Node ID
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: slot_type
                    
                    	Slot type
                    	**type**\:  :py:class:`DiagSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_diag_admin_oper.DiagSlot>`
                    
                    .. attribute:: description
                    
                    	Description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'asr9k-sc-diag-admin-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Summary.Summary_, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('node', YLeaf(YType.str, 'node')),
                            ('slot_type', YLeaf(YType.enumeration, 'slot-type')),
                            ('description', YLeaf(YType.str, 'description')),
                        ])
                        self.type = None
                        self.node = None
                        self.slot_type = None
                        self.description = None
                        self._segment_path = lambda: "summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Summary.Summary_, ['type', 'node', 'slot_type', 'description'], name, value)

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

