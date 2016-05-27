""" Cisco_IOS_XR_infra_sla_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package configuration.

This module contains definitions
for the following management objects\:
  sla\: SLA prtocol and profile Configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaBucketsSizeUnitsEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaBurstIntervalUnitsEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaPacketIntervalUnitsEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaPaddingPatternEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaProbeDurationUnitsEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaProbeIntervalDayEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaProbeIntervalUnitsEnumEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaSendEnum
from ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes import SlaStatisticTypeEnumEnum


class Sla(object):
    """
    SLA prtocol and profile Configuration
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\: :py:class:`Protocols <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.protocols = Sla.Protocols()
        self.protocols.parent = self


    class Protocols(object):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\: :py:class:`Ethernet <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self


        class Ethernet(object):
            """
            The Ethernet SLA protocol
            
            .. attribute:: profiles
            
            	Table of SLA profiles on the protocol
            	**type**\: :py:class:`Profiles <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.profiles = Sla.Protocols.Ethernet.Profiles()
                self.profiles.parent = self


            class Profiles(object):
                """
                Table of SLA profiles on the protocol
                
                .. attribute:: profile
                
                	Name of the profile
                	**type**\: list of :py:class:`Profile <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = YList()
                    self.profile.parent = self
                    self.profile.name = 'profile'


                class Profile(object):
                    """
                    Name of the profile
                    
                    .. attribute:: profile_name  <key>
                    
                    	Profile name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: statistics
                    
                    	Statistics configuration for the SLA profile
                    	**type**\: :py:class:`Statistics <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics>`
                    
                    .. attribute:: schedule
                    
                    	Schedule to use for probes within an operation
                    	**type**\: :py:class:`Schedule <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Schedule>`
                    
                    .. attribute:: probe
                    
                    	Probe configuration for the SLA profile
                    	**type**\: :py:class:`Probe <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe>`
                    
                    .. attribute:: packet_type
                    
                    	The possible packet types are cfm\-loopback, cfm\-delay\-measurement, cfm\-delay\-measurement\-version\-0 and cfm\-synthetic\-loss\-measurement
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile_name = None
                        self.statistics = Sla.Protocols.Ethernet.Profiles.Profile.Statistics()
                        self.statistics.parent = self
                        self.schedule = None
                        self.probe = Sla.Protocols.Ethernet.Profiles.Profile.Probe()
                        self.probe.parent = self
                        self.packet_type = None


                    class Statistics(object):
                        """
                        Statistics configuration for the SLA profile
                        
                        .. attribute:: statistic
                        
                        	Type of statistic
                        	**type**\: list of :py:class:`Statistic <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistic = YList()
                            self.statistic.parent = self
                            self.statistic.name = 'statistic'


                        class Statistic(object):
                            """
                            Type of statistic
                            
                            .. attribute:: statistic_name  <key>
                            
                            	The type of statistic to measure
                            	**type**\: :py:class:`SlaStatisticTypeEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaStatisticTypeEnumEnum>`
                            
                            .. attribute:: buckets_size
                            
                            	Size of the buckets into which statistics are collected
                            	**type**\: :py:class:`BucketsSize <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize>`
                            
                            .. attribute:: aggregation
                            
                            	Aggregation to apply to results for the statistic
                            	**type**\: :py:class:`Aggregation <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation>`
                            
                            .. attribute:: enable
                            
                            	Enable statistic gathering of the metric
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: buckets_archive
                            
                            	Number of buckets to archive in memory
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.statistic_name = None
                                self.buckets_size = None
                                self.aggregation = None
                                self.enable = None
                                self.buckets_archive = None


                            class BucketsSize(object):
                                """
                                Size of the buckets into which statistics
                                are collected
                                
                                .. attribute:: buckets_size
                                
                                	Size of each bucket
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                .. attribute:: buckets_size_unit
                                
                                	Unit associated with the BucketsSize
                                	**type**\: :py:class:`SlaBucketsSizeUnitsEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaBucketsSizeUnitsEnumEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.buckets_size = None
                                    self.buckets_size_unit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:buckets-size'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.buckets_size is not None:
                                        return True

                                    if self.buckets_size_unit is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize']['meta_info']


                            class Aggregation(object):
                                """
                                Aggregation to apply to results for the
                                statistic
                                
                                .. attribute:: bins_count
                                
                                	Number of bins to aggregate results into (0 for no aggregation)
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin
                                	**type**\: int
                                
                                	**range:** 1..10000
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                .. attribute:: bins_width_tenths
                                
                                	Tenths portion of the bin width
                                	**type**\: int
                                
                                	**range:** 0..9
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bins_width_tenths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:aggregation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.bins_count is not None:
                                        return True

                                    if self.bins_width is not None:
                                        return True

                                    if self.bins_width_tenths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.statistic_name is None:
                                    raise YPYDataValidationError('Key property statistic_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:statistic[Cisco-IOS-XR-ethernet-cfm-cfg:statistic-name = ' + str(self.statistic_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.statistic_name is not None:
                                    return True

                                if self.buckets_size is not None and self.buckets_size._has_data():
                                    return True

                                if self.aggregation is not None and self.aggregation._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.statistic is not None:
                                for child_ref in self.statistic:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics']['meta_info']


                    class Schedule(object):
                        """
                        Schedule to use for probes within an
                        operation
                        
                        .. attribute:: probe_interval
                        
                        	Interval between probes.  This must be specified if, and only if, ProbeIntervalUnit is not 'Week' or 'Day'
                        	**type**\: int
                        
                        	**range:** 1..90
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: probe_interval_day
                        
                        	Day of week on which to schedule probes.  This must be specified if, and only if, ProbeIntervalUnit is 'Week'
                        	**type**\: :py:class:`SlaProbeIntervalDayEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalDayEnumEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: probe_interval_unit
                        
                        	Time unit associated with the ProbeInterval. The value must not be 'Once'.  If 'Week' or 'Day' is specified, probes are scheduled weekly or daily respectively
                        	**type**\: :py:class:`SlaProbeIntervalUnitsEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalUnitsEnumEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: start_time_hour
                        
                        	Time after midnight (in UTC) to send the first packet each day
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: start_time_minute
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must be specified if, and only if, StartTimeHour is specified
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: start_time_second
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must only be specified if StartTimeHour is specified, and must not be specified if ProbeIntervalUnit is 'Week' or 'Day'
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: probe_duration
                        
                        	Duration of each probe.  This must be specified if, and only if, ProbeDurationUnit is specified
                        	**type**\: int
                        
                        	**range:** 1..3600
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: probe_duration_unit
                        
                        	Time unit associated with the ProbeDuration. The value must not be 'Once'
                        	**type**\: :py:class:`SlaProbeDurationUnitsEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeDurationUnitsEnumEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.probe_interval = None
                            self.probe_interval_day = None
                            self.probe_interval_unit = None
                            self.start_time_hour = None
                            self.start_time_minute = None
                            self.start_time_second = None
                            self.probe_duration = None
                            self.probe_duration_unit = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.probe_interval is not None:
                                return True

                            if self.probe_interval_day is not None:
                                return True

                            if self.probe_interval_unit is not None:
                                return True

                            if self.start_time_hour is not None:
                                return True

                            if self.start_time_minute is not None:
                                return True

                            if self.start_time_second is not None:
                                return True

                            if self.probe_duration is not None:
                                return True

                            if self.probe_duration_unit is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Schedule']['meta_info']


                    class Probe(object):
                        """
                        Probe configuration for the SLA profile
                        
                        .. attribute:: send
                        
                        	Schedule to use for packets within a burst.  The default value is to send a single packet once
                        	**type**\: :py:class:`Send <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send>`
                        
                        .. attribute:: packet_size_and_padding
                        
                        	Minimum size to pad outgoing packet to
                        	**type**\: :py:class:`PacketSizeAndPadding <ydk.models.infra.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding>`
                        
                        .. attribute:: priority
                        
                        	Priority class to assign to outgoing SLA packets
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: synthetic_loss_calculation_packets
                        
                        	Number of packets to use in each FLR calculation
                        	**type**\: int
                        
                        	**range:** 10..12096000
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.send = None
                            self.packet_size_and_padding = None
                            self.priority = None
                            self.synthetic_loss_calculation_packets = None


                        class Send(object):
                            """
                            Schedule to use for packets within a burst. 
                            The default value is to send a single packet
                            once.
                            
                            .. attribute:: burst_interval
                            
                            	Interval between bursts.  This must be specified if, and only if, the SendType is 'Burst' and the 'BurstIntervalUnit' is not 'Once'
                            	**type**\: int
                            
                            	**range:** 1..3600
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: burst_interval_unit
                            
                            	Time unit associated with the BurstInterval .  This must be specified if, and only is, SendType is 'Burst'
                            	**type**\: :py:class:`SlaBurstIntervalUnitsEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaBurstIntervalUnitsEnumEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: packet_interval
                            
                            	Interval between packets
                            	**type**\: int
                            
                            	**range:** 1..10000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: packet_interval_unit
                            
                            	Time unit associated with the PacketInterval, must not be 'Once'
                            	**type**\: :py:class:`SlaPacketIntervalUnitsEnumEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaPacketIntervalUnitsEnumEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: packet_count
                            
                            	The number of packets in each burst.  This must be specified if, and only if, the SendType is 'Burst'
                            	**type**\: int
                            
                            	**range:** 2..1200
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: send_type
                            
                            	The packet distribution\: single packets or bursts of packets.  If 'Burst' is specified , PacketCount and BurstInterval must be specified
                            	**type**\: :py:class:`SlaSendEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaSendEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.burst_interval = None
                                self.burst_interval_unit = None
                                self.packet_interval = None
                                self.packet_interval_unit = None
                                self.packet_count = None
                                self.send_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:send'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.burst_interval is not None:
                                    return True

                                if self.burst_interval_unit is not None:
                                    return True

                                if self.packet_interval is not None:
                                    return True

                                if self.packet_interval_unit is not None:
                                    return True

                                if self.packet_count is not None:
                                    return True

                                if self.send_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send']['meta_info']


                        class PacketSizeAndPadding(object):
                            """
                            Minimum size to pad outgoing packet to
                            
                            .. attribute:: size
                            
                            	Minimum size to pad outgoing packet to
                            	**type**\: int
                            
                            	**range:** 1..9000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: padding_type
                            
                            	Type of padding to be used for the packet
                            	**type**\: :py:class:`SlaPaddingPatternEnum <ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes.SlaPaddingPatternEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: padding_value
                            
                            	Pattern to be used for hex padding. This can be specified if, and only if, the PaddingType is 'Hex'
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.size = None
                                self.padding_type = None
                                self.padding_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:packet-size-and-padding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.size is not None:
                                    return True

                                if self.padding_type is not None:
                                    return True

                                if self.padding_value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:probe'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.send is not None and self.send._has_data():
                                return True

                            if self.packet_size_and_padding is not None and self.packet_size_and_padding._has_data():
                                return True

                            if self.priority is not None:
                                return True

                            if self.synthetic_loss_calculation_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe']['meta_info']

                    @property
                    def _common_path(self):
                        if self.profile_name is None:
                            raise YPYDataValidationError('Key property profile_name is None')

                        return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/Cisco-IOS-XR-ethernet-cfm-cfg:profiles/Cisco-IOS-XR-ethernet-cfm-cfg:profile[Cisco-IOS-XR-ethernet-cfm-cfg:profile-name = ' + str(self.profile_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.profile_name is not None:
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        if self.schedule is not None and self.schedule._has_data():
                            return True

                        if self.probe is not None and self.probe._has_data():
                            return True

                        if self.packet_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/Cisco-IOS-XR-ethernet-cfm-cfg:profiles'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        for child_ref in self.profile:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.profiles is not None and self.profiles._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                return meta._meta_table['Sla.Protocols.Ethernet']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ethernet is not None and self.ethernet._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
            return meta._meta_table['Sla.Protocols']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-sla-cfg:sla'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.protocols is not None and self.protocols._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
        return meta._meta_table['Sla']['meta_info']


