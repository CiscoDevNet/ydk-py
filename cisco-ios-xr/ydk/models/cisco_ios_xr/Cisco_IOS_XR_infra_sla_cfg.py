""" Cisco_IOS_XR_infra_sla_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package configuration.

This module contains definitions
for the following management objects\:
  sla\: SLA prtocol and profile Configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Sla(Entity):
    """
    SLA prtocol and profile Configuration
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sla, self).__init__()
        self._top_entity = None

        self.yang_name = "sla"
        self.yang_parent_name = "Cisco-IOS-XR-infra-sla-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"protocols" : ("protocols", Sla.Protocols)}
        self._child_list_classes = {}

        self.protocols = Sla.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._children_yang_names.add("protocols")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-sla-cfg:sla"


    class Protocols(Entity):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\:   :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sla.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "sla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ethernet" : ("ethernet", Sla.Protocols.Ethernet)}
            self._child_list_classes = {}

            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self
            self._children_name_map["ethernet"] = "ethernet"
            self._children_yang_names.add("ethernet")
            self._segment_path = lambda: "protocols"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-cfg:sla/%s" % self._segment_path()


        class Ethernet(Entity):
            """
            The Ethernet SLA protocol
            
            .. attribute:: profiles
            
            	Table of SLA profiles on the protocol
            	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sla.Protocols.Ethernet, self).__init__()

                self.yang_name = "ethernet"
                self.yang_parent_name = "protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"profiles" : ("profiles", Sla.Protocols.Ethernet.Profiles)}
                self._child_list_classes = {}

                self.profiles = Sla.Protocols.Ethernet.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
                self._children_yang_names.add("profiles")
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-cfg:ethernet"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/%s" % self._segment_path()


            class Profiles(Entity):
                """
                Table of SLA profiles on the protocol
                
                .. attribute:: profile
                
                	Name of the profile
                	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.Profiles, self).__init__()

                    self.yang_name = "profiles"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"profile" : ("profile", Sla.Protocols.Ethernet.Profiles.Profile)}

                    self.profile = YList(self)
                    self._segment_path = lambda: "profiles"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sla.Protocols.Ethernet.Profiles, [], name, value)


                class Profile(Entity):
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
                        super(Sla.Protocols.Ethernet.Profiles.Profile, self).__init__()

                        self.yang_name = "profile"
                        self.yang_parent_name = "profiles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"probe" : ("probe", Sla.Protocols.Ethernet.Profiles.Profile.Probe), "schedule" : ("schedule", Sla.Protocols.Ethernet.Profiles.Profile.Schedule), "statistics" : ("statistics", Sla.Protocols.Ethernet.Profiles.Profile.Statistics)}
                        self._child_list_classes = {}

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.packet_type = YLeaf(YType.str, "packet-type")

                        self.probe = Sla.Protocols.Ethernet.Profiles.Profile.Probe()
                        self.probe.parent = self
                        self._children_name_map["probe"] = "probe"
                        self._children_yang_names.add("probe")

                        self.schedule = None
                        self._children_name_map["schedule"] = "schedule"
                        self._children_yang_names.add("schedule")

                        self.statistics = Sla.Protocols.Ethernet.Profiles.Profile.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._children_yang_names.add("statistics")
                        self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/profiles/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile, ['profile_name', 'packet_type'], name, value)


                    class Probe(Entity):
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
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Probe, self).__init__()

                            self.yang_name = "probe"
                            self.yang_parent_name = "profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"packet-size-and-padding" : ("packet_size_and_padding", Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding), "send" : ("send", Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send)}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.synthetic_loss_calculation_packets = YLeaf(YType.uint32, "synthetic-loss-calculation-packets")

                            self.packet_size_and_padding = None
                            self._children_name_map["packet_size_and_padding"] = "packet-size-and-padding"
                            self._children_yang_names.add("packet-size-and-padding")

                            self.send = None
                            self._children_name_map["send"] = "send"
                            self._children_yang_names.add("send")
                            self._segment_path = lambda: "probe"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Probe, ['priority', 'synthetic_loss_calculation_packets'], name, value)


                        class PacketSizeAndPadding(Entity):
                            """
                            Minimum size to pad outgoing packet to
                            
                            .. attribute:: padding_type
                            
                            	Type of padding to be used for the packet
                            	**type**\:   :py:class:`SlaPaddingPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPaddingPattern>`
                            
                            .. attribute:: padding_value
                            
                            	Pattern to be used for hex padding. This can be specified if, and only if, the PaddingType is 'Hex'
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: size
                            
                            	Minimum size to pad outgoing packet to
                            	**type**\:  int
                            
                            	**range:** 1..9000
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding, self).__init__()

                                self.yang_name = "packet-size-and-padding"
                                self.yang_parent_name = "probe"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.padding_type = YLeaf(YType.enumeration, "padding-type")

                                self.padding_value = YLeaf(YType.str, "padding-value")

                                self.size = YLeaf(YType.uint32, "size")
                                self._segment_path = lambda: "packet-size-and-padding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding, ['padding_type', 'padding_value', 'size'], name, value)


                        class Send(Entity):
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
                            	**type**\:   :py:class:`SlaBurstIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBurstIntervalUnitsEnum>`
                            
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
                            	**type**\:   :py:class:`SlaPacketIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPacketIntervalUnitsEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: send_type
                            
                            	The packet distribution\: single packets or bursts of packets.  If 'Burst' is specified , PacketCount and BurstInterval must be specified
                            	**type**\:   :py:class:`SlaSend <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaSend>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send, self).__init__()

                                self.yang_name = "send"
                                self.yang_parent_name = "probe"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.burst_interval = YLeaf(YType.uint32, "burst-interval")

                                self.burst_interval_unit = YLeaf(YType.enumeration, "burst-interval-unit")

                                self.packet_count = YLeaf(YType.uint32, "packet-count")

                                self.packet_interval = YLeaf(YType.uint32, "packet-interval")

                                self.packet_interval_unit = YLeaf(YType.enumeration, "packet-interval-unit")

                                self.send_type = YLeaf(YType.enumeration, "send-type")
                                self._segment_path = lambda: "send"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send, ['burst_interval', 'burst_interval_unit', 'packet_count', 'packet_interval', 'packet_interval_unit', 'send_type'], name, value)


                    class Schedule(Entity):
                        """
                        Schedule to use for probes within an
                        operation
                        
                        .. attribute:: probe_duration
                        
                        	Duration of each probe.  This must be specified if, and only if, ProbeDurationUnit is specified
                        	**type**\:  int
                        
                        	**range:** 1..3600
                        
                        .. attribute:: probe_duration_unit
                        
                        	Time unit associated with the ProbeDuration. The value must not be 'Once'
                        	**type**\:   :py:class:`SlaProbeDurationUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeDurationUnitsEnum>`
                        
                        .. attribute:: probe_interval
                        
                        	Interval between probes.  This must be specified if, and only if, ProbeIntervalUnit is not 'Week' or 'Day'
                        	**type**\:  int
                        
                        	**range:** 1..90
                        
                        .. attribute:: probe_interval_day
                        
                        	Day of week on which to schedule probes.  This must be specified if, and only if, ProbeIntervalUnit is 'Week'
                        	**type**\:   :py:class:`SlaProbeIntervalDayEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalDayEnum>`
                        
                        .. attribute:: probe_interval_unit
                        
                        	Time unit associated with the ProbeInterval. The value must not be 'Once'.  If 'Week' or 'Day' is specified, probes are scheduled weekly or daily respectively
                        	**type**\:   :py:class:`SlaProbeIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalUnitsEnum>`
                        
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
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Schedule, self).__init__()

                            self.yang_name = "schedule"
                            self.yang_parent_name = "profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.probe_duration = YLeaf(YType.uint32, "probe-duration")

                            self.probe_duration_unit = YLeaf(YType.enumeration, "probe-duration-unit")

                            self.probe_interval = YLeaf(YType.uint32, "probe-interval")

                            self.probe_interval_day = YLeaf(YType.enumeration, "probe-interval-day")

                            self.probe_interval_unit = YLeaf(YType.enumeration, "probe-interval-unit")

                            self.start_time_hour = YLeaf(YType.uint32, "start-time-hour")

                            self.start_time_minute = YLeaf(YType.uint32, "start-time-minute")

                            self.start_time_second = YLeaf(YType.uint32, "start-time-second")
                            self._segment_path = lambda: "schedule"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Schedule, ['probe_duration', 'probe_duration_unit', 'probe_interval', 'probe_interval_day', 'probe_interval_unit', 'start_time_hour', 'start_time_minute', 'start_time_second'], name, value)


                    class Statistics(Entity):
                        """
                        Statistics configuration for the SLA profile
                        
                        .. attribute:: statistic
                        
                        	Type of statistic
                        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"statistic" : ("statistic", Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic)}

                            self.statistic = YList(self)
                            self._segment_path = lambda: "statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Statistics, [], name, value)


                        class Statistic(Entity):
                            """
                            Type of statistic
                            
                            .. attribute:: statistic_name  <key>
                            
                            	The type of statistic to measure
                            	**type**\:   :py:class:`SlaStatisticTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaStatisticTypeEnum>`
                            
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
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic, self).__init__()

                                self.yang_name = "statistic"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"aggregation" : ("aggregation", Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation), "buckets-size" : ("buckets_size", Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize)}
                                self._child_list_classes = {}

                                self.statistic_name = YLeaf(YType.enumeration, "statistic-name")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.aggregation = None
                                self._children_name_map["aggregation"] = "aggregation"
                                self._children_yang_names.add("aggregation")

                                self.buckets_size = None
                                self._children_name_map["buckets_size"] = "buckets-size"
                                self._children_yang_names.add("buckets-size")
                                self._segment_path = lambda: "statistic" + "[statistic-name='" + self.statistic_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic, ['statistic_name', 'buckets_archive', 'enable'], name, value)


                            class Aggregation(Entity):
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
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation, self).__init__()

                                    self.yang_name = "aggregation"
                                    self.yang_parent_name = "statistic"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self.is_presence_container = True

                                    self.bins_count = YLeaf(YType.uint32, "bins-count")

                                    self.bins_width = YLeaf(YType.uint32, "bins-width")

                                    self.bins_width_tenths = YLeaf(YType.uint32, "bins-width-tenths")
                                    self._segment_path = lambda: "aggregation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation, ['bins_count', 'bins_width', 'bins_width_tenths'], name, value)


                            class BucketsSize(Entity):
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
                                	**type**\:   :py:class:`SlaBucketsSizeUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBucketsSizeUnitsEnum>`
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize, self).__init__()

                                    self.yang_name = "buckets-size"
                                    self.yang_parent_name = "statistic"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self.is_presence_container = True

                                    self.buckets_size = YLeaf(YType.uint32, "buckets-size")

                                    self.buckets_size_unit = YLeaf(YType.enumeration, "buckets-size-unit")
                                    self._segment_path = lambda: "buckets-size"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize, ['buckets_size', 'buckets_size_unit'], name, value)

    def clone_ptr(self):
        self._top_entity = Sla()
        return self._top_entity

