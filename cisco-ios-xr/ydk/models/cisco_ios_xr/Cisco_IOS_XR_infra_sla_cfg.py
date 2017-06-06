""" Cisco_IOS_XR_infra_sla_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package configuration.

This module contains definitions
for the following management objects\:
  sla\: SLA prtocol and profile Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Sla(object):
    """
    SLA prtocol and profile Configuration
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols>`
    
    

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
        	**type**\:   :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet>`
        
        

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
            	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles>`
            
            

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
                	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile>`
                
                

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
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: packet_type
                    
                    	The possible packet types are cfm\-loopback, cfm\-delay\-measurement, cfm\-delay\-measurement\-version\-0, cfm\-loss\-measurement and cfm\-synthetic\-loss\-measurement
                    	**type**\:  str
                    
                    .. attribute:: probe
                    
                    	Probe configuration for the SLA profile
                    	**type**\:   :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe>`
                    
                    .. attribute:: schedule
                    
                    	Schedule to use for probes within an operation
                    	**type**\:   :py:class:`Schedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Schedule>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: statistics
                    
                    	Statistics configuration for the SLA profile
                    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile_name = None
                        self.packet_type = None
                        self.probe = Sla.Protocols.Ethernet.Profiles.Profile.Probe()
                        self.probe.parent = self
                        self.schedule = None
                        self.statistics = Sla.Protocols.Ethernet.Profiles.Profile.Statistics()
                        self.statistics.parent = self


                    class Statistics(object):
                        """
                        Statistics configuration for the SLA profile
                        
                        .. attribute:: statistic
                        
                        	Type of statistic
                        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic>`
                        
                        

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
                            	**type**\:   :py:class:`SlaStatisticTypeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaStatisticTypeEnumEnum>`
                            
                            .. attribute:: aggregation
                            
                            	Aggregation to apply to results for the statistic
                            	**type**\:   :py:class:`Aggregation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: buckets_archive
                            
                            	Number of buckets to archive in memory
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            .. attribute:: buckets_size
                            
                            	Size of the buckets into which statistics are collected
                            	**type**\:   :py:class:`BucketsSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: enable
                            
                            	Enable statistic gathering of the metric
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.statistic_name = None
                                self.aggregation = None
                                self.buckets_archive = None
                                self.buckets_size = None
                                self.enable = None


                            class BucketsSize(object):
                                """
                                Size of the buckets into which statistics
                                are collected
                                
                                .. attribute:: buckets_size
                                
                                	Size of each bucket
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: buckets_size_unit
                                
                                	Unit associated with the BucketsSize
                                	**type**\:   :py:class:`SlaBucketsSizeUnitsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBucketsSizeUnitsEnumEnum>`
                                
                                	**mandatory**\: True
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.buckets_size = None
                                    self.buckets_size_unit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:buckets-size'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.buckets_size is not None:
                                        return True

                                    if self.buckets_size_unit is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize']['meta_info']


                            class Aggregation(object):
                                """
                                Aggregation to apply to results for the
                                statistic
                                
                                .. attribute:: bins_count
                                
                                	Number of bins to aggregate results into (0 for no aggregation)
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin
                                	**type**\:  int
                                
                                	**range:** 1..10000
                                
                                .. attribute:: bins_width_tenths
                                
                                	Tenths portion of the bin width
                                	**type**\:  int
                                
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
                                    self._is_presence = True
                                    self.bins_count = None
                                    self.bins_width = None
                                    self.bins_width_tenths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:aggregation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.bins_count is not None:
                                        return True

                                    if self.bins_width is not None:
                                        return True

                                    if self.bins_width_tenths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.statistic_name is None:
                                    raise YPYModelError('Key property statistic_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:statistic[Cisco-IOS-XR-ethernet-cfm-cfg:statistic-name = ' + str(self.statistic_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.statistic_name is not None:
                                    return True

                                if self.aggregation is not None and self.aggregation._has_data():
                                    return True

                                if self.buckets_archive is not None:
                                    return True

                                if self.buckets_size is not None and self.buckets_size._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.statistic is not None:
                                for child_ref in self.statistic:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics']['meta_info']


                    class Schedule(object):
                        """
                        Schedule to use for probes within an
                        operation
                        
                        .. attribute:: probe_duration
                        
                        	Duration of each probe.  This must be specified if, and only if, ProbeDurationUnit is specified
                        	**type**\:  int
                        
                        	**range:** 1..3600
                        
                        .. attribute:: probe_duration_unit
                        
                        	Time unit associated with the ProbeDuration. The value must not be 'Once'
                        	**type**\:   :py:class:`SlaProbeDurationUnitsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeDurationUnitsEnumEnum>`
                        
                        .. attribute:: probe_interval
                        
                        	Interval between probes.  This must be specified if, and only if, ProbeIntervalUnit is not 'Week' or 'Day'
                        	**type**\:  int
                        
                        	**range:** 1..90
                        
                        .. attribute:: probe_interval_day
                        
                        	Day of week on which to schedule probes.  This must be specified if, and only if, ProbeIntervalUnit is 'Week'
                        	**type**\:   :py:class:`SlaProbeIntervalDayEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalDayEnumEnum>`
                        
                        .. attribute:: probe_interval_unit
                        
                        	Time unit associated with the ProbeInterval. The value must not be 'Once'.  If 'Week' or 'Day' is specified, probes are scheduled weekly or daily respectively
                        	**type**\:   :py:class:`SlaProbeIntervalUnitsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalUnitsEnumEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: start_time_hour
                        
                        	Time after midnight (in UTC) to send the first packet each day
                        	**type**\:  int
                        
                        	**range:** 0..23
                        
                        .. attribute:: start_time_minute
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must be specified if, and only if, StartTimeHour is specified
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: start_time_second
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must only be specified if StartTimeHour is specified, and must not be specified if ProbeIntervalUnit is 'Week' or 'Day'
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.probe_duration = None
                            self.probe_duration_unit = None
                            self.probe_interval = None
                            self.probe_interval_day = None
                            self.probe_interval_unit = None
                            self.start_time_hour = None
                            self.start_time_minute = None
                            self.start_time_second = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:schedule'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.probe_duration is not None:
                                return True

                            if self.probe_duration_unit is not None:
                                return True

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

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Schedule']['meta_info']


                    class Probe(object):
                        """
                        Probe configuration for the SLA profile
                        
                        .. attribute:: packet_size_and_padding
                        
                        	Minimum size to pad outgoing packet to
                        	**type**\:   :py:class:`PacketSizeAndPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: priority
                        
                        	Priority class to assign to outgoing SLA packets
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        .. attribute:: send
                        
                        	Schedule to use for packets within a burst.  The default value is to send a single packet once
                        	**type**\:   :py:class:`Send <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: synthetic_loss_calculation_packets
                        
                        	Number of packets to use in each FLR calculation
                        	**type**\:  int
                        
                        	**range:** 10..12096000
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.packet_size_and_padding = None
                            self.priority = None
                            self.send = None
                            self.synthetic_loss_calculation_packets = None


                        class Send(object):
                            """
                            Schedule to use for packets within a burst. 
                            The default value is to send a single packet
                            once.
                            
                            .. attribute:: burst_interval
                            
                            	Interval between bursts.  This must be specified if, and only if, the SendType is 'Burst' and the 'BurstIntervalUnit' is not 'Once'
                            	**type**\:  int
                            
                            	**range:** 1..3600
                            
                            .. attribute:: burst_interval_unit
                            
                            	Time unit associated with the BurstInterval .  This must be specified if, and only if, SendType is 'Burst'
                            	**type**\:   :py:class:`SlaBurstIntervalUnitsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBurstIntervalUnitsEnumEnum>`
                            
                            .. attribute:: packet_count
                            
                            	The number of packets in each burst.  This must be specified if, and only if, the SendType is 'Burst'
                            	**type**\:  int
                            
                            	**range:** 2..1200
                            
                            .. attribute:: packet_interval
                            
                            	Interval between packets.  This must be specified if, and only if, PacketIntervalUnit is not 'Once'
                            	**type**\:  int
                            
                            	**range:** 1..30000
                            
                            .. attribute:: packet_interval_unit
                            
                            	Time unit associated with the PacketInterval
                            	**type**\:   :py:class:`SlaPacketIntervalUnitsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPacketIntervalUnitsEnumEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: send_type
                            
                            	The packet distribution\: single packets or bursts of packets.  If 'Burst' is specified , PacketCount and BurstInterval must be specified
                            	**type**\:   :py:class:`SlaSendEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaSendEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.burst_interval = None
                                self.burst_interval_unit = None
                                self.packet_count = None
                                self.packet_interval = None
                                self.packet_interval_unit = None
                                self.send_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:send'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.burst_interval is not None:
                                    return True

                                if self.burst_interval_unit is not None:
                                    return True

                                if self.packet_count is not None:
                                    return True

                                if self.packet_interval is not None:
                                    return True

                                if self.packet_interval_unit is not None:
                                    return True

                                if self.send_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send']['meta_info']


                        class PacketSizeAndPadding(object):
                            """
                            Minimum size to pad outgoing packet to
                            
                            .. attribute:: padding_type
                            
                            	Type of padding to be used for the packet
                            	**type**\:   :py:class:`SlaPaddingPatternEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPaddingPatternEnum>`
                            
                            .. attribute:: padding_value
                            
                            	Pattern to be used for hex padding. This can be specified if, and only if, the PaddingType is 'Hex'
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: size
                            
                            	Minimum size to pad outgoing packet to
                            	**type**\:  int
                            
                            	**range:** 1..9000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.padding_type = None
                                self.padding_value = None
                                self.size = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:packet-size-and-padding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.padding_type is not None:
                                    return True

                                if self.padding_value is not None:
                                    return True

                                if self.size is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                                return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:probe'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.packet_size_and_padding is not None and self.packet_size_and_padding._has_data():
                                return True

                            if self.priority is not None:
                                return True

                            if self.send is not None and self.send._has_data():
                                return True

                            if self.synthetic_loss_calculation_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                            return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe']['meta_info']

                    @property
                    def _common_path(self):
                        if self.profile_name is None:
                            raise YPYModelError('Key property profile_name is None')

                        return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/Cisco-IOS-XR-ethernet-cfm-cfg:profiles/Cisco-IOS-XR-ethernet-cfm-cfg:profile[Cisco-IOS-XR-ethernet-cfm-cfg:profile-name = ' + str(self.profile_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.profile_name is not None:
                            return True

                        if self.packet_type is not None:
                            return True

                        if self.probe is not None and self.probe._has_data():
                            return True

                        if self.schedule is not None and self.schedule._has_data():
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                        return meta._meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/Cisco-IOS-XR-ethernet-cfm-cfg:profiles'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile is not None:
                        for child_ref in self.profile:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                    return meta._meta_table['Sla.Protocols.Ethernet.Profiles']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.profiles is not None and self.profiles._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
                return meta._meta_table['Sla.Protocols.Ethernet']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-sla-cfg:sla/Cisco-IOS-XR-infra-sla-cfg:protocols'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.ethernet is not None and self.ethernet._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
            return meta._meta_table['Sla.Protocols']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-sla-cfg:sla'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.protocols is not None and self.protocols._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_cfg as meta
        return meta._meta_table['Sla']['meta_info']


