""" Cisco_IOS_XR_wanphy_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package operational data.

This module contains definitions
for the following management objects\:
  wanphy\: WANPHY operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.controllers = Wanphy.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")


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

            self.controller = YList(self)

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
                        super(Wanphy.Controllers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Wanphy.Controllers, self).__setattr__(name, value)


        class Controller(Entity):
            """
            WANPHY controller operational data
            
            .. attribute:: controller_name  <key>
            
            	Controller name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.info = Wanphy.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("controller_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Wanphy.Controllers.Controller, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Wanphy.Controllers.Controller, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("admin_mode",
                                    "line_ais",
                                    "line_bip",
                                    "line_febe",
                                    "line_rdi",
                                    "operational_mode",
                                    "path_ais",
                                    "path_bip",
                                    "path_febe",
                                    "path_lop",
                                    "path_newptr",
                                    "path_nse",
                                    "path_pse",
                                    "path_rdi",
                                    "port_state",
                                    "register_j1_rx0",
                                    "register_j1_rx1",
                                    "register_j1_rx2",
                                    "register_j1_rx3",
                                    "register_j1_rx4",
                                    "register_j1_rx5",
                                    "register_j1_rx6",
                                    "register_j1_rx7",
                                    "register_l_bip",
                                    "register_l_fe_bip",
                                    "register_p_bec",
                                    "register_p_febe",
                                    "register_s_bip",
                                    "remote_ip",
                                    "sd_ber_report",
                                    "sd_ber_threshold",
                                    "section_bip",
                                    "section_lof",
                                    "section_los",
                                    "sf_ber_report",
                                    "sf_ber_threshold",
                                    "wanphy_poll_timer",
                                    "wis_alarms_feaisp",
                                    "wis_alarms_felcdp",
                                    "wis_alarms_lfebip",
                                    "wis_alarms_pbec",
                                    "wis_alarms_plcd",
                                    "wis_alarms_plmp",
                                    "wis_alarms_ser",
                                    "wis_alarms_wlos") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Wanphy.Controllers.Controller.Info, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Wanphy.Controllers.Controller.Info, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.admin_mode.is_set or
                        self.line_ais.is_set or
                        self.line_bip.is_set or
                        self.line_febe.is_set or
                        self.line_rdi.is_set or
                        self.operational_mode.is_set or
                        self.path_ais.is_set or
                        self.path_bip.is_set or
                        self.path_febe.is_set or
                        self.path_lop.is_set or
                        self.path_newptr.is_set or
                        self.path_nse.is_set or
                        self.path_pse.is_set or
                        self.path_rdi.is_set or
                        self.port_state.is_set or
                        self.register_j1_rx0.is_set or
                        self.register_j1_rx1.is_set or
                        self.register_j1_rx2.is_set or
                        self.register_j1_rx3.is_set or
                        self.register_j1_rx4.is_set or
                        self.register_j1_rx5.is_set or
                        self.register_j1_rx6.is_set or
                        self.register_j1_rx7.is_set or
                        self.register_l_bip.is_set or
                        self.register_l_fe_bip.is_set or
                        self.register_p_bec.is_set or
                        self.register_p_febe.is_set or
                        self.register_s_bip.is_set or
                        self.remote_ip.is_set or
                        self.sd_ber_report.is_set or
                        self.sd_ber_threshold.is_set or
                        self.section_bip.is_set or
                        self.section_lof.is_set or
                        self.section_los.is_set or
                        self.sf_ber_report.is_set or
                        self.sf_ber_threshold.is_set or
                        self.wanphy_poll_timer.is_set or
                        self.wis_alarms_feaisp.is_set or
                        self.wis_alarms_felcdp.is_set or
                        self.wis_alarms_lfebip.is_set or
                        self.wis_alarms_pbec.is_set or
                        self.wis_alarms_plcd.is_set or
                        self.wis_alarms_plmp.is_set or
                        self.wis_alarms_ser.is_set or
                        self.wis_alarms_wlos.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.admin_mode.yfilter != YFilter.not_set or
                        self.line_ais.yfilter != YFilter.not_set or
                        self.line_bip.yfilter != YFilter.not_set or
                        self.line_febe.yfilter != YFilter.not_set or
                        self.line_rdi.yfilter != YFilter.not_set or
                        self.operational_mode.yfilter != YFilter.not_set or
                        self.path_ais.yfilter != YFilter.not_set or
                        self.path_bip.yfilter != YFilter.not_set or
                        self.path_febe.yfilter != YFilter.not_set or
                        self.path_lop.yfilter != YFilter.not_set or
                        self.path_newptr.yfilter != YFilter.not_set or
                        self.path_nse.yfilter != YFilter.not_set or
                        self.path_pse.yfilter != YFilter.not_set or
                        self.path_rdi.yfilter != YFilter.not_set or
                        self.port_state.yfilter != YFilter.not_set or
                        self.register_j1_rx0.yfilter != YFilter.not_set or
                        self.register_j1_rx1.yfilter != YFilter.not_set or
                        self.register_j1_rx2.yfilter != YFilter.not_set or
                        self.register_j1_rx3.yfilter != YFilter.not_set or
                        self.register_j1_rx4.yfilter != YFilter.not_set or
                        self.register_j1_rx5.yfilter != YFilter.not_set or
                        self.register_j1_rx6.yfilter != YFilter.not_set or
                        self.register_j1_rx7.yfilter != YFilter.not_set or
                        self.register_l_bip.yfilter != YFilter.not_set or
                        self.register_l_fe_bip.yfilter != YFilter.not_set or
                        self.register_p_bec.yfilter != YFilter.not_set or
                        self.register_p_febe.yfilter != YFilter.not_set or
                        self.register_s_bip.yfilter != YFilter.not_set or
                        self.remote_ip.yfilter != YFilter.not_set or
                        self.sd_ber_report.yfilter != YFilter.not_set or
                        self.sd_ber_threshold.yfilter != YFilter.not_set or
                        self.section_bip.yfilter != YFilter.not_set or
                        self.section_lof.yfilter != YFilter.not_set or
                        self.section_los.yfilter != YFilter.not_set or
                        self.sf_ber_report.yfilter != YFilter.not_set or
                        self.sf_ber_threshold.yfilter != YFilter.not_set or
                        self.wanphy_poll_timer.yfilter != YFilter.not_set or
                        self.wis_alarms_feaisp.yfilter != YFilter.not_set or
                        self.wis_alarms_felcdp.yfilter != YFilter.not_set or
                        self.wis_alarms_lfebip.yfilter != YFilter.not_set or
                        self.wis_alarms_pbec.yfilter != YFilter.not_set or
                        self.wis_alarms_plcd.yfilter != YFilter.not_set or
                        self.wis_alarms_plmp.yfilter != YFilter.not_set or
                        self.wis_alarms_ser.yfilter != YFilter.not_set or
                        self.wis_alarms_wlos.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.admin_mode.is_set or self.admin_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.admin_mode.get_name_leafdata())
                    if (self.line_ais.is_set or self.line_ais.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_ais.get_name_leafdata())
                    if (self.line_bip.is_set or self.line_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_bip.get_name_leafdata())
                    if (self.line_febe.is_set or self.line_febe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_febe.get_name_leafdata())
                    if (self.line_rdi.is_set or self.line_rdi.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_rdi.get_name_leafdata())
                    if (self.operational_mode.is_set or self.operational_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_mode.get_name_leafdata())
                    if (self.path_ais.is_set or self.path_ais.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_ais.get_name_leafdata())
                    if (self.path_bip.is_set or self.path_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_bip.get_name_leafdata())
                    if (self.path_febe.is_set or self.path_febe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_febe.get_name_leafdata())
                    if (self.path_lop.is_set or self.path_lop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_lop.get_name_leafdata())
                    if (self.path_newptr.is_set or self.path_newptr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_newptr.get_name_leafdata())
                    if (self.path_nse.is_set or self.path_nse.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_nse.get_name_leafdata())
                    if (self.path_pse.is_set or self.path_pse.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_pse.get_name_leafdata())
                    if (self.path_rdi.is_set or self.path_rdi.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_rdi.get_name_leafdata())
                    if (self.port_state.is_set or self.port_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_state.get_name_leafdata())
                    if (self.register_j1_rx0.is_set or self.register_j1_rx0.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx0.get_name_leafdata())
                    if (self.register_j1_rx1.is_set or self.register_j1_rx1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx1.get_name_leafdata())
                    if (self.register_j1_rx2.is_set or self.register_j1_rx2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx2.get_name_leafdata())
                    if (self.register_j1_rx3.is_set or self.register_j1_rx3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx3.get_name_leafdata())
                    if (self.register_j1_rx4.is_set or self.register_j1_rx4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx4.get_name_leafdata())
                    if (self.register_j1_rx5.is_set or self.register_j1_rx5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx5.get_name_leafdata())
                    if (self.register_j1_rx6.is_set or self.register_j1_rx6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx6.get_name_leafdata())
                    if (self.register_j1_rx7.is_set or self.register_j1_rx7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_j1_rx7.get_name_leafdata())
                    if (self.register_l_bip.is_set or self.register_l_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_l_bip.get_name_leafdata())
                    if (self.register_l_fe_bip.is_set or self.register_l_fe_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_l_fe_bip.get_name_leafdata())
                    if (self.register_p_bec.is_set or self.register_p_bec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_p_bec.get_name_leafdata())
                    if (self.register_p_febe.is_set or self.register_p_febe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_p_febe.get_name_leafdata())
                    if (self.register_s_bip.is_set or self.register_s_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.register_s_bip.get_name_leafdata())
                    if (self.remote_ip.is_set or self.remote_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_ip.get_name_leafdata())
                    if (self.sd_ber_report.is_set or self.sd_ber_report.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sd_ber_report.get_name_leafdata())
                    if (self.sd_ber_threshold.is_set or self.sd_ber_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sd_ber_threshold.get_name_leafdata())
                    if (self.section_bip.is_set or self.section_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.section_bip.get_name_leafdata())
                    if (self.section_lof.is_set or self.section_lof.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.section_lof.get_name_leafdata())
                    if (self.section_los.is_set or self.section_los.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.section_los.get_name_leafdata())
                    if (self.sf_ber_report.is_set or self.sf_ber_report.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sf_ber_report.get_name_leafdata())
                    if (self.sf_ber_threshold.is_set or self.sf_ber_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sf_ber_threshold.get_name_leafdata())
                    if (self.wanphy_poll_timer.is_set or self.wanphy_poll_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wanphy_poll_timer.get_name_leafdata())
                    if (self.wis_alarms_feaisp.is_set or self.wis_alarms_feaisp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_feaisp.get_name_leafdata())
                    if (self.wis_alarms_felcdp.is_set or self.wis_alarms_felcdp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_felcdp.get_name_leafdata())
                    if (self.wis_alarms_lfebip.is_set or self.wis_alarms_lfebip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_lfebip.get_name_leafdata())
                    if (self.wis_alarms_pbec.is_set or self.wis_alarms_pbec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_pbec.get_name_leafdata())
                    if (self.wis_alarms_plcd.is_set or self.wis_alarms_plcd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_plcd.get_name_leafdata())
                    if (self.wis_alarms_plmp.is_set or self.wis_alarms_plmp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_plmp.get_name_leafdata())
                    if (self.wis_alarms_ser.is_set or self.wis_alarms_ser.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_ser.get_name_leafdata())
                    if (self.wis_alarms_wlos.is_set or self.wis_alarms_wlos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wis_alarms_wlos.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "admin-mode" or name == "line-ais" or name == "line-bip" or name == "line-febe" or name == "line-rdi" or name == "operational-mode" or name == "path-ais" or name == "path-bip" or name == "path-febe" or name == "path-lop" or name == "path-newptr" or name == "path-nse" or name == "path-pse" or name == "path-rdi" or name == "port-state" or name == "register-j1-rx0" or name == "register-j1-rx1" or name == "register-j1-rx2" or name == "register-j1-rx3" or name == "register-j1-rx4" or name == "register-j1-rx5" or name == "register-j1-rx6" or name == "register-j1-rx7" or name == "register-l-bip" or name == "register-l-fe-bip" or name == "register-p-bec" or name == "register-p-febe" or name == "register-s-bip" or name == "remote-ip" or name == "sd-ber-report" or name == "sd-ber-threshold" or name == "section-bip" or name == "section-lof" or name == "section-los" or name == "sf-ber-report" or name == "sf-ber-threshold" or name == "wanphy-poll-timer" or name == "wis-alarms-feaisp" or name == "wis-alarms-felcdp" or name == "wis-alarms-lfebip" or name == "wis-alarms-pbec" or name == "wis-alarms-plcd" or name == "wis-alarms-plmp" or name == "wis-alarms-ser" or name == "wis-alarms-wlos"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "admin-mode"):
                        self.admin_mode = value
                        self.admin_mode.value_namespace = name_space
                        self.admin_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-ais"):
                        self.line_ais = value
                        self.line_ais.value_namespace = name_space
                        self.line_ais.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-bip"):
                        self.line_bip = value
                        self.line_bip.value_namespace = name_space
                        self.line_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-febe"):
                        self.line_febe = value
                        self.line_febe.value_namespace = name_space
                        self.line_febe.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-rdi"):
                        self.line_rdi = value
                        self.line_rdi.value_namespace = name_space
                        self.line_rdi.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-mode"):
                        self.operational_mode = value
                        self.operational_mode.value_namespace = name_space
                        self.operational_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-ais"):
                        self.path_ais = value
                        self.path_ais.value_namespace = name_space
                        self.path_ais.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-bip"):
                        self.path_bip = value
                        self.path_bip.value_namespace = name_space
                        self.path_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-febe"):
                        self.path_febe = value
                        self.path_febe.value_namespace = name_space
                        self.path_febe.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-lop"):
                        self.path_lop = value
                        self.path_lop.value_namespace = name_space
                        self.path_lop.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-newptr"):
                        self.path_newptr = value
                        self.path_newptr.value_namespace = name_space
                        self.path_newptr.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-nse"):
                        self.path_nse = value
                        self.path_nse.value_namespace = name_space
                        self.path_nse.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-pse"):
                        self.path_pse = value
                        self.path_pse.value_namespace = name_space
                        self.path_pse.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-rdi"):
                        self.path_rdi = value
                        self.path_rdi.value_namespace = name_space
                        self.path_rdi.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-state"):
                        self.port_state = value
                        self.port_state.value_namespace = name_space
                        self.port_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx0"):
                        self.register_j1_rx0 = value
                        self.register_j1_rx0.value_namespace = name_space
                        self.register_j1_rx0.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx1"):
                        self.register_j1_rx1 = value
                        self.register_j1_rx1.value_namespace = name_space
                        self.register_j1_rx1.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx2"):
                        self.register_j1_rx2 = value
                        self.register_j1_rx2.value_namespace = name_space
                        self.register_j1_rx2.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx3"):
                        self.register_j1_rx3 = value
                        self.register_j1_rx3.value_namespace = name_space
                        self.register_j1_rx3.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx4"):
                        self.register_j1_rx4 = value
                        self.register_j1_rx4.value_namespace = name_space
                        self.register_j1_rx4.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx5"):
                        self.register_j1_rx5 = value
                        self.register_j1_rx5.value_namespace = name_space
                        self.register_j1_rx5.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx6"):
                        self.register_j1_rx6 = value
                        self.register_j1_rx6.value_namespace = name_space
                        self.register_j1_rx6.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-j1-rx7"):
                        self.register_j1_rx7 = value
                        self.register_j1_rx7.value_namespace = name_space
                        self.register_j1_rx7.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-l-bip"):
                        self.register_l_bip = value
                        self.register_l_bip.value_namespace = name_space
                        self.register_l_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-l-fe-bip"):
                        self.register_l_fe_bip = value
                        self.register_l_fe_bip.value_namespace = name_space
                        self.register_l_fe_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-p-bec"):
                        self.register_p_bec = value
                        self.register_p_bec.value_namespace = name_space
                        self.register_p_bec.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-p-febe"):
                        self.register_p_febe = value
                        self.register_p_febe.value_namespace = name_space
                        self.register_p_febe.value_namespace_prefix = name_space_prefix
                    if(value_path == "register-s-bip"):
                        self.register_s_bip = value
                        self.register_s_bip.value_namespace = name_space
                        self.register_s_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-ip"):
                        self.remote_ip = value
                        self.remote_ip.value_namespace = name_space
                        self.remote_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "sd-ber-report"):
                        self.sd_ber_report = value
                        self.sd_ber_report.value_namespace = name_space
                        self.sd_ber_report.value_namespace_prefix = name_space_prefix
                    if(value_path == "sd-ber-threshold"):
                        self.sd_ber_threshold = value
                        self.sd_ber_threshold.value_namespace = name_space
                        self.sd_ber_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "section-bip"):
                        self.section_bip = value
                        self.section_bip.value_namespace = name_space
                        self.section_bip.value_namespace_prefix = name_space_prefix
                    if(value_path == "section-lof"):
                        self.section_lof = value
                        self.section_lof.value_namespace = name_space
                        self.section_lof.value_namespace_prefix = name_space_prefix
                    if(value_path == "section-los"):
                        self.section_los = value
                        self.section_los.value_namespace = name_space
                        self.section_los.value_namespace_prefix = name_space_prefix
                    if(value_path == "sf-ber-report"):
                        self.sf_ber_report = value
                        self.sf_ber_report.value_namespace = name_space
                        self.sf_ber_report.value_namespace_prefix = name_space_prefix
                    if(value_path == "sf-ber-threshold"):
                        self.sf_ber_threshold = value
                        self.sf_ber_threshold.value_namespace = name_space
                        self.sf_ber_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "wanphy-poll-timer"):
                        self.wanphy_poll_timer = value
                        self.wanphy_poll_timer.value_namespace = name_space
                        self.wanphy_poll_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-feaisp"):
                        self.wis_alarms_feaisp = value
                        self.wis_alarms_feaisp.value_namespace = name_space
                        self.wis_alarms_feaisp.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-felcdp"):
                        self.wis_alarms_felcdp = value
                        self.wis_alarms_felcdp.value_namespace = name_space
                        self.wis_alarms_felcdp.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-lfebip"):
                        self.wis_alarms_lfebip = value
                        self.wis_alarms_lfebip.value_namespace = name_space
                        self.wis_alarms_lfebip.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-pbec"):
                        self.wis_alarms_pbec = value
                        self.wis_alarms_pbec.value_namespace = name_space
                        self.wis_alarms_pbec.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-plcd"):
                        self.wis_alarms_plcd = value
                        self.wis_alarms_plcd.value_namespace = name_space
                        self.wis_alarms_plcd.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-plmp"):
                        self.wis_alarms_plmp = value
                        self.wis_alarms_plmp.value_namespace = name_space
                        self.wis_alarms_plmp.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-ser"):
                        self.wis_alarms_ser = value
                        self.wis_alarms_ser.value_namespace = name_space
                        self.wis_alarms_ser.value_namespace_prefix = name_space_prefix
                    if(value_path == "wis-alarms-wlos"):
                        self.wis_alarms_wlos = value
                        self.wis_alarms_wlos.value_namespace = name_space
                        self.wis_alarms_wlos.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.controller_name.is_set or
                    (self.info is not None and self.info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.controller_name.yfilter != YFilter.not_set or
                    (self.info is not None and self.info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "controller" + "[controller-name='" + self.controller_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-wanphy-ui-oper:wanphy/controllers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.controller_name.is_set or self.controller_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.controller_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "info"):
                    if (self.info is None):
                        self.info = Wanphy.Controllers.Controller.Info()
                        self.info.parent = self
                        self._children_name_map["info"] = "info"
                    return self.info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "info" or name == "controller-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "controller-name"):
                    self.controller_name = value
                    self.controller_name.value_namespace = name_space
                    self.controller_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.controller:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.controller:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "controllers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-wanphy-ui-oper:wanphy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "controller"):
                for c in self.controller:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Wanphy.Controllers.Controller()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.controller.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "controller"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.controllers is not None and self.controllers.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.controllers is not None and self.controllers.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-wanphy-ui-oper:wanphy" + path_buffer

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

        if (child_yang_name == "controllers"):
            if (self.controllers is None):
                self.controllers = Wanphy.Controllers()
                self.controllers.parent = self
                self._children_name_map["controllers"] = "controllers"
            return self.controllers

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "controllers"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Wanphy()
        return self._top_entity

