""" Cisco_IOS_XR_wanphy_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package operational data.

This module contains definitions
for the following management objects\:
  wanphy\: WANPHY operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class WanphyAlarmRepStatus(Enum):
    """
    WanphyAlarmRepStatus (Enum Class)

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
    WanphyModeInfo (Enum Class)

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
    	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controllers", ("controllers", Wanphy.Controllers))])
        self._leafs = OrderedDict()

        self.controllers = Wanphy.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._segment_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Wanphy, [], name, value)


    class Controllers(Entity):
        """
        All WANPHY controller operational data
        
        .. attribute:: controller
        
        	WANPHY controller operational data
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers.Controller>`
        
        

        """

        _prefix = 'wanphy-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Wanphy.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "wanphy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("controller", ("controller", Wanphy.Controllers.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Wanphy.Controllers, [], name, value)


        class Controller(Entity):
            """
            WANPHY controller operational data
            
            .. attribute:: controller_name  (key)
            
            	Controller name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: info
            
            	WANPHY controller operational data
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers.Controller.Info>`
            
            

            """

            _prefix = 'wanphy-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Wanphy.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_classes = OrderedDict([("info", ("info", Wanphy.Controllers.Controller.Info))])
                self._leafs = OrderedDict([
                    ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                ])
                self.controller_name = None

                self.info = Wanphy.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-wanphy-ui-oper:wanphy/controllers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Wanphy.Controllers.Controller, ['controller_name'], name, value)


            class Info(Entity):
                """
                WANPHY controller operational data
                
                .. attribute:: admin_mode
                
                	Configuration Mode
                	**type**\:  :py:class:`WanphyModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfo>`
                
                .. attribute:: port_state
                
                	Port State
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: section_lof
                
                	Section LOF
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: section_los
                
                	Section LOS
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: section_bip
                
                	Section BIP(B1)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_ais
                
                	Line AIS
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_rdi
                
                	Line RDI
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_febe
                
                	Line FEBE
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_bip
                
                	Line BIP(B2) 
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_ais
                
                	Path AIS
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_rdi
                
                	Path RDI
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_febe
                
                	Path FEBE
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_bip
                
                	Path BIP(B3)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_lop
                
                	Path LOP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_newptr
                
                	Path NEWPTR
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_pse
                
                	Path PSE
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_nse
                
                	Path NSE
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_ser
                
                	WIS Alarms SER
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_felcdp
                
                	WIS Alarms FELCDP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_feaisp
                
                	WIS Alarms FEAISP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_wlos
                
                	WIS Alarms WLOS
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_plcd
                
                	WIS Alarms PLCD
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wis_alarms_lfebip
                
                	WIS Alarms LFEBIP
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wis_alarms_pbec
                
                	WIS Alarms PBEC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wis_alarms_plmp
                
                	WIS Alarms PLMP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sf_ber_threshold
                
                	BER thresholds\: SF. Value 'd' in 10e\-%d
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_ber_threshold
                
                	BER thresholds\: SD. Value 'd' in 10e\-%d
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sf_ber_report
                
                	SF\_BER Report
                	**type**\:  :py:class:`WanphyAlarmRepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatus>`
                
                .. attribute:: sd_ber_report
                
                	SD\_BER Report
                	**type**\:  :py:class:`WanphyAlarmRepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatus>`
                
                .. attribute:: operational_mode
                
                	Operational Mode
                	**type**\:  :py:class:`WanphyModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfo>`
                
                .. attribute:: remote_ip
                
                	Remote IP Address
                	**type**\: str
                
                .. attribute:: register_p_febe
                
                	Register P\_FEBE
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_l_fe_bip
                
                	Register L\_FE\_BIP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_l_bip
                
                	Register L\_BIP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_p_bec
                
                	Register P\_BEC
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_s_bip
                
                	Register S\_BIP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx0
                
                	Register J1\-Rx0
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx1
                
                	Register J1\-Rx1
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx2
                
                	Register J1\-Rx2
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx3
                
                	Register J1\-Rx3
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx4
                
                	Register J1\-Rx4
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx5
                
                	Register J1\-Rx5
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx6
                
                	Register J1\-Rx6
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: register_j1_rx7
                
                	Register J1\-Rx7
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wanphy_poll_timer
                
                	wanphy poll timer
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('admin_mode', (YLeaf(YType.enumeration, 'admin-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyModeInfo', '')])),
                        ('port_state', (YLeaf(YType.uint32, 'port-state'), ['int'])),
                        ('section_lof', (YLeaf(YType.uint32, 'section-lof'), ['int'])),
                        ('section_los', (YLeaf(YType.uint32, 'section-los'), ['int'])),
                        ('section_bip', (YLeaf(YType.uint64, 'section-bip'), ['int'])),
                        ('line_ais', (YLeaf(YType.uint32, 'line-ais'), ['int'])),
                        ('line_rdi', (YLeaf(YType.uint32, 'line-rdi'), ['int'])),
                        ('line_febe', (YLeaf(YType.uint64, 'line-febe'), ['int'])),
                        ('line_bip', (YLeaf(YType.uint64, 'line-bip'), ['int'])),
                        ('path_ais', (YLeaf(YType.uint32, 'path-ais'), ['int'])),
                        ('path_rdi', (YLeaf(YType.uint32, 'path-rdi'), ['int'])),
                        ('path_febe', (YLeaf(YType.uint64, 'path-febe'), ['int'])),
                        ('path_bip', (YLeaf(YType.uint64, 'path-bip'), ['int'])),
                        ('path_lop', (YLeaf(YType.uint32, 'path-lop'), ['int'])),
                        ('path_newptr', (YLeaf(YType.uint32, 'path-newptr'), ['int'])),
                        ('path_pse', (YLeaf(YType.uint32, 'path-pse'), ['int'])),
                        ('path_nse', (YLeaf(YType.uint32, 'path-nse'), ['int'])),
                        ('wis_alarms_ser', (YLeaf(YType.uint32, 'wis-alarms-ser'), ['int'])),
                        ('wis_alarms_felcdp', (YLeaf(YType.uint32, 'wis-alarms-felcdp'), ['int'])),
                        ('wis_alarms_feaisp', (YLeaf(YType.uint32, 'wis-alarms-feaisp'), ['int'])),
                        ('wis_alarms_wlos', (YLeaf(YType.uint32, 'wis-alarms-wlos'), ['int'])),
                        ('wis_alarms_plcd', (YLeaf(YType.uint32, 'wis-alarms-plcd'), ['int'])),
                        ('wis_alarms_lfebip', (YLeaf(YType.uint64, 'wis-alarms-lfebip'), ['int'])),
                        ('wis_alarms_pbec', (YLeaf(YType.uint64, 'wis-alarms-pbec'), ['int'])),
                        ('wis_alarms_plmp', (YLeaf(YType.uint32, 'wis-alarms-plmp'), ['int'])),
                        ('sf_ber_threshold', (YLeaf(YType.uint32, 'sf-ber-threshold'), ['int'])),
                        ('sd_ber_threshold', (YLeaf(YType.uint32, 'sd-ber-threshold'), ['int'])),
                        ('sf_ber_report', (YLeaf(YType.enumeration, 'sf-ber-report'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyAlarmRepStatus', '')])),
                        ('sd_ber_report', (YLeaf(YType.enumeration, 'sd-ber-report'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyAlarmRepStatus', '')])),
                        ('operational_mode', (YLeaf(YType.enumeration, 'operational-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyModeInfo', '')])),
                        ('remote_ip', (YLeaf(YType.str, 'remote-ip'), ['str'])),
                        ('register_p_febe', (YLeaf(YType.uint32, 'register-p-febe'), ['int'])),
                        ('register_l_fe_bip', (YLeaf(YType.uint32, 'register-l-fe-bip'), ['int'])),
                        ('register_l_bip', (YLeaf(YType.uint32, 'register-l-bip'), ['int'])),
                        ('register_p_bec', (YLeaf(YType.uint32, 'register-p-bec'), ['int'])),
                        ('register_s_bip', (YLeaf(YType.uint32, 'register-s-bip'), ['int'])),
                        ('register_j1_rx0', (YLeaf(YType.uint32, 'register-j1-rx0'), ['int'])),
                        ('register_j1_rx1', (YLeaf(YType.uint32, 'register-j1-rx1'), ['int'])),
                        ('register_j1_rx2', (YLeaf(YType.uint32, 'register-j1-rx2'), ['int'])),
                        ('register_j1_rx3', (YLeaf(YType.uint32, 'register-j1-rx3'), ['int'])),
                        ('register_j1_rx4', (YLeaf(YType.uint32, 'register-j1-rx4'), ['int'])),
                        ('register_j1_rx5', (YLeaf(YType.uint32, 'register-j1-rx5'), ['int'])),
                        ('register_j1_rx6', (YLeaf(YType.uint32, 'register-j1-rx6'), ['int'])),
                        ('register_j1_rx7', (YLeaf(YType.uint32, 'register-j1-rx7'), ['int'])),
                        ('wanphy_poll_timer', (YLeaf(YType.uint32, 'wanphy-poll-timer'), ['int'])),
                    ])
                    self.admin_mode = None
                    self.port_state = None
                    self.section_lof = None
                    self.section_los = None
                    self.section_bip = None
                    self.line_ais = None
                    self.line_rdi = None
                    self.line_febe = None
                    self.line_bip = None
                    self.path_ais = None
                    self.path_rdi = None
                    self.path_febe = None
                    self.path_bip = None
                    self.path_lop = None
                    self.path_newptr = None
                    self.path_pse = None
                    self.path_nse = None
                    self.wis_alarms_ser = None
                    self.wis_alarms_felcdp = None
                    self.wis_alarms_feaisp = None
                    self.wis_alarms_wlos = None
                    self.wis_alarms_plcd = None
                    self.wis_alarms_lfebip = None
                    self.wis_alarms_pbec = None
                    self.wis_alarms_plmp = None
                    self.sf_ber_threshold = None
                    self.sd_ber_threshold = None
                    self.sf_ber_report = None
                    self.sd_ber_report = None
                    self.operational_mode = None
                    self.remote_ip = None
                    self.register_p_febe = None
                    self.register_l_fe_bip = None
                    self.register_l_bip = None
                    self.register_p_bec = None
                    self.register_s_bip = None
                    self.register_j1_rx0 = None
                    self.register_j1_rx1 = None
                    self.register_j1_rx2 = None
                    self.register_j1_rx3 = None
                    self.register_j1_rx4 = None
                    self.register_j1_rx5 = None
                    self.register_j1_rx6 = None
                    self.register_j1_rx7 = None
                    self.wanphy_poll_timer = None
                    self._segment_path = lambda: "info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Wanphy.Controllers.Controller.Info, ['admin_mode', 'port_state', 'section_lof', 'section_los', 'section_bip', 'line_ais', 'line_rdi', 'line_febe', 'line_bip', 'path_ais', 'path_rdi', 'path_febe', 'path_bip', 'path_lop', 'path_newptr', 'path_pse', 'path_nse', 'wis_alarms_ser', 'wis_alarms_felcdp', 'wis_alarms_feaisp', 'wis_alarms_wlos', 'wis_alarms_plcd', 'wis_alarms_lfebip', 'wis_alarms_pbec', 'wis_alarms_plmp', 'sf_ber_threshold', 'sd_ber_threshold', 'sf_ber_report', 'sd_ber_report', 'operational_mode', 'remote_ip', 'register_p_febe', 'register_l_fe_bip', 'register_l_bip', 'register_p_bec', 'register_s_bip', 'register_j1_rx0', 'register_j1_rx1', 'register_j1_rx2', 'register_j1_rx3', 'register_j1_rx4', 'register_j1_rx5', 'register_j1_rx6', 'register_j1_rx7', 'wanphy_poll_timer'], name, value)

    def clone_ptr(self):
        self._top_entity = Wanphy()
        return self._top_entity

