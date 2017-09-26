""" Cisco_IOS_XR_wanphy_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package operational data.

This module contains definitions
for the following management objects\:
  wanphy\: WANPHY operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class WanphyAlarmRepStatus(Enum):
    """
    WanphyAlarmRepStatus

    WANPHY Alarm Report Status

    .. data:: disable = 0

    	Alarm reporting is disable

    .. data:: enable = 1

    	Alarm reporting is enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class WanphyModeInfo(Enum):
    """
    WanphyModeInfo

    WANPHY Modes

    .. data:: lan = 0

    	LAN mode

    .. data:: wan = 1

    	WAN mode

    """

    lan = Enum.YLeaf(0, "lan")

    wan = Enum.YLeaf(1, "wan")



class Wanphy(Entity):
    """
    WANPHY operational data
    
    .. attribute:: controllers
    
    	All WANPHY controller operational data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers>`
    
    

    """

    _prefix = 'wanphy-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Wanphy, self).__init__()
        self._top_entity = None

        self.yang_name = "wanphy"
        self.yang_parent_name = "Cisco-IOS-XR-wanphy-ui-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"controllers" : ("controllers", Wanphy.Controllers)}
        self._child_list_classes = {}

        self.controllers = Wanphy.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")
        self._segment_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy"


    class Controllers(Entity):
        """
        All WANPHY controller operational data
        
        .. attribute:: controller
        
        	WANPHY controller operational data
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers.Controller>`
        
        

        """

        _prefix = 'wanphy-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Wanphy.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "wanphy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"controller" : ("controller", Wanphy.Controllers.Controller)}

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Wanphy.Controllers, [], name, value)


        class Controller(Entity):
            """
            WANPHY controller operational data
            
            .. attribute:: controller_name  <key>
            
            	Controller name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: info
            
            	WANPHY controller operational data
            	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers.Controller.Info>`
            
            

            """

            _prefix = 'wanphy-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Wanphy.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"info" : ("info", Wanphy.Controllers.Controller.Info)}
                self._child_list_classes = {}

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.info = Wanphy.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")
                self._segment_path = lambda: "controller" + "[controller-name='" + self.controller_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy/controllers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Wanphy.Controllers.Controller, ['controller_name'], name, value)


            class Info(Entity):
                """
                WANPHY controller operational data
                
                .. attribute:: admin_mode
                
                	Configuration Mode
                	**type**\:   :py:class:`WanphyModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfo>`
                
                .. attribute:: line_ais
                
                	Line AIS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_bip
                
                	Line BIP(B2) 
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_febe
                
                	Line FEBE
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_rdi
                
                	Line RDI
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_mode
                
                	Operational Mode
                	**type**\:   :py:class:`WanphyModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfo>`
                
                .. attribute:: path_ais
                
                	Path AIS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_bip
                
                	Path BIP(B3)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_febe
                
                	Path FEBE
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_lop
                
                	Path LOP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_newptr
                
                	Path NEWPTR
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_nse
                
                	Path NSE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_pse
                
                	Path PSE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_rdi
                
                	Path RDI
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state
                
                	Port State
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx0
                
                	Register J1\-Rx0
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx1
                
                	Register J1\-Rx1
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx2
                
                	Register J1\-Rx2
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx3
                
                	Register J1\-Rx3
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx4
                
                	Register J1\-Rx4
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx5
                
                	Register J1\-Rx5
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx6
                
                	Register J1\-Rx6
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx7
                
                	Register J1\-Rx7
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_l_bip
                
                	Register L\_BIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_l_fe_bip
                
                	Register L\_FE\_BIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_p_bec
                
                	Register P\_BEC
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_p_febe
                
                	Register P\_FEBE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_s_bip
                
                	Register S\_BIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ip
                
                	Remote IP Address
                	**type**\:  str
                
                .. attribute:: sd_ber_report
                
                	SD\_BER Report
                	**type**\:   :py:class:`WanphyAlarmRepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatus>`
                
                .. attribute:: sd_ber_threshold
                
                	BER thresholds\: SD. Value 'd' in 10e\-%d
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: section_bip
                
                	Section BIP(B1)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: section_lof
                
                	Section LOF
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: section_los
                
                	Section LOS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sf_ber_report
                
                	SF\_BER Report
                	**type**\:   :py:class:`WanphyAlarmRepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatus>`
                
                .. attribute:: sf_ber_threshold
                
                	BER thresholds\: SF. Value 'd' in 10e\-%d
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wanphy_poll_timer
                
                	wanphy poll timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_feaisp
                
                	WIS Alarms FEAISP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_felcdp
                
                	WIS Alarms FELCDP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_lfebip
                
                	WIS Alarms LFEBIP
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wis_alarms_pbec
                
                	WIS Alarms PBEC
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wis_alarms_plcd
                
                	WIS Alarms PLCD
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_plmp
                
                	WIS Alarms PLMP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_ser
                
                	WIS Alarms SER
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_wlos
                
                	WIS Alarms WLOS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'wanphy-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Wanphy.Controllers.Controller.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_mode = YLeaf(YType.enumeration, "admin-mode")

                    self.line_ais = YLeaf(YType.uint32, "line-ais")

                    self.line_bip = YLeaf(YType.uint64, "line-bip")

                    self.line_febe = YLeaf(YType.uint64, "line-febe")

                    self.line_rdi = YLeaf(YType.uint32, "line-rdi")

                    self.operational_mode = YLeaf(YType.enumeration, "operational-mode")

                    self.path_ais = YLeaf(YType.uint32, "path-ais")

                    self.path_bip = YLeaf(YType.uint64, "path-bip")

                    self.path_febe = YLeaf(YType.uint64, "path-febe")

                    self.path_lop = YLeaf(YType.uint32, "path-lop")

                    self.path_newptr = YLeaf(YType.uint32, "path-newptr")

                    self.path_nse = YLeaf(YType.uint32, "path-nse")

                    self.path_pse = YLeaf(YType.uint32, "path-pse")

                    self.path_rdi = YLeaf(YType.uint32, "path-rdi")

                    self.port_state = YLeaf(YType.uint32, "port-state")

                    self.register_j1_rx0 = YLeaf(YType.uint32, "register-j1-rx0")

                    self.register_j1_rx1 = YLeaf(YType.uint32, "register-j1-rx1")

                    self.register_j1_rx2 = YLeaf(YType.uint32, "register-j1-rx2")

                    self.register_j1_rx3 = YLeaf(YType.uint32, "register-j1-rx3")

                    self.register_j1_rx4 = YLeaf(YType.uint32, "register-j1-rx4")

                    self.register_j1_rx5 = YLeaf(YType.uint32, "register-j1-rx5")

                    self.register_j1_rx6 = YLeaf(YType.uint32, "register-j1-rx6")

                    self.register_j1_rx7 = YLeaf(YType.uint32, "register-j1-rx7")

                    self.register_l_bip = YLeaf(YType.uint32, "register-l-bip")

                    self.register_l_fe_bip = YLeaf(YType.uint32, "register-l-fe-bip")

                    self.register_p_bec = YLeaf(YType.uint32, "register-p-bec")

                    self.register_p_febe = YLeaf(YType.uint32, "register-p-febe")

                    self.register_s_bip = YLeaf(YType.uint32, "register-s-bip")

                    self.remote_ip = YLeaf(YType.str, "remote-ip")

                    self.sd_ber_report = YLeaf(YType.enumeration, "sd-ber-report")

                    self.sd_ber_threshold = YLeaf(YType.uint32, "sd-ber-threshold")

                    self.section_bip = YLeaf(YType.uint64, "section-bip")

                    self.section_lof = YLeaf(YType.uint32, "section-lof")

                    self.section_los = YLeaf(YType.uint32, "section-los")

                    self.sf_ber_report = YLeaf(YType.enumeration, "sf-ber-report")

                    self.sf_ber_threshold = YLeaf(YType.uint32, "sf-ber-threshold")

                    self.wanphy_poll_timer = YLeaf(YType.uint32, "wanphy-poll-timer")

                    self.wis_alarms_feaisp = YLeaf(YType.uint32, "wis-alarms-feaisp")

                    self.wis_alarms_felcdp = YLeaf(YType.uint32, "wis-alarms-felcdp")

                    self.wis_alarms_lfebip = YLeaf(YType.uint64, "wis-alarms-lfebip")

                    self.wis_alarms_pbec = YLeaf(YType.uint64, "wis-alarms-pbec")

                    self.wis_alarms_plcd = YLeaf(YType.uint32, "wis-alarms-plcd")

                    self.wis_alarms_plmp = YLeaf(YType.uint32, "wis-alarms-plmp")

                    self.wis_alarms_ser = YLeaf(YType.uint32, "wis-alarms-ser")

                    self.wis_alarms_wlos = YLeaf(YType.uint32, "wis-alarms-wlos")
                    self._segment_path = lambda: "info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Wanphy.Controllers.Controller.Info, ['admin_mode', 'line_ais', 'line_bip', 'line_febe', 'line_rdi', 'operational_mode', 'path_ais', 'path_bip', 'path_febe', 'path_lop', 'path_newptr', 'path_nse', 'path_pse', 'path_rdi', 'port_state', 'register_j1_rx0', 'register_j1_rx1', 'register_j1_rx2', 'register_j1_rx3', 'register_j1_rx4', 'register_j1_rx5', 'register_j1_rx6', 'register_j1_rx7', 'register_l_bip', 'register_l_fe_bip', 'register_p_bec', 'register_p_febe', 'register_s_bip', 'remote_ip', 'sd_ber_report', 'sd_ber_threshold', 'section_bip', 'section_lof', 'section_los', 'sf_ber_report', 'sf_ber_threshold', 'wanphy_poll_timer', 'wis_alarms_feaisp', 'wis_alarms_felcdp', 'wis_alarms_lfebip', 'wis_alarms_pbec', 'wis_alarms_plcd', 'wis_alarms_plmp', 'wis_alarms_ser', 'wis_alarms_wlos'], name, value)

    def clone_ptr(self):
        self._top_entity = Wanphy()
        return self._top_entity

