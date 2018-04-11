""" Cisco_IOS_XR_controller_otu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package operational data.

This module contains definitions
for the following management objects\:
  otu\: OTU operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class GmplsOtuTtiMode(Enum):
    """
    GmplsOtuTtiMode (Enum Class)

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
    OtuDerState (Enum Class)

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
    OtuG709FecMode (Enum Class)

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
    OtuLoopBackMode (Enum Class)

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
    OtuPerMon (Enum Class)

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
    OtuPpFsmState (Enum Class)

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
    OtuPpIntfState (Enum Class)

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


class OtuPrbsMode(Enum):
    """
    OtuPrbsMode (Enum Class)

    Otu prbs mode

    .. data:: not_applicable = 0

    	OTU PRBS mode not applicable

    .. data:: source = 1

    	Source

    .. data:: sink = 2

    	Sink

    .. data:: source_sink = 3

    	Source Sink

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    source = Enum.YLeaf(1, "source")

    sink = Enum.YLeaf(2, "sink")

    source_sink = Enum.YLeaf(3, "source-sink")


class OtuPrbsPattern(Enum):
    """
    OtuPrbsPattern (Enum Class)

    Otu prbs pattern

    .. data:: not_applicable = 0

    	OTU PRBS pattern not applicable

    .. data:: pn31 = 1

    	PN31

    .. data:: pn23 = 2

    	PN23

    .. data:: pn11 = 4

    	PN11

    .. data:: inverted_pn31 = 8

    	INVERTED PN31

    .. data:: inverted_pn11 = 16

    	INVERTED PN11

    .. data:: pn15 = 32

    	PN15

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    pn31 = Enum.YLeaf(1, "pn31")

    pn23 = Enum.YLeaf(2, "pn23")

    pn11 = Enum.YLeaf(4, "pn11")

    inverted_pn31 = Enum.YLeaf(8, "inverted-pn31")

    inverted_pn11 = Enum.YLeaf(16, "inverted-pn11")

    pn15 = Enum.YLeaf(32, "pn15")


class OtuPrbsStatus(Enum):
    """
    OtuPrbsStatus (Enum Class)

    Otu prbs status

    .. data:: locked = 0

    	Locked

    .. data:: unlocked = 1

    	Unlocked

    .. data:: not_applicable = 2

    	Not Applicable

    """

    locked = Enum.YLeaf(0, "locked")

    unlocked = Enum.YLeaf(1, "unlocked")

    not_applicable = Enum.YLeaf(2, "not-applicable")


class OtuPrbsTest(Enum):
    """
    OtuPrbsTest (Enum Class)

    Otu prbs test

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OtuSecState(Enum):
    """
    OtuSecState (Enum Class)

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
    OtuStateEt (Enum Class)

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
    OtuTtiEt (Enum Class)

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
    	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers>`
    
    

    """

    _prefix = 'controller-otu-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Otu, self).__init__()
        self._top_entity = None

        self.yang_name = "otu"
        self.yang_parent_name = "Cisco-IOS-XR-controller-otu-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("controllers", ("controllers", Otu.Controllers))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.controllers = Otu.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")
        self._segment_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu"


    class Controllers(Entity):
        """
        All OTU Port operational data
        
        .. attribute:: controller
        
        	OTU Port operational data
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller>`
        
        

        """

        _prefix = 'controller-otu-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Otu.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "otu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("controller", ("controller", Otu.Controllers.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Otu.Controllers, [], name, value)


        class Controller(Entity):
            """
            OTU Port operational data
            
            .. attribute:: controller_name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: prbs
            
            	OTU port PRBS operational data
            	**type**\:  :py:class:`Prbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Prbs>`
            
            .. attribute:: info
            
            	OTU port operational data
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info>`
            
            

            """

            _prefix = 'controller-otu-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Otu.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_container_classes = OrderedDict([("prbs", ("prbs", Otu.Controllers.Controller.Prbs)), ("info", ("info", Otu.Controllers.Controller.Info))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('controller_name', YLeaf(YType.str, 'controller-name')),
                ])
                self.controller_name = None

                self.prbs = Otu.Controllers.Controller.Prbs()
                self.prbs.parent = self
                self._children_name_map["prbs"] = "prbs"
                self._children_yang_names.add("prbs")

                self.info = Otu.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")
                self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu/controllers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Otu.Controllers.Controller, ['controller_name'], name, value)


            class Prbs(Entity):
                """
                OTU port PRBS operational data
                
                .. attribute:: otu_prbs_test
                
                	otu prbs test
                	**type**\:  :py:class:`OtuPrbsTest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsTest>`
                
                .. attribute:: otu_prbs_mode
                
                	otu prbs mode
                	**type**\:  :py:class:`OtuPrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsMode>`
                
                .. attribute:: otu_prbs_pattern
                
                	otu prbs pattern
                	**type**\:  :py:class:`OtuPrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsPattern>`
                
                .. attribute:: otu_prbs_status
                
                	otu prbs status
                	**type**\:  :py:class:`OtuPrbsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsStatus>`
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Otu.Controllers.Controller.Prbs, self).__init__()

                    self.yang_name = "prbs"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('otu_prbs_test', YLeaf(YType.enumeration, 'otu-prbs-test')),
                        ('otu_prbs_mode', YLeaf(YType.enumeration, 'otu-prbs-mode')),
                        ('otu_prbs_pattern', YLeaf(YType.enumeration, 'otu-prbs-pattern')),
                        ('otu_prbs_status', YLeaf(YType.enumeration, 'otu-prbs-status')),
                    ])
                    self.otu_prbs_test = None
                    self.otu_prbs_mode = None
                    self.otu_prbs_pattern = None
                    self.otu_prbs_status = None
                    self._segment_path = lambda: "prbs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Otu.Controllers.Controller.Prbs, ['otu_prbs_test', 'otu_prbs_mode', 'otu_prbs_pattern', 'otu_prbs_status'], name, value)


            class Info(Entity):
                """
                OTU port operational data
                
                .. attribute:: local
                
                	TTI
                	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Local>`
                
                .. attribute:: remote
                
                	Remote
                	**type**\:  :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Remote>`
                
                .. attribute:: tti_mode
                
                	OTU TTI
                	**type**\:  :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode>`
                
                .. attribute:: network_srlg
                
                	Network Shared Risk Link Group information
                	**type**\:  :py:class:`NetworkSrlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg>`
                
                .. attribute:: otu_alarm_info
                
                	OTU layer alarm Information
                	**type**\:  :py:class:`OtuAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo>`
                
                .. attribute:: proactive
                
                	Proactive Protection
                	**type**\:  :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Proactive>`
                
                .. attribute:: otu_fec_satistics
                
                	OTU FEC Statistics
                	**type**\:  :py:class:`OtuFecSatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuFecSatistics>`
                
                .. attribute:: state
                
                	Admin State
                	**type**\:  :py:class:`OtuStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuStateEt>`
                
                .. attribute:: name
                
                	Interface Name
                	**type**\: str
                
                .. attribute:: sf
                
                	SF in the form of 1.0E \- <SF>
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: sd
                
                	SD in the form of 1.0E \- <SD>
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\:  :py:class:`OtuLoopBackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuLoopBackMode>`
                
                .. attribute:: fec_mode
                
                	FEC
                	**type**\:  :py:class:`OtuG709FecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuG709FecMode>`
                
                .. attribute:: derivedstate_mode
                
                	Derived State
                	**type**\:  :py:class:`OtuDerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuDerState>`
                
                .. attribute:: inherit_sec_state
                
                	Sec State
                	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                .. attribute:: config_sec_state
                
                	Sec State
                	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                .. attribute:: gcc_mode
                
                	OTU GCC
                	**type**\: bool
                
                .. attribute:: q
                
                	q value calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: q_margin
                
                	q margin calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\:  :py:class:`OtuPerMon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPerMon>`
                
                .. attribute:: ec
                
                	Average bit errors corrected
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: uc
                
                	Uncorrected word count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pre_fec_val
                
                	Pre FEC BER Value in form 0.00
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: pre_fec_mantissa
                
                	Pre FEC BER Mantissa in form E\-<mantisaa>
                	**type**\: int
                
                	**range:** \-128..127
                
                .. attribute:: ec_value
                
                	EC value present
                	**type**\: bool
                
                .. attribute:: uc_value
                
                	Uc value present
                	**type**\: bool
                
                .. attribute:: pre_fec_ber_value
                
                	Pre fec val present 
                	**type**\: bool
                
                .. attribute:: pre_fec_ber_mantissa
                
                	Pre fec val mantissa
                	**type**\: bool
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\: bool
                
                .. attribute:: gmpls_tti_mode
                
                	GMPLS TTI MODE
                	**type**\:  :py:class:`GmplsOtuTtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.GmplsOtuTtiMode>`
                
                .. attribute:: gmpls_tvm_id
                
                	GMPLS TCM ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: auto_tti_flag
                
                	Auto tti flag
                	**type**\: bool
                
                .. attribute:: description
                
                	Controller description string
                	**type**\: str
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Otu.Controllers.Controller.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("local", ("local", Otu.Controllers.Controller.Info.Local)), ("remote", ("remote", Otu.Controllers.Controller.Info.Remote)), ("tti-mode", ("tti_mode", Otu.Controllers.Controller.Info.TtiMode)), ("network-srlg", ("network_srlg", Otu.Controllers.Controller.Info.NetworkSrlg)), ("otu-alarm-info", ("otu_alarm_info", Otu.Controllers.Controller.Info.OtuAlarmInfo)), ("proactive", ("proactive", Otu.Controllers.Controller.Info.Proactive)), ("otu-fec-satistics", ("otu_fec_satistics", Otu.Controllers.Controller.Info.OtuFecSatistics))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('state', YLeaf(YType.enumeration, 'state')),
                        ('name', YLeaf(YType.str, 'name')),
                        ('sf', YLeaf(YType.uint8, 'sf')),
                        ('sd', YLeaf(YType.uint8, 'sd')),
                        ('loopback_mode', YLeaf(YType.enumeration, 'loopback-mode')),
                        ('fec_mode', YLeaf(YType.enumeration, 'fec-mode')),
                        ('derivedstate_mode', YLeaf(YType.enumeration, 'derivedstate-mode')),
                        ('inherit_sec_state', YLeaf(YType.enumeration, 'inherit-sec-state')),
                        ('config_sec_state', YLeaf(YType.enumeration, 'config-sec-state')),
                        ('gcc_mode', YLeaf(YType.boolean, 'gcc-mode')),
                        ('q', YLeaf(YType.uint64, 'q')),
                        ('q_margin', YLeaf(YType.uint64, 'q-margin')),
                        ('performance_monitoring', YLeaf(YType.enumeration, 'performance-monitoring')),
                        ('ec', YLeaf(YType.uint64, 'ec')),
                        ('uc', YLeaf(YType.uint64, 'uc')),
                        ('pre_fec_val', YLeaf(YType.int32, 'pre-fec-val')),
                        ('pre_fec_mantissa', YLeaf(YType.int8, 'pre-fec-mantissa')),
                        ('ec_value', YLeaf(YType.boolean, 'ec-value')),
                        ('uc_value', YLeaf(YType.boolean, 'uc-value')),
                        ('pre_fec_ber_value', YLeaf(YType.boolean, 'pre-fec-ber-value')),
                        ('pre_fec_ber_mantissa', YLeaf(YType.boolean, 'pre-fec-ber-mantissa')),
                        ('nv_optical_support', YLeaf(YType.boolean, 'nv-optical-support')),
                        ('gmpls_tti_mode', YLeaf(YType.enumeration, 'gmpls-tti-mode')),
                        ('gmpls_tvm_id', YLeaf(YType.uint8, 'gmpls-tvm-id')),
                        ('auto_tti_flag', YLeaf(YType.boolean, 'auto-tti-flag')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.state = None
                    self.name = None
                    self.sf = None
                    self.sd = None
                    self.loopback_mode = None
                    self.fec_mode = None
                    self.derivedstate_mode = None
                    self.inherit_sec_state = None
                    self.config_sec_state = None
                    self.gcc_mode = None
                    self.q = None
                    self.q_margin = None
                    self.performance_monitoring = None
                    self.ec = None
                    self.uc = None
                    self.pre_fec_val = None
                    self.pre_fec_mantissa = None
                    self.ec_value = None
                    self.uc_value = None
                    self.pre_fec_ber_value = None
                    self.pre_fec_ber_mantissa = None
                    self.nv_optical_support = None
                    self.gmpls_tti_mode = None
                    self.gmpls_tvm_id = None
                    self.auto_tti_flag = None
                    self.description = None

                    self.local = Otu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self._children_name_map["local"] = "local"
                    self._children_yang_names.add("local")

                    self.remote = Otu.Controllers.Controller.Info.Remote()
                    self.remote.parent = self
                    self._children_name_map["remote"] = "remote"
                    self._children_yang_names.add("remote")

                    self.tti_mode = Otu.Controllers.Controller.Info.TtiMode()
                    self.tti_mode.parent = self
                    self._children_name_map["tti_mode"] = "tti-mode"
                    self._children_yang_names.add("tti-mode")

                    self.network_srlg = Otu.Controllers.Controller.Info.NetworkSrlg()
                    self.network_srlg.parent = self
                    self._children_name_map["network_srlg"] = "network-srlg"
                    self._children_yang_names.add("network-srlg")

                    self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                    self.otu_alarm_info.parent = self
                    self._children_name_map["otu_alarm_info"] = "otu-alarm-info"
                    self._children_yang_names.add("otu-alarm-info")

                    self.proactive = Otu.Controllers.Controller.Info.Proactive()
                    self.proactive.parent = self
                    self._children_name_map["proactive"] = "proactive"
                    self._children_yang_names.add("proactive")

                    self.otu_fec_satistics = Otu.Controllers.Controller.Info.OtuFecSatistics()
                    self.otu_fec_satistics.parent = self
                    self._children_name_map["otu_fec_satistics"] = "otu-fec-satistics"
                    self._children_yang_names.add("otu-fec-satistics")
                    self._segment_path = lambda: "info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Otu.Controllers.Controller.Info, ['state', 'name', 'sf', 'sd', 'loopback_mode', 'fec_mode', 'derivedstate_mode', 'inherit_sec_state', 'config_sec_state', 'gcc_mode', 'q', 'q_margin', 'performance_monitoring', 'ec', 'uc', 'pre_fec_val', 'pre_fec_mantissa', 'ec_value', 'uc_value', 'pre_fec_ber_value', 'pre_fec_ber_mantissa', 'nv_optical_support', 'gmpls_tti_mode', 'gmpls_tvm_id', 'auto_tti_flag', 'description'], name, value)


                class Local(Entity):
                    """
                    TTI
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Local, self).__init__()

                        self.yang_name = "local"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', YLeaf(YType.uint32, 'router-id')),
                            ('if_index', YLeaf(YType.uint32, 'if-index')),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "local"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Local, ['router_id', 'if_index'], name, value)


                class Remote(Entity):
                    """
                    Remote
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', YLeaf(YType.uint32, 'router-id')),
                            ('if_index', YLeaf(YType.uint32, 'if-index')),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "remote"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Remote, ['router_id', 'if_index'], name, value)


                class TtiMode(Entity):
                    """
                    OTU TTI
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\:  :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\:  :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\:  :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI sent
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    .. attribute:: remote_interface
                    
                    	Remote Interface Name
                    	**type**\: str
                    
                    .. attribute:: remote_host_name
                    
                    	Remote host name
                    	**type**\: str
                    
                    .. attribute:: remote_ip_addr
                    
                    	Remote host ip
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.TtiMode, self).__init__()

                        self.yang_name = "tti-mode"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("tx", ("tx", Otu.Controllers.Controller.Info.TtiMode.Tx)), ("exp", ("exp", Otu.Controllers.Controller.Info.TtiMode.Exp)), ("rec", ("rec", Otu.Controllers.Controller.Info.TtiMode.Rec))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('g709tti_sent_mode', YLeaf(YType.enumeration, 'g709tti-sent-mode')),
                            ('g709tti_exp_mode', YLeaf(YType.enumeration, 'g709tti-exp-mode')),
                            ('g709tti_rec_mode', YLeaf(YType.enumeration, 'g709tti-rec-mode')),
                            ('remote_interface', YLeaf(YType.str, 'remote-interface')),
                            ('remote_host_name', YLeaf(YType.str, 'remote-host-name')),
                            ('remote_ip_addr', YLeaf(YType.str, 'remote-ip-addr')),
                        ])
                        self.g709tti_sent_mode = None
                        self.g709tti_exp_mode = None
                        self.g709tti_rec_mode = None
                        self.remote_interface = None
                        self.remote_host_name = None
                        self.remote_ip_addr = None

                        self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self
                        self._children_name_map["tx"] = "tx"
                        self._children_yang_names.add("tx")

                        self.exp = Otu.Controllers.Controller.Info.TtiMode.Exp()
                        self.exp.parent = self
                        self._children_name_map["exp"] = "exp"
                        self._children_yang_names.add("exp")

                        self.rec = Otu.Controllers.Controller.Info.TtiMode.Rec()
                        self.rec.parent = self
                        self._children_name_map["rec"] = "rec"
                        self._children_yang_names.add("rec")
                        self._segment_path = lambda: "tti-mode"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode, ['g709tti_sent_mode', 'g709tti_exp_mode', 'g709tti_rec_mode', 'remote_interface', 'remote_host_name', 'remote_ip_addr'], name, value)


                    class Tx(Entity):
                        """
                        String Sent
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Tx, self).__init__()

                            self.yang_name = "tx"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', YLeaf(YType.str, 'full-tti-ascii-string')),
                                ('sapi', YLeafList(YType.uint8, 'sapi')),
                                ('dapi', YLeafList(YType.uint8, 'dapi')),
                                ('operator_specific', YLeafList(YType.uint8, 'operator-specific')),
                            ])
                            self.full_tti_ascii_string = None
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "tx"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Tx, ['full_tti_ascii_string', 'sapi', 'dapi', 'operator_specific'], name, value)


                    class Exp(Entity):
                        """
                        String Expected
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Exp, self).__init__()

                            self.yang_name = "exp"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', YLeaf(YType.str, 'full-tti-ascii-string')),
                                ('sapi', YLeafList(YType.uint8, 'sapi')),
                                ('dapi', YLeafList(YType.uint8, 'dapi')),
                                ('operator_specific', YLeafList(YType.uint8, 'operator-specific')),
                            ])
                            self.full_tti_ascii_string = None
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "exp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Exp, ['full_tti_ascii_string', 'sapi', 'dapi', 'operator_specific'], name, value)


                    class Rec(Entity):
                        """
                        String Received
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.TtiMode.Rec, self).__init__()

                            self.yang_name = "rec"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', YLeaf(YType.str, 'full-tti-ascii-string')),
                                ('sapi', YLeafList(YType.uint8, 'sapi')),
                                ('dapi', YLeafList(YType.uint8, 'dapi')),
                                ('operator_specific', YLeafList(YType.uint8, 'operator-specific')),
                            ])
                            self.full_tti_ascii_string = None
                            self.sapi = []
                            self.dapi = []
                            self.operator_specific = []
                            self._segment_path = lambda: "rec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Rec, ['full_tti_ascii_string', 'sapi', 'dapi', 'operator_specific'], name, value)


                class NetworkSrlg(Entity):
                    """
                    Network Shared Risk Link Group information
                    
                    .. attribute:: srlg_info
                    
                    	Array of Network Shared Risk Link Group information
                    	**type**\: list of  		 :py:class:`SrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.NetworkSrlg, self).__init__()

                        self.yang_name = "network-srlg"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("srlg-info", ("srlg_info", Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo))])
                        self._leafs = OrderedDict()

                        self.srlg_info = YList(self)
                        self._segment_path = lambda: "network-srlg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.NetworkSrlg, [], name, value)


                    class SrlgInfo(Entity):
                        """
                        Array of Network Shared Risk Link Group
                        information
                        
                        .. attribute:: set_id
                        
                        	Array to maintain set id number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srlg
                        
                        	Shared Risk Link Group information expressed in integer format
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, self).__init__()

                            self.yang_name = "srlg-info"
                            self.yang_parent_name = "network-srlg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_id', YLeaf(YType.uint32, 'set-id')),
                                ('srlg', YLeafList(YType.uint32, 'srlg')),
                            ])
                            self.set_id = None
                            self.srlg = []
                            self._segment_path = lambda: "srlg-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, ['set_id', 'srlg'], name, value)


                class OtuAlarmInfo(Entity):
                    """
                    OTU layer alarm Information
                    
                    .. attribute:: los
                    
                    	Loss of Signal
                    	**type**\:  :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Los>`
                    
                    .. attribute:: lof
                    
                    	Loss of Frame
                    	**type**\:  :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof>`
                    
                    .. attribute:: lom
                    
                    	Loss of MultiFrame
                    	**type**\:  :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom>`
                    
                    .. attribute:: oof
                    
                    	Out of Frame
                    	**type**\:  :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof>`
                    
                    .. attribute:: oom
                    
                    	Out of MultiFrame
                    	**type**\:  :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom>`
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais>`
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\:  :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae>`
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae>`
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\:  :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi>`
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch
                    	**type**\:  :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim>`
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\:  :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc>`
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:  :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch>`
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\:  :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer>`
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\:  :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer>`
                    
                    .. attribute:: ec
                    
                    	EC alarm
                    	**type**\:  :py:class:`Ec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec>`
                    
                    .. attribute:: uc
                    
                    	UC alarm
                    	**type**\:  :py:class:`Uc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc>`
                    
                    .. attribute:: fecunc
                    
                    	FEC UnCorrected Word
                    	**type**\:  :py:class:`Fecunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.OtuAlarmInfo, self).__init__()

                        self.yang_name = "otu-alarm-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("los", ("los", Otu.Controllers.Controller.Info.OtuAlarmInfo.Los)), ("lof", ("lof", Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof)), ("lom", ("lom", Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom)), ("oof", ("oof", Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof)), ("oom", ("oom", Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom)), ("ais", ("ais", Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais)), ("iae", ("iae", Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae)), ("biae", ("biae", Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae)), ("bdi", ("bdi", Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi)), ("tim", ("tim", Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim)), ("eoc", ("eoc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc)), ("fec-mismatch", ("fec_mismatch", Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch)), ("sf-ber", ("sf_ber", Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer)), ("sd-ber", ("sd_ber", Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer)), ("ec", ("ec", Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec)), ("uc", ("uc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc)), ("fecunc", ("fecunc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.los = Otu.Controllers.Controller.Info.OtuAlarmInfo.Los()
                        self.los.parent = self
                        self._children_name_map["los"] = "los"
                        self._children_yang_names.add("los")

                        self.lof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof()
                        self.lof.parent = self
                        self._children_name_map["lof"] = "lof"
                        self._children_yang_names.add("lof")

                        self.lom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom()
                        self.lom.parent = self
                        self._children_name_map["lom"] = "lom"
                        self._children_yang_names.add("lom")

                        self.oof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof()
                        self.oof.parent = self
                        self._children_name_map["oof"] = "oof"
                        self._children_yang_names.add("oof")

                        self.oom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom()
                        self.oom.parent = self
                        self._children_name_map["oom"] = "oom"
                        self._children_yang_names.add("oom")

                        self.ais = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais()
                        self.ais.parent = self
                        self._children_name_map["ais"] = "ais"
                        self._children_yang_names.add("ais")

                        self.iae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae()
                        self.iae.parent = self
                        self._children_name_map["iae"] = "iae"
                        self._children_yang_names.add("iae")

                        self.biae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae()
                        self.biae.parent = self
                        self._children_name_map["biae"] = "biae"
                        self._children_yang_names.add("biae")

                        self.bdi = Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi()
                        self.bdi.parent = self
                        self._children_name_map["bdi"] = "bdi"
                        self._children_yang_names.add("bdi")

                        self.tim = Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim()
                        self.tim.parent = self
                        self._children_name_map["tim"] = "tim"
                        self._children_yang_names.add("tim")

                        self.eoc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc()
                        self.eoc.parent = self
                        self._children_name_map["eoc"] = "eoc"
                        self._children_yang_names.add("eoc")

                        self.fec_mismatch = Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch()
                        self.fec_mismatch.parent = self
                        self._children_name_map["fec_mismatch"] = "fec-mismatch"
                        self._children_yang_names.add("fec-mismatch")

                        self.sf_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer()
                        self.sf_ber.parent = self
                        self._children_name_map["sf_ber"] = "sf-ber"
                        self._children_yang_names.add("sf-ber")

                        self.sd_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer()
                        self.sd_ber.parent = self
                        self._children_name_map["sd_ber"] = "sd-ber"
                        self._children_yang_names.add("sd-ber")

                        self.ec = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec()
                        self.ec.parent = self
                        self._children_name_map["ec"] = "ec"
                        self._children_yang_names.add("ec")

                        self.uc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc()
                        self.uc.parent = self
                        self._children_name_map["uc"] = "uc"
                        self._children_yang_names.add("uc")

                        self.fecunc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc()
                        self.fecunc.parent = self
                        self._children_name_map["fecunc"] = "fecunc"
                        self._children_yang_names.add("fecunc")
                        self._segment_path = lambda: "otu-alarm-info"


                    class Los(Entity):
                        """
                        Loss of Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, self).__init__()

                            self.yang_name = "los"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "los"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Lof(Entity):
                        """
                        Loss of Frame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, self).__init__()

                            self.yang_name = "lof"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "lof"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Lom(Entity):
                        """
                        Loss of MultiFrame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, self).__init__()

                            self.yang_name = "lom"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "lom"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Oof(Entity):
                        """
                        Out of Frame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, self).__init__()

                            self.yang_name = "oof"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "oof"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Oom(Entity):
                        """
                        Out of MultiFrame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, self).__init__()

                            self.yang_name = "oom"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "oom"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Ais(Entity):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, self).__init__()

                            self.yang_name = "ais"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ais"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Iae(Entity):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, self).__init__()

                            self.yang_name = "iae"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "iae"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Biae(Entity):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, self).__init__()

                            self.yang_name = "biae"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "biae"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Bdi(Entity):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, self).__init__()

                            self.yang_name = "bdi"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "bdi"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Tim(Entity):
                        """
                        Trace Identifier Mismatch
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, self).__init__()

                            self.yang_name = "tim"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tim"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Eoc(Entity):
                        """
                        GCC End of Channel
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, self).__init__()

                            self.yang_name = "eoc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "eoc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class FecMismatch(Entity):
                        """
                        FEC mismatch alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, self).__init__()

                            self.yang_name = "fec-mismatch"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "fec-mismatch"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class SfBer(Entity):
                        """
                        SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, self).__init__()

                            self.yang_name = "sf-ber"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sf-ber"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class SdBer(Entity):
                        """
                        SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, self).__init__()

                            self.yang_name = "sd-ber"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sd-ber"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Ec(Entity):
                        """
                        EC alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, self).__init__()

                            self.yang_name = "ec"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Uc(Entity):
                        """
                        UC alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, self).__init__()

                            self.yang_name = "uc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "uc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class Fecunc(Entity):
                        """
                        FEC UnCorrected Word
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, self).__init__()

                            self.yang_name = "fecunc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', YLeaf(YType.boolean, 'reporting-enabled')),
                                ('is_detected', YLeaf(YType.boolean, 'is-detected')),
                                ('is_asserted', YLeaf(YType.boolean, 'is-asserted')),
                                ('counter', YLeaf(YType.uint64, 'counter')),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "fecunc"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                class Proactive(Entity):
                    """
                    Proactive Protection
                    
                    .. attribute:: proactive_status
                    
                    	Proactive Status
                    	**type**\: bool
                    
                    .. attribute:: inherit_sec_state
                    
                    	Secondary Admin State
                    	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    .. attribute:: config_sec_state
                    
                    	Sec State
                    	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:  :py:class:`OtuPpFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpFsmState>`
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:  :py:class:`OtuPpIntfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpIntfState>`
                    
                    .. attribute:: trig_thresh_coeff
                    
                    	Trigger threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_power
                    
                    	Trigger threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trigger_window
                    
                    	Trigger Integration window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('proactive_status', YLeaf(YType.boolean, 'proactive-status')),
                            ('inherit_sec_state', YLeaf(YType.enumeration, 'inherit-sec-state')),
                            ('config_sec_state', YLeaf(YType.enumeration, 'config-sec-state')),
                            ('proactive_fsm_state', YLeaf(YType.enumeration, 'proactive-fsm-state')),
                            ('proactive_fsm_if_state', YLeaf(YType.enumeration, 'proactive-fsm-if-state')),
                            ('trig_thresh_coeff', YLeaf(YType.uint8, 'trig-thresh-coeff')),
                            ('trig_thresh_power', YLeaf(YType.uint8, 'trig-thresh-power')),
                            ('rvrt_thresh_coeff', YLeaf(YType.uint8, 'rvrt-thresh-coeff')),
                            ('rvrt_thresh_power', YLeaf(YType.uint8, 'rvrt-thresh-power')),
                            ('trigger_window', YLeaf(YType.uint32, 'trigger-window')),
                            ('revert_window', YLeaf(YType.uint32, 'revert-window')),
                        ])
                        self.proactive_status = None
                        self.inherit_sec_state = None
                        self.config_sec_state = None
                        self.proactive_fsm_state = None
                        self.proactive_fsm_if_state = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.trigger_window = None
                        self.revert_window = None
                        self._segment_path = lambda: "proactive"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Proactive, ['proactive_status', 'inherit_sec_state', 'config_sec_state', 'proactive_fsm_state', 'proactive_fsm_if_state', 'trig_thresh_coeff', 'trig_thresh_power', 'rvrt_thresh_coeff', 'rvrt_thresh_power', 'trigger_window', 'revert_window'], name, value)


                class OtuFecSatistics(Entity):
                    """
                    OTU FEC Statistics
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit Error Rate After Forward Error Correction
                    	**type**\: str
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit Error Rate Before Forward Error Correction
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Otu.Controllers.Controller.Info.OtuFecSatistics, self).__init__()

                        self.yang_name = "otu-fec-satistics"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('post_fec_ber', YLeaf(YType.str, 'post-fec-ber')),
                            ('pre_fec_ber', YLeaf(YType.str, 'pre-fec-ber')),
                        ])
                        self.post_fec_ber = None
                        self.pre_fec_ber = None
                        self._segment_path = lambda: "otu-fec-satistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.OtuFecSatistics, ['post_fec_ber', 'pre_fec_ber'], name, value)

    def clone_ptr(self):
        self._top_entity = Otu()
        return self._top_entity

