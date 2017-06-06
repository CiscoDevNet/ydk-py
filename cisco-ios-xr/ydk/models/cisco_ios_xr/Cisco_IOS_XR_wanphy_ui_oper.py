""" Cisco_IOS_XR_wanphy_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package operational data.

This module contains definitions
for the following management objects\:
  wanphy\: WANPHY operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class WanphyAlarmRepStatusEnum(Enum):
    """
    WanphyAlarmRepStatusEnum

    WANPHY Alarm Report Status

    .. data:: disable = 0

    	Alarm reporting is disable

    .. data:: enable = 1

    	Alarm reporting is enable

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
        return meta._meta_table['WanphyAlarmRepStatusEnum']


class WanphyModeInfoEnum(Enum):
    """
    WanphyModeInfoEnum

    WANPHY Modes

    .. data:: lan = 0

    	LAN mode

    .. data:: wan = 1

    	WAN mode

    """

    lan = 0

    wan = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
        return meta._meta_table['WanphyModeInfoEnum']



class Wanphy(object):
    """
    WANPHY operational data
    
    .. attribute:: controllers
    
    	All WANPHY controller operational data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers>`
    
    

    """

    _prefix = 'wanphy-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.controllers = Wanphy.Controllers()
        self.controllers.parent = self


    class Controllers(object):
        """
        All WANPHY controller operational data
        
        .. attribute:: controller
        
        	WANPHY controller operational data
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.Wanphy.Controllers.Controller>`
        
        

        """

        _prefix = 'wanphy-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.controller = YList()
            self.controller.parent = self
            self.controller.name = 'controller'


        class Controller(object):
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
                self.parent = None
                self.controller_name = None
                self.info = Wanphy.Controllers.Controller.Info()
                self.info.parent = self


            class Info(object):
                """
                WANPHY controller operational data
                
                .. attribute:: admin_mode
                
                	Configuration Mode
                	**type**\:   :py:class:`WanphyModeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfoEnum>`
                
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
                	**type**\:   :py:class:`WanphyModeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyModeInfoEnum>`
                
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
                	**type**\:   :py:class:`WanphyAlarmRepStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatusEnum>`
                
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
                	**type**\:   :py:class:`WanphyAlarmRepStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper.WanphyAlarmRepStatusEnum>`
                
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
                    self.parent = None
                    self.admin_mode = None
                    self.line_ais = None
                    self.line_bip = None
                    self.line_febe = None
                    self.line_rdi = None
                    self.operational_mode = None
                    self.path_ais = None
                    self.path_bip = None
                    self.path_febe = None
                    self.path_lop = None
                    self.path_newptr = None
                    self.path_nse = None
                    self.path_pse = None
                    self.path_rdi = None
                    self.port_state = None
                    self.register_j1_rx0 = None
                    self.register_j1_rx1 = None
                    self.register_j1_rx2 = None
                    self.register_j1_rx3 = None
                    self.register_j1_rx4 = None
                    self.register_j1_rx5 = None
                    self.register_j1_rx6 = None
                    self.register_j1_rx7 = None
                    self.register_l_bip = None
                    self.register_l_fe_bip = None
                    self.register_p_bec = None
                    self.register_p_febe = None
                    self.register_s_bip = None
                    self.remote_ip = None
                    self.sd_ber_report = None
                    self.sd_ber_threshold = None
                    self.section_bip = None
                    self.section_lof = None
                    self.section_los = None
                    self.sf_ber_report = None
                    self.sf_ber_threshold = None
                    self.wanphy_poll_timer = None
                    self.wis_alarms_feaisp = None
                    self.wis_alarms_felcdp = None
                    self.wis_alarms_lfebip = None
                    self.wis_alarms_pbec = None
                    self.wis_alarms_plcd = None
                    self.wis_alarms_plmp = None
                    self.wis_alarms_ser = None
                    self.wis_alarms_wlos = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wanphy-ui-oper:info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_mode is not None:
                        return True

                    if self.line_ais is not None:
                        return True

                    if self.line_bip is not None:
                        return True

                    if self.line_febe is not None:
                        return True

                    if self.line_rdi is not None:
                        return True

                    if self.operational_mode is not None:
                        return True

                    if self.path_ais is not None:
                        return True

                    if self.path_bip is not None:
                        return True

                    if self.path_febe is not None:
                        return True

                    if self.path_lop is not None:
                        return True

                    if self.path_newptr is not None:
                        return True

                    if self.path_nse is not None:
                        return True

                    if self.path_pse is not None:
                        return True

                    if self.path_rdi is not None:
                        return True

                    if self.port_state is not None:
                        return True

                    if self.register_j1_rx0 is not None:
                        return True

                    if self.register_j1_rx1 is not None:
                        return True

                    if self.register_j1_rx2 is not None:
                        return True

                    if self.register_j1_rx3 is not None:
                        return True

                    if self.register_j1_rx4 is not None:
                        return True

                    if self.register_j1_rx5 is not None:
                        return True

                    if self.register_j1_rx6 is not None:
                        return True

                    if self.register_j1_rx7 is not None:
                        return True

                    if self.register_l_bip is not None:
                        return True

                    if self.register_l_fe_bip is not None:
                        return True

                    if self.register_p_bec is not None:
                        return True

                    if self.register_p_febe is not None:
                        return True

                    if self.register_s_bip is not None:
                        return True

                    if self.remote_ip is not None:
                        return True

                    if self.sd_ber_report is not None:
                        return True

                    if self.sd_ber_threshold is not None:
                        return True

                    if self.section_bip is not None:
                        return True

                    if self.section_lof is not None:
                        return True

                    if self.section_los is not None:
                        return True

                    if self.sf_ber_report is not None:
                        return True

                    if self.sf_ber_threshold is not None:
                        return True

                    if self.wanphy_poll_timer is not None:
                        return True

                    if self.wis_alarms_feaisp is not None:
                        return True

                    if self.wis_alarms_felcdp is not None:
                        return True

                    if self.wis_alarms_lfebip is not None:
                        return True

                    if self.wis_alarms_pbec is not None:
                        return True

                    if self.wis_alarms_plcd is not None:
                        return True

                    if self.wis_alarms_plmp is not None:
                        return True

                    if self.wis_alarms_ser is not None:
                        return True

                    if self.wis_alarms_wlos is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
                    return meta._meta_table['Wanphy.Controllers.Controller.Info']['meta_info']

            @property
            def _common_path(self):
                if self.controller_name is None:
                    raise YPYModelError('Key property controller_name is None')

                return '/Cisco-IOS-XR-wanphy-ui-oper:wanphy/Cisco-IOS-XR-wanphy-ui-oper:controllers/Cisco-IOS-XR-wanphy-ui-oper:controller[Cisco-IOS-XR-wanphy-ui-oper:controller-name = ' + str(self.controller_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.controller_name is not None:
                    return True

                if self.info is not None and self.info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
                return meta._meta_table['Wanphy.Controllers.Controller']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-wanphy-ui-oper:wanphy/Cisco-IOS-XR-wanphy-ui-oper:controllers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.controller is not None:
                for child_ref in self.controller:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
            return meta._meta_table['Wanphy.Controllers']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-wanphy-ui-oper:wanphy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.controllers is not None and self.controllers._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_oper as meta
        return meta._meta_table['Wanphy']['meta_info']


