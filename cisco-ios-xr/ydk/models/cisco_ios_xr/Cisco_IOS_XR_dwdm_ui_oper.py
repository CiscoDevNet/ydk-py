""" Cisco_IOS_XR_dwdm_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dwdm\-ui package operational data.

This module contains definitions
for the following management objects\:
  dwdm\: DWDM operational data
  vtxp\: vtxp

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DwdmControllerState(Enum):
    """
    DwdmControllerState

    Dwdm controller state

    .. data:: dwdm_ui_state_up = 0

    	Up

    .. data:: dwdm_ui_state_down = 1

    	Down

    .. data:: dwdm_ui_state_admin_down = 2

    	Administratively Down

    """

    dwdm_ui_state_up = Enum.YLeaf(0, "dwdm-ui-state-up")

    dwdm_ui_state_down = Enum.YLeaf(1, "dwdm-ui-state-down")

    dwdm_ui_state_admin_down = Enum.YLeaf(2, "dwdm-ui-state-admin-down")


class DwdmWaveChannelOwner(Enum):
    """
    DwdmWaveChannelOwner

    Dwdm wave channel owner

    .. data:: default = 0

    	Hardware Default

    .. data:: configuration = 1

    	Configuration

    .. data:: gmpls = 2

    	GMPLS Signaled

    """

    default = Enum.YLeaf(0, "default")

    configuration = Enum.YLeaf(1, "configuration")

    gmpls = Enum.YLeaf(2, "gmpls")


class DwdmtasState(Enum):
    """
    DwdmtasState

    Dwdmtas state

    .. data:: tas_oos = 0

    	Out of Service

    .. data:: tas_is = 1

    	In Service

    .. data:: tas_oos_mt = 2

    	Out of Service Maintenance

    .. data:: tas_is_cfg = 3

    	In Service Config allowed

    """

    tas_oos = Enum.YLeaf(0, "tas-oos")

    tas_is = Enum.YLeaf(1, "tas-is")

    tas_oos_mt = Enum.YLeaf(2, "tas-oos-mt")

    tas_is_cfg = Enum.YLeaf(3, "tas-is-cfg")


class G709apsByte(Enum):
    """
    G709apsByte

    G709aps byte

    .. data:: pp_no_protect = 0

    	No Protection

    .. data:: pp_no_request = 15

    	No Request

    .. data:: pp_regen_degrade = 63

    	Regenerator Degrade

    .. data:: pp_sig_degrade = 175

    	Signal Degrade

    .. data:: pp_remote_main = 239

    	Maintenance Request

    .. data:: pp_aps_unknown = 255

    	Unknown

    """

    pp_no_protect = Enum.YLeaf(0, "pp-no-protect")

    pp_no_request = Enum.YLeaf(15, "pp-no-request")

    pp_regen_degrade = Enum.YLeaf(63, "pp-regen-degrade")

    pp_sig_degrade = Enum.YLeaf(175, "pp-sig-degrade")

    pp_remote_main = Enum.YLeaf(239, "pp-remote-main")

    pp_aps_unknown = Enum.YLeaf(255, "pp-aps-unknown")


class G709efecMode(Enum):
    """
    G709efecMode

    G709efec mode

    .. data:: g975_none = 0

    .. data:: g975_1_i4 = 1

    	G975.1 I.4

    .. data:: g975_1_i7 = 2

    	G975.1 I.7

    """

    g975_none = Enum.YLeaf(0, "g975-none")

    g975_1_i4 = Enum.YLeaf(1, "g975-1-i4")

    g975_1_i7 = Enum.YLeaf(2, "g975-1-i7")


class G709ppfsmMode(Enum):
    """
    G709ppfsmMode

    G709ppfsm mode

    .. data:: pp_disable = 0

    	OFF

    .. data:: pp_default_mode = 1

    	ON (Default Mode)

    .. data:: pp_graceful_mode = 2

    	ON (Graceful Mode)

    """

    pp_disable = Enum.YLeaf(0, "pp-disable")

    pp_default_mode = Enum.YLeaf(1, "pp-default-mode")

    pp_graceful_mode = Enum.YLeaf(2, "pp-graceful-mode")


class G709ppfsmState(Enum):
    """
    G709ppfsmState

    G709ppfsm state

    .. data:: in_active = 0

    	In Active

    .. data:: disabled = 1

    	Disabled

    .. data:: normal_state = 2

    	Normal

    .. data:: local_failing = 3

    	Local Failing

    .. data:: remote_failing = 4

    	Remote Failing

    .. data:: main_t_failing = 5

    	Maintance Failing

    .. data:: regen_failing = 6

    	Regenerator Failing

    .. data:: local_failed = 7

    	Local Failed

    .. data:: remote_failed = 8

    	Remote Failed

    .. data:: main_t_failed = 9

    	Maintance Failed

    .. data:: regen_failed = 10

    	Regenerator Failed

    """

    in_active = Enum.YLeaf(0, "in-active")

    disabled = Enum.YLeaf(1, "disabled")

    normal_state = Enum.YLeaf(2, "normal-state")

    local_failing = Enum.YLeaf(3, "local-failing")

    remote_failing = Enum.YLeaf(4, "remote-failing")

    main_t_failing = Enum.YLeaf(5, "main-t-failing")

    regen_failing = Enum.YLeaf(6, "regen-failing")

    local_failed = Enum.YLeaf(7, "local-failed")

    remote_failed = Enum.YLeaf(8, "remote-failed")

    main_t_failed = Enum.YLeaf(9, "main-t-failed")

    regen_failed = Enum.YLeaf(10, "regen-failed")


class G709ppintfState(Enum):
    """
    G709ppintfState

    G709ppintf state

    .. data:: pp_intf_up = 0

    	Interface is Up

    .. data:: pp_intf_failing = 1

    	Interface is Going Down

    .. data:: pp_intf_down = 2

    	Interface Down

    """

    pp_intf_up = Enum.YLeaf(0, "pp-intf-up")

    pp_intf_failing = Enum.YLeaf(1, "pp-intf-failing")

    pp_intf_down = Enum.YLeaf(2, "pp-intf-down")


class G709prbsInterval(Enum):
    """
    G709prbsInterval

    PRBS test interval information

    .. data:: current_interval = 0

    	Current interval

    .. data:: previous_interval = 1

    	Previous interval

    .. data:: previous_interval2 = 2

    	Previous interval 2

    .. data:: previous_interval3 = 3

    	Previous interval 3

    .. data:: previous_interval4 = 4

    	Previous interval 4

    .. data:: previous_interval5 = 5

    	Previous interval 5

    .. data:: previous_interval6 = 6

    	Previous interval 6

    .. data:: previous_interval7 = 7

    	Previous interval 7

    .. data:: previous_interval8 = 8

    	Previous interval 8

    .. data:: previous_interval9 = 9

    	Previous interval 9

    .. data:: previous_interval10 = 10

    	Previous interval 10

    .. data:: previous_interval11 = 11

    	Previous interval 11

    .. data:: previous_interval12 = 12

    	Previous interval 12

    .. data:: previous_interval13 = 13

    	Previous interval 13

    .. data:: previous_interval14 = 14

    	Previous interval 14

    .. data:: previous_interval15 = 15

    	Previous interval 15

    .. data:: previous_interval16 = 16

    	Previous interval 16

    .. data:: previous_interval17 = 17

    	Previous interval 17

    .. data:: previous_interval18 = 18

    	Previous interval 18

    .. data:: previous_interval19 = 19

    	Previous interval 19

    .. data:: previous_interval20 = 20

    	Previous interval 20

    .. data:: previous_interval21 = 21

    	Previous interval 21

    .. data:: previous_interval22 = 22

    	Previous interval 22

    .. data:: previous_interval23 = 23

    	Previous interval 23

    .. data:: previous_interval24 = 24

    	Previous interval 24

    .. data:: previous_interval25 = 25

    	Previous interval 25

    .. data:: previous_interval26 = 26

    	Previous interval 26

    .. data:: previous_interval27 = 27

    	Previous interval 27

    .. data:: previous_interval28 = 28

    	Previous interval 28

    .. data:: previous_interval29 = 29

    	Previous interval 29

    .. data:: previous_interval30 = 30

    	Previous interval 30

    .. data:: previous_interval31 = 31

    	Previous interval 31

    .. data:: previous_interval32 = 32

    	Previous interval 32

    """

    current_interval = Enum.YLeaf(0, "current-interval")

    previous_interval = Enum.YLeaf(1, "previous-interval")

    previous_interval2 = Enum.YLeaf(2, "previous-interval2")

    previous_interval3 = Enum.YLeaf(3, "previous-interval3")

    previous_interval4 = Enum.YLeaf(4, "previous-interval4")

    previous_interval5 = Enum.YLeaf(5, "previous-interval5")

    previous_interval6 = Enum.YLeaf(6, "previous-interval6")

    previous_interval7 = Enum.YLeaf(7, "previous-interval7")

    previous_interval8 = Enum.YLeaf(8, "previous-interval8")

    previous_interval9 = Enum.YLeaf(9, "previous-interval9")

    previous_interval10 = Enum.YLeaf(10, "previous-interval10")

    previous_interval11 = Enum.YLeaf(11, "previous-interval11")

    previous_interval12 = Enum.YLeaf(12, "previous-interval12")

    previous_interval13 = Enum.YLeaf(13, "previous-interval13")

    previous_interval14 = Enum.YLeaf(14, "previous-interval14")

    previous_interval15 = Enum.YLeaf(15, "previous-interval15")

    previous_interval16 = Enum.YLeaf(16, "previous-interval16")

    previous_interval17 = Enum.YLeaf(17, "previous-interval17")

    previous_interval18 = Enum.YLeaf(18, "previous-interval18")

    previous_interval19 = Enum.YLeaf(19, "previous-interval19")

    previous_interval20 = Enum.YLeaf(20, "previous-interval20")

    previous_interval21 = Enum.YLeaf(21, "previous-interval21")

    previous_interval22 = Enum.YLeaf(22, "previous-interval22")

    previous_interval23 = Enum.YLeaf(23, "previous-interval23")

    previous_interval24 = Enum.YLeaf(24, "previous-interval24")

    previous_interval25 = Enum.YLeaf(25, "previous-interval25")

    previous_interval26 = Enum.YLeaf(26, "previous-interval26")

    previous_interval27 = Enum.YLeaf(27, "previous-interval27")

    previous_interval28 = Enum.YLeaf(28, "previous-interval28")

    previous_interval29 = Enum.YLeaf(29, "previous-interval29")

    previous_interval30 = Enum.YLeaf(30, "previous-interval30")

    previous_interval31 = Enum.YLeaf(31, "previous-interval31")

    previous_interval32 = Enum.YLeaf(32, "previous-interval32")


class G709prbsMode(Enum):
    """
    G709prbsMode

    G709prbs mode

    .. data:: mode_source = 0

    	mode source

    .. data:: mode_sink = 1

    	mode sink

    .. data:: mode_source_sink = 2

    	mode source sink

    .. data:: mode_invalid = 3

    	mode invalid

    """

    mode_source = Enum.YLeaf(0, "mode-source")

    mode_sink = Enum.YLeaf(1, "mode-sink")

    mode_source_sink = Enum.YLeaf(2, "mode-source-sink")

    mode_invalid = Enum.YLeaf(3, "mode-invalid")


class G709prbsPattern(Enum):
    """
    G709prbsPattern

    G709prbs pattern

    .. data:: pattern_none = 0

    	pattern none

    .. data:: pattern_null = 1

    	pattern null

    .. data:: pattern_pn11 = 2

    	pattern pn11

    .. data:: pattern_pn23 = 3

    	pattern pn23

    .. data:: pattern_pn31 = 4

    	pattern pn31

    """

    pattern_none = Enum.YLeaf(0, "pattern-none")

    pattern_null = Enum.YLeaf(1, "pattern-null")

    pattern_pn11 = Enum.YLeaf(2, "pattern-pn11")

    pattern_pn23 = Enum.YLeaf(3, "pattern-pn23")

    pattern_pn31 = Enum.YLeaf(4, "pattern-pn31")



class Dwdm(Entity):
    """
    DWDM operational data
    
    .. attribute:: ports
    
    	All DWDM Port operational data
    	**type**\:   :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports>`
    
    

    """

    _prefix = 'dwdm-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dwdm, self).__init__()
        self._top_entity = None

        self.yang_name = "dwdm"
        self.yang_parent_name = "Cisco-IOS-XR-dwdm-ui-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ports" : ("ports", Dwdm.Ports)}
        self._child_list_classes = {}

        self.ports = Dwdm.Ports()
        self.ports.parent = self
        self._children_name_map["ports"] = "ports"
        self._children_yang_names.add("ports")
        self._segment_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm"


    class Ports(Entity):
        """
        All DWDM Port operational data
        
        .. attribute:: port
        
        	DWDM Port operational data
        	**type**\: list of    :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dwdm.Ports, self).__init__()

            self.yang_name = "ports"
            self.yang_parent_name = "dwdm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"port" : ("port", Dwdm.Ports.Port)}

            self.port = YList(self)
            self._segment_path = lambda: "ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dwdm.Ports, [], name, value)


        class Port(Entity):
            """
            DWDM Port operational data
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: info
            
            	DWDM port operational data
            	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info>`
            
            .. attribute:: optics
            
            	DWDM Port optics operational data
            	**type**\:   :py:class:`Optics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Optics>`
            
            .. attribute:: prbs
            
            	DWDM Port PRBS related data
            	**type**\:   :py:class:`Prbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs>`
            
            

            """

            _prefix = 'dwdm-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dwdm.Ports.Port, self).__init__()

                self.yang_name = "port"
                self.yang_parent_name = "ports"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"info" : ("info", Dwdm.Ports.Port.Info), "optics" : ("optics", Dwdm.Ports.Port.Optics), "prbs" : ("prbs", Dwdm.Ports.Port.Prbs)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.info = Dwdm.Ports.Port.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._children_yang_names.add("info")

                self.optics = Dwdm.Ports.Port.Optics()
                self.optics.parent = self
                self._children_name_map["optics"] = "optics"
                self._children_yang_names.add("optics")

                self.prbs = Dwdm.Ports.Port.Prbs()
                self.prbs.parent = self
                self._children_name_map["prbs"] = "prbs"
                self._children_yang_names.add("prbs")
                self._segment_path = lambda: "port" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm/ports/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dwdm.Ports.Port, ['name'], name, value)


            class Info(Entity):
                """
                DWDM port operational data
                
                .. attribute:: controller_state
                
                	DWDM controller state\: Up, Down or Administratively Down
                	**type**\:   :py:class:`DwdmControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmControllerState>`
                
                .. attribute:: g709_info
                
                	G709 operational information
                	**type**\:   :py:class:`G709Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:   :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.NetworkSrlgInfo>`
                
                .. attribute:: optics_info
                
                	Optics operational information
                	**type**\:   :py:class:`OpticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.OpticsInfo>`
                
                .. attribute:: proactive
                
                	Proactive protection information
                	**type**\:   :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.Proactive>`
                
                .. attribute:: signal_log
                
                	Signal log information
                	**type**\:   :py:class:`SignalLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.SignalLog>`
                
                .. attribute:: slice_state
                
                	DWDM port slice state Up/Down
                	**type**\:  bool
                
                .. attribute:: tdc_info
                
                	TDC operational information
                	**type**\:   :py:class:`TdcInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.TdcInfo>`
                
                .. attribute:: transport_admin_state
                
                	DWDM controller TAS state\: IS, OOS, OOS\-MT or IS\-CFG
                	**type**\:   :py:class:`DwdmtasState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasState>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"g709-info" : ("g709_info", Dwdm.Ports.Port.Info.G709Info), "network-srlg-info" : ("network_srlg_info", Dwdm.Ports.Port.Info.NetworkSrlgInfo), "optics-info" : ("optics_info", Dwdm.Ports.Port.Info.OpticsInfo), "proactive" : ("proactive", Dwdm.Ports.Port.Info.Proactive), "signal-log" : ("signal_log", Dwdm.Ports.Port.Info.SignalLog), "tdc-info" : ("tdc_info", Dwdm.Ports.Port.Info.TdcInfo)}
                    self._child_list_classes = {}

                    self.controller_state = YLeaf(YType.enumeration, "controller-state")

                    self.slice_state = YLeaf(YType.boolean, "slice-state")

                    self.transport_admin_state = YLeaf(YType.enumeration, "transport-admin-state")

                    self.g709_info = Dwdm.Ports.Port.Info.G709Info()
                    self.g709_info.parent = self
                    self._children_name_map["g709_info"] = "g709-info"
                    self._children_yang_names.add("g709-info")

                    self.network_srlg_info = Dwdm.Ports.Port.Info.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"
                    self._children_yang_names.add("network-srlg-info")

                    self.optics_info = Dwdm.Ports.Port.Info.OpticsInfo()
                    self.optics_info.parent = self
                    self._children_name_map["optics_info"] = "optics-info"
                    self._children_yang_names.add("optics-info")

                    self.proactive = Dwdm.Ports.Port.Info.Proactive()
                    self.proactive.parent = self
                    self._children_name_map["proactive"] = "proactive"
                    self._children_yang_names.add("proactive")

                    self.signal_log = Dwdm.Ports.Port.Info.SignalLog()
                    self.signal_log.parent = self
                    self._children_name_map["signal_log"] = "signal-log"
                    self._children_yang_names.add("signal-log")

                    self.tdc_info = Dwdm.Ports.Port.Info.TdcInfo()
                    self.tdc_info.parent = self
                    self._children_name_map["tdc_info"] = "tdc-info"
                    self._children_yang_names.add("tdc-info")
                    self._segment_path = lambda: "info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dwdm.Ports.Port.Info, ['controller_state', 'slice_state', 'transport_admin_state'], name, value)


                class G709Info(Entity):
                    """
                    G709 operational information
                    
                    .. attribute:: ec
                    
                    	Corrected bit error counter 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ec_accum
                    
                    	FEC Corrected bit error accumulated counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ec_tca
                    
                    	FEC Corrected bits TCA information
                    	**type**\:   :py:class:`EcTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.EcTca>`
                    
                    .. attribute:: efec_mode
                    
                    	EFEC information
                    	**type**\:   :py:class:`G709efecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709efecMode>`
                    
                    .. attribute:: fe_cstr
                    
                    	FEC BER String 
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: fec_ber
                    
                    	pre fec ber calculated
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_ber_man
                    
                    	pre fec ber calculated
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:   :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.FecMismatch>`
                    
                    .. attribute:: fec_mode
                    
                    	FEC information
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: g709_prbs_mode
                    
                    	Configured mode of PRBS Test
                    	**type**\:   :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                    
                    .. attribute:: g709_prbs_pattern
                    
                    	Pattern of PRBS Test
                    	**type**\:   :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                    
                    .. attribute:: is_fec_mode_default
                    
                    	 Is Operating FEC Mode Default
                    	**type**\:  bool
                    
                    .. attribute:: is_g709_enabled
                    
                    	 Is G709 framing enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_prbs_enabled
                    
                    	'true' if Prbs is enabled 'false' otherwise
                    	**type**\:  bool
                    
                    .. attribute:: loopback_mode
                    
                    	Loopback information
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: network_conn_id
                    
                    	Network connection ID
                    	**type**\:  str
                    
                    	**length:** 0..65
                    
                    .. attribute:: network_port_id
                    
                    	Network port ID
                    	**type**\:  str
                    
                    	**length:** 0..65
                    
                    .. attribute:: odu_info
                    
                    	ODU layer Information
                    	**type**\:   :py:class:`OduInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo>`
                    
                    .. attribute:: otu_info
                    
                    	OTU layer information
                    	**type**\:   :py:class:`OtuInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo>`
                    
                    .. attribute:: prbs_time_stamp
                    
                    	Time stamp for prbs configuration
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: q
                    
                    	q value calculated
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: q_margin
                    
                    	q margin calculated
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: qmargin_str
                    
                    	QMargin String
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: qstr
                    
                    	Q String 
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: remote_fec_mode
                    
                    	Remote FEC information
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: uc
                    
                    	FEC Uncorrected words counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: uc_tca
                    
                    	FEC uncorrected words TCA information
                    	**type**\:   :py:class:`UcTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.UcTca>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.G709Info, self).__init__()

                        self.yang_name = "g709-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ec-tca" : ("ec_tca", Dwdm.Ports.Port.Info.G709Info.EcTca), "fec-mismatch" : ("fec_mismatch", Dwdm.Ports.Port.Info.G709Info.FecMismatch), "odu-info" : ("odu_info", Dwdm.Ports.Port.Info.G709Info.OduInfo), "otu-info" : ("otu_info", Dwdm.Ports.Port.Info.G709Info.OtuInfo), "uc-tca" : ("uc_tca", Dwdm.Ports.Port.Info.G709Info.UcTca)}
                        self._child_list_classes = {}

                        self.ec = YLeaf(YType.uint64, "ec")

                        self.ec_accum = YLeaf(YType.uint64, "ec-accum")

                        self.efec_mode = YLeaf(YType.enumeration, "efec-mode")

                        self.fe_cstr = YLeaf(YType.str, "fe-cstr")

                        self.fec_ber = YLeaf(YType.uint64, "fec-ber")

                        self.fec_ber_man = YLeaf(YType.int32, "fec-ber-man")

                        self.fec_mode = YLeaf(YType.int32, "fec-mode")

                        self.g709_prbs_mode = YLeaf(YType.enumeration, "g709-prbs-mode")

                        self.g709_prbs_pattern = YLeaf(YType.enumeration, "g709-prbs-pattern")

                        self.is_fec_mode_default = YLeaf(YType.boolean, "is-fec-mode-default")

                        self.is_g709_enabled = YLeaf(YType.boolean, "is-g709-enabled")

                        self.is_prbs_enabled = YLeaf(YType.boolean, "is-prbs-enabled")

                        self.loopback_mode = YLeaf(YType.int32, "loopback-mode")

                        self.network_conn_id = YLeaf(YType.str, "network-conn-id")

                        self.network_port_id = YLeaf(YType.str, "network-port-id")

                        self.prbs_time_stamp = YLeaf(YType.uint64, "prbs-time-stamp")

                        self.q = YLeaf(YType.uint64, "q")

                        self.q_margin = YLeaf(YType.uint64, "q-margin")

                        self.qmargin_str = YLeaf(YType.str, "qmargin-str")

                        self.qstr = YLeaf(YType.str, "qstr")

                        self.remote_fec_mode = YLeaf(YType.int32, "remote-fec-mode")

                        self.uc = YLeaf(YType.uint64, "uc")

                        self.ec_tca = Dwdm.Ports.Port.Info.G709Info.EcTca()
                        self.ec_tca.parent = self
                        self._children_name_map["ec_tca"] = "ec-tca"
                        self._children_yang_names.add("ec-tca")

                        self.fec_mismatch = Dwdm.Ports.Port.Info.G709Info.FecMismatch()
                        self.fec_mismatch.parent = self
                        self._children_name_map["fec_mismatch"] = "fec-mismatch"
                        self._children_yang_names.add("fec-mismatch")

                        self.odu_info = Dwdm.Ports.Port.Info.G709Info.OduInfo()
                        self.odu_info.parent = self
                        self._children_name_map["odu_info"] = "odu-info"
                        self._children_yang_names.add("odu-info")

                        self.otu_info = Dwdm.Ports.Port.Info.G709Info.OtuInfo()
                        self.otu_info.parent = self
                        self._children_name_map["otu_info"] = "otu-info"
                        self._children_yang_names.add("otu-info")

                        self.uc_tca = Dwdm.Ports.Port.Info.G709Info.UcTca()
                        self.uc_tca.parent = self
                        self._children_name_map["uc_tca"] = "uc-tca"
                        self._children_yang_names.add("uc-tca")
                        self._segment_path = lambda: "g709-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.G709Info, ['ec', 'ec_accum', 'efec_mode', 'fe_cstr', 'fec_ber', 'fec_ber_man', 'fec_mode', 'g709_prbs_mode', 'g709_prbs_pattern', 'is_fec_mode_default', 'is_g709_enabled', 'is_prbs_enabled', 'loopback_mode', 'network_conn_id', 'network_port_id', 'prbs_time_stamp', 'q', 'q_margin', 'qmargin_str', 'qstr', 'remote_fec_mode', 'uc'], name, value)


                    class EcTca(Entity):
                        """
                        FEC Corrected bits TCA information
                        
                        .. attribute:: counter
                        
                        	Error counter
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
                        
                        .. attribute:: threshold
                        
                        	Error threshold power
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.EcTca, self).__init__()

                            self.yang_name = "ec-tca"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                            self.threshold = YLeaf(YType.int32, "threshold")
                            self._segment_path = lambda: "ec-tca"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.EcTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


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

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.FecMismatch, self).__init__()

                            self.yang_name = "fec-mismatch"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                            self._segment_path = lambda: "fec-mismatch"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.FecMismatch, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                    class OduInfo(Entity):
                        """
                        ODU layer Information
                        
                        .. attribute:: ais
                        
                        	Alarm Indication Signal information
                        	**type**\:   :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais>`
                        
                        .. attribute:: bbe
                        
                        	Background Block Error information
                        	**type**\:   :py:class:`Bbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe>`
                        
                        .. attribute:: bbe_tca
                        
                        	Background Block Error TCA information
                        	**type**\:   :py:class:`BbeTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca>`
                        
                        .. attribute:: bber
                        
                        	Background Block Error Rate count information
                        	**type**\:   :py:class:`Bber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber>`
                        
                        .. attribute:: bdi
                        
                        	Backward Defect Indication information
                        	**type**\:   :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi>`
                        
                        .. attribute:: bei
                        
                        	Backward Error Indication counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bip
                        
                        	Bit Interleave Parity(BIP) counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: eoc
                        
                        	GCC End of Channel information
                        	**type**\:   :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc>`
                        
                        .. attribute:: es
                        
                        	Errored Seconds information
                        	**type**\:   :py:class:`Es <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Es>`
                        
                        .. attribute:: es_tca
                        
                        	Errored Seconds TCA information
                        	**type**\:   :py:class:`EsTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca>`
                        
                        .. attribute:: esr
                        
                        	Errored Seconds Rate information
                        	**type**\:   :py:class:`Esr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr>`
                        
                        .. attribute:: fc
                        
                        	Failure count information
                        	**type**\:   :py:class:`Fc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc>`
                        
                        .. attribute:: lck
                        
                        	Upstream Connection Locked information
                        	**type**\:   :py:class:`Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck>`
                        
                        .. attribute:: oci
                        
                        	Open Connection Indiction information
                        	**type**\:   :py:class:`Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci>`
                        
                        .. attribute:: ptim
                        
                        	Payload Type Identifier Mismatch information
                        	**type**\:   :py:class:`Ptim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim>`
                        
                        .. attribute:: sd_ber
                        
                        	Signal Degrade BER information
                        	**type**\:   :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer>`
                        
                        .. attribute:: ses
                        
                        	Severly Errored Seconds information
                        	**type**\:   :py:class:`Ses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses>`
                        
                        .. attribute:: sesr
                        
                        	Severly Errored Seconds Rate information
                        	**type**\:   :py:class:`Sesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr>`
                        
                        .. attribute:: sf_ber
                        
                        	Signal Fail  BER information
                        	**type**\:   :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer>`
                        
                        .. attribute:: tim
                        
                        	Trace Identifier Mismatch information
                        	**type**\:   :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim>`
                        
                        .. attribute:: tti
                        
                        	Trail Trace Identifier information
                        	**type**\:   :py:class:`Tti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti>`
                        
                        .. attribute:: uas
                        
                        	Unavailability Seconds information
                        	**type**\:   :py:class:`Uas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo, self).__init__()

                            self.yang_name = "odu-info"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ais" : ("ais", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais), "bbe" : ("bbe", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe), "bbe-tca" : ("bbe_tca", Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca), "bber" : ("bber", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber), "bdi" : ("bdi", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi), "eoc" : ("eoc", Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc), "es" : ("es", Dwdm.Ports.Port.Info.G709Info.OduInfo.Es), "es-tca" : ("es_tca", Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca), "esr" : ("esr", Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr), "fc" : ("fc", Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc), "lck" : ("lck", Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck), "oci" : ("oci", Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci), "ptim" : ("ptim", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim), "sd-ber" : ("sd_ber", Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer), "ses" : ("ses", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses), "sesr" : ("sesr", Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr), "sf-ber" : ("sf_ber", Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer), "tim" : ("tim", Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim), "tti" : ("tti", Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti), "uas" : ("uas", Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas)}
                            self._child_list_classes = {}

                            self.bei = YLeaf(YType.uint64, "bei")

                            self.bip = YLeaf(YType.uint64, "bip")

                            self.ais = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"
                            self._children_yang_names.add("ais")

                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe()
                            self.bbe.parent = self
                            self._children_name_map["bbe"] = "bbe"
                            self._children_yang_names.add("bbe")

                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self._children_name_map["bbe_tca"] = "bbe-tca"
                            self._children_yang_names.add("bbe-tca")

                            self.bber = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber()
                            self.bber.parent = self
                            self._children_name_map["bber"] = "bber"
                            self._children_yang_names.add("bber")

                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi()
                            self.bdi.parent = self
                            self._children_name_map["bdi"] = "bdi"
                            self._children_yang_names.add("bdi")

                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc()
                            self.eoc.parent = self
                            self._children_name_map["eoc"] = "eoc"
                            self._children_yang_names.add("eoc")

                            self.es = Dwdm.Ports.Port.Info.G709Info.OduInfo.Es()
                            self.es.parent = self
                            self._children_name_map["es"] = "es"
                            self._children_yang_names.add("es")

                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca()
                            self.es_tca.parent = self
                            self._children_name_map["es_tca"] = "es-tca"
                            self._children_yang_names.add("es-tca")

                            self.esr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr()
                            self.esr.parent = self
                            self._children_name_map["esr"] = "esr"
                            self._children_yang_names.add("esr")

                            self.fc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc()
                            self.fc.parent = self
                            self._children_name_map["fc"] = "fc"
                            self._children_yang_names.add("fc")

                            self.lck = Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck()
                            self.lck.parent = self
                            self._children_name_map["lck"] = "lck"
                            self._children_yang_names.add("lck")

                            self.oci = Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci()
                            self.oci.parent = self
                            self._children_name_map["oci"] = "oci"
                            self._children_yang_names.add("oci")

                            self.ptim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim()
                            self.ptim.parent = self
                            self._children_name_map["ptim"] = "ptim"
                            self._children_yang_names.add("ptim")

                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer()
                            self.sd_ber.parent = self
                            self._children_name_map["sd_ber"] = "sd-ber"
                            self._children_yang_names.add("sd-ber")

                            self.ses = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses()
                            self.ses.parent = self
                            self._children_name_map["ses"] = "ses"
                            self._children_yang_names.add("ses")

                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr()
                            self.sesr.parent = self
                            self._children_name_map["sesr"] = "sesr"
                            self._children_yang_names.add("sesr")

                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer()
                            self.sf_ber.parent = self
                            self._children_name_map["sf_ber"] = "sf-ber"
                            self._children_yang_names.add("sf-ber")

                            self.tim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim()
                            self.tim.parent = self
                            self._children_name_map["tim"] = "tim"
                            self._children_yang_names.add("tim")

                            self.tti = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti()
                            self.tti.parent = self
                            self._children_name_map["tti"] = "tti"
                            self._children_yang_names.add("tti")

                            self.uas = Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas()
                            self.uas.parent = self
                            self._children_name_map["uas"] = "uas"
                            self._children_yang_names.add("uas")
                            self._segment_path = lambda: "odu-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo, ['bei', 'bip'], name, value)


                        class Ais(Entity):
                            """
                            Alarm Indication Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "ais"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Bbe(Entity):
                            """
                            Background Block Error information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe, self).__init__()

                                self.yang_name = "bbe"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "bbe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe, ['counter'], name, value)


                        class BbeTca(Entity):
                            """
                            Background Block Error TCA information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, self).__init__()

                                self.yang_name = "bbe-tca"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "bbe-tca"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Bber(Entity):
                            """
                            Background Block Error Rate count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber, self).__init__()

                                self.yang_name = "bber"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "bber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber, ['counter'], name, value)


                        class Bdi(Entity):
                            """
                            Backward Defect Indication information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, self).__init__()

                                self.yang_name = "bdi"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "bdi"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Eoc(Entity):
                            """
                            GCC End of Channel information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, self).__init__()

                                self.yang_name = "eoc"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "eoc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Es(Entity):
                            """
                            Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Es, self).__init__()

                                self.yang_name = "es"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "es"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Es, ['counter'], name, value)


                        class EsTca(Entity):
                            """
                            Errored Seconds TCA information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, self).__init__()

                                self.yang_name = "es-tca"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "es-tca"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Esr(Entity):
                            """
                            Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr, self).__init__()

                                self.yang_name = "esr"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "esr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr, ['counter'], name, value)


                        class Fc(Entity):
                            """
                            Failure count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc, self).__init__()

                                self.yang_name = "fc"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "fc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc, ['counter'], name, value)


                        class Lck(Entity):
                            """
                            Upstream Connection Locked information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, self).__init__()

                                self.yang_name = "lck"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "lck"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Oci(Entity):
                            """
                            Open Connection Indiction information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, self).__init__()

                                self.yang_name = "oci"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "oci"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Ptim(Entity):
                            """
                            Payload Type Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, self).__init__()

                                self.yang_name = "ptim"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "ptim"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class SdBer(Entity):
                            """
                            Signal Degrade BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, self).__init__()

                                self.yang_name = "sd-ber"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "sd-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Ses(Entity):
                            """
                            Severly Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses, self).__init__()

                                self.yang_name = "ses"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "ses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses, ['counter'], name, value)


                        class Sesr(Entity):
                            """
                            Severly Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr, self).__init__()

                                self.yang_name = "sesr"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "sesr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr, ['counter'], name, value)


                        class SfBer(Entity):
                            """
                            Signal Fail  BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, self).__init__()

                                self.yang_name = "sf-ber"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "sf-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Tim(Entity):
                            """
                            Trace Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, self).__init__()

                                self.yang_name = "tim"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "tim"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Tti(Entity):
                            """
                            Trail Trace Identifier information
                            
                            .. attribute:: exp_dapi_range
                            
                            	 Expected DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: exp_oper_spec_range
                            
                            	 Expected Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: exp_sapi_range
                            
                            	 Expected SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_dapi
                            
                            	Expected DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: expected_dapi0
                            
                            	Expected DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_oper_spec
                            
                            	Expected Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: expected_sapi
                            
                            	Expected SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: expected_sapi0
                            
                            	Expected SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expected_tti
                            
                            	Expected TTI String
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            .. attribute:: rx_dapi
                            
                            	Rx DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_dapi0
                            
                            	Rx DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_dapi_range
                            
                            	 Rx DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec
                            
                            	Rx Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: rx_oper_spec_range
                            
                            	 Rx Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_sapi
                            
                            	Rx SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_sapi0
                            
                            	Rx SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_sapi_range
                            
                            	 Rx SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tti
                            
                            	Rx TTI String 
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            .. attribute:: tx_dapi
                            
                            	Tx DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_dapi0
                            
                            	Tx DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_dapi_range
                            
                            	 Tx DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_oper_spec
                            
                            	Tx Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: tx_oper_spec_range
                            
                            	 Tx Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_sapi
                            
                            	Tx SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_sapi0
                            
                            	Tx SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_sapi_range
                            
                            	 Tx SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tx_tti
                            
                            	Tx TTI String 
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, self).__init__()

                                self.yang_name = "tti"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exp_dapi_range = YLeaf(YType.str, "exp-dapi-range")

                                self.exp_oper_spec_range = YLeaf(YType.str, "exp-oper-spec-range")

                                self.exp_sapi_range = YLeaf(YType.str, "exp-sapi-range")

                                self.expected_dapi = YLeaf(YType.str, "expected-dapi")

                                self.expected_dapi0 = YLeaf(YType.str, "expected-dapi0")

                                self.expected_oper_spec = YLeaf(YType.str, "expected-oper-spec")

                                self.expected_sapi = YLeaf(YType.str, "expected-sapi")

                                self.expected_sapi0 = YLeaf(YType.str, "expected-sapi0")

                                self.expected_string_type = YLeaf(YType.uint32, "expected-string-type")

                                self.expected_tti = YLeaf(YType.str, "expected-tti")

                                self.rx_dapi = YLeaf(YType.str, "rx-dapi")

                                self.rx_dapi0 = YLeaf(YType.str, "rx-dapi0")

                                self.rx_dapi_range = YLeaf(YType.str, "rx-dapi-range")

                                self.rx_oper_spec = YLeaf(YType.str, "rx-oper-spec")

                                self.rx_oper_spec_range = YLeaf(YType.str, "rx-oper-spec-range")

                                self.rx_sapi = YLeaf(YType.str, "rx-sapi")

                                self.rx_sapi0 = YLeaf(YType.str, "rx-sapi0")

                                self.rx_sapi_range = YLeaf(YType.str, "rx-sapi-range")

                                self.rx_string_type = YLeaf(YType.uint32, "rx-string-type")

                                self.rx_tti = YLeaf(YType.str, "rx-tti")

                                self.tx_dapi = YLeaf(YType.str, "tx-dapi")

                                self.tx_dapi0 = YLeaf(YType.str, "tx-dapi0")

                                self.tx_dapi_range = YLeaf(YType.str, "tx-dapi-range")

                                self.tx_oper_spec = YLeaf(YType.str, "tx-oper-spec")

                                self.tx_oper_spec_range = YLeaf(YType.str, "tx-oper-spec-range")

                                self.tx_sapi = YLeaf(YType.str, "tx-sapi")

                                self.tx_sapi0 = YLeaf(YType.str, "tx-sapi0")

                                self.tx_sapi_range = YLeaf(YType.str, "tx-sapi-range")

                                self.tx_string_type = YLeaf(YType.uint32, "tx-string-type")

                                self.tx_tti = YLeaf(YType.str, "tx-tti")
                                self._segment_path = lambda: "tti"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, ['exp_dapi_range', 'exp_oper_spec_range', 'exp_sapi_range', 'expected_dapi', 'expected_dapi0', 'expected_oper_spec', 'expected_sapi', 'expected_sapi0', 'expected_string_type', 'expected_tti', 'rx_dapi', 'rx_dapi0', 'rx_dapi_range', 'rx_oper_spec', 'rx_oper_spec_range', 'rx_sapi', 'rx_sapi0', 'rx_sapi_range', 'rx_string_type', 'rx_tti', 'tx_dapi', 'tx_dapi0', 'tx_dapi_range', 'tx_oper_spec', 'tx_oper_spec_range', 'tx_sapi', 'tx_sapi0', 'tx_sapi_range', 'tx_string_type', 'tx_tti'], name, value)


                        class Uas(Entity):
                            """
                            Unavailability Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas, self).__init__()

                                self.yang_name = "uas"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "uas"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas, ['counter'], name, value)


                    class OtuInfo(Entity):
                        """
                        OTU layer information
                        
                        .. attribute:: ais
                        
                        	Alarm Indication Signal information
                        	**type**\:   :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais>`
                        
                        .. attribute:: bbe
                        
                        	Backgound Block Error information
                        	**type**\:   :py:class:`Bbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe>`
                        
                        .. attribute:: bbe_tca
                        
                        	 Backgound Block Error TCA information
                        	**type**\:   :py:class:`BbeTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca>`
                        
                        .. attribute:: bber
                        
                        	Backgound Block Error Rate information
                        	**type**\:   :py:class:`Bber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber>`
                        
                        .. attribute:: bdi
                        
                        	Backward Defect Indication information
                        	**type**\:   :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi>`
                        
                        .. attribute:: bei
                        
                        	Backward Error Indication counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bip
                        
                        	Bit Interleave Parity(BIP) counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: eoc
                        
                        	GCC End of Channel information
                        	**type**\:   :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc>`
                        
                        .. attribute:: es
                        
                        	Errored Seconds information 
                        	**type**\:   :py:class:`Es <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es>`
                        
                        .. attribute:: es_tca
                        
                        	Errored Seconds TCA information
                        	**type**\:   :py:class:`EsTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca>`
                        
                        .. attribute:: esr
                        
                        	Errored Seconds Rate information
                        	**type**\:   :py:class:`Esr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr>`
                        
                        .. attribute:: fc
                        
                        	Failure Count information
                        	**type**\:   :py:class:`Fc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc>`
                        
                        .. attribute:: iae
                        
                        	Incoming Alignment Error information
                        	**type**\:   :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae>`
                        
                        .. attribute:: lof
                        
                        	Loss of Frame information
                        	**type**\:   :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof>`
                        
                        .. attribute:: lom
                        
                        	Loss of MultiFrame information
                        	**type**\:   :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom>`
                        
                        .. attribute:: los
                        
                        	Loss of Signal information
                        	**type**\:   :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los>`
                        
                        .. attribute:: oof
                        
                        	Out of Frame information
                        	**type**\:   :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof>`
                        
                        .. attribute:: oom
                        
                        	Out of MultiFrame information
                        	**type**\:   :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom>`
                        
                        .. attribute:: prefec_sd_ber
                        
                        	Prefec Signal Degrade BER information
                        	**type**\:   :py:class:`PrefecSdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer>`
                        
                        .. attribute:: prefec_sf_ber
                        
                        	Prefec Signal Fail BER information
                        	**type**\:   :py:class:`PrefecSfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer>`
                        
                        .. attribute:: sd_ber
                        
                        	Signal Degrade BER information
                        	**type**\:   :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer>`
                        
                        .. attribute:: ses
                        
                        	Severly Errored Seconds information
                        	**type**\:   :py:class:`Ses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses>`
                        
                        .. attribute:: sesr
                        
                        	Severly Errored Seconds Rate information
                        	**type**\:   :py:class:`Sesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr>`
                        
                        .. attribute:: sf_ber
                        
                        	Signal Fail  BER information
                        	**type**\:   :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer>`
                        
                        .. attribute:: tim
                        
                        	Trace Identifier Mismatch information
                        	**type**\:   :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim>`
                        
                        .. attribute:: tti
                        
                        	Trail Trace Identifier information
                        	**type**\:   :py:class:`Tti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti>`
                        
                        .. attribute:: uas
                        
                        	Unavailability Seconds information
                        	**type**\:   :py:class:`Uas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo, self).__init__()

                            self.yang_name = "otu-info"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ais" : ("ais", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais), "bbe" : ("bbe", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe), "bbe-tca" : ("bbe_tca", Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca), "bber" : ("bber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber), "bdi" : ("bdi", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi), "eoc" : ("eoc", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc), "es" : ("es", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es), "es-tca" : ("es_tca", Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca), "esr" : ("esr", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr), "fc" : ("fc", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc), "iae" : ("iae", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae), "lof" : ("lof", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof), "lom" : ("lom", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom), "los" : ("los", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los), "oof" : ("oof", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof), "oom" : ("oom", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom), "prefec-sd-ber" : ("prefec_sd_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer), "prefec-sf-ber" : ("prefec_sf_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer), "sd-ber" : ("sd_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer), "ses" : ("ses", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses), "sesr" : ("sesr", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr), "sf-ber" : ("sf_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer), "tim" : ("tim", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim), "tti" : ("tti", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti), "uas" : ("uas", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas)}
                            self._child_list_classes = {}

                            self.bei = YLeaf(YType.uint64, "bei")

                            self.bip = YLeaf(YType.uint64, "bip")

                            self.ais = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"
                            self._children_yang_names.add("ais")

                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe()
                            self.bbe.parent = self
                            self._children_name_map["bbe"] = "bbe"
                            self._children_yang_names.add("bbe")

                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self._children_name_map["bbe_tca"] = "bbe-tca"
                            self._children_yang_names.add("bbe-tca")

                            self.bber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber()
                            self.bber.parent = self
                            self._children_name_map["bber"] = "bber"
                            self._children_yang_names.add("bber")

                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi()
                            self.bdi.parent = self
                            self._children_name_map["bdi"] = "bdi"
                            self._children_yang_names.add("bdi")

                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc()
                            self.eoc.parent = self
                            self._children_name_map["eoc"] = "eoc"
                            self._children_yang_names.add("eoc")

                            self.es = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es()
                            self.es.parent = self
                            self._children_name_map["es"] = "es"
                            self._children_yang_names.add("es")

                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca()
                            self.es_tca.parent = self
                            self._children_name_map["es_tca"] = "es-tca"
                            self._children_yang_names.add("es-tca")

                            self.esr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr()
                            self.esr.parent = self
                            self._children_name_map["esr"] = "esr"
                            self._children_yang_names.add("esr")

                            self.fc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc()
                            self.fc.parent = self
                            self._children_name_map["fc"] = "fc"
                            self._children_yang_names.add("fc")

                            self.iae = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae()
                            self.iae.parent = self
                            self._children_name_map["iae"] = "iae"
                            self._children_yang_names.add("iae")

                            self.lof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof()
                            self.lof.parent = self
                            self._children_name_map["lof"] = "lof"
                            self._children_yang_names.add("lof")

                            self.lom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom()
                            self.lom.parent = self
                            self._children_name_map["lom"] = "lom"
                            self._children_yang_names.add("lom")

                            self.los = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los()
                            self.los.parent = self
                            self._children_name_map["los"] = "los"
                            self._children_yang_names.add("los")

                            self.oof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof()
                            self.oof.parent = self
                            self._children_name_map["oof"] = "oof"
                            self._children_yang_names.add("oof")

                            self.oom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom()
                            self.oom.parent = self
                            self._children_name_map["oom"] = "oom"
                            self._children_yang_names.add("oom")

                            self.prefec_sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer()
                            self.prefec_sd_ber.parent = self
                            self._children_name_map["prefec_sd_ber"] = "prefec-sd-ber"
                            self._children_yang_names.add("prefec-sd-ber")

                            self.prefec_sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer()
                            self.prefec_sf_ber.parent = self
                            self._children_name_map["prefec_sf_ber"] = "prefec-sf-ber"
                            self._children_yang_names.add("prefec-sf-ber")

                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer()
                            self.sd_ber.parent = self
                            self._children_name_map["sd_ber"] = "sd-ber"
                            self._children_yang_names.add("sd-ber")

                            self.ses = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses()
                            self.ses.parent = self
                            self._children_name_map["ses"] = "ses"
                            self._children_yang_names.add("ses")

                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr()
                            self.sesr.parent = self
                            self._children_name_map["sesr"] = "sesr"
                            self._children_yang_names.add("sesr")

                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer()
                            self.sf_ber.parent = self
                            self._children_name_map["sf_ber"] = "sf-ber"
                            self._children_yang_names.add("sf-ber")

                            self.tim = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim()
                            self.tim.parent = self
                            self._children_name_map["tim"] = "tim"
                            self._children_yang_names.add("tim")

                            self.tti = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti()
                            self.tti.parent = self
                            self._children_name_map["tti"] = "tti"
                            self._children_yang_names.add("tti")

                            self.uas = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas()
                            self.uas.parent = self
                            self._children_name_map["uas"] = "uas"
                            self._children_yang_names.add("uas")
                            self._segment_path = lambda: "otu-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo, ['bei', 'bip'], name, value)


                        class Ais(Entity):
                            """
                            Alarm Indication Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "ais"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Bbe(Entity):
                            """
                            Backgound Block Error information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe, self).__init__()

                                self.yang_name = "bbe"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "bbe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe, ['counter'], name, value)


                        class BbeTca(Entity):
                            """
                             Backgound Block Error TCA information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, self).__init__()

                                self.yang_name = "bbe-tca"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "bbe-tca"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Bber(Entity):
                            """
                            Backgound Block Error Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber, self).__init__()

                                self.yang_name = "bber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "bber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber, ['counter'], name, value)


                        class Bdi(Entity):
                            """
                            Backward Defect Indication information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, self).__init__()

                                self.yang_name = "bdi"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "bdi"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Eoc(Entity):
                            """
                            GCC End of Channel information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, self).__init__()

                                self.yang_name = "eoc"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "eoc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Es(Entity):
                            """
                            Errored Seconds information 
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es, self).__init__()

                                self.yang_name = "es"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "es"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es, ['counter'], name, value)


                        class EsTca(Entity):
                            """
                            Errored Seconds TCA information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, self).__init__()

                                self.yang_name = "es-tca"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "es-tca"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Esr(Entity):
                            """
                            Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr, self).__init__()

                                self.yang_name = "esr"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "esr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr, ['counter'], name, value)


                        class Fc(Entity):
                            """
                            Failure Count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc, self).__init__()

                                self.yang_name = "fc"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "fc"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc, ['counter'], name, value)


                        class Iae(Entity):
                            """
                            Incoming Alignment Error information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, self).__init__()

                                self.yang_name = "iae"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "iae"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Lof(Entity):
                            """
                            Loss of Frame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, self).__init__()

                                self.yang_name = "lof"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "lof"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Lom(Entity):
                            """
                            Loss of MultiFrame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, self).__init__()

                                self.yang_name = "lom"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "lom"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Los(Entity):
                            """
                            Loss of Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, self).__init__()

                                self.yang_name = "los"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "los"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Oof(Entity):
                            """
                            Out of Frame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, self).__init__()

                                self.yang_name = "oof"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "oof"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Oom(Entity):
                            """
                            Out of MultiFrame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, self).__init__()

                                self.yang_name = "oom"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "oom"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class PrefecSdBer(Entity):
                            """
                            Prefec Signal Degrade BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, self).__init__()

                                self.yang_name = "prefec-sd-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "prefec-sd-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class PrefecSfBer(Entity):
                            """
                            Prefec Signal Fail BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, self).__init__()

                                self.yang_name = "prefec-sf-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "prefec-sf-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class SdBer(Entity):
                            """
                            Signal Degrade BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, self).__init__()

                                self.yang_name = "sd-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "sd-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Ses(Entity):
                            """
                            Severly Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses, self).__init__()

                                self.yang_name = "ses"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "ses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses, ['counter'], name, value)


                        class Sesr(Entity):
                            """
                            Severly Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr, self).__init__()

                                self.yang_name = "sesr"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "sesr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr, ['counter'], name, value)


                        class SfBer(Entity):
                            """
                            Signal Fail  BER information
                            
                            .. attribute:: counter
                            
                            	Error counter
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
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, self).__init__()

                                self.yang_name = "sf-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")
                                self._segment_path = lambda: "sf-ber"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                        class Tim(Entity):
                            """
                            Trace Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, self).__init__()

                                self.yang_name = "tim"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")
                                self._segment_path = lambda: "tim"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled'], name, value)


                        class Tti(Entity):
                            """
                            Trail Trace Identifier information
                            
                            .. attribute:: exp_dapi_range
                            
                            	 Expected DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: exp_oper_spec_range
                            
                            	 Expected Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: exp_sapi_range
                            
                            	 Expected SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_dapi
                            
                            	Expected DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: expected_dapi0
                            
                            	Expected DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_oper_spec
                            
                            	Expected Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: expected_sapi
                            
                            	Expected SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: expected_sapi0
                            
                            	Expected SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expected_tti
                            
                            	Expected TTI String
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            .. attribute:: rx_dapi
                            
                            	Rx DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_dapi0
                            
                            	Rx DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_dapi_range
                            
                            	 Rx DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec
                            
                            	Rx Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: rx_oper_spec_range
                            
                            	 Rx Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_sapi
                            
                            	Rx SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_sapi0
                            
                            	Rx SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_sapi_range
                            
                            	 Rx SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tti
                            
                            	Rx TTI String 
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            .. attribute:: tx_dapi
                            
                            	Tx DAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_dapi0
                            
                            	Tx DAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_dapi_range
                            
                            	 Tx DAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_oper_spec
                            
                            	Tx Operator Specific Field
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: tx_oper_spec_range
                            
                            	 Tx Operator Specific Field Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_sapi
                            
                            	Tx SAPI[1\-15] Field
                            	**type**\:  str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_sapi0
                            
                            	Tx SAPI[0] Field
                            	**type**\:  str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_sapi_range
                            
                            	 Tx SAPI Range String
                            	**type**\:  str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_string_type
                            
                            	Type of String
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tx_tti
                            
                            	Tx TTI String 
                            	**type**\:  str
                            
                            	**length:** 0..129
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, self).__init__()

                                self.yang_name = "tti"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exp_dapi_range = YLeaf(YType.str, "exp-dapi-range")

                                self.exp_oper_spec_range = YLeaf(YType.str, "exp-oper-spec-range")

                                self.exp_sapi_range = YLeaf(YType.str, "exp-sapi-range")

                                self.expected_dapi = YLeaf(YType.str, "expected-dapi")

                                self.expected_dapi0 = YLeaf(YType.str, "expected-dapi0")

                                self.expected_oper_spec = YLeaf(YType.str, "expected-oper-spec")

                                self.expected_sapi = YLeaf(YType.str, "expected-sapi")

                                self.expected_sapi0 = YLeaf(YType.str, "expected-sapi0")

                                self.expected_string_type = YLeaf(YType.uint32, "expected-string-type")

                                self.expected_tti = YLeaf(YType.str, "expected-tti")

                                self.rx_dapi = YLeaf(YType.str, "rx-dapi")

                                self.rx_dapi0 = YLeaf(YType.str, "rx-dapi0")

                                self.rx_dapi_range = YLeaf(YType.str, "rx-dapi-range")

                                self.rx_oper_spec = YLeaf(YType.str, "rx-oper-spec")

                                self.rx_oper_spec_range = YLeaf(YType.str, "rx-oper-spec-range")

                                self.rx_sapi = YLeaf(YType.str, "rx-sapi")

                                self.rx_sapi0 = YLeaf(YType.str, "rx-sapi0")

                                self.rx_sapi_range = YLeaf(YType.str, "rx-sapi-range")

                                self.rx_string_type = YLeaf(YType.uint32, "rx-string-type")

                                self.rx_tti = YLeaf(YType.str, "rx-tti")

                                self.tx_dapi = YLeaf(YType.str, "tx-dapi")

                                self.tx_dapi0 = YLeaf(YType.str, "tx-dapi0")

                                self.tx_dapi_range = YLeaf(YType.str, "tx-dapi-range")

                                self.tx_oper_spec = YLeaf(YType.str, "tx-oper-spec")

                                self.tx_oper_spec_range = YLeaf(YType.str, "tx-oper-spec-range")

                                self.tx_sapi = YLeaf(YType.str, "tx-sapi")

                                self.tx_sapi0 = YLeaf(YType.str, "tx-sapi0")

                                self.tx_sapi_range = YLeaf(YType.str, "tx-sapi-range")

                                self.tx_string_type = YLeaf(YType.uint32, "tx-string-type")

                                self.tx_tti = YLeaf(YType.str, "tx-tti")
                                self._segment_path = lambda: "tti"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, ['exp_dapi_range', 'exp_oper_spec_range', 'exp_sapi_range', 'expected_dapi', 'expected_dapi0', 'expected_oper_spec', 'expected_sapi', 'expected_sapi0', 'expected_string_type', 'expected_tti', 'rx_dapi', 'rx_dapi0', 'rx_dapi_range', 'rx_oper_spec', 'rx_oper_spec_range', 'rx_sapi', 'rx_sapi0', 'rx_sapi_range', 'rx_string_type', 'rx_tti', 'tx_dapi', 'tx_dapi0', 'tx_dapi_range', 'tx_oper_spec', 'tx_oper_spec_range', 'tx_sapi', 'tx_sapi0', 'tx_sapi_range', 'tx_string_type', 'tx_tti'], name, value)


                        class Uas(Entity):
                            """
                            Unavailability Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas, self).__init__()

                                self.yang_name = "uas"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.counter = YLeaf(YType.uint64, "counter")
                                self._segment_path = lambda: "uas"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas, ['counter'], name, value)


                    class UcTca(Entity):
                        """
                        FEC uncorrected words TCA information
                        
                        .. attribute:: counter
                        
                        	Error counter
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
                        
                        .. attribute:: threshold
                        
                        	Error threshold power
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.UcTca, self).__init__()

                            self.yang_name = "uc-tca"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                            self.threshold = YLeaf(YType.int32, "threshold")
                            self._segment_path = lambda: "uc-tca"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.UcTca, ['counter', 'is_asserted', 'is_detected', 'reporting_enabled', 'threshold'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg
                    
                    	Network Srlg
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.NetworkSrlgInfo, self).__init__()

                        self.yang_name = "network-srlg-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.network_srlg = YLeafList(YType.uint32, "network-srlg")
                        self._segment_path = lambda: "network-srlg-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.NetworkSrlgInfo, ['network_srlg'], name, value)


                class OpticsInfo(Entity):
                    """
                    Optics operational information
                    
                    .. attribute:: chromatic_dispersion
                    
                    	Current chromatic dispersion
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: clock_source
                    
                    	Actual transmit clock source
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: configured_wave_channel
                    
                    	Wavelength channel set from configuration
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: default_wave_channel
                    
                    	Wavelength channel default from hardware
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: differential_group_delay
                    
                    	Current differential group Delay
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: gmpls_set_wave_channel
                    
                    	Wavelength channel set by GMPLS
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: input_power_fail
                    
                    	Receive power failure(above/belowe a threshold) count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_rx_los_threshold_supported
                    
                    	TRUE if  Rx LOS thresold configurable
                    	**type**\:  bool
                    
                    .. attribute:: is_wave_frequency_progressive_valid
                    
                    	True if Progressive Frequency is supported by hw
                    	**type**\:  bool
                    
                    .. attribute:: is_wave_frequency_valid
                    
                    	True if hw supported wavelength frequency readback
                    	**type**\:  bool
                    
                    .. attribute:: laser_bias_current_avg
                    
                    	Laser bias current average value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_bias_current_max
                    
                    	Laser bias current maxinum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_bias_current_min
                    
                    	Laser bias current minimum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_current_bias
                    
                    	Laser current bias value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_current_bias_threshold
                    
                    	 Laser Current Bias threshold value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optics_type
                    
                    	Optics type name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: output_power_fail
                    
                    	Transmit power failure(above/belowe a threshold) count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: phase_noise
                    
                    	Current Phase Noise
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: polarization_change_rate
                    
                    	Current Polarization change rate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: polarization_dependent_loss
                    
                    	Current Polarization Dependent loss
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: polarization_mode_dispersion
                    
                    	Current polarization mode dispersion
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_avg
                    
                    	Recieve power average value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_max
                    
                    	Receive power maximum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_min
                    
                    	Recieve power mininum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rx_los_threshold
                    
                    	Rx LOS threshold value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: signal_to_noise_ratio
                    
                    	Current optical signal to noise ratio
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dbm
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_avg
                    
                    	Transmit optical average value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_max
                    
                    	Transmit power maximum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_min
                    
                    	Transmit  power mininum value in the interval time
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_threshold
                    
                    	Transmit power threshold value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: wave_band
                    
                    	Wavelength band information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel
                    
                    	Current ITU wavelength channel number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel_owner
                    
                    	Owner of current wavelength
                    	**type**\:   :py:class:`DwdmWaveChannelOwner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmWaveChannelOwner>`
                    
                    .. attribute:: wave_frequency
                    
                    	 wavelenght frequency read from hw in the uint 0 .01nm
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_frequency_progressive_string
                    
                    	Wave Frequency Information for Progressive Frequencies
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: wavelength_progressive
                    
                    	Wavelength Information for Progressive Frequencies
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wavelength_progressive_string
                    
                    	Wavelength Information for Progressive Frequencies
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.OpticsInfo, self).__init__()

                        self.yang_name = "optics-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.chromatic_dispersion = YLeaf(YType.int32, "chromatic-dispersion")

                        self.clock_source = YLeaf(YType.uint8, "clock-source")

                        self.configured_wave_channel = YLeaf(YType.uint16, "configured-wave-channel")

                        self.default_wave_channel = YLeaf(YType.uint16, "default-wave-channel")

                        self.differential_group_delay = YLeaf(YType.int32, "differential-group-delay")

                        self.gmpls_set_wave_channel = YLeaf(YType.uint16, "gmpls-set-wave-channel")

                        self.input_power_fail = YLeaf(YType.uint32, "input-power-fail")

                        self.is_rx_los_threshold_supported = YLeaf(YType.boolean, "is-rx-los-threshold-supported")

                        self.is_wave_frequency_progressive_valid = YLeaf(YType.boolean, "is-wave-frequency-progressive-valid")

                        self.is_wave_frequency_valid = YLeaf(YType.boolean, "is-wave-frequency-valid")

                        self.laser_bias_current_avg = YLeaf(YType.int32, "laser-bias-current-avg")

                        self.laser_bias_current_max = YLeaf(YType.int32, "laser-bias-current-max")

                        self.laser_bias_current_min = YLeaf(YType.int32, "laser-bias-current-min")

                        self.laser_current_bias = YLeaf(YType.int32, "laser-current-bias")

                        self.laser_current_bias_threshold = YLeaf(YType.int32, "laser-current-bias-threshold")

                        self.optics_type = YLeaf(YType.str, "optics-type")

                        self.output_power_fail = YLeaf(YType.uint32, "output-power-fail")

                        self.phase_noise = YLeaf(YType.uint32, "phase-noise")

                        self.polarization_change_rate = YLeaf(YType.uint32, "polarization-change-rate")

                        self.polarization_dependent_loss = YLeaf(YType.int32, "polarization-dependent-loss")

                        self.polarization_mode_dispersion = YLeaf(YType.int32, "polarization-mode-dispersion")

                        self.receive_power = YLeaf(YType.int32, "receive-power")

                        self.receive_power_avg = YLeaf(YType.int32, "receive-power-avg")

                        self.receive_power_max = YLeaf(YType.int32, "receive-power-max")

                        self.receive_power_min = YLeaf(YType.int32, "receive-power-min")

                        self.rx_los_threshold = YLeaf(YType.int32, "rx-los-threshold")

                        self.signal_to_noise_ratio = YLeaf(YType.int32, "signal-to-noise-ratio")

                        self.transmit_power = YLeaf(YType.int32, "transmit-power")

                        self.transmit_power_avg = YLeaf(YType.int32, "transmit-power-avg")

                        self.transmit_power_max = YLeaf(YType.int32, "transmit-power-max")

                        self.transmit_power_min = YLeaf(YType.int32, "transmit-power-min")

                        self.transmit_power_threshold = YLeaf(YType.int32, "transmit-power-threshold")

                        self.wave_band = YLeaf(YType.uint32, "wave-band")

                        self.wave_channel = YLeaf(YType.uint32, "wave-channel")

                        self.wave_channel_owner = YLeaf(YType.enumeration, "wave-channel-owner")

                        self.wave_frequency = YLeaf(YType.uint32, "wave-frequency")

                        self.wave_frequency_progressive_string = YLeaf(YType.str, "wave-frequency-progressive-string")

                        self.wavelength_progressive = YLeaf(YType.uint32, "wavelength-progressive")

                        self.wavelength_progressive_string = YLeaf(YType.str, "wavelength-progressive-string")
                        self._segment_path = lambda: "optics-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.OpticsInfo, ['chromatic_dispersion', 'clock_source', 'configured_wave_channel', 'default_wave_channel', 'differential_group_delay', 'gmpls_set_wave_channel', 'input_power_fail', 'is_rx_los_threshold_supported', 'is_wave_frequency_progressive_valid', 'is_wave_frequency_valid', 'laser_bias_current_avg', 'laser_bias_current_max', 'laser_bias_current_min', 'laser_current_bias', 'laser_current_bias_threshold', 'optics_type', 'output_power_fail', 'phase_noise', 'polarization_change_rate', 'polarization_dependent_loss', 'polarization_mode_dispersion', 'receive_power', 'receive_power_avg', 'receive_power_max', 'receive_power_min', 'rx_los_threshold', 'signal_to_noise_ratio', 'transmit_power', 'transmit_power_avg', 'transmit_power_max', 'transmit_power_min', 'transmit_power_threshold', 'wave_band', 'wave_channel', 'wave_channel_owner', 'wave_frequency', 'wave_frequency_progressive_string', 'wavelength_progressive', 'wavelength_progressive_string'], name, value)


                class Proactive(Entity):
                    """
                    Proactive protection information
                    
                    .. attribute:: alarm_state
                    
                    	AlarmState
                    	**type**\:  bool
                    
                    .. attribute:: default_rvrt_thresh_coeff
                    
                    	Default Revert threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_rvrt_thresh_power
                    
                    	Default Revert threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_trig_thresh_coeff
                    
                    	Default Trigger threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_trig_thresh_power
                    
                    	Default Trigger threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: interface_trigger
                    
                    	Proactive Interface Triffer
                    	**type**\:  bool
                    
                    .. attribute:: prefec_thresh_crossed
                    
                    	Prefec Trigger Thresh Crossed
                    	**type**\:  bool
                    
                    .. attribute:: proactive_feature
                    
                    	Feature Support
                    	**type**\:  bool
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:   :py:class:`G709ppintfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppintfState>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:   :py:class:`G709ppfsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppfsmState>`
                    
                    .. attribute:: proactive_mode
                    
                    	Proactive Mode
                    	**type**\:   :py:class:`G709ppfsmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppfsmMode>`
                    
                    .. attribute:: protection_trigger
                    
                    	Protection Trigger State
                    	**type**\:  bool
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_ec_cnt
                    
                    	Revert EC Cnt
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_samples
                    
                    	Required Revert Samples
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_aps
                    
                    	Received APS byte
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_aps_descr
                    
                    	Rx APS Description
                    	**type**\:   :py:class:`G709apsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709apsByte>`
                    
                    .. attribute:: tas_state
                    
                    	TAS State
                    	**type**\:   :py:class:`DwdmtasState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasState>`
                    
                    .. attribute:: trig_ec_cnt
                    
                    	Trigger EC Cnt
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: trig_samples
                    
                    	Required Trigger Samples
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
                    
                    .. attribute:: tx_aps
                    
                    	Transmitted APS Byte
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tx_aps_descr
                    
                    	Tx APS Description
                    	**type**\:   :py:class:`G709apsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709apsByte>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.alarm_state = YLeaf(YType.boolean, "alarm-state")

                        self.default_rvrt_thresh_coeff = YLeaf(YType.uint8, "default-rvrt-thresh-coeff")

                        self.default_rvrt_thresh_power = YLeaf(YType.uint8, "default-rvrt-thresh-power")

                        self.default_trig_thresh_coeff = YLeaf(YType.uint8, "default-trig-thresh-coeff")

                        self.default_trig_thresh_power = YLeaf(YType.uint8, "default-trig-thresh-power")

                        self.interface_trigger = YLeaf(YType.boolean, "interface-trigger")

                        self.prefec_thresh_crossed = YLeaf(YType.boolean, "prefec-thresh-crossed")

                        self.proactive_feature = YLeaf(YType.boolean, "proactive-feature")

                        self.proactive_fsm_if_state = YLeaf(YType.enumeration, "proactive-fsm-if-state")

                        self.proactive_fsm_state = YLeaf(YType.enumeration, "proactive-fsm-state")

                        self.proactive_mode = YLeaf(YType.enumeration, "proactive-mode")

                        self.protection_trigger = YLeaf(YType.boolean, "protection-trigger")

                        self.revert_window = YLeaf(YType.uint32, "revert-window")

                        self.rvrt_ec_cnt = YLeaf(YType.uint32, "rvrt-ec-cnt")

                        self.rvrt_samples = YLeaf(YType.uint8, "rvrt-samples")

                        self.rvrt_thresh_coeff = YLeaf(YType.uint8, "rvrt-thresh-coeff")

                        self.rvrt_thresh_power = YLeaf(YType.uint8, "rvrt-thresh-power")

                        self.rx_aps = YLeaf(YType.uint8, "rx-aps")

                        self.rx_aps_descr = YLeaf(YType.enumeration, "rx-aps-descr")

                        self.tas_state = YLeaf(YType.enumeration, "tas-state")

                        self.trig_ec_cnt = YLeaf(YType.uint32, "trig-ec-cnt")

                        self.trig_samples = YLeaf(YType.uint8, "trig-samples")

                        self.trig_thresh_coeff = YLeaf(YType.uint8, "trig-thresh-coeff")

                        self.trig_thresh_power = YLeaf(YType.uint8, "trig-thresh-power")

                        self.trigger_window = YLeaf(YType.uint32, "trigger-window")

                        self.tx_aps = YLeaf(YType.uint8, "tx-aps")

                        self.tx_aps_descr = YLeaf(YType.enumeration, "tx-aps-descr")
                        self._segment_path = lambda: "proactive"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.Proactive, ['alarm_state', 'default_rvrt_thresh_coeff', 'default_rvrt_thresh_power', 'default_trig_thresh_coeff', 'default_trig_thresh_power', 'interface_trigger', 'prefec_thresh_crossed', 'proactive_feature', 'proactive_fsm_if_state', 'proactive_fsm_state', 'proactive_mode', 'protection_trigger', 'revert_window', 'rvrt_ec_cnt', 'rvrt_samples', 'rvrt_thresh_coeff', 'rvrt_thresh_power', 'rx_aps', 'rx_aps_descr', 'tas_state', 'trig_ec_cnt', 'trig_samples', 'trig_thresh_coeff', 'trig_thresh_power', 'trigger_window', 'tx_aps', 'tx_aps_descr'], name, value)


                class SignalLog(Entity):
                    """
                    Signal log information
                    
                    .. attribute:: is_log_enabled
                    
                    	'true' if signal log is enabled 'false' otherwise
                    	**type**\:  bool
                    
                    .. attribute:: log_filename
                    
                    	Log file name 
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.SignalLog, self).__init__()

                        self.yang_name = "signal-log"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                        self.log_filename = YLeaf(YType.str, "log-filename")
                        self._segment_path = lambda: "signal-log"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.SignalLog, ['is_log_enabled', 'log_filename'], name, value)


                class TdcInfo(Entity):
                    """
                    TDC operational information
                    
                    .. attribute:: dispersion_offset
                    
                    	TDC Dispersion Offset
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_reroute_control_enabled
                    
                    	TRUE for ENABLED else DISABLED
                    	**type**\:  bool
                    
                    .. attribute:: major_alarm
                    
                    	TRUE for Alarm condition else FALSE
                    	**type**\:  bool
                    
                    .. attribute:: operation_mode
                    
                    	TRUE for MANUAL else AUTO
                    	**type**\:  bool
                    
                    .. attribute:: reroute_ber
                    
                    	Reroute BER
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tdc_status
                    
                    	TRUE if TDC Aquiring else Locked
                    	**type**\:  bool
                    
                    .. attribute:: tdc_valid
                    
                    	TRUE for Valid else Invalid
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.TdcInfo, self).__init__()

                        self.yang_name = "tdc-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dispersion_offset = YLeaf(YType.int32, "dispersion-offset")

                        self.is_reroute_control_enabled = YLeaf(YType.boolean, "is-reroute-control-enabled")

                        self.major_alarm = YLeaf(YType.boolean, "major-alarm")

                        self.operation_mode = YLeaf(YType.boolean, "operation-mode")

                        self.reroute_ber = YLeaf(YType.int32, "reroute-ber")

                        self.tdc_status = YLeaf(YType.boolean, "tdc-status")

                        self.tdc_valid = YLeaf(YType.boolean, "tdc-valid")
                        self._segment_path = lambda: "tdc-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.TdcInfo, ['dispersion_offset', 'is_reroute_control_enabled', 'major_alarm', 'operation_mode', 'reroute_ber', 'tdc_status', 'tdc_valid'], name, value)


            class Optics(Entity):
                """
                DWDM Port optics operational data
                
                .. attribute:: wave_info
                
                	DWDM port wavelength information data
                	**type**\:   :py:class:`WaveInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Optics.WaveInfo>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Optics, self).__init__()

                    self.yang_name = "optics"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"wave-info" : ("wave_info", Dwdm.Ports.Port.Optics.WaveInfo)}
                    self._child_list_classes = {}

                    self.wave_info = Dwdm.Ports.Port.Optics.WaveInfo()
                    self.wave_info.parent = self
                    self._children_name_map["wave_info"] = "wave-info"
                    self._children_yang_names.add("wave-info")
                    self._segment_path = lambda: "optics"


                class WaveInfo(Entity):
                    """
                    DWDM port wavelength information data
                    
                    .. attribute:: wave_band
                    
                    	Wavelength band
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel_max
                    
                    	Highest ITU wavelength channel number supported
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel_min
                    
                    	Lowest ITU wavelength channel number supported
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Optics.WaveInfo, self).__init__()

                        self.yang_name = "wave-info"
                        self.yang_parent_name = "optics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.wave_band = YLeaf(YType.uint32, "wave-band")

                        self.wave_channel_max = YLeaf(YType.uint32, "wave-channel-max")

                        self.wave_channel_min = YLeaf(YType.uint32, "wave-channel-min")
                        self._segment_path = lambda: "wave-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Optics.WaveInfo, ['wave_band', 'wave_channel_max', 'wave_channel_min'], name, value)


            class Prbs(Entity):
                """
                DWDM Port PRBS related data
                
                .. attribute:: fifteen_minutes_bucket
                
                	Port 15\-minute PRBS statistics table
                	**type**\:   :py:class:`FifteenMinutesBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket>`
                
                .. attribute:: twenty_four_hours_bucket
                
                	Port 24\-hour PRBS statistics table
                	**type**\:   :py:class:`TwentyFourHoursBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Prbs, self).__init__()

                    self.yang_name = "prbs"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"fifteen-minutes-bucket" : ("fifteen_minutes_bucket", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket), "twenty-four-hours-bucket" : ("twenty_four_hours_bucket", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket)}
                    self._child_list_classes = {}

                    self.fifteen_minutes_bucket = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket()
                    self.fifteen_minutes_bucket.parent = self
                    self._children_name_map["fifteen_minutes_bucket"] = "fifteen-minutes-bucket"
                    self._children_yang_names.add("fifteen-minutes-bucket")

                    self.twenty_four_hours_bucket = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket()
                    self.twenty_four_hours_bucket.parent = self
                    self._children_name_map["twenty_four_hours_bucket"] = "twenty-four-hours-bucket"
                    self._children_yang_names.add("twenty-four-hours-bucket")
                    self._segment_path = lambda: "prbs"


                class FifteenMinutesBucket(Entity):
                    """
                    Port 15\-minute PRBS statistics table
                    
                    .. attribute:: fifteen_minutes_statistics
                    
                    	Port 15\-minute PRBS statistics data
                    	**type**\:   :py:class:`FifteenMinutesStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket, self).__init__()

                        self.yang_name = "fifteen-minutes-bucket"
                        self.yang_parent_name = "prbs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"fifteen-minutes-statistics" : ("fifteen_minutes_statistics", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics)}
                        self._child_list_classes = {}

                        self.fifteen_minutes_statistics = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics()
                        self.fifteen_minutes_statistics.parent = self
                        self._children_name_map["fifteen_minutes_statistics"] = "fifteen-minutes-statistics"
                        self._children_yang_names.add("fifteen-minutes-statistics")
                        self._segment_path = lambda: "fifteen-minutes-bucket"


                    class FifteenMinutesStatistics(Entity):
                        """
                        Port 15\-minute PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of    :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, self).__init__()

                            self.yang_name = "fifteen-minutes-statistics"
                            self.yang_parent_name = "fifteen-minutes-bucket"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"prbs-entry" : ("prbs_entry", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry)}

                            self.is_prbs_enabled = YLeaf(YType.boolean, "is-prbs-enabled")

                            self.prbs_config_mode = YLeaf(YType.enumeration, "prbs-config-mode")

                            self.prbs_entry = YList(self)
                            self._segment_path = lambda: "fifteen-minutes-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, ['is_prbs_enabled', 'prbs_config_mode'], name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: found_at
                            
                            	Pattern first found at timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: found_count
                            
                            	Count of pattern found in interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: interval_index
                            
                            	Index of bucket, current and previous
                            	**type**\:   :py:class:`G709prbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsInterval>`
                            
                            .. attribute:: lost_at
                            
                            	Pattern first lost at timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: lost_count
                            
                            	Count of pattern lost in interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_pattern
                            
                            	Received Pattern of PRBS Test
                            	**type**\:   :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: start_at
                            
                            	Interval start timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: stop_at
                            
                            	Interval stop timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry, self).__init__()

                                self.yang_name = "prbs-entry"
                                self.yang_parent_name = "fifteen-minutes-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bit_error_count = YLeaf(YType.uint64, "bit-error-count")

                                self.configured_pattern = YLeaf(YType.enumeration, "configured-pattern")

                                self.found_at = YLeaf(YType.str, "found-at")

                                self.found_count = YLeaf(YType.uint64, "found-count")

                                self.interval_index = YLeaf(YType.enumeration, "interval-index")

                                self.lost_at = YLeaf(YType.str, "lost-at")

                                self.lost_count = YLeaf(YType.uint64, "lost-count")

                                self.received_pattern = YLeaf(YType.enumeration, "received-pattern")

                                self.start_at = YLeaf(YType.str, "start-at")

                                self.stop_at = YLeaf(YType.str, "stop-at")
                                self._segment_path = lambda: "prbs-entry"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry, ['bit_error_count', 'configured_pattern', 'found_at', 'found_count', 'interval_index', 'lost_at', 'lost_count', 'received_pattern', 'start_at', 'stop_at'], name, value)


                class TwentyFourHoursBucket(Entity):
                    """
                    Port 24\-hour PRBS statistics table
                    
                    .. attribute:: twenty_four_hours_statistics
                    
                    	Port 24\-hour PRBS statistics data
                    	**type**\:   :py:class:`TwentyFourHoursStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket, self).__init__()

                        self.yang_name = "twenty-four-hours-bucket"
                        self.yang_parent_name = "prbs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"twenty-four-hours-statistics" : ("twenty_four_hours_statistics", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics)}
                        self._child_list_classes = {}

                        self.twenty_four_hours_statistics = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics()
                        self.twenty_four_hours_statistics.parent = self
                        self._children_name_map["twenty_four_hours_statistics"] = "twenty-four-hours-statistics"
                        self._children_yang_names.add("twenty-four-hours-statistics")
                        self._segment_path = lambda: "twenty-four-hours-bucket"


                    class TwentyFourHoursStatistics(Entity):
                        """
                        Port 24\-hour PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of    :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, self).__init__()

                            self.yang_name = "twenty-four-hours-statistics"
                            self.yang_parent_name = "twenty-four-hours-bucket"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"prbs-entry" : ("prbs_entry", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry)}

                            self.is_prbs_enabled = YLeaf(YType.boolean, "is-prbs-enabled")

                            self.prbs_config_mode = YLeaf(YType.enumeration, "prbs-config-mode")

                            self.prbs_entry = YList(self)
                            self._segment_path = lambda: "twenty-four-hours-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, ['is_prbs_enabled', 'prbs_config_mode'], name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: found_at
                            
                            	Pattern first found at timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: found_count
                            
                            	Count of pattern found in interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: interval_index
                            
                            	Index of bucket, current and previous
                            	**type**\:   :py:class:`G709prbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsInterval>`
                            
                            .. attribute:: lost_at
                            
                            	Pattern first lost at timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: lost_count
                            
                            	Count of pattern lost in interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_pattern
                            
                            	Received Pattern of PRBS Test
                            	**type**\:   :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: start_at
                            
                            	Interval start timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: stop_at
                            
                            	Interval stop timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry, self).__init__()

                                self.yang_name = "prbs-entry"
                                self.yang_parent_name = "twenty-four-hours-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bit_error_count = YLeaf(YType.uint64, "bit-error-count")

                                self.configured_pattern = YLeaf(YType.enumeration, "configured-pattern")

                                self.found_at = YLeaf(YType.str, "found-at")

                                self.found_count = YLeaf(YType.uint64, "found-count")

                                self.interval_index = YLeaf(YType.enumeration, "interval-index")

                                self.lost_at = YLeaf(YType.str, "lost-at")

                                self.lost_count = YLeaf(YType.uint64, "lost-count")

                                self.received_pattern = YLeaf(YType.enumeration, "received-pattern")

                                self.start_at = YLeaf(YType.str, "start-at")

                                self.stop_at = YLeaf(YType.str, "stop-at")
                                self._segment_path = lambda: "prbs-entry"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry, ['bit_error_count', 'configured_pattern', 'found_at', 'found_count', 'interval_index', 'lost_at', 'lost_count', 'received_pattern', 'start_at', 'stop_at'], name, value)

    def clone_ptr(self):
        self._top_entity = Dwdm()
        return self._top_entity

class Vtxp(Entity):
    """
    vtxp
    
    .. attribute:: dwdm_vtxp
    
    	DWDM operational data
    	**type**\:   :py:class:`DwdmVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp>`
    
    

    """

    _prefix = 'dwdm-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vtxp, self).__init__()
        self._top_entity = None

        self.yang_name = "vtxp"
        self.yang_parent_name = "Cisco-IOS-XR-dwdm-ui-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"dwdm-vtxp" : ("dwdm_vtxp", Vtxp.DwdmVtxp)}
        self._child_list_classes = {}

        self.dwdm_vtxp = Vtxp.DwdmVtxp()
        self.dwdm_vtxp.parent = self
        self._children_name_map["dwdm_vtxp"] = "dwdm-vtxp"
        self._children_yang_names.add("dwdm-vtxp")
        self._segment_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp"


    class DwdmVtxp(Entity):
        """
        DWDM operational data
        
        .. attribute:: port_vtxps
        
        	All DWDM Port operational data
        	**type**\:   :py:class:`PortVtxps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vtxp.DwdmVtxp, self).__init__()

            self.yang_name = "dwdm-vtxp"
            self.yang_parent_name = "vtxp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"port-vtxps" : ("port_vtxps", Vtxp.DwdmVtxp.PortVtxps)}
            self._child_list_classes = {}

            self.port_vtxps = Vtxp.DwdmVtxp.PortVtxps()
            self.port_vtxps.parent = self
            self._children_name_map["port_vtxps"] = "port-vtxps"
            self._children_yang_names.add("port-vtxps")
            self._segment_path = lambda: "dwdm-vtxp"
            self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/%s" % self._segment_path()


        class PortVtxps(Entity):
            """
            All DWDM Port operational data
            
            .. attribute:: port_vtxp
            
            	DWDM Port operational data
            	**type**\: list of    :py:class:`PortVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps.PortVtxp>`
            
            

            """

            _prefix = 'dwdm-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vtxp.DwdmVtxp.PortVtxps, self).__init__()

                self.yang_name = "port-vtxps"
                self.yang_parent_name = "dwdm-vtxp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"port-vtxp" : ("port_vtxp", Vtxp.DwdmVtxp.PortVtxps.PortVtxp)}

                self.port_vtxp = YList(self)
                self._segment_path = lambda: "port-vtxps"
                self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps, [], name, value)


            class PortVtxp(Entity):
                """
                DWDM Port operational data
                
                .. attribute:: name  <key>
                
                	Port name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: info
                
                	DWDM port operational data
                	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, self).__init__()

                    self.yang_name = "port-vtxp"
                    self.yang_parent_name = "port-vtxps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"info" : ("info", Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.info = Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"
                    self._children_yang_names.add("info")
                    self._segment_path = lambda: "port-vtxp" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/port-vtxps/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, ['name'], name, value)


                class Info(Entity):
                    """
                    DWDM port operational data
                    
                    .. attribute:: vtxp_enable
                    
                    	Is VTXP attribute enabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "port-vtxp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.vtxp_enable = YLeaf(YType.boolean, "vtxp-enable")
                        self._segment_path = lambda: "info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, ['vtxp_enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Vtxp()
        return self._top_entity

