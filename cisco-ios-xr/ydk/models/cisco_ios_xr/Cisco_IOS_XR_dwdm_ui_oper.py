""" Cisco_IOS_XR_dwdm_ui_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dwdm\-ui package operational data.

This module contains definitions
for the following management objects\:
  dwdm\: DWDM operational data
  vtxp\: vtxp

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DwdmControllerState(Enum):
    """
    DwdmControllerState (Enum Class)

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
    DwdmWaveChannelOwner (Enum Class)

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
    DwdmtasState (Enum Class)

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
    G709apsByte (Enum Class)

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
    G709efecMode (Enum Class)

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
    G709ppfsmMode (Enum Class)

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
    G709ppfsmState (Enum Class)

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
    G709ppintfState (Enum Class)

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
    G709prbsInterval (Enum Class)

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
    G709prbsMode (Enum Class)

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
    G709prbsPattern (Enum Class)

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
    	**type**\:  :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ports", ("ports", Dwdm.Ports))])
        self._leafs = OrderedDict()

        self.ports = Dwdm.Ports()
        self.ports.parent = self
        self._children_name_map["ports"] = "ports"
        self._segment_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dwdm, [], name, value)


    class Ports(Entity):
        """
        All DWDM Port operational data
        
        .. attribute:: port
        
        	DWDM Port operational data
        	**type**\: list of  		 :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dwdm.Ports, self).__init__()

            self.yang_name = "ports"
            self.yang_parent_name = "dwdm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("port", ("port", Dwdm.Ports.Port))])
            self._leafs = OrderedDict()

            self.port = YList(self)
            self._segment_path = lambda: "ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dwdm.Ports, [], name, value)


        class Port(Entity):
            """
            DWDM Port operational data
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: prbs
            
            	DWDM Port PRBS related data
            	**type**\:  :py:class:`Prbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs>`
            
            .. attribute:: optics
            
            	DWDM Port optics operational data
            	**type**\:  :py:class:`Optics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Optics>`
            
            .. attribute:: info
            
            	DWDM port operational data
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info>`
            
            

            """

            _prefix = 'dwdm-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dwdm.Ports.Port, self).__init__()

                self.yang_name = "port"
                self.yang_parent_name = "ports"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("prbs", ("prbs", Dwdm.Ports.Port.Prbs)), ("optics", ("optics", Dwdm.Ports.Port.Optics)), ("info", ("info", Dwdm.Ports.Port.Info))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.prbs = Dwdm.Ports.Port.Prbs()
                self.prbs.parent = self
                self._children_name_map["prbs"] = "prbs"

                self.optics = Dwdm.Ports.Port.Optics()
                self.optics.parent = self
                self._children_name_map["optics"] = "optics"

                self.info = Dwdm.Ports.Port.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._segment_path = lambda: "port" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:dwdm/ports/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dwdm.Ports.Port, ['name'], name, value)


            class Prbs(Entity):
                """
                DWDM Port PRBS related data
                
                .. attribute:: twenty_four_hours_bucket
                
                	Port 24\-hour PRBS statistics table
                	**type**\:  :py:class:`TwentyFourHoursBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket>`
                
                .. attribute:: fifteen_minutes_bucket
                
                	Port 15\-minute PRBS statistics table
                	**type**\:  :py:class:`FifteenMinutesBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Prbs, self).__init__()

                    self.yang_name = "prbs"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("twenty-four-hours-bucket", ("twenty_four_hours_bucket", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket)), ("fifteen-minutes-bucket", ("fifteen_minutes_bucket", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket))])
                    self._leafs = OrderedDict()

                    self.twenty_four_hours_bucket = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket()
                    self.twenty_four_hours_bucket.parent = self
                    self._children_name_map["twenty_four_hours_bucket"] = "twenty-four-hours-bucket"

                    self.fifteen_minutes_bucket = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket()
                    self.fifteen_minutes_bucket.parent = self
                    self._children_name_map["fifteen_minutes_bucket"] = "fifteen-minutes-bucket"
                    self._segment_path = lambda: "prbs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dwdm.Ports.Port.Prbs, [], name, value)


                class TwentyFourHoursBucket(Entity):
                    """
                    Port 24\-hour PRBS statistics table
                    
                    .. attribute:: twenty_four_hours_statistics
                    
                    	Port 24\-hour PRBS statistics data
                    	**type**\:  :py:class:`TwentyFourHoursStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket, self).__init__()

                        self.yang_name = "twenty-four-hours-bucket"
                        self.yang_parent_name = "prbs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("twenty-four-hours-statistics", ("twenty_four_hours_statistics", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics))])
                        self._leafs = OrderedDict()

                        self.twenty_four_hours_statistics = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics()
                        self.twenty_four_hours_statistics.parent = self
                        self._children_name_map["twenty_four_hours_statistics"] = "twenty-four-hours-statistics"
                        self._segment_path = lambda: "twenty-four-hours-bucket"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket, [], name, value)


                    class TwentyFourHoursStatistics(Entity):
                        """
                        Port 24\-hour PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\: bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:  :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of  		 :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, self).__init__()

                            self.yang_name = "twenty-four-hours-statistics"
                            self.yang_parent_name = "twenty-four-hours-bucket"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prbs-entry", ("prbs_entry", Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry))])
                            self._leafs = OrderedDict([
                                ('is_prbs_enabled', (YLeaf(YType.boolean, 'is-prbs-enabled'), ['bool'])),
                                ('prbs_config_mode', (YLeaf(YType.enumeration, 'prbs-config-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsMode', '')])),
                            ])
                            self.is_prbs_enabled = None
                            self.prbs_config_mode = None

                            self.prbs_entry = YList(self)
                            self._segment_path = lambda: "twenty-four-hours-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics, ['is_prbs_enabled', 'prbs_config_mode'], name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: interval_index
                            
                            	Index of bucket, current and previous
                            	**type**\:  :py:class:`G709prbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsInterval>`
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:  :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: start_at
                            
                            	Interval start timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: stop_at
                            
                            	Interval stop timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: received_pattern
                            
                            	Received Pattern of PRBS Test
                            	**type**\:  :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: found_count
                            
                            	Count of pattern found in interval
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lost_count
                            
                            	Count of pattern lost in interval
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: found_at
                            
                            	Pattern first found at timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: lost_at
                            
                            	Pattern first lost at timestamp
                            	**type**\: str
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interval_index', (YLeaf(YType.enumeration, 'interval-index'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsInterval', '')])),
                                    ('configured_pattern', (YLeaf(YType.enumeration, 'configured-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsPattern', '')])),
                                    ('start_at', (YLeaf(YType.str, 'start-at'), ['str'])),
                                    ('stop_at', (YLeaf(YType.str, 'stop-at'), ['str'])),
                                    ('received_pattern', (YLeaf(YType.enumeration, 'received-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsPattern', '')])),
                                    ('bit_error_count', (YLeaf(YType.uint64, 'bit-error-count'), ['int'])),
                                    ('found_count', (YLeaf(YType.uint64, 'found-count'), ['int'])),
                                    ('lost_count', (YLeaf(YType.uint64, 'lost-count'), ['int'])),
                                    ('found_at', (YLeaf(YType.str, 'found-at'), ['str'])),
                                    ('lost_at', (YLeaf(YType.str, 'lost-at'), ['str'])),
                                ])
                                self.interval_index = None
                                self.configured_pattern = None
                                self.start_at = None
                                self.stop_at = None
                                self.received_pattern = None
                                self.bit_error_count = None
                                self.found_count = None
                                self.lost_count = None
                                self.found_at = None
                                self.lost_at = None
                                self._segment_path = lambda: "prbs-entry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry, ['interval_index', 'configured_pattern', 'start_at', 'stop_at', 'received_pattern', 'bit_error_count', 'found_count', 'lost_count', 'found_at', 'lost_at'], name, value)


                class FifteenMinutesBucket(Entity):
                    """
                    Port 15\-minute PRBS statistics table
                    
                    .. attribute:: fifteen_minutes_statistics
                    
                    	Port 15\-minute PRBS statistics data
                    	**type**\:  :py:class:`FifteenMinutesStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket, self).__init__()

                        self.yang_name = "fifteen-minutes-bucket"
                        self.yang_parent_name = "prbs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("fifteen-minutes-statistics", ("fifteen_minutes_statistics", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics))])
                        self._leafs = OrderedDict()

                        self.fifteen_minutes_statistics = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics()
                        self.fifteen_minutes_statistics.parent = self
                        self._children_name_map["fifteen_minutes_statistics"] = "fifteen-minutes-statistics"
                        self._segment_path = lambda: "fifteen-minutes-bucket"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket, [], name, value)


                    class FifteenMinutesStatistics(Entity):
                        """
                        Port 15\-minute PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\: bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:  :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of  		 :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, self).__init__()

                            self.yang_name = "fifteen-minutes-statistics"
                            self.yang_parent_name = "fifteen-minutes-bucket"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prbs-entry", ("prbs_entry", Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry))])
                            self._leafs = OrderedDict([
                                ('is_prbs_enabled', (YLeaf(YType.boolean, 'is-prbs-enabled'), ['bool'])),
                                ('prbs_config_mode', (YLeaf(YType.enumeration, 'prbs-config-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsMode', '')])),
                            ])
                            self.is_prbs_enabled = None
                            self.prbs_config_mode = None

                            self.prbs_entry = YList(self)
                            self._segment_path = lambda: "fifteen-minutes-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics, ['is_prbs_enabled', 'prbs_config_mode'], name, value)


                        class PrbsEntry(Entity):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: interval_index
                            
                            	Index of bucket, current and previous
                            	**type**\:  :py:class:`G709prbsInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsInterval>`
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:  :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: start_at
                            
                            	Interval start timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: stop_at
                            
                            	Interval stop timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: received_pattern
                            
                            	Received Pattern of PRBS Test
                            	**type**\:  :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: found_count
                            
                            	Count of pattern found in interval
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lost_count
                            
                            	Count of pattern lost in interval
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: found_at
                            
                            	Pattern first found at timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: lost_at
                            
                            	Pattern first lost at timestamp
                            	**type**\: str
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interval_index', (YLeaf(YType.enumeration, 'interval-index'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsInterval', '')])),
                                    ('configured_pattern', (YLeaf(YType.enumeration, 'configured-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsPattern', '')])),
                                    ('start_at', (YLeaf(YType.str, 'start-at'), ['str'])),
                                    ('stop_at', (YLeaf(YType.str, 'stop-at'), ['str'])),
                                    ('received_pattern', (YLeaf(YType.enumeration, 'received-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsPattern', '')])),
                                    ('bit_error_count', (YLeaf(YType.uint64, 'bit-error-count'), ['int'])),
                                    ('found_count', (YLeaf(YType.uint64, 'found-count'), ['int'])),
                                    ('lost_count', (YLeaf(YType.uint64, 'lost-count'), ['int'])),
                                    ('found_at', (YLeaf(YType.str, 'found-at'), ['str'])),
                                    ('lost_at', (YLeaf(YType.str, 'lost-at'), ['str'])),
                                ])
                                self.interval_index = None
                                self.configured_pattern = None
                                self.start_at = None
                                self.stop_at = None
                                self.received_pattern = None
                                self.bit_error_count = None
                                self.found_count = None
                                self.lost_count = None
                                self.found_at = None
                                self.lost_at = None
                                self._segment_path = lambda: "prbs-entry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry, ['interval_index', 'configured_pattern', 'start_at', 'stop_at', 'received_pattern', 'bit_error_count', 'found_count', 'lost_count', 'found_at', 'lost_at'], name, value)


            class Optics(Entity):
                """
                DWDM Port optics operational data
                
                .. attribute:: wave_info
                
                	DWDM port wavelength information data
                	**type**\:  :py:class:`WaveInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Optics.WaveInfo>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Optics, self).__init__()

                    self.yang_name = "optics"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("wave-info", ("wave_info", Dwdm.Ports.Port.Optics.WaveInfo))])
                    self._leafs = OrderedDict()

                    self.wave_info = Dwdm.Ports.Port.Optics.WaveInfo()
                    self.wave_info.parent = self
                    self._children_name_map["wave_info"] = "wave-info"
                    self._segment_path = lambda: "optics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dwdm.Ports.Port.Optics, [], name, value)


                class WaveInfo(Entity):
                    """
                    DWDM port wavelength information data
                    
                    .. attribute:: wave_band
                    
                    	Wavelength band
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel_min
                    
                    	Lowest ITU wavelength channel number supported
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel_max
                    
                    	Highest ITU wavelength channel number supported
                    	**type**\: int
                    
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
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('wave_band', (YLeaf(YType.uint32, 'wave-band'), ['int'])),
                            ('wave_channel_min', (YLeaf(YType.uint32, 'wave-channel-min'), ['int'])),
                            ('wave_channel_max', (YLeaf(YType.uint32, 'wave-channel-max'), ['int'])),
                        ])
                        self.wave_band = None
                        self.wave_channel_min = None
                        self.wave_channel_max = None
                        self._segment_path = lambda: "wave-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Optics.WaveInfo, ['wave_band', 'wave_channel_min', 'wave_channel_max'], name, value)


            class Info(Entity):
                """
                DWDM port operational data
                
                .. attribute:: g709_info
                
                	G709 operational information
                	**type**\:  :py:class:`G709Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info>`
                
                .. attribute:: optics_info
                
                	Optics operational information
                	**type**\:  :py:class:`OpticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.OpticsInfo>`
                
                .. attribute:: tdc_info
                
                	TDC operational information
                	**type**\:  :py:class:`TdcInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.TdcInfo>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\:  :py:class:`NetworkSrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.NetworkSrlgInfo>`
                
                .. attribute:: proactive
                
                	Proactive protection information
                	**type**\:  :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.Proactive>`
                
                .. attribute:: signal_log
                
                	Signal log information
                	**type**\:  :py:class:`SignalLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.SignalLog>`
                
                .. attribute:: controller_state
                
                	DWDM controller state\: Up, Down or Administratively Down
                	**type**\:  :py:class:`DwdmControllerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmControllerState>`
                
                .. attribute:: transport_admin_state
                
                	DWDM controller TAS state\: IS, OOS, OOS\-MT or IS\-CFG
                	**type**\:  :py:class:`DwdmtasState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasState>`
                
                .. attribute:: slice_state
                
                	DWDM port slice state Up/Down
                	**type**\: bool
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dwdm.Ports.Port.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("g709-info", ("g709_info", Dwdm.Ports.Port.Info.G709Info)), ("optics-info", ("optics_info", Dwdm.Ports.Port.Info.OpticsInfo)), ("tdc-info", ("tdc_info", Dwdm.Ports.Port.Info.TdcInfo)), ("network-srlg-info", ("network_srlg_info", Dwdm.Ports.Port.Info.NetworkSrlgInfo)), ("proactive", ("proactive", Dwdm.Ports.Port.Info.Proactive)), ("signal-log", ("signal_log", Dwdm.Ports.Port.Info.SignalLog))])
                    self._leafs = OrderedDict([
                        ('controller_state', (YLeaf(YType.enumeration, 'controller-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmControllerState', '')])),
                        ('transport_admin_state', (YLeaf(YType.enumeration, 'transport-admin-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmtasState', '')])),
                        ('slice_state', (YLeaf(YType.boolean, 'slice-state'), ['bool'])),
                    ])
                    self.controller_state = None
                    self.transport_admin_state = None
                    self.slice_state = None

                    self.g709_info = Dwdm.Ports.Port.Info.G709Info()
                    self.g709_info.parent = self
                    self._children_name_map["g709_info"] = "g709-info"

                    self.optics_info = Dwdm.Ports.Port.Info.OpticsInfo()
                    self.optics_info.parent = self
                    self._children_name_map["optics_info"] = "optics-info"

                    self.tdc_info = Dwdm.Ports.Port.Info.TdcInfo()
                    self.tdc_info.parent = self
                    self._children_name_map["tdc_info"] = "tdc-info"

                    self.network_srlg_info = Dwdm.Ports.Port.Info.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self._children_name_map["network_srlg_info"] = "network-srlg-info"

                    self.proactive = Dwdm.Ports.Port.Info.Proactive()
                    self.proactive.parent = self
                    self._children_name_map["proactive"] = "proactive"

                    self.signal_log = Dwdm.Ports.Port.Info.SignalLog()
                    self.signal_log.parent = self
                    self._children_name_map["signal_log"] = "signal-log"
                    self._segment_path = lambda: "info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dwdm.Ports.Port.Info, ['controller_state', 'transport_admin_state', 'slice_state'], name, value)


                class G709Info(Entity):
                    """
                    G709 operational information
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:  :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.FecMismatch>`
                    
                    .. attribute:: ec_tca
                    
                    	FEC Corrected bits TCA information
                    	**type**\:  :py:class:`EcTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.EcTca>`
                    
                    .. attribute:: uc_tca
                    
                    	FEC uncorrected words TCA information
                    	**type**\:  :py:class:`UcTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.UcTca>`
                    
                    .. attribute:: otu_info
                    
                    	OTU layer information
                    	**type**\:  :py:class:`OtuInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo>`
                    
                    .. attribute:: odu_info
                    
                    	ODU layer Information
                    	**type**\:  :py:class:`OduInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo>`
                    
                    .. attribute:: is_g709_enabled
                    
                    	 Is G709 framing enabled
                    	**type**\: bool
                    
                    .. attribute:: is_fec_mode_default
                    
                    	 Is Operating FEC Mode Default
                    	**type**\: bool
                    
                    .. attribute:: fec_mode
                    
                    	FEC information
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: remote_fec_mode
                    
                    	Remote FEC information
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: efec_mode
                    
                    	EFEC information
                    	**type**\:  :py:class:`G709efecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709efecMode>`
                    
                    .. attribute:: loopback_mode
                    
                    	Loopback information
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ec
                    
                    	Corrected bit error counter 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ec_accum
                    
                    	FEC Corrected bit error accumulated counter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: uc
                    
                    	FEC Uncorrected words counter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_ber
                    
                    	pre fec ber calculated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fec_ber_man
                    
                    	pre fec ber calculated
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: q
                    
                    	q value calculated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: q_margin
                    
                    	q margin calculated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: fe_cstr
                    
                    	FEC BER String 
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: qstr
                    
                    	Q String 
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: qmargin_str
                    
                    	QMargin String
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: network_port_id
                    
                    	Network port ID
                    	**type**\: str
                    
                    	**length:** 0..65
                    
                    .. attribute:: network_conn_id
                    
                    	Network connection ID
                    	**type**\: str
                    
                    	**length:** 0..65
                    
                    .. attribute:: is_prbs_enabled
                    
                    	'true' if Prbs is enabled 'false' otherwise
                    	**type**\: bool
                    
                    .. attribute:: g709_prbs_mode
                    
                    	Configured mode of PRBS Test
                    	**type**\:  :py:class:`G709prbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsMode>`
                    
                    .. attribute:: g709_prbs_pattern
                    
                    	Pattern of PRBS Test
                    	**type**\:  :py:class:`G709prbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709prbsPattern>`
                    
                    .. attribute:: prbs_time_stamp
                    
                    	Time stamp for prbs configuration
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.G709Info, self).__init__()

                        self.yang_name = "g709-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("fec-mismatch", ("fec_mismatch", Dwdm.Ports.Port.Info.G709Info.FecMismatch)), ("ec-tca", ("ec_tca", Dwdm.Ports.Port.Info.G709Info.EcTca)), ("uc-tca", ("uc_tca", Dwdm.Ports.Port.Info.G709Info.UcTca)), ("otu-info", ("otu_info", Dwdm.Ports.Port.Info.G709Info.OtuInfo)), ("odu-info", ("odu_info", Dwdm.Ports.Port.Info.G709Info.OduInfo))])
                        self._leafs = OrderedDict([
                            ('is_g709_enabled', (YLeaf(YType.boolean, 'is-g709-enabled'), ['bool'])),
                            ('is_fec_mode_default', (YLeaf(YType.boolean, 'is-fec-mode-default'), ['bool'])),
                            ('fec_mode', (YLeaf(YType.int32, 'fec-mode'), ['int'])),
                            ('remote_fec_mode', (YLeaf(YType.int32, 'remote-fec-mode'), ['int'])),
                            ('efec_mode', (YLeaf(YType.enumeration, 'efec-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709efecMode', '')])),
                            ('loopback_mode', (YLeaf(YType.int32, 'loopback-mode'), ['int'])),
                            ('ec', (YLeaf(YType.uint64, 'ec'), ['int'])),
                            ('ec_accum', (YLeaf(YType.uint64, 'ec-accum'), ['int'])),
                            ('uc', (YLeaf(YType.uint64, 'uc'), ['int'])),
                            ('fec_ber', (YLeaf(YType.uint64, 'fec-ber'), ['int'])),
                            ('fec_ber_man', (YLeaf(YType.int32, 'fec-ber-man'), ['int'])),
                            ('q', (YLeaf(YType.uint64, 'q'), ['int'])),
                            ('q_margin', (YLeaf(YType.uint64, 'q-margin'), ['int'])),
                            ('fe_cstr', (YLeaf(YType.str, 'fe-cstr'), ['str'])),
                            ('qstr', (YLeaf(YType.str, 'qstr'), ['str'])),
                            ('qmargin_str', (YLeaf(YType.str, 'qmargin-str'), ['str'])),
                            ('network_port_id', (YLeaf(YType.str, 'network-port-id'), ['str'])),
                            ('network_conn_id', (YLeaf(YType.str, 'network-conn-id'), ['str'])),
                            ('is_prbs_enabled', (YLeaf(YType.boolean, 'is-prbs-enabled'), ['bool'])),
                            ('g709_prbs_mode', (YLeaf(YType.enumeration, 'g709-prbs-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsMode', '')])),
                            ('g709_prbs_pattern', (YLeaf(YType.enumeration, 'g709-prbs-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709prbsPattern', '')])),
                            ('prbs_time_stamp', (YLeaf(YType.uint64, 'prbs-time-stamp'), ['int'])),
                        ])
                        self.is_g709_enabled = None
                        self.is_fec_mode_default = None
                        self.fec_mode = None
                        self.remote_fec_mode = None
                        self.efec_mode = None
                        self.loopback_mode = None
                        self.ec = None
                        self.ec_accum = None
                        self.uc = None
                        self.fec_ber = None
                        self.fec_ber_man = None
                        self.q = None
                        self.q_margin = None
                        self.fe_cstr = None
                        self.qstr = None
                        self.qmargin_str = None
                        self.network_port_id = None
                        self.network_conn_id = None
                        self.is_prbs_enabled = None
                        self.g709_prbs_mode = None
                        self.g709_prbs_pattern = None
                        self.prbs_time_stamp = None

                        self.fec_mismatch = Dwdm.Ports.Port.Info.G709Info.FecMismatch()
                        self.fec_mismatch.parent = self
                        self._children_name_map["fec_mismatch"] = "fec-mismatch"

                        self.ec_tca = Dwdm.Ports.Port.Info.G709Info.EcTca()
                        self.ec_tca.parent = self
                        self._children_name_map["ec_tca"] = "ec-tca"

                        self.uc_tca = Dwdm.Ports.Port.Info.G709Info.UcTca()
                        self.uc_tca.parent = self
                        self._children_name_map["uc_tca"] = "uc-tca"

                        self.otu_info = Dwdm.Ports.Port.Info.G709Info.OtuInfo()
                        self.otu_info.parent = self
                        self._children_name_map["otu_info"] = "otu-info"

                        self.odu_info = Dwdm.Ports.Port.Info.G709Info.OduInfo()
                        self.odu_info.parent = self
                        self._children_name_map["odu_info"] = "odu-info"
                        self._segment_path = lambda: "g709-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.G709Info, ['is_g709_enabled', 'is_fec_mode_default', 'fec_mode', 'remote_fec_mode', 'efec_mode', 'loopback_mode', 'ec', 'ec_accum', 'uc', 'fec_ber', 'fec_ber_man', 'q', 'q_margin', 'fe_cstr', 'qstr', 'qmargin_str', 'network_port_id', 'network_conn_id', 'is_prbs_enabled', 'g709_prbs_mode', 'g709_prbs_pattern', 'prbs_time_stamp'], name, value)


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

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.FecMismatch, self).__init__()

                            self.yang_name = "fec-mismatch"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "fec-mismatch"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.FecMismatch, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                    class EcTca(Entity):
                        """
                        FEC Corrected bits TCA information
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: threshold
                        
                        	Error threshold power
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: counter
                        
                        	Error counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.EcTca, self).__init__()

                            self.yang_name = "ec-tca"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.threshold = None
                            self.counter = None
                            self._segment_path = lambda: "ec-tca"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.EcTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                    class UcTca(Entity):
                        """
                        FEC uncorrected words TCA information
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: threshold
                        
                        	Error threshold power
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: counter
                        
                        	Error counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.UcTca, self).__init__()

                            self.yang_name = "uc-tca"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.threshold = None
                            self.counter = None
                            self._segment_path = lambda: "uc-tca"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.UcTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                    class OtuInfo(Entity):
                        """
                        OTU layer information
                        
                        .. attribute:: los
                        
                        	Loss of Signal information
                        	**type**\:  :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los>`
                        
                        .. attribute:: lof
                        
                        	Loss of Frame information
                        	**type**\:  :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof>`
                        
                        .. attribute:: lom
                        
                        	Loss of MultiFrame information
                        	**type**\:  :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom>`
                        
                        .. attribute:: oof
                        
                        	Out of Frame information
                        	**type**\:  :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof>`
                        
                        .. attribute:: oom
                        
                        	Out of MultiFrame information
                        	**type**\:  :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom>`
                        
                        .. attribute:: ais
                        
                        	Alarm Indication Signal information
                        	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais>`
                        
                        .. attribute:: iae
                        
                        	Incoming Alignment Error information
                        	**type**\:  :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae>`
                        
                        .. attribute:: bdi
                        
                        	Backward Defect Indication information
                        	**type**\:  :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi>`
                        
                        .. attribute:: tim
                        
                        	Trace Identifier Mismatch information
                        	**type**\:  :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim>`
                        
                        .. attribute:: eoc
                        
                        	GCC End of Channel information
                        	**type**\:  :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc>`
                        
                        .. attribute:: sf_ber
                        
                        	Signal Fail  BER information
                        	**type**\:  :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer>`
                        
                        .. attribute:: sd_ber
                        
                        	Signal Degrade BER information
                        	**type**\:  :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer>`
                        
                        .. attribute:: prefec_sf_ber
                        
                        	Prefec Signal Fail BER information
                        	**type**\:  :py:class:`PrefecSfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer>`
                        
                        .. attribute:: prefec_sd_ber
                        
                        	Prefec Signal Degrade BER information
                        	**type**\:  :py:class:`PrefecSdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer>`
                        
                        .. attribute:: bbe_tca
                        
                        	 Backgound Block Error TCA information
                        	**type**\:  :py:class:`BbeTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca>`
                        
                        .. attribute:: es_tca
                        
                        	Errored Seconds TCA information
                        	**type**\:  :py:class:`EsTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca>`
                        
                        .. attribute:: bbe
                        
                        	Backgound Block Error information
                        	**type**\:  :py:class:`Bbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe>`
                        
                        .. attribute:: es
                        
                        	Errored Seconds information 
                        	**type**\:  :py:class:`Es <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es>`
                        
                        .. attribute:: ses
                        
                        	Severly Errored Seconds information
                        	**type**\:  :py:class:`Ses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses>`
                        
                        .. attribute:: uas
                        
                        	Unavailability Seconds information
                        	**type**\:  :py:class:`Uas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas>`
                        
                        .. attribute:: fc
                        
                        	Failure Count information
                        	**type**\:  :py:class:`Fc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc>`
                        
                        .. attribute:: bber
                        
                        	Backgound Block Error Rate information
                        	**type**\:  :py:class:`Bber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber>`
                        
                        .. attribute:: esr
                        
                        	Errored Seconds Rate information
                        	**type**\:  :py:class:`Esr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr>`
                        
                        .. attribute:: sesr
                        
                        	Severly Errored Seconds Rate information
                        	**type**\:  :py:class:`Sesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr>`
                        
                        .. attribute:: tti
                        
                        	Trail Trace Identifier information
                        	**type**\:  :py:class:`Tti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti>`
                        
                        .. attribute:: bei
                        
                        	Backward Error Indication counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bip
                        
                        	Bit Interleave Parity(BIP) counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.OtuInfo, self).__init__()

                            self.yang_name = "otu-info"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("los", ("los", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los)), ("lof", ("lof", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof)), ("lom", ("lom", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom)), ("oof", ("oof", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof)), ("oom", ("oom", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom)), ("ais", ("ais", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais)), ("iae", ("iae", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae)), ("bdi", ("bdi", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi)), ("tim", ("tim", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim)), ("eoc", ("eoc", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc)), ("sf-ber", ("sf_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer)), ("sd-ber", ("sd_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer)), ("prefec-sf-ber", ("prefec_sf_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer)), ("prefec-sd-ber", ("prefec_sd_ber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer)), ("bbe-tca", ("bbe_tca", Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca)), ("es-tca", ("es_tca", Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca)), ("bbe", ("bbe", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe)), ("es", ("es", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es)), ("ses", ("ses", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses)), ("uas", ("uas", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas)), ("fc", ("fc", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc)), ("bber", ("bber", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber)), ("esr", ("esr", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr)), ("sesr", ("sesr", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr)), ("tti", ("tti", Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti))])
                            self._leafs = OrderedDict([
                                ('bei', (YLeaf(YType.uint64, 'bei'), ['int'])),
                                ('bip', (YLeaf(YType.uint64, 'bip'), ['int'])),
                            ])
                            self.bei = None
                            self.bip = None

                            self.los = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los()
                            self.los.parent = self
                            self._children_name_map["los"] = "los"

                            self.lof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof()
                            self.lof.parent = self
                            self._children_name_map["lof"] = "lof"

                            self.lom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom()
                            self.lom.parent = self
                            self._children_name_map["lom"] = "lom"

                            self.oof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof()
                            self.oof.parent = self
                            self._children_name_map["oof"] = "oof"

                            self.oom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom()
                            self.oom.parent = self
                            self._children_name_map["oom"] = "oom"

                            self.ais = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"

                            self.iae = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae()
                            self.iae.parent = self
                            self._children_name_map["iae"] = "iae"

                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi()
                            self.bdi.parent = self
                            self._children_name_map["bdi"] = "bdi"

                            self.tim = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim()
                            self.tim.parent = self
                            self._children_name_map["tim"] = "tim"

                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc()
                            self.eoc.parent = self
                            self._children_name_map["eoc"] = "eoc"

                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer()
                            self.sf_ber.parent = self
                            self._children_name_map["sf_ber"] = "sf-ber"

                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer()
                            self.sd_ber.parent = self
                            self._children_name_map["sd_ber"] = "sd-ber"

                            self.prefec_sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer()
                            self.prefec_sf_ber.parent = self
                            self._children_name_map["prefec_sf_ber"] = "prefec-sf-ber"

                            self.prefec_sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer()
                            self.prefec_sd_ber.parent = self
                            self._children_name_map["prefec_sd_ber"] = "prefec-sd-ber"

                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self._children_name_map["bbe_tca"] = "bbe-tca"

                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca()
                            self.es_tca.parent = self
                            self._children_name_map["es_tca"] = "es-tca"

                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe()
                            self.bbe.parent = self
                            self._children_name_map["bbe"] = "bbe"

                            self.es = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es()
                            self.es.parent = self
                            self._children_name_map["es"] = "es"

                            self.ses = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses()
                            self.ses.parent = self
                            self._children_name_map["ses"] = "ses"

                            self.uas = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas()
                            self.uas.parent = self
                            self._children_name_map["uas"] = "uas"

                            self.fc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc()
                            self.fc.parent = self
                            self._children_name_map["fc"] = "fc"

                            self.bber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber()
                            self.bber.parent = self
                            self._children_name_map["bber"] = "bber"

                            self.esr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr()
                            self.esr.parent = self
                            self._children_name_map["esr"] = "esr"

                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr()
                            self.sesr.parent = self
                            self._children_name_map["sesr"] = "sesr"

                            self.tti = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti()
                            self.tti.parent = self
                            self._children_name_map["tti"] = "tti"
                            self._segment_path = lambda: "otu-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo, ['bei', 'bip'], name, value)


                        class Los(Entity):
                            """
                            Loss of Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, self).__init__()

                                self.yang_name = "los"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "los"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Lof(Entity):
                            """
                            Loss of Frame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, self).__init__()

                                self.yang_name = "lof"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "lof"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Lom(Entity):
                            """
                            Loss of MultiFrame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, self).__init__()

                                self.yang_name = "lom"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "lom"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Oof(Entity):
                            """
                            Out of Frame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, self).__init__()

                                self.yang_name = "oof"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "oof"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Oom(Entity):
                            """
                            Out of MultiFrame information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, self).__init__()

                                self.yang_name = "oom"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "oom"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Ais(Entity):
                            """
                            Alarm Indication Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "ais"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Iae(Entity):
                            """
                            Incoming Alignment Error information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, self).__init__()

                                self.yang_name = "iae"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "iae"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Bdi(Entity):
                            """
                            Backward Defect Indication information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, self).__init__()

                                self.yang_name = "bdi"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "bdi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Tim(Entity):
                            """
                            Trace Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, self).__init__()

                                self.yang_name = "tim"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "tim"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Eoc(Entity):
                            """
                            GCC End of Channel information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, self).__init__()

                                self.yang_name = "eoc"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "eoc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class SfBer(Entity):
                            """
                            Signal Fail  BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, self).__init__()

                                self.yang_name = "sf-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "sf-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class SdBer(Entity):
                            """
                            Signal Degrade BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, self).__init__()

                                self.yang_name = "sd-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "sd-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class PrefecSfBer(Entity):
                            """
                            Prefec Signal Fail BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, self).__init__()

                                self.yang_name = "prefec-sf-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "prefec-sf-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class PrefecSdBer(Entity):
                            """
                            Prefec Signal Degrade BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, self).__init__()

                                self.yang_name = "prefec-sd-ber"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "prefec-sd-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class BbeTca(Entity):
                            """
                             Backgound Block Error TCA information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, self).__init__()

                                self.yang_name = "bbe-tca"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "bbe-tca"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class EsTca(Entity):
                            """
                            Errored Seconds TCA information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, self).__init__()

                                self.yang_name = "es-tca"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "es-tca"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class Bbe(Entity):
                            """
                            Backgound Block Error information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "bbe"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe, ['counter'], name, value)


                        class Es(Entity):
                            """
                            Errored Seconds information 
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "es"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es, ['counter'], name, value)


                        class Ses(Entity):
                            """
                            Severly Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "ses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses, ['counter'], name, value)


                        class Uas(Entity):
                            """
                            Unavailability Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "uas"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas, ['counter'], name, value)


                        class Fc(Entity):
                            """
                            Failure Count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "fc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc, ['counter'], name, value)


                        class Bber(Entity):
                            """
                            Backgound Block Error Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "bber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber, ['counter'], name, value)


                        class Esr(Entity):
                            """
                            Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "esr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr, ['counter'], name, value)


                        class Sesr(Entity):
                            """
                            Severly Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "sesr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr, ['counter'], name, value)


                        class Tti(Entity):
                            """
                            Trail Trace Identifier information
                            
                            .. attribute:: tx_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expected_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tx_tti
                            
                            	Tx TTI String 
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: tx_sapi0
                            
                            	Tx SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_sapi
                            
                            	Tx SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_sapi_range
                            
                            	 Tx SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_dapi0
                            
                            	Tx DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_dapi
                            
                            	Tx DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_dapi_range
                            
                            	 Tx DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_oper_spec
                            
                            	Tx Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: tx_oper_spec_range
                            
                            	 Tx Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_tti
                            
                            	Rx TTI String 
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: rx_sapi0
                            
                            	Rx SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_sapi
                            
                            	Rx SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_sapi_range
                            
                            	 Rx SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_dapi0
                            
                            	Rx DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_dapi
                            
                            	Rx DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_dapi_range
                            
                            	 Rx DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec_range
                            
                            	 Rx Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec
                            
                            	Rx Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: expected_tti
                            
                            	Expected TTI String
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: expected_sapi0
                            
                            	Expected SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_sapi
                            
                            	Expected SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: exp_sapi_range
                            
                            	 Expected SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_dapi0
                            
                            	Expected DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_dapi
                            
                            	Expected DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: exp_dapi_range
                            
                            	 Expected DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_oper_spec
                            
                            	Expected Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: exp_oper_spec_range
                            
                            	 Expected Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, self).__init__()

                                self.yang_name = "tti"
                                self.yang_parent_name = "otu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tx_string_type', (YLeaf(YType.uint32, 'tx-string-type'), ['int'])),
                                    ('expected_string_type', (YLeaf(YType.uint32, 'expected-string-type'), ['int'])),
                                    ('rx_string_type', (YLeaf(YType.uint32, 'rx-string-type'), ['int'])),
                                    ('tx_tti', (YLeaf(YType.str, 'tx-tti'), ['str'])),
                                    ('tx_sapi0', (YLeaf(YType.str, 'tx-sapi0'), ['str'])),
                                    ('tx_sapi', (YLeaf(YType.str, 'tx-sapi'), ['str'])),
                                    ('tx_sapi_range', (YLeaf(YType.str, 'tx-sapi-range'), ['str'])),
                                    ('tx_dapi0', (YLeaf(YType.str, 'tx-dapi0'), ['str'])),
                                    ('tx_dapi', (YLeaf(YType.str, 'tx-dapi'), ['str'])),
                                    ('tx_dapi_range', (YLeaf(YType.str, 'tx-dapi-range'), ['str'])),
                                    ('tx_oper_spec', (YLeaf(YType.str, 'tx-oper-spec'), ['str'])),
                                    ('tx_oper_spec_range', (YLeaf(YType.str, 'tx-oper-spec-range'), ['str'])),
                                    ('rx_tti', (YLeaf(YType.str, 'rx-tti'), ['str'])),
                                    ('rx_sapi0', (YLeaf(YType.str, 'rx-sapi0'), ['str'])),
                                    ('rx_sapi', (YLeaf(YType.str, 'rx-sapi'), ['str'])),
                                    ('rx_sapi_range', (YLeaf(YType.str, 'rx-sapi-range'), ['str'])),
                                    ('rx_dapi0', (YLeaf(YType.str, 'rx-dapi0'), ['str'])),
                                    ('rx_dapi', (YLeaf(YType.str, 'rx-dapi'), ['str'])),
                                    ('rx_dapi_range', (YLeaf(YType.str, 'rx-dapi-range'), ['str'])),
                                    ('rx_oper_spec_range', (YLeaf(YType.str, 'rx-oper-spec-range'), ['str'])),
                                    ('rx_oper_spec', (YLeaf(YType.str, 'rx-oper-spec'), ['str'])),
                                    ('expected_tti', (YLeaf(YType.str, 'expected-tti'), ['str'])),
                                    ('expected_sapi0', (YLeaf(YType.str, 'expected-sapi0'), ['str'])),
                                    ('expected_sapi', (YLeaf(YType.str, 'expected-sapi'), ['str'])),
                                    ('exp_sapi_range', (YLeaf(YType.str, 'exp-sapi-range'), ['str'])),
                                    ('expected_dapi0', (YLeaf(YType.str, 'expected-dapi0'), ['str'])),
                                    ('expected_dapi', (YLeaf(YType.str, 'expected-dapi'), ['str'])),
                                    ('exp_dapi_range', (YLeaf(YType.str, 'exp-dapi-range'), ['str'])),
                                    ('expected_oper_spec', (YLeaf(YType.str, 'expected-oper-spec'), ['str'])),
                                    ('exp_oper_spec_range', (YLeaf(YType.str, 'exp-oper-spec-range'), ['str'])),
                                ])
                                self.tx_string_type = None
                                self.expected_string_type = None
                                self.rx_string_type = None
                                self.tx_tti = None
                                self.tx_sapi0 = None
                                self.tx_sapi = None
                                self.tx_sapi_range = None
                                self.tx_dapi0 = None
                                self.tx_dapi = None
                                self.tx_dapi_range = None
                                self.tx_oper_spec = None
                                self.tx_oper_spec_range = None
                                self.rx_tti = None
                                self.rx_sapi0 = None
                                self.rx_sapi = None
                                self.rx_sapi_range = None
                                self.rx_dapi0 = None
                                self.rx_dapi = None
                                self.rx_dapi_range = None
                                self.rx_oper_spec_range = None
                                self.rx_oper_spec = None
                                self.expected_tti = None
                                self.expected_sapi0 = None
                                self.expected_sapi = None
                                self.exp_sapi_range = None
                                self.expected_dapi0 = None
                                self.expected_dapi = None
                                self.exp_dapi_range = None
                                self.expected_oper_spec = None
                                self.exp_oper_spec_range = None
                                self._segment_path = lambda: "tti"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti, ['tx_string_type', 'expected_string_type', 'rx_string_type', 'tx_tti', 'tx_sapi0', 'tx_sapi', 'tx_sapi_range', 'tx_dapi0', 'tx_dapi', 'tx_dapi_range', 'tx_oper_spec', 'tx_oper_spec_range', 'rx_tti', 'rx_sapi0', 'rx_sapi', 'rx_sapi_range', 'rx_dapi0', 'rx_dapi', 'rx_dapi_range', 'rx_oper_spec_range', 'rx_oper_spec', 'expected_tti', 'expected_sapi0', 'expected_sapi', 'exp_sapi_range', 'expected_dapi0', 'expected_dapi', 'exp_dapi_range', 'expected_oper_spec', 'exp_oper_spec_range'], name, value)


                    class OduInfo(Entity):
                        """
                        ODU layer Information
                        
                        .. attribute:: oci
                        
                        	Open Connection Indiction information
                        	**type**\:  :py:class:`Oci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci>`
                        
                        .. attribute:: ais
                        
                        	Alarm Indication Signal information
                        	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais>`
                        
                        .. attribute:: lck
                        
                        	Upstream Connection Locked information
                        	**type**\:  :py:class:`Lck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck>`
                        
                        .. attribute:: bdi
                        
                        	Backward Defect Indication information
                        	**type**\:  :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi>`
                        
                        .. attribute:: eoc
                        
                        	GCC End of Channel information
                        	**type**\:  :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc>`
                        
                        .. attribute:: ptim
                        
                        	Payload Type Identifier Mismatch information
                        	**type**\:  :py:class:`Ptim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim>`
                        
                        .. attribute:: tim
                        
                        	Trace Identifier Mismatch information
                        	**type**\:  :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim>`
                        
                        .. attribute:: sf_ber
                        
                        	Signal Fail  BER information
                        	**type**\:  :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer>`
                        
                        .. attribute:: sd_ber
                        
                        	Signal Degrade BER information
                        	**type**\:  :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer>`
                        
                        .. attribute:: bbe_tca
                        
                        	Background Block Error TCA information
                        	**type**\:  :py:class:`BbeTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca>`
                        
                        .. attribute:: es_tca
                        
                        	Errored Seconds TCA information
                        	**type**\:  :py:class:`EsTca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca>`
                        
                        .. attribute:: bbe
                        
                        	Background Block Error information
                        	**type**\:  :py:class:`Bbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe>`
                        
                        .. attribute:: es
                        
                        	Errored Seconds information
                        	**type**\:  :py:class:`Es <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Es>`
                        
                        .. attribute:: ses
                        
                        	Severly Errored Seconds information
                        	**type**\:  :py:class:`Ses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses>`
                        
                        .. attribute:: uas
                        
                        	Unavailability Seconds information
                        	**type**\:  :py:class:`Uas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas>`
                        
                        .. attribute:: fc
                        
                        	Failure count information
                        	**type**\:  :py:class:`Fc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc>`
                        
                        .. attribute:: bber
                        
                        	Background Block Error Rate count information
                        	**type**\:  :py:class:`Bber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber>`
                        
                        .. attribute:: esr
                        
                        	Errored Seconds Rate information
                        	**type**\:  :py:class:`Esr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr>`
                        
                        .. attribute:: sesr
                        
                        	Severly Errored Seconds Rate information
                        	**type**\:  :py:class:`Sesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr>`
                        
                        .. attribute:: tti
                        
                        	Trail Trace Identifier information
                        	**type**\:  :py:class:`Tti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti>`
                        
                        .. attribute:: bip
                        
                        	Bit Interleave Parity(BIP) counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bei
                        
                        	Backward Error Indication counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dwdm.Ports.Port.Info.G709Info.OduInfo, self).__init__()

                            self.yang_name = "odu-info"
                            self.yang_parent_name = "g709-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("oci", ("oci", Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci)), ("ais", ("ais", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais)), ("lck", ("lck", Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck)), ("bdi", ("bdi", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi)), ("eoc", ("eoc", Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc)), ("ptim", ("ptim", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim)), ("tim", ("tim", Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim)), ("sf-ber", ("sf_ber", Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer)), ("sd-ber", ("sd_ber", Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer)), ("bbe-tca", ("bbe_tca", Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca)), ("es-tca", ("es_tca", Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca)), ("bbe", ("bbe", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe)), ("es", ("es", Dwdm.Ports.Port.Info.G709Info.OduInfo.Es)), ("ses", ("ses", Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses)), ("uas", ("uas", Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas)), ("fc", ("fc", Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc)), ("bber", ("bber", Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber)), ("esr", ("esr", Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr)), ("sesr", ("sesr", Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr)), ("tti", ("tti", Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti))])
                            self._leafs = OrderedDict([
                                ('bip', (YLeaf(YType.uint64, 'bip'), ['int'])),
                                ('bei', (YLeaf(YType.uint64, 'bei'), ['int'])),
                            ])
                            self.bip = None
                            self.bei = None

                            self.oci = Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci()
                            self.oci.parent = self
                            self._children_name_map["oci"] = "oci"

                            self.ais = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"

                            self.lck = Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck()
                            self.lck.parent = self
                            self._children_name_map["lck"] = "lck"

                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi()
                            self.bdi.parent = self
                            self._children_name_map["bdi"] = "bdi"

                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc()
                            self.eoc.parent = self
                            self._children_name_map["eoc"] = "eoc"

                            self.ptim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim()
                            self.ptim.parent = self
                            self._children_name_map["ptim"] = "ptim"

                            self.tim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim()
                            self.tim.parent = self
                            self._children_name_map["tim"] = "tim"

                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer()
                            self.sf_ber.parent = self
                            self._children_name_map["sf_ber"] = "sf-ber"

                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer()
                            self.sd_ber.parent = self
                            self._children_name_map["sd_ber"] = "sd-ber"

                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self._children_name_map["bbe_tca"] = "bbe-tca"

                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca()
                            self.es_tca.parent = self
                            self._children_name_map["es_tca"] = "es-tca"

                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe()
                            self.bbe.parent = self
                            self._children_name_map["bbe"] = "bbe"

                            self.es = Dwdm.Ports.Port.Info.G709Info.OduInfo.Es()
                            self.es.parent = self
                            self._children_name_map["es"] = "es"

                            self.ses = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses()
                            self.ses.parent = self
                            self._children_name_map["ses"] = "ses"

                            self.uas = Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas()
                            self.uas.parent = self
                            self._children_name_map["uas"] = "uas"

                            self.fc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc()
                            self.fc.parent = self
                            self._children_name_map["fc"] = "fc"

                            self.bber = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber()
                            self.bber.parent = self
                            self._children_name_map["bber"] = "bber"

                            self.esr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr()
                            self.esr.parent = self
                            self._children_name_map["esr"] = "esr"

                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr()
                            self.sesr.parent = self
                            self._children_name_map["sesr"] = "sesr"

                            self.tti = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti()
                            self.tti.parent = self
                            self._children_name_map["tti"] = "tti"
                            self._segment_path = lambda: "odu-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo, ['bip', 'bei'], name, value)


                        class Oci(Entity):
                            """
                            Open Connection Indiction information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, self).__init__()

                                self.yang_name = "oci"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "oci"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Ais(Entity):
                            """
                            Alarm Indication Signal information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "ais"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Lck(Entity):
                            """
                            Upstream Connection Locked information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, self).__init__()

                                self.yang_name = "lck"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "lck"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Bdi(Entity):
                            """
                            Backward Defect Indication information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, self).__init__()

                                self.yang_name = "bdi"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "bdi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Eoc(Entity):
                            """
                            GCC End of Channel information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, self).__init__()

                                self.yang_name = "eoc"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "eoc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Ptim(Entity):
                            """
                            Payload Type Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, self).__init__()

                                self.yang_name = "ptim"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "ptim"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class Tim(Entity):
                            """
                            Trace Identifier Mismatch information
                            
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

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, self).__init__()

                                self.yang_name = "tim"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.counter = None
                                self._segment_path = lambda: "tim"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)


                        class SfBer(Entity):
                            """
                            Signal Fail  BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, self).__init__()

                                self.yang_name = "sf-ber"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "sf-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class SdBer(Entity):
                            """
                            Signal Degrade BER information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, self).__init__()

                                self.yang_name = "sd-ber"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "sd-ber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class BbeTca(Entity):
                            """
                            Background Block Error TCA information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, self).__init__()

                                self.yang_name = "bbe-tca"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "bbe-tca"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class EsTca(Entity):
                            """
                            Errored Seconds TCA information
                            
                            .. attribute:: reporting_enabled
                            
                            	Is reporting enabled?
                            	**type**\: bool
                            
                            .. attribute:: is_detected
                            
                            	Is defect detected?
                            	**type**\: bool
                            
                            .. attribute:: is_asserted
                            
                            	Is defect delared?
                            	**type**\: bool
                            
                            .. attribute:: threshold
                            
                            	Error threshold power
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counter
                            
                            	Error counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, self).__init__()

                                self.yang_name = "es-tca"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                    ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                    ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                    ('threshold', (YLeaf(YType.int32, 'threshold'), ['int'])),
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.reporting_enabled = None
                                self.is_detected = None
                                self.is_asserted = None
                                self.threshold = None
                                self.counter = None
                                self._segment_path = lambda: "es-tca"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca, ['reporting_enabled', 'is_detected', 'is_asserted', 'threshold', 'counter'], name, value)


                        class Bbe(Entity):
                            """
                            Background Block Error information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "bbe"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe, ['counter'], name, value)


                        class Es(Entity):
                            """
                            Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "es"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Es, ['counter'], name, value)


                        class Ses(Entity):
                            """
                            Severly Errored Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "ses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses, ['counter'], name, value)


                        class Uas(Entity):
                            """
                            Unavailability Seconds information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "uas"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas, ['counter'], name, value)


                        class Fc(Entity):
                            """
                            Failure count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "fc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc, ['counter'], name, value)


                        class Bber(Entity):
                            """
                            Background Block Error Rate count information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "bber"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber, ['counter'], name, value)


                        class Esr(Entity):
                            """
                            Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "esr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr, ['counter'], name, value)


                        class Sesr(Entity):
                            """
                            Severly Errored Seconds Rate information
                            
                            .. attribute:: counter
                            
                            	Performance Monitoring counter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                                ])
                                self.counter = None
                                self._segment_path = lambda: "sesr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr, ['counter'], name, value)


                        class Tti(Entity):
                            """
                            Trail Trace Identifier information
                            
                            .. attribute:: tx_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expected_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_string_type
                            
                            	Type of String
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tx_tti
                            
                            	Tx TTI String 
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: tx_sapi0
                            
                            	Tx SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_sapi
                            
                            	Tx SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_sapi_range
                            
                            	 Tx SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_dapi0
                            
                            	Tx DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: tx_dapi
                            
                            	Tx DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: tx_dapi_range
                            
                            	 Tx DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: tx_oper_spec
                            
                            	Tx Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: tx_oper_spec_range
                            
                            	 Tx Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_tti
                            
                            	Rx TTI String 
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: rx_sapi0
                            
                            	Rx SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_sapi
                            
                            	Rx SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_sapi_range
                            
                            	 Rx SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_dapi0
                            
                            	Rx DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: rx_dapi
                            
                            	Rx DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: rx_dapi_range
                            
                            	 Rx DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec_range
                            
                            	 Rx Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: rx_oper_spec
                            
                            	Rx Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: expected_tti
                            
                            	Expected TTI String
                            	**type**\: str
                            
                            	**length:** 0..129
                            
                            .. attribute:: expected_sapi0
                            
                            	Expected SAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_sapi
                            
                            	Expected SAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: exp_sapi_range
                            
                            	 Expected SAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_dapi0
                            
                            	Expected DAPI[0] Field
                            	**type**\: str
                            
                            	**length:** 0..5
                            
                            .. attribute:: expected_dapi
                            
                            	Expected DAPI[1\-15] Field
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: exp_dapi_range
                            
                            	 Expected DAPI Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            .. attribute:: expected_oper_spec
                            
                            	Expected Operator Specific Field
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: exp_oper_spec_range
                            
                            	 Expected Operator Specific Field Range String
                            	**type**\: str
                            
                            	**length:** 0..6
                            
                            

                            """

                            _prefix = 'dwdm-ui-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, self).__init__()

                                self.yang_name = "tti"
                                self.yang_parent_name = "odu-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tx_string_type', (YLeaf(YType.uint32, 'tx-string-type'), ['int'])),
                                    ('expected_string_type', (YLeaf(YType.uint32, 'expected-string-type'), ['int'])),
                                    ('rx_string_type', (YLeaf(YType.uint32, 'rx-string-type'), ['int'])),
                                    ('tx_tti', (YLeaf(YType.str, 'tx-tti'), ['str'])),
                                    ('tx_sapi0', (YLeaf(YType.str, 'tx-sapi0'), ['str'])),
                                    ('tx_sapi', (YLeaf(YType.str, 'tx-sapi'), ['str'])),
                                    ('tx_sapi_range', (YLeaf(YType.str, 'tx-sapi-range'), ['str'])),
                                    ('tx_dapi0', (YLeaf(YType.str, 'tx-dapi0'), ['str'])),
                                    ('tx_dapi', (YLeaf(YType.str, 'tx-dapi'), ['str'])),
                                    ('tx_dapi_range', (YLeaf(YType.str, 'tx-dapi-range'), ['str'])),
                                    ('tx_oper_spec', (YLeaf(YType.str, 'tx-oper-spec'), ['str'])),
                                    ('tx_oper_spec_range', (YLeaf(YType.str, 'tx-oper-spec-range'), ['str'])),
                                    ('rx_tti', (YLeaf(YType.str, 'rx-tti'), ['str'])),
                                    ('rx_sapi0', (YLeaf(YType.str, 'rx-sapi0'), ['str'])),
                                    ('rx_sapi', (YLeaf(YType.str, 'rx-sapi'), ['str'])),
                                    ('rx_sapi_range', (YLeaf(YType.str, 'rx-sapi-range'), ['str'])),
                                    ('rx_dapi0', (YLeaf(YType.str, 'rx-dapi0'), ['str'])),
                                    ('rx_dapi', (YLeaf(YType.str, 'rx-dapi'), ['str'])),
                                    ('rx_dapi_range', (YLeaf(YType.str, 'rx-dapi-range'), ['str'])),
                                    ('rx_oper_spec_range', (YLeaf(YType.str, 'rx-oper-spec-range'), ['str'])),
                                    ('rx_oper_spec', (YLeaf(YType.str, 'rx-oper-spec'), ['str'])),
                                    ('expected_tti', (YLeaf(YType.str, 'expected-tti'), ['str'])),
                                    ('expected_sapi0', (YLeaf(YType.str, 'expected-sapi0'), ['str'])),
                                    ('expected_sapi', (YLeaf(YType.str, 'expected-sapi'), ['str'])),
                                    ('exp_sapi_range', (YLeaf(YType.str, 'exp-sapi-range'), ['str'])),
                                    ('expected_dapi0', (YLeaf(YType.str, 'expected-dapi0'), ['str'])),
                                    ('expected_dapi', (YLeaf(YType.str, 'expected-dapi'), ['str'])),
                                    ('exp_dapi_range', (YLeaf(YType.str, 'exp-dapi-range'), ['str'])),
                                    ('expected_oper_spec', (YLeaf(YType.str, 'expected-oper-spec'), ['str'])),
                                    ('exp_oper_spec_range', (YLeaf(YType.str, 'exp-oper-spec-range'), ['str'])),
                                ])
                                self.tx_string_type = None
                                self.expected_string_type = None
                                self.rx_string_type = None
                                self.tx_tti = None
                                self.tx_sapi0 = None
                                self.tx_sapi = None
                                self.tx_sapi_range = None
                                self.tx_dapi0 = None
                                self.tx_dapi = None
                                self.tx_dapi_range = None
                                self.tx_oper_spec = None
                                self.tx_oper_spec_range = None
                                self.rx_tti = None
                                self.rx_sapi0 = None
                                self.rx_sapi = None
                                self.rx_sapi_range = None
                                self.rx_dapi0 = None
                                self.rx_dapi = None
                                self.rx_dapi_range = None
                                self.rx_oper_spec_range = None
                                self.rx_oper_spec = None
                                self.expected_tti = None
                                self.expected_sapi0 = None
                                self.expected_sapi = None
                                self.exp_sapi_range = None
                                self.expected_dapi0 = None
                                self.expected_dapi = None
                                self.exp_dapi_range = None
                                self.expected_oper_spec = None
                                self.exp_oper_spec_range = None
                                self._segment_path = lambda: "tti"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti, ['tx_string_type', 'expected_string_type', 'rx_string_type', 'tx_tti', 'tx_sapi0', 'tx_sapi', 'tx_sapi_range', 'tx_dapi0', 'tx_dapi', 'tx_dapi_range', 'tx_oper_spec', 'tx_oper_spec_range', 'rx_tti', 'rx_sapi0', 'rx_sapi', 'rx_sapi_range', 'rx_dapi0', 'rx_dapi', 'rx_dapi_range', 'rx_oper_spec_range', 'rx_oper_spec', 'expected_tti', 'expected_sapi0', 'expected_sapi', 'exp_sapi_range', 'expected_dapi0', 'expected_dapi', 'exp_dapi_range', 'expected_oper_spec', 'exp_oper_spec_range'], name, value)


                class OpticsInfo(Entity):
                    """
                    Optics operational information
                    
                    .. attribute:: optics_type
                    
                    	Optics type name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clock_source
                    
                    	Actual transmit clock source
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: wave_frequency_progressive_string
                    
                    	Wave Frequency Information for Progressive Frequencies
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: wavelength_progressive_string
                    
                    	Wavelength Information for Progressive Frequencies
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: is_wave_frequency_progressive_valid
                    
                    	True if Progressive Frequency is supported by hw
                    	**type**\: bool
                    
                    .. attribute:: wavelength_progressive
                    
                    	Wavelength Information for Progressive Frequencies
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_band
                    
                    	Wavelength band information
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_channel
                    
                    	Current ITU wavelength channel number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wave_frequency
                    
                    	 wavelenght frequency read from hw in the uint 0 .01nm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_wave_frequency_valid
                    
                    	True if hw supported wavelength frequency readback
                    	**type**\: bool
                    
                    .. attribute:: wave_channel_owner
                    
                    	Owner of current wavelength
                    	**type**\:  :py:class:`DwdmWaveChannelOwner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmWaveChannelOwner>`
                    
                    .. attribute:: gmpls_set_wave_channel
                    
                    	Wavelength channel set by GMPLS
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: configured_wave_channel
                    
                    	Wavelength channel set from configuration
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: default_wave_channel
                    
                    	Wavelength channel default from hardware
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dbm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_threshold
                    
                    	Transmit power threshold value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_current_bias
                    
                    	Laser current bias value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_current_bias_threshold
                    
                    	 Laser Current Bias threshold value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_rx_los_threshold_supported
                    
                    	TRUE if  Rx LOS thresold configurable
                    	**type**\: bool
                    
                    .. attribute:: rx_los_threshold
                    
                    	Rx LOS threshold value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_min
                    
                    	Transmit  power mininum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_max
                    
                    	Transmit power maximum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power_avg
                    
                    	Transmit optical average value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_min
                    
                    	Recieve power mininum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_max
                    
                    	Receive power maximum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power_avg
                    
                    	Recieve power average value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_bias_current_min
                    
                    	Laser bias current minimum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_bias_current_max
                    
                    	Laser bias current maxinum value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_bias_current_avg
                    
                    	Laser bias current average value in the interval time
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: chromatic_dispersion
                    
                    	Current chromatic dispersion
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: differential_group_delay
                    
                    	Current differential group Delay
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: polarization_mode_dispersion
                    
                    	Current polarization mode dispersion
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: signal_to_noise_ratio
                    
                    	Current optical signal to noise ratio
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: polarization_dependent_loss
                    
                    	Current Polarization Dependent loss
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: polarization_change_rate
                    
                    	Current Polarization change rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: phase_noise
                    
                    	Current Phase Noise
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_power_fail
                    
                    	Transmit power failure(above/belowe a threshold) count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_power_fail
                    
                    	Receive power failure(above/belowe a threshold) count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.OpticsInfo, self).__init__()

                        self.yang_name = "optics-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('optics_type', (YLeaf(YType.str, 'optics-type'), ['str'])),
                            ('clock_source', (YLeaf(YType.uint8, 'clock-source'), ['int'])),
                            ('wave_frequency_progressive_string', (YLeaf(YType.str, 'wave-frequency-progressive-string'), ['str'])),
                            ('wavelength_progressive_string', (YLeaf(YType.str, 'wavelength-progressive-string'), ['str'])),
                            ('is_wave_frequency_progressive_valid', (YLeaf(YType.boolean, 'is-wave-frequency-progressive-valid'), ['bool'])),
                            ('wavelength_progressive', (YLeaf(YType.uint32, 'wavelength-progressive'), ['int'])),
                            ('wave_band', (YLeaf(YType.uint32, 'wave-band'), ['int'])),
                            ('wave_channel', (YLeaf(YType.uint32, 'wave-channel'), ['int'])),
                            ('wave_frequency', (YLeaf(YType.uint32, 'wave-frequency'), ['int'])),
                            ('is_wave_frequency_valid', (YLeaf(YType.boolean, 'is-wave-frequency-valid'), ['bool'])),
                            ('wave_channel_owner', (YLeaf(YType.enumeration, 'wave-channel-owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmWaveChannelOwner', '')])),
                            ('gmpls_set_wave_channel', (YLeaf(YType.uint16, 'gmpls-set-wave-channel'), ['int'])),
                            ('configured_wave_channel', (YLeaf(YType.uint16, 'configured-wave-channel'), ['int'])),
                            ('default_wave_channel', (YLeaf(YType.uint16, 'default-wave-channel'), ['int'])),
                            ('transmit_power', (YLeaf(YType.int32, 'transmit-power'), ['int'])),
                            ('transmit_power_threshold', (YLeaf(YType.int32, 'transmit-power-threshold'), ['int'])),
                            ('laser_current_bias', (YLeaf(YType.int32, 'laser-current-bias'), ['int'])),
                            ('laser_current_bias_threshold', (YLeaf(YType.int32, 'laser-current-bias-threshold'), ['int'])),
                            ('receive_power', (YLeaf(YType.int32, 'receive-power'), ['int'])),
                            ('is_rx_los_threshold_supported', (YLeaf(YType.boolean, 'is-rx-los-threshold-supported'), ['bool'])),
                            ('rx_los_threshold', (YLeaf(YType.int32, 'rx-los-threshold'), ['int'])),
                            ('transmit_power_min', (YLeaf(YType.int32, 'transmit-power-min'), ['int'])),
                            ('transmit_power_max', (YLeaf(YType.int32, 'transmit-power-max'), ['int'])),
                            ('transmit_power_avg', (YLeaf(YType.int32, 'transmit-power-avg'), ['int'])),
                            ('receive_power_min', (YLeaf(YType.int32, 'receive-power-min'), ['int'])),
                            ('receive_power_max', (YLeaf(YType.int32, 'receive-power-max'), ['int'])),
                            ('receive_power_avg', (YLeaf(YType.int32, 'receive-power-avg'), ['int'])),
                            ('laser_bias_current_min', (YLeaf(YType.int32, 'laser-bias-current-min'), ['int'])),
                            ('laser_bias_current_max', (YLeaf(YType.int32, 'laser-bias-current-max'), ['int'])),
                            ('laser_bias_current_avg', (YLeaf(YType.int32, 'laser-bias-current-avg'), ['int'])),
                            ('chromatic_dispersion', (YLeaf(YType.int32, 'chromatic-dispersion'), ['int'])),
                            ('differential_group_delay', (YLeaf(YType.int32, 'differential-group-delay'), ['int'])),
                            ('polarization_mode_dispersion', (YLeaf(YType.int32, 'polarization-mode-dispersion'), ['int'])),
                            ('signal_to_noise_ratio', (YLeaf(YType.int32, 'signal-to-noise-ratio'), ['int'])),
                            ('polarization_dependent_loss', (YLeaf(YType.int32, 'polarization-dependent-loss'), ['int'])),
                            ('polarization_change_rate', (YLeaf(YType.uint32, 'polarization-change-rate'), ['int'])),
                            ('phase_noise', (YLeaf(YType.uint32, 'phase-noise'), ['int'])),
                            ('output_power_fail', (YLeaf(YType.uint32, 'output-power-fail'), ['int'])),
                            ('input_power_fail', (YLeaf(YType.uint32, 'input-power-fail'), ['int'])),
                        ])
                        self.optics_type = None
                        self.clock_source = None
                        self.wave_frequency_progressive_string = None
                        self.wavelength_progressive_string = None
                        self.is_wave_frequency_progressive_valid = None
                        self.wavelength_progressive = None
                        self.wave_band = None
                        self.wave_channel = None
                        self.wave_frequency = None
                        self.is_wave_frequency_valid = None
                        self.wave_channel_owner = None
                        self.gmpls_set_wave_channel = None
                        self.configured_wave_channel = None
                        self.default_wave_channel = None
                        self.transmit_power = None
                        self.transmit_power_threshold = None
                        self.laser_current_bias = None
                        self.laser_current_bias_threshold = None
                        self.receive_power = None
                        self.is_rx_los_threshold_supported = None
                        self.rx_los_threshold = None
                        self.transmit_power_min = None
                        self.transmit_power_max = None
                        self.transmit_power_avg = None
                        self.receive_power_min = None
                        self.receive_power_max = None
                        self.receive_power_avg = None
                        self.laser_bias_current_min = None
                        self.laser_bias_current_max = None
                        self.laser_bias_current_avg = None
                        self.chromatic_dispersion = None
                        self.differential_group_delay = None
                        self.polarization_mode_dispersion = None
                        self.signal_to_noise_ratio = None
                        self.polarization_dependent_loss = None
                        self.polarization_change_rate = None
                        self.phase_noise = None
                        self.output_power_fail = None
                        self.input_power_fail = None
                        self._segment_path = lambda: "optics-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.OpticsInfo, ['optics_type', 'clock_source', 'wave_frequency_progressive_string', 'wavelength_progressive_string', 'is_wave_frequency_progressive_valid', 'wavelength_progressive', 'wave_band', 'wave_channel', 'wave_frequency', 'is_wave_frequency_valid', 'wave_channel_owner', 'gmpls_set_wave_channel', 'configured_wave_channel', 'default_wave_channel', 'transmit_power', 'transmit_power_threshold', 'laser_current_bias', 'laser_current_bias_threshold', 'receive_power', 'is_rx_los_threshold_supported', 'rx_los_threshold', 'transmit_power_min', 'transmit_power_max', 'transmit_power_avg', 'receive_power_min', 'receive_power_max', 'receive_power_avg', 'laser_bias_current_min', 'laser_bias_current_max', 'laser_bias_current_avg', 'chromatic_dispersion', 'differential_group_delay', 'polarization_mode_dispersion', 'signal_to_noise_ratio', 'polarization_dependent_loss', 'polarization_change_rate', 'phase_noise', 'output_power_fail', 'input_power_fail'], name, value)


                class TdcInfo(Entity):
                    """
                    TDC operational information
                    
                    .. attribute:: tdc_valid
                    
                    	TRUE for Valid else Invalid
                    	**type**\: bool
                    
                    .. attribute:: major_alarm
                    
                    	TRUE for Alarm condition else FALSE
                    	**type**\: bool
                    
                    .. attribute:: operation_mode
                    
                    	TRUE for MANUAL else AUTO
                    	**type**\: bool
                    
                    .. attribute:: tdc_status
                    
                    	TRUE if TDC Aquiring else Locked
                    	**type**\: bool
                    
                    .. attribute:: dispersion_offset
                    
                    	TDC Dispersion Offset
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: reroute_ber
                    
                    	Reroute BER
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_reroute_control_enabled
                    
                    	TRUE for ENABLED else DISABLED
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.TdcInfo, self).__init__()

                        self.yang_name = "tdc-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tdc_valid', (YLeaf(YType.boolean, 'tdc-valid'), ['bool'])),
                            ('major_alarm', (YLeaf(YType.boolean, 'major-alarm'), ['bool'])),
                            ('operation_mode', (YLeaf(YType.boolean, 'operation-mode'), ['bool'])),
                            ('tdc_status', (YLeaf(YType.boolean, 'tdc-status'), ['bool'])),
                            ('dispersion_offset', (YLeaf(YType.int32, 'dispersion-offset'), ['int'])),
                            ('reroute_ber', (YLeaf(YType.int32, 'reroute-ber'), ['int'])),
                            ('is_reroute_control_enabled', (YLeaf(YType.boolean, 'is-reroute-control-enabled'), ['bool'])),
                        ])
                        self.tdc_valid = None
                        self.major_alarm = None
                        self.operation_mode = None
                        self.tdc_status = None
                        self.dispersion_offset = None
                        self.reroute_ber = None
                        self.is_reroute_control_enabled = None
                        self._segment_path = lambda: "tdc-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.TdcInfo, ['tdc_valid', 'major_alarm', 'operation_mode', 'tdc_status', 'dispersion_offset', 'reroute_ber', 'is_reroute_control_enabled'], name, value)


                class NetworkSrlgInfo(Entity):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg
                    
                    	Network Srlg
                    	**type**\: list of int
                    
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
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('network_srlg', (YLeafList(YType.uint32, 'network-srlg'), ['int'])),
                        ])
                        self.network_srlg = []
                        self._segment_path = lambda: "network-srlg-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.NetworkSrlgInfo, ['network_srlg'], name, value)


                class Proactive(Entity):
                    """
                    Proactive protection information
                    
                    .. attribute:: proactive_feature
                    
                    	Feature Support
                    	**type**\: bool
                    
                    .. attribute:: proactive_mode
                    
                    	Proactive Mode
                    	**type**\:  :py:class:`G709ppfsmMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppfsmMode>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:  :py:class:`G709ppfsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppfsmState>`
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:  :py:class:`G709ppintfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ppintfState>`
                    
                    .. attribute:: tas_state
                    
                    	TAS State
                    	**type**\:  :py:class:`DwdmtasState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasState>`
                    
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
                    
                    .. attribute:: default_trig_thresh_coeff
                    
                    	Default Trigger threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_trig_thresh_power
                    
                    	Default Trigger threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_rvrt_thresh_coeff
                    
                    	Default Revert threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: default_rvrt_thresh_power
                    
                    	Default Revert threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_samples
                    
                    	Required Trigger Samples
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_samples
                    
                    	Required Revert Samples
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
                    
                    .. attribute:: protection_trigger
                    
                    	Protection Trigger State
                    	**type**\: bool
                    
                    .. attribute:: interface_trigger
                    
                    	Proactive Interface Triffer
                    	**type**\: bool
                    
                    .. attribute:: tx_aps
                    
                    	Transmitted APS Byte
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tx_aps_descr
                    
                    	Tx APS Description
                    	**type**\:  :py:class:`G709apsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709apsByte>`
                    
                    .. attribute:: rx_aps
                    
                    	Received APS byte
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_aps_descr
                    
                    	Rx APS Description
                    	**type**\:  :py:class:`G709apsByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709apsByte>`
                    
                    .. attribute:: alarm_state
                    
                    	AlarmState
                    	**type**\: bool
                    
                    .. attribute:: trig_ec_cnt
                    
                    	Trigger EC Cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_ec_cnt
                    
                    	Revert EC Cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefec_thresh_crossed
                    
                    	Prefec Trigger Thresh Crossed
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dwdm.Ports.Port.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('proactive_feature', (YLeaf(YType.boolean, 'proactive-feature'), ['bool'])),
                            ('proactive_mode', (YLeaf(YType.enumeration, 'proactive-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709ppfsmMode', '')])),
                            ('proactive_fsm_state', (YLeaf(YType.enumeration, 'proactive-fsm-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709ppfsmState', '')])),
                            ('proactive_fsm_if_state', (YLeaf(YType.enumeration, 'proactive-fsm-if-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709ppintfState', '')])),
                            ('tas_state', (YLeaf(YType.enumeration, 'tas-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmtasState', '')])),
                            ('trig_thresh_coeff', (YLeaf(YType.uint8, 'trig-thresh-coeff'), ['int'])),
                            ('trig_thresh_power', (YLeaf(YType.uint8, 'trig-thresh-power'), ['int'])),
                            ('rvrt_thresh_coeff', (YLeaf(YType.uint8, 'rvrt-thresh-coeff'), ['int'])),
                            ('rvrt_thresh_power', (YLeaf(YType.uint8, 'rvrt-thresh-power'), ['int'])),
                            ('default_trig_thresh_coeff', (YLeaf(YType.uint8, 'default-trig-thresh-coeff'), ['int'])),
                            ('default_trig_thresh_power', (YLeaf(YType.uint8, 'default-trig-thresh-power'), ['int'])),
                            ('default_rvrt_thresh_coeff', (YLeaf(YType.uint8, 'default-rvrt-thresh-coeff'), ['int'])),
                            ('default_rvrt_thresh_power', (YLeaf(YType.uint8, 'default-rvrt-thresh-power'), ['int'])),
                            ('trig_samples', (YLeaf(YType.uint8, 'trig-samples'), ['int'])),
                            ('rvrt_samples', (YLeaf(YType.uint8, 'rvrt-samples'), ['int'])),
                            ('trigger_window', (YLeaf(YType.uint32, 'trigger-window'), ['int'])),
                            ('revert_window', (YLeaf(YType.uint32, 'revert-window'), ['int'])),
                            ('protection_trigger', (YLeaf(YType.boolean, 'protection-trigger'), ['bool'])),
                            ('interface_trigger', (YLeaf(YType.boolean, 'interface-trigger'), ['bool'])),
                            ('tx_aps', (YLeaf(YType.uint8, 'tx-aps'), ['int'])),
                            ('tx_aps_descr', (YLeaf(YType.enumeration, 'tx-aps-descr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709apsByte', '')])),
                            ('rx_aps', (YLeaf(YType.uint8, 'rx-aps'), ['int'])),
                            ('rx_aps_descr', (YLeaf(YType.enumeration, 'rx-aps-descr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709apsByte', '')])),
                            ('alarm_state', (YLeaf(YType.boolean, 'alarm-state'), ['bool'])),
                            ('trig_ec_cnt', (YLeaf(YType.uint32, 'trig-ec-cnt'), ['int'])),
                            ('rvrt_ec_cnt', (YLeaf(YType.uint32, 'rvrt-ec-cnt'), ['int'])),
                            ('prefec_thresh_crossed', (YLeaf(YType.boolean, 'prefec-thresh-crossed'), ['bool'])),
                        ])
                        self.proactive_feature = None
                        self.proactive_mode = None
                        self.proactive_fsm_state = None
                        self.proactive_fsm_if_state = None
                        self.tas_state = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.default_trig_thresh_coeff = None
                        self.default_trig_thresh_power = None
                        self.default_rvrt_thresh_coeff = None
                        self.default_rvrt_thresh_power = None
                        self.trig_samples = None
                        self.rvrt_samples = None
                        self.trigger_window = None
                        self.revert_window = None
                        self.protection_trigger = None
                        self.interface_trigger = None
                        self.tx_aps = None
                        self.tx_aps_descr = None
                        self.rx_aps = None
                        self.rx_aps_descr = None
                        self.alarm_state = None
                        self.trig_ec_cnt = None
                        self.rvrt_ec_cnt = None
                        self.prefec_thresh_crossed = None
                        self._segment_path = lambda: "proactive"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.Proactive, ['proactive_feature', 'proactive_mode', 'proactive_fsm_state', 'proactive_fsm_if_state', 'tas_state', 'trig_thresh_coeff', 'trig_thresh_power', 'rvrt_thresh_coeff', 'rvrt_thresh_power', 'default_trig_thresh_coeff', 'default_trig_thresh_power', 'default_rvrt_thresh_coeff', 'default_rvrt_thresh_power', 'trig_samples', 'rvrt_samples', 'trigger_window', 'revert_window', 'protection_trigger', 'interface_trigger', 'tx_aps', 'tx_aps_descr', 'rx_aps', 'rx_aps_descr', 'alarm_state', 'trig_ec_cnt', 'rvrt_ec_cnt', 'prefec_thresh_crossed'], name, value)


                class SignalLog(Entity):
                    """
                    Signal log information
                    
                    .. attribute:: is_log_enabled
                    
                    	'true' if signal log is enabled 'false' otherwise
                    	**type**\: bool
                    
                    .. attribute:: log_filename
                    
                    	Log file name 
                    	**type**\: str
                    
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
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                            ('log_filename', (YLeaf(YType.str, 'log-filename'), ['str'])),
                        ])
                        self.is_log_enabled = None
                        self.log_filename = None
                        self._segment_path = lambda: "signal-log"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dwdm.Ports.Port.Info.SignalLog, ['is_log_enabled', 'log_filename'], name, value)

    def clone_ptr(self):
        self._top_entity = Dwdm()
        return self._top_entity

class Vtxp(Entity):
    """
    vtxp
    
    .. attribute:: dwdm_vtxp
    
    	DWDM operational data
    	**type**\:  :py:class:`DwdmVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dwdm-vtxp", ("dwdm_vtxp", Vtxp.DwdmVtxp))])
        self._leafs = OrderedDict()

        self.dwdm_vtxp = Vtxp.DwdmVtxp()
        self.dwdm_vtxp.parent = self
        self._children_name_map["dwdm_vtxp"] = "dwdm-vtxp"
        self._segment_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vtxp, [], name, value)


    class DwdmVtxp(Entity):
        """
        DWDM operational data
        
        .. attribute:: port_vtxps
        
        	All DWDM Port operational data
        	**type**\:  :py:class:`PortVtxps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vtxp.DwdmVtxp, self).__init__()

            self.yang_name = "dwdm-vtxp"
            self.yang_parent_name = "vtxp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("port-vtxps", ("port_vtxps", Vtxp.DwdmVtxp.PortVtxps))])
            self._leafs = OrderedDict()

            self.port_vtxps = Vtxp.DwdmVtxp.PortVtxps()
            self.port_vtxps.parent = self
            self._children_name_map["port_vtxps"] = "port-vtxps"
            self._segment_path = lambda: "dwdm-vtxp"
            self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vtxp.DwdmVtxp, [], name, value)


        class PortVtxps(Entity):
            """
            All DWDM Port operational data
            
            .. attribute:: port_vtxp
            
            	DWDM Port operational data
            	**type**\: list of  		 :py:class:`PortVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps.PortVtxp>`
            
            

            """

            _prefix = 'dwdm-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vtxp.DwdmVtxp.PortVtxps, self).__init__()

                self.yang_name = "port-vtxps"
                self.yang_parent_name = "dwdm-vtxp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("port-vtxp", ("port_vtxp", Vtxp.DwdmVtxp.PortVtxps.PortVtxp))])
                self._leafs = OrderedDict()

                self.port_vtxp = YList(self)
                self._segment_path = lambda: "port-vtxps"
                self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps, [], name, value)


            class PortVtxp(Entity):
                """
                DWDM Port operational data
                
                .. attribute:: name  (key)
                
                	Port name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: info
                
                	DWDM port operational data
                	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, self).__init__()

                    self.yang_name = "port-vtxp"
                    self.yang_parent_name = "port-vtxps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("info", ("info", Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.info = Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"
                    self._segment_path = lambda: "port-vtxp" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dwdm-ui-oper:vtxp/dwdm-vtxp/port-vtxps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps.PortVtxp, ['name'], name, value)


                class Info(Entity):
                    """
                    DWDM port operational data
                    
                    .. attribute:: vtxp_enable
                    
                    	Is VTXP attribute enabled
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "port-vtxp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vtxp_enable', (YLeaf(YType.boolean, 'vtxp-enable'), ['bool'])),
                        ])
                        self.vtxp_enable = None
                        self._segment_path = lambda: "info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info, ['vtxp_enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Vtxp()
        return self._top_entity

