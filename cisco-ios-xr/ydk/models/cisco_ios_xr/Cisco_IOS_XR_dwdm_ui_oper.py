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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DwdmControllerStateEnum(Enum):
    """
    DwdmControllerStateEnum

    Dwdm controller state

    .. data:: dwdm_ui_state_up = 0

    	Up

    .. data:: dwdm_ui_state_down = 1

    	Down

    .. data:: dwdm_ui_state_admin_down = 2

    	Administratively Down

    """

    dwdm_ui_state_up = 0

    dwdm_ui_state_down = 1

    dwdm_ui_state_admin_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['DwdmControllerStateEnum']


class DwdmWaveChannelOwnerEnum(Enum):
    """
    DwdmWaveChannelOwnerEnum

    Dwdm wave channel owner

    .. data:: default = 0

    	Hardware Default

    .. data:: configuration = 1

    	Configuration

    .. data:: gmpls = 2

    	GMPLS Signaled

    """

    default = 0

    configuration = 1

    gmpls = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['DwdmWaveChannelOwnerEnum']


class DwdmtasStateEnum(Enum):
    """
    DwdmtasStateEnum

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

    tas_oos = 0

    tas_is = 1

    tas_oos_mt = 2

    tas_is_cfg = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['DwdmtasStateEnum']


class G709ApsByteEnum(Enum):
    """
    G709ApsByteEnum

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

    pp_no_protect = 0

    pp_no_request = 15

    pp_regen_degrade = 63

    pp_sig_degrade = 175

    pp_remote_main = 239

    pp_aps_unknown = 255


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709ApsByteEnum']


class G709EfecModeEnum(Enum):
    """
    G709EfecModeEnum

    G709efec mode

    .. data:: g975_none = 0

    .. data:: g975_1_i4 = 1

    	G975.1 I.4

    .. data:: g975_1_i7 = 2

    	G975.1 I.7

    """

    g975_none = 0

    g975_1_i4 = 1

    g975_1_i7 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709EfecModeEnum']


class G709PpfsmModeEnum(Enum):
    """
    G709PpfsmModeEnum

    G709ppfsm mode

    .. data:: pp_disable = 0

    	OFF

    .. data:: pp_default_mode = 1

    	ON (Default Mode)

    .. data:: pp_graceful_mode = 2

    	ON (Graceful Mode)

    """

    pp_disable = 0

    pp_default_mode = 1

    pp_graceful_mode = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PpfsmModeEnum']


class G709PpfsmStateEnum(Enum):
    """
    G709PpfsmStateEnum

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

    in_active = 0

    disabled = 1

    normal_state = 2

    local_failing = 3

    remote_failing = 4

    main_t_failing = 5

    regen_failing = 6

    local_failed = 7

    remote_failed = 8

    main_t_failed = 9

    regen_failed = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PpfsmStateEnum']


class G709PpintfStateEnum(Enum):
    """
    G709PpintfStateEnum

    G709ppintf state

    .. data:: pp_intf_up = 0

    	Interface is Up

    .. data:: pp_intf_failing = 1

    	Interface is Going Down

    .. data:: pp_intf_down = 2

    	Interface Down

    """

    pp_intf_up = 0

    pp_intf_failing = 1

    pp_intf_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PpintfStateEnum']


class G709PrbsIntervalEnum(Enum):
    """
    G709PrbsIntervalEnum

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

    current_interval = 0

    previous_interval = 1

    previous_interval2 = 2

    previous_interval3 = 3

    previous_interval4 = 4

    previous_interval5 = 5

    previous_interval6 = 6

    previous_interval7 = 7

    previous_interval8 = 8

    previous_interval9 = 9

    previous_interval10 = 10

    previous_interval11 = 11

    previous_interval12 = 12

    previous_interval13 = 13

    previous_interval14 = 14

    previous_interval15 = 15

    previous_interval16 = 16

    previous_interval17 = 17

    previous_interval18 = 18

    previous_interval19 = 19

    previous_interval20 = 20

    previous_interval21 = 21

    previous_interval22 = 22

    previous_interval23 = 23

    previous_interval24 = 24

    previous_interval25 = 25

    previous_interval26 = 26

    previous_interval27 = 27

    previous_interval28 = 28

    previous_interval29 = 29

    previous_interval30 = 30

    previous_interval31 = 31

    previous_interval32 = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PrbsIntervalEnum']


class G709PrbsModeEnum(Enum):
    """
    G709PrbsModeEnum

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

    mode_source = 0

    mode_sink = 1

    mode_source_sink = 2

    mode_invalid = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PrbsModeEnum']


class G709PrbsPatternEnum(Enum):
    """
    G709PrbsPatternEnum

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

    pattern_none = 0

    pattern_null = 1

    pattern_pn11 = 2

    pattern_pn23 = 3

    pattern_pn31 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['G709PrbsPatternEnum']



class Dwdm(object):
    """
    DWDM operational data
    
    .. attribute:: ports
    
    	All DWDM Port operational data
    	**type**\:   :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports>`
    
    

    """

    _prefix = 'dwdm-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.ports = Dwdm.Ports()
        self.ports.parent = self


    class Ports(object):
        """
        All DWDM Port operational data
        
        .. attribute:: port
        
        	DWDM Port operational data
        	**type**\: list of    :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.port = YList()
            self.port.parent = self
            self.port.name = 'port'


        class Port(object):
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
                self.parent = None
                self.name = None
                self.info = Dwdm.Ports.Port.Info()
                self.info.parent = self
                self.optics = Dwdm.Ports.Port.Optics()
                self.optics.parent = self
                self.prbs = Dwdm.Ports.Port.Prbs()
                self.prbs.parent = self


            class Prbs(object):
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
                    self.parent = None
                    self.fifteen_minutes_bucket = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket()
                    self.fifteen_minutes_bucket.parent = self
                    self.twenty_four_hours_bucket = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket()
                    self.twenty_four_hours_bucket.parent = self


                class TwentyFourHoursBucket(object):
                    """
                    Port 24\-hour PRBS statistics table
                    
                    .. attribute:: twenty_four_hours_statistics
                    
                    	Port 24\-hour PRBS statistics data
                    	**type**\:   :py:class:`TwentyFourHoursStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.twenty_four_hours_statistics = Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics()
                        self.twenty_four_hours_statistics.parent = self


                    class TwentyFourHoursStatistics(object):
                        """
                        Port 24\-hour PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709PrbsModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsModeEnum>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of    :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_prbs_enabled = None
                            self.prbs_config_mode = None
                            self.prbs_entry = YList()
                            self.prbs_entry.parent = self
                            self.prbs_entry.name = 'prbs_entry'


                        class PrbsEntry(object):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709PrbsPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPatternEnum>`
                            
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
                            	**type**\:   :py:class:`G709PrbsIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsIntervalEnum>`
                            
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
                            	**type**\:   :py:class:`G709PrbsPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPatternEnum>`
                            
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
                                self.parent = None
                                self.bit_error_count = None
                                self.configured_pattern = None
                                self.found_at = None
                                self.found_count = None
                                self.interval_index = None
                                self.lost_at = None
                                self.lost_count = None
                                self.received_pattern = None
                                self.start_at = None
                                self.stop_at = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:prbs-entry'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bit_error_count is not None:
                                    return True

                                if self.configured_pattern is not None:
                                    return True

                                if self.found_at is not None:
                                    return True

                                if self.found_count is not None:
                                    return True

                                if self.interval_index is not None:
                                    return True

                                if self.lost_at is not None:
                                    return True

                                if self.lost_count is not None:
                                    return True

                                if self.received_pattern is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.stop_at is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:twenty-four-hours-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_prbs_enabled is not None:
                                return True

                            if self.prbs_config_mode is not None:
                                return True

                            if self.prbs_entry is not None:
                                for child_ref in self.prbs_entry:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:twenty-four-hours-bucket'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.twenty_four_hours_statistics is not None and self.twenty_four_hours_statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket']['meta_info']


                class FifteenMinutesBucket(object):
                    """
                    Port 15\-minute PRBS statistics table
                    
                    .. attribute:: fifteen_minutes_statistics
                    
                    	Port 15\-minute PRBS statistics data
                    	**type**\:   :py:class:`FifteenMinutesStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.fifteen_minutes_statistics = Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics()
                        self.fifteen_minutes_statistics.parent = self


                    class FifteenMinutesStatistics(object):
                        """
                        Port 15\-minute PRBS statistics data
                        
                        .. attribute:: is_prbs_enabled
                        
                        	'True' if PRBS is enabled 'False' otherwise
                        	**type**\:  bool
                        
                        .. attribute:: prbs_config_mode
                        
                        	Configured mode of PRBS test
                        	**type**\:   :py:class:`G709PrbsModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsModeEnum>`
                        
                        .. attribute:: prbs_entry
                        
                        	History consists of 15\-minute/24\-hour intervals
                        	**type**\: list of    :py:class:`PrbsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry>`
                        
                        

                        """

                        _prefix = 'dwdm-ui-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_prbs_enabled = None
                            self.prbs_config_mode = None
                            self.prbs_entry = YList()
                            self.prbs_entry.parent = self
                            self.prbs_entry.name = 'prbs_entry'


                        class PrbsEntry(object):
                            """
                            History consists of 15\-minute/24\-hour intervals
                            
                            .. attribute:: bit_error_count
                            
                            	Bit Error Count
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_pattern
                            
                            	Configured pattern of PRBS test
                            	**type**\:   :py:class:`G709PrbsPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPatternEnum>`
                            
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
                            	**type**\:   :py:class:`G709PrbsIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsIntervalEnum>`
                            
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
                            	**type**\:   :py:class:`G709PrbsPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPatternEnum>`
                            
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
                                self.parent = None
                                self.bit_error_count = None
                                self.configured_pattern = None
                                self.found_at = None
                                self.found_count = None
                                self.interval_index = None
                                self.lost_at = None
                                self.lost_count = None
                                self.received_pattern = None
                                self.start_at = None
                                self.stop_at = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:prbs-entry'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bit_error_count is not None:
                                    return True

                                if self.configured_pattern is not None:
                                    return True

                                if self.found_at is not None:
                                    return True

                                if self.found_count is not None:
                                    return True

                                if self.interval_index is not None:
                                    return True

                                if self.lost_at is not None:
                                    return True

                                if self.lost_count is not None:
                                    return True

                                if self.received_pattern is not None:
                                    return True

                                if self.start_at is not None:
                                    return True

                                if self.stop_at is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:fifteen-minutes-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_prbs_enabled is not None:
                                return True

                            if self.prbs_config_mode is not None:
                                return True

                            if self.prbs_entry is not None:
                                for child_ref in self.prbs_entry:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:fifteen-minutes-bucket'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.fifteen_minutes_statistics is not None and self.fifteen_minutes_statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:prbs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fifteen_minutes_bucket is not None and self.fifteen_minutes_bucket._has_data():
                        return True

                    if self.twenty_four_hours_bucket is not None and self.twenty_four_hours_bucket._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                    return meta._meta_table['Dwdm.Ports.Port.Prbs']['meta_info']


            class Optics(object):
                """
                DWDM Port optics operational data
                
                .. attribute:: wave_info
                
                	DWDM port wavelength information data
                	**type**\:   :py:class:`WaveInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Dwdm.Ports.Port.Optics.WaveInfo>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.wave_info = Dwdm.Ports.Port.Optics.WaveInfo()
                    self.wave_info.parent = self


                class WaveInfo(object):
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
                        self.parent = None
                        self.wave_band = None
                        self.wave_channel_max = None
                        self.wave_channel_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:wave-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.wave_band is not None:
                            return True

                        if self.wave_channel_max is not None:
                            return True

                        if self.wave_channel_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Optics.WaveInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:optics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.wave_info is not None and self.wave_info._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                    return meta._meta_table['Dwdm.Ports.Port.Optics']['meta_info']


            class Info(object):
                """
                DWDM port operational data
                
                .. attribute:: controller_state
                
                	DWDM controller state\: Up, Down or Administratively Down
                	**type**\:   :py:class:`DwdmControllerStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmControllerStateEnum>`
                
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
                	**type**\:   :py:class:`DwdmtasStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasStateEnum>`
                
                

                """

                _prefix = 'dwdm-ui-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.controller_state = None
                    self.g709_info = Dwdm.Ports.Port.Info.G709Info()
                    self.g709_info.parent = self
                    self.network_srlg_info = Dwdm.Ports.Port.Info.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self.optics_info = Dwdm.Ports.Port.Info.OpticsInfo()
                    self.optics_info.parent = self
                    self.proactive = Dwdm.Ports.Port.Info.Proactive()
                    self.proactive.parent = self
                    self.signal_log = Dwdm.Ports.Port.Info.SignalLog()
                    self.signal_log.parent = self
                    self.slice_state = None
                    self.tdc_info = Dwdm.Ports.Port.Info.TdcInfo()
                    self.tdc_info.parent = self
                    self.transport_admin_state = None


                class G709Info(object):
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
                    	**type**\:   :py:class:`G709EfecModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709EfecModeEnum>`
                    
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
                    	**type**\:   :py:class:`G709PrbsModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsModeEnum>`
                    
                    .. attribute:: g709_prbs_pattern
                    
                    	Pattern of PRBS Test
                    	**type**\:   :py:class:`G709PrbsPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PrbsPatternEnum>`
                    
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
                        self.parent = None
                        self.ec = None
                        self.ec_accum = None
                        self.ec_tca = Dwdm.Ports.Port.Info.G709Info.EcTca()
                        self.ec_tca.parent = self
                        self.efec_mode = None
                        self.fe_cstr = None
                        self.fec_ber = None
                        self.fec_ber_man = None
                        self.fec_mismatch = Dwdm.Ports.Port.Info.G709Info.FecMismatch()
                        self.fec_mismatch.parent = self
                        self.fec_mode = None
                        self.g709_prbs_mode = None
                        self.g709_prbs_pattern = None
                        self.is_fec_mode_default = None
                        self.is_g709_enabled = None
                        self.is_prbs_enabled = None
                        self.loopback_mode = None
                        self.network_conn_id = None
                        self.network_port_id = None
                        self.odu_info = Dwdm.Ports.Port.Info.G709Info.OduInfo()
                        self.odu_info.parent = self
                        self.otu_info = Dwdm.Ports.Port.Info.G709Info.OtuInfo()
                        self.otu_info.parent = self
                        self.prbs_time_stamp = None
                        self.q = None
                        self.q_margin = None
                        self.qmargin_str = None
                        self.qstr = None
                        self.remote_fec_mode = None
                        self.uc = None
                        self.uc_tca = Dwdm.Ports.Port.Info.G709Info.UcTca()
                        self.uc_tca.parent = self


                    class FecMismatch(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:fec-mismatch'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.FecMismatch']['meta_info']


                    class EcTca(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None
                            self.threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ec-tca'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            if self.threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.EcTca']['meta_info']


                    class UcTca(object):
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
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None
                            self.threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:uc-tca'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            if self.threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.UcTca']['meta_info']


                    class OtuInfo(object):
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
                            self.parent = None
                            self.ais = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais()
                            self.ais.parent = self
                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe()
                            self.bbe.parent = self
                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self.bber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber()
                            self.bber.parent = self
                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi()
                            self.bdi.parent = self
                            self.bei = None
                            self.bip = None
                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc()
                            self.eoc.parent = self
                            self.es = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es()
                            self.es.parent = self
                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca()
                            self.es_tca.parent = self
                            self.esr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr()
                            self.esr.parent = self
                            self.fc = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc()
                            self.fc.parent = self
                            self.iae = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae()
                            self.iae.parent = self
                            self.lof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof()
                            self.lof.parent = self
                            self.lom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom()
                            self.lom.parent = self
                            self.los = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los()
                            self.los.parent = self
                            self.oof = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof()
                            self.oof.parent = self
                            self.oom = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom()
                            self.oom.parent = self
                            self.prefec_sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer()
                            self.prefec_sd_ber.parent = self
                            self.prefec_sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer()
                            self.prefec_sf_ber.parent = self
                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer()
                            self.sd_ber.parent = self
                            self.ses = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses()
                            self.ses.parent = self
                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr()
                            self.sesr.parent = self
                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer()
                            self.sf_ber.parent = self
                            self.tim = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim()
                            self.tim.parent = self
                            self.tti = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti()
                            self.tti.parent = self
                            self.uas = Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas()
                            self.uas.parent = self


                        class Los(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:los'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los']['meta_info']


                        class Lof(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:lof'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof']['meta_info']


                        class Lom(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:lom'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom']['meta_info']


                        class Oof(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:oof'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof']['meta_info']


                        class Oom(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:oom'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom']['meta_info']


                        class Ais(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ais'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais']['meta_info']


                        class Iae(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:iae'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae']['meta_info']


                        class Bdi(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bdi'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi']['meta_info']


                        class Tim(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:tim'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim']['meta_info']


                        class Eoc(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:eoc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc']['meta_info']


                        class SfBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sf-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer']['meta_info']


                        class SdBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sd-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer']['meta_info']


                        class PrefecSfBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:prefec-sf-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer']['meta_info']


                        class PrefecSdBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:prefec-sd-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer']['meta_info']


                        class BbeTca(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bbe-tca'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca']['meta_info']


                        class EsTca(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:es-tca'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca']['meta_info']


                        class Bbe(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bbe'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe']['meta_info']


                        class Es(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:es'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es']['meta_info']


                        class Ses(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses']['meta_info']


                        class Uas(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:uas'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas']['meta_info']


                        class Fc(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:fc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc']['meta_info']


                        class Bber(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber']['meta_info']


                        class Esr(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:esr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr']['meta_info']


                        class Sesr(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sesr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr']['meta_info']


                        class Tti(object):
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
                                self.parent = None
                                self.exp_dapi_range = None
                                self.exp_oper_spec_range = None
                                self.exp_sapi_range = None
                                self.expected_dapi = None
                                self.expected_dapi0 = None
                                self.expected_oper_spec = None
                                self.expected_sapi = None
                                self.expected_sapi0 = None
                                self.expected_string_type = None
                                self.expected_tti = None
                                self.rx_dapi = None
                                self.rx_dapi0 = None
                                self.rx_dapi_range = None
                                self.rx_oper_spec = None
                                self.rx_oper_spec_range = None
                                self.rx_sapi = None
                                self.rx_sapi0 = None
                                self.rx_sapi_range = None
                                self.rx_string_type = None
                                self.rx_tti = None
                                self.tx_dapi = None
                                self.tx_dapi0 = None
                                self.tx_dapi_range = None
                                self.tx_oper_spec = None
                                self.tx_oper_spec_range = None
                                self.tx_sapi = None
                                self.tx_sapi0 = None
                                self.tx_sapi_range = None
                                self.tx_string_type = None
                                self.tx_tti = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:tti'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.exp_dapi_range is not None:
                                    return True

                                if self.exp_oper_spec_range is not None:
                                    return True

                                if self.exp_sapi_range is not None:
                                    return True

                                if self.expected_dapi is not None:
                                    return True

                                if self.expected_dapi0 is not None:
                                    return True

                                if self.expected_oper_spec is not None:
                                    return True

                                if self.expected_sapi is not None:
                                    return True

                                if self.expected_sapi0 is not None:
                                    return True

                                if self.expected_string_type is not None:
                                    return True

                                if self.expected_tti is not None:
                                    return True

                                if self.rx_dapi is not None:
                                    return True

                                if self.rx_dapi0 is not None:
                                    return True

                                if self.rx_dapi_range is not None:
                                    return True

                                if self.rx_oper_spec is not None:
                                    return True

                                if self.rx_oper_spec_range is not None:
                                    return True

                                if self.rx_sapi is not None:
                                    return True

                                if self.rx_sapi0 is not None:
                                    return True

                                if self.rx_sapi_range is not None:
                                    return True

                                if self.rx_string_type is not None:
                                    return True

                                if self.rx_tti is not None:
                                    return True

                                if self.tx_dapi is not None:
                                    return True

                                if self.tx_dapi0 is not None:
                                    return True

                                if self.tx_dapi_range is not None:
                                    return True

                                if self.tx_oper_spec is not None:
                                    return True

                                if self.tx_oper_spec_range is not None:
                                    return True

                                if self.tx_sapi is not None:
                                    return True

                                if self.tx_sapi0 is not None:
                                    return True

                                if self.tx_sapi_range is not None:
                                    return True

                                if self.tx_string_type is not None:
                                    return True

                                if self.tx_tti is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:otu-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ais is not None and self.ais._has_data():
                                return True

                            if self.bbe is not None and self.bbe._has_data():
                                return True

                            if self.bbe_tca is not None and self.bbe_tca._has_data():
                                return True

                            if self.bber is not None and self.bber._has_data():
                                return True

                            if self.bdi is not None and self.bdi._has_data():
                                return True

                            if self.bei is not None:
                                return True

                            if self.bip is not None:
                                return True

                            if self.eoc is not None and self.eoc._has_data():
                                return True

                            if self.es is not None and self.es._has_data():
                                return True

                            if self.es_tca is not None and self.es_tca._has_data():
                                return True

                            if self.esr is not None and self.esr._has_data():
                                return True

                            if self.fc is not None and self.fc._has_data():
                                return True

                            if self.iae is not None and self.iae._has_data():
                                return True

                            if self.lof is not None and self.lof._has_data():
                                return True

                            if self.lom is not None and self.lom._has_data():
                                return True

                            if self.los is not None and self.los._has_data():
                                return True

                            if self.oof is not None and self.oof._has_data():
                                return True

                            if self.oom is not None and self.oom._has_data():
                                return True

                            if self.prefec_sd_ber is not None and self.prefec_sd_ber._has_data():
                                return True

                            if self.prefec_sf_ber is not None and self.prefec_sf_ber._has_data():
                                return True

                            if self.sd_ber is not None and self.sd_ber._has_data():
                                return True

                            if self.ses is not None and self.ses._has_data():
                                return True

                            if self.sesr is not None and self.sesr._has_data():
                                return True

                            if self.sf_ber is not None and self.sf_ber._has_data():
                                return True

                            if self.tim is not None and self.tim._has_data():
                                return True

                            if self.tti is not None and self.tti._has_data():
                                return True

                            if self.uas is not None and self.uas._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']


                    class OduInfo(object):
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
                            self.parent = None
                            self.ais = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais()
                            self.ais.parent = self
                            self.bbe = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe()
                            self.bbe.parent = self
                            self.bbe_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca()
                            self.bbe_tca.parent = self
                            self.bber = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber()
                            self.bber.parent = self
                            self.bdi = Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi()
                            self.bdi.parent = self
                            self.bei = None
                            self.bip = None
                            self.eoc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc()
                            self.eoc.parent = self
                            self.es = Dwdm.Ports.Port.Info.G709Info.OduInfo.Es()
                            self.es.parent = self
                            self.es_tca = Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca()
                            self.es_tca.parent = self
                            self.esr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr()
                            self.esr.parent = self
                            self.fc = Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc()
                            self.fc.parent = self
                            self.lck = Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck()
                            self.lck.parent = self
                            self.oci = Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci()
                            self.oci.parent = self
                            self.ptim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim()
                            self.ptim.parent = self
                            self.sd_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer()
                            self.sd_ber.parent = self
                            self.ses = Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses()
                            self.ses.parent = self
                            self.sesr = Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr()
                            self.sesr.parent = self
                            self.sf_ber = Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer()
                            self.sf_ber.parent = self
                            self.tim = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim()
                            self.tim.parent = self
                            self.tti = Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti()
                            self.tti.parent = self
                            self.uas = Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas()
                            self.uas.parent = self


                        class Oci(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:oci'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci']['meta_info']


                        class Ais(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ais'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais']['meta_info']


                        class Lck(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:lck'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck']['meta_info']


                        class Bdi(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bdi'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi']['meta_info']


                        class Eoc(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:eoc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc']['meta_info']


                        class Ptim(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ptim'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim']['meta_info']


                        class Tim(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:tim'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim']['meta_info']


                        class SfBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sf-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer']['meta_info']


                        class SdBer(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sd-ber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer']['meta_info']


                        class BbeTca(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bbe-tca'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca']['meta_info']


                        class EsTca(object):
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
                                self.parent = None
                                self.counter = None
                                self.is_asserted = None
                                self.is_detected = None
                                self.reporting_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:es-tca'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                if self.is_asserted is not None:
                                    return True

                                if self.is_detected is not None:
                                    return True

                                if self.reporting_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca']['meta_info']


                        class Bbe(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bbe'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe']['meta_info']


                        class Es(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:es'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Es']['meta_info']


                        class Ses(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:ses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses']['meta_info']


                        class Uas(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:uas'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas']['meta_info']


                        class Fc(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:fc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc']['meta_info']


                        class Bber(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:bber'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber']['meta_info']


                        class Esr(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:esr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr']['meta_info']


                        class Sesr(object):
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
                                self.parent = None
                                self.counter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:sesr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr']['meta_info']


                        class Tti(object):
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
                                self.parent = None
                                self.exp_dapi_range = None
                                self.exp_oper_spec_range = None
                                self.exp_sapi_range = None
                                self.expected_dapi = None
                                self.expected_dapi0 = None
                                self.expected_oper_spec = None
                                self.expected_sapi = None
                                self.expected_sapi0 = None
                                self.expected_string_type = None
                                self.expected_tti = None
                                self.rx_dapi = None
                                self.rx_dapi0 = None
                                self.rx_dapi_range = None
                                self.rx_oper_spec = None
                                self.rx_oper_spec_range = None
                                self.rx_sapi = None
                                self.rx_sapi0 = None
                                self.rx_sapi_range = None
                                self.rx_string_type = None
                                self.rx_tti = None
                                self.tx_dapi = None
                                self.tx_dapi0 = None
                                self.tx_dapi_range = None
                                self.tx_oper_spec = None
                                self.tx_oper_spec_range = None
                                self.tx_sapi = None
                                self.tx_sapi0 = None
                                self.tx_sapi_range = None
                                self.tx_string_type = None
                                self.tx_tti = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:tti'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.exp_dapi_range is not None:
                                    return True

                                if self.exp_oper_spec_range is not None:
                                    return True

                                if self.exp_sapi_range is not None:
                                    return True

                                if self.expected_dapi is not None:
                                    return True

                                if self.expected_dapi0 is not None:
                                    return True

                                if self.expected_oper_spec is not None:
                                    return True

                                if self.expected_sapi is not None:
                                    return True

                                if self.expected_sapi0 is not None:
                                    return True

                                if self.expected_string_type is not None:
                                    return True

                                if self.expected_tti is not None:
                                    return True

                                if self.rx_dapi is not None:
                                    return True

                                if self.rx_dapi0 is not None:
                                    return True

                                if self.rx_dapi_range is not None:
                                    return True

                                if self.rx_oper_spec is not None:
                                    return True

                                if self.rx_oper_spec_range is not None:
                                    return True

                                if self.rx_sapi is not None:
                                    return True

                                if self.rx_sapi0 is not None:
                                    return True

                                if self.rx_sapi_range is not None:
                                    return True

                                if self.rx_string_type is not None:
                                    return True

                                if self.rx_tti is not None:
                                    return True

                                if self.tx_dapi is not None:
                                    return True

                                if self.tx_dapi0 is not None:
                                    return True

                                if self.tx_dapi_range is not None:
                                    return True

                                if self.tx_oper_spec is not None:
                                    return True

                                if self.tx_oper_spec_range is not None:
                                    return True

                                if self.tx_sapi is not None:
                                    return True

                                if self.tx_sapi0 is not None:
                                    return True

                                if self.tx_sapi_range is not None:
                                    return True

                                if self.tx_string_type is not None:
                                    return True

                                if self.tx_tti is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                                return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:odu-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ais is not None and self.ais._has_data():
                                return True

                            if self.bbe is not None and self.bbe._has_data():
                                return True

                            if self.bbe_tca is not None and self.bbe_tca._has_data():
                                return True

                            if self.bber is not None and self.bber._has_data():
                                return True

                            if self.bdi is not None and self.bdi._has_data():
                                return True

                            if self.bei is not None:
                                return True

                            if self.bip is not None:
                                return True

                            if self.eoc is not None and self.eoc._has_data():
                                return True

                            if self.es is not None and self.es._has_data():
                                return True

                            if self.es_tca is not None and self.es_tca._has_data():
                                return True

                            if self.esr is not None and self.esr._has_data():
                                return True

                            if self.fc is not None and self.fc._has_data():
                                return True

                            if self.lck is not None and self.lck._has_data():
                                return True

                            if self.oci is not None and self.oci._has_data():
                                return True

                            if self.ptim is not None and self.ptim._has_data():
                                return True

                            if self.sd_ber is not None and self.sd_ber._has_data():
                                return True

                            if self.ses is not None and self.ses._has_data():
                                return True

                            if self.sesr is not None and self.sesr._has_data():
                                return True

                            if self.sf_ber is not None and self.sf_ber._has_data():
                                return True

                            if self.tim is not None and self.tim._has_data():
                                return True

                            if self.tti is not None and self.tti._has_data():
                                return True

                            if self.uas is not None and self.uas._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                            return meta._meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:g709-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ec is not None:
                            return True

                        if self.ec_accum is not None:
                            return True

                        if self.ec_tca is not None and self.ec_tca._has_data():
                            return True

                        if self.efec_mode is not None:
                            return True

                        if self.fe_cstr is not None:
                            return True

                        if self.fec_ber is not None:
                            return True

                        if self.fec_ber_man is not None:
                            return True

                        if self.fec_mismatch is not None and self.fec_mismatch._has_data():
                            return True

                        if self.fec_mode is not None:
                            return True

                        if self.g709_prbs_mode is not None:
                            return True

                        if self.g709_prbs_pattern is not None:
                            return True

                        if self.is_fec_mode_default is not None:
                            return True

                        if self.is_g709_enabled is not None:
                            return True

                        if self.is_prbs_enabled is not None:
                            return True

                        if self.loopback_mode is not None:
                            return True

                        if self.network_conn_id is not None:
                            return True

                        if self.network_port_id is not None:
                            return True

                        if self.odu_info is not None and self.odu_info._has_data():
                            return True

                        if self.otu_info is not None and self.otu_info._has_data():
                            return True

                        if self.prbs_time_stamp is not None:
                            return True

                        if self.q is not None:
                            return True

                        if self.q_margin is not None:
                            return True

                        if self.qmargin_str is not None:
                            return True

                        if self.qstr is not None:
                            return True

                        if self.remote_fec_mode is not None:
                            return True

                        if self.uc is not None:
                            return True

                        if self.uc_tca is not None and self.uc_tca._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']


                class OpticsInfo(object):
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
                    	**type**\:   :py:class:`DwdmWaveChannelOwnerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmWaveChannelOwnerEnum>`
                    
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
                        self.parent = None
                        self.chromatic_dispersion = None
                        self.clock_source = None
                        self.configured_wave_channel = None
                        self.default_wave_channel = None
                        self.differential_group_delay = None
                        self.gmpls_set_wave_channel = None
                        self.input_power_fail = None
                        self.is_rx_los_threshold_supported = None
                        self.is_wave_frequency_progressive_valid = None
                        self.is_wave_frequency_valid = None
                        self.laser_bias_current_avg = None
                        self.laser_bias_current_max = None
                        self.laser_bias_current_min = None
                        self.laser_current_bias = None
                        self.laser_current_bias_threshold = None
                        self.optics_type = None
                        self.output_power_fail = None
                        self.phase_noise = None
                        self.polarization_change_rate = None
                        self.polarization_dependent_loss = None
                        self.polarization_mode_dispersion = None
                        self.receive_power = None
                        self.receive_power_avg = None
                        self.receive_power_max = None
                        self.receive_power_min = None
                        self.rx_los_threshold = None
                        self.signal_to_noise_ratio = None
                        self.transmit_power = None
                        self.transmit_power_avg = None
                        self.transmit_power_max = None
                        self.transmit_power_min = None
                        self.transmit_power_threshold = None
                        self.wave_band = None
                        self.wave_channel = None
                        self.wave_channel_owner = None
                        self.wave_frequency = None
                        self.wave_frequency_progressive_string = None
                        self.wavelength_progressive = None
                        self.wavelength_progressive_string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:optics-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.chromatic_dispersion is not None:
                            return True

                        if self.clock_source is not None:
                            return True

                        if self.configured_wave_channel is not None:
                            return True

                        if self.default_wave_channel is not None:
                            return True

                        if self.differential_group_delay is not None:
                            return True

                        if self.gmpls_set_wave_channel is not None:
                            return True

                        if self.input_power_fail is not None:
                            return True

                        if self.is_rx_los_threshold_supported is not None:
                            return True

                        if self.is_wave_frequency_progressive_valid is not None:
                            return True

                        if self.is_wave_frequency_valid is not None:
                            return True

                        if self.laser_bias_current_avg is not None:
                            return True

                        if self.laser_bias_current_max is not None:
                            return True

                        if self.laser_bias_current_min is not None:
                            return True

                        if self.laser_current_bias is not None:
                            return True

                        if self.laser_current_bias_threshold is not None:
                            return True

                        if self.optics_type is not None:
                            return True

                        if self.output_power_fail is not None:
                            return True

                        if self.phase_noise is not None:
                            return True

                        if self.polarization_change_rate is not None:
                            return True

                        if self.polarization_dependent_loss is not None:
                            return True

                        if self.polarization_mode_dispersion is not None:
                            return True

                        if self.receive_power is not None:
                            return True

                        if self.receive_power_avg is not None:
                            return True

                        if self.receive_power_max is not None:
                            return True

                        if self.receive_power_min is not None:
                            return True

                        if self.rx_los_threshold is not None:
                            return True

                        if self.signal_to_noise_ratio is not None:
                            return True

                        if self.transmit_power is not None:
                            return True

                        if self.transmit_power_avg is not None:
                            return True

                        if self.transmit_power_max is not None:
                            return True

                        if self.transmit_power_min is not None:
                            return True

                        if self.transmit_power_threshold is not None:
                            return True

                        if self.wave_band is not None:
                            return True

                        if self.wave_channel is not None:
                            return True

                        if self.wave_channel_owner is not None:
                            return True

                        if self.wave_frequency is not None:
                            return True

                        if self.wave_frequency_progressive_string is not None:
                            return True

                        if self.wavelength_progressive is not None:
                            return True

                        if self.wavelength_progressive_string is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.OpticsInfo']['meta_info']


                class TdcInfo(object):
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
                        self.parent = None
                        self.dispersion_offset = None
                        self.is_reroute_control_enabled = None
                        self.major_alarm = None
                        self.operation_mode = None
                        self.reroute_ber = None
                        self.tdc_status = None
                        self.tdc_valid = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:tdc-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dispersion_offset is not None:
                            return True

                        if self.is_reroute_control_enabled is not None:
                            return True

                        if self.major_alarm is not None:
                            return True

                        if self.operation_mode is not None:
                            return True

                        if self.reroute_ber is not None:
                            return True

                        if self.tdc_status is not None:
                            return True

                        if self.tdc_valid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.TdcInfo']['meta_info']


                class NetworkSrlgInfo(object):
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
                        self.parent = None
                        self.network_srlg = YLeafList()
                        self.network_srlg.parent = self
                        self.network_srlg.name = 'network_srlg'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:network-srlg-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.network_srlg is not None:
                            for child in self.network_srlg:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.NetworkSrlgInfo']['meta_info']


                class Proactive(object):
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
                    	**type**\:   :py:class:`G709PpintfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpintfStateEnum>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:   :py:class:`G709PpfsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpfsmStateEnum>`
                    
                    .. attribute:: proactive_mode
                    
                    	Proactive Mode
                    	**type**\:   :py:class:`G709PpfsmModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709PpfsmModeEnum>`
                    
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
                    	**type**\:   :py:class:`G709ApsByteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ApsByteEnum>`
                    
                    .. attribute:: tas_state
                    
                    	TAS State
                    	**type**\:   :py:class:`DwdmtasStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.DwdmtasStateEnum>`
                    
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
                    	**type**\:   :py:class:`G709ApsByteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.G709ApsByteEnum>`
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.alarm_state = None
                        self.default_rvrt_thresh_coeff = None
                        self.default_rvrt_thresh_power = None
                        self.default_trig_thresh_coeff = None
                        self.default_trig_thresh_power = None
                        self.interface_trigger = None
                        self.prefec_thresh_crossed = None
                        self.proactive_feature = None
                        self.proactive_fsm_if_state = None
                        self.proactive_fsm_state = None
                        self.proactive_mode = None
                        self.protection_trigger = None
                        self.revert_window = None
                        self.rvrt_ec_cnt = None
                        self.rvrt_samples = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.rx_aps = None
                        self.rx_aps_descr = None
                        self.tas_state = None
                        self.trig_ec_cnt = None
                        self.trig_samples = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.trigger_window = None
                        self.tx_aps = None
                        self.tx_aps_descr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:proactive'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.alarm_state is not None:
                            return True

                        if self.default_rvrt_thresh_coeff is not None:
                            return True

                        if self.default_rvrt_thresh_power is not None:
                            return True

                        if self.default_trig_thresh_coeff is not None:
                            return True

                        if self.default_trig_thresh_power is not None:
                            return True

                        if self.interface_trigger is not None:
                            return True

                        if self.prefec_thresh_crossed is not None:
                            return True

                        if self.proactive_feature is not None:
                            return True

                        if self.proactive_fsm_if_state is not None:
                            return True

                        if self.proactive_fsm_state is not None:
                            return True

                        if self.proactive_mode is not None:
                            return True

                        if self.protection_trigger is not None:
                            return True

                        if self.revert_window is not None:
                            return True

                        if self.rvrt_ec_cnt is not None:
                            return True

                        if self.rvrt_samples is not None:
                            return True

                        if self.rvrt_thresh_coeff is not None:
                            return True

                        if self.rvrt_thresh_power is not None:
                            return True

                        if self.rx_aps is not None:
                            return True

                        if self.rx_aps_descr is not None:
                            return True

                        if self.tas_state is not None:
                            return True

                        if self.trig_ec_cnt is not None:
                            return True

                        if self.trig_samples is not None:
                            return True

                        if self.trig_thresh_coeff is not None:
                            return True

                        if self.trig_thresh_power is not None:
                            return True

                        if self.trigger_window is not None:
                            return True

                        if self.tx_aps is not None:
                            return True

                        if self.tx_aps_descr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.Proactive']['meta_info']


                class SignalLog(object):
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
                        self.parent = None
                        self.is_log_enabled = None
                        self.log_filename = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:signal-log'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.is_log_enabled is not None:
                            return True

                        if self.log_filename is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Dwdm.Ports.Port.Info.SignalLog']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.controller_state is not None:
                        return True

                    if self.g709_info is not None and self.g709_info._has_data():
                        return True

                    if self.network_srlg_info is not None and self.network_srlg_info._has_data():
                        return True

                    if self.optics_info is not None and self.optics_info._has_data():
                        return True

                    if self.proactive is not None and self.proactive._has_data():
                        return True

                    if self.signal_log is not None and self.signal_log._has_data():
                        return True

                    if self.slice_state is not None:
                        return True

                    if self.tdc_info is not None and self.tdc_info._has_data():
                        return True

                    if self.transport_admin_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                    return meta._meta_table['Dwdm.Ports.Port.Info']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-dwdm-ui-oper:dwdm/Cisco-IOS-XR-dwdm-ui-oper:ports/Cisco-IOS-XR-dwdm-ui-oper:port[Cisco-IOS-XR-dwdm-ui-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.info is not None and self.info._has_data():
                    return True

                if self.optics is not None and self.optics._has_data():
                    return True

                if self.prbs is not None and self.prbs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                return meta._meta_table['Dwdm.Ports.Port']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-dwdm-ui-oper:dwdm/Cisco-IOS-XR-dwdm-ui-oper:ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.port is not None:
                for child_ref in self.port:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
            return meta._meta_table['Dwdm.Ports']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-dwdm-ui-oper:dwdm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ports is not None and self.ports._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['Dwdm']['meta_info']


class Vtxp(object):
    """
    vtxp
    
    .. attribute:: dwdm_vtxp
    
    	DWDM operational data
    	**type**\:   :py:class:`DwdmVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp>`
    
    

    """

    _prefix = 'dwdm-ui-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.dwdm_vtxp = Vtxp.DwdmVtxp()
        self.dwdm_vtxp.parent = self


    class DwdmVtxp(object):
        """
        DWDM operational data
        
        .. attribute:: port_vtxps
        
        	All DWDM Port operational data
        	**type**\:   :py:class:`PortVtxps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps>`
        
        

        """

        _prefix = 'dwdm-ui-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.port_vtxps = Vtxp.DwdmVtxp.PortVtxps()
            self.port_vtxps.parent = self


        class PortVtxps(object):
            """
            All DWDM Port operational data
            
            .. attribute:: port_vtxp
            
            	DWDM Port operational data
            	**type**\: list of    :py:class:`PortVtxp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper.Vtxp.DwdmVtxp.PortVtxps.PortVtxp>`
            
            

            """

            _prefix = 'dwdm-ui-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.port_vtxp = YList()
                self.port_vtxp.parent = self
                self.port_vtxp.name = 'port_vtxp'


            class PortVtxp(object):
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
                    self.parent = None
                    self.name = None
                    self.info = Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info()
                    self.info.parent = self


                class Info(object):
                    """
                    DWDM port operational data
                    
                    .. attribute:: vtxp_enable
                    
                    	Is VTXP attribute enabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'dwdm-ui-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vtxp_enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dwdm-ui-oper:info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vtxp_enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                        return meta._meta_table['Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-dwdm-ui-oper:vtxp/Cisco-IOS-XR-dwdm-ui-oper:dwdm-vtxp/Cisco-IOS-XR-dwdm-ui-oper:port-vtxps/Cisco-IOS-XR-dwdm-ui-oper:port-vtxp[Cisco-IOS-XR-dwdm-ui-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.info is not None and self.info._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                    return meta._meta_table['Vtxp.DwdmVtxp.PortVtxps.PortVtxp']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-dwdm-ui-oper:vtxp/Cisco-IOS-XR-dwdm-ui-oper:dwdm-vtxp/Cisco-IOS-XR-dwdm-ui-oper:port-vtxps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.port_vtxp is not None:
                    for child_ref in self.port_vtxp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
                return meta._meta_table['Vtxp.DwdmVtxp.PortVtxps']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-dwdm-ui-oper:vtxp/Cisco-IOS-XR-dwdm-ui-oper:dwdm-vtxp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.port_vtxps is not None and self.port_vtxps._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
            return meta._meta_table['Vtxp.DwdmVtxp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-dwdm-ui-oper:vtxp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dwdm_vtxp is not None and self.dwdm_vtxp._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dwdm_ui_oper as meta
        return meta._meta_table['Vtxp']['meta_info']


