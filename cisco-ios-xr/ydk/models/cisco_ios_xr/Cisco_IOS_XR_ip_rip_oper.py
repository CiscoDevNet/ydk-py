""" Cisco_IOS_XR_ip_rip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package operational data.

This module contains definitions
for the following management objects\:
  rip\: RIP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class InterfaceStateEnum(Enum):
    """
    InterfaceStateEnum

    Interface state

    .. data:: interface_none = 0

    	Interface does not exist

    .. data:: interface_down = 1

    	Interface exists but IP is down

    .. data:: interface_up = 2

    	Interface exists and IP is up

    .. data:: interface_unknown = 3

    	Unknown state

    """

    interface_none = 0

    interface_down = 1

    interface_up = 2

    interface_unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
        return meta._meta_table['InterfaceStateEnum']


class RipRouteOriginEnum(Enum):
    """
    RipRouteOriginEnum

    Rip route origin

    .. data:: rip_rt_org_runover = 0

    	configured 'network'

    .. data:: rip_rt_org_redist = 1

    	redistributed

    .. data:: rip_rt_org_auto_summary = 2

    	auto summary

    .. data:: rip_rt_org_rip = 3

    	learned via RIP

    .. data:: rip_rt_org_intsummary = 4

    	interface summary-address

    .. data:: rip_rt_org_unused = 5

    	route stay in for triggered rip

    """

    rip_rt_org_runover = 0

    rip_rt_org_redist = 1

    rip_rt_org_auto_summary = 2

    rip_rt_org_rip = 3

    rip_rt_org_intsummary = 4

    rip_rt_org_unused = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
        return meta._meta_table['RipRouteOriginEnum']



class Rip(object):
    """
    RIP operational data
    
    .. attribute:: default_vrf
    
    	RIP operational data for Default VRF
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf>`
    
    .. attribute:: protocol
    
    	Protocol operational data
    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol>`
    
    .. attribute:: vrfs
    
    	VRF related operational data
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs>`
    
    

    """

    _prefix = 'ip-rip-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self.protocol = Rip.Protocol()
        self.protocol.parent = self
        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF related operational data
        
        .. attribute:: vrf
        
        	Operational data for a particular VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            Operational data for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
            	Name of the VRF
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Configuration>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Statistics>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.configuration = Rip.Vrfs.Vrf.Configuration()
                self.configuration.parent = self
                self.global_ = Rip.Vrfs.Vrf.Global_()
                self.global_.parent = self
                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self.routes = Rip.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self.statistics = Rip.Vrfs.Vrf.Statistics()
                self.statistics.parent = self


            class Routes(object):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.route = YList()
                    self.route.parent = self
                    self.route.name = 'route'


                class Route(object):
                    """
                    A route in the RIP database
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\:  bool
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\:  bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:   :py:class:`RipRouteOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOriginEnum>`
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route.Paths>`
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\:  bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.attributes = None
                        self.bgp_count = None
                        self.destination_address = None
                        self.distance = None
                        self.hold_down = None
                        self.path_origin = None
                        self.paths = YList()
                        self.paths.parent = self
                        self.paths.name = 'paths'
                        self.prefix = None
                        self.prefix_length = None
                        self.prefix_length_xr = None
                        self.route_summary = None
                        self.route_tag = None
                        self.route_type = None
                        self.version = None


                    class Paths(object):
                        """
                        The paths for this route
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\:  bool
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface = None
                            self.is_permanent = None
                            self.metric = None
                            self.next_hop_address = None
                            self.source_address = None
                            self.tag = None
                            self.uptime = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:paths'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                return True

                            if self.is_permanent is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.tag is not None:
                                return True

                            if self.uptime is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Routes.Route.Paths']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active is not None:
                            return True

                        if self.attributes is not None:
                            return True

                        if self.bgp_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.distance is not None:
                            return True

                        if self.hold_down is not None:
                            return True

                        if self.path_origin is not None:
                            return True

                        if self.paths is not None:
                            for child_ref in self.paths:
                                if child_ref._has_data():
                                    return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.prefix_length_xr is not None:
                            return True

                        if self.route_summary is not None:
                            return True

                        if self.route_tag is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Routes.Route']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:routes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.route is not None:
                        for child_ref in self.route:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Routes']['meta_info']


            class Configuration(object):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\:  bool
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\:  bool
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\:  bool
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\:  bool
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\:  bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.auto_summarize = None
                    self.default_metric = None
                    self.flash_threshold = None
                    self.flush_timer = None
                    self.hold_down_timer = None
                    self.input_q_length = None
                    self.invalid_timer = None
                    self.maximum_paths = None
                    self.multicast_address = None
                    self.next_update_time = None
                    self.nsf_life_time = None
                    self.nsf_status = None
                    self.oom_flags = None
                    self.rip_version = None
                    self.triggered_rip = None
                    self.update_timer = None
                    self.validation_indicator = None
                    self.vr_fised_socket = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.auto_summarize is not None:
                        return True

                    if self.default_metric is not None:
                        return True

                    if self.flash_threshold is not None:
                        return True

                    if self.flush_timer is not None:
                        return True

                    if self.hold_down_timer is not None:
                        return True

                    if self.input_q_length is not None:
                        return True

                    if self.invalid_timer is not None:
                        return True

                    if self.maximum_paths is not None:
                        return True

                    if self.multicast_address is not None:
                        return True

                    if self.next_update_time is not None:
                        return True

                    if self.nsf_life_time is not None:
                        return True

                    if self.nsf_status is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.rip_version is not None:
                        return True

                    if self.triggered_rip is not None:
                        return True

                    if self.update_timer is not None:
                        return True

                    if self.validation_indicator is not None:
                        return True

                    if self.vr_fised_socket is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Configuration']['meta_info']


            class Statistics(object):
                """
                RIP statistics information
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.discarded_packets = None
                    self.discarded_routes = None
                    self.path_count = None
                    self.path_malloc_failures = None
                    self.periodic_updates = None
                    self.query_responses = None
                    self.received_packets = None
                    self.rib_updates = None
                    self.route_count = None
                    self.route_malloc_failures = None
                    self.sent_message_failures = None
                    self.sent_messages = None
                    self.standby_packets_received = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.discarded_packets is not None:
                        return True

                    if self.discarded_routes is not None:
                        return True

                    if self.path_count is not None:
                        return True

                    if self.path_malloc_failures is not None:
                        return True

                    if self.periodic_updates is not None:
                        return True

                    if self.query_responses is not None:
                        return True

                    if self.received_packets is not None:
                        return True

                    if self.rib_updates is not None:
                        return True

                    if self.route_count is not None:
                        return True

                    if self.route_malloc_failures is not None:
                        return True

                    if self.sent_message_failures is not None:
                        return True

                    if self.sent_messages is not None:
                        return True

                    if self.standby_packets_received is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Statistics']['meta_info']


            class Interfaces(object):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\:  str
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\:  bool
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\:  bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\:  bool
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\:  bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\:  bool
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer>`
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\:  bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.accept_metric = None
                        self.auth_key_md5 = None
                        self.auth_key_send_id = None
                        self.auth_keychain = None
                        self.auth_mode = None
                        self.destination_address = None
                        self.if_handle = None
                        self.interface = None
                        self.is_passive_interface = None
                        self.join_status = None
                        self.lpts_state = None
                        self.metric_cost = None
                        self.multicast_address = None
                        self.neighbor_address = None
                        self.oom_flags = None
                        self.pkt_accepted_valid_auth = None
                        self.pkt_drop_invalid_auth = None
                        self.pkt_drop_no_auth = None
                        self.pkt_drop_wrong_kc = None
                        self.poison_horizon = None
                        self.prefix_length = None
                        self.receive_version = None
                        self.rip_enabled = None
                        self.rip_peer = YList()
                        self.rip_peer.parent = self
                        self.rip_peer.name = 'rip_peer'
                        self.rip_summary = YList()
                        self.rip_summary.parent = self
                        self.rip_summary.name = 'rip_summary'
                        self.send_auth_key_exists = None
                        self.send_version = None
                        self.split_horizon = None
                        self.state = None
                        self.total_pkt_recvd = None
                        self.triggered_rip = None


                    class RipSummary(object):
                        """
                        User defined summary addresses
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.metric = None
                            self.next_hop_address = None
                            self.prefix = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary']['meta_info']


                    class RipPeer(object):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.discarded_peer_packets = None
                            self.discarded_peer_routes = None
                            self.peer_address = None
                            self.peer_uptime = None
                            self.peer_version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-peer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.discarded_peer_packets is not None:
                                return True

                            if self.discarded_peer_routes is not None:
                                return True

                            if self.peer_address is not None:
                                return True

                            if self.peer_uptime is not None:
                                return True

                            if self.peer_version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:interface[Cisco-IOS-XR-ip-rip-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.accept_metric is not None:
                            return True

                        if self.auth_key_md5 is not None:
                            return True

                        if self.auth_key_send_id is not None:
                            return True

                        if self.auth_keychain is not None:
                            return True

                        if self.auth_mode is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.if_handle is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.is_passive_interface is not None:
                            return True

                        if self.join_status is not None:
                            return True

                        if self.lpts_state is not None:
                            return True

                        if self.metric_cost is not None:
                            return True

                        if self.multicast_address is not None:
                            return True

                        if self.neighbor_address is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.pkt_accepted_valid_auth is not None:
                            return True

                        if self.pkt_drop_invalid_auth is not None:
                            return True

                        if self.pkt_drop_no_auth is not None:
                            return True

                        if self.pkt_drop_wrong_kc is not None:
                            return True

                        if self.poison_horizon is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.receive_version is not None:
                            return True

                        if self.rip_enabled is not None:
                            return True

                        if self.rip_peer is not None:
                            for child_ref in self.rip_peer:
                                if child_ref._has_data():
                                    return True

                        if self.rip_summary is not None:
                            for child_ref in self.rip_summary:
                                if child_ref._has_data():
                                    return True

                        if self.send_auth_key_exists is not None:
                            return True

                        if self.send_version is not None:
                            return True

                        if self.split_horizon is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.total_pkt_recvd is not None:
                            return True

                        if self.triggered_rip is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info']


            class Global_(object):
                """
                Global Information 
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.InterfaceSummary>`
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.VrfSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_summary = YList()
                    self.interface_summary.parent = self
                    self.interface_summary.name = 'interface_summary'
                    self.vrf_summary = Rip.Vrfs.Vrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self


                class VrfSummary(object):
                    """
                    VRF summary data
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\:  bool
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.active_interface_count = None
                        self.flush_timer = None
                        self.hold_down_timer = None
                        self.interface_configured_count = None
                        self.invalid_timer = None
                        self.next_update_time = None
                        self.oom_flags = None
                        self.path_count = None
                        self.route_count = None
                        self.update_timer = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:vrf-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active is not None:
                            return True

                        if self.active_interface_count is not None:
                            return True

                        if self.flush_timer is not None:
                            return True

                        if self.hold_down_timer is not None:
                            return True

                        if self.interface_configured_count is not None:
                            return True

                        if self.invalid_timer is not None:
                            return True

                        if self.next_update_time is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.path_count is not None:
                            return True

                        if self.route_count is not None:
                            return True

                        if self.update_timer is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Global_.VrfSummary']['meta_info']


                class InterfaceSummary(object):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_address = None
                        self.enabled = None
                        self.interface_name = None
                        self.neighbor_count = None
                        self.oom_flags = None
                        self.prefix_length = None
                        self.receive_version = None
                        self.send_version = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:interface-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_address is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.neighbor_count is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.receive_version is not None:
                            return True

                        if self.send_version is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Global_.InterfaceSummary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_summary is not None:
                        for child_ref in self.interface_summary:
                            if child_ref._has_data():
                                return True

                    if self.vrf_summary is not None and self.vrf_summary._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Global_']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:vrfs/Cisco-IOS-XR-ip-rip-oper:vrf[Cisco-IOS-XR-ip-rip-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.configuration is not None and self.configuration._has_data():
                    return True

                if self.global_ is not None and self.global_._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.routes is not None and self.routes._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
            return meta._meta_table['Rip.Vrfs']['meta_info']


    class Protocol(object):
        """
        Protocol operational data
        
        .. attribute:: default_vrf
        
        	RIP operational data for Default VRF
        	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf>`
        
        .. attribute:: process
        
        	RIP global process 
        	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.default_vrf = Rip.Protocol.DefaultVrf()
            self.default_vrf.parent = self
            self.process = Rip.Protocol.Process()
            self.process.parent = self


        class Process(object):
            """
            RIP global process 
            
            .. attribute:: current_oom_state
            
            	Current OOM state
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: socket_descriptor
            
            	Socket descriptior
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: vrf_active_count
            
            	Number of active VRFs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_config_count
            
            	Number of VRFs configured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_summary
            
            	List of VRFs configured
            	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process.VrfSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.current_oom_state = None
                self.path_count = None
                self.route_count = None
                self.socket_descriptor = None
                self.vrf_active_count = None
                self.vrf_config_count = None
                self.vrf_summary = YList()
                self.vrf_summary.parent = self
                self.vrf_summary.name = 'vrf_summary'


            class VrfSummary(object):
                """
                List of VRFs configured
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\:  bool
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.active_interface_count = None
                    self.flush_timer = None
                    self.hold_down_timer = None
                    self.interface_configured_count = None
                    self.invalid_timer = None
                    self.next_update_time = None
                    self.oom_flags = None
                    self.path_count = None
                    self.route_count = None
                    self.update_timer = None
                    self.vrf_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:process/Cisco-IOS-XR-ip-rip-oper:vrf-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.active_interface_count is not None:
                        return True

                    if self.flush_timer is not None:
                        return True

                    if self.hold_down_timer is not None:
                        return True

                    if self.interface_configured_count is not None:
                        return True

                    if self.invalid_timer is not None:
                        return True

                    if self.next_update_time is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.path_count is not None:
                        return True

                    if self.route_count is not None:
                        return True

                    if self.update_timer is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.Process.VrfSummary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:process'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.current_oom_state is not None:
                    return True

                if self.path_count is not None:
                    return True

                if self.route_count is not None:
                    return True

                if self.socket_descriptor is not None:
                    return True

                if self.vrf_active_count is not None:
                    return True

                if self.vrf_config_count is not None:
                    return True

                if self.vrf_summary is not None:
                    for child_ref in self.vrf_summary:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.Protocol.Process']['meta_info']


        class DefaultVrf(object):
            """
            RIP operational data for Default VRF
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Configuration>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces>`
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Statistics>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.configuration = Rip.Protocol.DefaultVrf.Configuration()
                self.configuration.parent = self
                self.global_ = Rip.Protocol.DefaultVrf.Global_()
                self.global_.parent = self
                self.interfaces = Rip.Protocol.DefaultVrf.Interfaces()
                self.interfaces.parent = self
                self.routes = Rip.Protocol.DefaultVrf.Routes()
                self.routes.parent = self
                self.statistics = Rip.Protocol.DefaultVrf.Statistics()
                self.statistics.parent = self


            class Routes(object):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.route = YList()
                    self.route.parent = self
                    self.route.name = 'route'


                class Route(object):
                    """
                    A route in the RIP database
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\:  bool
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\:  bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:   :py:class:`RipRouteOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOriginEnum>`
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route.Paths>`
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\:  bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.attributes = None
                        self.bgp_count = None
                        self.destination_address = None
                        self.distance = None
                        self.hold_down = None
                        self.path_origin = None
                        self.paths = YList()
                        self.paths.parent = self
                        self.paths.name = 'paths'
                        self.prefix = None
                        self.prefix_length = None
                        self.prefix_length_xr = None
                        self.route_summary = None
                        self.route_tag = None
                        self.route_type = None
                        self.version = None


                    class Paths(object):
                        """
                        The paths for this route
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\:  bool
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface = None
                            self.is_permanent = None
                            self.metric = None
                            self.next_hop_address = None
                            self.source_address = None
                            self.tag = None
                            self.uptime = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes/Cisco-IOS-XR-ip-rip-oper:route/Cisco-IOS-XR-ip-rip-oper:paths'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                return True

                            if self.is_permanent is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.tag is not None:
                                return True

                            if self.uptime is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Protocol.DefaultVrf.Routes.Route.Paths']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes/Cisco-IOS-XR-ip-rip-oper:route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active is not None:
                            return True

                        if self.attributes is not None:
                            return True

                        if self.bgp_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.distance is not None:
                            return True

                        if self.hold_down is not None:
                            return True

                        if self.path_origin is not None:
                            return True

                        if self.paths is not None:
                            for child_ref in self.paths:
                                if child_ref._has_data():
                                    return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.prefix_length_xr is not None:
                            return True

                        if self.route_summary is not None:
                            return True

                        if self.route_tag is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Protocol.DefaultVrf.Routes.Route']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.route is not None:
                        for child_ref in self.route:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.DefaultVrf.Routes']['meta_info']


            class Configuration(object):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\:  bool
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\:  bool
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\:  bool
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\:  bool
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\:  bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.auto_summarize = None
                    self.default_metric = None
                    self.flash_threshold = None
                    self.flush_timer = None
                    self.hold_down_timer = None
                    self.input_q_length = None
                    self.invalid_timer = None
                    self.maximum_paths = None
                    self.multicast_address = None
                    self.next_update_time = None
                    self.nsf_life_time = None
                    self.nsf_status = None
                    self.oom_flags = None
                    self.rip_version = None
                    self.triggered_rip = None
                    self.update_timer = None
                    self.validation_indicator = None
                    self.vr_fised_socket = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.auto_summarize is not None:
                        return True

                    if self.default_metric is not None:
                        return True

                    if self.flash_threshold is not None:
                        return True

                    if self.flush_timer is not None:
                        return True

                    if self.hold_down_timer is not None:
                        return True

                    if self.input_q_length is not None:
                        return True

                    if self.invalid_timer is not None:
                        return True

                    if self.maximum_paths is not None:
                        return True

                    if self.multicast_address is not None:
                        return True

                    if self.next_update_time is not None:
                        return True

                    if self.nsf_life_time is not None:
                        return True

                    if self.nsf_status is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.rip_version is not None:
                        return True

                    if self.triggered_rip is not None:
                        return True

                    if self.update_timer is not None:
                        return True

                    if self.validation_indicator is not None:
                        return True

                    if self.vr_fised_socket is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.DefaultVrf.Configuration']['meta_info']


            class Statistics(object):
                """
                RIP statistics information
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.discarded_packets = None
                    self.discarded_routes = None
                    self.path_count = None
                    self.path_malloc_failures = None
                    self.periodic_updates = None
                    self.query_responses = None
                    self.received_packets = None
                    self.rib_updates = None
                    self.route_count = None
                    self.route_malloc_failures = None
                    self.sent_message_failures = None
                    self.sent_messages = None
                    self.standby_packets_received = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.discarded_packets is not None:
                        return True

                    if self.discarded_routes is not None:
                        return True

                    if self.path_count is not None:
                        return True

                    if self.path_malloc_failures is not None:
                        return True

                    if self.periodic_updates is not None:
                        return True

                    if self.query_responses is not None:
                        return True

                    if self.received_packets is not None:
                        return True

                    if self.rib_updates is not None:
                        return True

                    if self.route_count is not None:
                        return True

                    if self.route_malloc_failures is not None:
                        return True

                    if self.sent_message_failures is not None:
                        return True

                    if self.sent_messages is not None:
                        return True

                    if self.standby_packets_received is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.DefaultVrf.Statistics']['meta_info']


            class Interfaces(object):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\:  str
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\:  bool
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\:  bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\:  bool
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\:  bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\:  bool
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer>`
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\:  bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.accept_metric = None
                        self.auth_key_md5 = None
                        self.auth_key_send_id = None
                        self.auth_keychain = None
                        self.auth_mode = None
                        self.destination_address = None
                        self.if_handle = None
                        self.interface = None
                        self.is_passive_interface = None
                        self.join_status = None
                        self.lpts_state = None
                        self.metric_cost = None
                        self.multicast_address = None
                        self.neighbor_address = None
                        self.oom_flags = None
                        self.pkt_accepted_valid_auth = None
                        self.pkt_drop_invalid_auth = None
                        self.pkt_drop_no_auth = None
                        self.pkt_drop_wrong_kc = None
                        self.poison_horizon = None
                        self.prefix_length = None
                        self.receive_version = None
                        self.rip_enabled = None
                        self.rip_peer = YList()
                        self.rip_peer.parent = self
                        self.rip_peer.name = 'rip_peer'
                        self.rip_summary = YList()
                        self.rip_summary.parent = self
                        self.rip_summary.name = 'rip_summary'
                        self.send_auth_key_exists = None
                        self.send_version = None
                        self.split_horizon = None
                        self.state = None
                        self.total_pkt_recvd = None
                        self.triggered_rip = None


                    class RipSummary(object):
                        """
                        User defined summary addresses
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.metric = None
                            self.next_hop_address = None
                            self.prefix = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary']['meta_info']


                    class RipPeer(object):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.discarded_peer_packets = None
                            self.discarded_peer_routes = None
                            self.peer_address = None
                            self.peer_uptime = None
                            self.peer_version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-peer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.discarded_peer_packets is not None:
                                return True

                            if self.discarded_peer_routes is not None:
                                return True

                            if self.peer_address is not None:
                                return True

                            if self.peer_uptime is not None:
                                return True

                            if self.peer_version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                            return meta._meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:interfaces/Cisco-IOS-XR-ip-rip-oper:interface[Cisco-IOS-XR-ip-rip-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.accept_metric is not None:
                            return True

                        if self.auth_key_md5 is not None:
                            return True

                        if self.auth_key_send_id is not None:
                            return True

                        if self.auth_keychain is not None:
                            return True

                        if self.auth_mode is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.if_handle is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.is_passive_interface is not None:
                            return True

                        if self.join_status is not None:
                            return True

                        if self.lpts_state is not None:
                            return True

                        if self.metric_cost is not None:
                            return True

                        if self.multicast_address is not None:
                            return True

                        if self.neighbor_address is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.pkt_accepted_valid_auth is not None:
                            return True

                        if self.pkt_drop_invalid_auth is not None:
                            return True

                        if self.pkt_drop_no_auth is not None:
                            return True

                        if self.pkt_drop_wrong_kc is not None:
                            return True

                        if self.poison_horizon is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.receive_version is not None:
                            return True

                        if self.rip_enabled is not None:
                            return True

                        if self.rip_peer is not None:
                            for child_ref in self.rip_peer:
                                if child_ref._has_data():
                                    return True

                        if self.rip_summary is not None:
                            for child_ref in self.rip_summary:
                                if child_ref._has_data():
                                    return True

                        if self.send_auth_key_exists is not None:
                            return True

                        if self.send_version is not None:
                            return True

                        if self.split_horizon is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.total_pkt_recvd is not None:
                            return True

                        if self.triggered_rip is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.DefaultVrf.Interfaces']['meta_info']


            class Global_(object):
                """
                Global Information 
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.InterfaceSummary>`
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.VrfSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_summary = YList()
                    self.interface_summary.parent = self
                    self.interface_summary.name = 'interface_summary'
                    self.vrf_summary = Rip.Protocol.DefaultVrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self


                class VrfSummary(object):
                    """
                    VRF summary data
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\:  bool
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.active_interface_count = None
                        self.flush_timer = None
                        self.hold_down_timer = None
                        self.interface_configured_count = None
                        self.invalid_timer = None
                        self.next_update_time = None
                        self.oom_flags = None
                        self.path_count = None
                        self.route_count = None
                        self.update_timer = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global/Cisco-IOS-XR-ip-rip-oper:vrf-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active is not None:
                            return True

                        if self.active_interface_count is not None:
                            return True

                        if self.flush_timer is not None:
                            return True

                        if self.hold_down_timer is not None:
                            return True

                        if self.interface_configured_count is not None:
                            return True

                        if self.invalid_timer is not None:
                            return True

                        if self.next_update_time is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.path_count is not None:
                            return True

                        if self.route_count is not None:
                            return True

                        if self.update_timer is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Protocol.DefaultVrf.Global_.VrfSummary']['meta_info']


                class InterfaceSummary(object):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_address = None
                        self.enabled = None
                        self.interface_name = None
                        self.neighbor_count = None
                        self.oom_flags = None
                        self.prefix_length = None
                        self.receive_version = None
                        self.send_version = None
                        self.state = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global/Cisco-IOS-XR-ip-rip-oper:interface-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_address is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.neighbor_count is not None:
                            return True

                        if self.oom_flags is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.receive_version is not None:
                            return True

                        if self.send_version is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.Protocol.DefaultVrf.Global_.InterfaceSummary']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_summary is not None:
                        for child_ref in self.interface_summary:
                            if child_ref._has_data():
                                return True

                    if self.vrf_summary is not None and self.vrf_summary._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.Protocol.DefaultVrf.Global_']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol/Cisco-IOS-XR-ip-rip-oper:default-vrf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.configuration is not None and self.configuration._has_data():
                    return True

                if self.global_ is not None and self.global_._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.routes is not None and self.routes._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.Protocol.DefaultVrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:protocol'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.default_vrf is not None and self.default_vrf._has_data():
                return True

            if self.process is not None and self.process._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
            return meta._meta_table['Rip.Protocol']['meta_info']


    class DefaultVrf(object):
        """
        RIP operational data for Default VRF
        
        .. attribute:: configuration
        
        	RIP global configuration
        	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Configuration>`
        
        .. attribute:: global_
        
        	Global Information 
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_>`
        
        .. attribute:: interfaces
        
        	RIP interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: routes
        
        	RIP route database
        	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes>`
        
        .. attribute:: statistics
        
        	RIP statistics information
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Statistics>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.configuration = Rip.DefaultVrf.Configuration()
            self.configuration.parent = self
            self.global_ = Rip.DefaultVrf.Global_()
            self.global_.parent = self
            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self.routes = Rip.DefaultVrf.Routes()
            self.routes.parent = self
            self.statistics = Rip.DefaultVrf.Statistics()
            self.statistics.parent = self


        class Routes(object):
            """
            RIP route database
            
            .. attribute:: route
            
            	A route in the RIP database
            	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.route = YList()
                self.route.parent = self
                self.route.name = 'route'


            class Route(object):
                """
                A route in the RIP database
                
                .. attribute:: active
                
                	Active route indicator
                	**type**\:  bool
                
                .. attribute:: attributes
                
                	RIB supplied route attributes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bgp_count
                
                	Hop count for this route
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: destination_address
                
                	Destination IP Address for this route
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Route administrative distance
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: hold_down
                
                	Indicates whether route is in holddown
                	**type**\:  bool
                
                .. attribute:: path_origin
                
                	Where this route was learnt
                	**type**\:   :py:class:`RipRouteOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOriginEnum>`
                
                .. attribute:: paths
                
                	The paths for this route
                	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route.Paths>`
                
                .. attribute:: prefix
                
                	Network prefix
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..32
                
                .. attribute:: prefix_length_xr
                
                	Prefix length of IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_summary
                
                	Summary route placeholder indicator
                	**type**\:  bool
                
                .. attribute:: route_tag
                
                	Generic route information
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: route_type
                
                	Type of this route
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: version
                
                	RIB supplied version number
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.attributes = None
                    self.bgp_count = None
                    self.destination_address = None
                    self.distance = None
                    self.hold_down = None
                    self.path_origin = None
                    self.paths = YList()
                    self.paths.parent = self
                    self.paths.name = 'paths'
                    self.prefix = None
                    self.prefix_length = None
                    self.prefix_length_xr = None
                    self.route_summary = None
                    self.route_tag = None
                    self.route_type = None
                    self.version = None


                class Paths(object):
                    """
                    The paths for this route
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_permanent
                    
                    	Permanent indicator
                    	**type**\:  bool
                    
                    .. attribute:: metric
                    
                    	Metric
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: next_hop_address
                    
                    	Next hop address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tag
                    
                    	Tag
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: uptime
                    
                    	Up time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.is_permanent = None
                        self.metric = None
                        self.next_hop_address = None
                        self.source_address = None
                        self.tag = None
                        self.uptime = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes/Cisco-IOS-XR-ip-rip-oper:route/Cisco-IOS-XR-ip-rip-oper:paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.is_permanent is not None:
                            return True

                        if self.metric is not None:
                            return True

                        if self.next_hop_address is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.tag is not None:
                            return True

                        if self.uptime is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.DefaultVrf.Routes.Route.Paths']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes/Cisco-IOS-XR-ip-rip-oper:route'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.attributes is not None:
                        return True

                    if self.bgp_count is not None:
                        return True

                    if self.destination_address is not None:
                        return True

                    if self.distance is not None:
                        return True

                    if self.hold_down is not None:
                        return True

                    if self.path_origin is not None:
                        return True

                    if self.paths is not None:
                        for child_ref in self.paths:
                            if child_ref._has_data():
                                return True

                    if self.prefix is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    if self.prefix_length_xr is not None:
                        return True

                    if self.route_summary is not None:
                        return True

                    if self.route_tag is not None:
                        return True

                    if self.route_type is not None:
                        return True

                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.DefaultVrf.Routes.Route']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:routes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.route is not None:
                    for child_ref in self.route:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.DefaultVrf.Routes']['meta_info']


        class Configuration(object):
            """
            RIP global configuration
            
            .. attribute:: active
            
            	VRF active indicator
            	**type**\:  bool
            
            .. attribute:: auto_summarize
            
            	Auto\-summarization indicator
            	**type**\:  bool
            
            .. attribute:: default_metric
            
            	Default metric for RIP routes
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flash_threshold
            
            	Flash update threshold
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flush_timer
            
            	Flush timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hold_down_timer
            
            	Holddown timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: input_q_length
            
            	Length of the input queue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: invalid_timer
            
            	Invalid timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths a route can have
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: multicast_address
            
            	Use broadcast/multicast address indicator
            	**type**\:  bool
            
            .. attribute:: next_update_time
            
            	Time left for next update
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsf_life_time
            
            	NSF life time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsf_status
            
            	NSF Enable status
            	**type**\:  bool
            
            .. attribute:: oom_flags
            
            	Out\-of\-memory status flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rip_version
            
            	Version of RIP configured
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: triggered_rip
            
            	Triggered RIP enabled indicator
            	**type**\:  bool
            
            .. attribute:: update_timer
            
            	Update timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: validation_indicator
            
            	Incoming packet source validation indicator
            	**type**\:  bool
            
            .. attribute:: vr_fised_socket
            
            	VRF added to socket indicator
            	**type**\:  bool
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = None
                self.auto_summarize = None
                self.default_metric = None
                self.flash_threshold = None
                self.flush_timer = None
                self.hold_down_timer = None
                self.input_q_length = None
                self.invalid_timer = None
                self.maximum_paths = None
                self.multicast_address = None
                self.next_update_time = None
                self.nsf_life_time = None
                self.nsf_status = None
                self.oom_flags = None
                self.rip_version = None
                self.triggered_rip = None
                self.update_timer = None
                self.validation_indicator = None
                self.vr_fised_socket = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:configuration'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None:
                    return True

                if self.auto_summarize is not None:
                    return True

                if self.default_metric is not None:
                    return True

                if self.flash_threshold is not None:
                    return True

                if self.flush_timer is not None:
                    return True

                if self.hold_down_timer is not None:
                    return True

                if self.input_q_length is not None:
                    return True

                if self.invalid_timer is not None:
                    return True

                if self.maximum_paths is not None:
                    return True

                if self.multicast_address is not None:
                    return True

                if self.next_update_time is not None:
                    return True

                if self.nsf_life_time is not None:
                    return True

                if self.nsf_status is not None:
                    return True

                if self.oom_flags is not None:
                    return True

                if self.rip_version is not None:
                    return True

                if self.triggered_rip is not None:
                    return True

                if self.update_timer is not None:
                    return True

                if self.validation_indicator is not None:
                    return True

                if self.vr_fised_socket is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.DefaultVrf.Configuration']['meta_info']


        class Statistics(object):
            """
            RIP statistics information
            
            .. attribute:: discarded_packets
            
            	Total discarded packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: discarded_routes
            
            	Total discarded routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_malloc_failures
            
            	Number of failures to allocate memory for a path
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: periodic_updates
            
            	Number of periodic RIP updates
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: query_responses
            
            	Number of RIP queries responded to
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: received_packets
            
            	Total packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rib_updates
            
            	Number of route updates to RIB made by RIP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_malloc_failures
            
            	Number of failures to allocate memory for a route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_message_failures
            
            	Number of message send failures
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_messages
            
            	Number of messages sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: standby_packets_received
            
            	Packets rx in SRP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.discarded_packets = None
                self.discarded_routes = None
                self.path_count = None
                self.path_malloc_failures = None
                self.periodic_updates = None
                self.query_responses = None
                self.received_packets = None
                self.rib_updates = None
                self.route_count = None
                self.route_malloc_failures = None
                self.sent_message_failures = None
                self.sent_messages = None
                self.standby_packets_received = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.discarded_packets is not None:
                    return True

                if self.discarded_routes is not None:
                    return True

                if self.path_count is not None:
                    return True

                if self.path_malloc_failures is not None:
                    return True

                if self.periodic_updates is not None:
                    return True

                if self.query_responses is not None:
                    return True

                if self.received_packets is not None:
                    return True

                if self.rib_updates is not None:
                    return True

                if self.route_count is not None:
                    return True

                if self.route_malloc_failures is not None:
                    return True

                if self.sent_message_failures is not None:
                    return True

                if self.sent_messages is not None:
                    return True

                if self.standby_packets_received is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.DefaultVrf.Statistics']['meta_info']


        class Interfaces(object):
            """
            RIP interfaces
            
            .. attribute:: interface
            
            	Information about a particular RIP interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                Information about a particular RIP interface
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: accept_metric
                
                	Accept routes of metric 0 indicator
                	**type**\:  bool
                
                .. attribute:: auth_key_md5
                
                	Authentication key programmed with MD5 algorithm
                	**type**\:  bool
                
                .. attribute:: auth_key_send_id
                
                	Current active Send Authentication Key Id
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: auth_keychain
                
                	Authentication Keychain Name
                	**type**\:  str
                
                .. attribute:: auth_mode
                
                	Authentication Mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	IP Address of this interface
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: if_handle
                
                	Interface handle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	Interface name
                	**type**\:  str
                
                .. attribute:: is_passive_interface
                
                	Passive interface indicator
                	**type**\:  bool
                
                .. attribute:: join_status
                
                	Multicast group join status
                	**type**\:  bool
                
                .. attribute:: lpts_state
                
                	LPTSState
                	**type**\:  bool
                
                .. attribute:: metric_cost
                
                	Cost added to routes through this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: multicast_address
                
                	Use broadcast address for v2 packets
                	**type**\:  bool
                
                .. attribute:: neighbor_address
                
                	Interface's triggered RIP neighbor
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_accepted_valid_auth
                
                	Packets accepted with valid authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_invalid_auth
                
                	Packets dropped due to invalid authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_no_auth
                
                	Packets dropped due to missing authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_wrong_kc
                
                	Packets dropped due to wrong keychain configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: poison_horizon
                
                	Poisoned reverse enabled indicator
                	**type**\:  bool
                
                .. attribute:: prefix_length
                
                	Prefix length of the IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	Versions that the interface will recieve
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_enabled
                
                	Whether RIP is enabled on this interface
                	**type**\:  bool
                
                .. attribute:: rip_peer
                
                	Neighbors on this interface
                	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipPeer>`
                
                .. attribute:: rip_summary
                
                	User defined summary addresses
                	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipSummary>`
                
                .. attribute:: send_auth_key_exists
                
                	Authentication send key exists
                	**type**\:  bool
                
                .. attribute:: send_version
                
                	Versions that the interface is sending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: split_horizon
                
                	Split horizon enabled indicator
                	**type**\:  bool
                
                .. attribute:: state
                
                	Current state of the interface
                	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                
                .. attribute:: total_pkt_recvd
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.accept_metric = None
                    self.auth_key_md5 = None
                    self.auth_key_send_id = None
                    self.auth_keychain = None
                    self.auth_mode = None
                    self.destination_address = None
                    self.if_handle = None
                    self.interface = None
                    self.is_passive_interface = None
                    self.join_status = None
                    self.lpts_state = None
                    self.metric_cost = None
                    self.multicast_address = None
                    self.neighbor_address = None
                    self.oom_flags = None
                    self.pkt_accepted_valid_auth = None
                    self.pkt_drop_invalid_auth = None
                    self.pkt_drop_no_auth = None
                    self.pkt_drop_wrong_kc = None
                    self.poison_horizon = None
                    self.prefix_length = None
                    self.receive_version = None
                    self.rip_enabled = None
                    self.rip_peer = YList()
                    self.rip_peer.parent = self
                    self.rip_peer.name = 'rip_peer'
                    self.rip_summary = YList()
                    self.rip_summary.parent = self
                    self.rip_summary.name = 'rip_summary'
                    self.send_auth_key_exists = None
                    self.send_version = None
                    self.split_horizon = None
                    self.state = None
                    self.total_pkt_recvd = None
                    self.triggered_rip = None


                class RipSummary(object):
                    """
                    User defined summary addresses
                    
                    .. attribute:: metric
                    
                    	Summary metric
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: next_hop_address
                    
                    	Summary address next hop
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix
                    
                    	Summary address prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Summary address prefix length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.metric = None
                        self.next_hop_address = None
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.metric is not None:
                            return True

                        if self.next_hop_address is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.RipSummary']['meta_info']


                class RipPeer(object):
                    """
                    Neighbors on this interface
                    
                    .. attribute:: discarded_peer_packets
                    
                    	Discarded packets from this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discarded_peer_routes
                    
                    	Discarded routes from this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_address
                    
                    	IP Address of this peer
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_uptime
                    
                    	Uptime of this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_version
                    
                    	RIP version for this peer
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.discarded_peer_packets = None
                        self.discarded_peer_routes = None
                        self.peer_address = None
                        self.peer_uptime = None
                        self.peer_version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-oper:rip-peer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.discarded_peer_packets is not None:
                            return True

                        if self.discarded_peer_routes is not None:
                            return True

                        if self.peer_address is not None:
                            return True

                        if self.peer_uptime is not None:
                            return True

                        if self.peer_version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.RipPeer']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:interfaces/Cisco-IOS-XR-ip-rip-oper:interface[Cisco-IOS-XR-ip-rip-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.accept_metric is not None:
                        return True

                    if self.auth_key_md5 is not None:
                        return True

                    if self.auth_key_send_id is not None:
                        return True

                    if self.auth_keychain is not None:
                        return True

                    if self.auth_mode is not None:
                        return True

                    if self.destination_address is not None:
                        return True

                    if self.if_handle is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.is_passive_interface is not None:
                        return True

                    if self.join_status is not None:
                        return True

                    if self.lpts_state is not None:
                        return True

                    if self.metric_cost is not None:
                        return True

                    if self.multicast_address is not None:
                        return True

                    if self.neighbor_address is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.pkt_accepted_valid_auth is not None:
                        return True

                    if self.pkt_drop_invalid_auth is not None:
                        return True

                    if self.pkt_drop_no_auth is not None:
                        return True

                    if self.pkt_drop_wrong_kc is not None:
                        return True

                    if self.poison_horizon is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    if self.receive_version is not None:
                        return True

                    if self.rip_enabled is not None:
                        return True

                    if self.rip_peer is not None:
                        for child_ref in self.rip_peer:
                            if child_ref._has_data():
                                return True

                    if self.rip_summary is not None:
                        for child_ref in self.rip_summary:
                            if child_ref._has_data():
                                return True

                    if self.send_auth_key_exists is not None:
                        return True

                    if self.send_version is not None:
                        return True

                    if self.split_horizon is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.total_pkt_recvd is not None:
                        return True

                    if self.triggered_rip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.DefaultVrf.Interfaces']['meta_info']


        class Global_(object):
            """
            Global Information 
            
            .. attribute:: interface_summary
            
            	List of Interfaces configured
            	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.InterfaceSummary>`
            
            .. attribute:: vrf_summary
            
            	VRF summary data
            	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.VrfSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_summary = YList()
                self.interface_summary.parent = self
                self.interface_summary.name = 'interface_summary'
                self.vrf_summary = Rip.DefaultVrf.Global_.VrfSummary()
                self.vrf_summary.parent = self


            class VrfSummary(object):
                """
                VRF summary data
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\:  bool
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.active_interface_count = None
                    self.flush_timer = None
                    self.hold_down_timer = None
                    self.interface_configured_count = None
                    self.invalid_timer = None
                    self.next_update_time = None
                    self.oom_flags = None
                    self.path_count = None
                    self.route_count = None
                    self.update_timer = None
                    self.vrf_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global/Cisco-IOS-XR-ip-rip-oper:vrf-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.active_interface_count is not None:
                        return True

                    if self.flush_timer is not None:
                        return True

                    if self.hold_down_timer is not None:
                        return True

                    if self.interface_configured_count is not None:
                        return True

                    if self.invalid_timer is not None:
                        return True

                    if self.next_update_time is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.path_count is not None:
                        return True

                    if self.route_count is not None:
                        return True

                    if self.update_timer is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.DefaultVrf.Global_.VrfSummary']['meta_info']


            class InterfaceSummary(object):
                """
                List of Interfaces configured
                
                .. attribute:: destination_address
                
                	IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: enabled
                
                	RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  str
                
                .. attribute:: neighbor_count
                
                	Number of neighbors seen
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length of IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	RIP versions this interface will receive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: send_version
                
                	RIP versions this interface sends out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	Interface state
                	**type**\:   :py:class:`InterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceStateEnum>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.destination_address = None
                    self.enabled = None
                    self.interface_name = None
                    self.neighbor_count = None
                    self.oom_flags = None
                    self.prefix_length = None
                    self.receive_version = None
                    self.send_version = None
                    self.state = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global/Cisco-IOS-XR-ip-rip-oper:interface-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.destination_address is not None:
                        return True

                    if self.enabled is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.neighbor_count is not None:
                        return True

                    if self.oom_flags is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    if self.receive_version is not None:
                        return True

                    if self.send_version is not None:
                        return True

                    if self.state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                    return meta._meta_table['Rip.DefaultVrf.Global_.InterfaceSummary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf/Cisco-IOS-XR-ip-rip-oper:global'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_summary is not None:
                    for child_ref in self.interface_summary:
                        if child_ref._has_data():
                            return True

                if self.vrf_summary is not None and self.vrf_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
                return meta._meta_table['Rip.DefaultVrf.Global_']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rip-oper:rip/Cisco-IOS-XR-ip-rip-oper:default-vrf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.configuration is not None and self.configuration._has_data():
                return True

            if self.global_ is not None and self.global_._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.routes is not None and self.routes._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
            return meta._meta_table['Rip.DefaultVrf']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-rip-oper:rip'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.default_vrf is not None and self.default_vrf._has_data():
            return True

        if self.protocol is not None and self.protocol._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_oper as meta
        return meta._meta_table['Rip']['meta_info']


