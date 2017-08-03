""" Cisco_IOS_XR_dwdm_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dwdm\-ui package operational data.

This module contains definitions
for the following management objects\:
  dwdm\: DWDM operational data
  vtxp\: vtxp

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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


class G709ApsByte(Enum):
    """
    G709ApsByte

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


class G709EfecMode(Enum):
    """
    G709EfecMode

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


class G709PpfsmMode(Enum):
    """
    G709PpfsmMode

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


class G709PpfsmState(Enum):
    """
    G709PpfsmState

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


class G709PpintfState(Enum):
    """
    G709PpintfState

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


class G709PrbsInterval(Enum):
    """
    G709PrbsInterval

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


class G709PrbsMode(Enum):
    """
    G709PrbsMode

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


class G709PrbsPattern(Enum):
    """
    G709PrbsPattern

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

        self.ports = Dwdm.Ports()
        self.ports.parent = self
        self._children_name_map["ports"] = "ports"
        self._children_yang_names.add("ports")


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

            self.port = YList(self)

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
                        super(Dwdm.Ports, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Dwdm.Ports, self).__setattr__(name, value)


        class Port(Entity):
            """
            DWDM Port operational data
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Dwdm.Ports.Port, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Dwdm.Ports.Port, self).__setattr__(name, value)


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

                    self.fifteen_minutes_bucket = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket()
                    self.fifteen_minutes_bucket.parent = self
                    self._children_name_map["fifteen_minutes_bucket"] = "fifteen-minutes-bucket"
                    self._children_yang_names.add("fifteen-minutes-bucket")

                    self.twenty_four_hours_bucket = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket()
                    self.twenty_four_hours_bucket.parent = self
                    self._children_name_map["twenty_four_hours_bucket"] = "twenty-four-hours-bucket"
                    self._children_yang_names.add("twenty-four-hours-bucket")


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

                        self.twenty_four_hours_statistics = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics()
                        self.twenty_four_hours_statistics.parent = self
                        self._children_name_map["twenty_four_hours_statistics"] = "twenty-four-hours-statistics"
                        self._children_yang_names.add("twenty-four-hours-statistics")


                    class TwentyFourHoursStatistics(Entity):
                        """
                        Port 24\-hour PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709PrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsMode>`
                        
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

                            self.is_prbs_enabled = YLeaf(YType.boolean, "is-prbs-enabled")

                            self.prbs_config_mode = YLeaf(YType.enumeration, "prbs-config-mode")

                            self.prbs_entry = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_prbs_enabled",
                                            "prbs_config_mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, self).__setattr__(name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709PrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPattern>`
                            
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
                            	**type**\:   :py:class:`G709PrbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsInterval>`
                            
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
                            	**type**\:   :py:class:`G709PrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPattern>`
                            
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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bit_error_count",
                                                "configured_pattern",
                                                "found_at",
                                                "found_count",
                                                "interval_index",
                                                "lost_at",
                                                "lost_count",
                                                "received_pattern",
                                                "start_at",
                                                "stop_at") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bit_error_count.is_set or
                                    self.configured_pattern.is_set or
                                    self.found_at.is_set or
                                    self.found_count.is_set or
                                    self.interval_index.is_set or
                                    self.lost_at.is_set or
                                    self.lost_count.is_set or
                                    self.received_pattern.is_set or
                                    self.start_at.is_set or
                                    self.stop_at.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bit_error_count.yfilter != YFilter.not_set or
                                    self.configured_pattern.yfilter != YFilter.not_set or
                                    self.found_at.yfilter != YFilter.not_set or
                                    self.found_count.yfilter != YFilter.not_set or
                                    self.interval_index.yfilter != YFilter.not_set or
                                    self.lost_at.yfilter != YFilter.not_set or
                                    self.lost_count.yfilter != YFilter.not_set or
                                    self.received_pattern.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.stop_at.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prbs-entry" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bit_error_count.is_set or self.bit_error_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bit_error_count.get_name_leafdata())
                                if (self.configured_pattern.is_set or self.configured_pattern.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.configured_pattern.get_name_leafdata())
                                if (self.found_at.is_set or self.found_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.found_at.get_name_leafdata())
                                if (self.found_count.is_set or self.found_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.found_count.get_name_leafdata())
                                if (self.interval_index.is_set or self.interval_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interval_index.get_name_leafdata())
                                if (self.lost_at.is_set or self.lost_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost_at.get_name_leafdata())
                                if (self.lost_count.is_set or self.lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost_count.get_name_leafdata())
                                if (self.received_pattern.is_set or self.received_pattern.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_pattern.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.stop_at.is_set or self.stop_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stop_at.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bit-error-count" or name == "configured-pattern" or name == "found-at" or name == "found-count" or name == "interval-index" or name == "lost-at" or name == "lost-count" or name == "received-pattern" or name == "start-at" or name == "stop-at"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bit-error-count"):
                                    self.bit_error_count = value
                                    self.bit_error_count.value_namespace = name_space
                                    self.bit_error_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "configured-pattern"):
                                    self.configured_pattern = value
                                    self.configured_pattern.value_namespace = name_space
                                    self.configured_pattern.value_namespace_prefix = name_space_prefix
                                if(value_path == "found-at"):
                                    self.found_at = value
                                    self.found_at.value_namespace = name_space
                                    self.found_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "found-count"):
                                    self.found_count = value
                                    self.found_count.value_namespace = name_space
                                    self.found_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "interval-index"):
                                    self.interval_index = value
                                    self.interval_index.value_namespace = name_space
                                    self.interval_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost-at"):
                                    self.lost_at = value
                                    self.lost_at.value_namespace = name_space
                                    self.lost_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost-count"):
                                    self.lost_count = value
                                    self.lost_count.value_namespace = name_space
                                    self.lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-pattern"):
                                    self.received_pattern = value
                                    self.received_pattern.value_namespace = name_space
                                    self.received_pattern.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "stop-at"):
                                    self.stop_at = value
                                    self.stop_at.value_namespace = name_space
                                    self.stop_at.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.prbs_entry:
                                if (c.has_data()):
                                    return True
                            return (
                                self.is_prbs_enabled.is_set or
                                self.prbs_config_mode.is_set)

                        def has_operation(self):
                            for c in self.prbs_entry:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_prbs_enabled.yfilter != YFilter.not_set or
                                self.prbs_config_mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "twenty-four-hours-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_prbs_enabled.is_set or self.is_prbs_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_prbs_enabled.get_name_leafdata())
                            if (self.prbs_config_mode.is_set or self.prbs_config_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prbs_config_mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "prbs-entry"):
                                for c in self.prbs_entry:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.prbs_entry.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prbs-entry" or name == "is-prbs-enabled" or name == "prbs-config-mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-prbs-enabled"):
                                self.is_prbs_enabled = value
                                self.is_prbs_enabled.value_namespace = name_space
                                self.is_prbs_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "prbs-config-mode"):
                                self.prbs_config_mode = value
                                self.prbs_config_mode.value_namespace = name_space
                                self.prbs_config_mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.twenty_four_hours_statistics is not None and self.twenty_four_hours_statistics.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.twenty_four_hours_statistics is not None and self.twenty_four_hours_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "twenty-four-hours-bucket" + path_buffer

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

                        if (child_yang_name == "twenty-four-hours-statistics"):
                            if (self.twenty_four_hours_statistics is None):
                                self.twenty_four_hours_statistics = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics()
                                self.twenty_four_hours_statistics.parent = self
                                self._children_name_map["twenty_four_hours_statistics"] = "twenty-four-hours-statistics"
                            return self.twenty_four_hours_statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "twenty-four-hours-statistics"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.fifteen_minutes_statistics = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics()
                        self.fifteen_minutes_statistics.parent = self
                        self._children_name_map["fifteen_minutes_statistics"] = "fifteen-minutes-statistics"
                        self._children_yang_names.add("fifteen-minutes-statistics")


                    class FifteenMinutesStatistics(Entity):
                        """
                        Port 15\-minute PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709PrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsMode>`
                        
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

                            self.is_prbs_enabled = YLeaf(YType.boolean, "is-prbs-enabled")

                            self.prbs_config_mode = YLeaf(YType.enumeration, "prbs-config-mode")

                            self.prbs_entry = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_prbs_enabled",
                                            "prbs_config_mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, self).__setattr__(name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709PrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPattern>`
                            
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
                            	**type**\:   :py:class:`G709PrbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsInterval>`
                            
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
                            	**type**\:   :py:class:`G709PrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPattern>`
                            
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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bit_error_count",
                                                "configured_pattern",
                                                "found_at",
                                                "found_count",
                                                "interval_index",
                                                "lost_at",
                                                "lost_count",
                                                "received_pattern",
                                                "start_at",
                                                "stop_at") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bit_error_count.is_set or
                                    self.configured_pattern.is_set or
                                    self.found_at.is_set or
                                    self.found_count.is_set or
                                    self.interval_index.is_set or
                                    self.lost_at.is_set or
                                    self.lost_count.is_set or
                                    self.received_pattern.is_set or
                                    self.start_at.is_set or
                                    self.stop_at.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bit_error_count.yfilter != YFilter.not_set or
                                    self.configured_pattern.yfilter != YFilter.not_set or
                                    self.found_at.yfilter != YFilter.not_set or
                                    self.found_count.yfilter != YFilter.not_set or
                                    self.interval_index.yfilter != YFilter.not_set or
                                    self.lost_at.yfilter != YFilter.not_set or
                                    self.lost_count.yfilter != YFilter.not_set or
                                    self.received_pattern.yfilter != YFilter.not_set or
                                    self.start_at.yfilter != YFilter.not_set or
                                    self.stop_at.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prbs-entry" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bit_error_count.is_set or self.bit_error_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bit_error_count.get_name_leafdata())
                                if (self.configured_pattern.is_set or self.configured_pattern.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.configured_pattern.get_name_leafdata())
                                if (self.found_at.is_set or self.found_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.found_at.get_name_leafdata())
                                if (self.found_count.is_set or self.found_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.found_count.get_name_leafdata())
                                if (self.interval_index.is_set or self.interval_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interval_index.get_name_leafdata())
                                if (self.lost_at.is_set or self.lost_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost_at.get_name_leafdata())
                                if (self.lost_count.is_set or self.lost_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lost_count.get_name_leafdata())
                                if (self.received_pattern.is_set or self.received_pattern.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_pattern.get_name_leafdata())
                                if (self.start_at.is_set or self.start_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_at.get_name_leafdata())
                                if (self.stop_at.is_set or self.stop_at.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stop_at.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bit-error-count" or name == "configured-pattern" or name == "found-at" or name == "found-count" or name == "interval-index" or name == "lost-at" or name == "lost-count" or name == "received-pattern" or name == "start-at" or name == "stop-at"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bit-error-count"):
                                    self.bit_error_count = value
                                    self.bit_error_count.value_namespace = name_space
                                    self.bit_error_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "configured-pattern"):
                                    self.configured_pattern = value
                                    self.configured_pattern.value_namespace = name_space
                                    self.configured_pattern.value_namespace_prefix = name_space_prefix
                                if(value_path == "found-at"):
                                    self.found_at = value
                                    self.found_at.value_namespace = name_space
                                    self.found_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "found-count"):
                                    self.found_count = value
                                    self.found_count.value_namespace = name_space
                                    self.found_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "interval-index"):
                                    self.interval_index = value
                                    self.interval_index.value_namespace = name_space
                                    self.interval_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost-at"):
                                    self.lost_at = value
                                    self.lost_at.value_namespace = name_space
                                    self.lost_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "lost-count"):
                                    self.lost_count = value
                                    self.lost_count.value_namespace = name_space
                                    self.lost_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-pattern"):
                                    self.received_pattern = value
                                    self.received_pattern.value_namespace = name_space
                                    self.received_pattern.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-at"):
                                    self.start_at = value
                                    self.start_at.value_namespace = name_space
                                    self.start_at.value_namespace_prefix = name_space_prefix
                                if(value_path == "stop-at"):
                                    self.stop_at = value
                                    self.stop_at.value_namespace = name_space
                                    self.stop_at.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.prbs_entry:
                                if (c.has_data()):
                                    return True
                            return (
                                self.is_prbs_enabled.is_set or
                                self.prbs_config_mode.is_set)

                        def has_operation(self):
                            for c in self.prbs_entry:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_prbs_enabled.yfilter != YFilter.not_set or
                                self.prbs_config_mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fifteen-minutes-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_prbs_enabled.is_set or self.is_prbs_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_prbs_enabled.get_name_leafdata())
                            if (self.prbs_config_mode.is_set or self.prbs_config_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prbs_config_mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "prbs-entry"):
                                for c in self.prbs_entry:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.prbs_entry.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prbs-entry" or name == "is-prbs-enabled" or name == "prbs-config-mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-prbs-enabled"):
                                self.is_prbs_enabled = value
                                self.is_prbs_enabled.value_namespace = name_space
                                self.is_prbs_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "prbs-config-mode"):
                                self.prbs_config_mode = value
                                self.prbs_config_mode.value_namespace = name_space
                                self.prbs_config_mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.fifteen_minutes_statistics is not None and self.fifteen_minutes_statistics.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.fifteen_minutes_statistics is not None and self.fifteen_minutes_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fifteen-minutes-bucket" + path_buffer

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

                        if (child_yang_name == "fifteen-minutes-statistics"):
                            if (self.fifteen_minutes_statistics is None):
                                self.fifteen_minutes_statistics = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics()
                                self.fifteen_minutes_statistics.parent = self
                                self._children_name_map["fifteen_minutes_statistics"] = "fifteen-minutes-statistics"
                            return self.fifteen_minutes_statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "fifteen-minutes-statistics"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.fifteen_minutes_bucket is not None and self.fifteen_minutes_bucket.has_data()) or
                        (self.twenty_four_hours_bucket is not None and self.twenty_four_hours_bucket.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.fifteen_minutes_bucket is not None and self.fifteen_minutes_bucket.has_operation()) or
                        (self.twenty_four_hours_bucket is not None and self.twenty_four_hours_bucket.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prbs" + path_buffer

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

                    if (child_yang_name == "fifteen-minutes-bucket"):
                        if (self.fifteen_minutes_bucket is None):
                            self.fifteen_minutes_bucket = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket()
                            self.fifteen_minutes_bucket.parent = self
                            self._children_name_map["fifteen_minutes_bucket"] = "fifteen-minutes-bucket"
                        return self.fifteen_minutes_bucket

                    if (child_yang_name == "twenty-four-hours-bucket"):
                        if (self.twenty_four_hours_bucket is None):
                            self.twenty_four_hours_bucket = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket()
                            self.twenty_four_hours_bucket.parent = self
                            self._children_name_map["twenty_four_hours_bucket"] = "twenty-four-hours-bucket"
                        return self.twenty_four_hours_bucket

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fifteen-minutes-bucket" or name == "twenty-four-hours-bucket"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.wave_info = Dwdm.Ports.Port.Optics.WaveInfo()
                    self.wave_info.parent = self
                    self._children_name_map["wave_info"] = "wave-info"
                    self._children_yang_names.add("wave-info")


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

                        self.wave_band = YLeaf(YType.uint32, "wave-band")

                        self.wave_channel_max = YLeaf(YType.uint32, "wave-channel-max")

                        self.wave_channel_min = YLeaf(YType.uint32, "wave-channel-min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("wave_band",
                                        "wave_channel_max",
                                        "wave_channel_min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Optics.WaveInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Optics.WaveInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.wave_band.is_set or
                            self.wave_channel_max.is_set or
                            self.wave_channel_min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.wave_band.yfilter != YFilter.not_set or
                            self.wave_channel_max.yfilter != YFilter.not_set or
                            self.wave_channel_min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "wave-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.wave_band.is_set or self.wave_band.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_band.get_name_leafdata())
                        if (self.wave_channel_max.is_set or self.wave_channel_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_channel_max.get_name_leafdata())
                        if (self.wave_channel_min.is_set or self.wave_channel_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_channel_min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "wave-band" or name == "wave-channel-max" or name == "wave-channel-min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "wave-band"):
                            self.wave_band = value
                            self.wave_band.value_namespace = name_space
                            self.wave_band.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-channel-max"):
                            self.wave_channel_max = value
                            self.wave_channel_max.value_namespace = name_space
                            self.wave_channel_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-channel-min"):
                            self.wave_channel_min = value
                            self.wave_channel_min.value_namespace = name_space
                            self.wave_channel_min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.wave_info is not None and self.wave_info.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.wave_info is not None and self.wave_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optics" + path_buffer

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

                    if (child_yang_name == "wave-info"):
                        if (self.wave_info is None):
                            self.wave_info = Dwdm.Ports.Port.Optics.WaveInfo()
                            self.wave_info.parent = self
                            self._children_name_map["wave_info"] = "wave-info"
                        return self.wave_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "wave-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("controller_state",
                                    "slice_state",
                                    "transport_admin_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dwdm.Ports.Port.Info, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dwdm.Ports.Port.Info, self).__setattr__(name, value)


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
                    	**type**\:   :py:class:`G709EfecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709EfecMode>`
                    
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
                    	**type**\:   :py:class:`G709PrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsMode>`
                    
                    .. attribute:: g709_prbs_pattern
                    
                    	Pattern of PRBS Test
                    	**type**\:   :py:class:`G709PrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPattern>`
                    
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ec",
                                        "ec_accum",
                                        "efec_mode",
                                        "fe_cstr",
                                        "fec_ber",
                                        "fec_ber_man",
                                        "fec_mode",
                                        "g709_prbs_mode",
                                        "g709_prbs_pattern",
                                        "is_fec_mode_default",
                                        "is_g709_enabled",
                                        "is_prbs_enabled",
                                        "loopback_mode",
                                        "network_conn_id",
                                        "network_port_id",
                                        "prbs_time_stamp",
                                        "q",
                                        "q_margin",
                                        "qmargin_str",
                                        "qstr",
                                        "remote_fec_mode",
                                        "uc") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.G709Info, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.G709Info, self).__setattr__(name, value)


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
                                        super(Dwdm.Ports.Port.Info.G709Info.FecMismatch, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Info.G709Info.FecMismatch, self).__setattr__(name, value)

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

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                            self.threshold = YLeaf(YType.int32, "threshold")

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
                                            "reporting_enabled",
                                            "threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Info.G709Info.EcTca, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Info.G709Info.EcTca, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set or
                                self.threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set or
                                self.threshold.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ec-tca" + path_buffer

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
                            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                            if(value_path == "threshold"):
                                self.threshold = value
                                self.threshold.value_namespace = name_space
                                self.threshold.value_namespace_prefix = name_space_prefix


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

                            self.counter = YLeaf(YType.uint64, "counter")

                            self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                            self.is_detected = YLeaf(YType.boolean, "is-detected")

                            self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                            self.threshold = YLeaf(YType.int32, "threshold")

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
                                            "reporting_enabled",
                                            "threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Info.G709Info.UcTca, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Info.G709Info.UcTca, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.counter.is_set or
                                self.is_asserted.is_set or
                                self.is_detected.is_set or
                                self.reporting_enabled.is_set or
                                self.threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.counter.yfilter != YFilter.not_set or
                                self.is_asserted.yfilter != YFilter.not_set or
                                self.is_detected.yfilter != YFilter.not_set or
                                self.reporting_enabled.yfilter != YFilter.not_set or
                                self.threshold.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "uc-tca" + path_buffer

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
                            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                            if(value_path == "threshold"):
                                self.threshold = value
                                self.threshold.value_namespace = name_space
                                self.threshold.value_namespace_prefix = name_space_prefix


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bei",
                                            "bip") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Info.G709Info.OtuInfo, self).__setattr__(name, value)


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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, self).__setattr__(name, value)

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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefec-sf-ber" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefec-sd-ber" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bbe-tca" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "es-tca" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bbe" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "es" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ses" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "uas" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fc" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bber" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "esr" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sesr" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("exp_dapi_range",
                                                "exp_oper_spec_range",
                                                "exp_sapi_range",
                                                "expected_dapi",
                                                "expected_dapi0",
                                                "expected_oper_spec",
                                                "expected_sapi",
                                                "expected_sapi0",
                                                "expected_string_type",
                                                "expected_tti",
                                                "rx_dapi",
                                                "rx_dapi0",
                                                "rx_dapi_range",
                                                "rx_oper_spec",
                                                "rx_oper_spec_range",
                                                "rx_sapi",
                                                "rx_sapi0",
                                                "rx_sapi_range",
                                                "rx_string_type",
                                                "rx_tti",
                                                "tx_dapi",
                                                "tx_dapi0",
                                                "tx_dapi_range",
                                                "tx_oper_spec",
                                                "tx_oper_spec_range",
                                                "tx_sapi",
                                                "tx_sapi0",
                                                "tx_sapi_range",
                                                "tx_string_type",
                                                "tx_tti") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.exp_dapi_range.is_set or
                                    self.exp_oper_spec_range.is_set or
                                    self.exp_sapi_range.is_set or
                                    self.expected_dapi.is_set or
                                    self.expected_dapi0.is_set or
                                    self.expected_oper_spec.is_set or
                                    self.expected_sapi.is_set or
                                    self.expected_sapi0.is_set or
                                    self.expected_string_type.is_set or
                                    self.expected_tti.is_set or
                                    self.rx_dapi.is_set or
                                    self.rx_dapi0.is_set or
                                    self.rx_dapi_range.is_set or
                                    self.rx_oper_spec.is_set or
                                    self.rx_oper_spec_range.is_set or
                                    self.rx_sapi.is_set or
                                    self.rx_sapi0.is_set or
                                    self.rx_sapi_range.is_set or
                                    self.rx_string_type.is_set or
                                    self.rx_tti.is_set or
                                    self.tx_dapi.is_set or
                                    self.tx_dapi0.is_set or
                                    self.tx_dapi_range.is_set or
                                    self.tx_oper_spec.is_set or
                                    self.tx_oper_spec_range.is_set or
                                    self.tx_sapi.is_set or
                                    self.tx_sapi0.is_set or
                                    self.tx_sapi_range.is_set or
                                    self.tx_string_type.is_set or
                                    self.tx_tti.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.exp_dapi_range.yfilter != YFilter.not_set or
                                    self.exp_oper_spec_range.yfilter != YFilter.not_set or
                                    self.exp_sapi_range.yfilter != YFilter.not_set or
                                    self.expected_dapi.yfilter != YFilter.not_set or
                                    self.expected_dapi0.yfilter != YFilter.not_set or
                                    self.expected_oper_spec.yfilter != YFilter.not_set or
                                    self.expected_sapi.yfilter != YFilter.not_set or
                                    self.expected_sapi0.yfilter != YFilter.not_set or
                                    self.expected_string_type.yfilter != YFilter.not_set or
                                    self.expected_tti.yfilter != YFilter.not_set or
                                    self.rx_dapi.yfilter != YFilter.not_set or
                                    self.rx_dapi0.yfilter != YFilter.not_set or
                                    self.rx_dapi_range.yfilter != YFilter.not_set or
                                    self.rx_oper_spec.yfilter != YFilter.not_set or
                                    self.rx_oper_spec_range.yfilter != YFilter.not_set or
                                    self.rx_sapi.yfilter != YFilter.not_set or
                                    self.rx_sapi0.yfilter != YFilter.not_set or
                                    self.rx_sapi_range.yfilter != YFilter.not_set or
                                    self.rx_string_type.yfilter != YFilter.not_set or
                                    self.rx_tti.yfilter != YFilter.not_set or
                                    self.tx_dapi.yfilter != YFilter.not_set or
                                    self.tx_dapi0.yfilter != YFilter.not_set or
                                    self.tx_dapi_range.yfilter != YFilter.not_set or
                                    self.tx_oper_spec.yfilter != YFilter.not_set or
                                    self.tx_oper_spec_range.yfilter != YFilter.not_set or
                                    self.tx_sapi.yfilter != YFilter.not_set or
                                    self.tx_sapi0.yfilter != YFilter.not_set or
                                    self.tx_sapi_range.yfilter != YFilter.not_set or
                                    self.tx_string_type.yfilter != YFilter.not_set or
                                    self.tx_tti.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tti" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.exp_dapi_range.is_set or self.exp_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_dapi_range.get_name_leafdata())
                                if (self.exp_oper_spec_range.is_set or self.exp_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_oper_spec_range.get_name_leafdata())
                                if (self.exp_sapi_range.is_set or self.exp_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_sapi_range.get_name_leafdata())
                                if (self.expected_dapi.is_set or self.expected_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_dapi.get_name_leafdata())
                                if (self.expected_dapi0.is_set or self.expected_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_dapi0.get_name_leafdata())
                                if (self.expected_oper_spec.is_set or self.expected_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_oper_spec.get_name_leafdata())
                                if (self.expected_sapi.is_set or self.expected_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_sapi.get_name_leafdata())
                                if (self.expected_sapi0.is_set or self.expected_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_sapi0.get_name_leafdata())
                                if (self.expected_string_type.is_set or self.expected_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_string_type.get_name_leafdata())
                                if (self.expected_tti.is_set or self.expected_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_tti.get_name_leafdata())
                                if (self.rx_dapi.is_set or self.rx_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi.get_name_leafdata())
                                if (self.rx_dapi0.is_set or self.rx_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi0.get_name_leafdata())
                                if (self.rx_dapi_range.is_set or self.rx_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi_range.get_name_leafdata())
                                if (self.rx_oper_spec.is_set or self.rx_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_oper_spec.get_name_leafdata())
                                if (self.rx_oper_spec_range.is_set or self.rx_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_oper_spec_range.get_name_leafdata())
                                if (self.rx_sapi.is_set or self.rx_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi.get_name_leafdata())
                                if (self.rx_sapi0.is_set or self.rx_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi0.get_name_leafdata())
                                if (self.rx_sapi_range.is_set or self.rx_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi_range.get_name_leafdata())
                                if (self.rx_string_type.is_set or self.rx_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_string_type.get_name_leafdata())
                                if (self.rx_tti.is_set or self.rx_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tti.get_name_leafdata())
                                if (self.tx_dapi.is_set or self.tx_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi.get_name_leafdata())
                                if (self.tx_dapi0.is_set or self.tx_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi0.get_name_leafdata())
                                if (self.tx_dapi_range.is_set or self.tx_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi_range.get_name_leafdata())
                                if (self.tx_oper_spec.is_set or self.tx_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_oper_spec.get_name_leafdata())
                                if (self.tx_oper_spec_range.is_set or self.tx_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_oper_spec_range.get_name_leafdata())
                                if (self.tx_sapi.is_set or self.tx_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi.get_name_leafdata())
                                if (self.tx_sapi0.is_set or self.tx_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi0.get_name_leafdata())
                                if (self.tx_sapi_range.is_set or self.tx_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi_range.get_name_leafdata())
                                if (self.tx_string_type.is_set or self.tx_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_string_type.get_name_leafdata())
                                if (self.tx_tti.is_set or self.tx_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_tti.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exp-dapi-range" or name == "exp-oper-spec-range" or name == "exp-sapi-range" or name == "expected-dapi" or name == "expected-dapi0" or name == "expected-oper-spec" or name == "expected-sapi" or name == "expected-sapi0" or name == "expected-string-type" or name == "expected-tti" or name == "rx-dapi" or name == "rx-dapi0" or name == "rx-dapi-range" or name == "rx-oper-spec" or name == "rx-oper-spec-range" or name == "rx-sapi" or name == "rx-sapi0" or name == "rx-sapi-range" or name == "rx-string-type" or name == "rx-tti" or name == "tx-dapi" or name == "tx-dapi0" or name == "tx-dapi-range" or name == "tx-oper-spec" or name == "tx-oper-spec-range" or name == "tx-sapi" or name == "tx-sapi0" or name == "tx-sapi-range" or name == "tx-string-type" or name == "tx-tti"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "exp-dapi-range"):
                                    self.exp_dapi_range = value
                                    self.exp_dapi_range.value_namespace = name_space
                                    self.exp_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "exp-oper-spec-range"):
                                    self.exp_oper_spec_range = value
                                    self.exp_oper_spec_range.value_namespace = name_space
                                    self.exp_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "exp-sapi-range"):
                                    self.exp_sapi_range = value
                                    self.exp_sapi_range.value_namespace = name_space
                                    self.exp_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-dapi"):
                                    self.expected_dapi = value
                                    self.expected_dapi.value_namespace = name_space
                                    self.expected_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-dapi0"):
                                    self.expected_dapi0 = value
                                    self.expected_dapi0.value_namespace = name_space
                                    self.expected_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-oper-spec"):
                                    self.expected_oper_spec = value
                                    self.expected_oper_spec.value_namespace = name_space
                                    self.expected_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-sapi"):
                                    self.expected_sapi = value
                                    self.expected_sapi.value_namespace = name_space
                                    self.expected_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-sapi0"):
                                    self.expected_sapi0 = value
                                    self.expected_sapi0.value_namespace = name_space
                                    self.expected_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-string-type"):
                                    self.expected_string_type = value
                                    self.expected_string_type.value_namespace = name_space
                                    self.expected_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-tti"):
                                    self.expected_tti = value
                                    self.expected_tti.value_namespace = name_space
                                    self.expected_tti.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi"):
                                    self.rx_dapi = value
                                    self.rx_dapi.value_namespace = name_space
                                    self.rx_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi0"):
                                    self.rx_dapi0 = value
                                    self.rx_dapi0.value_namespace = name_space
                                    self.rx_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi-range"):
                                    self.rx_dapi_range = value
                                    self.rx_dapi_range.value_namespace = name_space
                                    self.rx_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-oper-spec"):
                                    self.rx_oper_spec = value
                                    self.rx_oper_spec.value_namespace = name_space
                                    self.rx_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-oper-spec-range"):
                                    self.rx_oper_spec_range = value
                                    self.rx_oper_spec_range.value_namespace = name_space
                                    self.rx_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi"):
                                    self.rx_sapi = value
                                    self.rx_sapi.value_namespace = name_space
                                    self.rx_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi0"):
                                    self.rx_sapi0 = value
                                    self.rx_sapi0.value_namespace = name_space
                                    self.rx_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi-range"):
                                    self.rx_sapi_range = value
                                    self.rx_sapi_range.value_namespace = name_space
                                    self.rx_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-string-type"):
                                    self.rx_string_type = value
                                    self.rx_string_type.value_namespace = name_space
                                    self.rx_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tti"):
                                    self.rx_tti = value
                                    self.rx_tti.value_namespace = name_space
                                    self.rx_tti.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi"):
                                    self.tx_dapi = value
                                    self.tx_dapi.value_namespace = name_space
                                    self.tx_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi0"):
                                    self.tx_dapi0 = value
                                    self.tx_dapi0.value_namespace = name_space
                                    self.tx_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi-range"):
                                    self.tx_dapi_range = value
                                    self.tx_dapi_range.value_namespace = name_space
                                    self.tx_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-oper-spec"):
                                    self.tx_oper_spec = value
                                    self.tx_oper_spec.value_namespace = name_space
                                    self.tx_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-oper-spec-range"):
                                    self.tx_oper_spec_range = value
                                    self.tx_oper_spec_range.value_namespace = name_space
                                    self.tx_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi"):
                                    self.tx_sapi = value
                                    self.tx_sapi.value_namespace = name_space
                                    self.tx_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi0"):
                                    self.tx_sapi0 = value
                                    self.tx_sapi0.value_namespace = name_space
                                    self.tx_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi-range"):
                                    self.tx_sapi_range = value
                                    self.tx_sapi_range.value_namespace = name_space
                                    self.tx_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-string-type"):
                                    self.tx_string_type = value
                                    self.tx_string_type.value_namespace = name_space
                                    self.tx_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-tti"):
                                    self.tx_tti = value
                                    self.tx_tti.value_namespace = name_space
                                    self.tx_tti.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.bei.is_set or
                                self.bip.is_set or
                                (self.ais is not None and self.ais.has_data()) or
                                (self.bbe is not None and self.bbe.has_data()) or
                                (self.bbe_tca is not None and self.bbe_tca.has_data()) or
                                (self.bber is not None and self.bber.has_data()) or
                                (self.bdi is not None and self.bdi.has_data()) or
                                (self.eoc is not None and self.eoc.has_data()) or
                                (self.es is not None and self.es.has_data()) or
                                (self.es_tca is not None and self.es_tca.has_data()) or
                                (self.esr is not None and self.esr.has_data()) or
                                (self.fc is not None and self.fc.has_data()) or
                                (self.iae is not None and self.iae.has_data()) or
                                (self.lof is not None and self.lof.has_data()) or
                                (self.lom is not None and self.lom.has_data()) or
                                (self.los is not None and self.los.has_data()) or
                                (self.oof is not None and self.oof.has_data()) or
                                (self.oom is not None and self.oom.has_data()) or
                                (self.prefec_sd_ber is not None and self.prefec_sd_ber.has_data()) or
                                (self.prefec_sf_ber is not None and self.prefec_sf_ber.has_data()) or
                                (self.sd_ber is not None and self.sd_ber.has_data()) or
                                (self.ses is not None and self.ses.has_data()) or
                                (self.sesr is not None and self.sesr.has_data()) or
                                (self.sf_ber is not None and self.sf_ber.has_data()) or
                                (self.tim is not None and self.tim.has_data()) or
                                (self.tti is not None and self.tti.has_data()) or
                                (self.uas is not None and self.uas.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bei.yfilter != YFilter.not_set or
                                self.bip.yfilter != YFilter.not_set or
                                (self.ais is not None and self.ais.has_operation()) or
                                (self.bbe is not None and self.bbe.has_operation()) or
                                (self.bbe_tca is not None and self.bbe_tca.has_operation()) or
                                (self.bber is not None and self.bber.has_operation()) or
                                (self.bdi is not None and self.bdi.has_operation()) or
                                (self.eoc is not None and self.eoc.has_operation()) or
                                (self.es is not None and self.es.has_operation()) or
                                (self.es_tca is not None and self.es_tca.has_operation()) or
                                (self.esr is not None and self.esr.has_operation()) or
                                (self.fc is not None and self.fc.has_operation()) or
                                (self.iae is not None and self.iae.has_operation()) or
                                (self.lof is not None and self.lof.has_operation()) or
                                (self.lom is not None and self.lom.has_operation()) or
                                (self.los is not None and self.los.has_operation()) or
                                (self.oof is not None and self.oof.has_operation()) or
                                (self.oom is not None and self.oom.has_operation()) or
                                (self.prefec_sd_ber is not None and self.prefec_sd_ber.has_operation()) or
                                (self.prefec_sf_ber is not None and self.prefec_sf_ber.has_operation()) or
                                (self.sd_ber is not None and self.sd_ber.has_operation()) or
                                (self.ses is not None and self.ses.has_operation()) or
                                (self.sesr is not None and self.sesr.has_operation()) or
                                (self.sf_ber is not None and self.sf_ber.has_operation()) or
                                (self.tim is not None and self.tim.has_operation()) or
                                (self.tti is not None and self.tti.has_operation()) or
                                (self.uas is not None and self.uas.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "otu-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bei.is_set or self.bei.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bei.get_name_leafdata())
                            if (self.bip.is_set or self.bip.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bip.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ais"):
                                if (self.ais is None):
                                    self.ais = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais()
                                    self.ais.parent = self
                                    self._children_name_map["ais"] = "ais"
                                return self.ais

                            if (child_yang_name == "bbe"):
                                if (self.bbe is None):
                                    self.bbe = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe()
                                    self.bbe.parent = self
                                    self._children_name_map["bbe"] = "bbe"
                                return self.bbe

                            if (child_yang_name == "bbe-tca"):
                                if (self.bbe_tca is None):
                                    self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca()
                                    self.bbe_tca.parent = self
                                    self._children_name_map["bbe_tca"] = "bbe-tca"
                                return self.bbe_tca

                            if (child_yang_name == "bber"):
                                if (self.bber is None):
                                    self.bber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber()
                                    self.bber.parent = self
                                    self._children_name_map["bber"] = "bber"
                                return self.bber

                            if (child_yang_name == "bdi"):
                                if (self.bdi is None):
                                    self.bdi = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi()
                                    self.bdi.parent = self
                                    self._children_name_map["bdi"] = "bdi"
                                return self.bdi

                            if (child_yang_name == "eoc"):
                                if (self.eoc is None):
                                    self.eoc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc()
                                    self.eoc.parent = self
                                    self._children_name_map["eoc"] = "eoc"
                                return self.eoc

                            if (child_yang_name == "es"):
                                if (self.es is None):
                                    self.es = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es()
                                    self.es.parent = self
                                    self._children_name_map["es"] = "es"
                                return self.es

                            if (child_yang_name == "es-tca"):
                                if (self.es_tca is None):
                                    self.es_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca()
                                    self.es_tca.parent = self
                                    self._children_name_map["es_tca"] = "es-tca"
                                return self.es_tca

                            if (child_yang_name == "esr"):
                                if (self.esr is None):
                                    self.esr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr()
                                    self.esr.parent = self
                                    self._children_name_map["esr"] = "esr"
                                return self.esr

                            if (child_yang_name == "fc"):
                                if (self.fc is None):
                                    self.fc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc()
                                    self.fc.parent = self
                                    self._children_name_map["fc"] = "fc"
                                return self.fc

                            if (child_yang_name == "iae"):
                                if (self.iae is None):
                                    self.iae = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae()
                                    self.iae.parent = self
                                    self._children_name_map["iae"] = "iae"
                                return self.iae

                            if (child_yang_name == "lof"):
                                if (self.lof is None):
                                    self.lof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof()
                                    self.lof.parent = self
                                    self._children_name_map["lof"] = "lof"
                                return self.lof

                            if (child_yang_name == "lom"):
                                if (self.lom is None):
                                    self.lom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom()
                                    self.lom.parent = self
                                    self._children_name_map["lom"] = "lom"
                                return self.lom

                            if (child_yang_name == "los"):
                                if (self.los is None):
                                    self.los = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los()
                                    self.los.parent = self
                                    self._children_name_map["los"] = "los"
                                return self.los

                            if (child_yang_name == "oof"):
                                if (self.oof is None):
                                    self.oof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof()
                                    self.oof.parent = self
                                    self._children_name_map["oof"] = "oof"
                                return self.oof

                            if (child_yang_name == "oom"):
                                if (self.oom is None):
                                    self.oom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom()
                                    self.oom.parent = self
                                    self._children_name_map["oom"] = "oom"
                                return self.oom

                            if (child_yang_name == "prefec-sd-ber"):
                                if (self.prefec_sd_ber is None):
                                    self.prefec_sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer()
                                    self.prefec_sd_ber.parent = self
                                    self._children_name_map["prefec_sd_ber"] = "prefec-sd-ber"
                                return self.prefec_sd_ber

                            if (child_yang_name == "prefec-sf-ber"):
                                if (self.prefec_sf_ber is None):
                                    self.prefec_sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer()
                                    self.prefec_sf_ber.parent = self
                                    self._children_name_map["prefec_sf_ber"] = "prefec-sf-ber"
                                return self.prefec_sf_ber

                            if (child_yang_name == "sd-ber"):
                                if (self.sd_ber is None):
                                    self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer()
                                    self.sd_ber.parent = self
                                    self._children_name_map["sd_ber"] = "sd-ber"
                                return self.sd_ber

                            if (child_yang_name == "ses"):
                                if (self.ses is None):
                                    self.ses = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses()
                                    self.ses.parent = self
                                    self._children_name_map["ses"] = "ses"
                                return self.ses

                            if (child_yang_name == "sesr"):
                                if (self.sesr is None):
                                    self.sesr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr()
                                    self.sesr.parent = self
                                    self._children_name_map["sesr"] = "sesr"
                                return self.sesr

                            if (child_yang_name == "sf-ber"):
                                if (self.sf_ber is None):
                                    self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer()
                                    self.sf_ber.parent = self
                                    self._children_name_map["sf_ber"] = "sf-ber"
                                return self.sf_ber

                            if (child_yang_name == "tim"):
                                if (self.tim is None):
                                    self.tim = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim()
                                    self.tim.parent = self
                                    self._children_name_map["tim"] = "tim"
                                return self.tim

                            if (child_yang_name == "tti"):
                                if (self.tti is None):
                                    self.tti = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti()
                                    self.tti.parent = self
                                    self._children_name_map["tti"] = "tti"
                                return self.tti

                            if (child_yang_name == "uas"):
                                if (self.uas is None):
                                    self.uas = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas()
                                    self.uas.parent = self
                                    self._children_name_map["uas"] = "uas"
                                return self.uas

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ais" or name == "bbe" or name == "bbe-tca" or name == "bber" or name == "bdi" or name == "eoc" or name == "es" or name == "es-tca" or name == "esr" or name == "fc" or name == "iae" or name == "lof" or name == "lom" or name == "los" or name == "oof" or name == "oom" or name == "prefec-sd-ber" or name == "prefec-sf-ber" or name == "sd-ber" or name == "ses" or name == "sesr" or name == "sf-ber" or name == "tim" or name == "tti" or name == "uas" or name == "bei" or name == "bip"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bei"):
                                self.bei = value
                                self.bei.value_namespace = name_space
                                self.bei.value_namespace_prefix = name_space_prefix
                            if(value_path == "bip"):
                                self.bip = value
                                self.bip.value_namespace = name_space
                                self.bip.value_namespace_prefix = name_space_prefix


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bei",
                                            "bip") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dwdm.Ports.Port.Info.G709Info.OduInfo, self).__setattr__(name, value)


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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, self).__setattr__(name, value)

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
                                path_buffer = "oci" + path_buffer

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, self).__setattr__(name, value)

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
                                path_buffer = "lck" + path_buffer

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, self).__setattr__(name, value)

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, self).__setattr__(name, value)

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
                                path_buffer = "ptim" + path_buffer

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
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, self).__setattr__(name, value)

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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bbe-tca" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                                self.is_asserted = YLeaf(YType.boolean, "is-asserted")

                                self.is_detected = YLeaf(YType.boolean, "is-detected")

                                self.reporting_enabled = YLeaf(YType.boolean, "reporting-enabled")

                                self.threshold = YLeaf(YType.int32, "threshold")

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
                                                "reporting_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.counter.is_set or
                                    self.is_asserted.is_set or
                                    self.is_detected.is_set or
                                    self.reporting_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set or
                                    self.is_asserted.yfilter != YFilter.not_set or
                                    self.is_detected.yfilter != YFilter.not_set or
                                    self.reporting_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "es-tca" + path_buffer

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
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter" or name == "is-asserted" or name == "is-detected" or name == "reporting-enabled" or name == "threshold"):
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
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bbe" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Es, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Es, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "es" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ses" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "uas" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fc" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bber" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "esr" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                                self.counter = YLeaf(YType.uint64, "counter")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("counter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr, self).__setattr__(name, value)

                            def has_data(self):
                                return self.counter.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.counter.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sesr" + path_buffer

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "counter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "counter"):
                                    self.counter = value
                                    self.counter.value_namespace = name_space
                                    self.counter.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("exp_dapi_range",
                                                "exp_oper_spec_range",
                                                "exp_sapi_range",
                                                "expected_dapi",
                                                "expected_dapi0",
                                                "expected_oper_spec",
                                                "expected_sapi",
                                                "expected_sapi0",
                                                "expected_string_type",
                                                "expected_tti",
                                                "rx_dapi",
                                                "rx_dapi0",
                                                "rx_dapi_range",
                                                "rx_oper_spec",
                                                "rx_oper_spec_range",
                                                "rx_sapi",
                                                "rx_sapi0",
                                                "rx_sapi_range",
                                                "rx_string_type",
                                                "rx_tti",
                                                "tx_dapi",
                                                "tx_dapi0",
                                                "tx_dapi_range",
                                                "tx_oper_spec",
                                                "tx_oper_spec_range",
                                                "tx_sapi",
                                                "tx_sapi0",
                                                "tx_sapi_range",
                                                "tx_string_type",
                                                "tx_tti") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.exp_dapi_range.is_set or
                                    self.exp_oper_spec_range.is_set or
                                    self.exp_sapi_range.is_set or
                                    self.expected_dapi.is_set or
                                    self.expected_dapi0.is_set or
                                    self.expected_oper_spec.is_set or
                                    self.expected_sapi.is_set or
                                    self.expected_sapi0.is_set or
                                    self.expected_string_type.is_set or
                                    self.expected_tti.is_set or
                                    self.rx_dapi.is_set or
                                    self.rx_dapi0.is_set or
                                    self.rx_dapi_range.is_set or
                                    self.rx_oper_spec.is_set or
                                    self.rx_oper_spec_range.is_set or
                                    self.rx_sapi.is_set or
                                    self.rx_sapi0.is_set or
                                    self.rx_sapi_range.is_set or
                                    self.rx_string_type.is_set or
                                    self.rx_tti.is_set or
                                    self.tx_dapi.is_set or
                                    self.tx_dapi0.is_set or
                                    self.tx_dapi_range.is_set or
                                    self.tx_oper_spec.is_set or
                                    self.tx_oper_spec_range.is_set or
                                    self.tx_sapi.is_set or
                                    self.tx_sapi0.is_set or
                                    self.tx_sapi_range.is_set or
                                    self.tx_string_type.is_set or
                                    self.tx_tti.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.exp_dapi_range.yfilter != YFilter.not_set or
                                    self.exp_oper_spec_range.yfilter != YFilter.not_set or
                                    self.exp_sapi_range.yfilter != YFilter.not_set or
                                    self.expected_dapi.yfilter != YFilter.not_set or
                                    self.expected_dapi0.yfilter != YFilter.not_set or
                                    self.expected_oper_spec.yfilter != YFilter.not_set or
                                    self.expected_sapi.yfilter != YFilter.not_set or
                                    self.expected_sapi0.yfilter != YFilter.not_set or
                                    self.expected_string_type.yfilter != YFilter.not_set or
                                    self.expected_tti.yfilter != YFilter.not_set or
                                    self.rx_dapi.yfilter != YFilter.not_set or
                                    self.rx_dapi0.yfilter != YFilter.not_set or
                                    self.rx_dapi_range.yfilter != YFilter.not_set or
                                    self.rx_oper_spec.yfilter != YFilter.not_set or
                                    self.rx_oper_spec_range.yfilter != YFilter.not_set or
                                    self.rx_sapi.yfilter != YFilter.not_set or
                                    self.rx_sapi0.yfilter != YFilter.not_set or
                                    self.rx_sapi_range.yfilter != YFilter.not_set or
                                    self.rx_string_type.yfilter != YFilter.not_set or
                                    self.rx_tti.yfilter != YFilter.not_set or
                                    self.tx_dapi.yfilter != YFilter.not_set or
                                    self.tx_dapi0.yfilter != YFilter.not_set or
                                    self.tx_dapi_range.yfilter != YFilter.not_set or
                                    self.tx_oper_spec.yfilter != YFilter.not_set or
                                    self.tx_oper_spec_range.yfilter != YFilter.not_set or
                                    self.tx_sapi.yfilter != YFilter.not_set or
                                    self.tx_sapi0.yfilter != YFilter.not_set or
                                    self.tx_sapi_range.yfilter != YFilter.not_set or
                                    self.tx_string_type.yfilter != YFilter.not_set or
                                    self.tx_tti.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tti" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.exp_dapi_range.is_set or self.exp_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_dapi_range.get_name_leafdata())
                                if (self.exp_oper_spec_range.is_set or self.exp_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_oper_spec_range.get_name_leafdata())
                                if (self.exp_sapi_range.is_set or self.exp_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exp_sapi_range.get_name_leafdata())
                                if (self.expected_dapi.is_set or self.expected_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_dapi.get_name_leafdata())
                                if (self.expected_dapi0.is_set or self.expected_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_dapi0.get_name_leafdata())
                                if (self.expected_oper_spec.is_set or self.expected_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_oper_spec.get_name_leafdata())
                                if (self.expected_sapi.is_set or self.expected_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_sapi.get_name_leafdata())
                                if (self.expected_sapi0.is_set or self.expected_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_sapi0.get_name_leafdata())
                                if (self.expected_string_type.is_set or self.expected_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_string_type.get_name_leafdata())
                                if (self.expected_tti.is_set or self.expected_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.expected_tti.get_name_leafdata())
                                if (self.rx_dapi.is_set or self.rx_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi.get_name_leafdata())
                                if (self.rx_dapi0.is_set or self.rx_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi0.get_name_leafdata())
                                if (self.rx_dapi_range.is_set or self.rx_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_dapi_range.get_name_leafdata())
                                if (self.rx_oper_spec.is_set or self.rx_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_oper_spec.get_name_leafdata())
                                if (self.rx_oper_spec_range.is_set or self.rx_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_oper_spec_range.get_name_leafdata())
                                if (self.rx_sapi.is_set or self.rx_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi.get_name_leafdata())
                                if (self.rx_sapi0.is_set or self.rx_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi0.get_name_leafdata())
                                if (self.rx_sapi_range.is_set or self.rx_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_sapi_range.get_name_leafdata())
                                if (self.rx_string_type.is_set or self.rx_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_string_type.get_name_leafdata())
                                if (self.rx_tti.is_set or self.rx_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_tti.get_name_leafdata())
                                if (self.tx_dapi.is_set or self.tx_dapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi.get_name_leafdata())
                                if (self.tx_dapi0.is_set or self.tx_dapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi0.get_name_leafdata())
                                if (self.tx_dapi_range.is_set or self.tx_dapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_dapi_range.get_name_leafdata())
                                if (self.tx_oper_spec.is_set or self.tx_oper_spec.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_oper_spec.get_name_leafdata())
                                if (self.tx_oper_spec_range.is_set or self.tx_oper_spec_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_oper_spec_range.get_name_leafdata())
                                if (self.tx_sapi.is_set or self.tx_sapi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi.get_name_leafdata())
                                if (self.tx_sapi0.is_set or self.tx_sapi0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi0.get_name_leafdata())
                                if (self.tx_sapi_range.is_set or self.tx_sapi_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_sapi_range.get_name_leafdata())
                                if (self.tx_string_type.is_set or self.tx_string_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_string_type.get_name_leafdata())
                                if (self.tx_tti.is_set or self.tx_tti.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_tti.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exp-dapi-range" or name == "exp-oper-spec-range" or name == "exp-sapi-range" or name == "expected-dapi" or name == "expected-dapi0" or name == "expected-oper-spec" or name == "expected-sapi" or name == "expected-sapi0" or name == "expected-string-type" or name == "expected-tti" or name == "rx-dapi" or name == "rx-dapi0" or name == "rx-dapi-range" or name == "rx-oper-spec" or name == "rx-oper-spec-range" or name == "rx-sapi" or name == "rx-sapi0" or name == "rx-sapi-range" or name == "rx-string-type" or name == "rx-tti" or name == "tx-dapi" or name == "tx-dapi0" or name == "tx-dapi-range" or name == "tx-oper-spec" or name == "tx-oper-spec-range" or name == "tx-sapi" or name == "tx-sapi0" or name == "tx-sapi-range" or name == "tx-string-type" or name == "tx-tti"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "exp-dapi-range"):
                                    self.exp_dapi_range = value
                                    self.exp_dapi_range.value_namespace = name_space
                                    self.exp_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "exp-oper-spec-range"):
                                    self.exp_oper_spec_range = value
                                    self.exp_oper_spec_range.value_namespace = name_space
                                    self.exp_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "exp-sapi-range"):
                                    self.exp_sapi_range = value
                                    self.exp_sapi_range.value_namespace = name_space
                                    self.exp_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-dapi"):
                                    self.expected_dapi = value
                                    self.expected_dapi.value_namespace = name_space
                                    self.expected_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-dapi0"):
                                    self.expected_dapi0 = value
                                    self.expected_dapi0.value_namespace = name_space
                                    self.expected_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-oper-spec"):
                                    self.expected_oper_spec = value
                                    self.expected_oper_spec.value_namespace = name_space
                                    self.expected_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-sapi"):
                                    self.expected_sapi = value
                                    self.expected_sapi.value_namespace = name_space
                                    self.expected_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-sapi0"):
                                    self.expected_sapi0 = value
                                    self.expected_sapi0.value_namespace = name_space
                                    self.expected_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-string-type"):
                                    self.expected_string_type = value
                                    self.expected_string_type.value_namespace = name_space
                                    self.expected_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "expected-tti"):
                                    self.expected_tti = value
                                    self.expected_tti.value_namespace = name_space
                                    self.expected_tti.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi"):
                                    self.rx_dapi = value
                                    self.rx_dapi.value_namespace = name_space
                                    self.rx_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi0"):
                                    self.rx_dapi0 = value
                                    self.rx_dapi0.value_namespace = name_space
                                    self.rx_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-dapi-range"):
                                    self.rx_dapi_range = value
                                    self.rx_dapi_range.value_namespace = name_space
                                    self.rx_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-oper-spec"):
                                    self.rx_oper_spec = value
                                    self.rx_oper_spec.value_namespace = name_space
                                    self.rx_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-oper-spec-range"):
                                    self.rx_oper_spec_range = value
                                    self.rx_oper_spec_range.value_namespace = name_space
                                    self.rx_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi"):
                                    self.rx_sapi = value
                                    self.rx_sapi.value_namespace = name_space
                                    self.rx_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi0"):
                                    self.rx_sapi0 = value
                                    self.rx_sapi0.value_namespace = name_space
                                    self.rx_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-sapi-range"):
                                    self.rx_sapi_range = value
                                    self.rx_sapi_range.value_namespace = name_space
                                    self.rx_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-string-type"):
                                    self.rx_string_type = value
                                    self.rx_string_type.value_namespace = name_space
                                    self.rx_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-tti"):
                                    self.rx_tti = value
                                    self.rx_tti.value_namespace = name_space
                                    self.rx_tti.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi"):
                                    self.tx_dapi = value
                                    self.tx_dapi.value_namespace = name_space
                                    self.tx_dapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi0"):
                                    self.tx_dapi0 = value
                                    self.tx_dapi0.value_namespace = name_space
                                    self.tx_dapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-dapi-range"):
                                    self.tx_dapi_range = value
                                    self.tx_dapi_range.value_namespace = name_space
                                    self.tx_dapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-oper-spec"):
                                    self.tx_oper_spec = value
                                    self.tx_oper_spec.value_namespace = name_space
                                    self.tx_oper_spec.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-oper-spec-range"):
                                    self.tx_oper_spec_range = value
                                    self.tx_oper_spec_range.value_namespace = name_space
                                    self.tx_oper_spec_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi"):
                                    self.tx_sapi = value
                                    self.tx_sapi.value_namespace = name_space
                                    self.tx_sapi.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi0"):
                                    self.tx_sapi0 = value
                                    self.tx_sapi0.value_namespace = name_space
                                    self.tx_sapi0.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-sapi-range"):
                                    self.tx_sapi_range = value
                                    self.tx_sapi_range.value_namespace = name_space
                                    self.tx_sapi_range.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-string-type"):
                                    self.tx_string_type = value
                                    self.tx_string_type.value_namespace = name_space
                                    self.tx_string_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-tti"):
                                    self.tx_tti = value
                                    self.tx_tti.value_namespace = name_space
                                    self.tx_tti.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.bei.is_set or
                                self.bip.is_set or
                                (self.ais is not None and self.ais.has_data()) or
                                (self.bbe is not None and self.bbe.has_data()) or
                                (self.bbe_tca is not None and self.bbe_tca.has_data()) or
                                (self.bber is not None and self.bber.has_data()) or
                                (self.bdi is not None and self.bdi.has_data()) or
                                (self.eoc is not None and self.eoc.has_data()) or
                                (self.es is not None and self.es.has_data()) or
                                (self.es_tca is not None and self.es_tca.has_data()) or
                                (self.esr is not None and self.esr.has_data()) or
                                (self.fc is not None and self.fc.has_data()) or
                                (self.lck is not None and self.lck.has_data()) or
                                (self.oci is not None and self.oci.has_data()) or
                                (self.ptim is not None and self.ptim.has_data()) or
                                (self.sd_ber is not None and self.sd_ber.has_data()) or
                                (self.ses is not None and self.ses.has_data()) or
                                (self.sesr is not None and self.sesr.has_data()) or
                                (self.sf_ber is not None and self.sf_ber.has_data()) or
                                (self.tim is not None and self.tim.has_data()) or
                                (self.tti is not None and self.tti.has_data()) or
                                (self.uas is not None and self.uas.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bei.yfilter != YFilter.not_set or
                                self.bip.yfilter != YFilter.not_set or
                                (self.ais is not None and self.ais.has_operation()) or
                                (self.bbe is not None and self.bbe.has_operation()) or
                                (self.bbe_tca is not None and self.bbe_tca.has_operation()) or
                                (self.bber is not None and self.bber.has_operation()) or
                                (self.bdi is not None and self.bdi.has_operation()) or
                                (self.eoc is not None and self.eoc.has_operation()) or
                                (self.es is not None and self.es.has_operation()) or
                                (self.es_tca is not None and self.es_tca.has_operation()) or
                                (self.esr is not None and self.esr.has_operation()) or
                                (self.fc is not None and self.fc.has_operation()) or
                                (self.lck is not None and self.lck.has_operation()) or
                                (self.oci is not None and self.oci.has_operation()) or
                                (self.ptim is not None and self.ptim.has_operation()) or
                                (self.sd_ber is not None and self.sd_ber.has_operation()) or
                                (self.ses is not None and self.ses.has_operation()) or
                                (self.sesr is not None and self.sesr.has_operation()) or
                                (self.sf_ber is not None and self.sf_ber.has_operation()) or
                                (self.tim is not None and self.tim.has_operation()) or
                                (self.tti is not None and self.tti.has_operation()) or
                                (self.uas is not None and self.uas.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "odu-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bei.is_set or self.bei.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bei.get_name_leafdata())
                            if (self.bip.is_set or self.bip.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bip.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ais"):
                                if (self.ais is None):
                                    self.ais = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais()
                                    self.ais.parent = self
                                    self._children_name_map["ais"] = "ais"
                                return self.ais

                            if (child_yang_name == "bbe"):
                                if (self.bbe is None):
                                    self.bbe = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe()
                                    self.bbe.parent = self
                                    self._children_name_map["bbe"] = "bbe"
                                return self.bbe

                            if (child_yang_name == "bbe-tca"):
                                if (self.bbe_tca is None):
                                    self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca()
                                    self.bbe_tca.parent = self
                                    self._children_name_map["bbe_tca"] = "bbe-tca"
                                return self.bbe_tca

                            if (child_yang_name == "bber"):
                                if (self.bber is None):
                                    self.bber = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber()
                                    self.bber.parent = self
                                    self._children_name_map["bber"] = "bber"
                                return self.bber

                            if (child_yang_name == "bdi"):
                                if (self.bdi is None):
                                    self.bdi = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi()
                                    self.bdi.parent = self
                                    self._children_name_map["bdi"] = "bdi"
                                return self.bdi

                            if (child_yang_name == "eoc"):
                                if (self.eoc is None):
                                    self.eoc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc()
                                    self.eoc.parent = self
                                    self._children_name_map["eoc"] = "eoc"
                                return self.eoc

                            if (child_yang_name == "es"):
                                if (self.es is None):
                                    self.es = Dwdm.Ports.Port.Info.G709Info.OduInfo.Es()
                                    self.es.parent = self
                                    self._children_name_map["es"] = "es"
                                return self.es

                            if (child_yang_name == "es-tca"):
                                if (self.es_tca is None):
                                    self.es_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca()
                                    self.es_tca.parent = self
                                    self._children_name_map["es_tca"] = "es-tca"
                                return self.es_tca

                            if (child_yang_name == "esr"):
                                if (self.esr is None):
                                    self.esr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr()
                                    self.esr.parent = self
                                    self._children_name_map["esr"] = "esr"
                                return self.esr

                            if (child_yang_name == "fc"):
                                if (self.fc is None):
                                    self.fc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc()
                                    self.fc.parent = self
                                    self._children_name_map["fc"] = "fc"
                                return self.fc

                            if (child_yang_name == "lck"):
                                if (self.lck is None):
                                    self.lck = Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck()
                                    self.lck.parent = self
                                    self._children_name_map["lck"] = "lck"
                                return self.lck

                            if (child_yang_name == "oci"):
                                if (self.oci is None):
                                    self.oci = Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci()
                                    self.oci.parent = self
                                    self._children_name_map["oci"] = "oci"
                                return self.oci

                            if (child_yang_name == "ptim"):
                                if (self.ptim is None):
                                    self.ptim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim()
                                    self.ptim.parent = self
                                    self._children_name_map["ptim"] = "ptim"
                                return self.ptim

                            if (child_yang_name == "sd-ber"):
                                if (self.sd_ber is None):
                                    self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer()
                                    self.sd_ber.parent = self
                                    self._children_name_map["sd_ber"] = "sd-ber"
                                return self.sd_ber

                            if (child_yang_name == "ses"):
                                if (self.ses is None):
                                    self.ses = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses()
                                    self.ses.parent = self
                                    self._children_name_map["ses"] = "ses"
                                return self.ses

                            if (child_yang_name == "sesr"):
                                if (self.sesr is None):
                                    self.sesr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr()
                                    self.sesr.parent = self
                                    self._children_name_map["sesr"] = "sesr"
                                return self.sesr

                            if (child_yang_name == "sf-ber"):
                                if (self.sf_ber is None):
                                    self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer()
                                    self.sf_ber.parent = self
                                    self._children_name_map["sf_ber"] = "sf-ber"
                                return self.sf_ber

                            if (child_yang_name == "tim"):
                                if (self.tim is None):
                                    self.tim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim()
                                    self.tim.parent = self
                                    self._children_name_map["tim"] = "tim"
                                return self.tim

                            if (child_yang_name == "tti"):
                                if (self.tti is None):
                                    self.tti = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti()
                                    self.tti.parent = self
                                    self._children_name_map["tti"] = "tti"
                                return self.tti

                            if (child_yang_name == "uas"):
                                if (self.uas is None):
                                    self.uas = Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas()
                                    self.uas.parent = self
                                    self._children_name_map["uas"] = "uas"
                                return self.uas

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ais" or name == "bbe" or name == "bbe-tca" or name == "bber" or name == "bdi" or name == "eoc" or name == "es" or name == "es-tca" or name == "esr" or name == "fc" or name == "lck" or name == "oci" or name == "ptim" or name == "sd-ber" or name == "ses" or name == "sesr" or name == "sf-ber" or name == "tim" or name == "tti" or name == "uas" or name == "bei" or name == "bip"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bei"):
                                self.bei = value
                                self.bei.value_namespace = name_space
                                self.bei.value_namespace_prefix = name_space_prefix
                            if(value_path == "bip"):
                                self.bip = value
                                self.bip.value_namespace = name_space
                                self.bip.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.ec.is_set or
                            self.ec_accum.is_set or
                            self.efec_mode.is_set or
                            self.fe_cstr.is_set or
                            self.fec_ber.is_set or
                            self.fec_ber_man.is_set or
                            self.fec_mode.is_set or
                            self.g709_prbs_mode.is_set or
                            self.g709_prbs_pattern.is_set or
                            self.is_fec_mode_default.is_set or
                            self.is_g709_enabled.is_set or
                            self.is_prbs_enabled.is_set or
                            self.loopback_mode.is_set or
                            self.network_conn_id.is_set or
                            self.network_port_id.is_set or
                            self.prbs_time_stamp.is_set or
                            self.q.is_set or
                            self.q_margin.is_set or
                            self.qmargin_str.is_set or
                            self.qstr.is_set or
                            self.remote_fec_mode.is_set or
                            self.uc.is_set or
                            (self.ec_tca is not None and self.ec_tca.has_data()) or
                            (self.fec_mismatch is not None and self.fec_mismatch.has_data()) or
                            (self.odu_info is not None and self.odu_info.has_data()) or
                            (self.otu_info is not None and self.otu_info.has_data()) or
                            (self.uc_tca is not None and self.uc_tca.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ec.yfilter != YFilter.not_set or
                            self.ec_accum.yfilter != YFilter.not_set or
                            self.efec_mode.yfilter != YFilter.not_set or
                            self.fe_cstr.yfilter != YFilter.not_set or
                            self.fec_ber.yfilter != YFilter.not_set or
                            self.fec_ber_man.yfilter != YFilter.not_set or
                            self.fec_mode.yfilter != YFilter.not_set or
                            self.g709_prbs_mode.yfilter != YFilter.not_set or
                            self.g709_prbs_pattern.yfilter != YFilter.not_set or
                            self.is_fec_mode_default.yfilter != YFilter.not_set or
                            self.is_g709_enabled.yfilter != YFilter.not_set or
                            self.is_prbs_enabled.yfilter != YFilter.not_set or
                            self.loopback_mode.yfilter != YFilter.not_set or
                            self.network_conn_id.yfilter != YFilter.not_set or
                            self.network_port_id.yfilter != YFilter.not_set or
                            self.prbs_time_stamp.yfilter != YFilter.not_set or
                            self.q.yfilter != YFilter.not_set or
                            self.q_margin.yfilter != YFilter.not_set or
                            self.qmargin_str.yfilter != YFilter.not_set or
                            self.qstr.yfilter != YFilter.not_set or
                            self.remote_fec_mode.yfilter != YFilter.not_set or
                            self.uc.yfilter != YFilter.not_set or
                            (self.ec_tca is not None and self.ec_tca.has_operation()) or
                            (self.fec_mismatch is not None and self.fec_mismatch.has_operation()) or
                            (self.odu_info is not None and self.odu_info.has_operation()) or
                            (self.otu_info is not None and self.otu_info.has_operation()) or
                            (self.uc_tca is not None and self.uc_tca.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "g709-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ec.is_set or self.ec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ec.get_name_leafdata())
                        if (self.ec_accum.is_set or self.ec_accum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ec_accum.get_name_leafdata())
                        if (self.efec_mode.is_set or self.efec_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.efec_mode.get_name_leafdata())
                        if (self.fe_cstr.is_set or self.fe_cstr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fe_cstr.get_name_leafdata())
                        if (self.fec_ber.is_set or self.fec_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_ber.get_name_leafdata())
                        if (self.fec_ber_man.is_set or self.fec_ber_man.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_ber_man.get_name_leafdata())
                        if (self.fec_mode.is_set or self.fec_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fec_mode.get_name_leafdata())
                        if (self.g709_prbs_mode.is_set or self.g709_prbs_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g709_prbs_mode.get_name_leafdata())
                        if (self.g709_prbs_pattern.is_set or self.g709_prbs_pattern.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.g709_prbs_pattern.get_name_leafdata())
                        if (self.is_fec_mode_default.is_set or self.is_fec_mode_default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_fec_mode_default.get_name_leafdata())
                        if (self.is_g709_enabled.is_set or self.is_g709_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_g709_enabled.get_name_leafdata())
                        if (self.is_prbs_enabled.is_set or self.is_prbs_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_prbs_enabled.get_name_leafdata())
                        if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                        if (self.network_conn_id.is_set or self.network_conn_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.network_conn_id.get_name_leafdata())
                        if (self.network_port_id.is_set or self.network_port_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.network_port_id.get_name_leafdata())
                        if (self.prbs_time_stamp.is_set or self.prbs_time_stamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prbs_time_stamp.get_name_leafdata())
                        if (self.q.is_set or self.q.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.q.get_name_leafdata())
                        if (self.q_margin.is_set or self.q_margin.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.q_margin.get_name_leafdata())
                        if (self.qmargin_str.is_set or self.qmargin_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qmargin_str.get_name_leafdata())
                        if (self.qstr.is_set or self.qstr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qstr.get_name_leafdata())
                        if (self.remote_fec_mode.is_set or self.remote_fec_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_fec_mode.get_name_leafdata())
                        if (self.uc.is_set or self.uc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uc.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ec-tca"):
                            if (self.ec_tca is None):
                                self.ec_tca = Dwdm.Ports.Port.Info.G709Info.EcTca()
                                self.ec_tca.parent = self
                                self._children_name_map["ec_tca"] = "ec-tca"
                            return self.ec_tca

                        if (child_yang_name == "fec-mismatch"):
                            if (self.fec_mismatch is None):
                                self.fec_mismatch = Dwdm.Ports.Port.Info.G709Info.FecMismatch()
                                self.fec_mismatch.parent = self
                                self._children_name_map["fec_mismatch"] = "fec-mismatch"
                            return self.fec_mismatch

                        if (child_yang_name == "odu-info"):
                            if (self.odu_info is None):
                                self.odu_info = Dwdm.Ports.Port.Info.G709Info.OduInfo()
                                self.odu_info.parent = self
                                self._children_name_map["odu_info"] = "odu-info"
                            return self.odu_info

                        if (child_yang_name == "otu-info"):
                            if (self.otu_info is None):
                                self.otu_info = Dwdm.Ports.Port.Info.G709Info.OtuInfo()
                                self.otu_info.parent = self
                                self._children_name_map["otu_info"] = "otu-info"
                            return self.otu_info

                        if (child_yang_name == "uc-tca"):
                            if (self.uc_tca is None):
                                self.uc_tca = Dwdm.Ports.Port.Info.G709Info.UcTca()
                                self.uc_tca.parent = self
                                self._children_name_map["uc_tca"] = "uc-tca"
                            return self.uc_tca

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ec-tca" or name == "fec-mismatch" or name == "odu-info" or name == "otu-info" or name == "uc-tca" or name == "ec" or name == "ec-accum" or name == "efec-mode" or name == "fe-cstr" or name == "fec-ber" or name == "fec-ber-man" or name == "fec-mode" or name == "g709-prbs-mode" or name == "g709-prbs-pattern" or name == "is-fec-mode-default" or name == "is-g709-enabled" or name == "is-prbs-enabled" or name == "loopback-mode" or name == "network-conn-id" or name == "network-port-id" or name == "prbs-time-stamp" or name == "q" or name == "q-margin" or name == "qmargin-str" or name == "qstr" or name == "remote-fec-mode" or name == "uc"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ec"):
                            self.ec = value
                            self.ec.value_namespace = name_space
                            self.ec.value_namespace_prefix = name_space_prefix
                        if(value_path == "ec-accum"):
                            self.ec_accum = value
                            self.ec_accum.value_namespace = name_space
                            self.ec_accum.value_namespace_prefix = name_space_prefix
                        if(value_path == "efec-mode"):
                            self.efec_mode = value
                            self.efec_mode.value_namespace = name_space
                            self.efec_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "fe-cstr"):
                            self.fe_cstr = value
                            self.fe_cstr.value_namespace = name_space
                            self.fe_cstr.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-ber"):
                            self.fec_ber = value
                            self.fec_ber.value_namespace = name_space
                            self.fec_ber.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-ber-man"):
                            self.fec_ber_man = value
                            self.fec_ber_man.value_namespace = name_space
                            self.fec_ber_man.value_namespace_prefix = name_space_prefix
                        if(value_path == "fec-mode"):
                            self.fec_mode = value
                            self.fec_mode.value_namespace = name_space
                            self.fec_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "g709-prbs-mode"):
                            self.g709_prbs_mode = value
                            self.g709_prbs_mode.value_namespace = name_space
                            self.g709_prbs_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "g709-prbs-pattern"):
                            self.g709_prbs_pattern = value
                            self.g709_prbs_pattern.value_namespace = name_space
                            self.g709_prbs_pattern.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-fec-mode-default"):
                            self.is_fec_mode_default = value
                            self.is_fec_mode_default.value_namespace = name_space
                            self.is_fec_mode_default.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-g709-enabled"):
                            self.is_g709_enabled = value
                            self.is_g709_enabled.value_namespace = name_space
                            self.is_g709_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-prbs-enabled"):
                            self.is_prbs_enabled = value
                            self.is_prbs_enabled.value_namespace = name_space
                            self.is_prbs_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "loopback-mode"):
                            self.loopback_mode = value
                            self.loopback_mode.value_namespace = name_space
                            self.loopback_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "network-conn-id"):
                            self.network_conn_id = value
                            self.network_conn_id.value_namespace = name_space
                            self.network_conn_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "network-port-id"):
                            self.network_port_id = value
                            self.network_port_id.value_namespace = name_space
                            self.network_port_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "prbs-time-stamp"):
                            self.prbs_time_stamp = value
                            self.prbs_time_stamp.value_namespace = name_space
                            self.prbs_time_stamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "q"):
                            self.q = value
                            self.q.value_namespace = name_space
                            self.q.value_namespace_prefix = name_space_prefix
                        if(value_path == "q-margin"):
                            self.q_margin = value
                            self.q_margin.value_namespace = name_space
                            self.q_margin.value_namespace_prefix = name_space_prefix
                        if(value_path == "qmargin-str"):
                            self.qmargin_str = value
                            self.qmargin_str.value_namespace = name_space
                            self.qmargin_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "qstr"):
                            self.qstr = value
                            self.qstr.value_namespace = name_space
                            self.qstr.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-fec-mode"):
                            self.remote_fec_mode = value
                            self.remote_fec_mode.value_namespace = name_space
                            self.remote_fec_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "uc"):
                            self.uc = value
                            self.uc.value_namespace = name_space
                            self.uc.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("chromatic_dispersion",
                                        "clock_source",
                                        "configured_wave_channel",
                                        "default_wave_channel",
                                        "differential_group_delay",
                                        "gmpls_set_wave_channel",
                                        "input_power_fail",
                                        "is_rx_los_threshold_supported",
                                        "is_wave_frequency_progressive_valid",
                                        "is_wave_frequency_valid",
                                        "laser_bias_current_avg",
                                        "laser_bias_current_max",
                                        "laser_bias_current_min",
                                        "laser_current_bias",
                                        "laser_current_bias_threshold",
                                        "optics_type",
                                        "output_power_fail",
                                        "phase_noise",
                                        "polarization_change_rate",
                                        "polarization_dependent_loss",
                                        "polarization_mode_dispersion",
                                        "receive_power",
                                        "receive_power_avg",
                                        "receive_power_max",
                                        "receive_power_min",
                                        "rx_los_threshold",
                                        "signal_to_noise_ratio",
                                        "transmit_power",
                                        "transmit_power_avg",
                                        "transmit_power_max",
                                        "transmit_power_min",
                                        "transmit_power_threshold",
                                        "wave_band",
                                        "wave_channel",
                                        "wave_channel_owner",
                                        "wave_frequency",
                                        "wave_frequency_progressive_string",
                                        "wavelength_progressive",
                                        "wavelength_progressive_string") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.OpticsInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.OpticsInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.chromatic_dispersion.is_set or
                            self.clock_source.is_set or
                            self.configured_wave_channel.is_set or
                            self.default_wave_channel.is_set or
                            self.differential_group_delay.is_set or
                            self.gmpls_set_wave_channel.is_set or
                            self.input_power_fail.is_set or
                            self.is_rx_los_threshold_supported.is_set or
                            self.is_wave_frequency_progressive_valid.is_set or
                            self.is_wave_frequency_valid.is_set or
                            self.laser_bias_current_avg.is_set or
                            self.laser_bias_current_max.is_set or
                            self.laser_bias_current_min.is_set or
                            self.laser_current_bias.is_set or
                            self.laser_current_bias_threshold.is_set or
                            self.optics_type.is_set or
                            self.output_power_fail.is_set or
                            self.phase_noise.is_set or
                            self.polarization_change_rate.is_set or
                            self.polarization_dependent_loss.is_set or
                            self.polarization_mode_dispersion.is_set or
                            self.receive_power.is_set or
                            self.receive_power_avg.is_set or
                            self.receive_power_max.is_set or
                            self.receive_power_min.is_set or
                            self.rx_los_threshold.is_set or
                            self.signal_to_noise_ratio.is_set or
                            self.transmit_power.is_set or
                            self.transmit_power_avg.is_set or
                            self.transmit_power_max.is_set or
                            self.transmit_power_min.is_set or
                            self.transmit_power_threshold.is_set or
                            self.wave_band.is_set or
                            self.wave_channel.is_set or
                            self.wave_channel_owner.is_set or
                            self.wave_frequency.is_set or
                            self.wave_frequency_progressive_string.is_set or
                            self.wavelength_progressive.is_set or
                            self.wavelength_progressive_string.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.chromatic_dispersion.yfilter != YFilter.not_set or
                            self.clock_source.yfilter != YFilter.not_set or
                            self.configured_wave_channel.yfilter != YFilter.not_set or
                            self.default_wave_channel.yfilter != YFilter.not_set or
                            self.differential_group_delay.yfilter != YFilter.not_set or
                            self.gmpls_set_wave_channel.yfilter != YFilter.not_set or
                            self.input_power_fail.yfilter != YFilter.not_set or
                            self.is_rx_los_threshold_supported.yfilter != YFilter.not_set or
                            self.is_wave_frequency_progressive_valid.yfilter != YFilter.not_set or
                            self.is_wave_frequency_valid.yfilter != YFilter.not_set or
                            self.laser_bias_current_avg.yfilter != YFilter.not_set or
                            self.laser_bias_current_max.yfilter != YFilter.not_set or
                            self.laser_bias_current_min.yfilter != YFilter.not_set or
                            self.laser_current_bias.yfilter != YFilter.not_set or
                            self.laser_current_bias_threshold.yfilter != YFilter.not_set or
                            self.optics_type.yfilter != YFilter.not_set or
                            self.output_power_fail.yfilter != YFilter.not_set or
                            self.phase_noise.yfilter != YFilter.not_set or
                            self.polarization_change_rate.yfilter != YFilter.not_set or
                            self.polarization_dependent_loss.yfilter != YFilter.not_set or
                            self.polarization_mode_dispersion.yfilter != YFilter.not_set or
                            self.receive_power.yfilter != YFilter.not_set or
                            self.receive_power_avg.yfilter != YFilter.not_set or
                            self.receive_power_max.yfilter != YFilter.not_set or
                            self.receive_power_min.yfilter != YFilter.not_set or
                            self.rx_los_threshold.yfilter != YFilter.not_set or
                            self.signal_to_noise_ratio.yfilter != YFilter.not_set or
                            self.transmit_power.yfilter != YFilter.not_set or
                            self.transmit_power_avg.yfilter != YFilter.not_set or
                            self.transmit_power_max.yfilter != YFilter.not_set or
                            self.transmit_power_min.yfilter != YFilter.not_set or
                            self.transmit_power_threshold.yfilter != YFilter.not_set or
                            self.wave_band.yfilter != YFilter.not_set or
                            self.wave_channel.yfilter != YFilter.not_set or
                            self.wave_channel_owner.yfilter != YFilter.not_set or
                            self.wave_frequency.yfilter != YFilter.not_set or
                            self.wave_frequency_progressive_string.yfilter != YFilter.not_set or
                            self.wavelength_progressive.yfilter != YFilter.not_set or
                            self.wavelength_progressive_string.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "optics-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.chromatic_dispersion.is_set or self.chromatic_dispersion.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.chromatic_dispersion.get_name_leafdata())
                        if (self.clock_source.is_set or self.clock_source.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clock_source.get_name_leafdata())
                        if (self.configured_wave_channel.is_set or self.configured_wave_channel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_wave_channel.get_name_leafdata())
                        if (self.default_wave_channel.is_set or self.default_wave_channel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_wave_channel.get_name_leafdata())
                        if (self.differential_group_delay.is_set or self.differential_group_delay.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.differential_group_delay.get_name_leafdata())
                        if (self.gmpls_set_wave_channel.is_set or self.gmpls_set_wave_channel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.gmpls_set_wave_channel.get_name_leafdata())
                        if (self.input_power_fail.is_set or self.input_power_fail.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_power_fail.get_name_leafdata())
                        if (self.is_rx_los_threshold_supported.is_set or self.is_rx_los_threshold_supported.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_rx_los_threshold_supported.get_name_leafdata())
                        if (self.is_wave_frequency_progressive_valid.is_set or self.is_wave_frequency_progressive_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_wave_frequency_progressive_valid.get_name_leafdata())
                        if (self.is_wave_frequency_valid.is_set or self.is_wave_frequency_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_wave_frequency_valid.get_name_leafdata())
                        if (self.laser_bias_current_avg.is_set or self.laser_bias_current_avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_avg.get_name_leafdata())
                        if (self.laser_bias_current_max.is_set or self.laser_bias_current_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_max.get_name_leafdata())
                        if (self.laser_bias_current_min.is_set or self.laser_bias_current_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_bias_current_min.get_name_leafdata())
                        if (self.laser_current_bias.is_set or self.laser_current_bias.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_current_bias.get_name_leafdata())
                        if (self.laser_current_bias_threshold.is_set or self.laser_current_bias_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.laser_current_bias_threshold.get_name_leafdata())
                        if (self.optics_type.is_set or self.optics_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.optics_type.get_name_leafdata())
                        if (self.output_power_fail.is_set or self.output_power_fail.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_power_fail.get_name_leafdata())
                        if (self.phase_noise.is_set or self.phase_noise.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.phase_noise.get_name_leafdata())
                        if (self.polarization_change_rate.is_set or self.polarization_change_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.polarization_change_rate.get_name_leafdata())
                        if (self.polarization_dependent_loss.is_set or self.polarization_dependent_loss.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.polarization_dependent_loss.get_name_leafdata())
                        if (self.polarization_mode_dispersion.is_set or self.polarization_mode_dispersion.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.polarization_mode_dispersion.get_name_leafdata())
                        if (self.receive_power.is_set or self.receive_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power.get_name_leafdata())
                        if (self.receive_power_avg.is_set or self.receive_power_avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power_avg.get_name_leafdata())
                        if (self.receive_power_max.is_set or self.receive_power_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power_max.get_name_leafdata())
                        if (self.receive_power_min.is_set or self.receive_power_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_power_min.get_name_leafdata())
                        if (self.rx_los_threshold.is_set or self.rx_los_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_los_threshold.get_name_leafdata())
                        if (self.signal_to_noise_ratio.is_set or self.signal_to_noise_ratio.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.signal_to_noise_ratio.get_name_leafdata())
                        if (self.transmit_power.is_set or self.transmit_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power.get_name_leafdata())
                        if (self.transmit_power_avg.is_set or self.transmit_power_avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power_avg.get_name_leafdata())
                        if (self.transmit_power_max.is_set or self.transmit_power_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power_max.get_name_leafdata())
                        if (self.transmit_power_min.is_set or self.transmit_power_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power_min.get_name_leafdata())
                        if (self.transmit_power_threshold.is_set or self.transmit_power_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_power_threshold.get_name_leafdata())
                        if (self.wave_band.is_set or self.wave_band.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_band.get_name_leafdata())
                        if (self.wave_channel.is_set or self.wave_channel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_channel.get_name_leafdata())
                        if (self.wave_channel_owner.is_set or self.wave_channel_owner.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_channel_owner.get_name_leafdata())
                        if (self.wave_frequency.is_set or self.wave_frequency.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_frequency.get_name_leafdata())
                        if (self.wave_frequency_progressive_string.is_set or self.wave_frequency_progressive_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wave_frequency_progressive_string.get_name_leafdata())
                        if (self.wavelength_progressive.is_set or self.wavelength_progressive.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wavelength_progressive.get_name_leafdata())
                        if (self.wavelength_progressive_string.is_set or self.wavelength_progressive_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wavelength_progressive_string.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "chromatic-dispersion" or name == "clock-source" or name == "configured-wave-channel" or name == "default-wave-channel" or name == "differential-group-delay" or name == "gmpls-set-wave-channel" or name == "input-power-fail" or name == "is-rx-los-threshold-supported" or name == "is-wave-frequency-progressive-valid" or name == "is-wave-frequency-valid" or name == "laser-bias-current-avg" or name == "laser-bias-current-max" or name == "laser-bias-current-min" or name == "laser-current-bias" or name == "laser-current-bias-threshold" or name == "optics-type" or name == "output-power-fail" or name == "phase-noise" or name == "polarization-change-rate" or name == "polarization-dependent-loss" or name == "polarization-mode-dispersion" or name == "receive-power" or name == "receive-power-avg" or name == "receive-power-max" or name == "receive-power-min" or name == "rx-los-threshold" or name == "signal-to-noise-ratio" or name == "transmit-power" or name == "transmit-power-avg" or name == "transmit-power-max" or name == "transmit-power-min" or name == "transmit-power-threshold" or name == "wave-band" or name == "wave-channel" or name == "wave-channel-owner" or name == "wave-frequency" or name == "wave-frequency-progressive-string" or name == "wavelength-progressive" or name == "wavelength-progressive-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "chromatic-dispersion"):
                            self.chromatic_dispersion = value
                            self.chromatic_dispersion.value_namespace = name_space
                            self.chromatic_dispersion.value_namespace_prefix = name_space_prefix
                        if(value_path == "clock-source"):
                            self.clock_source = value
                            self.clock_source.value_namespace = name_space
                            self.clock_source.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-wave-channel"):
                            self.configured_wave_channel = value
                            self.configured_wave_channel.value_namespace = name_space
                            self.configured_wave_channel.value_namespace_prefix = name_space_prefix
                        if(value_path == "default-wave-channel"):
                            self.default_wave_channel = value
                            self.default_wave_channel.value_namespace = name_space
                            self.default_wave_channel.value_namespace_prefix = name_space_prefix
                        if(value_path == "differential-group-delay"):
                            self.differential_group_delay = value
                            self.differential_group_delay.value_namespace = name_space
                            self.differential_group_delay.value_namespace_prefix = name_space_prefix
                        if(value_path == "gmpls-set-wave-channel"):
                            self.gmpls_set_wave_channel = value
                            self.gmpls_set_wave_channel.value_namespace = name_space
                            self.gmpls_set_wave_channel.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-power-fail"):
                            self.input_power_fail = value
                            self.input_power_fail.value_namespace = name_space
                            self.input_power_fail.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-rx-los-threshold-supported"):
                            self.is_rx_los_threshold_supported = value
                            self.is_rx_los_threshold_supported.value_namespace = name_space
                            self.is_rx_los_threshold_supported.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-wave-frequency-progressive-valid"):
                            self.is_wave_frequency_progressive_valid = value
                            self.is_wave_frequency_progressive_valid.value_namespace = name_space
                            self.is_wave_frequency_progressive_valid.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-wave-frequency-valid"):
                            self.is_wave_frequency_valid = value
                            self.is_wave_frequency_valid.value_namespace = name_space
                            self.is_wave_frequency_valid.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-avg"):
                            self.laser_bias_current_avg = value
                            self.laser_bias_current_avg.value_namespace = name_space
                            self.laser_bias_current_avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-max"):
                            self.laser_bias_current_max = value
                            self.laser_bias_current_max.value_namespace = name_space
                            self.laser_bias_current_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-bias-current-min"):
                            self.laser_bias_current_min = value
                            self.laser_bias_current_min.value_namespace = name_space
                            self.laser_bias_current_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-current-bias"):
                            self.laser_current_bias = value
                            self.laser_current_bias.value_namespace = name_space
                            self.laser_current_bias.value_namespace_prefix = name_space_prefix
                        if(value_path == "laser-current-bias-threshold"):
                            self.laser_current_bias_threshold = value
                            self.laser_current_bias_threshold.value_namespace = name_space
                            self.laser_current_bias_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "optics-type"):
                            self.optics_type = value
                            self.optics_type.value_namespace = name_space
                            self.optics_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-power-fail"):
                            self.output_power_fail = value
                            self.output_power_fail.value_namespace = name_space
                            self.output_power_fail.value_namespace_prefix = name_space_prefix
                        if(value_path == "phase-noise"):
                            self.phase_noise = value
                            self.phase_noise.value_namespace = name_space
                            self.phase_noise.value_namespace_prefix = name_space_prefix
                        if(value_path == "polarization-change-rate"):
                            self.polarization_change_rate = value
                            self.polarization_change_rate.value_namespace = name_space
                            self.polarization_change_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "polarization-dependent-loss"):
                            self.polarization_dependent_loss = value
                            self.polarization_dependent_loss.value_namespace = name_space
                            self.polarization_dependent_loss.value_namespace_prefix = name_space_prefix
                        if(value_path == "polarization-mode-dispersion"):
                            self.polarization_mode_dispersion = value
                            self.polarization_mode_dispersion.value_namespace = name_space
                            self.polarization_mode_dispersion.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power"):
                            self.receive_power = value
                            self.receive_power.value_namespace = name_space
                            self.receive_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power-avg"):
                            self.receive_power_avg = value
                            self.receive_power_avg.value_namespace = name_space
                            self.receive_power_avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power-max"):
                            self.receive_power_max = value
                            self.receive_power_max.value_namespace = name_space
                            self.receive_power_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-power-min"):
                            self.receive_power_min = value
                            self.receive_power_min.value_namespace = name_space
                            self.receive_power_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-los-threshold"):
                            self.rx_los_threshold = value
                            self.rx_los_threshold.value_namespace = name_space
                            self.rx_los_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "signal-to-noise-ratio"):
                            self.signal_to_noise_ratio = value
                            self.signal_to_noise_ratio.value_namespace = name_space
                            self.signal_to_noise_ratio.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power"):
                            self.transmit_power = value
                            self.transmit_power.value_namespace = name_space
                            self.transmit_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power-avg"):
                            self.transmit_power_avg = value
                            self.transmit_power_avg.value_namespace = name_space
                            self.transmit_power_avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power-max"):
                            self.transmit_power_max = value
                            self.transmit_power_max.value_namespace = name_space
                            self.transmit_power_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power-min"):
                            self.transmit_power_min = value
                            self.transmit_power_min.value_namespace = name_space
                            self.transmit_power_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-power-threshold"):
                            self.transmit_power_threshold = value
                            self.transmit_power_threshold.value_namespace = name_space
                            self.transmit_power_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-band"):
                            self.wave_band = value
                            self.wave_band.value_namespace = name_space
                            self.wave_band.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-channel"):
                            self.wave_channel = value
                            self.wave_channel.value_namespace = name_space
                            self.wave_channel.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-channel-owner"):
                            self.wave_channel_owner = value
                            self.wave_channel_owner.value_namespace = name_space
                            self.wave_channel_owner.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-frequency"):
                            self.wave_frequency = value
                            self.wave_frequency.value_namespace = name_space
                            self.wave_frequency.value_namespace_prefix = name_space_prefix
                        if(value_path == "wave-frequency-progressive-string"):
                            self.wave_frequency_progressive_string = value
                            self.wave_frequency_progressive_string.value_namespace = name_space
                            self.wave_frequency_progressive_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "wavelength-progressive"):
                            self.wavelength_progressive = value
                            self.wavelength_progressive.value_namespace = name_space
                            self.wavelength_progressive.value_namespace_prefix = name_space_prefix
                        if(value_path == "wavelength-progressive-string"):
                            self.wavelength_progressive_string = value
                            self.wavelength_progressive_string.value_namespace = name_space
                            self.wavelength_progressive_string.value_namespace_prefix = name_space_prefix


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

                        self.dispersion_offset = YLeaf(YType.int32, "dispersion-offset")

                        self.is_reroute_control_enabled = YLeaf(YType.boolean, "is-reroute-control-enabled")

                        self.major_alarm = YLeaf(YType.boolean, "major-alarm")

                        self.operation_mode = YLeaf(YType.boolean, "operation-mode")

                        self.reroute_ber = YLeaf(YType.int32, "reroute-ber")

                        self.tdc_status = YLeaf(YType.boolean, "tdc-status")

                        self.tdc_valid = YLeaf(YType.boolean, "tdc-valid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dispersion_offset",
                                        "is_reroute_control_enabled",
                                        "major_alarm",
                                        "operation_mode",
                                        "reroute_ber",
                                        "tdc_status",
                                        "tdc_valid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.TdcInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.TdcInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dispersion_offset.is_set or
                            self.is_reroute_control_enabled.is_set or
                            self.major_alarm.is_set or
                            self.operation_mode.is_set or
                            self.reroute_ber.is_set or
                            self.tdc_status.is_set or
                            self.tdc_valid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dispersion_offset.yfilter != YFilter.not_set or
                            self.is_reroute_control_enabled.yfilter != YFilter.not_set or
                            self.major_alarm.yfilter != YFilter.not_set or
                            self.operation_mode.yfilter != YFilter.not_set or
                            self.reroute_ber.yfilter != YFilter.not_set or
                            self.tdc_status.yfilter != YFilter.not_set or
                            self.tdc_valid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tdc-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dispersion_offset.is_set or self.dispersion_offset.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dispersion_offset.get_name_leafdata())
                        if (self.is_reroute_control_enabled.is_set or self.is_reroute_control_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_reroute_control_enabled.get_name_leafdata())
                        if (self.major_alarm.is_set or self.major_alarm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.major_alarm.get_name_leafdata())
                        if (self.operation_mode.is_set or self.operation_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.operation_mode.get_name_leafdata())
                        if (self.reroute_ber.is_set or self.reroute_ber.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reroute_ber.get_name_leafdata())
                        if (self.tdc_status.is_set or self.tdc_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tdc_status.get_name_leafdata())
                        if (self.tdc_valid.is_set or self.tdc_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tdc_valid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dispersion-offset" or name == "is-reroute-control-enabled" or name == "major-alarm" or name == "operation-mode" or name == "reroute-ber" or name == "tdc-status" or name == "tdc-valid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dispersion-offset"):
                            self.dispersion_offset = value
                            self.dispersion_offset.value_namespace = name_space
                            self.dispersion_offset.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-reroute-control-enabled"):
                            self.is_reroute_control_enabled = value
                            self.is_reroute_control_enabled.value_namespace = name_space
                            self.is_reroute_control_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "major-alarm"):
                            self.major_alarm = value
                            self.major_alarm.value_namespace = name_space
                            self.major_alarm.value_namespace_prefix = name_space_prefix
                        if(value_path == "operation-mode"):
                            self.operation_mode = value
                            self.operation_mode.value_namespace = name_space
                            self.operation_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "reroute-ber"):
                            self.reroute_ber = value
                            self.reroute_ber.value_namespace = name_space
                            self.reroute_ber.value_namespace_prefix = name_space_prefix
                        if(value_path == "tdc-status"):
                            self.tdc_status = value
                            self.tdc_status.value_namespace = name_space
                            self.tdc_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "tdc-valid"):
                            self.tdc_valid = value
                            self.tdc_valid.value_namespace = name_space
                            self.tdc_valid.value_namespace_prefix = name_space_prefix


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

                        self.network_srlg = YLeafList(YType.uint32, "network-srlg")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("network_srlg") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.NetworkSrlgInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.NetworkSrlgInfo, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.network_srlg.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return False

                    def has_operation(self):
                        for leaf in self.network_srlg.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.network_srlg.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network-srlg-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.network_srlg.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "network-srlg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "network-srlg"):
                            self.network_srlg.append(value)


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
                    	**type**\:   :py:class:`G709PpintfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpintfState>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:   :py:class:`G709PpfsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpfsmState>`
                    
                    .. attribute:: proactive_mode
                    
                    	Proactive Mode
                    	**type**\:   :py:class:`G709PpfsmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpfsmMode>`
                    
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
                    	**type**\:   :py:class:`G709ApsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ApsByte>`
                    
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
                    	**type**\:   :py:class:`G709ApsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ApsByte>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("alarm_state",
                                        "default_rvrt_thresh_coeff",
                                        "default_rvrt_thresh_power",
                                        "default_trig_thresh_coeff",
                                        "default_trig_thresh_power",
                                        "interface_trigger",
                                        "prefec_thresh_crossed",
                                        "proactive_feature",
                                        "proactive_fsm_if_state",
                                        "proactive_fsm_state",
                                        "proactive_mode",
                                        "protection_trigger",
                                        "revert_window",
                                        "rvrt_ec_cnt",
                                        "rvrt_samples",
                                        "rvrt_thresh_coeff",
                                        "rvrt_thresh_power",
                                        "rx_aps",
                                        "rx_aps_descr",
                                        "tas_state",
                                        "trig_ec_cnt",
                                        "trig_samples",
                                        "trig_thresh_coeff",
                                        "trig_thresh_power",
                                        "trigger_window",
                                        "tx_aps",
                                        "tx_aps_descr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.Proactive, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.Proactive, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.alarm_state.is_set or
                            self.default_rvrt_thresh_coeff.is_set or
                            self.default_rvrt_thresh_power.is_set or
                            self.default_trig_thresh_coeff.is_set or
                            self.default_trig_thresh_power.is_set or
                            self.interface_trigger.is_set or
                            self.prefec_thresh_crossed.is_set or
                            self.proactive_feature.is_set or
                            self.proactive_fsm_if_state.is_set or
                            self.proactive_fsm_state.is_set or
                            self.proactive_mode.is_set or
                            self.protection_trigger.is_set or
                            self.revert_window.is_set or
                            self.rvrt_ec_cnt.is_set or
                            self.rvrt_samples.is_set or
                            self.rvrt_thresh_coeff.is_set or
                            self.rvrt_thresh_power.is_set or
                            self.rx_aps.is_set or
                            self.rx_aps_descr.is_set or
                            self.tas_state.is_set or
                            self.trig_ec_cnt.is_set or
                            self.trig_samples.is_set or
                            self.trig_thresh_coeff.is_set or
                            self.trig_thresh_power.is_set or
                            self.trigger_window.is_set or
                            self.tx_aps.is_set or
                            self.tx_aps_descr.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.alarm_state.yfilter != YFilter.not_set or
                            self.default_rvrt_thresh_coeff.yfilter != YFilter.not_set or
                            self.default_rvrt_thresh_power.yfilter != YFilter.not_set or
                            self.default_trig_thresh_coeff.yfilter != YFilter.not_set or
                            self.default_trig_thresh_power.yfilter != YFilter.not_set or
                            self.interface_trigger.yfilter != YFilter.not_set or
                            self.prefec_thresh_crossed.yfilter != YFilter.not_set or
                            self.proactive_feature.yfilter != YFilter.not_set or
                            self.proactive_fsm_if_state.yfilter != YFilter.not_set or
                            self.proactive_fsm_state.yfilter != YFilter.not_set or
                            self.proactive_mode.yfilter != YFilter.not_set or
                            self.protection_trigger.yfilter != YFilter.not_set or
                            self.revert_window.yfilter != YFilter.not_set or
                            self.rvrt_ec_cnt.yfilter != YFilter.not_set or
                            self.rvrt_samples.yfilter != YFilter.not_set or
                            self.rvrt_thresh_coeff.yfilter != YFilter.not_set or
                            self.rvrt_thresh_power.yfilter != YFilter.not_set or
                            self.rx_aps.yfilter != YFilter.not_set or
                            self.rx_aps_descr.yfilter != YFilter.not_set or
                            self.tas_state.yfilter != YFilter.not_set or
                            self.trig_ec_cnt.yfilter != YFilter.not_set or
                            self.trig_samples.yfilter != YFilter.not_set or
                            self.trig_thresh_coeff.yfilter != YFilter.not_set or
                            self.trig_thresh_power.yfilter != YFilter.not_set or
                            self.trigger_window.yfilter != YFilter.not_set or
                            self.tx_aps.yfilter != YFilter.not_set or
                            self.tx_aps_descr.yfilter != YFilter.not_set)

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
                        if (self.alarm_state.is_set or self.alarm_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_state.get_name_leafdata())
                        if (self.default_rvrt_thresh_coeff.is_set or self.default_rvrt_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_rvrt_thresh_coeff.get_name_leafdata())
                        if (self.default_rvrt_thresh_power.is_set or self.default_rvrt_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_rvrt_thresh_power.get_name_leafdata())
                        if (self.default_trig_thresh_coeff.is_set or self.default_trig_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_trig_thresh_coeff.get_name_leafdata())
                        if (self.default_trig_thresh_power.is_set or self.default_trig_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_trig_thresh_power.get_name_leafdata())
                        if (self.interface_trigger.is_set or self.interface_trigger.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_trigger.get_name_leafdata())
                        if (self.prefec_thresh_crossed.is_set or self.prefec_thresh_crossed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefec_thresh_crossed.get_name_leafdata())
                        if (self.proactive_feature.is_set or self.proactive_feature.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_feature.get_name_leafdata())
                        if (self.proactive_fsm_if_state.is_set or self.proactive_fsm_if_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_fsm_if_state.get_name_leafdata())
                        if (self.proactive_fsm_state.is_set or self.proactive_fsm_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_fsm_state.get_name_leafdata())
                        if (self.proactive_mode.is_set or self.proactive_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proactive_mode.get_name_leafdata())
                        if (self.protection_trigger.is_set or self.protection_trigger.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protection_trigger.get_name_leafdata())
                        if (self.revert_window.is_set or self.revert_window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.revert_window.get_name_leafdata())
                        if (self.rvrt_ec_cnt.is_set or self.rvrt_ec_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_ec_cnt.get_name_leafdata())
                        if (self.rvrt_samples.is_set or self.rvrt_samples.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_samples.get_name_leafdata())
                        if (self.rvrt_thresh_coeff.is_set or self.rvrt_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_thresh_coeff.get_name_leafdata())
                        if (self.rvrt_thresh_power.is_set or self.rvrt_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rvrt_thresh_power.get_name_leafdata())
                        if (self.rx_aps.is_set or self.rx_aps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_aps.get_name_leafdata())
                        if (self.rx_aps_descr.is_set or self.rx_aps_descr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_aps_descr.get_name_leafdata())
                        if (self.tas_state.is_set or self.tas_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tas_state.get_name_leafdata())
                        if (self.trig_ec_cnt.is_set or self.trig_ec_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_ec_cnt.get_name_leafdata())
                        if (self.trig_samples.is_set or self.trig_samples.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_samples.get_name_leafdata())
                        if (self.trig_thresh_coeff.is_set or self.trig_thresh_coeff.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_thresh_coeff.get_name_leafdata())
                        if (self.trig_thresh_power.is_set or self.trig_thresh_power.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trig_thresh_power.get_name_leafdata())
                        if (self.trigger_window.is_set or self.trigger_window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trigger_window.get_name_leafdata())
                        if (self.tx_aps.is_set or self.tx_aps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_aps.get_name_leafdata())
                        if (self.tx_aps_descr.is_set or self.tx_aps_descr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_aps_descr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "alarm-state" or name == "default-rvrt-thresh-coeff" or name == "default-rvrt-thresh-power" or name == "default-trig-thresh-coeff" or name == "default-trig-thresh-power" or name == "interface-trigger" or name == "prefec-thresh-crossed" or name == "proactive-feature" or name == "proactive-fsm-if-state" or name == "proactive-fsm-state" or name == "proactive-mode" or name == "protection-trigger" or name == "revert-window" or name == "rvrt-ec-cnt" or name == "rvrt-samples" or name == "rvrt-thresh-coeff" or name == "rvrt-thresh-power" or name == "rx-aps" or name == "rx-aps-descr" or name == "tas-state" or name == "trig-ec-cnt" or name == "trig-samples" or name == "trig-thresh-coeff" or name == "trig-thresh-power" or name == "trigger-window" or name == "tx-aps" or name == "tx-aps-descr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "alarm-state"):
                            self.alarm_state = value
                            self.alarm_state.value_namespace = name_space
                            self.alarm_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "default-rvrt-thresh-coeff"):
                            self.default_rvrt_thresh_coeff = value
                            self.default_rvrt_thresh_coeff.value_namespace = name_space
                            self.default_rvrt_thresh_coeff.value_namespace_prefix = name_space_prefix
                        if(value_path == "default-rvrt-thresh-power"):
                            self.default_rvrt_thresh_power = value
                            self.default_rvrt_thresh_power.value_namespace = name_space
                            self.default_rvrt_thresh_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "default-trig-thresh-coeff"):
                            self.default_trig_thresh_coeff = value
                            self.default_trig_thresh_coeff.value_namespace = name_space
                            self.default_trig_thresh_coeff.value_namespace_prefix = name_space_prefix
                        if(value_path == "default-trig-thresh-power"):
                            self.default_trig_thresh_power = value
                            self.default_trig_thresh_power.value_namespace = name_space
                            self.default_trig_thresh_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-trigger"):
                            self.interface_trigger = value
                            self.interface_trigger.value_namespace = name_space
                            self.interface_trigger.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefec-thresh-crossed"):
                            self.prefec_thresh_crossed = value
                            self.prefec_thresh_crossed.value_namespace = name_space
                            self.prefec_thresh_crossed.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-feature"):
                            self.proactive_feature = value
                            self.proactive_feature.value_namespace = name_space
                            self.proactive_feature.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-fsm-if-state"):
                            self.proactive_fsm_if_state = value
                            self.proactive_fsm_if_state.value_namespace = name_space
                            self.proactive_fsm_if_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-fsm-state"):
                            self.proactive_fsm_state = value
                            self.proactive_fsm_state.value_namespace = name_space
                            self.proactive_fsm_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "proactive-mode"):
                            self.proactive_mode = value
                            self.proactive_mode.value_namespace = name_space
                            self.proactive_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "protection-trigger"):
                            self.protection_trigger = value
                            self.protection_trigger.value_namespace = name_space
                            self.protection_trigger.value_namespace_prefix = name_space_prefix
                        if(value_path == "revert-window"):
                            self.revert_window = value
                            self.revert_window.value_namespace = name_space
                            self.revert_window.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-ec-cnt"):
                            self.rvrt_ec_cnt = value
                            self.rvrt_ec_cnt.value_namespace = name_space
                            self.rvrt_ec_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-samples"):
                            self.rvrt_samples = value
                            self.rvrt_samples.value_namespace = name_space
                            self.rvrt_samples.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-thresh-coeff"):
                            self.rvrt_thresh_coeff = value
                            self.rvrt_thresh_coeff.value_namespace = name_space
                            self.rvrt_thresh_coeff.value_namespace_prefix = name_space_prefix
                        if(value_path == "rvrt-thresh-power"):
                            self.rvrt_thresh_power = value
                            self.rvrt_thresh_power.value_namespace = name_space
                            self.rvrt_thresh_power.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-aps"):
                            self.rx_aps = value
                            self.rx_aps.value_namespace = name_space
                            self.rx_aps.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-aps-descr"):
                            self.rx_aps_descr = value
                            self.rx_aps_descr.value_namespace = name_space
                            self.rx_aps_descr.value_namespace_prefix = name_space_prefix
                        if(value_path == "tas-state"):
                            self.tas_state = value
                            self.tas_state.value_namespace = name_space
                            self.tas_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "trig-ec-cnt"):
                            self.trig_ec_cnt = value
                            self.trig_ec_cnt.value_namespace = name_space
                            self.trig_ec_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "trig-samples"):
                            self.trig_samples = value
                            self.trig_samples.value_namespace = name_space
                            self.trig_samples.value_namespace_prefix = name_space_prefix
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
                        if(value_path == "tx-aps"):
                            self.tx_aps = value
                            self.tx_aps.value_namespace = name_space
                            self.tx_aps.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-aps-descr"):
                            self.tx_aps_descr = value
                            self.tx_aps_descr.value_namespace = name_space
                            self.tx_aps_descr.value_namespace_prefix = name_space_prefix


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

                        self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                        self.log_filename = YLeaf(YType.str, "log-filename")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("is_log_enabled",
                                        "log_filename") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dwdm.Ports.Port.Info.SignalLog, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dwdm.Ports.Port.Info.SignalLog, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.is_log_enabled.is_set or
                            self.log_filename.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.is_log_enabled.yfilter != YFilter.not_set or
                            self.log_filename.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "signal-log" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                        if (self.log_filename.is_set or self.log_filename.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.log_filename.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "is-log-enabled" or name == "log-filename"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "is-log-enabled"):
                            self.is_log_enabled = value
                            self.is_log_enabled.value_namespace = name_space
                            self.is_log_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "log-filename"):
                            self.log_filename = value
                            self.log_filename.value_namespace = name_space
                            self.log_filename.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.controller_state.is_set or
                        self.slice_state.is_set or
                        self.transport_admin_state.is_set or
                        (self.g709_info is not None and self.g709_info.has_data()) or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_data()) or
                        (self.optics_info is not None and self.optics_info.has_data()) or
                        (self.proactive is not None and self.proactive.has_data()) or
                        (self.signal_log is not None and self.signal_log.has_data()) or
                        (self.tdc_info is not None and self.tdc_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.controller_state.yfilter != YFilter.not_set or
                        self.slice_state.yfilter != YFilter.not_set or
                        self.transport_admin_state.yfilter != YFilter.not_set or
                        (self.g709_info is not None and self.g709_info.has_operation()) or
                        (self.network_srlg_info is not None and self.network_srlg_info.has_operation()) or
                        (self.optics_info is not None and self.optics_info.has_operation()) or
                        (self.proactive is not None and self.proactive.has_operation()) or
                        (self.signal_log is not None and self.signal_log.has_operation()) or
                        (self.tdc_info is not None and self.tdc_info.has_operation()))

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
                    if (self.controller_state.is_set or self.controller_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.controller_state.get_name_leafdata())
                    if (self.slice_state.is_set or self.slice_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slice_state.get_name_leafdata())
                    if (self.transport_admin_state.is_set or self.transport_admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transport_admin_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "g709-info"):
                        if (self.g709_info is None):
                            self.g709_info = Dwdm.Ports.Port.Info.G709Info()
                            self.g709_info.parent = self
                            self._children_name_map["g709_info"] = "g709-info"
                        return self.g709_info

                    if (child_yang_name == "network-srlg-info"):
                        if (self.network_srlg_info is None):
                            self.network_srlg_info = Dwdm.Ports.Port.Info.NetworkSrlgInfo()
                            self.network_srlg_info.parent = self
                            self._children_name_map["network_srlg_info"] = "network-srlg-info"
                        return self.network_srlg_info

                    if (child_yang_name == "optics-info"):
                        if (self.optics_info is None):
                            self.optics_info = Dwdm.Ports.Port.Info.OpticsInfo()
                            self.optics_info.parent = self
                            self._children_name_map["optics_info"] = "optics-info"
                        return self.optics_info

                    if (child_yang_name == "proactive"):
                        if (self.proactive is None):
                            self.proactive = Dwdm.Ports.Port.Info.Proactive()
                            self.proactive.parent = self
                            self._children_name_map["proactive"] = "proactive"
                        return self.proactive

                    if (child_yang_name == "signal-log"):
                        if (self.signal_log is None):
                            self.signal_log = Dwdm.Ports.Port.Info.SignalLog()
                            self.signal_log.parent = self
                            self._children_name_map["signal_log"] = "signal-log"
                        return self.signal_log

                    if (child_yang_name == "tdc-info"):
                        if (self.tdc_info is None):
                            self.tdc_info = Dwdm.Ports.Port.Info.TdcInfo()
                            self.tdc_info.parent = self
                            self._children_name_map["tdc_info"] = "tdc-info"
                        return self.tdc_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "g709-info" or name == "network-srlg-info" or name == "optics-info" or name == "proactive" or name == "signal-log" or name == "tdc-info" or name == "controller-state" or name == "slice-state" or name == "transport-admin-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "controller-state"):
                        self.controller_state = value
                        self.controller_state.value_namespace = name_space
                        self.controller_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "slice-state"):
                        self.slice_state = value
                        self.slice_state.value_namespace = name_space
                        self.slice_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "transport-admin-state"):
                        self.transport_admin_state = value
                        self.transport_admin_state.value_namespace = name_space
                        self.transport_admin_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.info is not None and self.info.has_data()) or
                    (self.optics is not None and self.optics.has_data()) or
                    (self.prbs is not None and self.prbs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.info is not None and self.info.has_operation()) or
                    (self.optics is not None and self.optics.has_operation()) or
                    (self.prbs is not None and self.prbs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "port" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:dwdm/ports/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "info"):
                    if (self.info is None):
                        self.info = Dwdm.Ports.Port.Info()
                        self.info.parent = self
                        self._children_name_map["info"] = "info"
                    return self.info

                if (child_yang_name == "optics"):
                    if (self.optics is None):
                        self.optics = Dwdm.Ports.Port.Optics()
                        self.optics.parent = self
                        self._children_name_map["optics"] = "optics"
                    return self.optics

                if (child_yang_name == "prbs"):
                    if (self.prbs is None):
                        self.prbs = Dwdm.Ports.Port.Prbs()
                        self.prbs.parent = self
                        self._children_name_map["prbs"] = "prbs"
                    return self.prbs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "info" or name == "optics" or name == "prbs" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.port:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.port:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ports" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:dwdm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "port"):
                for c in self.port:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Dwdm.Ports.Port()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.port.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "port"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.ports is not None and self.ports.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ports is not None and self.ports.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:dwdm" + path_buffer

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

        if (child_yang_name == "ports"):
            if (self.ports is None):
                self.ports = Dwdm.Ports()
                self.ports.parent = self
                self._children_name_map["ports"] = "ports"
            return self.ports

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ports"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

        self.dwdm_vtxp = Vtxp.DwdmVtxp()
        self.dwdm_vtxp.parent = self
        self._children_name_map["dwdm_vtxp"] = "dwdm-vtxp"
        self._children_yang_names.add("dwdm-vtxp")


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

            self.port_vtxps = Vtxp.DwdmVtxp.PortVtxps()
            self.port_vtxps.parent = self
            self._children_name_map["port_vtxps"] = "port-vtxps"
            self._children_yang_names.add("port-vtxps")


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

                self.port_vtxp = YList(self)

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
                            super(Vtxp.DwdmVtxp.PortVtxps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vtxp.DwdmVtxp.PortVtxps, self).__setattr__(name, value)


            class PortVtxp(Entity):
                """
                DWDM Port operational data
                
                .. attribute:: name  <key>
                
                	Port name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
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

                    self.name = YLeaf(YType.str, "name")

                    self.info = Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info()
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
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, self).__setattr__(name, value)


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

                        self.vtxp_enable = YLeaf(YType.boolean, "vtxp-enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vtxp_enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, self).__setattr__(name, value)

                    def has_data(self):
                        return self.vtxp_enable.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vtxp_enable.yfilter != YFilter.not_set)

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
                        if (self.vtxp_enable.is_set or self.vtxp_enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vtxp_enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vtxp-enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vtxp-enable"):
                            self.vtxp_enable = value
                            self.vtxp_enable.value_namespace = name_space
                            self.vtxp_enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.info is not None and self.info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.info is not None and self.info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "port-vtxp" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/port-vtxps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "info"):
                        if (self.info is None):
                            self.info = Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info()
                            self.info.parent = self
                            self._children_name_map["info"] = "info"
                        return self.info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "info" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.port_vtxp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.port_vtxp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "port-vtxps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "port-vtxp"):
                    for c in self.port_vtxp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vtxp.DwdmVtxp.PortVtxps.PortVtxp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.port_vtxp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "port-vtxp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.port_vtxps is not None and self.port_vtxps.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.port_vtxps is not None and self.port_vtxps.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dwdm-vtxp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:vtxp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "port-vtxps"):
                if (self.port_vtxps is None):
                    self.port_vtxps = Vtxp.DwdmVtxp.PortVtxps()
                    self.port_vtxps.parent = self
                    self._children_name_map["port_vtxps"] = "port-vtxps"
                return self.port_vtxps

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "port-vtxps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.dwdm_vtxp is not None and self.dwdm_vtxp.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dwdm_vtxp is not None and self.dwdm_vtxp.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-dwdm-ui-oper:vtxp" + path_buffer

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

        if (child_yang_name == "dwdm-vtxp"):
            if (self.dwdm_vtxp is None):
                self.dwdm_vtxp = Vtxp.DwdmVtxp()
                self.dwdm_vtxp.parent = self
                self._children_name_map["dwdm_vtxp"] = "dwdm-vtxp"
            return self.dwdm_vtxp

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dwdm-vtxp"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vtxp()
        return self._top_entity

