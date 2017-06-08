""" ietf_lspping 

MPLS LSP\-PING Yang Module

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OperationalStatusEnum(Enum):
    """
    OperationalStatusEnum

    Operational state of a LSP Ping test.

    .. data:: enabled = 1

    	The Test is active.

    .. data:: disabled = 2

    	The test has stopped.

    .. data:: completed = 3

    	The test is completed.

    """

    enabled = 1

    disabled = 2

    completed = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['OperationalStatusEnum']


class ReplyModeEnum(Enum):
    """
    ReplyModeEnum

    Reply mode.

    .. data:: do_not_reply = 1

    	Do not reply

    .. data:: reply_via_udp = 2

    	Reply via an IPv4/IPv6 UDP packet

    .. data:: reply_via_udp_router_alert = 3

    	Reply via an IPv4/IPv6 UDP packet with

    	Router Alert

    .. data:: reply_via_control_channel = 4

    	Reply via application level control

    	channel

    """

    do_not_reply = 1

    reply_via_udp = 2

    reply_via_udp_router_alert = 3

    reply_via_control_channel = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['ReplyModeEnum']


class ResultTypeEnum(Enum):
    """
    ResultTypeEnum

    Result of each LSP Ping test probe.

    .. data:: success = 1

    	The test probe is successed.

    .. data:: fail = 2

    	The test probe has failed.

    .. data:: timeout = 3

    	The test probe is timeout.

    """

    success = 1

    fail = 2

    timeout = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['ResultTypeEnum']


class TargetFecTypeEnum(Enum):
    """
    TargetFecTypeEnum

    Target FEC type.

    .. data:: ip_prefix = 0

    	IPv4/IPv6 prefix

    .. data:: bgp = 1

    	BGP IPv4/IPv6 prefix

    .. data:: rsvp = 2

    	Tunnel interface

    .. data:: vpn = 3

    	VPN IPv4/IPv6 prefix

    .. data:: pw = 4

    	FEC 128 pseudowire IPv4/IPv6

    .. data:: vpls = 5

    	FEC 129 pseudowire IPv4/IPv6

    """

    ip_prefix = 0

    bgp = 1

    rsvp = 2

    vpn = 3

    pw = 4

    vpls = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['TargetFecTypeEnum']


class UnitsEnum(Enum):
    """
    UnitsEnum

    Time units

    .. data:: seconds = 0

    	Seconds

    .. data:: milliseconds = 1

    	Milliseconds

    .. data:: microseconds = 2

    	Microseconds

    .. data:: nanoseconds = 3

    	Nanoseconds

    """

    seconds = 0

    milliseconds = 1

    microseconds = 2

    nanoseconds = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['UnitsEnum']



class LspPings(object):
    """
    Multi instance of LSP Ping test.
    
    .. attribute:: lsp_ping
    
    	LSP Ping test
    	**type**\: list of    :py:class:`LspPing <ydk.models.ietf.ietf_lspping.LspPings.LspPing>`
    
    

    """

    _prefix = 'lspping'
    _revision = '2016-03-18'

    def __init__(self):
        self.lsp_ping = YList()
        self.lsp_ping.parent = self
        self.lsp_ping.name = 'lsp_ping'


    class LspPing(object):
        """
        LSP Ping test
        
        .. attribute:: lsp_ping_name  <key>
        
        	LSP Ping test name
        	**type**\:  str
        
        	**length:** 1..31
        
        	**mandatory**\: True
        
        .. attribute:: control_info
        
        	Control information of the LSP Ping test
        	**type**\:   :py:class:`ControlInfo <ydk.models.ietf.ietf_lspping.LspPings.LspPing.ControlInfo>`
        
        .. attribute:: result_info
        
        	LSP Ping test result information
        	**type**\:   :py:class:`ResultInfo <ydk.models.ietf.ietf_lspping.LspPings.LspPing.ResultInfo>`
        
        .. attribute:: schedule_parameters
        
        	LSP Ping test schedule parameter
        	**type**\:   :py:class:`ScheduleParameters <ydk.models.ietf.ietf_lspping.LspPings.LspPing.ScheduleParameters>`
        
        

        """

        _prefix = 'lspping'
        _revision = '2016-03-18'

        def __init__(self):
            self.parent = None
            self.lsp_ping_name = None
            self.control_info = LspPings.LspPing.ControlInfo()
            self.control_info.parent = self
            self.result_info = LspPings.LspPing.ResultInfo()
            self.result_info.parent = self
            self.schedule_parameters = LspPings.LspPing.ScheduleParameters()
            self.schedule_parameters.parent = self


        class ControlInfo(object):
            """
            Control information of the LSP Ping test.
            
            .. attribute:: bgp
            
            	BGP IPv4/IPv6 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: data_fill
            
            	Used together with the corresponding data\-size value to determine how to fill the data portion of a probe packet
            	**type**\:  str
            
            	**length:** 0..1564
            
            .. attribute:: data_size
            
            	Specifies the size of the data portion to be transmitted in a LSP Ping operation, in octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: description
            
            	A descriptive name of the LSP Ping test
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: interface_name
            
            	Specifies the outgoing interface
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: interval
            
            	Specifies the interval to send a LSP Ping echo request packet(probe) as part of one LSP Ping test
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 1
            
            .. attribute:: interval_units
            
            	Interval units
            	**type**\:   :py:class:`UnitsEnum <ydk.models.ietf.ietf_lspping.UnitsEnum>`
            
            	**default value**\: seconds
            
            .. attribute:: ip_address
            
            	IPv4/IPv6 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: nexthop
            
            	Specifies the nexthop
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: probe_count
            
            	Specifies the number of probe sent of one LSP Ping test
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 5
            
            .. attribute:: reply_mode
            
            	Specifies the reply mode
            	**type**\:   :py:class:`ReplyModeEnum <ydk.models.ietf.ietf_lspping.ReplyModeEnum>`
            
            .. attribute:: source_address
            
            	Specifies the source address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: source_address_type
            
            	Specifies the type of the source address
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
            .. attribute:: target_fec_type
            
            	Specifies the address type of Target FEC
            	**type**\:   :py:class:`TargetFecTypeEnum <ydk.models.ietf.ietf_lspping.TargetFecTypeEnum>`
            
            .. attribute:: timeout
            
            	Specifies the time\-out value for a LSP Ping operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeout_units
            
            	Time\-out units
            	**type**\:   :py:class:`UnitsEnum <ydk.models.ietf.ietf_lspping.UnitsEnum>`
            
            .. attribute:: traffic_class
            
            	Specifies the Traffic Class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: ttl
            
            	Time to live
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 255
            
            .. attribute:: tunnel_interface
            
            	Tunnel interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vcid
            
            	VC ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vpn_ip_address
            
            	Layer3 VPN IPv4 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: vrf_name
            
            	Layer3 VPN Name
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vsi_name
            
            	VPLS VSI
            	**type**\:  str
            
            

            """

            _prefix = 'lspping'
            _revision = '2016-03-18'

            def __init__(self):
                self.parent = None
                self.bgp = None
                self.data_fill = None
                self.data_size = None
                self.description = None
                self.interface_name = None
                self.interval = None
                self.interval_units = None
                self.ip_address = None
                self.nexthop = None
                self.probe_count = None
                self.reply_mode = None
                self.source_address = None
                self.source_address_type = None
                self.target_fec_type = None
                self.timeout = None
                self.timeout_units = None
                self.traffic_class = None
                self.ttl = None
                self.tunnel_interface = None
                self.vcid = None
                self.vpn_ip_address = None
                self.vrf_name = None
                self.vsi_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-lspping:control-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bgp is not None:
                    return True

                if self.data_fill is not None:
                    return True

                if self.data_size is not None:
                    return True

                if self.description is not None:
                    return True

                if self.interface_name is not None:
                    return True

                if self.interval is not None:
                    return True

                if self.interval_units is not None:
                    return True

                if self.ip_address is not None:
                    return True

                if self.nexthop is not None:
                    return True

                if self.probe_count is not None:
                    return True

                if self.reply_mode is not None:
                    return True

                if self.source_address is not None:
                    return True

                if self.source_address_type is not None:
                    return True

                if self.target_fec_type is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.timeout_units is not None:
                    return True

                if self.traffic_class is not None:
                    return True

                if self.ttl is not None:
                    return True

                if self.tunnel_interface is not None:
                    return True

                if self.vcid is not None:
                    return True

                if self.vpn_ip_address is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vsi_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_lspping as meta
                return meta._meta_table['LspPings.LspPing.ControlInfo']['meta_info']


        class ScheduleParameters(object):
            """
            LSP Ping test schedule parameter
            
            .. attribute:: end_test_at
            
            	End test at a specific time
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: end_test_delay
            
            	End after a specific delay
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: end_test_delay_units
            
            	Delay units
            	**type**\:   :py:class:`UnitsEnum <ydk.models.ietf.ietf_lspping.UnitsEnum>`
            
            	**default value**\: seconds
            
            .. attribute:: end_test_lifetime
            
            	Set the test lifetime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lifetime_units
            
            	Lifetime units
            	**type**\:   :py:class:`UnitsEnum <ydk.models.ietf.ietf_lspping.UnitsEnum>`
            
            	**default value**\: seconds
            
            .. attribute:: start_test_at
            
            	Start test at a specific time
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: start_test_daily
            
            	Start test daily
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: start_test_delay
            
            	Start after a specific delay
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: start_test_delay_units
            
            	Delay units
            	**type**\:   :py:class:`UnitsEnum <ydk.models.ietf.ietf_lspping.UnitsEnum>`
            
            	**default value**\: seconds
            
            .. attribute:: start_test_now
            
            	Start test now
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'lspping'
            _revision = '2016-03-18'

            def __init__(self):
                self.parent = None
                self.end_test_at = None
                self.end_test_delay = None
                self.end_test_delay_units = None
                self.end_test_lifetime = None
                self.lifetime_units = None
                self.start_test_at = None
                self.start_test_daily = None
                self.start_test_delay = None
                self.start_test_delay_units = None
                self.start_test_now = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-lspping:schedule-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.end_test_at is not None:
                    return True

                if self.end_test_delay is not None:
                    return True

                if self.end_test_delay_units is not None:
                    return True

                if self.end_test_lifetime is not None:
                    return True

                if self.lifetime_units is not None:
                    return True

                if self.start_test_at is not None:
                    return True

                if self.start_test_daily is not None:
                    return True

                if self.start_test_delay is not None:
                    return True

                if self.start_test_delay_units is not None:
                    return True

                if self.start_test_now is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_lspping as meta
                return meta._meta_table['LspPings.LspPing.ScheduleParameters']['meta_info']


        class ResultInfo(object):
            """
            LSP Ping test result information.
            
            .. attribute:: average_rtt
            
            	The current average LSP Ping round\-trip\-time (RTT)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgp
            
            	BGP IPv4/IPv6 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: ip_address
            
            	IPv4/IPv6 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: last_good_probe
            
            	Date and time when the last response was received for a probe
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: max_rtt
            
            	The maximum LSP Ping round\-trip\-time (RTT) received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: min_rtt
            
            	The minimum LSP Ping round\-trip\-time (RTT) received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: operational_status
            
            	Operational state of a LSP Ping test
            	**type**\:   :py:class:`OperationalStatusEnum <ydk.models.ietf.ietf_lspping.OperationalStatusEnum>`
            
            .. attribute:: probe_responses
            
            	Number of responses received for the corresponding LSP Ping test
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: probe_results
            
            	Result info of test probes
            	**type**\:   :py:class:`ProbeResults <ydk.models.ietf.ietf_lspping.LspPings.LspPing.ResultInfo.ProbeResults>`
            
            .. attribute:: sent_probes
            
            	Number of probes sent for the corresponding LSP Ping test
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: source_address
            
            	The source address of the test
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: source_address_type
            
            	The source address type
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
            .. attribute:: sum_of_squares
            
            	The sum of the squares for all replys received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: target_fec_type
            
            	The Target FEC address type
            	**type**\:   :py:class:`TargetFecTypeEnum <ydk.models.ietf.ietf_lspping.TargetFecTypeEnum>`
            
            .. attribute:: tunnel_interface
            
            	Tunnel interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vcid
            
            	VC ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vpn_ip_address
            
            	Layer3 VPN IPv4 Prefix
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: vrf_name
            
            	Layer3 VPN Name
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vsi_name
            
            	VPLS VSI
            	**type**\:  str
            
            

            """

            _prefix = 'lspping'
            _revision = '2016-03-18'

            def __init__(self):
                self.parent = None
                self.average_rtt = None
                self.bgp = None
                self.ip_address = None
                self.last_good_probe = None
                self.max_rtt = None
                self.min_rtt = None
                self.operational_status = None
                self.probe_responses = None
                self.probe_results = LspPings.LspPing.ResultInfo.ProbeResults()
                self.probe_results.parent = self
                self.sent_probes = None
                self.source_address = None
                self.source_address_type = None
                self.sum_of_squares = None
                self.target_fec_type = None
                self.tunnel_interface = None
                self.vcid = None
                self.vpn_ip_address = None
                self.vrf_name = None
                self.vsi_name = None


            class ProbeResults(object):
                """
                Result info of test probes.
                
                .. attribute:: probe_result
                
                	Result info of each test probe
                	**type**\: list of    :py:class:`ProbeResult <ydk.models.ietf.ietf_lspping.LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult>`
                
                

                """

                _prefix = 'lspping'
                _revision = '2016-03-18'

                def __init__(self):
                    self.parent = None
                    self.probe_result = YList()
                    self.probe_result.parent = self
                    self.probe_result.name = 'probe_result'


                class ProbeResult(object):
                    """
                    Result info of each test probe.
                    
                    .. attribute:: probe_index  <key>
                    
                    	Probe index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: result_type
                    
                    	The probe result type
                    	**type**\:   :py:class:`ResultTypeEnum <ydk.models.ietf.ietf_lspping.ResultTypeEnum>`
                    
                    .. attribute:: return_code
                    
                    	The Return Code set in the echo reply
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: return_sub_code
                    
                    	The Return Sub\-code set in the echo reply
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rtt
                    
                    	The round\-trip\-time (RTT) received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'lspping'
                    _revision = '2016-03-18'

                    def __init__(self):
                        self.parent = None
                        self.probe_index = None
                        self.result_type = None
                        self.return_code = None
                        self.return_sub_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.probe_index is None:
                            raise YPYModelError('Key property probe_index is None')

                        return self.parent._common_path +'/ietf-lspping:probe-result[ietf-lspping:probe-index = ' + str(self.probe_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.probe_index is not None:
                            return True

                        if self.result_type is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.return_sub_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_lspping as meta
                        return meta._meta_table['LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-lspping:probe-results'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.probe_result is not None:
                        for child_ref in self.probe_result:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_lspping as meta
                    return meta._meta_table['LspPings.LspPing.ResultInfo.ProbeResults']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-lspping:result-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.average_rtt is not None:
                    return True

                if self.bgp is not None:
                    return True

                if self.ip_address is not None:
                    return True

                if self.last_good_probe is not None:
                    return True

                if self.max_rtt is not None:
                    return True

                if self.min_rtt is not None:
                    return True

                if self.operational_status is not None:
                    return True

                if self.probe_responses is not None:
                    return True

                if self.probe_results is not None and self.probe_results._has_data():
                    return True

                if self.sent_probes is not None:
                    return True

                if self.source_address is not None:
                    return True

                if self.source_address_type is not None:
                    return True

                if self.sum_of_squares is not None:
                    return True

                if self.target_fec_type is not None:
                    return True

                if self.tunnel_interface is not None:
                    return True

                if self.vcid is not None:
                    return True

                if self.vpn_ip_address is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vsi_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_lspping as meta
                return meta._meta_table['LspPings.LspPing.ResultInfo']['meta_info']

        @property
        def _common_path(self):
            if self.lsp_ping_name is None:
                raise YPYModelError('Key property lsp_ping_name is None')

            return '/ietf-lspping:lsp-pings/ietf-lspping:lsp-ping[ietf-lspping:lsp-ping-name = ' + str(self.lsp_ping_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.lsp_ping_name is not None:
                return True

            if self.control_info is not None and self.control_info._has_data():
                return True

            if self.result_info is not None and self.result_info._has_data():
                return True

            if self.schedule_parameters is not None and self.schedule_parameters._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_lspping as meta
            return meta._meta_table['LspPings.LspPing']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-lspping:lsp-pings'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.lsp_ping is not None:
            for child_ref in self.lsp_ping:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lspping as meta
        return meta._meta_table['LspPings']['meta_info']


