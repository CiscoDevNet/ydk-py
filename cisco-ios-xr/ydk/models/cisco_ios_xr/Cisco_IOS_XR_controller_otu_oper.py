""" Cisco_IOS_XR_controller_otu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package operational data.

This module contains definitions
for the following management objects\:
  otu\: OTU operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class GmplsOtuTtiMode(Enum):
    """
    GmplsOtuTtiMode

    Gmpls otu tti mode

    .. data:: gmpls_otu_tti_mode_none = 0

    	Not Set

    .. data:: gmpls_otu_tti_mode_sm = 1

    	Section Monitoring

    .. data:: gmpls_otu_tti_mode_pm = 2

    	Path Monitoring

    .. data:: gmpls_otu_tti_mode_tcm = 3

    	Tandem Connection Monitoring

    """

    gmpls_otu_tti_mode_none = Enum.YLeaf(0, "gmpls-otu-tti-mode-none")

    gmpls_otu_tti_mode_sm = Enum.YLeaf(1, "gmpls-otu-tti-mode-sm")

    gmpls_otu_tti_mode_pm = Enum.YLeaf(2, "gmpls-otu-tti-mode-pm")

    gmpls_otu_tti_mode_tcm = Enum.YLeaf(3, "gmpls-otu-tti-mode-tcm")


class OtuDerState(Enum):
    """
    OtuDerState

    Otu der state

    .. data:: out_of_service = 0

    	Out Of Service

    .. data:: in_service = 1

    	In Service

    .. data:: maintenance = 2

    	Maintenance

    .. data:: ais = 3

    	Automatic In Service

    """

    out_of_service = Enum.YLeaf(0, "out-of-service")

    in_service = Enum.YLeaf(1, "in-service")

    maintenance = Enum.YLeaf(2, "maintenance")

    ais = Enum.YLeaf(3, "ais")


class OtuG709FecMode(Enum):
    """
    OtuG709FecMode

    Otu g709fec mode

    .. data:: otu_bag_none_fec = 1

    	NONE

    .. data:: otu_bag_standard_fec = 2

    	STANDARD

    .. data:: otu_bag_1_i_7_fec = 4

    	ENHANCEDI.7

    .. data:: otu_bag_1_i_4_fec = 8

    	ENHANCEDI.4

    .. data:: otu_bag_swizzle_fec = 16

    	SWIZZLE

    .. data:: otu_bag_hg20_fec = 32

    	HIGH GAIN20

    .. data:: otu_bag_enhanced_hg7_fec = 64

    	Enhanced High Gain 7

    .. data:: otu_bag_sd20_fec = 128

    	Soft-Decision 20

    .. data:: otu_bag_sd7_fec = 256

    	Soft-Decision 7

    .. data:: otu_bag_all_fec = 512

    	ALL

    """

    otu_bag_none_fec = Enum.YLeaf(1, "otu-bag-none-fec")

    otu_bag_standard_fec = Enum.YLeaf(2, "otu-bag-standard-fec")

    otu_bag_1_i_7_fec = Enum.YLeaf(4, "otu-bag-1-i-7-fec")

    otu_bag_1_i_4_fec = Enum.YLeaf(8, "otu-bag-1-i-4-fec")

    otu_bag_swizzle_fec = Enum.YLeaf(16, "otu-bag-swizzle-fec")

    otu_bag_hg20_fec = Enum.YLeaf(32, "otu-bag-hg20-fec")

    otu_bag_enhanced_hg7_fec = Enum.YLeaf(64, "otu-bag-enhanced-hg7-fec")

    otu_bag_sd20_fec = Enum.YLeaf(128, "otu-bag-sd20-fec")

    otu_bag_sd7_fec = Enum.YLeaf(256, "otu-bag-sd7-fec")

    otu_bag_all_fec = Enum.YLeaf(512, "otu-bag-all-fec")


class OtuLoopBackMode(Enum):
    """
    OtuLoopBackMode

    Otu loop back mode

    .. data:: none = 1

    	None

    .. data:: line = 2

    	Line

    .. data:: internal = 4

    	Internal

    """

    none = Enum.YLeaf(1, "none")

    line = Enum.YLeaf(2, "line")

    internal = Enum.YLeaf(4, "internal")


class OtuPerMon(Enum):
    """
    OtuPerMon

    Otu per mon

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OtuPpFsmState(Enum):
    """
    OtuPpFsmState

    Otu pp fsm state

    .. data:: otu_in_active = 0

    	In Active

    .. data:: otu_disabled = 1

    	Disabled

    .. data:: otu_normal_state = 2

    	Normal

    .. data:: otu_local_failing = 3

    	Local Failing

    .. data:: otu_remote_failing = 4

    	Remote Failing

    .. data:: otu_main_t_failing = 5

    	Maintance Failing

    .. data:: otu_regen_failing = 6

    	Regenerator Failing

    .. data:: otu_local_failed = 7

    	Local Failed

    .. data:: otu_remote_failed = 8

    	Remote Failed

    .. data:: otu_main_t_failed = 9

    	Maintance Failed

    .. data:: otu_regen_failed = 10

    	Regenerator Failed

    """

    otu_in_active = Enum.YLeaf(0, "otu-in-active")

    otu_disabled = Enum.YLeaf(1, "otu-disabled")

    otu_normal_state = Enum.YLeaf(2, "otu-normal-state")

    otu_local_failing = Enum.YLeaf(3, "otu-local-failing")

    otu_remote_failing = Enum.YLeaf(4, "otu-remote-failing")

    otu_main_t_failing = Enum.YLeaf(5, "otu-main-t-failing")

    otu_regen_failing = Enum.YLeaf(6, "otu-regen-failing")

    otu_local_failed = Enum.YLeaf(7, "otu-local-failed")

    otu_remote_failed = Enum.YLeaf(8, "otu-remote-failed")

    otu_main_t_failed = Enum.YLeaf(9, "otu-main-t-failed")

    otu_regen_failed = Enum.YLeaf(10, "otu-regen-failed")


class OtuPpIntfState(Enum):
    """
    OtuPpIntfState

    Otu pp intf state

    .. data:: otu_pp_intf_up = 0

    	Interface is Up

    .. data:: otu_pp_intf_failing = 1

    	Interface is Going Down

    .. data:: otu_pp_intf_down = 2

    	Interface Down

    """

    otu_pp_intf_up = Enum.YLeaf(0, "otu-pp-intf-up")

    otu_pp_intf_failing = Enum.YLeaf(1, "otu-pp-intf-failing")

    otu_pp_intf_down = Enum.YLeaf(2, "otu-pp-intf-down")


class OtuSecState(Enum):
    """
    OtuSecState

    Otu sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintenance = 1

    	Maintenance

    .. data:: ais = 2

    	Automatic In Service

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")

    ais = Enum.YLeaf(2, "ais")


class OtuStateEt(Enum):
    """
    OtuStateEt

    Otu state et

    .. data:: not_ready = 0

    	Not Ready

    .. data:: admin_down = 1

    	Admin Down

    .. data:: down = 2

    	Down

    .. data:: up = 3

    	Up

    .. data:: shutdown = 4

    	Shutdown

    .. data:: error_disable = 5

    	Error Disable

    .. data:: down_immediate = 6

    	Down Immediate

    .. data:: down_immediate_admin = 7

    	Down Immediate Admin

    .. data:: down_graceful = 8

    	Down Graceful

    .. data:: begin_shutdown = 9

    	Begin Shutdown

    .. data:: end_shutdown = 10

    	End Shutdown

    .. data:: begin_error_disable = 11

    	Begin Error Disable

    .. data:: end_error_disable = 12

    	End Error Disable

    .. data:: begin_down_graceful = 13

    	Begin Down Graceful

    .. data:: reset = 14

    	Reset

    .. data:: operational = 15

    	Operational

    .. data:: not_operational = 16

    	Not Operational

    .. data:: unknown = 17

    	Unknown

    .. data:: last = 18

    	Last

    """

    not_ready = Enum.YLeaf(0, "not-ready")

    admin_down = Enum.YLeaf(1, "admin-down")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    shutdown = Enum.YLeaf(4, "shutdown")

    error_disable = Enum.YLeaf(5, "error-disable")

    down_immediate = Enum.YLeaf(6, "down-immediate")

    down_immediate_admin = Enum.YLeaf(7, "down-immediate-admin")

    down_graceful = Enum.YLeaf(8, "down-graceful")

    begin_shutdown = Enum.YLeaf(9, "begin-shutdown")

    end_shutdown = Enum.YLeaf(10, "end-shutdown")

    begin_error_disable = Enum.YLeaf(11, "begin-error-disable")

    end_error_disable = Enum.YLeaf(12, "end-error-disable")

    begin_down_graceful = Enum.YLeaf(13, "begin-down-graceful")

    reset = Enum.YLeaf(14, "reset")

    operational = Enum.YLeaf(15, "operational")

    not_operational = Enum.YLeaf(16, "not-operational")

    unknown = Enum.YLeaf(17, "unknown")

    last = Enum.YLeaf(18, "last")


class OtuTtiEt(Enum):
    """
    OtuTtiEt

    Otu tti et

    .. data:: ascii = 0

    	ASCII

    .. data:: hex = 1

    	HEX

    .. data:: full_ascii = 2

    	FULL ASCII

    .. data:: full_hex = 3

    	FULL HEX

    """

    ascii = Enum.YLeaf(0, "ascii")

    hex = Enum.YLeaf(1, "hex")

    full_ascii = Enum.YLeaf(2, "full-ascii")

    full_hex = Enum.YLeaf(3, "full-hex")



class Otu(Entity):
    """
    OTU operational data
    
    .. attribute:: controllers
    
    	All OTU Port operational data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers>`
    
    

    """

    _prefix = 'controller-otu-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Otu, self).__init__()
        self._top_entity = None

        self.yang_name = "otu"
        self.yang_parent_name = "Cisco-IOS-XR-controller-otu-oper"

        self.controllers = Otu.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")


    class Controllers(Entity):
        """
        All OTU Port operational data
        
        .. attribute:: controller
        
        	OTU Port operational data
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller>`
        
        

        """

        _prefix = 'controller-otu-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Otu.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "otu"

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
                        super(Otu.Controllers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Otu.Controllers, self).__setattr__(name, value)


        class Controller(Entity):
            """
            OTU Port operational data
            
            .. attribute:: controller_name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: info
            
            	OTU port operational data
            	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info>`
            
            

            """

            _prefix = 'controller-otu-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Otu.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.info = Otu.Controllers.Controller.Info()
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
                            super(Otu.Controllers.Controller, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Otu.Controllers.Controller, self).__setattr__(name, value)


            class Info(Entity):
                """
                OTU port operational data
                
                .. attribute:: auto_tti_flag
                
                	Auto tti flag
                	**type**\:  bool
                
                .. attribute:: config_sec_state
                
                	Sec State
                	**type**\:   :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                .. attribute:: derivedstate_mode
                
                	Derived State
                	**type**\:   :py:class:`OtuDerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuDerState>`
                
                .. attribute:: ec
                
                	Average bit errors corrected
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ec_value
                
                	EC value present
                	**type**\:  bool
                
                .. attribute:: fec_mode
                
                	FEC
                	**type**\:   :py:class:`OtuG709FecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuG709FecMode>`
                
                .. attribute:: gcc_mode
                
                	OTU GCC
                	**type**\:  bool
                
                .. attribute:: gmpls_tti_mode
                
                	GMPLS TTI MODE
                	**type**\:   :py:class:`GmplsOtuTtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.GmplsOtuTtiMode>`
                
                .. attribute:: gmpls_tvm_id
                
                	GMPLS TCM ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: inherit_sec_state
                
                	Sec State
                	**type**\:   :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                .. attribute:: local
                
                	TTI
                	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Local>`
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\:   :py:class:`OtuLoopBackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuLoopBackMode>`
                
                .. attribute:: name
                
                	Interface Name
                	**type**\:  str
                
                .. attribute:: network_srlg
                
                	Network Shared Risk Link Group information
                	**type**\:   :py:class:`NetworkSrlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg>`
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\:  bool
                
                .. attribute:: otu_alarm_info
                
                	OTU layer alarm Information
                	**type**\:   :py:class:`OtuAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo>`
                
                .. attribute:: otu_fec_satistics
                
                	OTU FEC Statistics
                	**type**\:   :py:class:`OtuFecSatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuFecSatistics>`
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\:   :py:class:`OtuPerMon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPerMon>`
                
                .. attribute:: pre_fec_ber_mantissa
                
                	Pre fec val mantissa
                	**type**\:  bool
                
                .. attribute:: pre_fec_ber_value
                
                	Pre fec val present 
                	**type**\:  bool
                
                .. attribute:: pre_fec_mantissa
                
                	Pre FEC BER Mantissa in form E\-<mantisaa>
                	**type**\:  int
                
                	**range:** \-128..127
                
                .. attribute:: pre_fec_val
                
                	Pre FEC BER Value in form 0.00
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: proactive
                
                	Proactive Protection
                	**type**\:   :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Proactive>`
                
                .. attribute:: q
                
                	q value calculated
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: q_margin
                
                	q margin calculated
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote
                
                	Remote
                	**type**\:   :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Remote>`
                
                .. attribute:: sd
                
                	SD in the form of 1.0E \- <SD>
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: sf
                
                	SF in the form of 1.0E \- <SF>
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: state
                
                	Admin State
                	**type**\:   :py:class:`OtuStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuStateEt>`
                
                .. attribute:: tti_mode
                
                	OTU TTI
                	**type**\:   :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode>`
                
                .. attribute:: uc
                
                	Uncorrected word count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: uc_value
                
                	Uc value present
                	**type**\:  bool
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Otu.Controllers.Controller.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "controller"

                    self.auto_tti_flag = YLeaf(YType.boolean, "auto-tti-flag")

                    self.config_sec_state = YLeaf(YType.enumeration, "config-sec-state")

                    self.derivedstate_mode = YLeaf(YType.enumeration, "derivedstate-mode")

                    self.ec = YLeaf(YType.uint64, "ec")

                    self.ec_value = YLeaf(YType.boolean, "ec-value")

                    self.fec_mode = YLeaf(YType.enumeration, "fec-mode")

                    self.gcc_mode = YLeaf(YType.boolean, "gcc-mode")

                    self.gmpls_tti_mode = YLeaf(YType.enumeration, "gmpls-tti-mode")

                    self.gmpls_tvm_id = YLeaf(YType.uint8, "gmpls-tvm-id")

                    self.inherit_sec_state = YLeaf(YType.enumeration, "inherit-sec-state")

                    self.loopback_mode = YLeaf(YType.enumeration, "loopback-mode")

                    self.name = YLeaf(YType.str, "name")

                    self.nv_optical_support = YLeaf(YType.boolean, "nv-optical-support")

                    self.performance_monitoring = YLeaf(YType.enumeration, "performance-monitoring")

                    self.pre_fec_ber_mantissa = YLeaf(YType.boolean, "pre-fec-ber-mantissa")

                    self.pre_fec_ber_value = YLeaf(YType.boolean, "pre-fec-ber-value")

                    self.pre_fec_mantissa = YLeaf(YType.int8, "pre-fec-mantissa")

                    self.pre_fec_val = YLeaf(YType.int32, "pre-fec-val")

                    self.q = YLeaf(YType.uint64, "q")

                    self.q_margin = YLeaf(YType.uint64, "q-margin")

                    self.sd = YLeaf(YType.uint8, "sd")

                    self.sf = YLeaf(YType.uint8, "sf")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.uc = YLeaf(YType.uint64, "uc")

                    self.uc_value = YLeaf(YType.boolean, "uc-value")

                    self.local = Otu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self._children_name_map["local"] = "local"
                    self._children_yang_names.add("local")

                    self.network_srlg = Otu.Controllers.Controller.Info.NetworkSrlg()
                    self.network_srlg.parent = self
                    self._children_name_map["network_srlg"] = "network-srlg"
                    self._children_yang_names.add("network-srlg")

                    self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                    self.otu_alarm_info.parent = self
                    self._children_name_map["otu_alarm_info"] = "otu-alarm-info"
                    self._children_yang_names.add("otu-alarm-info")

                    self.otu_fec_satistics = Otu.Controllers.Controller.Info.OtuFecSatistics()
                    self.otu_fec_satistics.parent = self
                    self._children_name_map["otu_fec_satistics"] = "otu-fec-satistics"
                    self._children_yang_names.add("otu-fec-satistics")

                    self.proactive = Otu.Controllers.Controller.Info.Proactive()
                    self.proactive.parent = self
                    self._children_name_map["proactive"] = "proactive"
                    self._children_yang_names.add("proactive")

                    self.remote = Otu.Controllers.Controller.Info.Remote()
                    self.remote.parent = self
                    self._children_name_map["remote"] = "remote"
                    self._children_yang_names.add("remote")

                    self.tti_mode = Otu.Controllers.Controller.Info.TtiMode()
                    self.tti_mode.parent = self
                    self._children_name_map["tti_mode"] = "tti-mode"
                    self._children_yang_names.add("tti-mode")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("auto_tti_flag",
                                    "config_sec_state",
                                    "derivedstate_mode",
                                    "ec",
                                    "ec_value",
                                    "fec_mode",
                                    "gcc_mode",
                                    "gmpls_tti_mode",
                                    "gmpls_tvm_id",
                                    "inherit_sec_state",
                                    "loopback_mode",
                                    "name",
                                    "nv_optical_support",
                                    "performance_monitoring",
                                    "pre_fec_ber_mantissa",
                                    "pre_fec_ber_value",
                                    "pre_fec_mantissa",
                                    "pre_fec_val",
                                    "q",
                                    "q_margin",
                                    "sd",
                                    "sf",
                                    "state",
                                    "uc",
                                    "uc_value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Otu.Controllers.Controller.Info, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Otu.Controllers.Controller.Info, self).__setattr__(name, value)


                class Local(Entity):
                    """
                    TTI
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Local, self).__init__()

                        self.yang_name = "local"
                        self.yang_parent_name = "info"

                        self.if_index = YLeaf(YType.uint32, "if-index")

                        self.router_id = YLeaf(YType.uint32, "router-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_index",
                                        "router_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Otu.Controllers.Controller.Info.Local, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.Local, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.if_index.is_set or
                            self.router_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_index.yfilter != YFilter.not_set or
                            self.router_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "local" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_index.get_name_leafdata())
                        if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-index" or name == "router-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-index"):
                            self.if_index = value
                            self.if_index.value_namespace = name_space
                            self.if_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "router-id"):
                            self.router_id = value
                            self.router_id.value_namespace = name_space
                            self.router_id.value_namespace_prefix = name_space_prefix


                class Remote(Entity):
                    """
                    Remote
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "info"

                        self.if_index = YLeaf(YType.uint32, "if-index")

                        self.router_id = YLeaf(YType.uint32, "router-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_index",
                                        "router_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Otu.Controllers.Controller.Info.Remote, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.Remote, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.if_index.is_set or
                            self.router_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_index.yfilter != YFilter.not_set or
                            self.router_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_index.get_name_leafdata())
                        if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-index" or name == "router-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-index"):
                            self.if_index = value
                            self.if_index.value_namespace = name_space
                            self.if_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "router-id"):
                            self.router_id = value
                            self.router_id.value_namespace = name_space
                            self.router_id.value_namespace_prefix = name_space_prefix


                class TtiMode(Entity):
                    """
                    OTU TTI
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\:   :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\:   :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\:   :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI sent
                    	**type**\:   :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\:   :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    .. attribute:: remote_host_name
                    
                    	Remote host name
                    	**type**\:  str
                    
                    .. attribute:: remote_interface
                    
                    	Remote Interface Name
                    	**type**\:  str
                    
                    .. attribute:: remote_ip_addr
                    
                    	Remote host ip
                    	**type**\:  str
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\:   :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.TtiMode, self).__init__()

                        self.yang_name = "tti-mode"
                        self.yang_parent_name = "info"

                        self.g709tti_exp_mode = YLeaf(YType.enumeration, "g709tti-exp-mode")

                        self.g709tti_rec_mode = YLeaf(YType.enumeration, "g709tti-rec-mode")

                        self.g709tti_sent_mode = YLeaf(YType.enumeration, "g709tti-sent-mode")

                        self.remote_host_name = YLeaf(YType.str, "remote-host-name")

                        self.remote_interface = YLeaf(YType.str, "remote-interface")

                        self.remote_ip_addr = YLeaf(YType.str, "remote-ip-addr")

                        self.exp = Otu.Controllers.Controller.Info.TtiMode.Exp()
                        self.exp.parent = self
                        self._children_name_map["exp"] = "exp"
                        self._children_yang_names.add("exp")

                        self.rec = Otu.Controllers.Controller.Info.TtiMode.Rec()
                        self.rec.parent = self
                        self._children_name_map["rec"] = "rec"
                        self._children_yang_names.add("rec")

                        self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self
                        self._children_name_map["tx"] = "tx"
                        self._children_yang_names.add("tx")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("g709tti_exp_mode",
                                        "g709tti_rec_mode",
                                        "g709tti_sent_mode",
                                        "remote_host_name",
                                        "remote_interface",
                                        "remote_ip_addr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Otu.Controllers.Controller.Info.TtiMode, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.TtiMode, self).__setattr__(name, value)


                    class Tx(Entity):
                        """
                        String Sent
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Tx, self).__init__()

                            self.yang_name = "tx"
                            self.yang_parent_name = "tti-mode"

                            self.dapi = YLeafList(YType.uint8, "dapi")

                            self.full_tti_ascii_string = YLeaf(YType.str, "full-tti-ascii-string")

                            self.operator_specific = YLeafList(YType.uint8, "operator-specific")

                            self.sapi = YLeafList(YType.uint8, "sapi")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dapi",
                                            "full_tti_ascii_string",
                                            "operator_specific",
                                            "sapi") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.TtiMode.Tx, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.TtiMode.Tx, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.full_tti_ascii_string.is_set

                        def has_operation(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dapi.yfilter != YFilter.not_set or
                                self.full_tti_ascii_string.yfilter != YFilter.not_set or
                                self.operator_specific.yfilter != YFilter.not_set or
                                self.sapi.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.full_tti_ascii_string.is_set or self.full_tti_ascii_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.full_tti_ascii_string.get_name_leafdata())

                            leaf_name_data.extend(self.dapi.get_name_leafdata())

                            leaf_name_data.extend(self.operator_specific.get_name_leafdata())

                            leaf_name_data.extend(self.sapi.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dapi" or name == "full-tti-ascii-string" or name == "operator-specific" or name == "sapi"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dapi"):
                                self.dapi.append(value)
                            if(value_path == "full-tti-ascii-string"):
                                self.full_tti_ascii_string = value
                                self.full_tti_ascii_string.value_namespace = name_space
                                self.full_tti_ascii_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "operator-specific"):
                                self.operator_specific.append(value)
                            if(value_path == "sapi"):
                                self.sapi.append(value)


                    class Exp(Entity):
                        """
                        String Expected
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Exp, self).__init__()

                            self.yang_name = "exp"
                            self.yang_parent_name = "tti-mode"

                            self.dapi = YLeafList(YType.uint8, "dapi")

                            self.full_tti_ascii_string = YLeaf(YType.str, "full-tti-ascii-string")

                            self.operator_specific = YLeafList(YType.uint8, "operator-specific")

                            self.sapi = YLeafList(YType.uint8, "sapi")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dapi",
                                            "full_tti_ascii_string",
                                            "operator_specific",
                                            "sapi") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.TtiMode.Exp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.TtiMode.Exp, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.full_tti_ascii_string.is_set

                        def has_operation(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dapi.yfilter != YFilter.not_set or
                                self.full_tti_ascii_string.yfilter != YFilter.not_set or
                                self.operator_specific.yfilter != YFilter.not_set or
                                self.sapi.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "exp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.full_tti_ascii_string.is_set or self.full_tti_ascii_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.full_tti_ascii_string.get_name_leafdata())

                            leaf_name_data.extend(self.dapi.get_name_leafdata())

                            leaf_name_data.extend(self.operator_specific.get_name_leafdata())

                            leaf_name_data.extend(self.sapi.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dapi" or name == "full-tti-ascii-string" or name == "operator-specific" or name == "sapi"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dapi"):
                                self.dapi.append(value)
                            if(value_path == "full-tti-ascii-string"):
                                self.full_tti_ascii_string = value
                                self.full_tti_ascii_string.value_namespace = name_space
                                self.full_tti_ascii_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "operator-specific"):
                                self.operator_specific.append(value)
                            if(value_path == "sapi"):
                                self.sapi.append(value)


                    class Rec(Entity):
                        """
                        String Received
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Rec, self).__init__()

                            self.yang_name = "rec"
                            self.yang_parent_name = "tti-mode"

                            self.dapi = YLeafList(YType.uint8, "dapi")

                            self.full_tti_ascii_string = YLeaf(YType.str, "full-tti-ascii-string")

                            self.operator_specific = YLeafList(YType.uint8, "operator-specific")

                            self.sapi = YLeafList(YType.uint8, "sapi")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dapi",
                                            "full_tti_ascii_string",
                                            "operator_specific",
                                            "sapi") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.TtiMode.Rec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.TtiMode.Rec, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.full_tti_ascii_string.is_set

                        def has_operation(self):
                            for leaf in self.dapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.operator_specific.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            for leaf in self.sapi.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dapi.yfilter != YFilter.not_set or
                                self.full_tti_ascii_string.yfilter != YFilter.not_set or
                                self.operator_specific.yfilter != YFilter.not_set or
                                self.sapi.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.full_tti_ascii_string.is_set or self.full_tti_ascii_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.full_tti_ascii_string.get_name_leafdata())

                            leaf_name_data.extend(self.dapi.get_name_leafdata())

                            leaf_name_data.extend(self.operator_specific.get_name_leafdata())

                            leaf_name_data.extend(self.sapi.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dapi" or name == "full-tti-ascii-string" or name == "operator-specific" or name == "sapi"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dapi"):
                                self.dapi.append(value)
                            if(value_path == "full-tti-ascii-string"):
                                self.full_tti_ascii_string = value
                                self.full_tti_ascii_string.value_namespace = name_space
                                self.full_tti_ascii_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "operator-specific"):
                                self.operator_specific.append(value)
                            if(value_path == "sapi"):
                                self.sapi.append(value)

                    def has_data(self):
                        return (
                            self.g709tti_exp_mode.is_set or
                            self.g709tti_rec_mode.is_set or
                            self.g709tti_sent_mode.is_set or
                            self.remote_host_name.is_set or
                            self.remote_interface.is_set or
                            self.remote_ip_addr.is_set or
                            (self.exp is not None and self.exp.has_data()) or
                            (self.rec is not None and self.rec.has_data()) or
                            (self.tx is not None and self.tx.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.g709tti_exp_mode.yfilter != YFilter.not_set or
                            self.g709tti_rec_mode.yfilter != YFilter.not_set or
                            self.g709tti_sent_mode.yfilter != YFilter.not_set or
                            self.remote_host_name.yfilter != YFilter.not_set or
                            self.remote_interface.yfilter != YFilter.not_set or
                            self.remote_ip_addr.yfilter != YFilter.not_set or
                            (self.exp is not None and self.exp.has_operation()) or
                            (self.rec is not None and self.rec.has_operation()) or
                            (self.tx is not None and self.tx.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tti-mode" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.g709tti_exp_mode.is_set or self.g709tti_exp_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g709tti_exp_mode.get_name_leafdata())
                        if (self.g709tti_rec_mode.is_set or self.g709tti_rec_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g709tti_rec_mode.get_name_leafdata())
                        if (self.g709tti_sent_mode.is_set or self.g709tti_sent_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g709tti_sent_mode.get_name_leafdata())
                        if (self.remote_host_name.is_set or self.remote_host_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_host_name.get_name_leafdata())
                        if (self.remote_interface.is_set or self.remote_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_interface.get_name_leafdata())
                        if (self.remote_ip_addr.is_set or self.remote_ip_addr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_ip_addr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "exp"):
                            if (self.exp is None):
                                self.exp = Otu.Controllers.Controller.Info.TtiMode.Exp()
                                self.exp.parent = self
                                self._children_name_map["exp"] = "exp"
                            return self.exp

                        if (child_yang_name == "rec"):
                            if (self.rec is None):
                                self.rec = Otu.Controllers.Controller.Info.TtiMode.Rec()
                                self.rec.parent = self
                                self._children_name_map["rec"] = "rec"
                            return self.rec

                        if (child_yang_name == "tx"):
                            if (self.tx is None):
                                self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                                self.tx.parent = self
                                self._children_name_map["tx"] = "tx"
                            return self.tx

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "exp" or name == "rec" or name == "tx" or name == "g709tti-exp-mode" or name == "g709tti-rec-mode" or name == "g709tti-sent-mode" or name == "remote-host-name" or name == "remote-interface" or name == "remote-ip-addr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "g709tti-exp-mode"):
                            self.g709tti_exp_mode = value
                            self.g709tti_exp_mode.value_namespace = name_space
                            self.g709tti_exp_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "g709tti-rec-mode"):
                            self.g709tti_rec_mode = value
                            self.g709tti_rec_mode.value_namespace = name_space
                            self.g709tti_rec_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "g709tti-sent-mode"):
                            self.g709tti_sent_mode = value
                            self.g709tti_sent_mode.value_namespace = name_space
                            self.g709tti_sent_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-host-name"):
                            self.remote_host_name = value
                            self.remote_host_name.value_namespace = name_space
                            self.remote_host_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-interface"):
                            self.remote_interface = value
                            self.remote_interface.value_namespace = name_space
                            self.remote_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-ip-addr"):
                            self.remote_ip_addr = value
                            self.remote_ip_addr.value_namespace = name_space
                            self.remote_ip_addr.value_namespace_prefix = name_space_prefix


                class NetworkSrlg(Entity):
                    """
                    Network Shared Risk Link Group information
                    
                    .. attribute:: srlg_info
                    
                    	Array of Network Shared Risk Link Group information
                    	**type**\: list of    :py:class:`SrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.NetworkSrlg, self).__init__()

                        self.yang_name = "network-srlg"
                        self.yang_parent_name = "info"

                        self.srlg_info = YList(self)

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
                                    super(Otu.Controllers.Controller.Info.NetworkSrlg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.NetworkSrlg, self).__setattr__(name, value)


                    class SrlgInfo(Entity):
                        """
                        Array of Network Shared Risk Link Group
                        information
                        
                        .. attribute:: set_id
                        
                        	Array to maintain set id number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srlg
                        
                        	Shared Risk Link Group information expressed in integer format
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, self).__init__()

                            self.yang_name = "srlg-info"
                            self.yang_parent_name = "network-srlg"

                            self.set_id = YLeaf(YType.uint32, "set-id")

                            self.srlg = YLeafList(YType.uint32, "srlg")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("set_id",
                                            "srlg") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.srlg.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.set_id.is_set

                        def has_operation(self):
                            for leaf in self.srlg.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.set_id.yfilter != YFilter.not_set or
                                self.srlg.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srlg-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_id.is_set or self.set_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_id.get_name_leafdata())

                            leaf_name_data.extend(self.srlg.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set-id" or name == "srlg"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "set-id"):
                                self.set_id = value
                                self.set_id.value_namespace = name_space
                                self.set_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg"):
                                self.srlg.append(value)

                    def has_data(self):
                        for c in self.srlg_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.srlg_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network-srlg" + path_buffer

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

                        if (child_yang_name == "srlg-info"):
                            for c in self.srlg_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.srlg_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class OtuAlarmInfo(Entity):
                    """
                    OTU layer alarm Information
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\:   :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais>`
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\:   :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi>`
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\:   :py:class:`Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae>`
                    
                    .. attribute:: ec
                    
                    	EC alarm
                    	**type**\:   :py:class:`Ec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec>`
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\:   :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc>`
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:   :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch>`
                    
                    .. attribute:: fecunc
                    
                    	FEC UnCorrected Word
                    	**type**\:   :py:class:`Fecunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc>`
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\:   :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae>`
                    
                    .. attribute:: lof
                    
                    	Loss of Frame
                    	**type**\:   :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof>`
                    
                    .. attribute:: lom
                    
                    	Loss of MultiFrame
                    	**type**\:   :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom>`
                    
                    .. attribute:: los
                    
                    	Loss of Signal
                    	**type**\:   :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Los>`
                    
                    .. attribute:: oof
                    
                    	Out of Frame
                    	**type**\:   :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof>`
                    
                    .. attribute:: oom
                    
                    	Out of MultiFrame
                    	**type**\:   :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom>`
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\:   :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer>`
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\:   :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer>`
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch
                    	**type**\:   :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim>`
                    
                    .. attribute:: uc
                    
                    	UC alarm
                    	**type**\:   :py:class:`Uc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo, self).__init__()

                        self.yang_name = "otu-alarm-info"
                        self.yang_parent_name = "info"

                        self.ais = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais()
                        self.ais.parent = self
                        self._children_name_map["ais"] = "ais"
                        self._children_yang_names.add("ais")

                        self.bdi = Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi()
                        self.bdi.parent = self
                        self._children_name_map["bdi"] = "bdi"
                        self._children_yang_names.add("bdi")

                        self.biae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae()
                        self.biae.parent = self
                        self._children_name_map["biae"] = "biae"
                        self._children_yang_names.add("biae")

                        self.ec = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec()
                        self.ec.parent = self
                        self._children_name_map["ec"] = "ec"
                        self._children_yang_names.add("ec")

                        self.eoc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc()
                        self.eoc.parent = self
                        self._children_name_map["eoc"] = "eoc"
                        self._children_yang_names.add("eoc")

                        self.fec_mismatch = Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch()
                        self.fec_mismatch.parent = self
                        self._children_name_map["fec_mismatch"] = "fec-mismatch"
                        self._children_yang_names.add("fec-mismatch")

                        self.fecunc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc()
                        self.fecunc.parent = self
                        self._children_name_map["fecunc"] = "fecunc"
                        self._children_yang_names.add("fecunc")

                        self.iae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae()
                        self.iae.parent = self
                        self._children_name_map["iae"] = "iae"
                        self._children_yang_names.add("iae")

                        self.lof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof()
                        self.lof.parent = self
                        self._children_name_map["lof"] = "lof"
                        self._children_yang_names.add("lof")

                        self.lom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom()
                        self.lom.parent = self
                        self._children_name_map["lom"] = "lom"
                        self._children_yang_names.add("lom")

                        self.los = Otu.Controllers.Controller.Info.OtuAlarmInfo.Los()
                        self.los.parent = self
                        self._children_name_map["los"] = "los"
                        self._children_yang_names.add("los")

                        self.oof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof()
                        self.oof.parent = self
                        self._children_name_map["oof"] = "oof"
                        self._children_yang_names.add("oof")

                        self.oom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom()
                        self.oom.parent = self
                        self._children_name_map["oom"] = "oom"
                        self._children_yang_names.add("oom")

                        self.sd_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer()
                        self.sd_ber.parent = self
                        self._children_name_map["sd_ber"] = "sd-ber"
                        self._children_yang_names.add("sd-ber")

                        self.sf_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer()
                        self.sf_ber.parent = self
                        self._children_name_map["sf_ber"] = "sf-ber"
                        self._children_yang_names.add("sf-ber")

                        self.tim = Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim()
                        self.tim.parent = self
                        self._children_name_map["tim"] = "tim"
                        self._children_yang_names.add("tim")

                        self.uc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc()
                        self.uc.parent = self
                        self._children_name_map["uc"] = "uc"
                        self._children_yang_names.add("uc")


                    class Los(Entity):
                        """
                        Loss of Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, self).__init__()

                            self.yang_name = "los"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "los" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Lof(Entity):
                        """
                        Loss of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, self).__init__()

                            self.yang_name = "lof"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lof" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Lom(Entity):
                        """
                        Loss of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, self).__init__()

                            self.yang_name = "lom"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "lom" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Oof(Entity):
                        """
                        Out of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, self).__init__()

                            self.yang_name = "oof"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oof" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Oom(Entity):
                        """
                        Out of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, self).__init__()

                            self.yang_name = "oom"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oom" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Ais(Entity):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, self).__init__()

                            self.yang_name = "ais"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ais" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Iae(Entity):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, self).__init__()

                            self.yang_name = "iae"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "iae" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Biae(Entity):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, self).__init__()

                            self.yang_name = "biae"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "biae" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Bdi(Entity):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, self).__init__()

                            self.yang_name = "bdi"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bdi" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Tim(Entity):
                        """
                        Trace Identifier Mismatch
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, self).__init__()

                            self.yang_name = "tim"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tim" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Eoc(Entity):
                        """
                        GCC End of Channel
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, self).__init__()

                            self.yang_name = "eoc"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "eoc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class FecMismatch(Entity):
                        """
                        FEC mismatch alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, self).__init__()

                            self.yang_name = "fec-mismatch"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fec-mismatch" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class SfBer(Entity):
                        """
                        SF BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, self).__init__()

                            self.yang_name = "sf-ber"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sf-ber" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class SdBer(Entity):
                        """
                        SD BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, self).__init__()

                            self.yang_name = "sd-ber"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sd-ber" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Ec(Entity):
                        """
                        EC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, self).__init__()

                            self.yang_name = "ec"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Uc(Entity):
                        """
                        UC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, self).__init__()

                            self.yang_name = "uc"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "uc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix


                    class Fecunc(Entity):
                        """
                        FEC UnCorrected Word
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, self).__init__()

                            self.yang_name = "fecunc"
                            self.yang_parent_name = "otu-alarm-info"

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("counter",
                                            "is_asserted",
                                            "is_detected",
                                            "reporting_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fecunc" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.counter.is_set or self.counter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter.get_name_leafdata())
                            if (self.is_asserted.is_set or self.is_asserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_asserted.get_name_leafdata())
                            if (self.is_detected.is_set or self.is_detected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_detected.get_name_leafdata())
                            if (self.reporting_enabled.is_set or self.reporting_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reporting_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "counter"):
                                self.counter = value
                                self.counter.value_namespace = name_space
                                self.counter.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-asserted"):
                                self.is_asserted = value
                                self.is_asserted.value_namespace = name_space
                                self.is_asserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-detected"):
                                self.is_detected = value
                                self.is_detected.value_namespace = name_space
                                self.is_detected.value_namespace_prefix = name_space_prefix
                            if(value_path == "reporting-enabled"):
                                self.reporting_enabled = value
                                self.reporting_enabled.value_namespace = name_space
                                self.reporting_enabled.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.ais is not None and self.ais.has_data()) or
                            (self.bdi is not None and self.bdi.has_data()) or
                            (self.biae is not None and self.biae.has_data()) or
                            (self.ec is not None and self.ec.has_data()) or
                            (self.eoc is not None and self.eoc.has_data()) or
                            (self.fec_mismatch is not None and self.fec_mismatch.has_data()) or
                            (self.fecunc is not None and self.fecunc.has_data()) or
                            (self.iae is not None and self.iae.has_data()) or
                            (self.lof is not None and self.lof.has_data()) or
                            (self.lom is not None and self.lom.has_data()) or
                            (self.los is not None and self.los.has_data()) or
                            (self.oof is not None and self.oof.has_data()) or
                            (self.oom is not None and self.oom.has_data()) or
                            (self.sd_ber is not None and self.sd_ber.has_data()) or
                            (self.sf_ber is not None and self.sf_ber.has_data()) or
                            (self.tim is not None and self.tim.has_data()) or
                            (self.uc is not None and self.uc.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.ais is not None and self.ais.has_operation()) or
                            (self.bdi is not None and self.bdi.has_operation()) or
                            (self.biae is not None and self.biae.has_operation()) or
                            (self.ec is not None and self.ec.has_operation()) or
                            (self.eoc is not None and self.eoc.has_operation()) or
                            (self.fec_mismatch is not None and self.fec_mismatch.has_operation()) or
                            (self.fecunc is not None and self.fecunc.has_operation()) or
                            (self.iae is not None and self.iae.has_operation()) or
                            (self.lof is not None and self.lof.has_operation()) or
                            (self.lom is not None and self.lom.has_operation()) or
                            (self.los is not None and self.los.has_operation()) or
                            (self.oof is not None and self.oof.has_operation()) or
                            (self.oom is not None and self.oom.has_operation()) or
                            (self.sd_ber is not None and self.sd_ber.has_operation()) or
                            (self.sf_ber is not None and self.sf_ber.has_operation()) or
                            (self.tim is not None and self.tim.has_operation()) or
                            (self.uc is not None and self.uc.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "otu-alarm-info" + path_buffer

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

                        if (child_yang_name == "ais"):
                            if (self.ais is None):
                                self.ais = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais()
                                self.ais.parent = self
                                self._children_name_map["ais"] = "ais"
                            return self.ais

                        if (child_yang_name == "bdi"):
                            if (self.bdi is None):
                                self.bdi = Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi()
                                self.bdi.parent = self
                                self._children_name_map["bdi"] = "bdi"
                            return self.bdi

                        if (child_yang_name == "biae"):
                            if (self.biae is None):
                                self.biae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae()
                                self.biae.parent = self
                                self._children_name_map["biae"] = "biae"
                            return self.biae

                        if (child_yang_name == "ec"):
                            if (self.ec is None):
                                self.ec = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec()
                                self.ec.parent = self
                                self._children_name_map["ec"] = "ec"
                            return self.ec

                        if (child_yang_name == "eoc"):
                            if (self.eoc is None):
                                self.eoc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc()
                                self.eoc.parent = self
                                self._children_name_map["eoc"] = "eoc"
                            return self.eoc

                        if (child_yang_name == "fec-mismatch"):
                            if (self.fec_mismatch is None):
                                self.fec_mismatch = Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch()
                                self.fec_mismatch.parent = self
                                self._children_name_map["fec_mismatch"] = "fec-mismatch"
                            return self.fec_mismatch

                        if (child_yang_name == "fecunc"):
                            if (self.fecunc is None):
                                self.fecunc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc()
                                self.fecunc.parent = self
                                self._children_name_map["fecunc"] = "fecunc"
                            return self.fecunc

                        if (child_yang_name == "iae"):
                            if (self.iae is None):
                                self.iae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae()
                                self.iae.parent = self
                                self._children_name_map["iae"] = "iae"
                            return self.iae

                        if (child_yang_name == "lof"):
                            if (self.lof is None):
                                self.lof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof()
                                self.lof.parent = self
                                self._children_name_map["lof"] = "lof"
                            return self.lof

                        if (child_yang_name == "lom"):
                            if (self.lom is None):
                                self.lom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom()
                                self.lom.parent = self
                                self._children_name_map["lom"] = "lom"
                            return self.lom

                        if (child_yang_name == "los"):
                            if (self.los is None):
                                self.los = Otu.Controllers.Controller.Info.OtuAlarmInfo.Los()
                                self.los.parent = self
                                self._children_name_map["los"] = "los"
                            return self.los

                        if (child_yang_name == "oof"):
                            if (self.oof is None):
                                self.oof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof()
                                self.oof.parent = self
                                self._children_name_map["oof"] = "oof"
                            return self.oof

                        if (child_yang_name == "oom"):
                            if (self.oom is None):
                                self.oom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom()
                                self.oom.parent = self
                                self._children_name_map["oom"] = "oom"
                            return self.oom

                        if (child_yang_name == "sd-ber"):
                            if (self.sd_ber is None):
                                self.sd_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer()
                                self.sd_ber.parent = self
                                self._children_name_map["sd_ber"] = "sd-ber"
                            return self.sd_ber

                        if (child_yang_name == "sf-ber"):
                            if (self.sf_ber is None):
                                self.sf_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer()
                                self.sf_ber.parent = self
                                self._children_name_map["sf_ber"] = "sf-ber"
                            return self.sf_ber

                        if (child_yang_name == "tim"):
                            if (self.tim is None):
                                self.tim = Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim()
                                self.tim.parent = self
                                self._children_name_map["tim"] = "tim"
                            return self.tim

                        if (child_yang_name == "uc"):
                            if (self.uc is None):
                                self.uc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc()
                                self.uc.parent = self
                                self._children_name_map["uc"] = "uc"
                            return self.uc

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ais" or name == "bdi" or name == "biae" or name == "ec" or name == "eoc" or name == "fec-mismatch" or name == "fecunc" or name == "iae" or name == "lof" or name == "lom" or name == "los" or name == "oof" or name == "oom" or name == "sd-ber" or name == "sf-ber" or name == "tim" or name == "uc"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Proactive(Entity):
                    """
                    Proactive Protection
                    
                    .. attribute:: config_sec_state
                    
                    	Sec State
                    	**type**\:   :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    .. attribute:: inherit_sec_state
                    
                    	Secondary Admin State
                    	**type**\:   :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:   :py:class:`OtuPpIntfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpIntfState>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:   :py:class:`OtuPpFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpFsmState>`
                    
                    .. attribute:: proactive_status
                    
                    	Proactive Status
                    	**type**\:  bool
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_coeff
                    
                    	Trigger threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_power
                    
                    	Trigger threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trigger_window
                    
                    	Trigger Integration window
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"

                        self.config_sec_state = YLeaf(YType.enumeration, "config-sec-state")

                        self.inherit_sec_state = YLeaf(YType.enumeration, "inherit-sec-state")

                        self.proactive_fsm_if_state = YLeaf(YType.enumeration, "proactive-fsm-if-state")

                        self.proactive_fsm_state = YLeaf(YType.enumeration, "proactive-fsm-state")

                        self.proactive_status = YLeaf(YType.boolean, "proactive-status")

                        self.revert_window = YLeaf(YType.uint32, "revert-window")

                        self.rvrt_thresh_coeff = YLeaf(YType.uint8, "rvrt-thresh-coeff")

                        self.rvrt_thresh_power = YLeaf(YType.uint8, "rvrt-thresh-power")

                        self.trig_thresh_coeff = YLeaf(YType.uint8, "trig-thresh-coeff")

                        self.trig_thresh_power = YLeaf(YType.uint8, "trig-thresh-power")

                        self.trigger_window = YLeaf(YType.uint32, "trigger-window")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("config_sec_state",
                                        "inherit_sec_state",
                                        "proactive_fsm_if_state",
                                        "proactive_fsm_state",
                                        "proactive_status",
                                        "revert_window",
                                        "rvrt_thresh_coeff",
                                        "rvrt_thresh_power",
                                        "trig_thresh_coeff",
                                        "trig_thresh_power",
                                        "trigger_window") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Otu.Controllers.Controller.Info.Proactive, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.Proactive, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.config_sec_state.is_set or
                            self.inherit_sec_state.is_set or
                            self.proactive_fsm_if_state.is_set or
                            self.proactive_fsm_state.is_set or
                            self.proactive_status.is_set or
                            self.revert_window.is_set or
                            self.rvrt_thresh_coeff.is_set or
                            self.rvrt_thresh_power.is_set or
                            self.trig_thresh_coeff.is_set or
                            self.trig_thresh_power.is_set or
                            self.trigger_window.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.config_sec_state.yfilter != YFilter.not_set or
                            self.inherit_sec_state.yfilter != YFilter.not_set or
                            self.proactive_fsm_if_state.yfilter != YFilter.not_set or
                            self.proactive_fsm_state.yfilter != YFilter.not_set or
                            self.proactive_status.yfilter != YFilter.not_set or
                            self.revert_window.yfilter != YFilter.not_set or
                            self.rvrt_thresh_coeff.yfilter != YFilter.not_set or
                            self.rvrt_thresh_power.yfilter != YFilter.not_set or
                            self.trig_thresh_coeff.yfilter != YFilter.not_set or
                            self.trig_thresh_power.yfilter != YFilter.not_set or
                            self.trigger_window.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "proactive" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.config_sec_state.is_set or self.config_sec_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_sec_state.get_name_leafdata())
                        if (self.inherit_sec_state.is_set or self.inherit_sec_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inherit_sec_state.get_name_leafdata())
                        if (self.proactive_fsm_if_state.is_set or self.proactive_fsm_if_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_fsm_if_state.get_name_leafdata())
                        if (self.proactive_fsm_state.is_set or self.proactive_fsm_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_fsm_state.get_name_leafdata())
                        if (self.proactive_status.is_set or self.proactive_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_status.get_name_leafdata())
                        if (self.revert_window.is_set or self.revert_window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.revert_window.get_name_leafdata())
                        if (self.rvrt_thresh_coeff.is_set or self.rvrt_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_thresh_coeff.get_name_leafdata())
                        if (self.rvrt_thresh_power.is_set or self.rvrt_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_thresh_power.get_name_leafdata())
                        if (self.trig_thresh_coeff.is_set or self.trig_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_thresh_coeff.get_name_leafdata())
                        if (self.trig_thresh_power.is_set or self.trig_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_thresh_power.get_name_leafdata())
                        if (self.trigger_window.is_set or self.trigger_window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trigger_window.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config-sec-state" or name == "inherit-sec-state" or name == "proactive-fsm-if-state" or name == "proactive-fsm-state" or name == "proactive-status" or name == "revert-window" or name == "rvrt-thresh-coeff" or name == "rvrt-thresh-power" or name == "trig-thresh-coeff" or name == "trig-thresh-power" or name == "trigger-window"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "config-sec-state"):
                            self.config_sec_state = value
                            self.config_sec_state.value_namespace = name_space
                            self.config_sec_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "inherit-sec-state"):
                            self.inherit_sec_state = value
                            self.inherit_sec_state.value_namespace = name_space
                            self.inherit_sec_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-fsm-if-state"):
                            self.proactive_fsm_if_state = value
                            self.proactive_fsm_if_state.value_namespace = name_space
                            self.proactive_fsm_if_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-fsm-state"):
                            self.proactive_fsm_state = value
                            self.proactive_fsm_state.value_namespace = name_space
                            self.proactive_fsm_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-status"):
                            self.proactive_status = value
                            self.proactive_status.value_namespace = name_space
                            self.proactive_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "revert-window"):
                            self.revert_window = value
                            self.revert_window.value_namespace = name_space
                            self.revert_window.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-thresh-coeff"):
                            self.rvrt_thresh_coeff = value
                            self.rvrt_thresh_coeff.value_namespace = name_space
                            self.rvrt_thresh_coeff.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-thresh-power"):
                            self.rvrt_thresh_power = value
                            self.rvrt_thresh_power.value_namespace = name_space
                            self.rvrt_thresh_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "trig-thresh-coeff"):
                            self.trig_thresh_coeff = value
                            self.trig_thresh_coeff.value_namespace = name_space
                            self.trig_thresh_coeff.value_namespace_prefix = name_space_prefix
                        if(value_path == "trig-thresh-power"):
                            self.trig_thresh_power = value
                            self.trig_thresh_power.value_namespace = name_space
                            self.trig_thresh_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "trigger-window"):
                            self.trigger_window = value
                            self.trigger_window.value_namespace = name_space
                            self.trigger_window.value_namespace_prefix = name_space_prefix


                class OtuFecSatistics(Entity):
                    """
                    OTU FEC Statistics
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit Error Rate After Forward Error Correction
                    	**type**\:  str
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit Error Rate Before Forward Error Correction
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.OtuFecSatistics, self).__init__()

                        self.yang_name = "otu-fec-satistics"
                        self.yang_parent_name = "info"

                        self.post_fec_ber = YLeaf(YType.str, "post-fec-ber")

                        self.pre_fec_ber = YLeaf(YType.str, "pre-fec-ber")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("post_fec_ber",
                                        "pre_fec_ber") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Otu.Controllers.Controller.Info.OtuFecSatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Otu.Controllers.Controller.Info.OtuFecSatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.post_fec_ber.is_set or
                            self.pre_fec_ber.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.post_fec_ber.yfilter != YFilter.not_set or
                            self.pre_fec_ber.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "otu-fec-satistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.post_fec_ber.is_set or self.post_fec_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.post_fec_ber.get_name_leafdata())
                        if (self.pre_fec_ber.is_set or self.pre_fec_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pre_fec_ber.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "post-fec-ber" or name == "pre-fec-ber"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "post-fec-ber"):
                            self.post_fec_ber = value
                            self.post_fec_ber.value_namespace = name_space
                            self.post_fec_ber.value_namespace_prefix = name_space_prefix
                        if(value_path == "pre-fec-ber"):
                            self.pre_fec_ber = value
                            self.pre_fec_ber.value_namespace = name_space
                            self.pre_fec_ber.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.auto_tti_flag.is_set or
                        self.config_sec_state.is_set or
                        self.derivedstate_mode.is_set or
                        self.ec.is_set or
                        self.ec_value.is_set or
                        self.fec_mode.is_set or
                        self.gcc_mode.is_set or
                        self.gmpls_tti_mode.is_set or
                        self.gmpls_tvm_id.is_set or
                        self.inherit_sec_state.is_set or
                        self.loopback_mode.is_set or
                        self.name.is_set or
                        self.nv_optical_support.is_set or
                        self.performance_monitoring.is_set or
                        self.pre_fec_ber_mantissa.is_set or
                        self.pre_fec_ber_value.is_set or
                        self.pre_fec_mantissa.is_set or
                        self.pre_fec_val.is_set or
                        self.q.is_set or
                        self.q_margin.is_set or
                        self.sd.is_set or
                        self.sf.is_set or
                        self.state.is_set or
                        self.uc.is_set or
                        self.uc_value.is_set or
                        (self.local is not None and self.local.has_data()) or
                        (self.network_srlg is not None and self.network_srlg.has_data()) or
                        (self.otu_alarm_info is not None and self.otu_alarm_info.has_data()) or
                        (self.otu_fec_satistics is not None and self.otu_fec_satistics.has_data()) or
                        (self.proactive is not None and self.proactive.has_data()) or
                        (self.remote is not None and self.remote.has_data()) or
                        (self.tti_mode is not None and self.tti_mode.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.auto_tti_flag.yfilter != YFilter.not_set or
                        self.config_sec_state.yfilter != YFilter.not_set or
                        self.derivedstate_mode.yfilter != YFilter.not_set or
                        self.ec.yfilter != YFilter.not_set or
                        self.ec_value.yfilter != YFilter.not_set or
                        self.fec_mode.yfilter != YFilter.not_set or
                        self.gcc_mode.yfilter != YFilter.not_set or
                        self.gmpls_tti_mode.yfilter != YFilter.not_set or
                        self.gmpls_tvm_id.yfilter != YFilter.not_set or
                        self.inherit_sec_state.yfilter != YFilter.not_set or
                        self.loopback_mode.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.nv_optical_support.yfilter != YFilter.not_set or
                        self.performance_monitoring.yfilter != YFilter.not_set or
                        self.pre_fec_ber_mantissa.yfilter != YFilter.not_set or
                        self.pre_fec_ber_value.yfilter != YFilter.not_set or
                        self.pre_fec_mantissa.yfilter != YFilter.not_set or
                        self.pre_fec_val.yfilter != YFilter.not_set or
                        self.q.yfilter != YFilter.not_set or
                        self.q_margin.yfilter != YFilter.not_set or
                        self.sd.yfilter != YFilter.not_set or
                        self.sf.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.uc.yfilter != YFilter.not_set or
                        self.uc_value.yfilter != YFilter.not_set or
                        (self.local is not None and self.local.has_operation()) or
                        (self.network_srlg is not None and self.network_srlg.has_operation()) or
                        (self.otu_alarm_info is not None and self.otu_alarm_info.has_operation()) or
                        (self.otu_fec_satistics is not None and self.otu_fec_satistics.has_operation()) or
                        (self.proactive is not None and self.proactive.has_operation()) or
                        (self.remote is not None and self.remote.has_operation()) or
                        (self.tti_mode is not None and self.tti_mode.has_operation()))

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
                    if (self.auto_tti_flag.is_set or self.auto_tti_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auto_tti_flag.get_name_leafdata())
                    if (self.config_sec_state.is_set or self.config_sec_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.config_sec_state.get_name_leafdata())
                    if (self.derivedstate_mode.is_set or self.derivedstate_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.derivedstate_mode.get_name_leafdata())
                    if (self.ec.is_set or self.ec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ec.get_name_leafdata())
                    if (self.ec_value.is_set or self.ec_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ec_value.get_name_leafdata())
                    if (self.fec_mode.is_set or self.fec_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fec_mode.get_name_leafdata())
                    if (self.gcc_mode.is_set or self.gcc_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.gcc_mode.get_name_leafdata())
                    if (self.gmpls_tti_mode.is_set or self.gmpls_tti_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.gmpls_tti_mode.get_name_leafdata())
                    if (self.gmpls_tvm_id.is_set or self.gmpls_tvm_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.gmpls_tvm_id.get_name_leafdata())
                    if (self.inherit_sec_state.is_set or self.inherit_sec_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.inherit_sec_state.get_name_leafdata())
                    if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.nv_optical_support.is_set or self.nv_optical_support.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nv_optical_support.get_name_leafdata())
                    if (self.performance_monitoring.is_set or self.performance_monitoring.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.performance_monitoring.get_name_leafdata())
                    if (self.pre_fec_ber_mantissa.is_set or self.pre_fec_ber_mantissa.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pre_fec_ber_mantissa.get_name_leafdata())
                    if (self.pre_fec_ber_value.is_set or self.pre_fec_ber_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pre_fec_ber_value.get_name_leafdata())
                    if (self.pre_fec_mantissa.is_set or self.pre_fec_mantissa.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pre_fec_mantissa.get_name_leafdata())
                    if (self.pre_fec_val.is_set or self.pre_fec_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pre_fec_val.get_name_leafdata())
                    if (self.q.is_set or self.q.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.q.get_name_leafdata())
                    if (self.q_margin.is_set or self.q_margin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.q_margin.get_name_leafdata())
                    if (self.sd.is_set or self.sd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sd.get_name_leafdata())
                    if (self.sf.is_set or self.sf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sf.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.uc.is_set or self.uc.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.uc.get_name_leafdata())
                    if (self.uc_value.is_set or self.uc_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.uc_value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "local"):
                        if (self.local is None):
                            self.local = Otu.Controllers.Controller.Info.Local()
                            self.local.parent = self
                            self._children_name_map["local"] = "local"
                        return self.local

                    if (child_yang_name == "network-srlg"):
                        if (self.network_srlg is None):
                            self.network_srlg = Otu.Controllers.Controller.Info.NetworkSrlg()
                            self.network_srlg.parent = self
                            self._children_name_map["network_srlg"] = "network-srlg"
                        return self.network_srlg

                    if (child_yang_name == "otu-alarm-info"):
                        if (self.otu_alarm_info is None):
                            self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                            self.otu_alarm_info.parent = self
                            self._children_name_map["otu_alarm_info"] = "otu-alarm-info"
                        return self.otu_alarm_info

                    if (child_yang_name == "otu-fec-satistics"):
                        if (self.otu_fec_satistics is None):
                            self.otu_fec_satistics = Otu.Controllers.Controller.Info.OtuFecSatistics()
                            self.otu_fec_satistics.parent = self
                            self._children_name_map["otu_fec_satistics"] = "otu-fec-satistics"
                        return self.otu_fec_satistics

                    if (child_yang_name == "proactive"):
                        if (self.proactive is None):
                            self.proactive = Otu.Controllers.Controller.Info.Proactive()
                            self.proactive.parent = self
                            self._children_name_map["proactive"] = "proactive"
                        return self.proactive

                    if (child_yang_name == "remote"):
                        if (self.remote is None):
                            self.remote = Otu.Controllers.Controller.Info.Remote()
                            self.remote.parent = self
                            self._children_name_map["remote"] = "remote"
                        return self.remote

                    if (child_yang_name == "tti-mode"):
                        if (self.tti_mode is None):
                            self.tti_mode = Otu.Controllers.Controller.Info.TtiMode()
                            self.tti_mode.parent = self
                            self._children_name_map["tti_mode"] = "tti-mode"
                        return self.tti_mode

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "local" or name == "network-srlg" or name == "otu-alarm-info" or name == "otu-fec-satistics" or name == "proactive" or name == "remote" or name == "tti-mode" or name == "auto-tti-flag" or name == "config-sec-state" or name == "derivedstate-mode" or name == "ec" or name == "ec-value" or name == "fec-mode" or name == "gcc-mode" or name == "gmpls-tti-mode" or name == "gmpls-tvm-id" or name == "inherit-sec-state" or name == "loopback-mode" or name == "name" or name == "nv-optical-support" or name == "performance-monitoring" or name == "pre-fec-ber-mantissa" or name == "pre-fec-ber-value" or name == "pre-fec-mantissa" or name == "pre-fec-val" or name == "q" or name == "q-margin" or name == "sd" or name == "sf" or name == "state" or name == "uc" or name == "uc-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "auto-tti-flag"):
                        self.auto_tti_flag = value
                        self.auto_tti_flag.value_namespace = name_space
                        self.auto_tti_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "config-sec-state"):
                        self.config_sec_state = value
                        self.config_sec_state.value_namespace = name_space
                        self.config_sec_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "derivedstate-mode"):
                        self.derivedstate_mode = value
                        self.derivedstate_mode.value_namespace = name_space
                        self.derivedstate_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "ec"):
                        self.ec = value
                        self.ec.value_namespace = name_space
                        self.ec.value_namespace_prefix = name_space_prefix
                    if(value_path == "ec-value"):
                        self.ec_value = value
                        self.ec_value.value_namespace = name_space
                        self.ec_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "fec-mode"):
                        self.fec_mode = value
                        self.fec_mode.value_namespace = name_space
                        self.fec_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "gcc-mode"):
                        self.gcc_mode = value
                        self.gcc_mode.value_namespace = name_space
                        self.gcc_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "gmpls-tti-mode"):
                        self.gmpls_tti_mode = value
                        self.gmpls_tti_mode.value_namespace = name_space
                        self.gmpls_tti_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "gmpls-tvm-id"):
                        self.gmpls_tvm_id = value
                        self.gmpls_tvm_id.value_namespace = name_space
                        self.gmpls_tvm_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "inherit-sec-state"):
                        self.inherit_sec_state = value
                        self.inherit_sec_state.value_namespace = name_space
                        self.inherit_sec_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "loopback-mode"):
                        self.loopback_mode = value
                        self.loopback_mode.value_namespace = name_space
                        self.loopback_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "nv-optical-support"):
                        self.nv_optical_support = value
                        self.nv_optical_support.value_namespace = name_space
                        self.nv_optical_support.value_namespace_prefix = name_space_prefix
                    if(value_path == "performance-monitoring"):
                        self.performance_monitoring = value
                        self.performance_monitoring.value_namespace = name_space
                        self.performance_monitoring.value_namespace_prefix = name_space_prefix
                    if(value_path == "pre-fec-ber-mantissa"):
                        self.pre_fec_ber_mantissa = value
                        self.pre_fec_ber_mantissa.value_namespace = name_space
                        self.pre_fec_ber_mantissa.value_namespace_prefix = name_space_prefix
                    if(value_path == "pre-fec-ber-value"):
                        self.pre_fec_ber_value = value
                        self.pre_fec_ber_value.value_namespace = name_space
                        self.pre_fec_ber_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "pre-fec-mantissa"):
                        self.pre_fec_mantissa = value
                        self.pre_fec_mantissa.value_namespace = name_space
                        self.pre_fec_mantissa.value_namespace_prefix = name_space_prefix
                    if(value_path == "pre-fec-val"):
                        self.pre_fec_val = value
                        self.pre_fec_val.value_namespace = name_space
                        self.pre_fec_val.value_namespace_prefix = name_space_prefix
                    if(value_path == "q"):
                        self.q = value
                        self.q.value_namespace = name_space
                        self.q.value_namespace_prefix = name_space_prefix
                    if(value_path == "q-margin"):
                        self.q_margin = value
                        self.q_margin.value_namespace = name_space
                        self.q_margin.value_namespace_prefix = name_space_prefix
                    if(value_path == "sd"):
                        self.sd = value
                        self.sd.value_namespace = name_space
                        self.sd.value_namespace_prefix = name_space_prefix
                    if(value_path == "sf"):
                        self.sf = value
                        self.sf.value_namespace = name_space
                        self.sf.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "uc"):
                        self.uc = value
                        self.uc.value_namespace = name_space
                        self.uc.value_namespace_prefix = name_space_prefix
                    if(value_path == "uc-value"):
                        self.uc_value = value
                        self.uc_value.value_namespace = name_space
                        self.uc_value.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-controller-otu-oper:otu/controllers/%s" % self.get_segment_path()
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
                        self.info = Otu.Controllers.Controller.Info()
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
                path_buffer = "Cisco-IOS-XR-controller-otu-oper:otu/%s" % self.get_segment_path()
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
                c = Otu.Controllers.Controller()
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
        path_buffer = "Cisco-IOS-XR-controller-otu-oper:otu" + path_buffer

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
                self.controllers = Otu.Controllers()
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
        self._top_entity = Otu()
        return self._top_entity

