""" Cisco_IOS_XE_ip_sla_oper 

This module contains a collection of YANG definitions for
monitoring IP SLA statistics of a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AccuracyTypeEnum(Enum):
    """
    AccuracyTypeEnum

    .. data:: milliseconds = 0

    .. data:: microseconds = 1

    """

    milliseconds = 0

    microseconds = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['AccuracyTypeEnum']


class RttTypeEnum(Enum):
    """
    RttTypeEnum

    .. data:: rtt_known = 0

    .. data:: rtt_unknown = 1

    .. data:: rtt_could_not_find = 2

    """

    rtt_known = 0

    rtt_unknown = 1

    rtt_could_not_find = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['RttTypeEnum']


class SlaOperTypeEnum(Enum):
    """
    SlaOperTypeEnum

    .. data:: unknown = 0

    .. data:: udp_echo = 1

    .. data:: udp_jitter = 2

    .. data:: icmp_jitter = 3

    .. data:: ethernet_jitter = 4

    .. data:: ethernet_echo = 5

    .. data:: y1731_delay = 6

    .. data:: y1731_loss = 7

    .. data:: video = 8

    .. data:: mcast = 9

    .. data:: pong = 10

    .. data:: path_jitter = 11

    """

    unknown = 0

    udp_echo = 1

    udp_jitter = 2

    icmp_jitter = 3

    ethernet_jitter = 4

    ethernet_echo = 5

    y1731_delay = 6

    y1731_loss = 7

    video = 8

    mcast = 9

    pong = 10

    path_jitter = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['SlaOperTypeEnum']


class SlaReturnCodeEnum(Enum):
    """
    SlaReturnCodeEnum

    .. data:: unknown = 0

    .. data:: ok = 1

    .. data:: disconnected = 2

    .. data:: busy = 3

    .. data:: timeout = 4

    .. data:: no_connection = 5

    .. data:: internal_error = 6

    .. data:: operation_failure = 7

    .. data:: could_not_find = 8

    """

    unknown = 0

    ok = 1

    disconnected = 2

    busy = 3

    timeout = 4

    no_connection = 5

    internal_error = 6

    operation_failure = 7

    could_not_find = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['SlaReturnCodeEnum']


class TtlTypeEnum(Enum):
    """
    TtlTypeEnum

    .. data:: ttl_finite = 0

    .. data:: ttl_forever = 1

    """

    ttl_finite = 0

    ttl_forever = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['TtlTypeEnum']



class IpSlaStats(object):
    """
    Data nodes for All IP SLA Statistics.
    
    .. attribute:: sla_oper_entry
    
    	The list of IP SLA operations with statistics info
    	**type**\: list of    :py:class:`SlaOperEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry>`
    
    

    """

    _prefix = 'ip-sla-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.sla_oper_entry = YList()
        self.sla_oper_entry.parent = self
        self.sla_oper_entry.name = 'sla_oper_entry'


    class SlaOperEntry(object):
        """
        The list of IP SLA operations with statistics info.
        
        .. attribute:: oper_id  <key>
        
        	The name of the memory pool
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: failure_count
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: latest_oper_start_time
        
        	The time\-stamp for the latest SLA operation
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: latest_return_code
        
        	
        	**type**\:   :py:class:`SlaReturnCodeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaReturnCodeEnum>`
        
        .. attribute:: measure_stats
        
        	
        	**type**\:   :py:class:`MeasureStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.MeasureStats>`
        
        .. attribute:: oper_type
        
        	
        	**type**\:   :py:class:`SlaOperTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaOperTypeEnum>`
        
        .. attribute:: rtt_info
        
        	
        	**type**\:   :py:class:`RttInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo>`
        
        .. attribute:: stats
        
        	
        	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats>`
        
        .. attribute:: success_count
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ip-sla-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.oper_id = None
            self.failure_count = None
            self.latest_oper_start_time = None
            self.latest_return_code = None
            self.measure_stats = IpSlaStats.SlaOperEntry.MeasureStats()
            self.measure_stats.parent = self
            self.oper_type = None
            self.rtt_info = IpSlaStats.SlaOperEntry.RttInfo()
            self.rtt_info.parent = self
            self.stats = IpSlaStats.SlaOperEntry.Stats()
            self.stats.parent = self
            self.success_count = None


        class RttInfo(object):
            """
            
            
            .. attribute:: latest_rtt
            
            	
            	**type**\:   :py:class:`LatestRtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.LatestRtt>`
            
            .. attribute:: time_to_live
            
            	
            	**type**\:   :py:class:`TimeToLive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.TimeToLive>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.latest_rtt = IpSlaStats.SlaOperEntry.RttInfo.LatestRtt()
                self.latest_rtt.parent = self
                self.time_to_live = IpSlaStats.SlaOperEntry.RttInfo.TimeToLive()
                self.time_to_live.parent = self


            class LatestRtt(object):
                """
                
                
                .. attribute:: could_not_find
                
                	One of no\-connection/busy/timeout
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rtt
                
                	
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: unknown
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.could_not_find = None
                    self.rtt = None
                    self.unknown = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:latest-rtt'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.could_not_find is not None:
                        return True

                    if self.rtt is not None:
                        return True

                    if self.unknown is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.RttInfo.LatestRtt']['meta_info']


            class TimeToLive(object):
                """
                
                
                .. attribute:: forever
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ttl
                
                	
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.forever = None
                    self.ttl = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:time-to-live'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.forever is not None:
                        return True

                    if self.ttl is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.RttInfo.TimeToLive']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:rtt-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.latest_rtt is not None and self.latest_rtt._has_data():
                    return True

                if self.time_to_live is not None and self.time_to_live._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                return meta._meta_table['IpSlaStats.SlaOperEntry.RttInfo']['meta_info']


        class MeasureStats(object):
            """
            
            
            .. attribute:: complete_count
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_count
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intv_start_time
            
            	
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: valid
            
            	
            	**type**\:  bool
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.complete_count = None
                self.init_count = None
                self.intv_start_time = None
                self.valid = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:measure-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.complete_count is not None:
                    return True

                if self.init_count is not None:
                    return True

                if self.intv_start_time is not None:
                    return True

                if self.valid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                return meta._meta_table['IpSlaStats.SlaOperEntry.MeasureStats']['meta_info']


        class Stats(object):
            """
            
            
            .. attribute:: icmp_packet_loss
            
            	
            	**type**\:   :py:class:`IcmpPacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss>`
            
            .. attribute:: jitter
            
            	
            	**type**\:   :py:class:`Jitter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter>`
            
            .. attribute:: oneway_latency
            
            	
            	**type**\:   :py:class:`OnewayLatency <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency>`
            
            .. attribute:: over_threshold
            
            	
            	**type**\:   :py:class:`OverThreshold <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OverThreshold>`
            
            .. attribute:: packet_loss
            
            	
            	**type**\:   :py:class:`PacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss>`
            
            .. attribute:: rtt
            
            	
            	**type**\:   :py:class:`Rtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt>`
            
            .. attribute:: voice_score
            
            	
            	**type**\:   :py:class:`VoiceScore <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.VoiceScore>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.icmp_packet_loss = IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss()
                self.icmp_packet_loss.parent = self
                self.jitter = IpSlaStats.SlaOperEntry.Stats.Jitter()
                self.jitter.parent = self
                self.oneway_latency = IpSlaStats.SlaOperEntry.Stats.OnewayLatency()
                self.oneway_latency.parent = self
                self.over_threshold = IpSlaStats.SlaOperEntry.Stats.OverThreshold()
                self.over_threshold.parent = self
                self.packet_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss()
                self.packet_loss.parent = self
                self.rtt = IpSlaStats.SlaOperEntry.Stats.Rtt()
                self.rtt.parent = self
                self.voice_score = IpSlaStats.SlaOperEntry.Stats.VoiceScore()
                self.voice_score.parent = self


            class Rtt(object):
                """
                
                
                .. attribute:: rtt_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sla_time_values
                
                	
                	**type**\:   :py:class:`SlaTimeValues <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.rtt_count = None
                    self.sla_time_values = IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues()
                    self.sla_time_values.parent = self


                class SlaTimeValues(object):
                    """
                    
                    
                    .. attribute:: accuracy
                    
                    	
                    	**type**\:   :py:class:`AccuracyTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyTypeEnum>`
                    
                    .. attribute:: avg
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.accuracy = None
                        self.avg = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:sla-time-values'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accuracy is not None:
                            return True

                        if self.avg is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:rtt'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rtt_count is not None:
                        return True

                    if self.sla_time_values is not None and self.sla_time_values._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.Rtt']['meta_info']


            class OnewayLatency(object):
                """
                
                
                .. attribute:: ds
                
                	
                	**type**\:   :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds>`
                
                .. attribute:: sample_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	
                	**type**\:   :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.ds = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds()
                    self.ds.parent = self
                    self.sample_count = None
                    self.sd = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd()
                    self.sd.parent = self


                class Sd(object):
                    """
                    
                    
                    .. attribute:: accuracy
                    
                    	
                    	**type**\:   :py:class:`AccuracyTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyTypeEnum>`
                    
                    .. attribute:: avg
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.accuracy = None
                        self.avg = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:sd'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accuracy is not None:
                            return True

                        if self.avg is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd']['meta_info']


                class Ds(object):
                    """
                    
                    
                    .. attribute:: accuracy
                    
                    	
                    	**type**\:   :py:class:`AccuracyTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyTypeEnum>`
                    
                    .. attribute:: avg
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.accuracy = None
                        self.avg = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:ds'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accuracy is not None:
                            return True

                        if self.avg is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:oneway-latency'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ds is not None and self.ds._has_data():
                        return True

                    if self.sample_count is not None:
                        return True

                    if self.sd is not None and self.sd._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.OnewayLatency']['meta_info']


            class Jitter(object):
                """
                
                
                .. attribute:: ds
                
                	
                	**type**\:   :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Ds>`
                
                .. attribute:: ds_sample_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	
                	**type**\:   :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Sd>`
                
                .. attribute:: sd_sample_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.ds = IpSlaStats.SlaOperEntry.Stats.Jitter.Ds()
                    self.ds.parent = self
                    self.ds_sample_count = None
                    self.sd = IpSlaStats.SlaOperEntry.Stats.Jitter.Sd()
                    self.sd.parent = self
                    self.sd_sample_count = None


                class Sd(object):
                    """
                    
                    
                    .. attribute:: accuracy
                    
                    	
                    	**type**\:   :py:class:`AccuracyTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyTypeEnum>`
                    
                    .. attribute:: avg
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.accuracy = None
                        self.avg = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:sd'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accuracy is not None:
                            return True

                        if self.avg is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.Jitter.Sd']['meta_info']


                class Ds(object):
                    """
                    
                    
                    .. attribute:: accuracy
                    
                    	
                    	**type**\:   :py:class:`AccuracyTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyTypeEnum>`
                    
                    .. attribute:: avg
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.accuracy = None
                        self.avg = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:ds'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accuracy is not None:
                            return True

                        if self.avg is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.Jitter.Ds']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:jitter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ds is not None and self.ds._has_data():
                        return True

                    if self.ds_sample_count is not None:
                        return True

                    if self.sd is not None and self.sd._has_data():
                        return True

                    if self.sd_sample_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.Jitter']['meta_info']


            class OverThreshold(object):
                """
                
                
                .. attribute:: percent
                
                	
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: rtt_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.percent = None
                    self.rtt_count = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:over-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.percent is not None:
                        return True

                    if self.rtt_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.OverThreshold']['meta_info']


            class PacketLoss(object):
                """
                
                
                .. attribute:: drops
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_loss
                
                	
                	**type**\:   :py:class:`DsLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss>`
                
                .. attribute:: late_arrivals
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_loss
                
                	
                	**type**\:   :py:class:`SdLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss>`
                
                .. attribute:: skipped_packets
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unprocessed_packets
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.drops = None
                    self.ds_count = None
                    self.ds_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss()
                    self.ds_loss.parent = self
                    self.late_arrivals = None
                    self.out_of_sequence = None
                    self.sd_count = None
                    self.sd_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss()
                    self.sd_loss.parent = self
                    self.skipped_packets = None
                    self.unprocessed_packets = None


                class SdLoss(object):
                    """
                    
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_count
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.inter_loss_period_len_max = None
                        self.inter_loss_period_len_min = None
                        self.loss_period_count = None
                        self.loss_period_len_max = None
                        self.loss_period_len_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:sd-loss'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.inter_loss_period_len_max is not None:
                            return True

                        if self.inter_loss_period_len_min is not None:
                            return True

                        if self.loss_period_count is not None:
                            return True

                        if self.loss_period_len_max is not None:
                            return True

                        if self.loss_period_len_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss']['meta_info']


                class DsLoss(object):
                    """
                    
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_count
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.inter_loss_period_len_max = None
                        self.inter_loss_period_len_min = None
                        self.loss_period_count = None
                        self.loss_period_len_max = None
                        self.loss_period_len_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:ds-loss'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.inter_loss_period_len_max is not None:
                            return True

                        if self.inter_loss_period_len_min is not None:
                            return True

                        if self.loss_period_count is not None:
                            return True

                        if self.loss_period_len_max is not None:
                            return True

                        if self.loss_period_len_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                        return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:packet-loss'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.drops is not None:
                        return True

                    if self.ds_count is not None:
                        return True

                    if self.ds_loss is not None and self.ds_loss._has_data():
                        return True

                    if self.late_arrivals is not None:
                        return True

                    if self.out_of_sequence is not None:
                        return True

                    if self.sd_count is not None:
                        return True

                    if self.sd_loss is not None and self.sd_loss._has_data():
                        return True

                    if self.skipped_packets is not None:
                        return True

                    if self.unprocessed_packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.PacketLoss']['meta_info']


            class IcmpPacketLoss(object):
                """
                
                
                .. attribute:: ds_out_of_sequence_ds
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inter_loss_period_len_max
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inter_loss_period_len_min
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: late_arrivals
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_count
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_max
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_min
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_both
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_sd
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_loss
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: skipped_packets
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unprocessed_packets
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.ds_out_of_sequence_ds = None
                    self.inter_loss_period_len_max = None
                    self.inter_loss_period_len_min = None
                    self.late_arrivals = None
                    self.loss_period_count = None
                    self.loss_period_len_max = None
                    self.loss_period_len_min = None
                    self.out_of_sequence = None
                    self.out_of_sequence_both = None
                    self.out_of_sequence_sd = None
                    self.packet_loss = None
                    self.skipped_packets = None
                    self.unprocessed_packets = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:icmp-packet-loss'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ds_out_of_sequence_ds is not None:
                        return True

                    if self.inter_loss_period_len_max is not None:
                        return True

                    if self.inter_loss_period_len_min is not None:
                        return True

                    if self.late_arrivals is not None:
                        return True

                    if self.loss_period_count is not None:
                        return True

                    if self.loss_period_len_max is not None:
                        return True

                    if self.loss_period_len_min is not None:
                        return True

                    if self.out_of_sequence is not None:
                        return True

                    if self.out_of_sequence_both is not None:
                        return True

                    if self.out_of_sequence_sd is not None:
                        return True

                    if self.packet_loss is not None:
                        return True

                    if self.skipped_packets is not None:
                        return True

                    if self.unprocessed_packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss']['meta_info']


            class VoiceScore(object):
                """
                
                
                .. attribute:: icpif
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mos
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.icpif = None
                    self.mos = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:voice-score'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.icpif is not None:
                        return True

                    if self.mos is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                    return meta._meta_table['IpSlaStats.SlaOperEntry.Stats.VoiceScore']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-ip-sla-oper:stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.icmp_packet_loss is not None and self.icmp_packet_loss._has_data():
                    return True

                if self.jitter is not None and self.jitter._has_data():
                    return True

                if self.oneway_latency is not None and self.oneway_latency._has_data():
                    return True

                if self.over_threshold is not None and self.over_threshold._has_data():
                    return True

                if self.packet_loss is not None and self.packet_loss._has_data():
                    return True

                if self.rtt is not None and self.rtt._has_data():
                    return True

                if self.voice_score is not None and self.voice_score._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
                return meta._meta_table['IpSlaStats.SlaOperEntry.Stats']['meta_info']

        @property
        def _common_path(self):
            if self.oper_id is None:
                raise YPYModelError('Key property oper_id is None')

            return '/Cisco-IOS-XE-ip-sla-oper:ip-sla-stats/Cisco-IOS-XE-ip-sla-oper:sla-oper-entry[Cisco-IOS-XE-ip-sla-oper:oper-id = ' + str(self.oper_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.oper_id is not None:
                return True

            if self.failure_count is not None:
                return True

            if self.latest_oper_start_time is not None:
                return True

            if self.latest_return_code is not None:
                return True

            if self.measure_stats is not None and self.measure_stats._has_data():
                return True

            if self.oper_type is not None:
                return True

            if self.rtt_info is not None and self.rtt_info._has_data():
                return True

            if self.stats is not None and self.stats._has_data():
                return True

            if self.success_count is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
            return meta._meta_table['IpSlaStats.SlaOperEntry']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-ip-sla-oper:ip-sla-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.sla_oper_entry is not None:
            for child_ref in self.sla_oper_entry:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ip_sla_oper as meta
        return meta._meta_table['IpSlaStats']['meta_info']


