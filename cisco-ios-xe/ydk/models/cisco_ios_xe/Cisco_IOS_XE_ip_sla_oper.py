""" Cisco_IOS_XE_ip_sla_oper 

This module contains a collection of YANG definitions
for monitoring of IP SLA statistics of a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AccuracyType(Enum):
    """
    AccuracyType (Enum Class)

    IP SLA accuracy type

    .. data:: accuracy_milliseconds = 0

    .. data:: accuracy_microseconds = 1

    """

    accuracy_milliseconds = Enum.YLeaf(0, "accuracy-milliseconds")

    accuracy_microseconds = Enum.YLeaf(1, "accuracy-microseconds")


class RttType(Enum):
    """
    RttType (Enum Class)

    IP SLA RTT type

    .. data:: rtt_known = 0

    .. data:: rtt_unknown = 1

    .. data:: rtt_could_not_find = 2

    """

    rtt_known = Enum.YLeaf(0, "rtt-known")

    rtt_unknown = Enum.YLeaf(1, "rtt-unknown")

    rtt_could_not_find = Enum.YLeaf(2, "rtt-could-not-find")


class SlaOperType(Enum):
    """
    SlaOperType (Enum Class)

    IP SLA operational type

    .. data:: oper_type_unknown = 0

    .. data:: oper_type_udp_echo = 1

    .. data:: oper_type_udp_jitter = 2

    .. data:: oper_type_icmp_jitter = 3

    .. data:: oper_type_ethernet_jitter = 4

    .. data:: oper_type_ethernet_echo = 5

    .. data:: oper_type_y1731_delay = 6

    .. data:: oper_type_y1731_loss = 7

    .. data:: oper_type_video = 8

    .. data:: oper_type_mcast = 9

    .. data:: oper_type_pong = 10

    .. data:: oper_type_path_jitter = 11

    .. data:: oper_type_icmp_echo = 12

    """

    oper_type_unknown = Enum.YLeaf(0, "oper-type-unknown")

    oper_type_udp_echo = Enum.YLeaf(1, "oper-type-udp-echo")

    oper_type_udp_jitter = Enum.YLeaf(2, "oper-type-udp-jitter")

    oper_type_icmp_jitter = Enum.YLeaf(3, "oper-type-icmp-jitter")

    oper_type_ethernet_jitter = Enum.YLeaf(4, "oper-type-ethernet-jitter")

    oper_type_ethernet_echo = Enum.YLeaf(5, "oper-type-ethernet-echo")

    oper_type_y1731_delay = Enum.YLeaf(6, "oper-type-y1731-delay")

    oper_type_y1731_loss = Enum.YLeaf(7, "oper-type-y1731-loss")

    oper_type_video = Enum.YLeaf(8, "oper-type-video")

    oper_type_mcast = Enum.YLeaf(9, "oper-type-mcast")

    oper_type_pong = Enum.YLeaf(10, "oper-type-pong")

    oper_type_path_jitter = Enum.YLeaf(11, "oper-type-path-jitter")

    oper_type_icmp_echo = Enum.YLeaf(12, "oper-type-icmp-echo")


class SlaReturnCode(Enum):
    """
    SlaReturnCode (Enum Class)

    IP SLA return code

    .. data:: ret_code_unknown = 0

    .. data:: ret_code_ok = 1

    .. data:: ret_code_disconnected = 2

    .. data:: ret_code_busy = 3

    .. data:: ret_code_timeout = 4

    .. data:: ret_code_no_connection = 5

    .. data:: ret_code_internal_error = 6

    .. data:: ret_code_operation_failure = 7

    .. data:: ret_code_could_not_find = 8

    """

    ret_code_unknown = Enum.YLeaf(0, "ret-code-unknown")

    ret_code_ok = Enum.YLeaf(1, "ret-code-ok")

    ret_code_disconnected = Enum.YLeaf(2, "ret-code-disconnected")

    ret_code_busy = Enum.YLeaf(3, "ret-code-busy")

    ret_code_timeout = Enum.YLeaf(4, "ret-code-timeout")

    ret_code_no_connection = Enum.YLeaf(5, "ret-code-no-connection")

    ret_code_internal_error = Enum.YLeaf(6, "ret-code-internal-error")

    ret_code_operation_failure = Enum.YLeaf(7, "ret-code-operation-failure")

    ret_code_could_not_find = Enum.YLeaf(8, "ret-code-could-not-find")


class TtlType(Enum):
    """
    TtlType (Enum Class)

    IP SLA time\-to\-live type

    .. data:: ttl_finite = 0

    .. data:: ttl_forever = 1

    """

    ttl_finite = Enum.YLeaf(0, "ttl-finite")

    ttl_forever = Enum.YLeaf(1, "ttl-forever")



class IpSlaStats(Entity):
    """
    Data nodes for All IP SLA Statistics
    
    .. attribute:: sla_oper_entry
    
    	The list of IP SLA operations with statistics info
    	**type**\: list of  		 :py:class:`SlaOperEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry>`
    
    

    """

    _prefix = 'ip-sla-ios-xe-oper'
    _revision = '2017-09-25'

    def __init__(self):
        super(IpSlaStats, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-sla-stats"
        self.yang_parent_name = "Cisco-IOS-XE-ip-sla-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("sla-oper-entry", ("sla_oper_entry", IpSlaStats.SlaOperEntry))])
        self._leafs = OrderedDict()

        self.sla_oper_entry = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-ip-sla-oper:ip-sla-stats"

    def __setattr__(self, name, value):
        self._perform_setattr(IpSlaStats, [], name, value)


    class SlaOperEntry(Entity):
        """
        The list of IP SLA operations with statistics info
        
        .. attribute:: oper_id  (key)
        
        	Entry unique identifier
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: oper_type
        
        	Entry type
        	**type**\:  :py:class:`SlaOperType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaOperType>`
        
        .. attribute:: latest_return_code
        
        	Latest return code
        	**type**\:  :py:class:`SlaReturnCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaReturnCode>`
        
        .. attribute:: success_count
        
        	Success count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: failure_count
        
        	Failure count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: latest_oper_start_time
        
        	Latest start time
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: rtt_info
        
        	RTT information
        	**type**\:  :py:class:`RttInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo>`
        
        .. attribute:: measure_stats
        
        	Measured statistics
        	**type**\:  :py:class:`MeasureStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.MeasureStats>`
        
        .. attribute:: stats
        
        	Statistics
        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats>`
        
        

        """

        _prefix = 'ip-sla-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(IpSlaStats.SlaOperEntry, self).__init__()

            self.yang_name = "sla-oper-entry"
            self.yang_parent_name = "ip-sla-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['oper_id']
            self._child_container_classes = OrderedDict([("rtt-info", ("rtt_info", IpSlaStats.SlaOperEntry.RttInfo)), ("measure-stats", ("measure_stats", IpSlaStats.SlaOperEntry.MeasureStats)), ("stats", ("stats", IpSlaStats.SlaOperEntry.Stats))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('oper_id', YLeaf(YType.uint32, 'oper-id')),
                ('oper_type', YLeaf(YType.enumeration, 'oper-type')),
                ('latest_return_code', YLeaf(YType.enumeration, 'latest-return-code')),
                ('success_count', YLeaf(YType.uint32, 'success-count')),
                ('failure_count', YLeaf(YType.uint32, 'failure-count')),
                ('latest_oper_start_time', YLeaf(YType.str, 'latest-oper-start-time')),
            ])
            self.oper_id = None
            self.oper_type = None
            self.latest_return_code = None
            self.success_count = None
            self.failure_count = None
            self.latest_oper_start_time = None

            self.rtt_info = IpSlaStats.SlaOperEntry.RttInfo()
            self.rtt_info.parent = self
            self._children_name_map["rtt_info"] = "rtt-info"
            self._children_yang_names.add("rtt-info")

            self.measure_stats = IpSlaStats.SlaOperEntry.MeasureStats()
            self.measure_stats.parent = self
            self._children_name_map["measure_stats"] = "measure-stats"
            self._children_yang_names.add("measure-stats")

            self.stats = IpSlaStats.SlaOperEntry.Stats()
            self.stats.parent = self
            self._children_name_map["stats"] = "stats"
            self._children_yang_names.add("stats")
            self._segment_path = lambda: "sla-oper-entry" + "[oper-id='" + str(self.oper_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-ip-sla-oper:ip-sla-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IpSlaStats.SlaOperEntry, ['oper_id', 'oper_type', 'latest_return_code', 'success_count', 'failure_count', 'latest_oper_start_time'], name, value)


        class RttInfo(Entity):
            """
            RTT information
            
            .. attribute:: latest_rtt
            
            	The last Round Trip Time recorded for this SLA
            	**type**\:  :py:class:`LatestRtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.LatestRtt>`
            
            .. attribute:: time_to_live
            
            	Time\-to\-live for the SLA operation
            	**type**\:  :py:class:`TimeToLive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.TimeToLive>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.RttInfo, self).__init__()

                self.yang_name = "rtt-info"
                self.yang_parent_name = "sla-oper-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("latest-rtt", ("latest_rtt", IpSlaStats.SlaOperEntry.RttInfo.LatestRtt)), ("time-to-live", ("time_to_live", IpSlaStats.SlaOperEntry.RttInfo.TimeToLive))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.latest_rtt = IpSlaStats.SlaOperEntry.RttInfo.LatestRtt()
                self.latest_rtt.parent = self
                self._children_name_map["latest_rtt"] = "latest-rtt"
                self._children_yang_names.add("latest-rtt")

                self.time_to_live = IpSlaStats.SlaOperEntry.RttInfo.TimeToLive()
                self.time_to_live.parent = self
                self._children_name_map["time_to_live"] = "time-to-live"
                self._children_yang_names.add("time-to-live")
                self._segment_path = lambda: "rtt-info"


            class LatestRtt(Entity):
                """
                The last Round Trip Time recorded for this SLA
                
                .. attribute:: rtt
                
                	Round trip time value
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: unknown
                
                	Round trip time is unknown
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: could_not_find
                
                	Round trip time could not be determined
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.RttInfo.LatestRtt, self).__init__()

                    self.yang_name = "latest-rtt"
                    self.yang_parent_name = "rtt-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rtt', YLeaf(YType.uint64, 'rtt')),
                        ('unknown', YLeaf(YType.empty, 'unknown')),
                        ('could_not_find', YLeaf(YType.empty, 'could-not-find')),
                    ])
                    self.rtt = None
                    self.unknown = None
                    self.could_not_find = None
                    self._segment_path = lambda: "latest-rtt"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.RttInfo.LatestRtt, ['rtt', 'unknown', 'could_not_find'], name, value)


            class TimeToLive(Entity):
                """
                Time\-to\-live for the SLA operation
                
                .. attribute:: ttl
                
                	Time to live value
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forever
                
                	Time to live unbound
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.RttInfo.TimeToLive, self).__init__()

                    self.yang_name = "time-to-live"
                    self.yang_parent_name = "rtt-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ttl', YLeaf(YType.uint64, 'ttl')),
                        ('forever', YLeaf(YType.empty, 'forever')),
                    ])
                    self.ttl = None
                    self.forever = None
                    self._segment_path = lambda: "time-to-live"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.RttInfo.TimeToLive, ['ttl', 'forever'], name, value)


        class MeasureStats(Entity):
            """
            Measured statistics
            
            .. attribute:: intv_start_time
            
            	Interval start time
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: init_count
            
            	Initial count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: complete_count
            
            	Complete count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: valid
            
            	Validity
            	**type**\: bool
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.MeasureStats, self).__init__()

                self.yang_name = "measure-stats"
                self.yang_parent_name = "sla-oper-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('intv_start_time', YLeaf(YType.str, 'intv-start-time')),
                    ('init_count', YLeaf(YType.uint32, 'init-count')),
                    ('complete_count', YLeaf(YType.uint32, 'complete-count')),
                    ('valid', YLeaf(YType.boolean, 'valid')),
                ])
                self.intv_start_time = None
                self.init_count = None
                self.complete_count = None
                self.valid = None
                self._segment_path = lambda: "measure-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(IpSlaStats.SlaOperEntry.MeasureStats, ['intv_start_time', 'init_count', 'complete_count', 'valid'], name, value)


        class Stats(Entity):
            """
            Statistics
            
            .. attribute:: rtt
            
            	RTT value
            	**type**\:  :py:class:`Rtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt>`
            
            .. attribute:: oneway_latency
            
            	Latency information
            	**type**\:  :py:class:`OnewayLatency <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency>`
            
            .. attribute:: jitter
            
            	Jitter information
            	**type**\:  :py:class:`Jitter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter>`
            
            .. attribute:: over_threshold
            
            	Over threshold information
            	**type**\:  :py:class:`OverThreshold <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OverThreshold>`
            
            .. attribute:: packet_loss
            
            	Packet loss information
            	**type**\:  :py:class:`PacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss>`
            
            .. attribute:: icmp_packet_loss
            
            	ICMP packet loss information
            	**type**\:  :py:class:`IcmpPacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss>`
            
            .. attribute:: voice_score
            
            	Voice score information
            	**type**\:  :py:class:`VoiceScore <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.VoiceScore>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.Stats, self).__init__()

                self.yang_name = "stats"
                self.yang_parent_name = "sla-oper-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("rtt", ("rtt", IpSlaStats.SlaOperEntry.Stats.Rtt)), ("oneway-latency", ("oneway_latency", IpSlaStats.SlaOperEntry.Stats.OnewayLatency)), ("jitter", ("jitter", IpSlaStats.SlaOperEntry.Stats.Jitter)), ("over-threshold", ("over_threshold", IpSlaStats.SlaOperEntry.Stats.OverThreshold)), ("packet-loss", ("packet_loss", IpSlaStats.SlaOperEntry.Stats.PacketLoss)), ("icmp-packet-loss", ("icmp_packet_loss", IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss)), ("voice-score", ("voice_score", IpSlaStats.SlaOperEntry.Stats.VoiceScore))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.rtt = IpSlaStats.SlaOperEntry.Stats.Rtt()
                self.rtt.parent = self
                self._children_name_map["rtt"] = "rtt"
                self._children_yang_names.add("rtt")

                self.oneway_latency = IpSlaStats.SlaOperEntry.Stats.OnewayLatency()
                self.oneway_latency.parent = self
                self._children_name_map["oneway_latency"] = "oneway-latency"
                self._children_yang_names.add("oneway-latency")

                self.jitter = IpSlaStats.SlaOperEntry.Stats.Jitter()
                self.jitter.parent = self
                self._children_name_map["jitter"] = "jitter"
                self._children_yang_names.add("jitter")

                self.over_threshold = IpSlaStats.SlaOperEntry.Stats.OverThreshold()
                self.over_threshold.parent = self
                self._children_name_map["over_threshold"] = "over-threshold"
                self._children_yang_names.add("over-threshold")

                self.packet_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss()
                self.packet_loss.parent = self
                self._children_name_map["packet_loss"] = "packet-loss"
                self._children_yang_names.add("packet-loss")

                self.icmp_packet_loss = IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss()
                self.icmp_packet_loss.parent = self
                self._children_name_map["icmp_packet_loss"] = "icmp-packet-loss"
                self._children_yang_names.add("icmp-packet-loss")

                self.voice_score = IpSlaStats.SlaOperEntry.Stats.VoiceScore()
                self.voice_score.parent = self
                self._children_name_map["voice_score"] = "voice-score"
                self._children_yang_names.add("voice-score")
                self._segment_path = lambda: "stats"


            class Rtt(Entity):
                """
                RTT value
                
                .. attribute:: rtt_count
                
                	RTT count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sla_time_values
                
                	Timing information
                	**type**\:  :py:class:`SlaTimeValues <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.Rtt, self).__init__()

                    self.yang_name = "rtt"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sla-time-values", ("sla_time_values", IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rtt_count', YLeaf(YType.uint32, 'rtt-count')),
                    ])
                    self.rtt_count = None

                    self.sla_time_values = IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues()
                    self.sla_time_values.parent = self
                    self._children_name_map["sla_time_values"] = "sla-time-values"
                    self._children_yang_names.add("sla-time-values")
                    self._segment_path = lambda: "rtt"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.Rtt, ['rtt_count'], name, value)


                class SlaTimeValues(Entity):
                    """
                    Timing information
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:  :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues, self).__init__()

                        self.yang_name = "sla-time-values"
                        self.yang_parent_name = "rtt"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('min', YLeaf(YType.uint32, 'min')),
                            ('avg', YLeaf(YType.uint32, 'avg')),
                            ('max', YLeaf(YType.uint32, 'max')),
                            ('accuracy', YLeaf(YType.enumeration, 'accuracy')),
                        ])
                        self.min = None
                        self.avg = None
                        self.max = None
                        self.accuracy = None
                        self._segment_path = lambda: "sla-time-values"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues, ['min', 'avg', 'max', 'accuracy'], name, value)


            class OnewayLatency(Entity):
                """
                Latency information
                
                .. attribute:: sample_count
                
                	Sample count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	Source to Destination for the one\-way latency
                	**type**\:  :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd>`
                
                .. attribute:: ds
                
                	Destination to Source for the one\-way latency
                	**type**\:  :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency, self).__init__()

                    self.yang_name = "oneway-latency"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sd", ("sd", IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd)), ("ds", ("ds", IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sample_count', YLeaf(YType.uint32, 'sample-count')),
                    ])
                    self.sample_count = None

                    self.sd = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd()
                    self.sd.parent = self
                    self._children_name_map["sd"] = "sd"
                    self._children_yang_names.add("sd")

                    self.ds = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds()
                    self.ds.parent = self
                    self._children_name_map["ds"] = "ds"
                    self._children_yang_names.add("ds")
                    self._segment_path = lambda: "oneway-latency"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.OnewayLatency, ['sample_count'], name, value)


                class Sd(Entity):
                    """
                    Source to Destination for the one\-way latency
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:  :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd, self).__init__()

                        self.yang_name = "sd"
                        self.yang_parent_name = "oneway-latency"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('min', YLeaf(YType.uint32, 'min')),
                            ('avg', YLeaf(YType.uint32, 'avg')),
                            ('max', YLeaf(YType.uint32, 'max')),
                            ('accuracy', YLeaf(YType.enumeration, 'accuracy')),
                        ])
                        self.min = None
                        self.avg = None
                        self.max = None
                        self.accuracy = None
                        self._segment_path = lambda: "sd"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd, ['min', 'avg', 'max', 'accuracy'], name, value)


                class Ds(Entity):
                    """
                    Destination to Source for the one\-way latency
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:  :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds, self).__init__()

                        self.yang_name = "ds"
                        self.yang_parent_name = "oneway-latency"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('min', YLeaf(YType.uint32, 'min')),
                            ('avg', YLeaf(YType.uint32, 'avg')),
                            ('max', YLeaf(YType.uint32, 'max')),
                            ('accuracy', YLeaf(YType.enumeration, 'accuracy')),
                        ])
                        self.min = None
                        self.avg = None
                        self.max = None
                        self.accuracy = None
                        self._segment_path = lambda: "ds"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds, ['min', 'avg', 'max', 'accuracy'], name, value)


            class Jitter(Entity):
                """
                Jitter information
                
                .. attribute:: sd_sample_count
                
                	Sample count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_sample_count
                
                	Sample count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	Source to Destination for the jitter
                	**type**\:  :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Sd>`
                
                .. attribute:: ds
                
                	Destination to Source for the jitter
                	**type**\:  :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Ds>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.Jitter, self).__init__()

                    self.yang_name = "jitter"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sd", ("sd", IpSlaStats.SlaOperEntry.Stats.Jitter.Sd)), ("ds", ("ds", IpSlaStats.SlaOperEntry.Stats.Jitter.Ds))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sd_sample_count', YLeaf(YType.uint32, 'sd-sample-count')),
                        ('ds_sample_count', YLeaf(YType.uint32, 'ds-sample-count')),
                    ])
                    self.sd_sample_count = None
                    self.ds_sample_count = None

                    self.sd = IpSlaStats.SlaOperEntry.Stats.Jitter.Sd()
                    self.sd.parent = self
                    self._children_name_map["sd"] = "sd"
                    self._children_yang_names.add("sd")

                    self.ds = IpSlaStats.SlaOperEntry.Stats.Jitter.Ds()
                    self.ds.parent = self
                    self._children_name_map["ds"] = "ds"
                    self._children_yang_names.add("ds")
                    self._segment_path = lambda: "jitter"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.Jitter, ['sd_sample_count', 'ds_sample_count'], name, value)


                class Sd(Entity):
                    """
                    Source to Destination for the jitter
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:  :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Jitter.Sd, self).__init__()

                        self.yang_name = "sd"
                        self.yang_parent_name = "jitter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('min', YLeaf(YType.uint32, 'min')),
                            ('avg', YLeaf(YType.uint32, 'avg')),
                            ('max', YLeaf(YType.uint32, 'max')),
                            ('accuracy', YLeaf(YType.enumeration, 'accuracy')),
                        ])
                        self.min = None
                        self.avg = None
                        self.max = None
                        self.accuracy = None
                        self._segment_path = lambda: "sd"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.Jitter.Sd, ['min', 'avg', 'max', 'accuracy'], name, value)


                class Ds(Entity):
                    """
                    Destination to Source for the jitter
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:  :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Jitter.Ds, self).__init__()

                        self.yang_name = "ds"
                        self.yang_parent_name = "jitter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('min', YLeaf(YType.uint32, 'min')),
                            ('avg', YLeaf(YType.uint32, 'avg')),
                            ('max', YLeaf(YType.uint32, 'max')),
                            ('accuracy', YLeaf(YType.enumeration, 'accuracy')),
                        ])
                        self.min = None
                        self.avg = None
                        self.max = None
                        self.accuracy = None
                        self._segment_path = lambda: "ds"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.Jitter.Ds, ['min', 'avg', 'max', 'accuracy'], name, value)


            class OverThreshold(Entity):
                """
                Over threshold information
                
                .. attribute:: rtt_count
                
                	Round Trip Time (RTT) over threshold count (the number of times that the RTT was over the configured threshold)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: percent
                
                	Round Trip Time over threshold percentage (the percentage that the RTT was over the configured threshold)
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.OverThreshold, self).__init__()

                    self.yang_name = "over-threshold"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rtt_count', YLeaf(YType.uint32, 'rtt-count')),
                        ('percent', YLeaf(YType.uint8, 'percent')),
                    ])
                    self.rtt_count = None
                    self.percent = None
                    self._segment_path = lambda: "over-threshold"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.OverThreshold, ['rtt_count', 'percent'], name, value)


            class PacketLoss(Entity):
                """
                Packet loss information
                
                .. attribute:: unprocessed_packets
                
                	Unprocessed packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_count
                
                	Number of packets lost from Source to Destination
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_loss
                
                	Source to Destination packet loss details
                	**type**\:  :py:class:`SdLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss>`
                
                .. attribute:: ds_count
                
                	Number of packets lost from Destination to Source
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_loss
                
                	Destination to Source packet loss details
                	**type**\:  :py:class:`DsLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss>`
                
                .. attribute:: out_of_sequence
                
                	Out of sequence packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: drops
                
                	Dropped packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: late_arrivals
                
                	Late arrival packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: skipped_packets
                
                	Skipped packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.PacketLoss, self).__init__()

                    self.yang_name = "packet-loss"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sd-loss", ("sd_loss", IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss)), ("ds-loss", ("ds_loss", IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('unprocessed_packets', YLeaf(YType.uint32, 'unprocessed-packets')),
                        ('sd_count', YLeaf(YType.uint32, 'sd-count')),
                        ('ds_count', YLeaf(YType.uint32, 'ds-count')),
                        ('out_of_sequence', YLeaf(YType.uint32, 'out-of-sequence')),
                        ('drops', YLeaf(YType.uint32, 'drops')),
                        ('late_arrivals', YLeaf(YType.uint32, 'late-arrivals')),
                        ('skipped_packets', YLeaf(YType.uint32, 'skipped-packets')),
                    ])
                    self.unprocessed_packets = None
                    self.sd_count = None
                    self.ds_count = None
                    self.out_of_sequence = None
                    self.drops = None
                    self.late_arrivals = None
                    self.skipped_packets = None

                    self.sd_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss()
                    self.sd_loss.parent = self
                    self._children_name_map["sd_loss"] = "sd-loss"
                    self._children_yang_names.add("sd-loss")

                    self.ds_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss()
                    self.ds_loss.parent = self
                    self._children_name_map["ds_loss"] = "ds-loss"
                    self._children_yang_names.add("ds-loss")
                    self._segment_path = lambda: "packet-loss"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.PacketLoss, ['unprocessed_packets', 'sd_count', 'ds_count', 'out_of_sequence', 'drops', 'late_arrivals', 'skipped_packets'], name, value)


                class SdLoss(Entity):
                    """
                    Source to Destination packet loss details
                    
                    .. attribute:: loss_period_count
                    
                    	Loss period count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	Shortest loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	Longest loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	Shortest inter loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	Longest inter loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss, self).__init__()

                        self.yang_name = "sd-loss"
                        self.yang_parent_name = "packet-loss"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('loss_period_count', YLeaf(YType.uint32, 'loss-period-count')),
                            ('loss_period_len_min', YLeaf(YType.uint32, 'loss-period-len-min')),
                            ('loss_period_len_max', YLeaf(YType.uint32, 'loss-period-len-max')),
                            ('inter_loss_period_len_min', YLeaf(YType.uint32, 'inter-loss-period-len-min')),
                            ('inter_loss_period_len_max', YLeaf(YType.uint32, 'inter-loss-period-len-max')),
                        ])
                        self.loss_period_count = None
                        self.loss_period_len_min = None
                        self.loss_period_len_max = None
                        self.inter_loss_period_len_min = None
                        self.inter_loss_period_len_max = None
                        self._segment_path = lambda: "sd-loss"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss, ['loss_period_count', 'loss_period_len_min', 'loss_period_len_max', 'inter_loss_period_len_min', 'inter_loss_period_len_max'], name, value)


                class DsLoss(Entity):
                    """
                    Destination to Source packet loss details
                    
                    .. attribute:: loss_period_count
                    
                    	Loss period count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	Shortest loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	Longest loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	Shortest inter loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	Longest inter loss period length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss, self).__init__()

                        self.yang_name = "ds-loss"
                        self.yang_parent_name = "packet-loss"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('loss_period_count', YLeaf(YType.uint32, 'loss-period-count')),
                            ('loss_period_len_min', YLeaf(YType.uint32, 'loss-period-len-min')),
                            ('loss_period_len_max', YLeaf(YType.uint32, 'loss-period-len-max')),
                            ('inter_loss_period_len_min', YLeaf(YType.uint32, 'inter-loss-period-len-min')),
                            ('inter_loss_period_len_max', YLeaf(YType.uint32, 'inter-loss-period-len-max')),
                        ])
                        self.loss_period_count = None
                        self.loss_period_len_min = None
                        self.loss_period_len_max = None
                        self.inter_loss_period_len_min = None
                        self.inter_loss_period_len_max = None
                        self._segment_path = lambda: "ds-loss"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss, ['loss_period_count', 'loss_period_len_min', 'loss_period_len_max', 'inter_loss_period_len_min', 'inter_loss_period_len_max'], name, value)


            class IcmpPacketLoss(Entity):
                """
                ICMP packet loss information
                
                .. attribute:: late_arrivals
                
                	Late arrival packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence
                
                	Out of sequence packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_sd
                
                	Out of sequence packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_ds
                
                	Out of sequence packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_both
                
                	Out of sequence packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: skipped_packets
                
                	Skipped packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unprocessed_packets
                
                	Unprocessed packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_loss
                
                	Lost packet count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_count
                
                	Loss period count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_min
                
                	Shortest loss period length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_max
                
                	Longest loss period length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: inter_loss_period_len_min
                
                	Shortest inter loss period length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: inter_loss_period_len_max
                
                	Longest inter loss period length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss, self).__init__()

                    self.yang_name = "icmp-packet-loss"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('late_arrivals', YLeaf(YType.uint32, 'late-arrivals')),
                        ('out_of_sequence', YLeaf(YType.uint32, 'out-of-sequence')),
                        ('out_of_sequence_sd', YLeaf(YType.uint32, 'out-of-sequence-sd')),
                        ('out_of_sequence_ds', YLeaf(YType.uint32, 'out-of-sequence-ds')),
                        ('out_of_sequence_both', YLeaf(YType.uint32, 'out-of-sequence-both')),
                        ('skipped_packets', YLeaf(YType.uint32, 'skipped-packets')),
                        ('unprocessed_packets', YLeaf(YType.uint32, 'unprocessed-packets')),
                        ('packet_loss', YLeaf(YType.uint32, 'packet-loss')),
                        ('loss_period_count', YLeaf(YType.uint32, 'loss-period-count')),
                        ('loss_period_len_min', YLeaf(YType.uint32, 'loss-period-len-min')),
                        ('loss_period_len_max', YLeaf(YType.uint32, 'loss-period-len-max')),
                        ('inter_loss_period_len_min', YLeaf(YType.uint32, 'inter-loss-period-len-min')),
                        ('inter_loss_period_len_max', YLeaf(YType.uint32, 'inter-loss-period-len-max')),
                    ])
                    self.late_arrivals = None
                    self.out_of_sequence = None
                    self.out_of_sequence_sd = None
                    self.out_of_sequence_ds = None
                    self.out_of_sequence_both = None
                    self.skipped_packets = None
                    self.unprocessed_packets = None
                    self.packet_loss = None
                    self.loss_period_count = None
                    self.loss_period_len_min = None
                    self.loss_period_len_max = None
                    self.inter_loss_period_len_min = None
                    self.inter_loss_period_len_max = None
                    self._segment_path = lambda: "icmp-packet-loss"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss, ['late_arrivals', 'out_of_sequence', 'out_of_sequence_sd', 'out_of_sequence_ds', 'out_of_sequence_both', 'skipped_packets', 'unprocessed_packets', 'packet_loss', 'loss_period_count', 'loss_period_len_min', 'loss_period_len_max', 'inter_loss_period_len_min', 'inter_loss_period_len_max'], name, value)


            class VoiceScore(Entity):
                """
                Voice score information
                
                .. attribute:: icpif
                
                	Calculated planning impairment factor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mos
                
                	Mean opinion score
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.VoiceScore, self).__init__()

                    self.yang_name = "voice-score"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('icpif', YLeaf(YType.uint32, 'icpif')),
                        ('mos', YLeaf(YType.uint32, 'mos')),
                    ])
                    self.icpif = None
                    self.mos = None
                    self._segment_path = lambda: "voice-score"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSlaStats.SlaOperEntry.Stats.VoiceScore, ['icpif', 'mos'], name, value)

    def clone_ptr(self):
        self._top_entity = IpSlaStats()
        return self._top_entity

